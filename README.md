# APS AI Friendly Docs

Lightweight, local Markdown mirror of Autodesk APS documentation.

This repository is organized into two documentation domains:
- `acc/` — APS ACC docs mirror and crawlers
- `oauth/` — APS OAuth docs mirror and crawlers

## Repository Structure

- `acc/` — ACC crawlers, generated docs, and source URL indexes
- `oauth/` — OAuth crawlers, generated docs, and source URL indexes

## Prerequisites

- Python 3.10+
- Internet access (scripts fetch live docs)

Install dependencies:

```bash
python -m pip install requests beautifulsoup4
```

## Usage

Use the domain-specific READMEs for crawler commands and details:
- [ACC docs](acc/README.md)
- [OAuth docs](oauth/README.md)

## Output Format

Each generated Markdown file includes:
- Page title
- Original APS source URL
- Extracted page content (headings, paragraphs, lists, code blocks, tables-as-text)

## Notes

- Generated filenames are slugified from APS URL paths.
- If two pages would produce the same filename, the crawler falls back to a full-path slug.
- Some pages may be skipped if source fetch/parsing fails; the scripts print warnings and a final summary.
