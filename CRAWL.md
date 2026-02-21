## Run in Dev Container

This repo includes a VS Code dev container configuration in `.devcontainer/devcontainer.json`.

1. Open this folder in VS Code.
2. Run **Dev Containers: Reopen in Container**.
3. Wait for container setup to finish. On first create, dependencies are installed automatically via:

	 ```bash
	 pip3 install --user -r requirements.txt
	 ```

No virtual environment is required inside this dev container.

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

## Improve README.md Summaries

Prerequisites:

- Run from the repo root.
- Install and authenticate the `claude` CLI, and ensure `claude` is available in your `PATH`.
- Make the script executable if needed:

Then run:

```bash
# run a specific folder
  ./generate_readme_summary.sh oauth

# run all
  ./generate_readme_summary.sh --all
```