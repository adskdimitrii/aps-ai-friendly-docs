# APS Data Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### File & Object Management (How-To Guides)

Six practical tutorials covering common data operations with the APS OSS and Data Management APIs.

- [App-Managed Bucket](how-to-docs/app-managed-bucket.md) — create and configure an application-owned OSS bucket
- [Upload File](how-to-docs/upload-file.md) — upload objects to OSS storage
- [Download File](how-to-docs/download-file.md) — retrieve objects from OSS
- [Delete and Restore File](how-to-docs/delete-and-restore-file.md) — soft-delete and restore files
- [Create Attachment](how-to-docs/create-attachment.md) — attach files to project items
- [Publish Model](how-to-docs/publish-model.md) — trigger model publishing/translation

### Object Storage Service (OSS)

Low-level bucket and object operations including direct upload/download, S3-accelerated multipart transfers, resumable uploads, and signed resource URLs. 23 HTTP reference files.

**Buckets (4 files):**
- [GET /buckets](http-docs/http-buckets-GET.md), [POST /buckets](http-docs/http-buckets-POST.md), [GET /buckets/:bucketKey/details](http-docs/http-buckets--bucketKey-details-GET.md), [DELETE /buckets/:bucketKey](http-docs/http-buckets--bucketKey-DELETE.md)

**Objects (15 files):**
- [GET /objects](http-docs/http-buckets--bucketKey-objects-GET.md) — list objects in bucket
- [GET /objects/:objectKey](http-docs/http-buckets--bucketKey-objects--objectKey-GET.md) — download object
- [PUT /objects/:objectKey](http-docs/http-buckets--bucketKey-objects--objectKey-PUT.md) — single-part upload
- [PUT …/resumable](http-docs/http-buckets--bucketKey-objects--objectKey-resumable-PUT.md) — resumable upload
- [PUT …/copyto/:newObjectKey](http-docs/http-buckets--bucketKey-objects--objectKey-copyto--newObjectKey-PUT.md) — copy object
- [DELETE /objects/:objectKey](http-docs/http-buckets--bucketKey-objects--objectKey-DELETE.md)
- S3-accelerated: [GET signeds3upload](http-docs/http-buckets--bucketKey-objects--objectKey-signeds3upload-GET.md), [POST batchsigneds3upload](http-docs/http-buckets--bucketKey-objects--objectKey-batchsigneds3upload-POST.md), [POST batchcompleteupload](http-docs/http-buckets--bucketKey-objects--objectKey-batchcompleteupload-POST.md), [GET signeds3download](http-docs/http-buckets--bucketKey-objects--objectKey-signeds3download-GET.md), [POST batchsigneds3download](http-docs/http-buckets--bucketKey-objects-batchsigneds3download-POST.md), [POST signeds3upload](http-docs/http-buckets--bucketKey-objects--objectKey-signeds3upload-POST.md), [GET status/:sessionId](http-docs/http-buckets--bucketKey-objects--objectKey-status--sessionId-GET.md), [GET details](http-docs/http-buckets--bucketKey-objects--objectKey-details-GET.md), [POST signed](http-docs/http-buckets--bucketKey-objects--objectKey-signed-POST.md)

**Signed Resources (4 files):**
- [GET](http-docs/http-signedresources--id-GET.md), [PUT](http-docs/http-signedresources--id-PUT.md), [PUT resumable](http-docs/http-signedresources--id-resumable-PUT.md), [DELETE](http-docs/http-signedresources--id-DELETE.md) `/signedresources/:id`

### Model Publishing

Endpoints for triggering and monitoring model publishing jobs within a project. 6 HTTP reference files.

- [POST PublishModel](http-docs/http-PublishModel.md), [POST PublishWithoutLinks](http-docs/http-PublishWithoutLinks.md) — initiate publish
- [GET GetPublishModelJob](http-docs/http-GetPublishModelJob.md) — poll job status
- [GET ListItems](http-docs/http-ListItems.md), [GET ListRefs](http-docs/http-ListRefs.md) — enumerate publishable content
- [POST CheckPermission](http-docs/http-CheckPermission.md) — verify publish permissions

### Hubs & Projects

Navigation endpoints for discovering hubs (BIM 360, ACC, Fusion Team) and their projects. 6 HTTP reference files.

- [GET /hubs](http-docs/http-hubs-GET.md) — list accessible hubs
- [GET /hubs/:hub_id](http-docs/http-hubs-hub_id-GET.md), [GET /hubs/:hub_id/projects](http-docs/http-hubs-hub_id-projects-GET.md)
- [GET /projects/:project_id](http-docs/http-hubs-hub_id-projects-project_id-GET.md), [GET …/hub](http-docs/http-hubs-hub_id-projects-project_id-hub-GET.md)
- [GET …/topFolders](http-docs/http-hubs-hub_id-projects-project_id-topFolders-GET.md) — entry points into folder tree

### Folders

Folder CRUD, traversal, search, and relationship management within a project. 10 HTTP reference files.

- [POST /folders](http-docs/http-projects-project_id-folders-POST.md) — create folder
- [GET /folders/:folder_id](http-docs/http-projects-project_id-folders-folder_id-GET.md), [PATCH](http-docs/http-projects-project_id-folders-folder_id-PATCH.md) — read/update
- [GET …/contents](http-docs/http-projects-project_id-folders-folder_id-contents-GET.md), [GET …/search](http-docs/http-projects-project_id-folders-folder_id-search-GET.md), [GET …/parent](http-docs/http-projects-project_id-folders-folder_id-parent-GET.md)
- Relationships (4 files): [refs GET](http-docs/http-projects-project_id-folders-folder_id-refs-GET.md), [relationships/refs GET](http-docs/http-projects-project_id-folders-folder_id-relationships-refs-GET.md) & [POST](http-docs/http-projects-project_id-folders-folder_id-relationships-refs-POST.md), [relationships/links GET](http-docs/http-projects-project_id-folders-folder_id-relationships-links-GET.md)

### Items

Item CRUD and relationship management (items represent the latest version of a file in a project). 10 HTTP reference files.

- [POST /items](http-docs/http-projects-project_id-items-POST.md) — create item
- [GET /items/:item_id](http-docs/http-projects-project_id-items-item_id-GET.md), [PATCH](http-docs/http-projects-project_id-items-item_id-PATCH.md) — read/update
- [GET …/tip](http-docs/http-projects-project_id-items-item_id-tip-GET.md) — latest version, [GET …/versions](http-docs/http-projects-project_id-items-item_id-versions-GET.md) — version history
- [GET …/parent](http-docs/http-projects-project_id-items-item_id-parent-GET.md)
- Relationships (4 files): [refs GET](http-docs/http-projects-project_id-items-item_id-refs-GET.md), [relationships/refs GET](http-docs/http-projects-project_id-items-item_id-relationships-refs-GET.md) & [POST](http-docs/http-projects-project_id-items-item_id-relationships-refs-POST.md), [relationships/links GET](http-docs/http-projects-project_id-items-item_id-relationships-links-GET.md)

### Versions & Downloads

Version management, download format queries, storage provisioning, and job polling. 14 HTTP reference files.

- [POST /versions](http-docs/http-projects-project_id-versions-POST.md) — create new version
- [GET /versions/:version_id](http-docs/http-projects-project_id-versions-version_id-GET.md), [PATCH](http-docs/http-projects-project_id-versions-version_id-PATCH.md) — read/update
- [GET …/downloadFormats](http-docs/http-projects-project_id-versions-version_id-downloadFormats-GET.md), [GET …/downloads](http-docs/http-projects-project_id-versions-version_id-downloads-GET.md), [GET …/item](http-docs/http-projects-project_id-versions-version_id-item-GET.md)
- Relationships (4 files): [refs GET](http-docs/http-projects-project_id-versions-version_id-refs-GET.md), [relationships/refs GET](http-docs/http-projects-project_id-versions-version_id-relationships-refs-GET.md) & [POST](http-docs/http-projects-project_id-versions-version_id-relationships-refs-POST.md), [relationships/links GET](http-docs/http-projects-project_id-versions-version_id-relationships-links-GET.md)
- Storage & jobs: [POST /storage](http-docs/http-projects-project_id-storage-POST.md), [POST /downloads](http-docs/http-projects-project_id-downloads-POST.md), [GET /downloads/:download_id](http-docs/http-projects-project_id-downloads-download_id-GET.md), [GET /jobs/:job_id](http-docs/http-projects-project_id-jobs-job_id-GET.md)
<!-- GENERATED:CONTENT_SUMMARY:END -->
