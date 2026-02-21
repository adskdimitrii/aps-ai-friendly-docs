# projects/{projectId}/version-sets

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-version-sets-POST/

---

Version Sets

POST

# projects/{projectId}/version-sets

Creates a version set.

A version set is required for uploading sheets. Version sets are used by document managers to group specific versions of sheets together.

For more details about the upload process, see the [Upload Files to ACC Sheets](/en/docs/acc/v1/tutorials/upload-sheets/) tutorial.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/version-sets |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](/en/docs/oauth/v2/tutorials/get-2-legged-token) or [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| x-user-id   string | The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. <br>When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.<br>You can use either the userâs ACC ID (id), or their Autodesk ID (autodeskId). |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. Use the [Data Management API](/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/). You can use a project ID either with a âb.â prefix or without a âb.â prefix. For instance, a project ID of âb.a4be0c34a-4ab7â can also be referred to as âa4be0c34a-4ab7â. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

| name*   string | The name of the version set. <br>The max length is 255.Should not be space only.<br>These handlings will be applied to the name before using it to create version set:<br>Spaces at the end or beginning will be removed.Continuous spaces inside will be reduced to one.<br>Max length: 255 |
| --- | --- |
| issuanceDate*   datetime: ISO 8601 | The issuance date of the version set, ISO-8601 date format (YYYY-MM-DD). |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Successfully created a version set. Note that this API does not support creating version sets within a collection. All version sets created will be ungrouped, and the `collection` property in the response will always be `null`. |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 403   Forbidden | The user or client represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource cannot be found. |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the target resource. |
| 429   Too Many Requests | The server has received too many requests. |
| 500   Internal Server Error | An unexpected error occurred on the server. |

### Response

## [Body Structure (201)](#body-structure-201)

Expand all

| id   string: UUID | The ID of the version set. |
| --- | --- |
| name   string | The name of the version set. |
| issuanceDate   datetime: ISO 8601 | The issuance date of the version set, in ISO-8601 date format (YYYY-MM-DD). |
| createdAt   datetime: ISO 8601 | The time when the version set was created, in ISO-8601 format (YYYY-MM-DDTHH:mm:ss.SSSZ). |
| createdBy   string | The ID of the user who created the version set. |
| createdByName   string | The name of the user who created the version set. |
| updatedAt   datetime: ISO 8601 | The time when the version set was last updated, in ISO-8601 format (YYYY-MM-DDTHH:mm:ss.SSSZ). |
| updatedBy   string | The ID of the user who last updated the version set. |
| updatedByName   string | The name of the user who last updated the version set. |
| collection   object | The collection object, if assigned. If no collection is assigned, this value is `null`. |
| id   string: UUID | The unique identifier of the collection. |
| name   string | The name of the collection. This corresponds to the Name column in the ACC Sheets Collections Settings UI. <br>Max length: 255 |

## [Example](#example)

Successfully created a version set.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/version-sets' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": "Preliminary Design - Phase 1",
        "issuanceDate": "2021-07-01"
      }'

```

Show More

### Response

```
{
  "id": "7c2ecde0-2406-49f9-9199-50176848a0b7",
  "name": "one set",
  "issuanceDate": "2021-07-01",
  "createdAt": "2021-07-01T05:21:05.391Z",
  "createdBy": "45GPJ4KAX789",
  "createdByName": "John Smith",
  "updatedAt": "2021-07-01T05:21:05.391Z",
  "updatedBy": "45GPJ4KAX789",
  "updatedByName": "John Smith",
  "collection": null
}

```

Show More
