#!/usr/bin/env python3
"""Link mapper for APS AI-friendly docs.

Scans all markdown files for links. When a link points to a path that doesn't
resolve locally (e.g. /en/docs/...), the script tries to map it to a local
markdown file. If no local file is found, the link is rewritten to point to
the full HTTP address on aps.autodesk.com.

Usage:
    python fix_links.py              # preview changes (dry run)
    python fix_links.py --write      # apply changes to files
"""
import argparse
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
APS_BASE = "https://aps.autodesk.com"

# Regex for markdown links: [text](url) — but not images ![alt](url)
LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)")


# ------------------------------------------------------------------
# 1. Build URL → local file index
# ------------------------------------------------------------------

def build_url_index() -> dict[str, Path]:
    """Build a mapping from URL paths to local markdown files.

    Sources:
      - The ``Source:`` line in every .md file gives the canonical URL.
      - The ``_url_index.md`` files list all known URLs per directory.

    Returns a dict keyed by the path portion of the URL (e.g.
    ``/en/docs/oauth/v2/reference/http/gettoken-POST/``), with values
    being the absolute Path to the local .md file.
    """
    index: dict[str, Path] = {}

    # Pass 1: Source: lines in every markdown file
    for md_file in REPO_ROOT.rglob("*.md"):
        if md_file.name == "_url_index.md":
            continue
        try:
            with open(md_file, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("Source:"):
                        url = line[len("Source:"):].strip()
                        path_key = _url_to_path_key(url)
                        if path_key:
                            index[path_key] = md_file
                        break
                    # Source line is typically in the first 5 lines
                    if line.startswith("---"):
                        break
        except (OSError, UnicodeDecodeError):
            continue

    # Pass 2: _url_index.md files — associate each listed URL with a local
    # file in the same directory by deriving the filename the same way the
    # crawl scripts do.
    for idx_file in REPO_ROOT.rglob("_url_index.md"):
        idx_dir = idx_file.parent
        try:
            text = idx_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for line in text.splitlines():
            line = line.strip()
            if not line.startswith("- http"):
                continue
            url = line.lstrip("- ").strip().rstrip("/")
            path_key = _url_to_path_key(url)
            if not path_key:
                continue
            if path_key in index:
                continue  # Source: line takes precedence
            # Try to find the local file by matching the existing files in
            # the directory — the crawl scripts use slug_from_path which we
            # replicate here.
            candidate = _find_local_file_for_url(url, idx_dir)
            if candidate:
                index[path_key] = candidate

    return index


def _url_to_path_key(url: str) -> str | None:
    """Normalise a URL to its path key for indexing.

    Strips scheme+host, lowercases, strips trailing slashes.
    Returns None for URLs we can't handle.
    """
    # Handle full URLs
    for prefix in ("https://aps.autodesk.com", "http://aps.autodesk.com"):
        if url.startswith(prefix):
            url = url[len(prefix):]
            break
    # Handle developer.api URLs (acc-dataconnector) — skip, not /en/docs/ paths
    if not url.startswith("/en/docs/"):
        return None
    return url.rstrip("/")


def _slug_from_path(path_value: str) -> str:
    """Replicate the crawl script's slug_from_path."""
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "-", path_value).strip("-")
    return slug or "index"


def _find_local_file_for_url(url: str, directory: Path) -> Path | None:
    """Try to find a local .md file for a _url_index.md entry."""
    # Extract the path after /en/docs/ and derive the slug
    path_key = _url_to_path_key(url)
    if not path_key:
        return None

    # The crawl scripts use output_slug_from_full_path which takes the
    # portion after the first two path segments of the full_path.
    # full_path in _url_index is like: acc/reference/http/some-endpoint-GET
    # The /en/docs/ prefix was stripped, so path_key is like:
    # /en/docs/acc/v1/reference/http/some-endpoint-GET
    segments = path_key.lstrip("/").split("/")
    # segments: [en, docs, acc, v1, reference, http, some-endpoint-GET]
    # The crawl scripts build full_path as: acc/reference/http/some-endpoint-GET
    # (without version). The slug derivation takes parts after the first 2
    # segments of full_path ([acc, reference]), i.e. [http, some-endpoint-GET],
    # which maps to segments[5:] here (en/docs/acc/v1/reference → skip 5).

    if len(segments) > 5:
        relative = "/".join(segments[5:])
    else:
        relative = segments[-1] if segments else ""

    slug = _slug_from_path(relative)

    # Determine the correct filename prefix based on directory name
    dir_name = directory.name
    if dir_name == "http-docs":
        # HTTP docs use "http-" prefix
        candidate_names = [f"http-{slug}.md", f"{slug}.md"]
    else:
        candidate_names = [f"{slug}.md"]

    # Also try the full path slug as fallback
    full_slug = _slug_from_path("/".join(segments[2:]))
    candidate_names.append(f"{full_slug}.md")

    for name in candidate_names:
        candidate = directory / name
        if candidate.is_file():
            return candidate

    return None


# ------------------------------------------------------------------
# 2. Scan and fix links
# ------------------------------------------------------------------

def process_file(md_file: Path, url_index: dict[str, Path], write: bool) -> dict:
    """Process a single markdown file, resolving/fixing links.

    Returns a stats dict: {resolved: int, rewritten_to_http: int, already_ok: int}
    """
    try:
        original = md_file.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {"resolved": 0, "rewritten_to_http": 0, "already_ok": 0}

    stats = {"resolved": 0, "rewritten_to_http": 0, "already_ok": 0}
    changes: list[str] = []

    def replace_link(match: re.Match) -> str:
        text = match.group(1)
        href = match.group(2)

        # Rewrite /myapp* links (e.g. /myapps) to full APS URLs
        if href.startswith("/myapp"):
            full_url = APS_BASE + href
            new_link = f"[{text}]({full_url})"
            if new_link != match.group(0):
                stats["rewritten_to_http"] += 1
                changes.append(f"  HTTP:  {href} -> {full_url}")
                return new_link
            else:
                stats["already_ok"] += 1
                return match.group(0)

        # Normalise en/docs/ links that are missing the leading slash
        if href.startswith("en/docs/"):
            href = "/" + href

        # Only process /en/docs/ links
        if not href.startswith("/en/docs/"):
            stats["already_ok"] += 1
            return match.group(0)

        # Strip fragment and normalise
        fragment = ""
        if "#" in href:
            href_base, fragment = href.rsplit("#", 1)
            fragment = "#" + fragment
        else:
            href_base = href

        path_key = href_base.rstrip("/")

        # Try exact match
        local_file = url_index.get(path_key)

        # Try fuzzy match: strip trailing slash variations
        if not local_file:
            local_file = url_index.get(path_key.rstrip("/"))

        # Try matching against the tail segment (endpoint name)
        if not local_file:
            local_file = _fuzzy_search(path_key, url_index)

        if local_file and local_file.is_file():
            # Build relative path from md_file's directory to the target
            try:
                rel = _relative_path(md_file, local_file)
                new_link = f"[{text}]({rel}{fragment})"
                if new_link != match.group(0):
                    stats["resolved"] += 1
                    changes.append(f"  LOCAL: {href} -> {rel}")
                    return new_link
                else:
                    stats["already_ok"] += 1
                    return match.group(0)
            except ValueError:
                pass

        # Cannot resolve locally — rewrite to full HTTP URL
        full_url = APS_BASE + href_base.rstrip("/") + "/" + fragment
        # Clean up double-fragment if any
        full_url = full_url.rstrip("/") + ("/" if not fragment else "")
        if fragment:
            full_url = APS_BASE + href_base.rstrip("/") + "/" + fragment
        else:
            full_url = APS_BASE + href_base.rstrip("/") + "/"
        new_link = f"[{text}]({full_url})"
        stats["rewritten_to_http"] += 1
        changes.append(f"  HTTP:  {href} -> {full_url}")
        return new_link

    result = LINK_RE.sub(replace_link, original)

    if changes:
        rel_path = md_file.relative_to(REPO_ROOT)
        print(f"\n{rel_path} ({len(changes)} link(s) changed):")
        for c in changes:
            print(c)
        if write and result != original:
            md_file.write_text(result, encoding="utf-8")

    return stats


def _relative_path(from_file: Path, to_file: Path) -> str:
    """Compute a relative path from from_file's directory to to_file."""
    from_dir = from_file.parent
    try:
        rel = to_file.relative_to(from_dir)
        return str(rel)
    except ValueError:
        pass

    # Walk up until we find a common ancestor
    rel = Path()
    ancestor = from_dir
    while True:
        try:
            target_rel = to_file.relative_to(ancestor)
            return str(rel / target_rel)
        except ValueError:
            rel = rel / ".."
            ancestor = ancestor.parent
            if ancestor == ancestor.parent:
                raise ValueError("No common ancestor")


def _fuzzy_search(path_key: str, url_index: dict[str, Path]) -> Path | None:
    """Try to find a matching file by progressively relaxing the match.

    Strategy:
      1. Try stripping the version segment (e.g. /v1/ or /v2/) from path_key
         and from index keys, then compare.
      2. Try bim360/bim360-private -> acc domain alias, with version stripped.
      3. Try matching on the category + endpoint tail (last 2 segments),
         but only when the domain also matches or is a known alias.
    """
    segments = path_key.strip("/").split("/")
    # segments like: [en, docs, acc, v1, reference, http, some-endpoint-GET]

    # Strategy 1: remove version segment and match
    key_no_version = _strip_version(path_key)
    for idx_key, idx_file in url_index.items():
        if _strip_version(idx_key) == key_no_version:
            return idx_file

    # Strategy 2: bim360 / bim360-private -> acc alias
    if len(segments) >= 3 and segments[2] in ("bim360", "bim360-private"):
        alt_key = path_key.replace(f"/{segments[2]}/", "/acc/", 1)
        alt_no_version = _strip_version(alt_key)
        for idx_key, idx_file in url_index.items():
            if _strip_version(idx_key) == alt_no_version:
                return idx_file

    # Strategy 3: match on tail (last 2 segments) but require the domain
    # (segments[2]) to match or be a known alias
    if len(segments) >= 4:
        domain = segments[2]
        domain_aliases = {domain}
        if domain in ("bim360", "bim360-private"):
            domain_aliases.add("acc")
        elif domain == "acc":
            domain_aliases.update(("bim360", "bim360-private"))

        tail = "/".join(segments[-2:])
        for idx_key, idx_file in url_index.items():
            idx_segments = idx_key.strip("/").split("/")
            if (
                len(idx_segments) >= 4
                and idx_segments[2] in domain_aliases
                and len(idx_segments) >= 2
                and "/".join(idx_segments[-2:]) == tail
            ):
                return idx_file

    return None


def _strip_version(path: str) -> str:
    """Remove version segments like /v1/ or /v2/ from a path."""
    return re.sub(r"/v\d+/", "/", path)


# ------------------------------------------------------------------
# 3. Main
# ------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Resolve and fix links in APS markdown docs."
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Apply changes to files (default is dry-run preview).",
    )
    args = parser.parse_args()

    print("Building URL index...")
    url_index = build_url_index()
    print(f"Indexed {len(url_index)} URL-to-file mappings.\n")

    totals = {"resolved": 0, "rewritten_to_http": 0, "already_ok": 0}

    md_files = sorted(REPO_ROOT.rglob("*.md"))
    # Skip _url_index.md and README files (those already use correct relative links)
    md_files = [
        f
        for f in md_files
        if f.name != "_url_index.md"
        and f.name != "README.md"
        and f.name != "AGENTS.md"
        and f.name != "CLAUDE.md"
        and f.name != "CRAWL.md"
        and f.name != "HUMANS.md"
    ]

    for md_file in md_files:
        stats = process_file(md_file, url_index, write=args.write)
        for k in totals:
            totals[k] += stats[k]

    print(f"\n{'=' * 60}")
    print(f"Summary:")
    print(f"  Links resolved to local files : {totals['resolved']}")
    print(f"  Links rewritten to HTTP URLs  : {totals['rewritten_to_http']}")
    print(f"  Links already OK (skipped)    : {totals['already_ok']}")
    if not args.write and (totals["resolved"] + totals["rewritten_to_http"]) > 0:
        print(f"\nThis was a dry run. Use --write to apply changes.")


if __name__ == "__main__":
    main()
