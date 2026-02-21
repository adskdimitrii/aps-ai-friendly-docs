# signedresources/:id

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/signedresources-:id-PUT/

---

# signedresources/:id

Overwrite a existing object using a signed URL.

Conditions to call this operation:

- Object is available

- Expiration period is valid

- Signed URL should be created with write or readwrite access.

- If you set the URL to expire after it is used the first time, it will expire when the upload is complete.

## Resource Information

Method and URI PUT https://developer.api.autodesk.com/oss/v2/signedresources/:id Authentication Context none Data Format JSON

### Request

## Headers

Content-Type * string Must be application/json . Content-Length * string Indicates the size of the entity-body. Content-Disposition string OSS will record the value of the header and on download, would send the header contents down. x-ads-region enum The region where the bucket containing the object resides. Acceptable values: - US - Data center for the US region. - EMEA - Data center for the Europe, Middle East, and Africa regions. - AUS - (Beta) Data center for the Australia region. - CAN - Data centre for the Canada region. - DEU - Data centre for the Germany region. - IND - Data centre for the India region. - JPN - Data centre for the Japan region. - GBR - Data centre for the United Kingdom region. Note : - Beta features are subject to change. Please avoid using them in production environments. If-Match string When overwriting an object, use the latest SHA-1 hash to verify that you are overwriting the latest data. A SHA-1 hash is returned every time you upload or overwrite an object.
If the SHA-1 hash in the header does not match the current SHA-1 hash stored for this object in OSS, the request fails (status code 412 ).

### Request

## URI Parameters

id * string Id of signed resource

### Request

## Body Structure

Contents of the file to upload

### Response

## HTTP Status Code Summary

200 OK Successful operation 400 BAD REQUEST The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications.
The response body may give an indication of what is wrong with the request. 401 UNAUTHORIZED The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify Authentication and try again. 403 FORBIDDEN The Authorization was successfully validated but permission is not granted. Donât try again unless you solve permissions first. 404 NOT FOUND The specified bucket does not exist. 412 PRECONDITION FAILED Conditional update failed because the hash value supplied in the header does not match the SHA1 hash value of the current object in OSS. 500 INTERNAL SERVER ERROR Internal failure while processing the request, reason depends on error.

### Response

## Body Structure (200)

```
{ "$schema" : "http://json-schema.org/draft-04/schema#" , "type" : "object" , "properties" : { "bucketKey" : { "type" : "string" }, "objectId" : { "type" : "string" }, "objectKey" : { "type" : "string" }, "sha1" : { "type" : "string" }, "size" : { "type" : "integer" }, "contentType" : { "type" : "string" }, "location" : { "type" : "string" } } }
```

bucketKey string Bucket Key objectId string Object URN objectKey string Object Key sha1 string SHA-1 hash of the object, to be used as the value of the If-Match header in subsequent calls to overwrite the object. size integer Object size contentType string Object content-type location string URL to download the object

## Example 1

Successful Upload with Signed URL (200)

Suppose someone created a signed resource with write access previously.

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/buckets/bucketexamplekey/objects/testobject/signed?access=write" -X POST -H "Authorization: Bearer G2KbfMBjPEnU1vYu92JrcYukJEVw" -H "Content-Type: application/json;charset=UTF-8" --data ' { } '
```

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/signedresources/e63f23e2-2486-4f32-a921-bcfe8fade5e3" -X PUT -H "Content-Type: text/plain; charset=UTF-8" --data ' BODY: new file content bytes... '
```

### Response

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Content-Type: application/json; charset=utf-8
Date: Wed, 25 May 2016 16:08:55 GMT
Server: Apigee Router
Content-Length: 372
Connection: keep-alive
      {
  "bucketKey" : "bucketexamplekey",
  "objectId" : "urn:adsk.objects:os.object:bucketexamplekey/testobject",
  "objectKey" : "testobject",
  "sha1" : "4c33cac14fbb94bd467caa97902aa6550992f0b6",
  "size" : 31,
  "contentType" : "text/plain; charset=UTF-8",
  "location" : "https://developer.api.autodesk.com/oss/v2/buckets/bucketexamplekey/objects/testobject"
}
```

## Example 1

Forbidden Upload to Signed URL (403)

If the signed resource did not have write access previously, it is not possible to update it.

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/signedresources/e63f23e2-2486-4f32-a921-bcfe8fade5e3" -X PUT
-H "Content-Type: text/plain; charset=UTF-8" --data ' BODY: new file content bytes... '
```

### Response

```
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Content-Type: application/json; charset=utf-8
Date: Wed, 25 May 2016 16:08:55 GMT
Server: Apigee Router
Content-Length: 372
Connection: keep-alive
      HTTP/1.1 403 Forbidden
      {
    "reason" : "Signed Resource does not grant write permissions"
}
```
