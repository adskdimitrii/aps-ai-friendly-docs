# projects/{projectId}/uploads/{uploadId}/review-sheets:publish

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-review-sheetspublish-POST/

---

Uploads

POST

# projects/{projectId}/uploads/{uploadId}/review-sheets:publish

Publishes uploaded review sheets.

To publish review sheets, all the sheets need to have either a `READY` or `FAILED` process status. Only review sheets with a `READY` status will be published.
To check the upload status call [GET review-sheets](http-sheets-review-sheets-GET.md).

For more details about the upload process, see the [Upload Files to Forma Sheets](https://aps.autodesk.com/en/docs/acc/v1/tutorials/upload-sheets/) tutorial.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/uploads/{uploadId}/review-sheets:publish |
| --- | --- |
| Authentication Context | User context optional |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

- Authorization*string Must be `Bearer <token>`, where `<token>` is a two-legged access token obtained via a [Client Credentials Grant flow](../../oauth/how-to-docs/get-2-legged-token.md), or a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context.
- x-user-idstring The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.You can use either the user’s Forma ID (id), or their Autodesk ID (autodeskId).

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring: UUID The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](../how-to-docs/getting-started-retrieve-account-and-project-id.md). You can use a project ID either with a “b.” prefix or without a “b.” prefix. For instance, a project ID of “b.a4be0c34a-4ab7” can also be referred to as “a4be0c34a-4ab7”.
- uploadIdstring The ID of the upload. The upload ID is generated when you [create an upload object](http-sheets-uploads-POST.md).

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 202   Accepted | The request was successfully accepted. |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 403   Forbidden | The user or client represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource cannot be found. |
| 429   Too Many Requests | The server has received too many requests. |
| 500   Internal Server Error | An unexpected error occurred on the server. |

### Response

## [Body Structure (202)](#body-structure-202)

Response for 202 has no body.

## [Example](#example)

The request was successfully accepted.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/uploads/5cb5d9da-060e-421e-bca9-97dd8b5cd800/review-sheets:publish' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```

```
