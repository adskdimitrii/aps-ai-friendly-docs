# APS Webhooks Friendly Docs

Lightweight, local Markdown mirror of Autodesk APS Webhooks documentation.

This folder contains:
- Crawled **How-to/Tutorial** docs from `https://aps.autodesk.com/en/docs/webhooks/v1/tutorials/`
- Crawled **HTTP Reference** docs from `https://aps.autodesk.com/en/docs/webhooks/v1/reference/http/`
- URL index files for traceability back to source pages

## Structure

- `crawl_howto_docs.py` — crawler for Webhooks how-to/tutorial docs
- `crawl_http_docs.py` — crawler for Webhooks HTTP reference docs
- `how-to-docs/` — generated Markdown files for Webhooks how-to/tutorial pages
- `http-docs/` — generated Markdown files for Webhooks HTTP reference pages
- `how-to-docs/_url_index.md` — list of source Webhooks how-to/tutorial URLs
- `http-docs/_url_index.md` — list of source Webhooks HTTP doc URLs

## Usage

From the repository root:

### Refresh Webhooks how-to docs

```bash
python webhooks/crawl_howto_docs.py
```

### Refresh Webhooks HTTP reference docs

```bash
python webhooks/crawl_http_docs.py
```

## Source

Autodesk APS Webhooks docs:
- https://aps.autodesk.com/en/docs/webhooks/v1/tutorials/
- https://aps.autodesk.com/en/docs/webhooks/v1/reference/http/
