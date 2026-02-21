# projects/{projectId}/uploads

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-uploads-GET/

---

Uploads

GET

# projects/{projectId}/uploads

Checks the processing status of all the uploaded files in the project.

For more details about uploading sheets, see the [Upload Sheets](/en/docs/acc/v1/tutorials/upload-sheets/) tutorial.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/uploads |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](/en/docs/oauth/v2/tutorials/get-2-legged-token) or [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| x-user-id   string | The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. <br>When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.<br>You can use either the userâs ACC ID (id), or their Autodesk ID (autodeskId). |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. Use the [Data Management API](/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/). You can use a project ID either with a âb.â prefix or without a âb.â prefix. For instance, a project ID of âb.a4be0c34a-4ab7â can also be referred to as âa4be0c34a-4ab7â. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| offset   int | The starting point for the results, specified by item number. The default value is `0`. For example, use `offset=3` to start the results from the third item. |
| --- | --- |
| limit   int | The number of results to return in the response. |
| sort   string | Sort the uploads by `createdAt` or `issuanceDate`. You need to add whether to sort in ascending (`asc`) or descending (`desc`) order. For example, `sort=issuanceDate desc`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved a list of uploads. |
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
| id   string: UUID | The ID of the upload. |
| versionSetId   string: UUID | The ID of the version set where the upload creates sheets to. |
| status   enum:string | The status of the upload. Possible values: <br>`PENDING`: the uploaded files are waiting for to be processed.`PROCESSING`: the uploaded files are being processed.`IN_REVIEW`: the file upload process is complete. The sheets are ready for review. You can now call [GET review-sheets](/en/docs/acc/v1/reference/http/sheets-review-sheets-GET/), [PATCH review-sheets](/en/docs/acc/v1/reference/http/sheets-review-sheets-PATCH/), or [POST review-sheets:publish](/en/docs/acc/v1/reference/http/sheets-review-sheetspublish-POST/).`FAILED`: the file upload process failed. One of the final status of an upload.`UPDATING_VERSION_SET`: the target version set is being updated.`PUBLISHING`: the review sheets are being published.`PUBLISHED`: the review sheets have been published. |
| createdAt   datetime: ISO 8601 | The time when the upload was created, in ISO-8601 format (YYYY-MM-DDTHH:mm:ss.SSSZ). |
| createdBy   string | The ID of the user who created the upload. |
| createdByName   string | The name of the user who created the upload. |
| updatedAt   datetime: ISO 8601 | The time when the upload was last updated, in ISO-8601 format (YYYY-MM-DDTHH:mm:ss.SSSZ). |
| updatedBy   string | The ID of the user who last updated the upload. |
| updatedByName   string | The name of the user who last updated the upload. |
| publishedAt   datetime: ISO 8601 | The time when all the review sheets of the upload were published, in ISO-8601 format (YYYY-MM-DDTHH:mm:ss.SSSZ). |
| publishedBy   string | The ID of the user who published all the review sheets of the upload. |
| publishedByName   string | The name of the user who published all the review sheets of the upload. |
| publishedCount   int | The number of files that have been published by the upload. |
| pagination   object | Pagination information for paged data. |
| limit   int | The number of results to return in the response. |
| offset   int | The item number from which the results begin. |
| previousUrl   string | The URL for the previous page of results. |
| nextUrl   string | The URL for the next page of results. |
| totalResults   int | The total number of results available. |

## [Example](#example)

Successfully retrieved a list of uploads.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/uploads?sort=createdAt desc' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "results": [
    {
      "id": "5cb5d9da-060e-421e-bca9-97dd8b5cd800",
      "versionSetId": "7c2ecde0-2406-49f9-9199-50176848a0b7",
      "status": "PENDING",
      "createdAt": "2021-07-01T05:21:05.391Z",
      "createdBy": "45GPJ4KAX789",
      "createdByName": "John Smith",
      "updatedAt": "2021-07-01T05:21:05.391Z",
      "updatedBy": "45GPJ4KAX789",
      "updatedByName": "John Smith",
      "publishedAt": "2021-07-01T05:21:05.391Z",
      "publishedBy": "45GPJ4KAX789",
      "publishedByName": "John Smith",
      "publishedCount": 1
    }
  ],
  "pagination": {
    "limit": 100,
    "offset": 0,
    "previousUrl": "",
    "nextUrl": "",
    "totalResults": 1
  }
}

```

Show More
