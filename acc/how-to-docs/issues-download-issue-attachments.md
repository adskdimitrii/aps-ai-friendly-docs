# Download Issue Attachments

Source: https://aps.autodesk.com/en/docs/acc/tutorials/issues/download-issue-attachments/

---

# Download Issue Attachments

This tutorial demonstrates how to download attachments that were added to issues in ACC Issues. The steps include finding the issue containing the attachment you want to download, retrieving attachment information, generating a signed URL for the attachment, and using the signed URL to download the attachment.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with the `data:read` scope.
- Verify that you have access to the relevant account and ACC project.
- Find the relevant project ID for the project you want to download an attachment from. See the [Retrieve a Project ID](getting-started-retrieve-account-and-project-id.md) tutorial for more details. In this example, assume the project ID is `b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5`.

## [Step 1: Find the Issue ID](#step-1-find-the-issue-id)

Find the ID of the issue that contains the attachment you want to download by calling [GET issues](../http-docs/http-issues-issues-GET.md) using the project ID (`b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5`).

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5/issues' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 100,
    "offset": 0,
    "totalResults": 2
  },
  "results": [
    {
      "id": "d4f9c2e1-3b8a-4c7d-9e2f-1a5b8c9d0e3f",
      "containerId": "b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5",
      "displayId": 101,
      "title": "Structural beam alignment issue",
      "description": "The structural beam at grid line A-3 appears to be misaligned with the architectural drawings.",
      "status": "open",
      "issueType": "design",
      "issueSubType": "clash",
      "assignedTo": "A3RGM375QTZ7",
      "assignedToType": "user",
      "createdBy": "MFEGJ9W5GGQL",
      "createdAt": "2024-11-09T14:30:00.000Z",
      "updatedBy": "MFEGJ9W5GGQL",
      "updatedAt": "2024-11-09T15:45:30.000Z",
      "dueDate": "2024-11-20T17:00:00.000Z",
      "locationDetails": "Building A, Level 2, Grid A-3",
      "attachmentCount": 3,
      "permittedActions": ["view", "edit", "add_comment", "add_attachment"]
    },
    {
      "id": "e8a2b5f7-4d6c-4e9a-b1c3-7f2e9a8b4d6c",
      "containerId": "b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5",
      "displayId": 102,
      "title": "HVAC duct clearance concern",
      "description": "Insufficient clearance for HVAC duct installation in mechanical room.",
      "status": "in_progress",
      "issueType": "quality",
      "issueSubType": "installation",
      "assignedTo": "B5THJ486RXW9",
      "assignedToType": "user",
      "createdBy": "A3RGM375QTZ7",
      "createdAt": "2024-11-08T09:15:00.000Z",
      "updatedBy": "B5THJ486RXW9",
      "updatedAt": "2024-11-09T10:20:15.000Z",
      "dueDate": "2024-11-18T17:00:00.000Z",
      "locationDetails": "Building B, Mechanical Room 1",
      "attachmentCount": 1,
      "permittedActions": ["view", "edit", "add_comment", "add_attachment"]
    }
  ]
}

```

Show More

Note the ID of the issue that contains the attachment you want to download (`results.id`). In this example, weâll use the first issue (`d4f9c2e1-3b8a-4c7d-9e2f-1a5b8c9d0e3f`) which has 3 attachments (`attachmentCount: 3`).

## [Step 2: Find the Attachment Information](#step-2-find-the-attachment-information)

Find the specific attachment you want to download by calling [GET attachments](../http-docs/http-issues-attachments-issueId-items-GET.md) using the project ID (`b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5`) and the issue ID (`d4f9c2e1-3b8a-4c7d-9e2f-1a5b8c9d0e3f`).

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5/attachments/d4f9c2e1-3b8a-4c7d-9e2f-1a5b8c9d0e3f/items' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "attachments": [
    {
      "attachmentId": "a9d330bc-411f-4aaf-874a-9844cc002d00",
      "displayName": "Structural Plan - Level 2.pdf",
      "fileName": "a9d330bc-411f-4aaf-874a-9844cc002d00.pdf",
      "attachmentType": "issue-attachment",
      "storageUrn": "urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b.jpg",
      "fileSize": 4729968,
      "fileType": "pdf",
      "domainEntityId": "d4f9c2e1-3b8a-4c7d-9e2f-1a5b8c9d0e3f",
      "lineageUrn": "urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ",
      "version": 1,
      "versionUrn": "urn:adsk.wipprod:fs.file:vf.1HROnsnfQgq4N0b-nUoGge?version=1",
      "tipVersionUrn": "urn:adsk.wipprod:fs.file:vf.1HROnsnfQgq4N0b-nUoGge?version=1",
      "createdBy": "MFEGJ9W5GGQL",
      "createdOn": "2024-11-09T14:32:15.000Z",
      "deletedBy": null,
      "deletedOn": null,
      "isDeleted": false
    },
    {
      "attachmentId": "f2e8c4a6-7b9d-4e1f-8c3a-5d7f9b2e6c8a",
      "displayName": "Photo - Beam Alignment Issue.jpg",
      "fileName": "f2e8c4a6-7b9d-4e1f-8c3a-5d7f9b2e6c8a.jpg",
      "attachmentType": "issue-attachment",
      "storageUrn": "urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b.jpg",
      "fileSize": 2458746,
      "fileType": "jpg",
      "domainEntityId": "d4f9c2e1-3b8a-4c7d-9e2f-1a5b8c9d0e3f",
      "lineageUrn": "urn:adsk.wipprod:dm.lineage:BfZhEudTSvqYpyNxeGIjjR",
      "version": 1,
      "versionUrn": "urn:adsk.wipprod:fs.file:vf.2ISPotngRhq5O1c-oVpHhf?version=1",
      "tipVersionUrn": "urn:adsk.wipprod:fs.file:vf.2ISPotngRhq5O1c-oVpHhf?version=1",
      "createdBy": "MFEGJ9W5GGQL",
      "createdOn": "2024-11-09T14:45:22.000Z",
      "deletedBy": null,
      "deletedOn": null,
      "isDeleted": false
    },
    {
      "attachmentId": "c7b5e9f3-2a4d-4f8c-9e1b-6d3a8f5c2e7b",
      "displayName": "Specification Sheet - Steel Beam.pdf",
      "fileName": "c7b5e9f3-2a4d-4f8c-9e1b-6d3a8f5c2e7b.pdf",
      "attachmentType": "issue-attachment",
      "storageUrn": "urn:adsk.objects:os.object:wip.dm.prod/1d6d61f2-21ut-3k5h.jpg",
      "fileSize": 856432,
      "fileType": "pdf",
      "domainEntityId": "d4f9c2e1-3b8a-4c7d-9e2f-1a5b8c9d0e3f",
      "lineageUrn": "urn:adsk.wipprod:dm.lineage:CgAiGvfUSvrZpzOyfHJkkS",
      "version": 1,
      "versionUrn": "urn:adsk.wipprod:fs.file:vf.3JTQpuohSiq6P2d-pWqIig?version=1",
      "tipVersionUrn": "urn:adsk.wipprod:fs.file:vf.3JTQpuohSiq6P2d-pWqIig?version=1",
      "createdBy": "A3RGM375QTZ7",
      "createdOn": "2024-11-09T15:10:45.000Z",
      "deletedBy": null,
      "deletedOn": null,
      "isDeleted": false
    }
  ]
}

```

Show More

Find the attachment you want to download (`attachments.displayName`). In this example, weâll download the âPhoto - Beam Alignment Issue.jpgâ file. Note the corresponding storage URN (`attachments.storageUrn`) - `urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b.jpg`.

The storage URN follows the format: `urn:adsk.objects:os.object:<bucket_key>/<object_key>`

From the storage URN, extract:
- **Bucket Key**: `wip.dm.prod` - **Object Key**: `2a6d61f2-49df-4d7b.jpg`

## [Step 3: Generate a Signed S3 URL](#step-3-generate-a-signed-s3-url)

Use the bucket key (`wip.dm.prod`) and object key (`2a6d61f2-49df-4d7b.jpg`) to call [GET signeds3download](../../data/http-docs/http-buckets--bucketKey-objects--objectKey-signeds3download-GET.md) to generate a signed URL for the storage object, which you can use to download the file directly from S3.

You need to repeat this step for each attachment.

### Request

```
curl -X GET 'https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/2a6d61f2-49df-4d7b.jpg/signeds3download' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "status": "complete",
  "url": "https://cdn.us.oss.api.autodesk.com/com.autodesk.oss-persistent/us-east-1/f2/e8/c4/a67b9d4e1f8c3a5d7f9b2e6c8a/issues-b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5?response-content-type=image%2Fjpeg&response-content-disposition=attachment%3B+filename%3D%22Photo+-+Beam+Alignment+Issue.jpg%22&Expires=1699540803&Signature=xKmD2HsP9Lk4aRG2HAhOCKYl0xtqsuujMJ~VKSXm1vBa-OxS4lPQBSlTx5bswpLBe1W6Rz94eIZW2sPN-v6Mzz~JyXNZ-V9Z7zlBoE1VoQhspLioC225hxq6ZmDSU5QnZXuNDV4ih~p1n3xacYvUvQWX-ONAGVUgQvZ253Svw~qx-pO4j-Yh4kVRmzDZqQut1xOI5ZGH6JFGhXLSzkgbYcfYx6fvCxnvYUJrgAcqncIwGVewI3uC0I84Fzrj8nXE8ojuojqJP0pNlxkfBe~2LfjjzqKDKaNvfC2Grt12j9QgC~cN7nQCRcVUhExpoV1VVB5x3AkVTJ-q5NoedvsfO__&Key-Pair-Id=APKAI5JGPYQ5LGB7QA",
  "params": {
    "content-type": "image/jpeg",
    "content-disposition": "attachment; filename=\"Photo - Beam Alignment Issue.jpg\""
  },
  "size": 2458746,
  "sha1": "f2e8c4a67b9d4e1f8c3a5d7f9b2e6c8a9c1d3e5f"
}

```

Show More

Note the signed URL (`url`) and file information:
- **URL**: Use this to download the file
- **Content-Type**: `image/jpeg` indicates this is a JPEG image
- **Size**: `2458746` bytes (approximately 2.5 MB)
- **SHA1**: Hash for file integrity verification

## [Step 4: Download the File](#step-4-download-the-file)

To download the file from the signed URL, use a GET method with the `url` attribute as the URI. You can save the file to your local system with the desired filename.

**Important Notes:** - Do not include a bearer token with this request
- The signed URL expires after a short amount of time (usually 15 minutes). If the time expires you need to call GET signeds3download again to get a new download link.

### Request

```
curl -X GET "https://cdn.us.oss.api.autodesk.com/com.autodesk.oss-persistent/us-east-1/f2/e8/c4/a67b9d4e1f8c3a5d7f9b2e6c8a/issues-b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5?response-content-type=image%2Fjpeg&response-content-disposition=attachment%3B+filename%3D%22Photo+-+Beam+Alignment+Issue.jpg%22&Expires=1699540803&Signature=xKmD2HsP9Lk4aRG2HAhOCKYl0xtqsuujMJ~VKSXm1vBa-OxS4lPQBSlTx5bswpLBe1W6Rz94eIZW2sPN-v6Mzz~JyXNZ-V9Z7zlBoE1VoQhspLioC225hxq6ZmDSU5QnZXuNDV4ih~p1n3xacYvUvQWX-ONAGVUgQvZ253Svw~qx-pO4j-Yh4kVRmzDZqQut1xOI5ZGH6JFGhXLSzkgbYcfYx6fvCxnvYUJrgAcqncIwGVewI3uC0I84Fzrj8nXE8ojuojqJP0pNlxkfBe~2LfjjzqKDKaNvfC2Grt12j9QgC~cN7nQCRcVUhExpoV1VVB5x3AkVTJ-q5NoedvsfO__&Key-Pair-Id=APKAI5JGPYQ5LGB7QA" \
  --output "Photo - Beam Alignment Issue.jpg"

```

### Response

The file will be downloaded and saved to your current directory with the specified filename. The HTTP response will be 200 OK with the file content in the response body.

Congratulations! You have successfully downloaded an attachment from an ACC issue. The file is now available on your local system for viewing, sharing, or further processing.
