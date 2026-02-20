# APS OAuth Friendly Docs

Lightweight, local Markdown mirror of Autodesk APS OAuth documentation.

This folder contains:
- Crawled **How-to/Tutorial** docs from `https://aps.autodesk.com/en/docs/oauth/v2/tutorials/create-app/`
- Crawled **Developer's Guide** docs from `https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/overview/`
- Crawled **HTTP Reference** docs from `https://aps.autodesk.com/en/docs/oauth/v2/reference/http/`
- URL index files for traceability back to source pages

## Structure

- `crawl_developers_guide_docs.py` — crawler for OAuth Developer's Guide docs
- `crawl_howto_docs.py` — crawler for OAuth how-to/tutorial docs
- `crawl_http_docs.py` — crawler for OAuth HTTP reference docs
- `how-to-docs/` — generated Markdown files for OAuth how-to/tutorial pages
- `developers-guide-docs/` — generated Markdown files for OAuth Developer's Guide pages
- `http-docs/` — generated Markdown files for OAuth HTTP reference pages
- `how-to-docs/_url_index.md` — list of source OAuth how-to/tutorial URLs
- `developers-guide-docs/_url_index.md` — list of source OAuth Developer's Guide URLs
- `http-docs/_url_index.md` — list of source OAuth HTTP doc URLs

## Usage

From the repository root:

### Refresh OAuth Developer's Guide docs

```bash
python oauth/crawl_developers_guide_docs.py
```

### Refresh OAuth how-to docs

```bash
python oauth/crawl_howto_docs.py
```

### Refresh OAuth HTTP reference docs

```bash
python oauth/crawl_http_docs.py
```

## Source

Autodesk APS OAuth docs:
- https://aps.autodesk.com/en/docs/oauth/v2/tutorials/create-app/
- https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/overview/
- https://aps.autodesk.com/en/docs/oauth/v2/reference/http/
