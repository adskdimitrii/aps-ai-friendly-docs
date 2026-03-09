# buckets

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-GET/

---

Buckets

GET

# buckets

This endpoint will return the buckets owned by the application. This endpoint supports pagination.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/oss/v2/buckets |
| --- | --- |
| Authentication Context | app-only |
| Required OAuth Scopes | `bucket:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be âBearer `<token>`â, where `<token>` is obtained via [POST token](../../oauth/http-docs/http-gettoken-POST.md). |
| --- | --- |
| region   enum | The region where the buckets reside. Possible values:       - `US` - (Default) Data center for the US region.   - `EMEA` - Data center for the Europe, Middle East, and Africa regions.   - `AUS` - (Beta) Data center for the Australia region.   - `CAN` - Data centre for the Canada region.   - `DEU` - Data centre for the Germany region.   - `IND` - Data centre for the India region.   - `JPN` - Data centre for the Japan region.   - `GBR` - Data centre for the United Kingdom region.       **Note**:       1. Beta features are subject to change. Please avoid using them in production environments.   2. If you specify the `region` header as well as the `region` query parameter, the `region` header takes precedence. |

* Required

### Request

## [Query String Parameters](#query-string-parameters)

| region   enum | The region where the buckets reside. Possible values:       - `US` - (Default) Data center for the US region.   - `EMEA` - Data center for the Europe, Middle East, and Africa regions.   - `AUS` - (Beta) Data center for the Australia region.   - `CAN` - Data centre for the Canada region.   - `DEU` - Data centre for the Germany region.   - `IND` - Data centre for the India region.   - `JPN` - Data centre for the Japan region.   - `GBR` - Data centre for the United Kingdom region.       **Note**:       1. Beta features are subject to change. Please avoid using them in production environments.   2. If you specify the `region` header as well as the `region` query parameter, the `region` header takes precedence. |
| --- | --- |
| limit   int | Limit to the response size,   Acceptable values: 1-100 Default = 10 |
| startAt   string | Key to use as an offset to continue pagination This is typically the last bucket key found in a preceding GET buckets response |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK |  |
| --- | --- |
| 400   BAD REQUEST | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 401   UNAUTHORIZED | The supplied authorization header was not valid or the supplied token scope was not acceptable. Verify authentication and try again. |
| 403   FORBIDDEN | Caller is not authorized to call this endpoint. |
| 404   NOT FOUND | Resource not found. |
| 500   INTERNAL SERVER ERROR | Internal failure while processing the request, reason depends on error. |

### Response

## [Body Structure (200)](#body-structure-200)

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "bucketKey": {
            "type": "string"
          },
          "createDate": {
            "type": "integer"
          },
          "policyKey": {
            "type": "string"
          }
        },
        "required": [
          "bucketKey",
          "createDate",
          "policyKey"
        ]
      }
    },
    "next": {
      "type": "string"
    }
  },
  "required": [
    "items",
    "next"
  ]
}

```

Show More

| items   array(buckets) | Array of items representing the buckets |
| --- | --- |
| bucketKey   string | Bucket key |
| createdDate   long | Timestamp in epoch time |
| policyKey   string | Policy values: `transient`, `temporary`, `persistent` |
| next   string | Next possible request |

## [Example 1](#example-1)

Basic Successful List Bucket (200)

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/buckets"
  -X GET
  -H "Authorization: Bearer RhS6iEVMnEfl77MBSK3l2je06UHj"

```

### Response

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Content-Type: application/json; charset=utf-8
Date: Wed, 25 May 2016 15:40:37 GMT
Server: Apigee Router
Content-Length: 1273
Connection: keep-alive
{
  "items" : [ {
    "bucketKey" : "00001fbf-8505-49ab-8a42-44c6a96adbd0",
    "createdDate" : 1441329298362,
    "policyKey" : "transient"
  }, {
    "bucketKey" : "0003114d",
    "createdDate" : 1440119769765,
    "policyKey" : "transient"
  }, {
    "bucketKey" : "0003fbc1-389a-4194-915a-38313797d753",
    "createdDate" : 1453886285506,
    "policyKey" : "transient"
  }, {
    "bucketKey" : "00048aa5",
    "createdDate" : 1436255268102,
    "policyKey" : "transient"
  }, {
    "bucketKey" : "000524bf",
    "createdDate" : 1453197455111,
    "policyKey" : "transient"
  }, {
    "bucketKey" : "0006db6d",
    "createdDate" : 1461978883040,
    "policyKey" : "transient"
  }, {
    "bucketKey" : "00074953-5d83-4aeb-b598-8f727703c94e",
    "createdDate" : 1447934893704,
    "policyKey" : "transient"
  }, {
    "bucketKey" : "00085601-78b2-44e4-82f3-a252fde022d2",
    "createdDate" : 1441504885576,
    "policyKey" : "transient"
  }, {
    "bucketKey" : "000b1e61-216e-4480-bcd3-9ec5ca56364f",
    "createdDate" : 1448268266859,
    "policyKey" : "transient"
  }, {
    "bucketKey" : "000e37cc",
    "createdDate" : 1437441338604,
    "policyKey" : "transient"
  } ],
  "next" : "https://developer.api.autodesk.com/oss/v2/buckets?region=US&startAt=000e37cc"
}

```

Show More

## [Example 2](#example-2)

List Bucket - Invalid Limit (400)

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/buckets?limit=300"
  -X GET
  -H "Authorization: Bearer R4wQlRMQJgAtRG3IeD0IQ2Wwyk8C"

```

### Response

```
HTTP/1.1 400 Bad Request
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Content-Type: application/json; charset=utf-8
Date: Wed, 25 May 2016 15:44:43 GMT
Server: Apigee Router
Content-Length: 26
Connection: keep-alive

{"reason":"Invalid limit"}

```

Show More
