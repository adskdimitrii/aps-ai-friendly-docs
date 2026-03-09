# buckets/:bucketKey/objects/:objectKey/copyto/:newObjectKey

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-copyto-:newObjectKey-PUT/

---

Objects

PUT

# buckets/:bucketKey/objects/:objectKey/copyto/:newObjectKey

Copies an object to another object key in the same bucket.

## [Resource Information](#resource-information)

| Method and URI | PUT https://developer.api.autodesk.com/oss/v2/buckets/:bucketKey/objects/:objectKey/copyto/:newObjectKey |
| --- | --- |
| Authentication Context | app-only |
| Required OAuth Scopes | `data:write` or `data:create` (`data:write` allows overwriting existing objects) |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be âBearer `<token>`â, where `<token>` is obtained via [POST token](../../oauth/http-docs/http-gettoken-POST.md). |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| bucketKey*   string | URL-encoded bucket key where object was uploaded into |
| --- | --- |
| objectKey*   string | URL-encoded object key to be use as the copy source |
| newObjectKey*   string | URL-encoded object key to use as the destination |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful copy operation. |
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
    "bucketKey": {
      "type": "string"
    },
    "objectId": {
      "type": "string"
    },
    "objectKey": {
      "type": "string"
    },
    "sha1": {
      "type": "string"
    },
    "size": {
      "type": "integer"
    },
    "contentType": {
      "type": "string"
    },
    "location": {
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
| contentType   string | Object content-type |
| location   string | URL to download the object |

## [Example](#example)

Successful Copy Object (200)

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/buckets/bucketexamplekey/objects/testobject/copyto/copyoftestobject"
  -X PUT
  -H "Authorization=Bearer 1B6FU8z9S2x1PrjADDfPCzSGrXmI"

```

### Response

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Date: Tue, 24 May 2016 20:57:40 GMT
Server: Apigee Router
Content-Length: 0
Connection: keep-alive

{
  "bucketKey" : "bucketexamplekey",
  "objectId" : "urn:adsk.objects:os.object:bucketexamplekey/copyoftestobject",
  "objectKey" : "copyoftestobject",
  "sha1" : "cdbf71bfc07cbc18372a5dd4b6e161463cb7fd35",
  "size" : 7,
  "contentType" : "text/plain; charset=UTF-8",
  "location" : "https://developer.api.autodesk.com/oss/v2/buckets/bucketexamplekey/objects/copyoftestobject"
}

```

Show More
