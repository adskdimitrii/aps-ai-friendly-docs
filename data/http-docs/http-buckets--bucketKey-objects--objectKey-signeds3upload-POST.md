# buckets/:bucketKey/objects/:objectKey/signeds3upload

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-POST/

---

Objects

POST

# buckets/:bucketKey/objects/:objectKey/signeds3upload

Instructs OSS to complete the object creation process after the bytes have been uploaded directly to S3.

An object will not be accessible until this endpoint is called. This endpoint must be called within 24 hours of the upload beginning, otherwise the object will be discarded, and the upload must begin again from scratch.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/oss/v2/buckets/:bucketKey/objects/:objectKey/signeds3upload |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:write` `data:create` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be “Bearer `<token>`”, where `<token>` is obtained via [POST token](../../oauth/http-docs/http-gettoken-POST.md). |
| --- | --- |
| Content-Type*   string | Must be exactly “application/json”. |
| x-ads-meta-Content-Type   string | The Content-Type value that OSS will store in the record for the uploaded object. |
| x-ads-meta-Content-Disposition   string | The Content-Disposition value that OSS will store in the record for the uploaded object. |
| x-ads-meta-Content-Encoding   string | The Content-Encoding value that OSS will store in the record for the uploaded object. |
| x-ads-meta-Cache-Control   string | The Cache-Control value that OSS will store in the record for the uploaded object. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| bucketKey*   string | URL-encoded bucket key |
| --- | --- |
| objectKey*   string | URL-encoded object key to create signed URL for |

* Required

### Request

## [Body Structure](#body-structure)

| uploadKey*   string | The identifier of the upload session, which was provided by OSS in the response to the Get Upload URL/s request. |
| --- | --- |
| size   integer | The expected size of the uploaded object. If provided, OSS will check this against the blob in S3 and return an error if the size does not match. |
| eTags   array: string | An array of eTags. S3 returns an eTag to each upload request, be it for a chunk or an entire file. For a single-part upload, this array contains the expected eTag of the entire object. For a multipart upload, this array contains the expected eTag of each part of the upload; the index of an eTag in the array corresponds to its part number in the upload. If provided, OSS will validate these eTags against the content in S3, and return an error if the eTags do not match (indicating some form of data corruption). |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK |  |
| --- | --- |
| 400   BAD REQUEST | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications.   The response body may give an indication of what is wrong with the request. |
| 401   UNAUTHORIZED | The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify Authentication and try again. |
| 403   FORBIDDEN | The Authorization was successfully validated but permission is not granted. Don’t try again unless you solve permissions first. |
| 404   NOT FOUND | Object or bucket does not exist |
| 429   RATE-LIMIT EXCEEDED | The maximum number of API calls that an app can make per minute was exceeded. |
| 500   INTERNAL SERVER ERROR | Internal failure while processing the request, reason depends on error |

### Response

## [Body Structure (200)](#body-structure-200)

| bucketKey   string | The key of the bucket into which the object has been uploaded. |
| --- | --- |
| objectId   string | The full OSS URN of the object. |
| objectKey   string | The name of the object provided by the client. |
| size   integer | The size of the object in bytes. |
| contentType   integer | The Content-Type of the object, specified in the request. |
| location   string | The URL at which to download the object. |

## [Error Body Structure](#error-body-structure)

| reason   string | Any top-level details about why the request was rejected. |
| --- | --- |
| uploadKey   string | The identifier of the upload the user attempted to complete, if one was provided. |
| size   object | See size object structure. |
| parts   object | See parts object structure. |

## [Size object Structure](#size-object-structure)

| expected   integer | The expected object size provided in the request. |
| --- | --- |
| detected   integer | The actual size of the object in S3, in bytes. |

## [Parts object Structure](#parts-object-structure)

| part   integer | The index of the part in the multipart upload. |
| --- | --- |
| status   string | Indicates whether this particular part uploaded to S3 is valid. Possible values are:   - Pending: no part has been uploaded to S3 for this index.   - Unexpected: the eTag of the part in S3 does not match the one provided in the request.   - TooSmall: the chunk uploaded to S3 is smaller than 5MB, for any chunk except the final one.   - Unexpected+TooSmall: the chunk is both too small and has an eTag mismatch.   - Ok: The chunk has no issues. |
| size   integer | The size of the corresponding part detected in S3. |
| eTag   string | The eTag of the detected part in S3. |

## [Example 1](#example-1)

Request to complete the object creation process after the bytes have been uploaded directly to S3. (200).

### Request

```
curl -X POST
  -H 'Authorization: Bearer eYeL5gYxAT2j3u9TEerxoJoToNbi'
  -H 'Content-Type: application/json'
  -H 'x-ads-meta-Content-Type: application/octet-stream'
  --data-raw '{
    "uploadKey": "{UPLOAD_KEY_PROVIDED_FROM_GET_UPLOAD_URLS_RESPONSE}"
  }'
  'https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/random_file.bin/signeds3upload'

```

Show More

### Response

```
{
  "bucketKey": "sampleosstestbucket20210722",
  "objectId": "urn:adsk.objects:os.object:sampleosstestbucket20210722/random_file.bin",
  "objectKey": "random_file.bin",
  "size": 12582912,
  "contentType": "application/octet-stream",
  "location": "https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/random_file.bin"
}

```

Show More

## [Example 2](#example-2)

Request to complete the object creation process after the bytes have been uploaded directly to S3 with Size and ETag validation (200).

### Request

```
curl -XPOST
  -H'Authorization: Bearer {YOUR_TOKEN}'
  -H 'Content-Type: application/json'
  -H 'x-ads-meta-Content-Type: application/octet-stream'
  --data-raw '{
    "uploadKey": "{UPLOAD_KEY_PROVIDED_FROM_GET_UPLOAD_URLS_RESPONSE}",
    "size": 1,
    "eTags": [
        "c4ca4238a0b923820dcc509a6f75849b",
        "68ed4d53c0c933b7bf7debbd640386b1",
        "12ee9a859b60e71df4ef727f41c6b6d8"
    ]
  }'
  'https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/random_file.bin/signeds3upload'

```

Show More

### Response

```
{
  "uploadKey": "{UPLOAD_KEY}",
  "status": "error",
  "reason": "MissingOrInvalidParts",
  "size": {
      "expected": 1,
      "detected": 12582912
  },
  "parts": [
      {
        "part": 1,
        "size": 5242880,
        "eTag": "9aec28c3d07e2978e6502f6427c515da",
        "status": "Unexpected"
      },
      {
        "part": 2,
        "size": 5242880,
        "eTag": "68ed4d53c0c933b7bf7debbd640386b1",
        "status": "Ok"
      },
      {
        "part": 3,
        "size": 2097152,
        "eTag": "12ee9a859b60e71df4ef727f41c6b6d8",
        "status": "Ok"
      }
  ]
}

```

Show More
