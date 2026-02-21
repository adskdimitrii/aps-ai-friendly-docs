# projects/{projectId}/attachments

Source: https://aps.autodesk.com/en/docs/acc/reference/http/issues-attachments-POST/

---

Issue Attachments

POST

# projects/{projectId}/attachments

Adds attachments to an existing issue.

Links one or more files in Autodesk Docs (uploaded via the Data Management OSS API) to the specified issue.

Note that an issue can have up to 100 attachments. Files can include images, PDFs, or other supported formats.

For more information about uploading attachments, see the [Upload Issue Attachment](/en/docs/acc/v1/tutorials/issues/upload-issue-attachments/) tutorial.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/issues/v1/projects/{projectId}/attachments |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

The body content.

Expand all

| domainEntityId   string: UUID | The unique identifier of the issue to which the attachments will be added. |
| --- | --- |
| attachments*   array: object | A list of attachments to add to the issue. |
| attachmentId*   string: UUID | The unique identifier for the attachment, set by the client when creating the attachment reference. This can be any unique GUID, but it is recommended to use the OSS storage GUID. For more information, see the [Upload Issue Attachment](/en/docs/acc/v1/tutorials/issues/upload-issue-attachments/) tutorial. |
| displayName*   string | The human-readable display name for the attachment, including the file extension (for example, `.pdf`, `.jpg`, `.dwg`). This name appears in the ACC web UI and is used when downloading the file from the issue. |
| fileName*   string | The unique filename of the attachment, typically formatted as {attachmentId}.{fileExtension}. <br>This value must exactly match the name of the file stored in Autodesk Docs (OSS) that you uploaded via the OSS process.<br>For more information, see the [Upload Issue Attachment](/en/docs/acc/v1/tutorials/issues/upload-issue-attachments/) tutorial. |
| attachmentType*   enum:string | The type of attachment to create. Set to `issue-attachment`. Will always be: `issue-attachment` |
| storageUrn*   string | The Object Storage Service (OSS) URN that uniquely identifies where the file is stored in Autodeskâs cloud infrastructure. You obtain this value after uploading the file to OSS (see the [Upload Issue Attachment](/en/docs/acc/v1/tutorials/issues/upload-issue-attachments/) tutorial) or by retrieving it from an existing attachment (see the [Downloading Issue Attachments](/en/docs/acc/v1/tutorials/issues/download-issue-attachments/) tutorial). |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | OK |
| --- | --- |
| 400   Bad Request | Invalid input |
| 403   Forbidden | The request is valid but lacks the necessary permissions. |
| 404   Not Found | Project not found |
| 409   Conflict | Conflict - one or more attachments already exist in the document service |
| 422   Unprocessable Entity | The limit of 100 attachments per issue has been reached |
| 500   Internal Server Error | Internal server error |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| attachments   array: object | A collection of attachments linked to the issue. |
| --- | --- |
| attachmentId   string: UUID | The unique identifier for the attachment, set by the client when creating the attachment reference. This can be any unique GUID, but it is recommended to use the OSS storage GUID. |
| displayName   string | The human-readable display name for the attachment, including the file extension (for example, `.pdf`, `.jpg`, `.dwg`). This name appears in the ACC web UI and is used when downloading the file from the issue. |
| fileName   string | The unique filename of the attachment, as stored in Autodesk Docs (OSS). This is the name assigned to the uploaded file in the system, typically formatted as {attachmentId}.{fileExtension}. |
| attachmentType   enum:string | The type of attachment. For issue attachments, this value is always `issue-attachment`. Will always be: `issue-attachment` |
| storageUrn   string | The Object Storage Service (OSS) URN identifying where the attachment file is stored in Autodeskâs cloud infrastructure. Use this value when downloading the file (see the Download Issue Attachment </en/docs/acc/v1/tutorials/issues/download-issue-attachments/>_ tutorial). |
| fileSize   int | The size of the file in bytes. |
| fileType   string | The file extension (without the dot), for example `pdf` or `jpg`. |
| domainEntityId   string: UUID | The ID of the issue that owns the attachment. |
| lineageUrn   string | The document lineage URN for the attachmentâs source file. |
| version   int | The document version number. |
| versionUrn   string | The URN for the specific file version that was attached to the issue. This may differ from the latest version URN (`tipVersionUrn`) if a newer version of the file exists in Autodesk Docs. |
| tipVersionUrn   string | The URN for the latest (tip) version of the file. |
| bubbleUrn   string | Not relevant |
| createdBy   string | The ID of the user who created the issue attachment. For details about the user, call [GET users](/en/docs/acc/v1/reference/http/admin-projectsprojectId-users-GET/). |
| createdOn   datetime: ISO 8601 | The date and time when the issue attachment was created, in ISO8601 format. |
| modifiedBy   string | Not relevant |
| modifiedOn   datetime: ISO 8601 | Not relevant |
| deletedBy   string | The ID of the user who deleted the issue attachment, if applicable. For details about the user, call [GET users](/en/docs/acc/v1/reference/http/admin-projectsprojectId-users-GET/). |
| deletedOn   datetime: ISO 8601 | The date and time when the issue attachment was deleted, if applicable. |
| isDeleted   boolean | `true`: The attachment has been deleted. <br>`false`: (default) The attachment has not been deleted. |

## [Example](#example)

OK

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/:projectId/attachments' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "domainEntityId": "be9ade84-e25d-412a-a08c-f5f14cf04957",
        "attachments": [
          {
            "attachmentId": "aea9f035-b63a-4e46-884d-3016454507e2",
            "displayName": "myfile.pdf",
            "fileName": "aea9f035-b63a-4e46-884d-3016454507e2.pdf",
            "attachmentType": "issue-attachment",
            "storageUrn": "urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b.jpg"
          }
        ]
      }'

```

Show More

### Response

```
{
  "attachments": [
    {
      "attachmentId": "aea9f035-b63a-4e46-884d-3016454507e2",
      "displayName": "myfile.pdf",
      "fileName": "aea9f035-b63a-4e46-884d-3016454507e2.pdf",
      "attachmentType": "issue-attachment",
      "storageUrn": "urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b.jpg",
      "fileSize": 1000000,
      "fileType": "png",
      "domainEntityId": "20c71442-d5b2-480b-9051-0ba108b62bb9",
      "lineageUrn": "urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ",
      "version": 32,
      "versionUrn": "urn:adsk.wipprod:fs.file:vf.1HROnsnfQgq4N0b-nUoGge?version=2",
      "tipVersionUrn": "urn:adsk.wipprod:fs.file:vf.1HROnsnfQgq4N0b-nUoGge?version=2",
      "bubbleUrn": "urn:adsk.objects:os.object:modelderivative/building.rvt",
      "createdBy": "A3RGM375QTZ7",
      "createdOn": "2018-07-22T15:05:58.033Z",
      "modifiedBy": "A3RGM375QTZ7",
      "modifiedOn": "2018-07-22T15:05:58.033Z",
      "deletedBy": "A3RGM375QTZ7",
      "deletedOn": "2018-07-22T15:05:58.033Z",
      "isDeleted": false
    }
  ]
}

```

Show More
