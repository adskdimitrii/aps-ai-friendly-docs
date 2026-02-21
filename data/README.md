# APS Data Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

This folder contains documentation for the **APS Data Management** and **Object Storage Service (OSS)** APIs, covering file storage, project/hub navigation, and model publishing. It includes 69 HTTP endpoint references and 6 how-to guides.

### Buckets & Object Storage (OSS) (~23 endpoints, 4 guides)

Core object storage operations: create and manage buckets, upload/download objects, generate S3-signed URLs, and perform batch operations.

- **Bucket management:** [Create Bucket](http-docs/http-buckets-POST.md), [List Buckets](http-docs/http-buckets-GET.md), [Get Bucket Details](http-docs/http-buckets--bucketKey-details-GET.md), [Delete Bucket](http-docs/http-buckets--bucketKey-DELETE.md)
- **Object operations:** [Upload Object](http-docs/http-buckets--bucketKey-objects--objectKey-PUT.md), [Download Object](http-docs/http-buckets--bucketKey-objects--objectKey-GET.md), [Delete Object](http-docs/http-buckets--bucketKey-objects--objectKey-DELETE.md), [Object Details](http-docs/http-buckets--bucketKey-objects--objectKey-details-GET.md), [Copy Object](http-docs/http-buckets--bucketKey-objects--objectKey-copyto--newObjectKey-PUT.md), [List Objects](http-docs/http-buckets--bucketKey-objects-GET.md)
- **S3-signed uploads/downloads:** [Signed S3 Upload (GET)](http-docs/http-buckets--bucketKey-objects--objectKey-signeds3upload-GET.md), [Signed S3 Upload (POST)](http-docs/http-buckets--bucketKey-objects--objectKey-signeds3upload-POST.md), [Batch Complete Upload](http-docs/http-buckets--bucketKey-objects--objectKey-batchcompleteupload-POST.md), [Signed S3 Download](http-docs/http-buckets--bucketKey-objects--objectKey-signeds3download-GET.md), [Batch Signed Download](http-docs/http-buckets--bucketKey-objects-batchsigneds3download-POST.md)
- **Resumable upload:** [Resumable PUT](http-docs/http-buckets--bucketKey-objects--objectKey-resumable-PUT.md), [Upload Status](http-docs/http-buckets--bucketKey-objects--objectKey-status--sessionId-GET.md)
- **Signed resources:** [GET](http-docs/http-signedresources--id-GET.md), [PUT](http-docs/http-signedresources--id-PUT.md), [DELETE](http-docs/http-signedresources--id-DELETE.md), [Resumable PUT](http-docs/http-signedresources--id-resumable-PUT.md)
- **How-to:** [Upload File](how-to-docs/upload-file.md), [Download File](how-to-docs/download-file.md), [Delete & Restore File](how-to-docs/delete-and-restore-file.md), [App-Managed Bucket](how-to-docs/app-managed-bucket.md)

### Hubs & Projects (~6 endpoints)

Navigate the Data Management hierarchy: list hubs, browse projects within hubs, and retrieve top-level folders.

- [List Hubs](http-docs/http-hubs-GET.md), [Get Hub](http-docs/http-hubs-hub_id-GET.md), [List Projects](http-docs/http-hubs-hub_id-projects-GET.md), [Get Project](http-docs/http-hubs-hub_id-projects-project_id-GET.md), [Get Project Hub](http-docs/http-hubs-hub_id-projects-project_id-hub-GET.md), [Top Folders](http-docs/http-hubs-hub_id-projects-project_id-topFolders-GET.md)

### Folders (~10 endpoints)

Full CRUD and relationship management for project folders, including content listing and search.

- [Create Folder](http-docs/http-projects-project_id-folders-POST.md), [Get Folder](http-docs/http-projects-project_id-folders-folder_id-GET.md), [Update Folder](http-docs/http-projects-project_id-folders-folder_id-PATCH.md), [Folder Contents](http-docs/http-projects-project_id-folders-folder_id-contents-GET.md), [Search Folder](http-docs/http-projects-project_id-folders-folder_id-search-GET.md), [Folder Parent](http-docs/http-projects-project_id-folders-folder_id-parent-GET.md)
- Plus 4 more endpoints for refs and relationship links.

### Items (~12 endpoints, 1 guide)

Manage items (files) within projects: CRUD operations, version history, relationships, and tip versions.

- [Create Item](http-docs/http-projects-project_id-items-POST.md), [Get Item](http-docs/http-projects-project_id-items-item_id-GET.md), [Update Item](http-docs/http-projects-project_id-items-item_id-PATCH.md), [Item Tip](http-docs/http-projects-project_id-items-item_id-tip-GET.md), [Item Versions](http-docs/http-projects-project_id-items-item_id-versions-GET.md), [List Items](http-docs/http-ListItems.md), [List Refs](http-docs/http-ListRefs.md)
- Plus 5 more endpoints for parent, refs, and relationships.
- **How-to:** [Create Attachment](how-to-docs/create-attachment.md)

### Versions (~10 endpoints)

Version management: create new versions, retrieve download formats, and manage version relationships.

- [Create Version](http-docs/http-projects-project_id-versions-POST.md), [Get Version](http-docs/http-projects-project_id-versions-version_id-GET.md), [Update Version](http-docs/http-projects-project_id-versions-version_id-PATCH.md), [Version Item](http-docs/http-projects-project_id-versions-version_id-item-GET.md), [Download Formats](http-docs/http-projects-project_id-versions-version_id-downloadFormats-GET.md), [Version Downloads](http-docs/http-projects-project_id-versions-version_id-downloads-GET.md)
- Plus 4 more endpoints for refs and relationships.

### Downloads, Storage & Jobs (~4 endpoints)

Create storage locations for file uploads, initiate downloads, and check job status.

- [Create Storage](http-docs/http-projects-project_id-storage-POST.md), [Create Download](http-docs/http-projects-project_id-downloads-POST.md), [Get Download](http-docs/http-projects-project_id-downloads-download_id-GET.md), [Get Job](http-docs/http-projects-project_id-jobs-job_id-GET.md)

### Model Publishing (~4 endpoints, 1 guide)

Publish models to make them available across APS services and check publishing permissions.

- [Publish Model](http-docs/http-PublishModel.md), [Publish Without Links](http-docs/http-PublishWithoutLinks.md), [Get Publish Job](http-docs/http-GetPublishModelJob.md), [Check Permission](http-docs/http-CheckPermission.md)
- **How-to:** [Publish Model](how-to-docs/publish-model.md)
<!-- GENERATED:CONTENT_SUMMARY:END -->
