# projects/{projectId}/sheets:batch-get

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-sheetsbatch-get-POST/

---

Sheets

POST

# projects/{projectId}/sheets:batch-get

Retrieves a list of sheets by IDs.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/sheets:batch-get |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-user-id   string | The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. <br>When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.<br>You can use either the userâs ACC ID (id), or their Autodesk ID (autodeskId). |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](../how-to-docs/getting-started-retrieve-account-and-project-id.md). You can use a project ID either with a âb.â prefix or without a âb.â prefix. For instance, a project ID of âb.a4be0c34a-4ab7â can also be referred to as âa4be0c34a-4ab7â. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

| ids*   array: string | The IDs of the sheets to retrieve. <br>The max number of items is 200. |
| --- | --- |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the list of sheets. |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 403   Forbidden | The user or client represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource cannot be found. |
| 429   Too Many Requests | The server has received too many requests. |
| 500   Internal Server Error | An unexpected error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | The list of results. |
| --- | --- |
| id   string: UUID | The ID of the sheet. |
| number   string | The number of the sheet. |
| versionSet   object | Basic version set data. For a complete collection of version set data, call [GET version-sets](http-sheets-version-sets-GET.md). |
| id   string: UUID | The ID of the version set. |
| name   string | The name of the version set. <br>Max length: 255 |
| issuanceDate   datetime: ISO 8601 | The issuance date of the version set in ISO-8601 format (YYYY-MM-DD). |
| deleted   boolean | `true` if the version set has been deleted.`false` if the version set has not been deleted. |
| createdAt   datetime: ISO 8601 | The time when the sheet was created, in ISO-8601 format (YYYY-MM-DDTHH:mm:ss.SSSZ). |
| createdBy   string | The ID of the user who created the sheet. |
| createdByName   string | The name of the user who created the sheet. |
| updatedAt   datetime: ISO 8601 | The time when the sheet was last updated, in ISO-8601 format (YYYY-MM-DDTHH:mm:ss.SSSZ). |
| updatedBy   string | The ID of the user who last updated the sheet. |
| updatedByName   string | The name of the user who last updated the sheet. |
| title   string | The title of the sheet. |
| uploadFileName   string | The name of the source file from which the sheet was generated. |
| uploadId   string: UUID | The ID of the upload that generated the sheet. |
| tags   array: string | The tags of the sheet. |
| paperSize   array: number | The size of the sheet in pixels. |
| isCurrent   boolean | `true` if the sheet is the version with the most recent issuance date. This is only relevant if you uploaded multiple versions of the same sheet that were assigned the same number. The `current` sheet is the sheet with the most recent issuance date.`false` if the sheet is not the version with the most recent issuance date. |
| deleted   boolean | `true` if the sheet has been deleted.`false` if the sheet has not been deleted. |
| deletedAt   datetime: ISO 8601 | The time when the sheet was deleted, in ISO-8601 format (YYYY-MM-DDTHH:mm:ss.SSSZ). |
| deletedBy   string | The ID of the user who deleted the sheet. |
| deletedByName   string | The name of the user who deleted the sheet. |
| viewable   object | Information about the sheet relevant for loading the sheet to the Viewer. See [Add Viewer to an HTML Page](https://forge.autodesk.com/en/docs/viewer/v7/developers_guide/viewer_basics/) for more information. |
| urn   string | The URN of the viewable resources. Multiple sheets created by the same original file may share the same viewable URN. <br>When loading the sheet to the viewer, this URN should be used as the documentId to get the manifest. |
| guid   string | The GUID of the viewable resources. <br>When loading the sheet to the viewer, this GUID should be used to find the related geometry node of the sheet. |
| collection   object | The collection object, if assigned. If no collection is assigned, this value is `null`. |
| id   string: UUID | The unique identifier of the collection. |
| name   string | The name of the collection. This corresponds to the Name column in the ACC Sheets Collections Settings UI. <br>Max length: 255 |

## [Example](#example)

Successfully retrieved the list of sheets.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/sheets:batch-get' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "ids": [
          "0d7a5883-1694-3078-a06d-ad24413f8b06"
        ]
      }'

```

Show More

### Response

```
{
  "results": [
    {
      "id": "0d7a5883-1694-3078-a06d-ad24413f8b06",
      "number": "A-01",
      "versionSet": {
        "id": "7c2ecde0-2406-49f9-9199-50176848a0b7",
        "name": "one set",
        "issuanceDate": "2021-07-01",
        "deleted": false
      },
      "createdAt": "2021-07-01T05:21:05.391Z",
      "createdBy": "45GPJ4KAX789",
      "createdByName": "John Smith",
      "updatedAt": "2021-07-01T05:21:05.391Z",
      "updatedBy": "45GPJ4KAX789",
      "updatedByName": "John Smith",
      "title": "Floor One",
      "uploadFileName": "example.pdf",
      "uploadId": "5cb5d9da-060e-421e-bca9-97dd8b5cd800",
      "tags": [
        "april",
        "floor"
      ],
      "paperSize": [
        1000,
        600
      ],
      "isCurrent": true,
      "deleted": false,
      "deletedAt": "",
      "deletedBy": "",
      "deletedByName": "",
      "viewable": {
        "urn": "urn:adsk.bimdocs:seed:207edb73-69c2-43d2-ba0e-e2ffe9fdcb56",
        "guid": "cc3eb847-737f-3408-bdbd-e2628a02b8de"
      },
      "collection": {
        "id": "619ef887-974f-45e4-9775-461e6a62d784",
        "name": "Group 1"
      }
    }
  ]
}

```

Show More
