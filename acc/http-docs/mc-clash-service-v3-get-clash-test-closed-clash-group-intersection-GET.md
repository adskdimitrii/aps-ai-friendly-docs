# containers/:containerId/tests/:testId/clashes/closed

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-clash-service-v3-get-clash-test-closed-clash-group-intersection-GET/

---

# containers/:containerId/tests/:testId/clashes/closed

Retrieves the state of all closed clash groups in a particular model set, relative to a specified clash test.

This endpoint takes the clashes contained within each closed clash group stored in the system for all clash tests on the same model set, and intersects them with the results of the specified clash test. Clashes which were present when the clash group was first defined can then be resolved.

The response contains a list of closed clash groups, restricted by the number specified by the pageLimit property. If set (that is, if there are more results than can be displayed at once), you can provide the continuationToken property in the response in a separate call to retrieve additional results.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/bim360/clash/v3/containers/:containerId/tests/:testId/clashes/closed Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. x-ads-region enum: string The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

containerId string: UUID The GUID that uniquely identifies the container. testId string: UUID The GUID that uniquely identifies the clash test.

### Request

## Query Parameters

pageLimit int The maximum number of closed clash groups to return in a page. If not set, the default page limit is used, as determined by the server. continuationToken string The token indicating the start of the page. If not set, the first page is retrieved.

### Response

## HTTP Status Code Summary

200 OK Success 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The Retry-After header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

page object Paging information associated with a paging response. continuationToken string A continuation token to retrieve the next page. modelSetId string: UUID The GUID that uniquely identifies the model set. modelSetVersion int The model set version number. groups array: object The list of clash groups intersected with the specified clash test. id string: UUID The unique identifier of the clash group. originalClashTestId string: UUID The unique identifier of the clash test originally associated with the clash group. createdAtVersion int The model set version number associated with the original clash test. existing array: int Clashes contained with the clash group that still exist within the specified clash test. resolved array: int Clashes contained with the clash group that have been resolved.

### Response

## Body Structure (400)

type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field which failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code.

## Example #1 (no query parameters)

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/clash/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/tests/c40b4498-1baa-405d-4fe9-423514bbbf10/clashes/closed' \ -H 'Authorization: Bearer <token>'
```

## Example #2 (with all query parameters)

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/clash/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/tests/c40b4498-1baa-405d-4fe9-423514bbbf10/clashes/closed?pageLimit=134&continuationToken=10' \ -H 'Authorization: Bearer <token>'
```

### Response (200)

```
{ "page" : {}, "modelSetId" : "00fb28a5-e8a4-2755-562a-7c2f0fc87911" , "modelSetVersion" : 94 , "groups" : [ { "id" : "74b70bb8-8802-a1fd-f201-890375a60c8f" , "originalClashTestId" : "dadf49a9-3496-20d1-308d-a9bee3b0a9a4" , "createdAtVersion" : 77 , "existing" : [ 2019963136 ], "resolved" : [ 2019963136 ] } ] }
```

### Response (400)

```
{ "type" : "BadInput" , "title" : "One or more input values in the request were bad" , "detail" : "The following parameters are invalid: containerId" , "errors" : [ { "field" : "containerId" , "title" : "Invalid parameter" , "detail" : "The value 'testing' is not valid." , "type" : "BadInput" } ] }
```
