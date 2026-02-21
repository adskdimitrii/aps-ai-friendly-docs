# APS Design Automation Friendly Docs

Lightweight, local Markdown mirror of Autodesk APS Design Automation documentation.

This folder contains:
- Crawled **How-to/Tutorial** docs from `https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/`
- Crawled **HTTP Reference** docs from `https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/`
- URL index files for traceability back to source pages

## Structure

- `crawl_howto_docs.py` — crawler for Design Automation how-to/tutorial docs
- `crawl_http_docs.py` — crawler for Design Automation HTTP reference docs
- `how-to-docs/` — generated Markdown files for Design Automation how-to/tutorial pages
- `http-docs/` — generated Markdown files for Design Automation HTTP reference pages
- `how-to-docs/_url_index.md` — list of source Design Automation how-to/tutorial URLs
- `http-docs/_url_index.md` — list of source Design Automation HTTP doc URLs

## Usage

From the repository root:

### Refresh Design Automation how-to docs

```bash
python design-automation/crawl_howto_docs.py
```

### Refresh Design Automation HTTP reference docs

```bash
python design-automation/crawl_http_docs.py
```

## Source

Autodesk APS Design Automation docs:
- https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/
- https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/
