# projects/{projectId}/specs/{id}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-specs-id-GET/

---

# projects/{projectId}/specs/{id}

Retrieve the details about a single spec section. For information about spec sections, see the Help documentation .

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/specs/:id Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow.

### Request

## URI Parameters

projectId string: UUID The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. id string The ID of the submittal item to retrieve revisions for. To obtain this ID, call GET items .

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

### Response

## HTTP Status Code Summary

200 OK Successful request to create a new spec section. 403 Forbidden Unauthorized

### Response

## Body Structure (200)

id string: UUID The internal, globally unique identifier (UUID) for the spec section. title string The title of the spec section. identifier string The unique ID assigned to the spec section within the UI. createdBy string The Autodesk ID of the user who created the spec section. createdAt datetime: ISO 8601 The time and date when the spec section was created. updatedBy string The Autodesk ID of the user who last updated the spec section. updatedAt datetime: ISO 8601 The time and date when spec section was last updated.

## Example

Successful request to create a new spec section.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/specs/:id' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "id" : "e6111f96-8437-491e-a1ae-16fd53f0cbef" , "title" : "Materials" , "identifier" : "500" , "createdBy" : "WD43ZJGKDFLFH" , "createdAt" : "2018-02-01T12:09:24.198466Z" , "updatedBy" : "WD43ZJGKDFLFH" , "updatedAt" : "2018-02-01T12:09:24.198466Z" }
```
