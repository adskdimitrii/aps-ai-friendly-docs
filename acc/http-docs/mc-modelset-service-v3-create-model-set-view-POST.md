# containers/:containerId/modelsets/:modelSetId/views

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-modelset-service-v3-create-model-set-view-POST/

---

# containers/:containerId/modelsets/:modelSetId/views

Creates a view for a given model set.

A view consists of a chosen set of distinct model document lineages that exist within a single model set. You can also supply the ID of a newly uploaded screenshot to associate it with the newly created view.

The response contains information about the created model set view job.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/bim360/modelset/v3/containers/:containerId/modelsets/:modelSetId/views Authentication Context user context required Required OAuth Scopes data:create , data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json x-ads-region enum: string The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

containerId string: UUID The GUID that uniquely identifies the container. modelSetId string: UUID The GUID that uniquely identifies the model set.

### Request

## Body Structure

name * string The name of the model set view. Min length: 1 Max length: 64. description string The description of the model set view. Min length: 1 Max length: 1024. isPrivate * boolean Determines whether the view is only accessible to its creator. definition * array: object The definition of models in a model set view, which is used to track the same models through time. Min items: 1 Max items: 1000. lineageUrn * string The lineage URN of the seed file or document lineage to track with this view. Min length: 1 Max length: 80. viewableName string The name of the viewable in the Model Derivative manifest to track along the seed file lineage. This value is ignored if lineageUrn is the URN of a BIM360 Docs Plans folder document. Min length: 1 Max length: 430. viewId string: UUID The GUID that uniquely identifies the view.

### Response

## HTTP Status Code Summary

202 Accepted The request has been accepted for processing, but the processing has not been completed. 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 415 Unsupported Media Type The Content-Type header must be application/json . 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The Retry-After header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (202)

jobId string: UUID The GUID that uniquely identifies the job. viewId string: UUID The GUID that uniquely identifies the view associated with the job. status enum: string The current job status. Possible values: Failed , Running , Succeeded , Archived . job object A job. operation string The operation associated with the job. seed object The JSON payload which seeded the job.

### Response

## Body Structure (400)

type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field which failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code.

## Example

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/modelsets/00fb28a5-e8a4-2755-562a-7c2f0fc87911/views' \ -X POST \ -H 'Authorization: Bearer <token>' \ -H 'Content-Type: application/json' \ -d '{ "name": "L1 - All disciplines", "description": "All discipline models for Level 1", "isPrivate": false, "definition": [ { "lineageUrn": "urn:adsk.wipprod:dm.lineage:jvMF7mrHR7OwG_DToKsJUA", "viewableName": "Level 1" } ] }'
```

### Response (202)

```
{ "jobId" : "49244371-ee08-9afa-01f8-26fcd8ecb03d" , "viewId" : "7ed27144-ac06-4b72-5dd6-76bee05854be" , "status" : "Succeeded" , "job" : { "operation" : "OperationName" , "seed" : {} } }
```

### Response (400)

```
{ "type" : "BadInput" , "title" : "One or more input values in the request were bad" , "detail" : "The following parameters are invalid: containerId" , "errors" : [ { "field" : "containerId" , "title" : "Invalid parameter" , "detail" : "The value 'testing' is not valid." , "type" : "BadInput" } ] }
```
