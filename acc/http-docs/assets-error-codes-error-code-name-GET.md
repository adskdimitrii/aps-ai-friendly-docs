# error-codes/:errorCodeName

Source: https://aps.autodesk.com/en/docs/acc/reference/http/assets-error-codes-error-code-name-GET/

---

Error-Codes

GET

# error-codes/:errorCodeName

Retrieves details about an error code by name.

To find a list of error codes, call [GET error-codes](en/docs/acc/v1/reference/http/assets-error-codes-GET/).

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/assets/v1/error-codes/{errorCodeName} |
| --- | --- |
| Authentication Context | No security required |
| Required OAuth Scopes | No scopes required |
| Data Format | JSON |

### Request

## [URI Parameters](#uri-parameters)

| errorCodeName   string | The name of an error code returned in an error response, in the `errorCode` field. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the error code details. |
| --- | --- |
| 401   Unauthorized | The request was not accepted because it lacked valid authentication credentials |
| 403   Forbidden | The request was not accepted because the client is authenticated, but is not authorized to access the target resource |
| 404   Not Found | The resource cannot be found |
| 429   Too Many Requests | The request was not accepted because the rate limit was exceeded due to too many requests being made. |
| 500   Internal Server Error | An unexpected error occurred on the server |

### Response

## [Body Structure (200)](#body-structure-200)

| name   string | The error code name. |
| --- | --- |
| description   string | A description of the error. |
| httpStatusCode   number | The HTTP status code typically returned when this error occurs. <br>Note that there may be exceptions, for example, if an internal server error occurs the status code associated with this error may be different. |
| metadataKeys   array: string | The metadata keys relevant to the error code. |

## [Example](#example)

Successfully retrieved the error code details.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/assets/v1/error-codes/FIELD_EXCEEDS_MAX_LENGTH'

```

### Response

```
{
  "name": "FIELD_EXCEEDS_MAX_LENGTH",
  "description": "A string field exceeds the max allowed length.",
  "httpStatusCode": 400,
  "metadataKeys": [
    "fieldName",
    "maxStringLength"
  ]
}

```

Show More
