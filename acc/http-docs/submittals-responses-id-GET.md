# projects/{projectId}/responses/{id}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-responses-id-GET/

---

# projects/{projectId}/responses/{id}

Retrieve details about a single submittal response for the specified project, see the Help documentation .

Note that this endpoint is not compatible with BIM 360 projects.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/responses/:id Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow.

### Request

## URI Parameters

projectId string: UUID The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. id string The ID of the submittal item to retrieve revisions for. To obtain this ID, call GET items .

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

### Response

## HTTP Status Code Summary

200 OK Successful retrieval of response 400 Bad Request The request could not be understood by the server due to malformed syntax or missing request headers. 401 Unauthorized Invalid or missing authorization header. Verify the Bearer token and try again. 403 Forbidden The user is not authorized to perform this action. 404 Not Found The specified resource was not found. 500 Internal Server Error An unexpected error occurred on the server while processing the request.

### Response

## Body Structure (200)

id string: UUID The internal, globally unique identifier (UUID) for the response. key string Not relevant value string The content of the response. platformId string Not relevant isActive boolean true : if the response was not deleted. false : if the response was deleted. categoryId string The type of response. Possible values: 1 (Approved), 2 (Revise and submit), 3 (Rejected). isApproval boolean true : settings this response for a submittal item means an approval. false : settings this response for a submittal item means dis-approval. This attribute is taken from the related categoryId isInUse boolean true : if the response is currently associated with a submittal item. false : if the response is not currently associated with a submittal item. createdBy string The Autodesk ID of the user who created the response. createdAt datetime: ISO 8601 The time and date when the response was created. updatedAt datetime: ISO 8601 The time and date when the response was last updated. updatedBy string The Autodesk ID of the user who last updated the response.

false : if the response was deleted.

false : settings this response for a submittal item means dis-approval.

This attribute is taken from the related categoryId

false : if the response is not currently associated with a submittal item.

## Example

Successful retrieval of response

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/responses/:id' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "id" : "5bab7f9b-61cf-45bc-8bce-f88ddd9d380e" , "key" : "my response" , "value" : "Approved" , "platformId" : "approved" , "isActive" : false , "categoryId" : "1" , "isApproval" : false , "isInUse" : false , "createdBy" : "WD43ZJGKDFLFH" , "createdAt" : "2018-02-01T12:09:24.198466Z" , "updatedAt" : "2018-02-01T12:09:24.198466Z" , "updatedBy" : "WD43ZJGKDFLFH" }
```
