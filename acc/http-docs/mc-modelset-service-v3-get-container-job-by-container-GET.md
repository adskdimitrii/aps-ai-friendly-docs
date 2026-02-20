# containers/:containerId/jobs/:jobId

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-modelset-service-v3-get-container-job-by-container-GET/

---

# containers/:containerId/jobs/:jobId

Retrieves information about a given container job.

All calls to the containers resource result in a job. You can use this endpoint to track the progress of these jobs.

You can find the x-ads-region to use from the GET hubs endpoint, under data.attributes.region . See GET hubs/:hub_id for more information.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/bim360/modelset/v3/containers/:containerId/jobs/:jobId Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. x-ads-region * enum: string The region the container resides in. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

containerId string: UUID The GUID that uniquely identifies the container. jobId string: UUID The GUID that uniquely identifies the job.

### Response

## HTTP Status Code Summary

200 OK Success 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The Retry-After header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

jobId string: UUID The GUID that uniquely identifies the job. containerId string: UUID The GUID that uniquely identifies the container associated with the job. status enum: string The current job status. Possible values: Failed , Running , Succeeded , Archived . job object A job. operation string The operation associated with the job. seed object The JSON payload which seeded the job.

### Response

## Body Structure (400)

type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field which failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code.

## Example

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/jobs/49244371-ee08-9afa-01f8-26fcd8ecb03d' \ -H 'Authorization: Bearer <token>'
```

### Response (200)

```
{ "jobId" : "49244371-ee08-9afa-01f8-26fcd8ecb03d" , "containerId" : "f0f4f36a-ac64-687f-b132-8efe04b22454" , "status" : "Succeeded" , "job" : { "operation" : "OperationName" , "seed" : {} } }
```

### Response (400)

```
{ "type" : "BadInput" , "title" : "One or more input values in the request were bad" , "detail" : "The following parameters are invalid: containerId" , "errors" : [ { "field" : "containerId" , "title" : "Invalid parameter" , "detail" : "The value 'testing' is not valid." , "type" : "BadInput" } ] }
```
