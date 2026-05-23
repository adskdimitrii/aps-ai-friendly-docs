# APS AI Friendly Docs

Local markdown mirror of Autodesk Platform Services (APS) documentation with scripts to re-crawl. This is an alternative to [https://aps.autodesk.com/llms.txt](https://aps.autodesk.com/llms.txt) that enables more targeted prompts, reduces token usage, tool usage and speeds up agent discovery to improve performance on complex tasks.

## Where to Find Things

- [OAuth Docs](oauth/README.md) - ALL APIs Require OAuth
- [ACC Docs](acc/README.md) - Also known as BIM 360, Autodesk Construction Cloud & Forma
- [ACC Data Connector Schema Docs](acc-dataconnector/README.md) - ACC/Forma Data Connector schema documentation
- [Data Docs](data/README.md) - Object Secuire Storage (OSS), Core Data Managment for ACC / Forma
- [Model Derivative Docs](model-derivative/README.md) - Extract Data from Files, Convert, Export
- [Viewer v7 Docs](viewer/README.md) - Web Viewer
- [Design Automation Docs](design-automation/README.md) - Also Known as `Automation APIs` run Revit / AutoCAD, etc... plugins in the cloud
- [AEC Data Model Docs](aecdatamodel/README.md) - GraphQL API for BIM Element Data in ACC / Forma / OSS
- [Webhooks Docs](webhooks/README.md)

## Re-Crawl

See [CRAWL.md](CRAWL.md) - How to run crawlers and post-process tools.

## Humans

See [HUMANS.md](HUMANS.md)

## Design Theory

See [DESIGN.md](DESIGN.md) — why local docs outperform `llms.txt` for agents, with a worked example.