# projects/:projectId/indexes/:indexId/fields

Source: https://aps.autodesk.com/en/docs/acc/reference/http/index-v2-index-fields-get/

---

# projects/:projectId/indexes/:indexId/fields

Retrieve a specific fields dictionary associated with a properties index. Since the fields dictionary, once created, is immutable, the response will set a long expiration HTTP header for efficient client side caching.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/index/v2/projects/:projectId/indexes/:indexId/fields Authentication Context user context required Required OAuth Scopes data:read Data Format json.gz

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. x-ads-region enum: string The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

projectId string: UUID The project ID. indexId string The index ID.

### Response

## HTTP Status Code Summary

200 OK The response is provided in the [line-delimited JSON streaming format (LDJSON)]( https://de.wikipedia.org/wiki/JSON_streaming )
with the definition of one field per line. 303 Redirect Method The response is provided in the [line-delimited JSON streaming format (LDJSON)]( https://de.wikipedia.org/wiki/JSON_streaming )
with the definition of one field per line. 401 Unauthorized Response in case of an error. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 429 Too Many Requests Rate limit exceeded. Wait some time before retrying. The Retry-After header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

key string The unique identifier for the attribute in file version. category string The property database attribute category, can be null. type enum: string field data type. Possible values: Unknown , Boolean , Integer , Double , Blob , DbKey , String , LocalizableString , DateTime , GeoLocation , Position name string The property database attribute name. uom string The property database attribute data type context or unit of measurement, e.g., âmâ, âftâ, âm^2â, âkip/inch^2â.

Possible values: Unknown , Boolean , Integer , Double , Blob , DbKey , String , LocalizableString , DateTime , GeoLocation , Position

### Response

## Body Structure (303)

key string The unique identifier for the attribute in file version. category string The property database attribute category, can be null. type enum: string field data type. Possible values: Unknown , Boolean , Integer , Double , Blob , DbKey , String , LocalizableString , DateTime , GeoLocation , Position name string The property database attribute name. uom string The property database attribute data type context or unit of measurement, e.g., âmâ, âftâ, âm^2â, âkip/inch^2â.

Possible values: Unknown , Boolean , Integer , Double , Blob , DbKey , String , LocalizableString , DateTime , GeoLocation , Position

### Response

## Body Structure (401)

type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field which failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code.

## Example

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/index/v2/projects/cd743656-f130-48bd-96e6-948175313637/indexes/da39a3ee5e6b4b0d/fields' \ -H 'Authorization: Bearer <token>'
```

### Response (200)

```
{ "key" : "p8e7b8610" , "category" : "Materials and Finishes" , "type" : "Double" , "name" : "Concrete compression" , "uom" : "kip/inch^2" }
```

### Response (303)

```
{ "key" : "p8e7b8610" , "category" : "Materials and Finishes" , "type" : "Double" , "name" : "Concrete compression" , "uom" : "kip/inch^2" }
```

### Response (401)

```
{ "type" : "BadInput" , "title" : "One or more input values in the request were bad" , "detail" : "The following parameters are invalid: containerId" , "errors" : [ { "field" : "containerId" , "title" : "Invalid parameter" , "detail" : "The value 'testing' is not valid." , "type" : "BadInput" } ] }
```
