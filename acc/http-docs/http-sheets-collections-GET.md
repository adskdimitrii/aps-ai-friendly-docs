# projects/{projectId}/collections

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-collections-GET/

---

Collections

GET

# projects/{projectId}/collections

Retrieves information about all the collections in a project. You can use [GET sheets](http-sheets-sheets-GET.md) to return all the sheets associated with a specific collection.

For more information about Sheets collections, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Sheets_Collections_Autodesk_Build).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/collections |
| --- | --- |
| Authentication Context | User context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

- Authorization*string Must be `Bearer <token>`, where `<token>` is a two-legged access token obtained via a [Client Credentials Grant flow](../../oauth/how-to-docs/get-2-legged-token.md), or a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context.
- x-user-idstring The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.You can use either the user’s Forma ID (id), or their Autodesk ID (autodeskId).

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](../how-to-docs/getting-started-retrieve-account-and-project-id.md). You can use a project ID either with a “b.” prefix or without a “b.” prefix. For instance, a project ID of “b.a4be0c34a-4ab7” can also be referred to as “a4be0c34a-4ab7”. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| offset   int | The starting point for the results, specified by item number. The default value is `0`. For example, use `offset=3` to start the results from the third item. |
| --- | --- |
| limit   int | The number of results to return in the response. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the collections data. |
| --- | --- |
| 400   Bad Request | The request parameters are invalid. <br>Sample error code and message:<br>ERR_BAD_INPUT: <br>  Failed to parse the token |
| 401   Unauthorized | The provided bearer token is invalid. <br>Sample error code and message:<br>ERR_AUTHENTICATED_ERROR: <br>  Authentication header is incorrect |
| 403   Forbidden | The user or service associated with the bearer token does not have permission to perform this operation. <br>Sample error code and messages:<br>ERR_NOT_ALLOWED: <br>  Hub inactive  Project inactive  User inactive  API access denied  User {userId} does not have download permission on resource {resource} |
| 404   Not Found | The requested resource (e.g., project, hub, user, sheet, or collection) does not exist. <br>Sample error code and messages:<br>ERR_RESOURCE_NOT_EXIST: <br>  Project not found  Project user not found  Collection does not exist |
| 500   Internal Server Error | An unexpected error occurred on the server. <br>Sample error code and messages:<br>ERR_INTERNAL_SERVER_ERROR: <br>  Request failed due to internal exception xxx  Failed to retrieve hub  Failed to retrieve project  Failed to retrieve user |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | The list of collections. |
| --- | --- |
| id   string: UUID | The unique identifier of the collection. |
| name   string | The name of the collection. This corresponds to the Name column in the Forma Sheets Collections Settings UI. |
| createdAt   datetime: ISO 8601 | The date and time the collection was created. |
| createdBy   string | The Autodesk ID of the user who created the collection. |
| createdByName   string | The name of the user who created the collection. |
| updatedAt   datetime: ISO 8601 | The date and time the collection was last updated. |
| updatedBy   string | The Autodesk ID of the user who last updated the collection. |
| updatedByName   string | The name of the user who last updated the collection. |
| pagination   object | Pagination information for paged data. |
| limit   int | The number of results to return in the response. |
| offset   int | The item number from which the results begin. |
| previousUrl   string | The URL for the previous page of results. |
| nextUrl   string | The URL for the next page of results. |
| totalResults   int | The total number of results available. |

## [Example](#example)

Successfully retrieved the collections data.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/collections' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "results": [
    {
      "id": "619ef887-974f-45e4-9775-461e6a62d784",
      "name": "Group 1",
      "createdAt": "2024-11-04T08:12:23.041Z",
      "createdBy": "45GPJ4KAX789",
      "createdByName": "John Smith",
      "updatedAt": "2024-11-04T08:12:23.041Z",
      "updatedBy": "45GPJ4KAX789",
      "updatedByName": "John Smith"
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
