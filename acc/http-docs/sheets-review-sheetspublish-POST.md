# projects/{projectId}/uploads/{uploadId}/review-sheets:publish

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-review-sheetspublish-POST/

---

# projects/{projectId}/uploads/{uploadId}/review-sheets:publish

Publishes uploaded review sheets.

To publish review sheets, all the sheets need to have either a READY or FAILED process status. Only review sheets with a READY status will be published.
To check the upload status call GET review-sheets .

For more details about the upload process, see the Upload Files to ACC Sheets tutorial.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/uploads/{uploadId}/review-sheets:publish Authentication Context user context optional Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. x-user-id string The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2. You can use either the userâs ACC ID (id), or their Autodesk ID (autodeskId).

When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.

You can use either the userâs ACC ID (id), or their Autodesk ID (autodeskId).

### Request

## URI Parameters

projectId string: UUID The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial . You can use a project ID either with a âb.â prefix or without a âb.â prefix. For instance, a project ID of âb.a4be0c34a-4ab7â can also be referred to as âa4be0c34a-4ab7â. uploadId string The ID of the upload. The upload ID is generated when you create an upload object .

### Response

## HTTP Status Code Summary

202 Accepted The request was successfully accepted. 400 Bad Request The parameters of the requested operation are invalid. 403 Forbidden The user or client represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource cannot be found. 429 Too Many Requests The server has received too many requests. 500 Internal Server Error An unexpected error occurred on the server.

### Response

## Body Structure (202)

Response for 202 has no body.

## Example

The request was successfully accepted.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/uploads/5cb5d9da-060e-421e-bca9-97dd8b5cd800/review-sheets:publish' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response
