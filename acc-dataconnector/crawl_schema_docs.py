#!/usr/bin/env python3
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse, parse_qs

import requests
from bs4 import BeautifulSoup, Tag
from html_to_markdown import ConversionOptions, convert

BASE_URL = "https://developer.api.autodesk.com"
INDEX_URL = f"{BASE_URL}/data-connector/v1/doc"
OUTPUT_DIR = Path(__file__).resolve().parent / "schema-docs"
TIMEOUT = 30


def table_to_markdown(table: Tag) -> str:
    """Convert an HTML table to a markdown table, handling malformed colgroup placement."""
    rows = [tr for tr in table.find_all("tr") if tr.find_parent("table") is table]
    if not rows:
        return ""

    md_rows = []
    for row in rows:
        cells = row.find_all(["th", "td"])
        cell_texts = [" ".join(c.get_text(" ", strip=True).split()) for c in cells]
        md_rows.append("| " + " | ".join(cell_texts) + " |")

    if not md_rows:
        return ""

    # Insert separator after header row
    first_cells = rows[0].find_all(["th", "td"])
    separator = "| " + " | ".join(["---"] * len(first_cells)) + " |"
    md_rows.insert(1, separator)

    return "\n".join(md_rows)


def get_html_schema_links(index_html: str) -> list[dict]:
    soup = BeautifulSoup(index_html, "html.parser")
    entries = []
    seen_names: set[str] = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]
        full_url = urljoin(BASE_URL, href)
        parsed = urlparse(full_url)
        qs = parse_qs(parsed.query)

        # Schema pages: /data-connector/v1/doc/schema?name=...&format=html
        if parsed.path.endswith("/schema") and qs.get("format") == ["html"]:
            name = qs.get("name", [""])[0]
            if name and name not in seen_names:
                seen_names.add(name)
                entries.append({"name": name, "url": full_url, "type": "schema"})

        # Changes page: /data-connector/v1/doc/changes?format=html
        elif parsed.path.endswith("/changes") and qs.get("format") == ["html"]:
            if "changes" not in seen_names:
                seen_names.add("changes")
                entries.append({"name": "changes", "url": full_url, "type": "changes"})

    return entries


def extract_main_markdown(html: str, doc_url: str, name: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    title_tag = soup.find("h1") or soup.find("title")
    title = title_tag.get_text(" ", strip=True) if title_tag else name

    container = soup.find("main") or soup.find("article") or soup.body or soup

    # Replace tables with markdown before converting the rest, since html_to_markdown
    # fails on malformed tables (colgroup inside tbody).
    for table in container.find_all("table"):
        md_table = table_to_markdown(table)
        placeholder = soup.new_tag("pre")
        placeholder.string = f"\n{md_table}\n"
        table.replace_with(placeholder)

    options = ConversionOptions(
        heading_style="atx",
        list_indent_width=2,
    )
    body = convert(str(container), options)
    # Unescape the pre blocks back to plain markdown tables
    body = re.sub(r"```\n(\|.*?)\n```", r"\1", body, flags=re.DOTALL)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()

    return f"# {title}\n\nSource: {doc_url}\n\n---\n\n{body}\n"


def slug_from_name(name: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "-", name).strip("-")
    return slug or "index"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for existing_markdown in OUTPUT_DIR.glob("*.md"):
        existing_markdown.unlink()

    # Fetch and save the index page
    index_response = requests.get(INDEX_URL, timeout=TIMEOUT)
    index_response.raise_for_status()
    index_markdown = extract_main_markdown(index_response.text, INDEX_URL, "Data Connector Schema Index")
    (OUTPUT_DIR / "_index.md").write_text(index_markdown, encoding="utf-8")
    print("[OK] _index.md")

    entries = get_html_schema_links(index_response.text)

    url_index_file = OUTPUT_DIR / "_url_index.md"
    index_lines = [
        "# ACC Data Connector Schema Doc URLs",
        "",
        f"Index page: {INDEX_URL}",
        "",
    ]
    index_lines.extend(f"- {entry['url']}" for entry in entries)
    url_index_file.write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    written = 0
    skipped = 0

    for entry in entries:
        try:
            page = requests.get(entry["url"], timeout=TIMEOUT)
            page.raise_for_status()
            markdown = extract_main_markdown(page.text, entry["url"], entry["name"])
        except Exception as exc:
            print(f"[WARN] Failed: {entry['url']} -> {exc}")
            skipped += 1
            continue

        slug = slug_from_name(entry["name"])
        out_file = OUTPUT_DIR / f"{slug}.md"
        out_file.write_text(markdown, encoding="utf-8")
        written += 1
        print(f"[OK] {out_file.name}")

    print(f"Completed. Schema pages found: {len(entries)}, files written: {written}, skipped: {skipped}")


if __name__ == "__main__":
    main()
