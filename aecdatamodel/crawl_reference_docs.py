#!/usr/bin/env python3
"""Crawl all AEC Data Model reference docs: graphqlendpoint, queries, objects, inputs, scalars."""
import re
from collections import deque
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from html_to_markdown import ConversionOptions, convert

ROOT_URL = "https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/"
CUSTOM_JS_URL = "https://aps.autodesk.com/params/custom.js"
CONFIG_FILENAME = "aecdatamodel_v1.json"
OUTPUT_DIR = Path(__file__).resolve().parent / "reference-docs"
TIMEOUT = 30

REFERENCE_PREFIXES = (
    "aecdatamodel/reference/graphqlendpoint",
    "aecdatamodel/reference/queries/",
    "aecdatamodel/reference/objects/",
    "aecdatamodel/reference/inputs/",
    "aecdatamodel/reference/scalars",
)


def get_doc_bases() -> tuple[str, str]:
    response = requests.get(CUSTOM_JS_URL, timeout=TIMEOUT)
    response.raise_for_status()

    conf_match = re.search(r"conf:\s*'([^']+)'", response.text)
    ext_match = re.search(r"ext:\s*'([^']+)'", response.text)
    if not conf_match or not ext_match:
        raise RuntimeError("Could not resolve docs base URLs from custom.js")

    conf_base = conf_match.group(1)
    ext_base = ext_match.group(1)

    if not conf_base.endswith("/"):
        conf_base += "/"
    if not ext_base.endswith("/"):
        ext_base += "/"

    return conf_base, ext_base


def collect_reference_leaf_nodes(config: dict) -> list[dict]:
    queue = deque([(config, "")])
    leaves: list[dict] = []

    while queue:
        node, path = queue.popleft()
        url_path = node.get("url_path", "")
        full_path = (path + "/" + url_path).strip("/") if path or url_path else ""

        children = node.get("children") or []
        if children:
            for child in children:
                queue.append((child, full_path))
            continue

        source = node.get("source")
        if source and any(full_path.startswith(p) for p in REFERENCE_PREFIXES):
            leaves.append(
                {
                    "full_path": full_path,
                    "url_path": url_path,
                    "display_name": node.get("display_name", ""),
                    "source": source,
                }
            )

    leaves.sort(key=lambda x: x["full_path"])
    return leaves


def slug_from_path(path_value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "-", path_value).strip("-")
    return slug or "index"


def output_slug_from_full_path(full_path: str) -> str:
    # aecdatamodel/reference/queries/hubs -> queries-hubs
    # aecdatamodel/reference/scalars -> scalars
    parts = full_path.split("/", 2)
    relative_path = parts[2] if len(parts) == 3 else full_path
    return slug_from_path(relative_path)


def extract_main_markdown(html: str, doc_url: str, display_name: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    title_tag = soup.find("h1") or soup.find("title")
    title = title_tag.get_text(" ", strip=True) if title_tag else (display_name or doc_url)

    container = soup.find("main") or soup.find("article") or soup.body or soup

    options = ConversionOptions(
        heading_style="atx",
        list_indent_width=2,
    )
    body = convert(str(container), options)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()

    return f"# {title}\n\nSource: {doc_url}\n\n---\n\n{body}\n"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for existing_markdown in OUTPUT_DIR.glob("*.md"):
        existing_markdown.unlink()

    config_base, docs_base = get_doc_bases()
    config_url = config_base + CONFIG_FILENAME
    config = requests.get(config_url, timeout=TIMEOUT)
    config.raise_for_status()
    leaf_nodes = collect_reference_leaf_nodes(config.json())

    url_list_file = OUTPUT_DIR / "_url_index.md"
    index_lines = [
        "# AEC Data Model Reference Doc URLs",
        "",
        f"Root page: {ROOT_URL}",
        f"Config source: {config_url}",
        "",
    ]
    index_lines.extend(
        f"- https://aps.autodesk.com/en/docs/{node['full_path']}/" for node in leaf_nodes
    )
    url_list_file.write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    written = 0
    skipped = 0
    seen_filenames: set[str] = set()

    for node in leaf_nodes:
        doc_url = f"https://aps.autodesk.com/en/docs/{node['full_path']}/"
        source_url = docs_base + node["source"]
        try:
            page = requests.get(source_url, timeout=TIMEOUT)
            page.raise_for_status()
            markdown = extract_main_markdown(page.text, doc_url, node["display_name"])
        except Exception as exc:
            print(f"[WARN] Failed: {doc_url} ({source_url}) -> {exc}")
            skipped += 1
            continue

        slug = output_slug_from_full_path(node["full_path"])
        out_file = OUTPUT_DIR / f"{slug}.md"

        if out_file.name in seen_filenames:
            alt_slug = slug_from_path(node["full_path"])
            out_file = OUTPUT_DIR / f"{alt_slug}.md"

        seen_filenames.add(out_file.name)

        out_file.write_text(markdown, encoding="utf-8")
        written += 1
        print(f"[OK] {out_file.name}")

    print(f"Completed. Reference pages found: {len(leaf_nodes)}, files written: {written}, skipped: {skipped}")


if __name__ == "__main__":
    main()
