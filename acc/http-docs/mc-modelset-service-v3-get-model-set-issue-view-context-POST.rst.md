# containers/:containerId/issues/viewcontext

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-modelset-service-v3-get-model-set-issue-view-context-POST.rst/

---

# containers/:containerId/issues/viewcontext

Retrieves the view context around a set of visual inspection issues, such as the model set and documents with which it is associated.

The BIM360 Issues API can be used to obtain individual issues. See GET issues/:issueId for more information.

The response contains context for the set of visual inspection issues.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/bim360/modelset/v3/containers/:containerId/issues/viewcontext Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json x-ads-region enum: string The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

containerId string: UUID The GUID that uniquely identifies the container.

### Request

## Body Structure

array: string: UUID * array: string: UUID The set of issue IDs to find the view context objects for. Min items: 1 Max items: 1.

### Response

## HTTP Status Code Summary

200 OK The set of inspection issue view context objects. 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 415 Unsupported Media Type The Content-Type header must be application/json . 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The Retry-After header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

issueId string: UUID The ID of the inspection issue for retrieving the issue. modelSetId string: UUID The ID of the model set with which inspection issue is associated. documents array: object The list of documents visible when the issue was created. lineageUrn string The lineage URN of the seed file or document lineage to track with this view. Min length: 1 Max length: 80. viewableName string The name of the viewable in the Model Derivative manifest to track along the seed file lineage. This value is ignored if lineageUrn is the URN of a BIM360 Docs Plans folder document. Min length: 1 Max length: 430.

### Response

## Body Structure (400)

type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field which failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code.

## Example

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/issues/viewcontext' \ -X POST \ -H 'Authorization: Bearer <token>' \ -H 'Content-Type: application/json' \ -d '[ "d98c1dd4-008f-04b2-e980-0998ecf8427e" ]'
```

### Response (200)

```
[ { "issueId" : "53e6a6c7-5bc9-7b2d-920b-b73efecd8fc1" , "modelSetId" : "00fb28a5-e8a4-2755-562a-7c2f0fc87911" , "documents" : [ { "lineageUrn" : "urn:adsk.wipprod:dm.lineage:jvMF7mrHR7OwG_DToKsJUA" , "viewableName" : "Level 1" } ] } ]
```

### Response (400)

```
{ "type" : "BadInput" , "title" : "One or more input values in the request were bad" , "detail" : "The following parameters are invalid: containerId" , "errors" : [ { "field" : "containerId" , "title" : "Invalid parameter" , "detail" : "The value 'testing' is not valid." , "type" : "BadInput" } ] }
```
