# projects/:projectId/diffs:batch-status

Source: https://aps.autodesk.com/en/docs/acc/reference/http/index-v2-diff-jobs-batch-status-post/

---

# projects/:projectId/diffs:batch-status

Retrieve the job status for several jobs in a single request.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/construction/index/v2/projects/:projectId/diffs:batch-status Authentication Context user context required Required OAuth Scopes data:read Data Format json

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json . x-ads-force-regenerate-cache boolean If set to true, force regeneration of S3 cache. x-ads-region enum: string The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

projectId string: UUID The project ID.

### Request

## Body Structure

diffs * array: object diffs. Min items: 1 Max items: 1000 prevVersionUrn * string file version urn. curVersionUrn * string file version urn. query object SQL AST for binary expression/filter columns object SQL AST for describing columns/projections

Min items: 1 Max items: 1000

### Response

## HTTP Status Code Summary

200 OK Success 401 Unauthorized Response in case of an error. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 415 Unsupported Media Type The Content-Type header must be application/json . 429 Too Many Requests Rate limit exceeded. Wait some time before retrying. The Retry-After header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

diffs array: object diffs. projectId string project id. diffId string diff id. queryId string query id. type enum: string type. Possible values: DIFF state enum: string job status. Possible values: PROCESSING , FINISHED , FAILED selfUrl string unique url for this job status. prevVersionUrns array: string The previous file versions used in this index. curVersionUrns array: string The current file versions used in this index. updatedAt datetime: ISO 8601 timestamp. retryAt datetime: ISO 8601 timestamp. stats object some higher level diff statistics. added int number of objects added. removed int number of objects removed. modified int number of objects modified. manifestUrl string url for downloading the diff manifest. fieldsUrl string url for downloading the diff fields. propertiesUrl string url for downloading the diff properties. queryResultsUrl string url for downloading the query result. errors array: object errors. type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field which failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code.

Possible values: DIFF

Possible values: PROCESSING , FINISHED , FAILED

### Response

## Body Structure (401)

type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field which failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code.

## Example

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/index/v2/projects/cd743656-f130-48bd-96e6-948175313637/diffs:batchStatus' \ -X POST \ -H 'Authorization: Bearer <token>' \ -H 'Content-Type: application/json' \ -d '{ "diffs": [ { "prevVersionUrn": "urn:adsk.wipstg:fs.file:vf.-7p38avKTMGWp2vcCW568Q?version=2", "curVersionUrn": "urn:adsk.wipstg:fs.file:vf.-7p38avKTMGWp2vcCW568Q?version=2", "query": { " $not ": [ { " s.p123 ": "17" }, { " s.pabc ": " ' \' 'Hello' \' ' " } ] }, "columns": { "a": { "$date_add": [ "YEAR", "5", "' \' '2010-01-01T' \' '" ] }, "b": { "$mul": [ { "$add": [ "5", "s.p789" ] }, "10" ] }, "s.svf2Id": "true" } } ] }'
```

### Response (200)

```
{ "diffs" : [ { "projectId" : "some_project_id" , "diffId" : "fe34bb65aeef" , "queryId" : "4af40764ae14" , "type" : "DIFF" , "selfUrl" : "https://developer.api.autodesk.com/construction/index/v2/projects/some_project_id/diffs/fe34bb65aeef/queries/4af40764ae14" , "prevVersionUrns" : [ "some_version_urn_1" ], "curVersionUrns" : [ "some_version_urn_2" ], "updatedAt" : "2020-09-18T07:44:04.946Z" , "state" : "FINISHED" , "stats" : { "added" : "15" , "removed" : "10" , "modified" : "42" }, "manifestUrl" : "https://developer.api.autodesk.com/construction/index/v2/projects/some_project_id/diffs/fe34bb65aeef/manifest" , "fieldsUrl" : "https://developer.api.autodesk.com/construction/index/v2/projects/some_project_id/diffs/fe34bb65aeef/fields" , "propertiesUrl" : "https://developer.api.autodesk.com/construction/index/v2/projects/some_project_id/diffs/fe34bb65aeef/properties" , "queryResultsUrl" : "https://developer.api.autodesk.com/construction/index/v2/projects/some_project_id/diffs/fe34bb65aeef/queries/4af40764ae14/properties" } ] }
```

### Response (401)

```
{ "type" : "BadInput" , "title" : "One or more input values in the request were bad" , "detail" : "The following parameters are invalid: containerId" , "errors" : [ { "field" : "containerId" , "title" : "Invalid parameter" , "detail" : "The value 'testing' is not valid." , "type" : "BadInput" } ] }
```
