# buckets/:bucketKey/objects/:objectKey/signed

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signed-POST/

---

Objects

POST

# buckets/:bucketKey/objects/:objectKey/signed

This endpoint creates a signed URL that can be used to download an object within the specified expiration time.
Be aware that if the object the signed URL points to is deleted or expires before the signed URL expires, then the signed URL will no longer be valid. You can also set the URL to expire after it is used the first time, and you can set read or write access to the URL.
A successful call to this endpoint requires bucket owner access.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/oss/v2/buckets/:bucketKey/objects/:objectKey/signed |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be “Bearer `<token>`”, where `<token>` is obtained via [POST token](../../oauth/http-docs/http-gettoken-POST.md). |
| --- | --- |
| Content-Type*   string | Must be `application/json`. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| bucketKey*   string | URL-encoded bucket key |
| --- | --- |
| objectKey*   string | URL-encoded object key to create signed URL for |

* Required

### Request

## [Query String Parameters](#query-string-parameters)

| useCdn   boolean | If true, this will generate a CloudFront URL for the S3 object |
| --- | --- |
| access   enum: string | Access for signed resource Acceptable values: `read`, `write`, `readwrite` Default value: `read` |

### Request

## [Body Structure](#body-structure)

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "minutesExpiration": {
        "type": "integer"
    },
    "singleUse": {
        "type": "boolean"
    }
  }
}

```

Show More

| minutesExpiration   integer | expiration time in minutes; default: `60` |
| --- | --- |
| singleUse   boolean | `true` if the URL will expire after it is used the first time. If you download the object, the URL will expire when the download is complete; default: `false` |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK |  |
| --- | --- |
| 400   BAD REQUEST | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 401   UNAUTHORIZED | The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify Authentication and try again. |
| 403   FORBIDDEN | The Authorization was successfully validated but permission is not granted. Don’t try again unless you solve permissions first. |
| 404   NOT FOUND | Object does not exist |
| 500   INTERNAL SERVER ERROR | Internal failure while processing the request, reason depends on error |

### Response

## [Body Structure (200)](#body-structure-200)

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "signedUrl": {
        "type": "string"
    },
    "expiration": {
        "type": "integer"
    },
    "singleUse": {
        "type": "boolean"
    }
  },
  "required": ["signedUrl", "expiration", "singleUse"]
}

```

Show More

| signedUrl   string | URL created for downloading the object |
| --- | --- |
| expiration   integer | Epoch time stamp for when the public URL will expire |
| singleUse   boolean | Indicates if the URL expires after it is used the first time |

## [Example 1](#example-1)

Successful Creation of Signed URL (200)

### Request

```
curl
  -X POST
  -H "Authorization=Bearer eYeL5gYxAT2j3u9TEerxoJoToNbi"
  -H "Content-Type=application/json;charset=UTF-8";
  --data '{ }'
  https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/objectKeyFoo/signed

```

### Response

```
HTTP/1.1 200 OK

{
  "signedUrl" : "https://developer.api.autodesk.com/oss/v2/apptestbucket/758955fa-58fa-46ba-a906-11fe2a3a1a08?region=US",
  "expiration" : 1462989939869,
  "singleUse" : false
}

```

## [Example 2](#example-2)

Successful Creation of Signed URL with Expiration Time and Read Access (200)

### Request

```
curl
  -X POST
  -H "Authorization: Bearer L1yVvPcJDWel0oV3xlYnq7AMZIQE"
  -H "Content-Type: application/json;charset=UTF-8"
  --data '
    {
      "minutesExpiration" : 30
    }'
  https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/test.txt/signed?access=read

```

Show More

### Response

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Content-Type: application/json; charset=utf-8
Date: Wed, 25 May 2016 01:30:09 GMT
Server: Apigee Router
Content-Length: 147
Connection: keep-alive

{
  "signedUrl":"https://developer.api.autodesk.com/oss/v2/apptestbucket/9d3be632-a4fc-457d-bc5d-9e75cefc54b7?region=US",
  "expiration":1464141609620
  "singleUse" : false
}

```

Show More

## [Example 3](#example-3)

Successful Creation of Signed, Single-Use URL with Expiration Time and Read-Write Access (200)

### Request

```
curl
  -X POST
  -H "Authorization: Bearer L1yVvPcJDWel0oV3xlYnq7AMZIQE"
  -H "Content-Type: application/json;charset=UTF-8" signed?access=write
  --data '
    {
      "minutesExpiration" : 45
      "singleUse" : true
    }'
  https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/test.txt/signed?access=readwrite

```

Show More

### Response

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Content-Type: application/json; charset=utf-8
Date: Wed, 25 May 2016 01:30:09 GMT
Server: Apigee Router
Content-Length: 147
Connection: keep-alive

{
  "signedUrl":"https://developer.api.autodesk.com/oss/v2/apptestbucket/9d3be632-a4fc-457d-bc5d-9e75cefc54b7?region=US",
  "expiration":1464141609620,
  "singleUse":true
}

```

Show More

## [Example 4](#example-4)

Successful Creation of Signed, Single-Use URL with Expiration Time using CloudFront (200)

### Request

```
curl
  -X POST
  -H "Authorization: Bearer L1yVvPcJDWel0oV3xlYnq7AMZIQE"
  -H "Content-Type: application/json;charset=UTF-8" signed?access=write
  --data '
    {
      "minutesExpiration" : 45
      "singleUse" : true
    }'
  https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/test.txt/signed?useCdn=true

```

Show More

### Response

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Content-Type: application/json; charset=utf-8
Date: Wed, 25 May 2016 01:30:09 GMT
Server: Apigee Router
Content-Length: 147
Connection: keep-alive

{
  "signedUrl": "https://cdn.oss.api.autodesk.com/oss/v2/signedresources/42231c8b-0132-4218-86b2-30c68150697d?region=US",
  "expiration":1464141609620,
  "singleUse":true
}

```

Show More
