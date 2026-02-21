# APS AI Friendly Docs

Local Markdown mirror of Autodesk APS documentation with scripts to re-crawl. It is an alternative to `https://aps.autodesk.com/llms-full.txt` that enables more targeted prompts, reduces token usage, and speeds up agent discovery to improve AI agent performance on complex tasks.

## Usage

Use the domain-specific READMEs for details:
- [ACC docs](acc/README.md)
- [Data docs](data/README.md)
- [OAuth docs](oauth/README.md)
- [Viewer v7 docs](viewer/README.md)
- [Design Automation docs](design-automation/README.md)
- [Webhooks docs](webhooks/README.md)


## How to Use This Repo

This repo has mainly been tested with Claude Code, but it should also work with other agents, such as Microsoft VS Code Copilot, Cursor, etc...

### Helps Create Solutions

```txt
Clone the APS docs https://github.com/adskdimitrii/aps-ai-friendly-docs and help me design an app.

Create a solution design Markdown document for the following app. Include a detailed implementation plan that will be used by an agent to create this app. Phase the implementation.

ACC User Clean Up Tool

This is a python script that will run on a weekly schedule that deactivates ACC users if they have not signed in for 3 months.
```