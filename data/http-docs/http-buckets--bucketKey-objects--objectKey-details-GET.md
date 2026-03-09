# buckets/:bucketKey/objects/:objectKey/details

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-details-GET/

---

Objects

GET

# buckets/:bucketKey/objects/:objectKey/details

Returns object details in JSON format.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/oss/v2/buckets/:bucketKey/objects/:objectKey/details |
| --- | --- |
| Authentication Context | app-only |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be âBearer `<token>`â, where `<token>` is obtained via [POST token](../../oauth/http-docs/http-gettoken-POST.md). |
| --- | --- |
| If-Modified-Since   HTTP date | If the requested object has not been modified since the time specified in this field, an entity will not be returned from the server; instead, a 304 (not modified) response will be returned without any message body. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| bucketKey*   string | URL-encoded bucket key |
| --- | --- |
| objectKey*   string | URL-encoded object key to get details for |

* Required

### Request

## [Query String Parameters](#query-string-parameters)

| with   enum | Extra information in details; multiple uses are supported Acceptable values: `createdDate`, `lastAccessedDate`, `lastModifiedDate` |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Get object details was successful. |
| --- | --- |
| 304   NOT MODIFIED | This response occurs if the timestamp on the If-Modified-Since header is greater than or equal to the last modified date of the object. |
| 400   BAD REQUEST | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 401   UNAUTHORIZED | The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify Authentication and try again. |
| 403   FORBIDDEN | The Authorization was successfully validated but permission is not granted. Donât try again unless you solve permissions first. |
| 404   NOT FOUND | Object does not exist. |
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
    },
    "blockSizes": {
      "type": "array",
      "items": {
        "type": "integer"
      }
    },
    "deltas": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "position": {
            "type": "integer"
          },
          "sha1": {
            "type": "string"
          }
        }
      }
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
| blockSizes   array | For delta-encoding. Represents whether a signature exists at a specific block size |
| deltas   array | Patch files available for download related to this object |

## [Example](#example)

Get Object Details - Success (200)

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/test.txt/details"
  -X GET
  -H "Authorization: Bearer ShiAeQ67rdNSfmyEmtGW8Lnrcqto"
  -H "Content-Type: application/json"

```

### Response

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Content-Type: application/json; charset=utf-8
Date: Sat, 21 May 2016 00:23:28 GMT
Server: Apigee Router
Content-Length: 401
Connection: keep-alive

{
  "bucketKey" : "apptestbucket",
  "objectId" : "urn:adsk.objects:os.object:apptestbucket/test.txt",
  "objectKey" : "test.txt",
  "sha1" : "33a16388013ce310564af70b0ef5320d8fd85444",
  "size" : 618,
  "contentType" : "application/x-www-form-urlencoded",
  "location" : "https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/test.txt",
  "blockSizes" : [ 2048 ],
  "deltas" : [ ]
}

```

Show More
