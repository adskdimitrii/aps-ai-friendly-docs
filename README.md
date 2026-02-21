# APS AI Friendly Docs

Local Markdown mirror of Autodesk APS documentation with scripts to re-crawl. An alternative to `https://aps.autodesk.com/llms-full.txt` that enables more targetted prompts that reduce token usage, speed up agent discovery to increase AI agent performance on complex tasks.

This repository is organized into the following documentation domains:
- `acc/` — APS ACC docs mirror and crawlers
- `data/` — APS Data docs mirror and crawlers
- `oauth/` — APS OAuth docs mirror and crawlers
- `viewer/` — APS Viewer v7 docs mirror and crawlers
- `design-automation/` — APS Design Automation docs mirror and crawlers
- `webhooks/` — APS Webhooks docs mirror and crawlers

## Usage

Use the domain-specific READMEs for crawler commands and details:
- [ACC docs](acc/README.md)
- [Data docs](data/README.md)
- [OAuth docs](oauth/README.md)
- [Viewer v7 docs](viewer/README.md)
- [Design Automation docs](design-automation/README.md)
- [Webhooks docs](webhooks/README.md)

## Run in Dev Container

This repo includes a VS Code dev container configuration in `.devcontainer/devcontainer.json`.

1. Open this folder in VS Code.
2. Run **Dev Containers: Reopen in Container**.
3. Wait for container setup to finish. On first create, dependencies are installed automatically via:

	 ```bash
	 pip3 install --user -r requirements.txt
	 ```

No virtual environment is required inside this dev container.

## Re-crawl Docs with a Coding Agent

Instead of running commands manually, you can ask your coding agent to run the crawlers for you.

Example prompts:

- Re-crawl one domain and doc type:

	```text
	Re-crawl ACC how-to docs.
	```

