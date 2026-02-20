# containers/:containerId/relationships:delete

Source: https://aps.autodesk.com/en/docs/acc/reference/http/relationship-service-v2-delete-relationships-POST/

---

# containers/:containerId/relationships:delete

Deletes one or more relationships by passing an array of relationship UUIDs.

Note that when a relationship is deleted, it is âsoftâ deleted, meaning it can still be retrieved by using the search endpoints. See GET relationships:search for more information.

Note that in order to delete a relationship, you must have access to both entities in the relationship.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/bim360/relationship/v2/containers/:containerId/relationships:delete Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json x-ads-region enum: string The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

containerId string: UUID The project ID.

### Request

## Body Structure

array: string: UUID * array: string: UUID The list of relationships (UUIDs) to delete. Min items: 1 Max items: 50

Min items: 1 Max items: 50

### Response

## HTTP Status Code Summary

200 OK Success 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 415 Unsupported Media Type The Content-Type header must be application/json . 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The Retry-After header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

deleted array: string: UUID The list of UUIDs that uniquely identify the deleted relationships.

### Response

## Body Structure (400)

type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field that failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code.

## Example

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/fbd6cb57-7d0e-4961-8c2c-69646514ef44/relationships:delete' \ -X POST \ -H 'Authorization: Bearer <token>' \ -H 'Content-Type: application/json' \ -d '[ "d98c1dd4-008f-04b2-e980-0998ecf8427e" ]'
```

### Response (200)

```
{ "deleted" : [ "d98c1dd4-008f-04b2-e980-0998ecf8427e" ] }
```

### Response (400)

```
{ "type" : "BadInput" , "title" : "One or more input values in the request were bad" , "detail" : "The following parameters are invalid: containerId" , "errors" : [ { "field" : "containerId" , "title" : "Invalid parameter" , "detail" : "The value 'testing' is not valid." , "type" : "BadInput" } ] }
```
