#!/usr/bin/env python3
import re
from pathlib import Path
from collections import deque

import requests
from bs4 import BeautifulSoup

ROOT_URL = "https://aps.autodesk.com/en/docs/webhooks/v1/reference/http/"
CUSTOM_JS_URL = "https://aps.autodesk.com/params/custom.js"
CONFIG_FILENAME = "webhooks_v1.json"
OUTPUT_DIR = Path(__file__).resolve().parent / "http-docs"
TIMEOUT = 30


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


def collect_http_leaf_nodes(config: dict) -> list[dict]:
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
        if full_path.startswith("webhooks/reference/http/") and source:
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


def extract_main_markdown(html: str, doc_url: str, display_name: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    title_tag = soup.find("h1") or soup.find("title")
    title = title_tag.get_text(" ", strip=True) if title_tag else (display_name or doc_url)

    container = soup.find("main") or soup.find("article") or soup.body or soup

    lines = []
    for element in container.find_all(["h1", "h2", "h3", "h4", "p", "li", "pre", "table"]):
        text = element.get_text(" ", strip=True)
        if not text:
            continue
        name = element.name
        if name == "h1":
            lines.append(f"# {text}")
        elif name == "h2":
            lines.append(f"## {text}")
        elif name == "h3":
            lines.append(f"### {text}")
        elif name == "h4":
            lines.append(f"#### {text}")
        elif name == "li":
            lines.append(f"- {text}")
        elif name == "pre":
            lines.append(f"```\n{text}\n```")
        else:
            lines.append(text)

    body = "\n\n".join(lines)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()

    return f"# {title}\n\nSource: {doc_url}\n\n---\n\n{body}\n"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    config_base, docs_base = get_doc_bases()
    config_url = config_base + CONFIG_FILENAME
    config = requests.get(config_url, timeout=TIMEOUT)
    config.raise_for_status()
    leaf_nodes = collect_http_leaf_nodes(config.json())

    url_list_file = OUTPUT_DIR / "_url_index.md"
    index_lines = ["# Webhooks HTTP API Doc URLs", "", f"Config source: {config_url}", ""]
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

        slug = slug_from_path(node["url_path"])
        out_file = OUTPUT_DIR / f"{slug}.md"

        if out_file.name in seen_filenames:
            alt_slug = slug_from_path(node["full_path"])
            out_file = OUTPUT_DIR / f"{alt_slug}.md"

        seen_filenames.add(out_file.name)

        out_file.write_text(markdown, encoding="utf-8")
        written += 1
        print(f"[OK] {out_file.name}")

    print(f"Completed. HTTP pages found: {len(leaf_nodes)}, files written: {written}, skipped: {skipped}")


if __name__ == "__main__":
    main()
