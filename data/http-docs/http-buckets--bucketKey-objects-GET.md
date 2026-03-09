# buckets/:bucketKey/objects

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-GET/

---

Objects

GET

# buckets/:bucketKey/objects

List objects in a bucket. It is only available to the bucket creator.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/oss/v2/buckets/:bucketKey/objects |
| --- | --- |
| Authentication Context | app-only |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be âBearer `<token>`â, where `<token>` is obtained via [POST token](../../oauth/http-docs/http-gettoken-POST.md). |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| bucketKey*   string | URL-encoded bucket key for which to get details |
| --- | --- |

* Required

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | The number of objects to return in the result set. Acceptable values = 1 - 100. Default = 10. |
| --- | --- |
| beginsWith   string | String to filter the result set by. The result set is restricted to items whose objectKey begins with the provided string. |
| startAt   string | The position to start listing the result set. This parameter is used to request the next set of items, when the response is paginated. The `next` attribute of the response provides the URI for the next result set, complete with the `startAt` parameter pre-populated. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful |
| --- | --- |
| 400   BAD REQUEST | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 401   UNAUTHORIZED | The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify Authentication and try again. |
| 403   FORBIDDEN | The Authorization was successfully validated but permission is not granted. Donât try again unless you solve permissions first. |
| 404   NOT FOUND | The specified bucket does not exist. |
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
          "objectKey": {
            "type": "string"
          },
          "objectId": {
            "type": "string"
          },
          "sha1": {
            "type": "string"
          },
          "size": {
            "type": "integer"
          },
          "location": {
            "type": "string"
          }
        }
      }
    },
    "next": {
      "type": "string"
    }
  }
}

```

Show More

| bucketKey   string | Bucket Key |
| --- | --- |
| objectId   string | Object URN |
| objectKey   string | Object Key |
| sha1   string | Object SHA1 |
| size   integer | Object size |
| location   string | URL to download the object |
| next   string | Next possible request |

## [Example](#example)

Successful object list (200)

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects?limit=1"
  -X GET
  -H "Authorization: Bearer ShiAeQ67rdNSfmyEmtGW8Lnrcqto"
  -H "Content-Type: application/json"

```

### Response

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Content-Type: application/json; charset=utf-8
Date: Sat, 21 May 2016 00:05:30 GMT
Server: Apigee Router
Connection: keep-alive

      {
  "items" : [
    {
      "bucketKey" : "apptestbucket",
      "objectKey" : "objectKeyFoo",
      "objectId" : "urn:adsk.objects:os.object:apptestbucket/objectKeyFoo",
      "sha1" : "cdbf71bfc07cbc18372a5dd4b6e161463cb7fd35",
      "size" : 7,
      "location" : "https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/objectKeyFoo"
    }
  ],
  "next" : "https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects?startAt=objectKeyFoo&limit=1"
}

```

Show More
