# projects/{projectId}/uploads/{uploadId}/review-sheets

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-review-sheets-GET/

---

Uploads

GET

# projects/{projectId}/uploads/{uploadId}/review-sheets

Retrieves a list of review sheets. This endpoint is typically used during the process of uploading files to the [ACC Sheets tool](https://help.autodesk.com/view/BUILD/ENU/?guid=Upload_And_Publish_Sheets).
It enables you to review the sheets that you uploaded before publishing them. For more details, see the [Upload Sheets](https://aps.autodesk.com/en/docs/acc/v1/tutorials/upload-sheets/) tutorial.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/uploads/{uploadId}/review-sheets |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-user-id   string | The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. <br>When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.<br>You can use either the userâs ACC ID (id), or their Autodesk ID (autodeskId). |

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring: UUID The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](../how-to-docs/getting-started-retrieve-account-and-project-id.md). You can use a project ID either with a âb.â prefix or without a âb.â prefix. For instance, a project ID of âb.a4be0c34a-4ab7â can also be referred to as âa4be0c34a-4ab7â.
- uploadIdstring The ID of the upload. The upload ID is generated when you [create an upload object](http-sheets-uploads-POST.md).

### Request

## [Query String Parameters](#query-string-parameters)

| offset   int | The starting point for the results, specified by item number. The default value is `0`. For example, use `offset=3` to start the results from the third item. |
| --- | --- |
| limit   int | The number of results to return in the response. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the list of review sheets. |
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
| id   string | The ID of the review sheet. |
| page   number | The page number of the source file from which the review sheet was generated. |
| fileName   string | The source file name of the review sheet. |
| number   string | The number of the review sheet. |
| title   string | The title of the review sheet. |
| deleted   boolean | `true` if the review sheet has been deleted.`false` if the review sheet has not been deleted.<br>Note that if the review sheet has been deleted, it will not be published. |
| tags   array: string | The tags of the review sheet. |
| rotation   number | The rotation of the review sheet. Possible values: `0`, `90`, `180`, `270`. |
| processingState   enum:string | The processing state of the review sheet. Possible values: <br>`PROCESSING`: the review sheet is being processed.`AUDITING`: the review sheet is being audited.`ROTATING`: the review sheet is being rotated.`READY`: the review sheet is ready for updating or publishing.`FAILED`: the processing of the review sheet failed.`PUBLISHING` the review sheet is publishing. |
| pagination   object | Pagination information for paged data. |
| limit   int | The number of results to return in the response. |
| offset   int | The item number from which the results begin. |
| previousUrl   string | The URL for the previous page of results. |
| nextUrl   string | The URL for the next page of results. |
| totalResults   int | The total number of results available. |

## [Example](#example)

Successfully retrieved the list of review sheets.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/uploads/5cb5d9da-060e-421e-bca9-97dd8b5cd800/review-sheets' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "results": [
    {
      "id": "0d7a5883-1694-3078-a06d-ad24413f8b06",
      "page": 1,
      "fileName": "example.pdf",
      "number": "A-01",
      "title": "Floor One",
      "deleted": false,
      "tags": [
        "april",
        "floor"
      ],
      "rotation": 0,
      "processingState": "READY"
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
