# containers/:containerId/modelsets/:modelSetId/screenshots

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-clash-service-v3-add-screen-shot-POST/

---

# containers/:containerId/modelsets/:modelSetId/screenshots

Uploads a screenshot, associating it with a given model set.

The new screenshot cannot be retrieved from the service until it has been associated with a closed clash group. It can also be associated with an assigned clash group, in which case it becomes available as an attachment to the created BIM 360 Issue.

Returns a token representing the uploaded screenshot.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/bim360/clash/v3/containers/:containerId/modelsets/:modelSetId/screenshots Authentication Context user context required Required OAuth Scopes data:create , data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be image/png x-ads-region enum: string The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

containerId string: UUID The GUID that uniquely identifies the container. modelSetId string: UUID The GUID that uniquely identifies the model set.

### Request

## Body Structure

binary * binary The raw screenshot image binary data to upload.

### Response

## HTTP Status Code Summary

200 OK Success 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 415 Unsupported Media Type The Content-Type header must be image/png . 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The Retry-After header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

id string: UUID The temporary ID of the new screenshot. size int The size of the screenshot in bytes.

### Response

## Body Structure (400)

type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field which failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code.

## Example

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/clash/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/modelsets/00fb28a5-e8a4-2755-562a-7c2f0fc87911/screenshots' \ -X POST \ -H 'Authorization: Bearer <token>' \ -H 'Content-Type: image/png' \ --data-binary image.png
```

### Response (200)

```
{ "id" : "74b70bb8-8802-a1fd-f201-890375a60c8f" , "size" : 3722098081 }
```

### Response (400)

```
{ "type" : "BadInput" , "title" : "One or more input values in the request were bad" , "detail" : "The following parameters are invalid: containerId" , "errors" : [ { "field" : "containerId" , "title" : "Invalid parameter" , "detail" : "The value 'testing' is not valid." , "type" : "BadInput" } ] }
```
