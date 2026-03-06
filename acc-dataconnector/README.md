# APS ACC Data Connector Schema Docs

Schema reference documentation for the [ACC Data Connector API](https://developer.api.autodesk.com/data-connector/v1/doc).

The Data Connector provides bulk data extraction for ACC projects. This folder documents the **data schemas** (column definitions and field types) for each extractable service group.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Schema Changes Changelog
A chronological log of all schema additions, modifications, deprecations, and deletions across all service groups.
- [Schema Changes](schema-docs/changes.md)

### Activities (~21 tables)
Audit trail data for admin, assets, bridge, cost, docs, issues, RFIs, sheets, and submittals — including activity records, change logs, custom attribute definitions, naming standards, and permissions.
- [activities](schema-docs/activities.md)
- Sub-schemas: [activities_admin_verb_column_details](schema-docs/activities_admin_verb_column_details.md), [activities_assets_verb_column_details](schema-docs/activities_assets_verb_column_details.md), [activities_cost_verb_column_details](schema-docs/activities_cost_verb_column_details.md), [activities_docs_verb_column_details](schema-docs/activities_docs_verb_column_details.md), [activities_issues_verb_column_details](schema-docs/activities_issues_verb_column_details.md), [activities_rfis_verb_column_details](schema-docs/activities_rfis_verb_column_details.md), [activities_sheets_verb_column_details](schema-docs/activities_sheets_verb_column_details.md), [activities_submittals_verb_column_details](schema-docs/activities_submittals_verb_column_details.md), [activities_bridge_verb_column_details](schema-docs/activities_bridge_verb_column_details.md)

### Admin
Account and project structure: accounts, projects, users, roles, companies, business units, services, and products.
- [admin](schema-docs/admin.md) — 16 tables

### Assets
Asset lifecycle data including asset records, categories, custom attributes, and status steps.
- [assets](schema-docs/assets.md)

### Cost (~40+ tables)
Full cost control schema: budgets, contracts, change orders, cost items, payments, schedule of values, expenses, time sheets, distribution curves, and approval workflows.
- [cost](schema-docs/cost.md)
- [estimates](schema-docs/estimates.md)

### Issues
Construction issue tracking with attachments, comments, custom attributes, placements, viewables, root causes, and subtypes.
- [issues](schema-docs/issues.md) — 13 tables (ACC Issues)
- [issuesbim360](schema-docs/issuesbim360.md) — BIM 360 issue schema variant

### RFIs
RFI records, responses, comments, attachments, and workflow data.
- [rfis](schema-docs/rfis.md)

### Sheets
Sheet metadata, version sets, uploads, and exports.
- [sheets](schema-docs/sheets.md)

### Submittals
Submittal items, packages, specs, tasks, revisions, and attachments.
- [submittals](schema-docs/submittals.md)
- [submittalsacc](schema-docs/submittalsacc.md)

### Checklists, Forms & Daily Logs
- [checklists](schema-docs/checklists.md)
- [forms](schema-docs/forms.md)
- [dailylogs](schema-docs/dailylogs.md)

### Model Coordination
Clash detection and model coordination data.
- [clashes](schema-docs/clashes.md)

### Locations, Relationships & Reviews
- [locations](schema-docs/locations.md)
- [relationships](schema-docs/relationships.md)
- [reviews](schema-docs/reviews.md)

### Other Service Groups
- [schedule](schema-docs/schedule.md), [classifications](schema-docs/classifications.md), [takeoff](schema-docs/takeoff.md), [markups](schema-docs/markups.md), [meetingminutes](schema-docs/meetingminutes.md), [photos](schema-docs/photos.md), [packages](schema-docs/packages.md), [transmittals](schema-docs/transmittals.md), [iq](schema-docs/iq.md)

### CDC (Cross-Data-Center) Variants
Alternative schema variants for CDC-routed data: [cdcadmin](schema-docs/cdcadmin.md), [cdccost](schema-docs/cdccost.md), [cdcissues](schema-docs/cdcissues.md), [cdcrfis](schema-docs/cdcrfis.md), [cdcsheets](schema-docs/cdcsheets.md), [cdcsubmittalsacc](schema-docs/cdcsubmittalsacc.md), [cdcschedule](schema-docs/cdcschedule.md), [cdclocations](schema-docs/cdclocations.md), [cdcmarkups](schema-docs/cdcmarkups.md), [cdcmeetingminutes](schema-docs/cdcmeetingminutes.md), [cdcrelationships](schema-docs/cdcrelationships.md), [cdctransmittals](schema-docs/cdctransmittals.md), [cdciq](schema-docs/cdciq.md), [cdcv2admin](schema-docs/cdcv2admin.md)
<!-- GENERATED:CONTENT_SUMMARY:END -->
