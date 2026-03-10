# projects/{projectId}/version-sets:batch-get

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-version-setsbatch-get-POST/

---

Version Sets

POST

# projects/{projectId}/version-sets:batch-get

Retrieves a list of version sets.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/version-sets:batch-get |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-user-id   string | The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. <br>When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.<br>You can use either the user’s ACC ID (id), or their Autodesk ID (autodeskId). |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](../how-to-docs/getting-started-retrieve-account-and-project-id.md). You can use a project ID either with a “b.” prefix or without a “b.” prefix. For instance, a project ID of “b.a4be0c34a-4ab7” can also be referred to as “a4be0c34a-4ab7”. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

| ids   array: string | The IDs of the version sets to retrieve. <br>The max number of items is 200. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the list of version sets. |
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
| id   string: UUID | The ID of the version set. |
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

Successfully retrieved the list of version sets.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/version-sets:batch-get' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "ids": [
          "7c2ecde0-2406-49f9-9199-50176848a0b7"
        ]
      }'

```

Show More

### Response

```
{
  "results": [
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
      "collection": {
        "id": "619ef887-974f-45e4-9775-461e6a62d784",
        "name": "Group 1"
      }
    }
  ]
}

```

Show More
