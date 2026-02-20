# error-codes

Source: https://aps.autodesk.com/en/docs/acc/reference/http/assets-error-codes-GET/

---

# error-codes

Retrieves a list of all error codes returned by the Assets API.

You can use this information to allow the client to better handle error responses programmatically.

Note that although the response is in a paginated format, all results will be returned for every request.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/assets/v1/error-codes Authentication Context No security required Required OAuth Scopes No scopes required Data Format JSON

### Response

## HTTP Status Code Summary

200 OK Successfully retrieved all error codes. 401 Unauthorized The request was not accepted because it lacked valid authentication credentials 403 Forbidden The request was not accepted because the client is authenticated, but is not authorized to access the target resource 404 Not Found The resource cannot be found 429 Too Many Requests The request was not accepted because the rate limit was exceeded due to too many requests being made. 500 Internal Server Error An unexpected error occurred on the server

### Response

## Body Structure (200)

pagination object The pagination object. limit int Always equal to totalResults (Pagination is not used by this endpoint. This object is returned for backward compatibility.). offset int Always equal to 0 (Pagination is not used by this endpoint. This object is returned for backward compatibility.). totalResults int The total number of results returned. results array: object A list of Assets API errors. name string The error code name. description string A description of the error. httpStatusCode number The HTTP status code typically returned when this error occurs. Note that there may be exceptions, for example, if an internal server error
occurs the status code associated with this error may be different. metadataKeys array: string The metadata keys relevant to the error code.

Note that there may be exceptions, for example, if an internal server error
occurs the status code associated with this error may be different.

## Example

Successfully retrieved all error codes.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/assets/v1/error-codes'
```

### Response

```
{ "pagination" : { "limit" : 61 , "offset" : 0 , "totalResults" : 61 }, "results" : [ { "name" : "FIELD_EXCEEDS_MAX_LENGTH" , "description" : "A string field exceeds the max allowed length." , "httpStatusCode" : 400 , "metadataKeys" : [ "fieldName" , "maxStringLength" ] } ] }
```
