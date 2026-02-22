# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This repo is a local markdown mirror of Autodesk Platform Services (APS) documentation. It is primarily used as a knowledge base for AI agents answering APS API questions — not as a software project with tests or a build system.

## Documentation Structure

Docs are organized by API domain, each with a consistent subdirectory layout:

```
<domain>/
  README.md              # Human/agent index with content summary
  crawl_*.py             # Crawler scripts to re-fetch docs from aps.autodesk.com
  how-to-docs/           # Tutorial/workflow guides
  http-docs/             # Per-endpoint HTTP reference (one file per endpoint)
  developers-guide-docs/ # Conceptual and developer guides
  reference-docs/        # API class/extension reference (e.g., Viewer SDK)
  _url_index.md          # Auto-generated URL→file mapping (do not edit manually)
```

**Start with a domain's `README.md`** — it has a content summary with links. If a specific endpoint isn't linked there, check the domain's `http-docs/` directory which contains all endpoints.

## Running Crawlers

Install dependencies (only needed outside the dev container):

```bash
pip3 install --user -r requirements.txt
```

Run a single crawler from the repo root:

```bash
python3 <domain>/crawl_<name>.py
# e.g.:
python3 acc/crawl_howto_docs.py
python3 viewer/crawl_developers_guide_docs.py
```

Run all crawlers:

```bash
find . -type f -name 'crawl_*.py' | sort | while IFS= read -r f; do
  echo "RUN $f"
  python3 "$f"
done
```

## Regenerating README Summaries

The `<!-- GENERATED:CONTENT_SUMMARY:START/END -->` blocks in each domain README are produced by:

```bash
# Single domain
./generate_readme_summary.sh oauth

# All domains
./generate_readme_summary.sh --all
```

This calls the `claude` CLI (`claude -p --output-format text`) and requires it to be installed and authenticated. The script replaces only the content between the markers, leaving the rest of the README intact.

## Adding a New Domain

Use an existing domain (e.g., `oauth/`) as the template. Each domain needs:
1. Crawler script(s) named `crawl_<name>.py`
2. Output subdirectories matching the pattern above
3. A `README.md` (the summary script will generate or update the content summary block)
