# APS AI Friendly Docs

Lightweight, local Markdown mirror of Autodesk APS documentation with scripts to re-crawl. An alternative to `https://aps.autodesk.com/llms-full.txt` that enables more targetted prompts that reduce token usage and increase AI agent performance.

This repository is organized into three documentation domains:
- `acc/` — APS ACC docs mirror and crawlers
- `data/` — APS Data docs mirror and crawlers
- `oauth/` — APS OAuth docs mirror and crawlers

## Prerequisites to Re-Crawl

- Python 3.10+
- Internet access (scripts fetch live docs)

Install dependencies:

```bash
python -m pip install requests beautifulsoup4
```

## Usage

Use the domain-specific READMEs for crawler commands and details:
- [ACC docs](acc/README.md)
- [Data docs](data/README.md)
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
