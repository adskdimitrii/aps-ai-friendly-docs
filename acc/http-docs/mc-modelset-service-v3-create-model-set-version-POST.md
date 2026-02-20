# containers/:containerId/modelsets/:modelSetId/versions

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-modelset-service-v3-create-model-set-version-POST/

---

# containers/:containerId/modelsets/:modelSetId/versions

Creates a new version of a given model set.

Note that this operation is not guaranteed to result in a new version of the model set being generated. If the folder contents have not changed, or the change does not necessitate a new model set version (for example, the changed models are not valid for use in Model Coordination) then no new model set version is created.

The response contains information about the created model set job.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/bim360/modelset/v3/containers/:containerId/modelsets/:modelSetId/versions Authentication Context user context required Required OAuth Scopes data:create , data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. x-ads-region enum: string The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

containerId string: UUID The GUID that uniquely identifies the container. modelSetId string: UUID The GUID that uniquely identifies the model set.

### Response

## HTTP Status Code Summary

202 Accepted The model set job associated with this request 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The Retry-After header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (202)

jobId string: UUID The GUID that uniquely identifies the job. modelSetId string: UUID The GUID that uniquely identifies the model set associated with the job. resource string The resource associated with the job. createdIssueIds array: string: UUID If this job tracks the creation of model set inspection issues, the IDs of the created issues. status enum: string The current job status. Possible values: Failed , Running , Succeeded , Archived . job object A job. operation string The operation associated with the job. seed object The JSON payload which seeded the job.

### Response

## Body Structure (400)

type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field which failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code.

## Example

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/modelsets/00fb28a5-e8a4-2755-562a-7c2f0fc87911/versions' \ -X POST \ -H 'Authorization: Bearer <token>'
```

### Response (202)

```
{ "jobId" : "49244371-ee08-9afa-01f8-26fcd8ecb03d" , "modelSetId" : "00fb28a5-e8a4-2755-562a-7c2f0fc87911" , "status" : "Succeeded" , "job" : { "operation" : "OperationName" , "seed" : {} } }
```

### Response (400)

```
{ "type" : "BadInput" , "title" : "One or more input values in the request were bad" , "detail" : "The following parameters are invalid: containerId" , "errors" : [ { "field" : "containerId" , "title" : "Invalid parameter" , "detail" : "The value 'testing' is not valid." , "type" : "BadInput" } ] }
```
