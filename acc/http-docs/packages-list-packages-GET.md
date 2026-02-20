# projects/{projectId}/packages

Source: https://aps.autodesk.com/en/docs/acc/reference/http/packages-list-packages-GET/

---

# projects/{projectId}/packages

Retrieves a list of all packages within a specified ACC project.

With two-legged authentication, returns all packages in the project.  With two-legged authentication and the x-user-id header, or with three-legged authentication, returns only the packages that the specified or current user has permission to access.

For information about creating packages, see the Create Packages documentation.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/packages/v1/projects/{projectId}/packages Authentication Context user context optional Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. x-user-id string The Autodesk ID of the user on whose behalf the request is made. This header is required only when using two-legged authentication. It is not needed for three-legged authentication. Your application can access only those users who are assigned to it in the SaaS Integrations UI. Only user Autodesk IDs ( autodeskId ) are supported.

This header is required only when using two-legged authentication. It is not needed for three-legged authentication.

Your application can access only those users who are assigned to it in the SaaS Integrations UI.

Only user Autodesk IDs ( autodeskId ) are supported.

### Request

## URI Parameters

projectId string: UUID The ID of the project. You can retrieve the project ID using the Data Management API . For more details, see the Retrieve a Project ID tutorial. You may provide the project ID with or without the b. prefix: With prefix: b.657a5565-09b7-48e0-bd03-acacfe42efaf Without prefix: 657a5565-09b7-48e0-bd03-acacfe42efaf

You can retrieve the project ID using the Data Management API . For more details, see the Retrieve a Project ID tutorial.

You may provide the project ID with or without the b. prefix:

- With prefix: b.657a5565-09b7-48e0-bd03-acacfe42efaf

- Without prefix: 657a5565-09b7-48e0-bd03-acacfe42efaf

### Request

## Query String Parameters

limit int The number of packages to return in the response payload. Possible values: 1-200 . Default: 200 . For example: limit=2 . offset int The number of packages that you want to begin retrieving results from. Default: 0 . For example: offset=10 filter[createdBy] string Filters results by the Autodesk ID of the users who created the packages. You can provide a single Autodesk ID or a comma-separated list of IDs. filter[updatedBy] string Filters results by the Autodesk ID of the users who last updated the packages. You can provide a single Autodesk ID or a comma-separated list of IDs. To find the IDs call GET users filter[createdAt] string Filter packages by their creation time. Use an ISO 8601 date-time range in the format startDate..endDate . Either date may be omitted to specify an open-ended range. Examples: After a specific time: 2025-03-26T16:00:00.000Z.. Before a specific time: ..2025-03-28T15:59:59.999Z Between two times: 2025-03-26T16:00:00.000Z..2025-03-28T15:59:59.999Z filter[updatedAt] string Filter packages by their last update time. Use an ISO 8601 date-time range in the format startDate..endDate . Either date may be omitted to specify an open-ended range. Examples: After a specific time: 2025-03-26T16:00:00.000Z.. Before a specific time: ..2025-03-28T15:59:59.999Z Between two times: 2025-03-26T16:00:00.000Z..2025-03-28T15:59:59.999Z sort enum:string Sorts the results by a supported field. By default, results are sorted in ascending ( asc ) order. To sort in descending order, add desc after the field name. Format: sort=fieldName [desc] Possible values: name , createdAt , updatedAt , displayId , Examples: Sort by name (ascending): sort=name Sort by creation time (descending): sort=createdAt desc filter[versionType] enum:string Filters results by the version type of the packages. Possible values: FIXED â Files in the package remain fixed at selected versions. CURRENT â Files in the package automatically update to the latest current versions. For more details, see the Flexible Package Types documentation.

Possible values: 1-200 . Default: 200 . For example: limit=2 .

Default: 0 . For example: offset=10

You can provide a single Autodesk ID or a comma-separated list of IDs.

You can provide a single Autodesk ID or a comma-separated list of IDs.

To find the IDs call GET users

Either date may be omitted to specify an open-ended range.

Examples:

- After a specific time: 2025-03-26T16:00:00.000Z..

- Before a specific time: ..2025-03-28T15:59:59.999Z

- Between two times: 2025-03-26T16:00:00.000Z..2025-03-28T15:59:59.999Z

Either date may be omitted to specify an open-ended range.

Examples:

- After a specific time: 2025-03-26T16:00:00.000Z..

- Before a specific time: ..2025-03-28T15:59:59.999Z

- Between two times: 2025-03-26T16:00:00.000Z..2025-03-28T15:59:59.999Z

By default, results are sorted in ascending ( asc ) order. To sort in descending order, add desc after the field name.

Format: sort=fieldName [desc]

Possible values: name , createdAt , updatedAt , displayId ,

Examples:

- Sort by name (ascending): sort=name

- Sort by creation time (descending): sort=createdAt desc

Possible values:

- FIXED â Files in the package remain fixed at selected versions.

- CURRENT â Files in the package automatically update to the latest current versions.

For more details, see the Flexible Package Types documentation.

### Response

## HTTP Status Code Summary

200 OK Successfully retrieved a list of packages 400 Bad Request Bad request. The input parameters were invalid. 403 Forbidden Forbidden. The user does not have permission to access this resource. 404 Not Found Not found. The resource does not exist or is inaccessible. 500 Internal Server Error An unexpected server error occurred.

### Response

## Body Structure (200)

results array: object The list of results. id string: UUID The unique identifier (UUID) of the package. displayId int The display ID of the package. name string The name of the package. Max length: 255 description string The description of the package. Max length: 2048 createdAt datetime: ISO 8601 The time the package was created. createdBy string The Autodesk ID of the user who created the package. For details about the user, call GET users . updatedAt datetime: ISO 8601 The time the package was last updated. updatedBy string The Autodesk ID of the user who last updated the package. For details about the user, call GET users . locked boolean true : The package is locked. Its contents cannot be modified until it is unlocked. false : The package is not locked. Files and resources can still be added, removed, or updated. lockedBy string The Autodesk ID of the user who locked the package. For details about the user, call GET users . lockedAt datetime: ISO 8601 The time the package was locked. resourceCount int The number of resources in the package. versionType object The version type of the package. Possible values: FIXED â The files in the package remain fixed at the selected versions. CURRENT â The files in the package automatically update to the latest current versions. CHANGING â The package is temporarily changing from one version type to another. This state usually lasts only a few seconds and cannot be used as a filter. For more details, see the Change Package Version Type documentation. pagination object The pagination information for the response. This object is included when results are returned in multiple pages. limit int The maximum number of objects that may be returned in the page. offset int The offset from the start of the collection to the first entry in the page. It is zero-based. nextUrl string The URL to retrieve the next page of results. If not included, this is the last page of results. totalResults int The total number of results that match the query, regardless of the limit value.

Max length: 255

Max length: 2048

false : The package is not locked. Files and resources can still be added, removed, or updated.

Possible values:

- FIXED â The files in the package remain fixed at the selected versions.

- CURRENT â The files in the package automatically update to the latest current versions.

- CHANGING â The package is temporarily changing from one version type to another. This state usually lasts only a few seconds and cannot be used as a filter.

For more details, see the Change Package Version Type documentation.

## Example

Successfully retrieved a list of packages

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/packages/v1/projects/657a5565-09b7-48e0-bd03-acacfe42efaf/packages?limit=200&filter[createdBy]=L9VDREARJ7X2,9NGKQKPXAUHG&filter[updatedBy]=L9VDREARJ7X2,9NGKQKPXAUHG&filter[createdAt]=2025-03-26T16:00:00.000Z..2025-03-28T15:59:59.999Z&filter[updatedAt]=2025-03-26T16:00:00.000Z..2025-03-28T15:59:59.999Z&sort=name&filter[versionType]=FIXED' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "results" : [ { "id" : "c25d1273-41e3-4e04-be1e-f4c1ba809d14" , "displayId" : 8642 , "name" : "Milestones" , "description" : "This package contains all the files related to the milestones." , "createdAt" : "2025-03-27T01:28:28.272Z" , "createdBy" : "L9VDREARJ7X2" , "updatedAt" : "2025-03-27T03:25:48.884Z" , "updatedBy" : "L9VDREARJ7X2" , "locked" : true , "lockedBy" : "L9VDREARJ7X2" , "lockedAt" : "2025-03-27T03:25:48.884Z" , "resourceCount" : 2 , "versionType" : "FIXED" } ], "pagination" : { "limit" : 200 , "offset" : 0 , "nextUrl" : "https://developer.api.autodesk.com/construction/packages/v1/projects/657a5565-09b7-48e0-bd03-acacfe42efaf/packages?limit=200&offset=400" , "totalResults" : 8618 } }
```
