# APS Viewer Friendly Docs

Lightweight, local Markdown mirror of Autodesk APS Viewer v7 documentation.

This folder contains:
- Crawled **Developer's Guide** docs from `https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/`
- Crawled **Reference** docs from `https://aps.autodesk.com/en/docs/viewer/v7/reference/`
- URL index files for traceability back to source pages

## Structure

- `crawl_developers_guide_docs.py` — crawler for Viewer v7 Developer's Guide docs
- `crawl_reference_docs.py` — crawler for Viewer v7 Reference docs
- `developers-guide-docs/` — generated Markdown files for Viewer v7 Developer's Guide pages
- `reference-docs/` — generated Markdown files for Viewer v7 Reference pages
- `developers-guide-docs/_url_index.md` — list of source Viewer v7 Developer's Guide URLs
- `reference-docs/_url_index.md` — list of source Viewer v7 Reference URLs

## Usage

From the repository root:

### Refresh Viewer v7 Developer's Guide docs

```bash
python viewer/crawl_developers_guide_docs.py
```

### Refresh Viewer v7 reference docs

```bash
python viewer/crawl_reference_docs.py
```

## Source

Autodesk APS Viewer v7 docs:
- https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/
- https://aps.autodesk.com/en/docs/viewer/v7/reference/
