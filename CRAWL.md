# Crawl

How to re-crawl the docs.

## Run in Dev Container

This repo includes a VS Code dev container configuration in `.devcontainer/devcontainer.json`.

1. Open this folder in VS Code.
2. Run **Dev Containers: Reopen in Container**.
3. Authenticate claude cli

No virtual environment is required to run python inside this dev container.

## Run Crawler Scripts

Run all commands from the repository root.

Run one crawler (example: Viewer Developer's Guide):

```bash
python3 viewer/crawl_developers_guide_docs.py
```

Run any single crawler by path:

```bash
python3 <folder>/crawl_<name>.py
```

Examples:

```bash
python3 acc/crawl_howto_docs.py
python3 acc/crawl_http_docs.py
python3 data/crawl_howto_docs.py
```

Run all crawler scripts in the repo:

```bash
find . -type f -name 'crawl_*.py' | sort | while IFS= read -r f; do
	echo "RUN $f"
	python3 "$f"
done
```

## Post-Processing: Fix Links, Images, and Special Characters

After re-crawling, run the cleanup scripts from the repository root to
normalize links, remove broken image tags, and repair mojibake special
characters.

1. Preview link fixes (dry run):

```bash
python3 scripts/fix_links.py
```

2. Apply link fixes:

```bash
python3 scripts/fix_links.py --write
```

3. Preview image removals (dry run):

```bash
python3 scripts/fix_images.py
```

4. Apply image removals:

```bash
python3 scripts/fix_images.py --write
```

5. Preview special character fixes (dry run):

```bash
python3 scripts/fix_special_chars.py
```

6. Apply special character fixes:

```bash
python3 scripts/fix_special_chars.py --write
```

Recommended order:

1. Run crawlers.
2. Run `scripts/fix_links.py --write`.
3. Run `scripts/fix_images.py --write`.
4. Run `scripts/fix_special_chars.py --write`.
5. Review changes with `git diff`.

## Improve README.md Summaries

Prerequisites:

- Authenticate claude cli

Then run:

```bash
# run a specific folder
./scripts/generate_readme_summary.sh oauth

# run all
./scripts/generate_readme_summary.sh --all
```