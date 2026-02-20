# projects/{projectId}/classification-systems/{systemId}/classifications

Source: https://aps.autodesk.com/en/docs/acc/reference/http/takeoff-projects-project_id-classification-systems-system_id-classifications-GET/

---

# projects/{projectId}/classification-systems/{systemId}/classifications

Retrieves the classification hierarchy for a classification system.

For more information, see the ACC Configure Takeoff Settings help documentation.

To learn how this endpoint is used, see the Takeoff Extract Inventory tutorial.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/takeoff/v1/projects/{projectId}/classification-systems/{systemId}/classifications Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. region string Specifies the region where the service is located. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

projectId string: UUID The ID of the project. This corresponds to project ID in the Data Management API , and can be specified in the form of âUUIDâ or b.âUUIDâ. To learn how to find the project ID, see the Retrieve ACC Account and project ID tutorial. systemId string: UUID The classification system ID. To find the ID, call GET classification-systems .

This corresponds to project ID in the Data Management API , and can be specified in the form of âUUIDâ or b.âUUIDâ.

To learn how to find the project ID, see the Retrieve ACC Account and project ID tutorial.

To find the ID, call GET classification-systems .

### Request

## Query String Parameters

offset int The classification index from which the pagination starts. This is zero-based. limit int The maximum number of classification objects per page. Acceptable values: 1-10000 . Default value: 10000 .

Acceptable values: 1-10000 .

Default value: 10000 .

### Response

## HTTP Status Code Summary

200 OK Successfully retrieved the classification hierarchy. 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The âRetry-Afterâ header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

pagination object The pagination object. limit int The maximum number of objects per page. nextUrl string The URL path that returns the next page of data. offset int The object number from which the pagination starts. This is zero-based. results array: object List of classifications in the classification system. code string The classification code. Max length: 256 parentCode string The classification parent code. Its value may be null , indicating that this classification is at the top level of the hierarchy. Max length: 256 description string A description of the classification. Max length: 256 measurementType enum:string Deprecated. Will be removed on September 15, 2025. The type of measurement. Possible values: AREA , COUNT , DISTANCE , VOLUME .

Max length: 256

Its value may be null , indicating that this classification is at the top level of the hierarchy.

Max length: 256

Max length: 256

The type of measurement.

Possible values: AREA , COUNT , DISTANCE , VOLUME .

## Example

Successfully retrieved the classification hierarchy.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/takeoff/v1/projects/:projectId/classification-systems/:systemId/classifications?limit=10000' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "pagination" : { "limit" : 100 , "nextUrl" : "https://developer.api.autodesk.com/construction/takeoff/v1/resources?limit=100&offset=200" , "offset" : 100 }, "results" : [ { "code" : "A1010.20" , "parentCode" : "A1010" , "description" : "Concrete" , "measurementType" : "AREA" } ] }
```
