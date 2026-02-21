# projects/{projectId}/collections/{collectionId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-collections-collectionId-GET/

---

Collections

GET

# projects/{projectId}/collections/{collectionId}

Retrieves a specific collection by its unique ID.

You can use [GET sheets](/en/docs/acc/v1/reference/http/sheets-sheets-GET/) to return all the sheets associated with a specific collection.

For more information about Sheets collections, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Sheets_Collections_Autodesk_Build).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/collections/{collectionId} |
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

- projectIdstring: UUID The ID of the project. Use the [Data Management API](/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/). You can use a project ID either with a âb.â prefix or without a âb.â prefix. For instance, a project ID of âb.a4be0c34a-4ab7â can also be referred to as âa4be0c34a-4ab7â.
- collectionIdstring: UUID The ID of the collection, To find the collection ID, call [GET collections](/en/docs/acc/v1/reference/http/sheets-collections-GET/).

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved collection data |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. <br>Sample error code with possible messages:<br>ERR_BAD_INPUT: <br>  Failed to parse the token |
| 401   Unauthorized | The provided bearer token is not valid. <br>Sample error code with possible messages:<br>ERR_AUTHENTICATED_ERROR: <br>  Authentication header is not correct |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. <br>Sample error code with possible messages:<br>ERR_NOT_ALLOWED: <br>  Account inactive  Project inactive  User inactive  API access denied  User {userId} does not have download permission on resource {resource} |
| 404   Not Found | The requested resources, such as the project, account, user, sheet, or collection, do not exist. <br>Sample error code with possible messages:<br>ERR_RESOURCE_NOT_EXIST: <br>  Project not found  Project user not found  The collection does not exist |
| 500   Internal Server Error | An unknown error occurred on the server. <br>Sample error code with possible messages:<br>ERR_INTERNAL_SERVER_ERROR: <br>  Request failed for internal exception xxx  Failed to get account  Failed to get project  Failed to get user |

### Response

## [Body Structure (200)](#body-structure-200)

| id   string: UUID | The unique identifier of the collection. |
| --- | --- |
| name   string | The name of the collection. This corresponds to the Name column in the ACC Sheets Collections Settings UI. |
| createdAt   datetime: ISO 8601 | The date and time the collection was created. |
| createdBy   string | The Autodesk ID of the user who created the collection. |
| createdByName   string | The name of the user who created the collection. |
| updatedAt   datetime: ISO 8601 | The date and time the collection was last updated. |
| updatedBy   string | The Autodesk ID of the user who last updated the collection. |
| updatedByName   string | The name of the user who last updated the collection. |

## [Example](#example)

Successfully retrieved collection data

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/collections/5cb5d9da-060e-421e-bca9-97dd8b5cd800' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
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

```

Show More
