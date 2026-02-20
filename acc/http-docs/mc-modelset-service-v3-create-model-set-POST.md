# containers/:containerId/modelsets

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-modelset-service-v3-create-model-set-POST/

---

# containers/:containerId/modelsets

Creates a model set within a given container specifying the folder used to determine the set of model document lineages comprising the model set.

Currently only a single folder is supported; however, sub-folders are supported.

The response contains information about the created model set job.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/bim360/modelset/v3/containers/:containerId/modelsets Authentication Context user context required Required OAuth Scopes data:create , data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json x-ads-region enum: string The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

containerId string: UUID The GUID that uniquely identifies the container in which the model set is created.

### Request

## Body Structure

modelSetId string: UUID The GUID that uniquely identifies the model set. If this value is not supplied a new GUID is created. name * string The name of the model set. This name must be unique within the specified container. Min length: 1 Max length: 64. description string A textual description of the model set. Min length: 1 Max length: 1024. isDisabled boolean Indicates if new versions are created for model set changes. folders * array: object A single folder URN that contains a set of document lineages that are added to the model set. Min items: 1 Max items: 1. folderUrn * string The ID of the folder in your project (can be found using the Data Management API).

### Response

## HTTP Status Code Summary

202 Accepted The model set job associated with this request 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 409 Conflict Limit exceeded for enabled model sets, create a disabled model set or disable an existing model set, or a model set with the same name already exists. 415 Unsupported Media Type The Content-Type header must be application/json . 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The Retry-After header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (202)

jobId string: UUID The GUID that uniquely identifies the job. modelSetId string: UUID The GUID that uniquely identifies the model set associated with the job. resource string The resource associated with the job. createdIssueIds array: string: UUID If this job tracks the creation of model set inspection issues, the IDs of the created issues. status enum: string The current job status. Possible values: Failed , Running , Succeeded , Archived . job object A job. operation string The operation associated with the job. seed object The JSON payload which seeded the job.

### Response

## Body Structure (400)

type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field which failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code.

### Response

## Body Structure (409)

type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field which failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code.

## Example

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/modelsets' \ -X POST \ -H 'Authorization: Bearer <token>' \ -H 'Content-Type: application/json' \ -d '{ "name": "Formal Coordination", "description": "Space for coordinating all disciplines", "folders": [ { "folderUrn": "urn:adsk.wipprod:fs.folder:co.WI8roO18TU2Cl3P9y64z4w" } ] }'
```

### Response (202)

```
{ "jobId" : "49244371-ee08-9afa-01f8-26fcd8ecb03d" , "modelSetId" : "00fb28a5-e8a4-2755-562a-7c2f0fc87911" , "status" : "Succeeded" , "job" : { "operation" : "OperationName" , "seed" : {} } }
```

### Response (400)

```
{ "type" : "BadInput" , "title" : "One or more input values in the request were bad" , "detail" : "The following parameters are invalid: containerId" , "errors" : [ { "field" : "containerId" , "title" : "Invalid parameter" , "detail" : "The value 'testing' is not valid." , "type" : "BadInput" } ] }
```

### Response (409)

```
{ "type" : "BadInput" , "title" : "One or more input values in the request were bad" , "detail" : "The following parameters are invalid: containerId" , "errors" : [ { "field" : "containerId" , "title" : "Invalid parameter" , "detail" : "The value 'testing' is not valid." , "type" : "BadInput" } ] }
```
