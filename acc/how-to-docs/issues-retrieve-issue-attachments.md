# Retrieve Issue Attachments

Source: https://aps.autodesk.com/en/docs/acc/tutorials/issues/retrieve-issue-attachments/

---

# Retrieve Issue Attachments

This tutorial demonstrates how to retrieve information about attachments associated with issues in a Forma project. The steps include finding issues in a project and retrieving attachment information for a specific issue.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with the `data:read` scope.
- Verify that you have access to the relevant hub and Forma project.
- Find the relevant project ID for the project containing issues with attachments by following the [Retrieve a Forma Hub and Project ID](getting-started-retrieve-account-and-project-id.md) tutorial. In this example, assume the project ID is `b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5`.

## [Step 1: Find Issues in Project](#step-1-find-issues-in-project)

Find issues in your project by calling [GET issues](../http-docs/http-issues-issues-GET.md) using the project ID (`b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5`).

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

Note the ID of the issue for which you want to retrieve attachments. In this example, we’ll use the first issue (`d4f9c2e1-3b8a-4c7d-9e2f-1a5b8c9d0e3f`) which has 3 attachments (`attachmentCount: 3`).

## [Step 2: Retrieve Attachments for a Specific Issue](#step-2-retrieve-attachments-for-a-specific-issue)

Retrieve information about all attachments associated with a specific issue by calling [GET attachments](../http-docs/http-issues-attachments-issueId-items-GET.md) using the project ID (`b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5`) and the issue ID (`d4f9c2e1-3b8a-4c7d-9e2f-1a5b8c9d0e3f`).

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
      "storageUrn": "urn:adsk.objects:os.object:issues-b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5/a9d330bc-411f-4aaf-874a-9844cc002d00.pdf",
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
      "storageUrn": "urn:adsk.objects:os.object:issues-b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5/f2e8c4a6-7b9d-4e1f-8c3a-5d7f9b2e6c8a.jpg",
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
      "storageUrn": "urn:adsk.objects:os.object:issues-b8c45fe1-2ab3-4b71-8563-d9f9c5c2a7e5/c7b5e9f3-2a4d-4f8c-9e1b-6d3a8f5c2e7b.pdf",
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

Congratulations! You have successfully retrieved attachment information for an issue in Forma. You can use this information to display attachment details, check file sizes, or prepare for downloading specific attachments.
