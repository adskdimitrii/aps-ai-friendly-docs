# AGENTS

This repo runs in a dev container. See `.devcontainer/devcontainer.json`. When running python do not create a venv.

## Running scripts

Run a specific crawler:

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