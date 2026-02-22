# APS ACC Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Getting Started
Guides for initial setup, access management, and retrieving key identifiers. See [Manage Access to ACC](how-to-docs/getting-started-manage-access-to-acc.md) and [Retrieve Account & Project ID](how-to-docs/getting-started-retrieve-account-and-project-id.md).

### Admin, Projects, Companies & Users (~30 HTTP endpoints + 1 how-to)
Project creation/configuration, user and role management, company administration, and bulk import.
- How-to: [Create & Configure Projects](how-to-docs/admin-admin-create-configure-projects.md)
- HTTP: [GET Projects](http-docs/http-admin-accounts-accountidprojects-GET.md), [POST Project Users](http-docs/http-admin-projects-project-Id-users-POST.md), [Import Users (v2)](http-docs/http-admin-v2-projects-project-Id-users-import-POST.md), [GET Companies](http-docs/http-companies-GET.md), [GET Business Units](http-docs/http-business_units_structure-GET.md), and 25 more.

### Cost Management (~100+ HTTP endpoints + 12 how-tos)
Full cost control lifecycle: budgets, contracts, PCOs, change orders, expenses, payments, schedule of values, time sheets, performance tracking, and external integrations.
- How-to: [Create PCO](how-to-docs/cost-create-pco.md), [Track Budget Performance](how-to-docs/cost-cost-track-aggregated-budget-performance.md), [Link Budgets & Contracts](how-to-docs/cost-link-budgets-and-contract-new.md), [Integrate with External System](how-to-docs/cost-integrate-with-external-system.md), and 8 more.
- HTTP: [GET Budgets](http-docs/http-cost-budgets-GET.md), [GET Contracts](http-docs/http-cost-contracts-GET.md), [GET Change Orders](http-docs/http-cost-change-orders-GET.md), [GET Expenses](http-docs/http-cost-expenses-GET.md), [GET Time Sheets](http-docs/http-cost-time-sheets-GET.md), and 95+ more endpoints.

### Issues (~22 files)
Create, retrieve, and manage construction issues with attachments, comments, references, and member/role lookups.
- How-to: [Create Issues](how-to-docs/issues-create-issues.md), [Retrieve Issues](how-to-docs/issues-retrieve-issues.md), [Upload Attachments](how-to-docs/issues-upload-issue-attachments.md), and 5 more.
- HTTP: [GET Issues](http-docs/http-issues-issues-GET.md), [POST Issues](http-docs/http-issues-issues-POST.md), [PATCH Issue](http-docs/http-issues-issues-issueId-PATCH.md), [GET Issue Types](http-docs/http-issues-issue-types-GET.md), and 10 more endpoints.

### RFIs (~20 files)
Full RFI lifecycle: creation, responses, comments, transitions, and file attachments.
- How-to: [Create RFI](how-to-docs/rfis3-rfi-create.md), [Official Response](how-to-docs/rfis3-rfi-official-response.md), [RFI Transitions](how-to-docs/rfis3-rfi-transitions.md), and 2 more.
- HTTP: [POST RFIs](http-docs/http-rfis-rfis-POST.md), [GET RFI](http-docs/http-rfis-rfis-id-GET.md), [POST Response](http-docs/http-rfis-rfis-id-responses-POST.md), and 12 more endpoints.

### Assets (~22 files)
Asset lifecycle management with categories, custom attributes, and status step sets.
- How-to: [Manage Assets](how-to-docs/assets-manage-assets.md), [Create Project Settings](how-to-docs/assets-create-assets-project-settings.md), [Retrieve Assets Data](how-to-docs/assets-retrieve-assets-data.md).
- HTTP: [GET Assets](http-docs/http-assets-assets-v2-GET.md), [Batch Create Assets](http-docs/http-assets-assets-batch-create-POST-v2.md), [GET Categories](http-docs/http-assets-categories-GET.md), and 15 more endpoints.

### Files & Document Management (~14 files)
Document upload/download via S3, PDF export, linked files, folder permissions, and custom attribute definitions.
- How-to: [Upload Document](how-to-docs/files-upload-document-s3.md), [Download Document](how-to-docs/files-download-document-s3.md), [Export PDF](how-to-docs/files-export-pdf-files.md), [RCM Linked Files](how-to-docs/files-rcm-linked-files.md).
- HTTP: [GET Linked Files](http-docs/http-rcm-linked-files-GET.md), [POST Export PDF](http-docs/http-v1-files-export-pdf-files-POST.md), folder permission batch endpoints, and custom attribute definitions.

### Forms (~8 files)
Form and template management with location-based filtering.
- How-to: [Create & Update Forms](how-to-docs/forms-create-update-forms.md), [Retrieve Forms](how-to-docs/forms-retrieve-forms.md), [Forms by Location](how-to-docs/forms-retrieve-forms-based-on-locations.md).
- HTTP: [GET Forms](http-docs/http-forms-forms-GET.md), [POST Forms](http-docs/http-forms-forms-POST.md), [GET Form Templates](http-docs/http-forms-form-templates-GET.md), and 2 more.

### Sheets (~25 files)
Sheet upload, export, version sets, review workflow, storage, and thumbnail management.
- How-to: [Upload Sheets](how-to-docs/sheets-upload-sheets.md), [Export Sheets](how-to-docs/sheets-export-sheets.md).
- HTTP: [GET Sheets](http-docs/http-sheets-sheets-GET.md), [POST Exports](http-docs/http-sheets-exports-POST.md), [GET Version Sets](http-docs/http-sheets-version-sets-GET.md), and 20 more endpoints.

### Submittals (~30 files)
Full submittal workflow: items, packages, specs, responses, revisions, tasks, transitions, and attachments.
- How-to: [Create Submittal Item](how-to-docs/submittals-create-submittal-item.md), [Attach Files](how-to-docs/submittals-attach-files-tool.md), [Download Attachments](how-to-docs/submittals-download-submittal-attachements.md), and 2 more.
- HTTP: [GET Items](http-docs/http-submittals-items-GET.md), [GET Packages](http-docs/http-submittals-packages-GET.md), [GET Specs](http-docs/http-submittals-specs-GET.md), [GET Tasks](http-docs/http-submittals-tasks-GET.md), and 22 more endpoints.

### Reviews (~13 files)
Review and approval workflow creation, progress tracking, and version approval status.
- How-to: [Create Review](how-to-docs/reviews-reviews-create-review.md), [Create Workflow](how-to-docs/reviews-reviews-create-workflow.md), [Query Review Resources](how-to-docs/reviews-reviews-query-review-resources.md).
- HTTP: [POST Create Review](http-docs/http-reviews-createreview-POST.md), [GET Review Progress](http-docs/http-reviews-getreviewprogress-GET.md), [GET Workflows](http-docs/http-reviews-workflows-GET.md), and 7 more endpoints.

### Locations (~5 files)
Location tree configuration and hierarchical node management.
- How-to: [Configure Locations Tree](how-to-docs/locations-configure-locations-tree.md).
- HTTP: [GET Nodes](http-docs/http-locations-nodes-GET.md), [POST Nodes](http-docs/http-locations-nodes-POST.md), [PATCH Node](http-docs/http-locations-nodesnodeid-PATCH.md), [DELETE Node](http-docs/http-locations-nodesnodeid-DELETE.md).

### Relationships (~11 files)
Cross-domain relationship creation, search, sync, and intersection queries.
- How-to: [Create Relationships](how-to-docs/relationships-relationships-create.md), [Relationships Tutorial](how-to-docs/relationships-relationships-tutorial.md).
- HTTP: [PUT Add Relationships](http-docs/http-relationship-service-v2-add-relationships-PUT.md), [GET Search Relationships](http-docs/http-relationship-service-v2-search-relationships-GET.md), [POST Intersect](http-docs/http-relationship-service-v2-intersect-relationships-POST.md), and 6 more endpoints.

### Model Coordination (~46 files)
Model set lifecycle (versions, views, issues, screenshots) and clash detection (groups, tests, intersections).
- How-to: [Clash Tutorial](how-to-docs/model-coordination-mc-tutorial-clash.md), [Model Set Tutorial](how-to-docs/model-coordination-mc-tutorial-model-set.md).
- HTTP: [GET Model Sets](http-docs/http-mc-modelset-service-v3-get-model-sets-GET.md), [Create Model Set](http-docs/http-mc-modelset-service-v3-create-model-set-POST.md), [GET Clash Test](http-docs/http-mc-clash-service-v3-get-clash-test-GET.md), [GET Grouped Clashes](http-docs/http-mc-clash-service-v3-get-grouped-clashes-GET.md), and 40+ more endpoints.

### Model Properties & Index (~19 files)
BIM model property querying, diffing, and indexing across versions.
- How-to: [Query Model Properties](how-to-docs/model-properties-query.md), [Diff Model Properties](how-to-docs/model-properties-diff.md), [Query Reference](how-to-docs/model-properties-query-ref.md).
- HTTP: [POST Index Query](http-docs/http-index-v2-index-query-post.md), [POST Diff Query](http-docs/http-index-v2-diff-query-post.md), [GET Index Fields](http-docs/http-index-v2-index-fields-get.md), and 13 more endpoints.

### Data Connector (~13 files)
Automated data extraction: submitting requests, monitoring jobs, and downloading extracted data.
- How-to: [Submit Data Request](how-to-docs/data-connector-dc-tutorial-submit-data-request.md), [Retrieve Data Extract](how-to-docs/data-connector-dc-tutorial-retrieve-data-extract.md), [Find & Update Request](how-to-docs/data-connector-dc-tutorial-find-update-data-request.md).
- HTTP: [POST Requests](http-docs/http-data-connector-requests-POST.md), [GET Jobs](http-docs/http-data-connector-jobs-GET.md), [GET Job Data](http-docs/http-data-connector-jobs-jobId-data-listing-GET.md), and 7 more endpoints.

### Takeoff (~14 files)
Quantity takeoff package management and classification system configuration.
- How-to: [Extract Takeoff Inventory](how-to-docs/takeoff-takeoff-extract-inventory.md).
- HTTP: [GET Packages](http-docs/http-takeoff-projects-project_id-packages-GET.md), [GET Classification Systems](http-docs/http-takeoff-projects-project_id-classification-systems-GET.md), [GET Takeoff Items](http-docs/http-takeoff-projects-project_id-packages-package_id-takeoff-items-GET.md), and 10 more endpoints.

### AutoSpecs, Photos, Transmittals & Packages (~14 files)
- **AutoSpecs** (5 files): Smart register and spec version metadata. How-to: [Retrieve Smart Register](how-to-docs/autospecs-retrieve-smart-register.md). HTTP: [GET Smart Register](http-docs/http-autospecs-getversionsmartregister-GET.md) and 3 more.
- **Photos** (2 files): Photo search and retrieval. HTTP: [POST Filtered Photos](http-docs/http-photos-getfilteredphotos-POST.md), [GET Photo](http-docs/http-photos-getphoto-GET.md).
- **Transmittals** (5 files): List transmittals, documents, folders, and recipients. HTTP: [GET Transmittals](http-docs/http-transmittals-listtransmittals-GET.md) and 4 more listing endpoints.
- **Packages** (2 files): HTTP: [GET Packages](http-docs/http-packages-list-packages-GET.md), [GET Package Resources](http-docs/http-packages-list-package-resources-GET.md).
<!-- GENERATED:CONTENT_SUMMARY:END -->
