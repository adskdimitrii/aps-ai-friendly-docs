# APS Data Friendly Docs

Lightweight, local Markdown mirror of Autodesk APS Data documentation.

This folder contains:
- Crawled **How-to/Tutorial** docs from `https://aps.autodesk.com/en/docs/data/v2/tutorials/`
- Crawled **HTTP Reference** docs from `https://aps.autodesk.com/en/docs/data/v2/reference/http/`
- URL index files for traceability back to source pages

## Structure

- `crawl_howto_docs.py` — crawler for Data how-to/tutorial docs
- `crawl_http_docs.py` — crawler for Data HTTP reference docs
- `how-to-docs/` — generated Markdown files for Data how-to/tutorial pages
- `http-docs/` — generated Markdown files for Data HTTP reference pages
- `how-to-docs/_url_index.md` — list of source Data how-to/tutorial URLs
- `http-docs/_url_index.md` — list of source Data HTTP doc URLs

## Usage

From the repository root:

### Refresh Data how-to docs

```bash
python data/crawl_howto_docs.py
```

### Refresh Data HTTP reference docs

```bash
python data/crawl_http_docs.py
```

## Source

Autodesk APS Data docs:
- https://aps.autodesk.com/en/docs/data/v2/tutorials/
- https://aps.autodesk.com/en/docs/data/v2/reference/http/
