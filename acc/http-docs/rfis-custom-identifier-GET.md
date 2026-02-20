# custom-identifier

Source: https://aps.autodesk.com/en/docs/acc/reference/http/rfis-custom-identifier-GET/

---

# custom-identifier

Returns the current and next available RFI custom identifier for the project.

Use this endpoint to display or pre-fill the next custom RFI number when creating a new RFI. The identifier is automatically incremented and skips numbers that are already in use.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/rfis/custom-identifier Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow.

### Request

## URI Parameters

projectId string The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

### Response

## HTTP Status Code Summary

200 OK Details of the last created and the next available custom identifiers. 400 Bad Request The parameters are invalid 401 Unauthorized The provided bearer token is not valid 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation 500 Internal Server Error An unknown error occurred on the server

### Response

## Body Structure (200)

current string,null The last custom identifier that was used for an RFI in this project. next string The next available custom identifier for the project.

## Example

Details of the last created and the next available custom identifiers.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/rfis/custom-identifier' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "current" : "353" , "next" : "354" }
```
