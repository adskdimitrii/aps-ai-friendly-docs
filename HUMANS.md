# Humans

Not for agents.

## How to Use This Repo

This repo has mainly been tested with Claude Code, but it should also work with other agents, such as Microsoft VS Code Copilot, Cursor, etc.

### Helps Create Solutions

```txt
Clone the APS docs https://github.com/adskdimitrii/aps-ai-friendly-docs and help me design an app.

Create a solution design Markdown document for the following app. Include a detailed implementation plan that an agent can use to create this app. Phase the implementation.

ACC User Clean Up Tool

This is a Python script that will run on a weekly schedule and deactivate ACC users if they have not signed in for 3 months.

This script will run in Azure as a Function. Create deploy, update, and destroy shell scripts using Azure CLI.
```

## How to Create APS Other Docs Contribute

Not all docs have been mirrored. If you want to add a doc, I recommend the following prompt:

```txt
Use the implementation of `./oauth/**/*` as a template to create docs for the following documentation:

https://aps.autodesk.com/en/docs/tokenflex/v1/tutorials/
https://aps.autodesk.com/en/docs/tokenflex/v1/reference/http/
```

Please make a pull request so we can build up documentation for others to use.