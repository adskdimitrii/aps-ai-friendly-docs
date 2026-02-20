# APS ACC Friendly Docs

Lightweight, local Markdown mirror of Autodesk APS ACC documentation.

This folder contains:
- Crawled **How-to/Tutorial** docs from `https://aps.autodesk.com/en/docs/acc/v1/tutorials/getting-started/`
- Crawled **HTTP Reference** docs from `https://aps.autodesk.com/en/docs/acc/v1/reference/http/`
- URL index files for traceability back to source pages

## Structure

- `crawl_howto_docs.py` — crawler for ACC how-to/tutorial docs
- `crawl_http_docs.py` — crawler for ACC HTTP reference docs
- `how-to-docs/` — generated Markdown files for how-to pages
- `http-docs/` — generated Markdown files for HTTP reference pages
- `how-to-docs/_url_index.md` — list of source how-to URLs
- `http-docs/_url_index.md` — list of source HTTP doc URLs

## Usage

From the repository root:

### Refresh ACC how-to docs

```bash
python acc/crawl_howto_docs.py
```

### Refresh ACC HTTP reference docs

```bash
python acc/crawl_http_docs.py
```

## Source

Autodesk APS ACC docs:
- https://aps.autodesk.com/en/docs/acc/v1/tutorials/getting-started/
- https://aps.autodesk.com/en/docs/acc/v1/reference/http/