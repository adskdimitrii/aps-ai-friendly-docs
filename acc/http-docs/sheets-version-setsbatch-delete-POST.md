# projects/{projectId}/version-sets:batch-delete

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-version-setsbatch-delete-POST/

---

# projects/{projectId}/version-sets:batch-delete

Deletes a list of version sets.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/version-sets:batch-delete Authentication Context user context optional Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. x-user-id string The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2. You can use either the userâs ACC ID (id), or their Autodesk ID (autodeskId). Content-Type * string Must be application/json

When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.

You can use either the userâs ACC ID (id), or their Autodesk ID (autodeskId).

### Request

## URI Parameters

projectId string: UUID The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial . You can use a project ID either with a âb.â prefix or without a âb.â prefix. For instance, a project ID of âb.a4be0c34a-4ab7â can also be referred to as âa4be0c34a-4ab7â.

### Request

## Body Structure

ids * array: string The IDs of the version set to delete. To find the version set IDs, call GET version-sets . The max number of items is 10.

- The max number of items is 10.

### Response

## HTTP Status Code Summary

204 No Content Successfully deleted the list of version sets. 400 Bad Request The parameters of the requested operation are invalid. 403 Forbidden The user or client represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource cannot be found. 429 Too Many Requests The server has received too many requests. 500 Internal Server Error An unexpected error occurred on the server.

### Response

## Body Structure (204)

Response for 204 has no body.

## Example

Successfully deleted the list of version sets.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/version-sets:batch-delete' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "ids": [ "7c2ecde0-2406-49f9-9199-50176848a0b7" ] }'
```

### Response

```
204 No Content
```
