# AGENTS

Guidance for coding agents working in this repository.

## Python environment in this repo

- Base image: `mcr.microsoft.com/devcontainers/python:2-3.12-bookworm`
- Use `python3` and `pip3` (not `python`/`pip`).
- Dependencies are installed at container creation via:
  - `pip3 install --user -r requirements.txt`

## Quick start

From the repository root:

```bash
python3 --version
pip3 --version
python3 -m pip install --user -r requirements.txt
```

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

## Working directory guidance

- If a script uses paths based on `__file__`, it can be run from any directory.
- Prefer running from repo root for consistency.

## Troubleshooting

- If imports fail, reinstall deps:

```bash
python3 -m pip install --user -r requirements.txt
```

- If a script fails on network calls, retry (these crawlers depend on external APS docs endpoints).