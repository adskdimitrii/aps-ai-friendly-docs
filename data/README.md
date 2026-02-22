# APS Data Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### How-To Guides — Data & File Operations

Practical tutorials for common data workflows using the APS Data Management and OSS APIs. Covers the full file lifecycle: creating app-managed buckets, uploading, downloading, attaching files, and publishing models to BIM 360/ACC.

- [App-Managed Bucket](how-to-docs/app-managed-bucket.md)
- [Upload File](how-to-docs/upload-file.md)
- [Download File](how-to-docs/download-file.md)
- [Create Attachment](how-to-docs/create-attachment.md)
- [Delete and Restore File](how-to-docs/delete-and-restore-file.md)
- [Publish Model](how-to-docs/publish-model.md)

---

### OSS — Buckets & Objects

HTTP reference for the Object Storage Service (OSS) API. Covers full CRUD on buckets and objects, S3-accelerated upload/download flows (signed URLs, batch operations, resumable uploads), and object copy/status endpoints. 23 files total.

- [GET /buckets](http-docs/http-buckets-GET.md) — list buckets
- [POST /buckets](http-docs/http-buckets-POST.md) — create bucket
- [DELETE /buckets/:bucketKey](http-docs/http-buckets--bucketKey-DELETE.md)
- [PUT /buckets/:bucketKey/objects/:objectKey](http-docs/http-buckets--bucketKey-objects--objectKey-PUT.md)
- [GET /buckets/:bucketKey/objects/:objectKey/signeds3download](http-docs/http-buckets--bucketKey-objects--objectKey-signeds3download-GET.md)
- [POST /buckets/:bucketKey/objects/:objectKey/batchsigneds3upload](http-docs/http-buckets--bucketKey-objects--objectKey-batchsigneds3upload-POST.md)
- [POST /buckets/:bucketKey/objects/:objectKey/batchcompleteupload](http-docs/http-buckets--bucketKey-objects--objectKey-batchcompleteupload-POST.md)
- Plus 16 additional object/bucket endpoints (details, resumable, copy, status, signed resources)

---

### OSS — Signed Resources

HTTP reference for managing public signed resource URLs (GET, PUT, DELETE, resumable PUT). 4 files.

- [GET /signedresources/:id](http-docs/http-signedresources--id-GET.md)
- [PUT /signedresources/:id](http-docs/http-signedresources--id-PUT.md)
- [DELETE /signedresources/:id](http-docs/http-signedresources--id-DELETE.md)
- [PUT /signedresources/:id/resumable](http-docs/http-signedresources--id-resumable-PUT.md)

---

### Data Management — Hubs & Projects

HTTP reference for navigating the hub/project hierarchy. Lists hubs, retrieves project details, and fetches top-level folders. 6 files.

- [GET /hubs](http-docs/http-hubs-GET.md)
- [GET /hubs/:hub_id/projects](http-docs/http-hubs-hub_id-projects-GET.md)
- [GET /hubs/:hub_id/projects/:project_id](http-docs/http-hubs-hub_id-projects-project_id-GET.md)
- [GET /hubs/:hub_id/projects/:project_id/topFolders](http-docs/http-hubs-hub_id-projects-project_id-topFolders-GET.md)

---

### Data Management — Folders

HTTP reference for folder operations within a project: create, read, update, list contents, search, navigate to parent, and manage refs/relationships. 10 files.

- [POST /projects/:project_id/folders](http-docs/http-projects-project_id-folders-POST.md)
- [GET /projects/:project_id/folders/:folder_id/contents](http-docs/http-projects-project_id-folders-folder_id-contents-GET.md)
- [GET /projects/:project_id/folders/:folder_id/search](http-docs/http-projects-project_id-folders-folder_id-search-GET.md)
- [POST /projects/:project_id/folders/:folder_id/relationships/refs](http-docs/http-projects-project_id-folders-folder_id-relationships-refs-POST.md)
- Plus 6 additional folder relationship, parent, refs, and links endpoints

---

### Data Management — Items

HTTP reference for item (file node) operations: create, read, update, navigate to parent/tip version, list versions, and manage refs/relationships. 10 files.

- [POST /projects/:project_id/items](http-docs/http-projects-project_id-items-POST.md)
- [GET /projects/:project_id/items/:item_id](http-docs/http-projects-project_id-items-item_id-GET.md)
- [PATCH /projects/:project_id/items/:item_id](http-docs/http-projects-project_id-items-item_id-PATCH.md)
- [GET /projects/:project_id/items/:item_id/tip](http-docs/http-projects-project_id-items-item_id-tip-GET.md)
- [GET /projects/:project_id/items/:item_id/versions](http-docs/http-projects-project_id-items-item_id-versions-GET.md)
- Plus 5 additional refs, relationships, and parent endpoints

---

### Data Management — Versions

HTTP reference for version operations: create, read, update, retrieve download formats, list downloads, navigate to parent item, and manage refs/relationships. 10 files.

- [POST /projects/:project_id/versions](http-docs/http-projects-project_id-versions-POST.md)
- [GET /projects/:project_id/versions/:version_id](http-docs/http-projects-project_id-versions-version_id-GET.md)
- [GET /projects/:project_id/versions/:version_id/downloadFormats](http-docs/http-projects-project_id-versions-version_id-downloadFormats-GET.md)
- [GET /projects/:project_id/versions/:version_id/item](http-docs/http-projects-project_id-versions-version_id-item-GET.md)
- Plus 6 additional download, refs, and relationship endpoints

---

### Data Management — Downloads & Storage

HTTP reference for initiating file downloads, polling download job status, creating storage locations, and retrieving job status. 4 files.

- [POST /projects/:project_id/downloads](http-docs/http-projects-project_id-downloads-POST.md)
- [GET /projects/:project_id/downloads/:download_id](http-docs/http-projects-project_id-downloads-download_id-GET.md)
- [POST /projects/:project_id/storage](http-docs/http-projects-project_id-storage-POST.md)
- [GET /projects/:project_id/jobs/:job_id](http-docs/http-projects-project_id-jobs-job_id-GET.md)

---

### Model Publishing (ACC / BIM 360)

HTTP reference for the model publishing workflow in ACC/BIM 360: check permissions, publish models (with or without links), list items and refs, and poll publish job status. 6 files.

- [POST /publish (PublishModel)](http-docs/http-PublishModel.md)
- [POST /publish (PublishWithoutLinks)](http-docs/http-PublishWithoutLinks.md)
- [GET /publish job status](http-docs/http-GetPublishModelJob.md)
- [GET /checkPermission](http-docs/http-CheckPermission.md)
- [GET /listItems](http-docs/http-ListItems.md)
- [GET /listRefs](http-docs/http-ListRefs.md)
<!-- GENERATED:CONTENT_SUMMARY:END -->
