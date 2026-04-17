# APS ACC Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Getting Started
Two onboarding guides: [Manage Access to ACC](how-to-docs/getting-started-manage-access-to-acc.md) and [Retrieve Account and Project IDs](how-to-docs/getting-started-retrieve-account-and-project-id.md).

### Admin & Projects (~12 files)
APIs for creating and managing ACC projects and user memberships, including roles and product assignments.

- How-to: [Create and Configure Projects](how-to-docs/admin-admin-create-configure-projects.md)
- HTTP: [GET Projects](http-docs/http-admin-accounts-accountidprojects-GET.md), [POST Projects](http-docs/http-admin-accounts-accountidprojects-POST.md), [Import Users](http-docs/http-admin-v2-projects-project-Id-users-import-POST.md), and 8 more.

### Companies & Users (~16 files)
Search, create, update, and import users and companies across accounts and projects.

- HTTP: [GET Users](http-docs/http-users-GET.md), [POST Users](http-docs/http-users-POST.md), [GET Companies](http-docs/http-companies-GET.md), [Import Companies](http-docs/http-companies-import-POST.md), and 12 more.

### Cost Management (~75 files)
The largest domain — full lifecycle cost management: budgets, contracts, change orders, expenses, payments, time sheets, and performance tracking.

- How-to: [Create PCO](how-to-docs/cost-create-pco.md), [Track Budget Performance](how-to-docs/cost-cost-track-aggregated-budget-performance.md), [Link Budgets and Contracts](how-to-docs/cost-link-budgets-and-contract-new.md), [Integrate with External System](how-to-docs/cost-integrate-with-external-system.md), and 11 more.
- HTTP: [GET Budgets](http-docs/http-cost-budgets-GET.md), [GET Contracts](http-docs/http-cost-contracts-GET.md), [GET Change Orders](http-docs/http-cost-change-orders-GET.md), [GET Expenses](http-docs/http-cost-expenses-GET.md), and ~55 more.

### Issues (~21 files)
Full CRUD for ACC Issues including attachments, comments, custom attributes, and type/root-cause configuration.

- How-to: [Create Issues](how-to-docs/issues-create-issues.md), [Retrieve Issues](how-to-docs/issues-retrieve-issues.md), [Upload Attachments](how-to-docs/issues-upload-issue-attachments.md), and 5 more.
- HTTP: [GET Issues](http-docs/http-issues-issues-GET.md), [POST Issues](http-docs/http-issues-issues-POST.md), [PATCH Issue](http-docs/http-issues-issues-issueId-PATCH.md), and 10 more.

### RFIs (~18 files)
Create and manage Requests for Information — responses, transitions, attachments, custom attributes, and workflow queries.

- How-to: [Create RFI](how-to-docs/rfis3-rfi-create.md), [Official Response](how-to-docs/rfis3-rfi-official-response.md), [Transitions](how-to-docs/rfis3-rfi-transitions.md), and 2 more.
- HTTP: [POST RFIs](http-docs/http-rfis-rfis-POST.md), [GET RFI](http-docs/http-rfis-rfis-id-GET.md), [Search RFIs](http-docs/http-rfis-rfi-search-POST.md), and 10 more.

### Submittals (~28 files)
Submittal item lifecycle: create, transition, respond, attach files, manage specs, packages, tasks, and templates.

- How-to: [Create Submittal Item](how-to-docs/submittals-create-submittal-item.md), [Attach Files](how-to-docs/submittals-attach-files-tool.md), [Download Attachments](how-to-docs/submittals-download-submittal-attachements.md), and 2 more.
- HTTP: [GET Items](http-docs/http-submittals-items-GET.md), [POST Items](http-docs/http-submittals-items-POST.md), [GET Packages](http-docs/http-submittals-packages-GET.md), and 20 more.

### Forms (~18 files)
Forms APIs including templates, layouts, sections, custom values, table values, and weather data.

- How-to: [Create/Update Forms](how-to-docs/forms-create-update-forms.md), [Manage Layouts and Tables](how-to-docs/forms-manage-layouts-and-tables.md), [Retrieve Forms by Location](how-to-docs/forms-retrieve-forms-based-on-locations.md), and 2 more.
- HTTP: [GET Forms](http-docs/http-forms-forms--New--Beta--GET.md), [POST Forms](http-docs/http-forms-forms-POST.md), [GET Templates](http-docs/http-forms-form-templates-GET.md), and 10 more.

### Sheets (~20 files)
Sheet upload, export, version sets, collections, review workflows, and batch operations.

- How-to: [Upload Sheets](how-to-docs/sheets-upload-sheets.md), [Export Sheets](how-to-docs/sheets-export-sheets.md)
- HTTP: [GET Sheets](http-docs/http-sheets-sheets-GET.md), [POST Storage](http-docs/http-sheets-storage-POST.md), [POST Exports](http-docs/http-sheets-exports-POST.md), [GET Version Sets](http-docs/http-sheets-version-sets-GET.md), and 14 more.

### Files & Document Management (~12 files)
Document upload/download (S3), PDF export, linked files, folder permissions, naming standards, and custom attribute definitions.

- How-to: [Upload Document](how-to-docs/files-upload-document-s3.md), [Download Document](how-to-docs/files-download-document-s3.md), [Export PDF Files](how-to-docs/files-export-pdf-files.md), [Linked Files](how-to-docs/files-rcm-linked-files.md)
- HTTP: [POST PDF Export](http-docs/http-v1-files-export-pdf-files-POST.md), [Folder Permissions](http-docs/http-document-management-projects-project_id-folders-folder_id-permissions-GET.md), and 6 more.

### Assets (~18 files)
Asset management including categories, custom attributes, status step sets, and batch operations.

- How-to: [Manage Assets](how-to-docs/assets-manage-assets.md), [Retrieve Assets Data](how-to-docs/assets-retrieve-assets-data.md), [Create Project Settings](how-to-docs/assets-create-assets-project-settings.md)
- HTTP: [GET Assets](http-docs/http-assets-assets-v2-GET.md), [Batch Create Assets](http-docs/http-assets-assets-batch-create-POST-v2.md), [GET Categories](http-docs/http-assets-categories-GET.md), and 12 more.

### Model Coordination (~37 files)
Model sets, versions, views, clash detection, clash groups, screenshots, and issue integration.

- How-to: [Model Set Tutorial](how-to-docs/model-coordination-mc-tutorial-model-set.md), [Clash Tutorial](how-to-docs/model-coordination-mc-tutorial-clash.md)
- HTTP (Model Sets): [Create Model Set](http-docs/http-mc-modelset-service-v3-create-model-set-POST.md), [GET Model Set](http-docs/http-mc-modelset-service-v3-get-model-set-GET.md), and 17 more.
- HTTP (Clash): [GET Clash Test](http-docs/http-mc-clash-service-v3-get-clash-test-GET.md), [GET Grouped Clashes](http-docs/http-mc-clash-service-v3-get-grouped-clashes-GET.md), and 14 more.

### Model Properties & Index (~19 files)
Query and diff model properties via the Index v2 API — fields, manifests, jobs, and property queries.

- How-to: [Query Properties](how-to-docs/model-properties-query.md), [Diff Properties](how-to-docs/model-properties-diff.md), [Query Reference](how-to-docs/model-properties-query-ref.md)
- HTTP: [POST Index Query](http-docs/http-index-v2-index-query-post.md), [GET Index Status](http-docs/http-index-v2-index-status-get.md), [POST Diff Query](http-docs/http-index-v2-diff-query-post.md), and 13 more.

### Data Connector (~13 files)
Extract and manage ACC data via scheduled requests and jobs.

- How-to: [Submit Data Request](how-to-docs/data-connector-dc-tutorial-submit-data-request.md), [Retrieve Data Extract](how-to-docs/data-connector-dc-tutorial-retrieve-data-extract.md), [Find and Update Requests](how-to-docs/data-connector-dc-tutorial-find-update-data-request.md)
- HTTP: [POST Requests](http-docs/http-data-connector-requests-POST.md), [GET Jobs](http-docs/http-data-connector-jobs-GET.md), [GET Job Data](http-docs/http-data-connector-jobs-jobId-data-name-GET.md), and 7 more.

### Locations (~5 files)
Manage project location trees — create, update, delete, and retrieve location nodes.

- How-to: [Configure Locations Tree](how-to-docs/locations-configure-locations-tree.md)
- HTTP: [GET Nodes](http-docs/http-locations-nodes-GET.md), [POST Nodes](http-docs/http-locations-nodes-POST.md), [PATCH Node](http-docs/http-locations-nodesnodeid-PATCH.md), [DELETE Node](http-docs/http-locations-nodesnodeid-DELETE.md)

### Reviews (~13 files)
Create and query review workflows, approvals, and version approval statuses.

- How-to: [Create Review](how-to-docs/reviews-reviews-create-review.md), [Create Workflow](how-to-docs/reviews-reviews-create-workflow.md), [Query Resources](how-to-docs/reviews-reviews-query-review-resources.md)
- HTTP: [POST Review](http-docs/http-reviews-createreview-POST.md), [GET Review](http-docs/http-reviews-getreview-GET.md), [GET Workflows](http-docs/http-reviews-workflows-GET.md), and 7 more.

### Relationships (~11 files)
Create, delete, search, and sync relationships between ACC entities across domains.

- How-to: [Create Relationships](how-to-docs/relationships-relationships-create.md), [Relationships Tutorial](how-to-docs/relationships-relationships-tutorial.md)
- HTTP: [Add Relationships](http-docs/http-relationship-service-v2-add-relationships-PUT.md), [Search Relationships](http-docs/http-relationship-service-v2-search-relationships-GET.md), [Sync Relationships](http-docs/http-relationship-service-v2-relationships-sync-POST.md), and 6 more.

### Takeoff (~14 files)
Takeoff packages, items, types, classification systems, and project settings.

- How-to: [Extract Inventory](how-to-docs/takeoff-takeoff-extract-inventory.md)
- HTTP: [GET Packages](http-docs/http-takeoff-projects-project_id-packages-GET.md), [GET Takeoff Items](http-docs/http-takeoff-projects-project_id-packages-package_id-takeoff-items-GET.md), [GET Classification Systems](http-docs/http-takeoff-projects-project_id-classification-systems-GET.md), and 10 more.

### Transmittals (~5 files)
List and retrieve transmittals, their documents, folders, and recipients.

- HTTP: [List Transmittals](http-docs/http-transmittals-listtransmittals-GET.md), [Get Transmittal](http-docs/http-transmittals-gettransmittal-GET.md), [List Documents](http-docs/http-transmittals-listtransmittaldocuments-GET.md), and 2 more.

### Photos & AutoSpecs (~6 files)
Photo retrieval and AutoSpecs smart register/version summary metadata.

- How-to: [Retrieve Smart Register](how-to-docs/autospecs-retrieve-smart-register.md)
- HTTP: [Get Filtered Photos](http-docs/http-photos-getfilteredphotos-POST.md), [Get Photo](http-docs/http-photos-getphoto-GET.md), [Get Project Metadata](http-docs/http-autospecs-getprojectmetadata-GET.md), and 3 more.

### Packages (~2 files)
List document packages and their resources within a project.

- HTTP: [List Packages](http-docs/http-packages-list-packages-GET.md), [List Package Resources](http-docs/http-packages-list-package-resources-GET.md)
<!-- GENERATED:CONTENT_SUMMARY:END -->
