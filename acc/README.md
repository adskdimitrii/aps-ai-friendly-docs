# APS ACC Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

This folder contains **435 files** across two subdirectories (`http-docs/` and `how-to-docs/`) covering the Autodesk Construction Cloud (ACC) platform APIs.

### Admin, Projects & Account Management
Account and project administration, user management, companies, and business units. Includes onboarding guides for retrieving account/project IDs and managing access.
- **How-to guides (2):** [Create & Configure Projects](how-to-docs/admin-admin-create-configure-projects.md), [Retrieve Account & Project ID](how-to-docs/getting-started-retrieve-account-and-project-id.md)
- **Getting started (1):** [Manage Access to ACC](how-to-docs/getting-started-manage-access-to-acc.md)
- **API endpoints (~30):** [GET Account Projects](http-docs/http-admin-accounts-accountidprojects-GET.md), [POST Project Users](http-docs/http-admin-projects-project-Id-users-POST.md), [GET Companies](http-docs/http-companies-GET.md), [POST Users](http-docs/http-users-POST.md), [GET Business Units](http-docs/http-business_units_structure-GET.md), and 25 more covering CRUD operations for accounts, projects, users, companies, and roles.

### Cost Management
The largest API surface — budgets, contracts, change orders, expenses, payments, cost items, schedule of values, time sheets, performance tracking, segments, and templates.
- **How-to guides (14):** [Setup Budget Code Template](how-to-docs/cost-cost-setup-budget-code-template.md), [Create PCO](how-to-docs/cost-create-pco.md), [Link Budgets & Contracts](how-to-docs/cost-link-budgets-and-contract-new.md), [Track Budget Performance](how-to-docs/cost-cost-track-aggregated-budget-performance.md), [Integrate with External System](how-to-docs/cost-integrate-with-external-system.md), [Attach Cost File to S3](how-to-docs/cost-attach-cost-file-s3.md), and 8 more.
- **API endpoints (~97):** [GET Budgets](http-docs/http-cost-budgets-GET.md), [POST Contracts](http-docs/http-cost-contracts-POST.md), [GET Change Orders](http-docs/http-cost-change-orders-GET.md), [POST Expenses](http-docs/http-cost-expenses-POST.md), [GET Main Contracts](http-docs/http-cost-main-contracts-GET.md), [GET Payments](http-docs/http-cost-payments-GET.md), [POST Time Sheets](http-docs/http-cost-time-sheets-POST.md), and 90 more.

### Issues
Create, retrieve, and manage project issues including attachments, comments, and references.
- **How-to guides (8):** [Create Issues](how-to-docs/issues-create-issues.md), [Retrieve Issues](how-to-docs/issues-retrieve-issues.md), [Upload Attachments](how-to-docs/issues-upload-issue-attachments.md), [Add References](how-to-docs/issues-add-references-to-issues.md), and 4 more.
- **API endpoints (~14):** [GET Issues](http-docs/http-issues-issues-GET.md), [POST Issues](http-docs/http-issues-issues-POST.md), [POST Attachments](http-docs/http-issues-attachments-POST.md), [GET Comments](http-docs/http-issues-comments-GET.md), and 10 more.

### RFIs (Requests for Information)
Full RFI lifecycle — creation, responses, official responses, transitions, attachments, and comments.
- **How-to guides (5):** [Create RFI](how-to-docs/rfis3-rfi-create.md), [RFI Response](how-to-docs/rfis3-rfi-response.md), [Official Response](how-to-docs/rfis3-rfi-official-response.md), [RFI Transitions](how-to-docs/rfis3-rfi-transitions.md), [Upload to RFI](how-to-docs/rfis3-rfi-upload.md)
- **API endpoints (~16):** [POST RFIs](http-docs/http-rfis-rfis-POST.md), [GET RFI by ID](http-docs/http-rfis-rfis-id-GET.md), [POST Responses](http-docs/http-rfis-rfis-id-responses-POST.md), [GET Attributes](http-docs/http-rfis-attributes-GET.md), and 12 more.

### Document Management & Files
File upload/download via S3, PDF export, custom attributes, folder permissions, naming standards, and linked files.
- **How-to guides (4):** [Upload Document to S3](how-to-docs/files-upload-document-s3.md), [Download Document from S3](how-to-docs/files-download-document-s3.md), [Export PDF Files](how-to-docs/files-export-pdf-files.md), [RCM Linked Files](how-to-docs/files-rcm-linked-files.md)
- **API endpoints (~10):** [GET Custom Attribute Definitions](http-docs/http-document-management-custom-attribute-definitions-GET.md), [GET Folder Permissions](http-docs/http-document-management-projects-project_id-folders-folder_id-permissions-GET.md), [POST Export PDF](http-docs/http-v1-files-export-pdf-files-POST.md), and 7 more.

### Sheets
Upload, export, manage, and review sheets; version sets and collections.
- **How-to guides (2):** [Upload Sheets](how-to-docs/sheets-upload-sheets.md), [Export Sheets](how-to-docs/sheets-export-sheets.md)
- **API endpoints (~22):** [GET Sheets](http-docs/http-sheets-sheets-GET.md), [POST Uploads](http-docs/http-sheets-uploads-POST.md), [POST Exports](http-docs/http-sheets-exports-POST.md), [GET Collections](http-docs/http-sheets-collections-GET.md), [POST Version Sets](http-docs/http-sheets-version-sets-POST.md), and 17 more.

### Model Coordination
Clash detection services and model set management — create model sets, run clash tests, manage clash groups, and views.
- **How-to guides (2):** [Clash Tutorial](how-to-docs/model-coordination-mc-tutorial-clash.md), [Model Set Tutorial](how-to-docs/model-coordination-mc-tutorial-model-set.md)
- **API endpoints (~42):** [GET Clash Tests](http-docs/http-mc-clash-service-v3-get-model-set-clash-tests-GET.md), [GET Grouped Clashes](http-docs/http-mc-clash-service-v3-get-grouped-clashes-GET.md), [POST Create Model Set](http-docs/http-mc-modelset-service-v3-create-model-set-POST.md), [GET Model Sets](http-docs/http-mc-modelset-service-v3-get-model-sets-GET.md), and 38 more.

### Model Properties & Indexing
Query, diff, and index model properties across versions. Supports batch jobs and field-level queries.
- **How-to guides (3):** [Query Properties](how-to-docs/model-properties-query.md), [Diff Properties](how-to-docs/model-properties-diff.md), [Query Reference](how-to-docs/model-properties-query-ref.md)
- **API endpoints (~16):** [POST Index Query](http-docs/http-index-v2-index-query-post.md), [GET Index Fields](http-docs/http-index-v2-index-fields-get.md), [POST Diff Query](http-docs/http-index-v2-diff-query-post.md), [GET Diff Status](http-docs/http-index-v2-diff-status-get.md), and 12 more.

### Assets
Asset lifecycle management — statuses, categories, custom attributes, and status step sets.
- **How-to guides (3):** [Create Assets & Settings](how-to-docs/assets-create-assets-project-settings.md), [Manage Assets](how-to-docs/assets-manage-assets.md), [Retrieve Asset Data](how-to-docs/assets-retrieve-assets-data.md)
- **API endpoints (~24):** [GET Assets](http-docs/http-assets-assets-v2-GET.md), [POST Batch Create](http-docs/http-assets-assets-batch-create-POST-v2.md), [GET Categories](http-docs/http-assets-categories-GET.md), [GET Custom Attributes](http-docs/http-assets-custom-attributes-GET.md), and 20 more.

### Submittals
Submittal items, packages, specs, revisions, tasks, responses, attachments, and workflow transitions.
- **How-to guides (5):** [Create Submittal Item](how-to-docs/submittals-create-submittal-item.md), [Attach Files](how-to-docs/submittals-attach-files-tool.md), [Attach Local Files](how-to-docs/submittals-attach-local-files.md), [Download Attachments](how-to-docs/submittals-download-submittal-attachements.md), [Transitions](how-to-docs/submittals-submittal-transitions.rst.md)
- **API endpoints (~26):** [GET Items](http-docs/http-submittals-items-GET.md), [POST Items](http-docs/http-submittals-items-POST.md), [GET Packages](http-docs/http-submittals-packages-GET.md), [GET Specs](http-docs/http-submittals-specs-GET.md), and 22 more.

### Forms
Create, update, and retrieve project forms with location-based filtering.
- **How-to guides (3):** [Create & Update Forms](how-to-docs/forms-create-update-forms.md), [Retrieve Forms](how-to-docs/forms-retrieve-forms.md), [Retrieve by Location](how-to-docs/forms-retrieve-forms-based-on-locations.md)
- **API endpoints (5):** [GET Forms](http-docs/http-forms-forms-GET.md), [POST Forms](http-docs/http-forms-forms-POST.md), [PATCH Form](http-docs/http-forms-forms-formId-PATCH.md), [GET Templates](http-docs/http-forms-form-templates-GET.md), [PUT Batch Update Values](http-docs/http-forms-valuesbatch-update-PUT.md)

### Reviews
Create and manage document reviews and approval workflows.
- **How-to guides (3):** [Create Review](how-to-docs/reviews-reviews-create-review.md), [Create Workflow](how-to-docs/reviews-reviews-create-workflow.md), [Query Review Resources](how-to-docs/reviews-reviews-query-review-resources.md)
- **API endpoints (~10):** [POST Create Review](http-docs/http-reviews-createreview-POST.md), [GET Reviews](http-docs/http-reviews-reviews-GET.md), [GET Workflow](http-docs/http-reviews-getworkflow-GET.md), and 7 more.

### Relationships
Create and query relationships between entities across ACC services.
- **How-to guides (2):** [Create Relationships](how-to-docs/relationships-relationships-create.md), [Relationships Tutorial](how-to-docs/relationships-relationships-tutorial.md)
- **API endpoints (~8):** [PUT Add Relationships](http-docs/http-relationship-service-v2-add-relationships-PUT.md), [GET Search Relationships](http-docs/http-relationship-service-v2-search-relationships-GET.md), and 6 more.

### Data Connector
Submit data extraction requests, track jobs, and retrieve exported data.
- **How-to guides (3):** [Submit Data Request](how-to-docs/data-connector-dc-tutorial-submit-data-request.md), [Retrieve Data Extract](how-to-docs/data-connector-dc-tutorial-retrieve-data-extract.md), [Find & Update Request](how-to-docs/data-connector-dc-tutorial-find-update-data-request.md)
- **API endpoints (~10):** [POST Requests](http-docs/http-data-connector-requests-POST.md), [GET Jobs](http-docs/http-data-connector-jobs-GET.md), and 8 more.

### Takeoff
Quantification takeoff — classification systems, packages, takeoff items/types, content views, and settings.
- **How-to guide (1):** [Extract Inventory](how-to-docs/takeoff-takeoff-extract-inventory.md)
- **API endpoints (~16):** [GET Packages](http-docs/http-takeoff-projects-project_id-packages-GET.md), [GET Classification Systems](http-docs/http-takeoff-projects-project_id-classification-systems-GET.md), [GET Takeoff Items](http-docs/http-takeoff-projects-project_id-packages-package_id-takeoff-items-GET.md), and 13 more.

### Locations, AutoSpecs, Transmittals, Photos & Packages
Smaller services for managing project location trees, automated specification analysis, document transmittals, project photos, and package resources.
- **How-to guides (2):** [Configure Locations Tree](how-to-docs/locations-configure-locations-tree.md), [Retrieve Smart Register](how-to-docs/autospecs-retrieve-smart-register.md)
- **API endpoints (~17):** [GET/POST Location Nodes](http-docs/http-locations-nodes-GET.md), [GET AutoSpecs Metadata](http-docs/http-autospecs-getprojectmetadata-GET.md), [GET Transmittals](http-docs/http-transmittals-listtransmittals-GET.md), [POST Filtered Photos](http-docs/http-photos-getfilteredphotos-POST.md), [GET Packages](http-docs/http-packages-list-packages-GET.md), and 12 more.
<!-- GENERATED:CONTENT_SUMMARY:END -->
