# Humans

Not for agents.

## How to Use This Repo

This repo has mainly been tested with Claude Code, but it should also work with other agents, such as Microsoft VS Code Copilot, Cursor, etc.

### Ask Questions

```txt
Clone the APS docs https://github.com/adskdimitrii/aps-ai-friendly-docs to help me answer some questions.

Can I use APS to automate the creation of PDF files from Revit files? How does this work, and what are the limitations?
```

Output from Claude Code using Sonnet 4.6:

```txt
How to Generate PDFs from Revit Files with APS                                                                                                                                                                                   
                                                                                                                                                                                                                                   
  Approach 1: Model Derivative API                                                                                                                                                                                                 

  The most straightforward programmatic approach. When submitting a translation job, set the 2dviews parameter to "pdf" in the advanced options:
                                                                                                                                                                                                                                   
  {                                                                                                                                                                                                                                
    "input": { "urn": "<encoded-file-urn>" },
    "output": {
      "formats": [{
        "type": "svf",
        "advanced": { "2dviews": "pdf" }
      }]
    }
  }

  This renders the Revit file's 2D views/sheets as PDFs alongside the normal translation output.

  Approach 2: ACC Files API (Batch Export)

  If your files live in Autodesk Construction Cloud, use POST /projects/{projectId}/exports. This supports:
  - Exporting 2D sheets/views from RVT files as PDFs
  - Batch exports (up to 200 files, max 10 GB total)
  - Including markups, issues, and photos
  - Async workflow: submit → poll status → download from signed S3 URL (valid 1 hour)
  - Results are packaged as a ZIP file

  Approach 3: Design Automation API

  For custom workflows, there is a shared AutoCAD.PlotToPDF+prod activity. For Revit-specific automation, you'd build a custom Design Automation activity using the Revit engine.

  ---
  Limitations

  ┌──────────────────────────┬───────────────────────────────────────────────────────────────────────────────────────────────────┐
  │        Constraint        │                                              Detail                                               │
  ├──────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Revit version            │ Revit 2022 or newer required for both Model Derivative and ACC PDF export                         │
  ├──────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ 2D only                  │ PDF output is limited to 2D views and sheets — 3D models cannot be exported to PDF                │
  ├──────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Model Derivative default │ The 2dviews parameter defaults to "legacy" (proprietary format), so you must explicitly set "pdf" │
  ├──────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ ACC batch limits         │ Max 200 files per export operation, 10 GB total                                                   │
  ├──────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ DWG restriction          │ For ACC, DWG files must have been uploaded after May 1, 2023                                      │
  ├──────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Async processing         │ Both Model Derivative and ACC require polling — no synchronous PDF response                       │
  └──────────────────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────┘

  The Model Derivative API is the best fit for a general automation pipeline, while the ACC Files API is ideal if your Revit files are already managed in ACC and you need bulk exports with markup support.

```

### Helps Create Solutions

```txt
Clone the APS docs https://github.com/adskdimitrii/aps-ai-friendly-docs and help me design an app.

Create a solution design Markdown document for the following app. Include a detailed implementation plan that an agent can use to create this app. Phase the implementation.

ACC User Clean Up Tool

This is a Python script that will run on a weekly schedule and deactivate ACC users if they have not signed in for three months.

This script will run in Azure as a Function. Create deploy, update, and destroy shell scripts using Azure CLI.
```

### Work on Complex Coding Tasks

```txt
Clone the APS docs https://github.com/adskdimitrii/aps-ai-friendly-docs and help me implement the following feature.

Implement APS Auth into my desktop app.
```

## How to Contribute Other APS Docs

Not all docs have been mirrored. If you want to add a doc, I recommend using the following prompt:

```txt
Use the implementation of `./oauth/**/*` as a template to create docs for the following documentation:

https://aps.autodesk.com/en/docs/tokenflex/v1/tutorials/
https://aps.autodesk.com/en/docs/tokenflex/v1/reference/http/
```

Please make a pull request so we can build up documentation for others to use.