# projects/{projectId}/packages

Source: https://aps.autodesk.com/en/docs/acc/reference/http/takeoff-projects-project_id-packages-POST/

---

# projects/{projectId}/packages

Creates a takeoff package for a project.

Takeoff packages organize and contain all takeoff data related to a scope of work in your project.

For more information about takeoff packages, see the ACC Takeoff - Working with Packages help documentation.

Note that the Takeoff API does not currently support adding takeoff types and items to a takeoff package. You add takeoff types and items to a takeoff package in the UI.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/construction/takeoff/v1/projects/{projectId}/packages Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. region string Specifies the region where the service is located. Possible values: US , EMEA . For the full list of supported regions, see the Regions page. Content-Type * string Must be application/json

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

projectId string: UUID The ID of the project. This corresponds to project ID in the Data Management API , and can be specified in the form of âUUIDâ or b.âUUIDâ. To learn how to find the project ID, see the Retrieve ACC Account and project ID tutorial.

This corresponds to project ID in the Data Management API , and can be specified in the form of âUUIDâ or b.âUUIDâ.

To learn how to find the project ID, see the Retrieve ACC Account and project ID tutorial.

### Request

## Body Structure

name * string The package name (user defined). Corresponding UI name: Title . Max length: 64

Corresponding UI name: Title .

Max length: 64

### Response

## HTTP Status Code Summary

201 Created Successfully created the takeoff package. 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 409 Conflict The package already exists in the project. 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The âRetry-Afterâ header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (201)

name string The package name (user defined). Corresponding UI name: Title . Max length: 64 id string: UUID The package ID. createdAt datetime: ISO 8601 The date and time when the resource was created, in the following format: YYYY-MM-DDThh:mm:ssZ . updatedAt datetime: ISO 8601 The date and time when the resource was last updated, in the following format: YYYY-MM-DDThh:mm:ssZ . updatedByName string The name of the user who last updated the resource.

Corresponding UI name: Title .

Max length: 64

## Example

Successfully created the takeoff package.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/takeoff/v1/projects/:projectId/packages' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "name": "Concrete" }'
```

### Response

```
{ "id" : "497f6eca-6276-4993-bfeb-53cbbbba6f08" , "name" : "Concrete" , "createdAt" : "2019-08-24T14:15:22Z" , "updatedAt" : "2020-11-11T12:32:45Z" , "updatedByName" : "Jane Johnson" }
```
