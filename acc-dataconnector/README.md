# APS ACC Data Connector Schema Docs

Schema reference documentation for the [ACC Data Connector API](https://developer.api.autodesk.com/data-connector/v1/doc).

The Data Connector provides bulk data extraction for ACC projects. This folder documents the **data schemas** (column definitions and field types) for each extractable service group.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

All documentation in this domain covers **ACC Data Connector schema definitions** — field-level reference for the tables and columns exposed by the Data Connector extraction pipeline. Files are in [`schema-docs/`](schema-docs/).

### Overview

- [Index](schema-docs/_index.md) — top-level index of all available Data Connector schemas.

### Activities

Schema for the unified activity feed and per-module verb column details (10 files).

- [Activities](schema-docs/activities.md) — base activity table schema
- [Admin verb details](schema-docs/activities_admin_verb_column_details.md), [Assets](schema-docs/activities_assets_verb_column_details.md), [Bridge](schema-docs/activities_bridge_verb_column_details.md), [Cost](schema-docs/activities_cost_verb_column_details.md), [Docs](schema-docs/activities_docs_verb_column_details.md), [Issues](schema-docs/activities_issues_verb_column_details.md), [RFIs](schema-docs/activities_rfis_verb_column_details.md), [Sheets](schema-docs/activities_sheets_verb_column_details.md), [Submittals](schema-docs/activities_submittals_verb_column_details.md)

### Admin & Projects

Schema for project and account administration tables (3 files).

- [Admin](schema-docs/admin.md), [CDC Admin](schema-docs/cdcadmin.md), [CDC v2 Admin](schema-docs/cdcv2admin.md)

### Cost Management

Schema for cost, estimates, and change management tables (5 files).

- [Cost](schema-docs/cost.md), [CDC Cost](schema-docs/cdccost.md), [Estimates](schema-docs/estimates.md), [Changes](schema-docs/changes.md), [Packages](schema-docs/packages.md)

### Issues & RFIs

Schema for issues (ACC and BIM 360) and RFI tables (5 files).

- [Issues](schema-docs/issues.md), [Issues (BIM 360)](schema-docs/issuesbim360.md), [CDC Issues](schema-docs/cdcissues.md), [RFIs](schema-docs/rfis.md), [CDC RFIs](schema-docs/cdcrfis.md)

### Assets

- [Assets](schema-docs/assets.md) — schema for asset tracking tables.

### Sheets & Markups

Schema for sheet management, markups, and photos (5 files).

- [Sheets](schema-docs/sheets.md), [CDC Sheets](schema-docs/cdcsheets.md), [Markups](schema-docs/markups.md), [CDC Markups](schema-docs/cdcmarkups.md), [Photos](schema-docs/photos.md)

### Submittals & Transmittals

Schema for submittal and transmittal workflows (5 files).

- [Submittals](schema-docs/submittals.md), [Submittals ACC](schema-docs/submittalsacc.md), [CDC Submittals ACC](schema-docs/cdcsubmittalsacc.md), [Transmittals](schema-docs/transmittals.md), [CDC Transmittals](schema-docs/cdctransmittals.md)

### Schedule

- [Schedule](schema-docs/schedule.md), [CDC Schedule](schema-docs/cdcschedule.md)

### Field Management

Schema for daily field operations (4 files).

- [Checklists](schema-docs/checklists.md), [Forms](schema-docs/forms.md), [Reviews](schema-docs/reviews.md), [Daily Logs](schema-docs/dailylogs.md)

### Locations & Classifications

- [Locations](schema-docs/locations.md), [CDC Locations](schema-docs/cdclocations.md), [Classifications](schema-docs/classifications.md)

### Relationships & Clashes

- [Relationships](schema-docs/relationships.md), [CDC Relationships](schema-docs/cdcrelationships.md), [Clashes](schema-docs/clashes.md)

### Meeting Minutes

- [Meeting Minutes](schema-docs/meetingminutes.md), [CDC Meeting Minutes](schema-docs/cdcmeetingminutes.md)

### Insight & Quality (IQ) and Takeoff

- [IQ](schema-docs/iq.md), [CDC IQ](schema-docs/cdciq.md), [Takeoff](schema-docs/takeoff.md)
<!-- GENERATED:CONTENT_SUMMARY:END -->
