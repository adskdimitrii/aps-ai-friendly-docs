# containers/:containerId/tests/:testId/resources

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-clash-service-v3-get-clash-test-resources-GET/

---

# containers/:containerId/tests/:testId/resources

Retrieves information about a given clash test result resources.

When a clash test against a model set version is successful it produces three file resources that contain the raw clash instances and the documents (models) to which these clash results pertain. See the Field Guide section of the API documentation for details.

Returns a list of URLs and secure headers necessary to access the resources generated for the given clash test.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/bim360/clash/v3/containers/:containerId/tests/:testId/resources Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. x-ads-region enum: string The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

containerId string: UUID The GUID that uniquely identifies the container. testId string: UUID The GUID that uniquely identifies the clash test.

### Response

## HTTP Status Code Summary

200 OK Success 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The Retry-After header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

page object Paging information associated with a paging response. continuationToken string A continuation token to retrieve the next page. resources array: object A list of clash test resources. type string The type of the clash test resource. extension enum: string The file extension used by the clash test resource. Possible values: json.gz , sqlite . url string The URL used to retrieve the clash test resource. headers object The headers used to retrieve the clash test resource. validUntil datetime: ISO 8601 The time in UTC that the request will stop working.

### Response

## Body Structure (400)

type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field which failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code.

## Example

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/clash/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/tests/c40b4498-1baa-405d-4fe9-423514bbbf10/resources' \ -H 'Authorization: Bearer <token>'
```

### Response (200)

```
{ "page" : {}, "resources" : [ { "type" : "scope-version-clash.1.0.0" , "extension" : "json.gz" , "url" : "https://example.com/6f760056-db07-4239-ba4c-d9739ac50142/file.json.gz?token=da39a3ee5e6b4b0d3255bfef95601890afd80709" , "headers" : {}, "validUntil" : "2015-10-21T16:29:19Z" } ] }
```

### Response (400)

```
{ "type" : "BadInput" , "title" : "One or more input values in the request were bad" , "detail" : "The following parameters are invalid: containerId" , "errors" : [ { "field" : "containerId" , "title" : "Invalid parameter" , "detail" : "The value 'testing' is not valid." , "type" : "BadInput" } ] }
```
