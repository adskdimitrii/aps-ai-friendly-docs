#!/usr/bin/env python3
"""Image tag remover for APS AI-friendly docs.

Scans all markdown files for image tags (![alt](url)) and removes them,
since all image links are broken in the local docs.

Usage:
    python fix_images.py              # preview changes (dry run)
    python fix_images.py --write      # apply changes to files
"""
import argparse
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Regex for markdown image tags: ![alt](url)
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


def process_file(md_file: Path, write: bool) -> int:
    """Process a single markdown file, removing all image tags.

    Returns the number of image tags removed.
    """
    try:
        original = md_file.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return 0

    matches = IMAGE_RE.findall(original)
    if not matches:
        return 0

    result = IMAGE_RE.sub("", original)

    rel_path = md_file.relative_to(REPO_ROOT)
    print(f"\n{rel_path} ({len(matches)} image(s) removed):")
    for alt, url in matches:
        print(f"  REMOVED: ![{alt}]({url})")

    if write and result != original:
        md_file.write_text(result, encoding="utf-8")

    return len(matches)


def main():
    parser = argparse.ArgumentParser(
        description="Remove broken image tags from APS markdown docs."
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Apply changes to files (default is dry-run preview).",
    )
    args = parser.parse_args()

    md_files = sorted(REPO_ROOT.rglob("*.md"))
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

    total_removed = 0
    for md_file in md_files:
        total_removed += process_file(md_file, write=args.write)

    print(f"\n{'=' * 60}")
    print(f"Summary:")
    print(f"  Image tags removed: {total_removed}")
    if not args.write and total_removed > 0:
        print(f"\nThis was a dry run. Use --write to apply changes.")


if __name__ == "__main__":
    main()
