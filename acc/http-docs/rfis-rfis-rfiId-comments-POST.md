# v3/projects/{projectId}/rfis/{rfiId}/comments

Source: https://aps.autodesk.com/en/docs/acc/reference/http/rfis-rfis-rfiId-comments-POST/

---

# v3/projects/{projectId}/rfis/{rfiId}/comments

Adds a comment to an RFI.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/rfis/:rfiId/comments Authentication Context user context required Required OAuth Scopes data:write data:create Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json

### Request

## URI Parameters

projectId string The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. rfiId string The ID of the RFI. To find the ID, call POST search:rfis .

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

### Request

## Body Structure

id string: UUID The comment ID. Leave empty if you want to let the system generate one. body string The content of the comment. Max length: 10000

Max length: 10000

### Response

## HTTP Status Code Summary

201 Created Created 400 Bad Request The parameters are invalid 401 Unauthorized The provided bearer token is not valid 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation 500 Internal Server Error An unknown error occurred on the server

### Response

## Body Structure (201)

id string The unique identifier of the comment. body string The content of the comment. createdBy string The Autodesk ID of the user who created the comment. To check the name of the user, call GET users . createdAt datetime: ISO 8601 The timestamp of the date and time the comment was created, in the following format: YYYY-MM-DDThh:mm:ss.sz . updatedAt datetime: ISO 8601 The timestamp of the date and time the comment was updated, in the following format: YYYY-MM-DDThh:mm:ss.sz . source enum:string The source of the comment. Indicates how the comment was created.
Possible values: web â The comment was created through the web interface or API. email â The comment was created by replying via email. rfiId string The ID of the RFI associated with this comment.

To check the name of the user, call GET users .

- web â The comment was created through the web interface or API.

- email â The comment was created by replying via email.

## Example

Created

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/rfis/:rfiId/comments' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "id": "", "body": "This needs more attention." }'
```

### Response

```
{ "id" : "94ce6921-e8f9-4bc5-bf5a-1a8f543a2564" , "body" : "This needs more attention." , "createdBy" : "PER8KQPK2JRT" , "createdAt" : "2018-08-01T08:56:48.699Z" , "updatedAt" : "2019-08-01T08:56:48.699Z" , "source" : "web" , "rfiId" : "f73e4dd9-cd44-4b3e-8651-901ba2e8bc8d" }
```
