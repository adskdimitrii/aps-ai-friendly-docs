# projects/{projectId}/attachments/{issueId}/items/{attachmentId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/issues-items-attachmentId-DELETE/

---

# projects/{projectId}/attachments/{issueId}/items/{attachmentId}

Deletes a specific attachment from an issue in a project.

## Resource Information

Method and URI DELETE https://developer.api.autodesk.com/construction/issues/v1/projects/{projectId}/attachments/{issueId}/items/{attachmentId} Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow.

### Request

## URI Parameters

projectId string: UUID The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. issueId string: UUID The unique identifier of the issue. To find the ID, call GET issues . attachmentId string: UUID The unique identifier of the attachment. To find the ID, call GET attachments .

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

### Response

## HTTP Status Code Summary

204 No Content OK 400 Bad Request Invalid input 403 Forbidden The request is valid but lacks the necessary permissions. 404 Not Found Issue or attachment not found, or attachment has already been deleted 500 Internal Server Error Internal server error

### Response

## Body Structure (204)

Response for 204 has no body.

## Example

OK

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/:projectId/attachments/:issueId/items/:attachmentId' \ -X 'DELETE' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
204 No Content
```
