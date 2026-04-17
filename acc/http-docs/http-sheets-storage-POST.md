# projects/{projectId}/storage

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-storage-POST/

---

Uploads

POST

# projects/{projectId}/storage

Creates a storage location in the Object Storage Service (OSS) for you to upload the file to. This endpoint is typically used during the process of uploading files to the [Forma Sheets tool](https://help.autodesk.com/view/BUILD/ENU/?guid=Upload_And_Publish_Sheets).

For more details, see the [Upload Sheets](https://aps.autodesk.com/en/docs/acc/v1/tutorials/upload-sheets/) tutorial.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/storage |
| --- | --- |
| Authentication Context | User context optional |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a two-legged access token obtained via a [Client Credentials Grant flow](../../oauth/how-to-docs/get-2-legged-token.md), or a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). <br>The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context. |
| --- | --- |
| x-user-id   string | The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. <br>When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.<br>You can use either the user’s Forma ID (id), or their Autodesk ID (autodeskId). |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](../how-to-docs/getting-started-retrieve-account-and-project-id.md). You can use a project ID either with a “b.” prefix or without a “b.” prefix. For instance, a project ID of “b.a4be0c34a-4ab7” can also be referred to as “a4be0c34a-4ab7”. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

| fileName   string | The name of the file. <br>Currently Sheets tool only supports PDF files.<br>Max length: 255 |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Successfully created a storage object. |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 403   Forbidden | The user or client represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource cannot be found. |
| 429   Too Many Requests | The server has received too many requests. |
| 500   Internal Server Error | An unexpected error occurred on the server. |

### Response

## [Body Structure (201)](#body-structure-201)

| urn   string | The URN of the storage. <br>Note that in Sheets each project has its own OSS bucket, it is recommended to extract bucket key from storage URN every time before you call OSS APIs. |
| --- | --- |

## [Example](#example)

Successfully created a storage object.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/storage' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "fileName": "example.pdf"
      }'

```

### Response

```
{
  "urn": "urn:adsk.objects:os.object:bimdocs.9ba6681e-1952-4d54-aac4-9de6d9858dd4/67a2d96a-b1d7-474f-86ba-9e01a5c0f5be.pdf"
}

```
