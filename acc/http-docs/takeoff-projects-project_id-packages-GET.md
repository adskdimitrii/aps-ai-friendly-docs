# projects/{projectId}/packages

Source: https://aps.autodesk.com/en/docs/acc/reference/http/takeoff-projects-project_id-packages-GET/

---

# projects/{projectId}/packages

Retrieves the takeoff packages for a project.

Takeoff packages organize and contain all takeoff data related to a scope of work in your project.

For more information about takeoff packages, see the ACC Takeoff - Working with Packages help documentation.

To learn how this endpoint is used, see the Takeoff Extract Inventory tutorial.

To find the takeoff types in a package, call GET takeoff-types .

To find the takeoff items in a package, call GET takeoff-items .

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/takeoff/v1/projects/{projectId}/packages Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. region string Specifies the region where the service is located. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

projectId string: UUID The ID of the project. This corresponds to project ID in the Data Management API , and can be specified in the form of âUUIDâ or b.âUUIDâ. To learn how to find the project ID, see the Retrieve ACC Account and project ID tutorial.

This corresponds to project ID in the Data Management API , and can be specified in the form of âUUIDâ or b.âUUIDâ.

To learn how to find the project ID, see the Retrieve ACC Account and project ID tutorial.

### Request

## Query String Parameters

offset int The package index from which the pagination starts. This is zero-based. limit int The maximum number of packages per page. Acceptable values: 1-200 . Default value: 200 .

Acceptable values: 1-200 .

Default value: 200 .

### Response

## HTTP Status Code Summary

200 OK Successfully retrieved the takeoff packages. 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The âRetry-Afterâ header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

pagination object The pagination object. limit int The maximum number of objects per page. nextUrl string The URL path that returns the next page of data. offset int The object number from which the pagination starts. This is zero-based. results array: object A list of takeoff packages for the project. name string The package name (user defined). Corresponding UI name: Title . Max length: 64 id string: UUID The package ID. createdAt datetime: ISO 8601 The date and time when the resource was created, in the following format: YYYY-MM-DDThh:mm:ssZ . updatedAt datetime: ISO 8601 The date and time when the resource was last updated, in the following format: YYYY-MM-DDThh:mm:ssZ . updatedByName string The name of the user who last updated the resource.

Corresponding UI name: Title .

Max length: 64

## Example

Successfully retrieved the takeoff packages.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/takeoff/v1/projects/:projectId/packages?limit=200' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "pagination" : { "limit" : 100 , "nextUrl" : "https://developer.api.autodesk.com/construction/takeoff/v1/resources?limit=100&offset=200" , "offset" : 100 }, "results" : [ { "id" : "497f6eca-6276-4993-bfeb-53cbbbba6f08" , "name" : "Concrete" , "createdAt" : "2019-08-24T14:15:22Z" , "updatedAt" : "2020-11-11T12:32:45Z" , "updatedByName" : "Jane Johnson" } ] }
```
