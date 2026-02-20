# containers/:containerId/tests/:testId/clashes/assigned

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-clash-service-v3-get-assigned-clash-group-batch-POST/

---

# containers/:containerId/tests/:testId/clashes/assigned

Retrieves the state of the specified assigned clash groups, relative to a specified clash test.

This endpoint takes the clashes contained within each specified assigned clash group, and intersects them with the results of the specified clash test. Clashes that were present when the clash group was first defined may have been resolved in this clash test.

This method can accept either a list of assigned clash group IDs or a list of BIM 360 Issue GUIDs. To retrieve results by BIM 360 Issue GUID, set the issues query parameter to true.

The response contains a list of assigned clash groups.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/bim360/clash/v3/containers/:containerId/tests/:testId/clashes/assigned Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json x-ads-region enum: string The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

containerId string: UUID The GUID that uniquely identifies the container. testId string: UUID The GUID that uniquely identifies the clash test.

### Request

## Query Parameters

issues boolean If set to true, the query is performed on issue IDs instead of clash group IDs.

### Request

## Body Structure

array: string: UUID * array: string: UUID The list of clash group IDs OR BIM 360 issue IDs to query (depending on the value of the issues query parameter). Min items: 1 Max items: 20.

### Response

## HTTP Status Code Summary

200 OK Success 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 415 Unsupported Media Type The Content-Type header must be application/json . 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The Retry-After header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

id string: UUID The unique identifier of the assigned clash group. clashTestId string: UUID The unique identifier of the clash test associated with the assigned clash group. issueId string: UUID The unique identifier of the issue associated with the assigned clash group. createdBy string The unique identifier of the user who created the assigned clash group. createdOn datetime: ISO 8601 The date and time that the assigned clash group was created. clashData object The clash data associated with a clash group. documents array: object The documents associated with the clash groups supplied. id int The document index ID. urn string The document URN. viewableName string The viewable name of the document in the model set version. clashes array: object The clashes associated with the clash groups supplied. id int The clash index ID. clash array: int The clash instance index ID. Min items: 2 Max items: 2. dist int The clash distance. status string The status of the clash. clashInstances array: object The clash instances associated with the clash groups supplied. cid int The clash ID in the model set version. ldid int The left-hand-side document ID. loid int The left-hand-side object ID. lvid int The left-hand-side viewable ID. rdid int The right-hand-side document ID. roid int The right-hand-side object ID. rvid int The left-hand-side viewable ID.

### Response

## Body Structure (400)

type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field which failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code.

## Example #1 (no query parameters)

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/clash/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/tests/c40b4498-1baa-405d-4fe9-423514bbbf10/clashes/assigned' \ -X POST \ -H 'Authorization: Bearer <token>' \ -H 'Content-Type: application/json' \ -d '[ "d98c1dd4-008f-04b2-e980-0998ecf8427e" ]'
```

## Example #2 (with all query parameters)

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/clash/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/tests/c40b4498-1baa-405d-4fe9-423514bbbf10/clashes/assigned?issues=True' \ -X POST \ -H 'Authorization: Bearer <token>' \ -H 'Content-Type: application/json' \ -d '[ "d98c1dd4-008f-04b2-e980-0998ecf8427e" ]'
```

### Response (200)

```
[ { "id" : "74b70bb8-8802-a1fd-f201-890375a60c8f" , "clashTestId" : "21469f89-986a-c194-ae45-cefade1c7bde" , "issueId" : "53e6a6c7-5bc9-7b2d-920b-b73efecd8fc1" , "createdBy" : "PD23PXGV8V3V" , "createdOn" : "2015-10-21T16:32:22Z" , "clashData" : { "documents" : [ { "id" : 184 , "urn" : "urn:adsk.wipprod:fs.file:vf.jvMF7mrHR7OwG_DToKsJUA?version=1" , "viewableName" : "Level 1" } ], "clashes" : [ { "id" : 184 , "clash" : [ 212 ], "dist" : 114.1678367952799 , "status" : "New" } ], "clashInstances" : [ { "cid" : 75 , "ldid" : 1 , "loid" : 91 , "lvid" : 69 , "rdid" : 147 , "roid" : 246 , "rvid" : 243 } ] } } ]
```

### Response (400)

```
{ "type" : "BadInput" , "title" : "One or more input values in the request were bad" , "detail" : "The following parameters are invalid: containerId" , "errors" : [ { "field" : "containerId" , "title" : "Invalid parameter" , "detail" : "The value 'testing' is not valid." , "type" : "BadInput" } ] }
```
