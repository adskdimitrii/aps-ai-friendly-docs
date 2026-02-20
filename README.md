# APS ACC Friendly Docs

Lightweight, local Markdown mirror of Autodesk APS ACC documentation.

This repository contains:
- Crawled **How-to/Tutorial** docs from `https://aps.autodesk.com/en/docs/acc/v1/tutorials/getting-started/`
- Crawled **HTTP Reference** docs from `https://aps.autodesk.com/en/docs/acc/v1/reference/http/`
- URL index files for traceability back to source pages

## Repository Structure

- `acc/crawl_howto_docs.py` — crawler for ACC how-to/tutorial docs
- `acc/crawl_http_docs.py` — crawler for ACC HTTP reference docs
- `acc/how-to-docs/` — generated Markdown files for how-to pages
- `acc/http-docs/` — generated Markdown files for HTTP reference pages
- `acc/how-to-docs/_url_index.md` — list of source how-to URLs
- `acc/http-docs/_url_index.md` — list of source HTTP doc URLs

## Prerequisites

- Python 3.10+
- Internet access (scripts fetch live docs)

Install dependencies:

```bash
python -m pip install requests beautifulsoup4
```

## Usage

From the repository root:

### Refresh how-to docs

```bash
python acc/crawl_howto_docs.py
```

### Refresh HTTP reference docs

```bash
python acc/crawl_http_docs.py
```

## Output Format

Each generated Markdown file includes:
- Page title
- Original APS source URL
- Extracted page content (headings, paragraphs, lists, code blocks, tables-as-text)

## Notes

- Generated filenames are slugified from APS URL paths.
- If two pages would produce the same filename, the crawler falls back to a full-path slug.
- Some pages may be skipped if source fetch/parsing fails; the scripts print warnings and a final summary.

## Source

Autodesk APS ACC docs:
- https://aps.autodesk.com/en/docs/acc/v1/tutorials/getting-started/
- https://aps.autodesk.com/en/docs/acc/v1/reference/http/
