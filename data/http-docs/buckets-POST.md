# buckets

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-POST/

---

# buckets

Creates a bucket. Buckets are arbitrary spaces that are created by applications and are used to store objects for later retrieval. A bucket is owned by the application that creates it.

Note that to create storage spaces for BIM 360 Document Management you need to use POST projects/:project_id/storage . For more details, see the Upload Files to BIM 360 Document Management tutorial.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/oss/v2/buckets Authentication Context app-only Required OAuth Scopes bucket:create Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained
via POST token . Content-Type * string Must be application/json . x-ads-region * enum The region where the bucket resides Note : This attribute is replaced by the region header. region * enum The region where the bucket resides. Possible values: - US - (Default) Data center for the US region. - EMEA - Data center for the Europe, Middle East, and Africa regions. - AUS - (Beta) Data center for the Australia region. - CAN - Data centre for the Canada region. - DEU - Data centre for the Germany region. - IND - Data centre for the India region. - JPN - Data centre for the Japan region. - GBR - Data centre for the United Kingdom region. Note : 1. Beta features are subject to change. Please avoid using them in production environments. 2. If you specify the region header as well as the x-ads-region header, the region header takes precedence.

### Request

## Body Structure

```
{ "$schema" : "http://json-schema.org/draft-04/schema#" , "type" : "object" , "properties" : { "bucketKey" : { "type" : "string" }, "allow" : { "type" : "array" , "items" : { "type" : "object" , "properties" : { "authId" : { "type" : "string" }, "access" : { "type" : "string" } }, "required" : [ "authId" , "access" ] } }, "policyKey" : { "type" : "string" } }, "required" : [ "bucketKey" , "policyKey" ] }
```

bucketKey * string A unique name you assign to a bucket. It must be globally unique across all applications and regions, otherwise the call will fail. Possible values: -_.a-z0-9 (between 3-128 characters in length). Note that you cannot change a bucket key. allow array Objects representing applications to which the owner wants to grant access at bucket creation time authId string The application key to grant access to. Required when _allow_ is used. access enum Acceptable values: full , read . Required when _allow_ is used. policyKey * enum Data retention policy Acceptable values: transient , temporary , persistent

### Response

## HTTP Status Code Summary

200 OK Bucket successfully created. 400 BAD REQUEST The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications.
The response body may give an indication of what is wrong with the request. 401 UNAUTHORIZED The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify Authentication and try again. 403 FORBIDDEN The Authorization was successfully validated but permission is not granted. Donât try again unless you solve permissions first. 409 CONFLICT The specified bucket key already exists. 500 INTERNAL SERVER ERROR Internal failure while processing the request, reason depends on error.

### Response

## Body Structure (200)

```
{ "$schema" : "http://json-schema.org/draft-04/schema#" , "type" : "object" , "properties" : { "bucketKey" : { "required" : true , "type" : "string" }, "bucketOwner" : { "required" : true , "type" : "string" }, "createdDate" : { "required" : true , "type" : "integer" }, "permissions" : { "required" : true , "type" : "array" , "items" : { "type" : [ "object" , "null" ], "properties" : { "authId" : { "required" : true , "type" : "string" }, "access" : { "required" : true , "type" : "string" } } } }, "policyKey" : { "required" : true , "type" : "string" } } }
```

bucketKey string The key for the created bucket bucketOwner string Owner of the bucket createdDate long Timestamp in epoch time permissions array(object) Array of objects representing the applications with access granted at bucket creation authId string The application to grant access to access enum Acceptable values: full , read policyKey enum Data retention policy. Acceptable values: transient , temporary , persistent

## Example 1

Create bucket - Success (200)

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/buckets" -X POST -H "Content-Type: application/json" -H "Authorization: Bearer kgEJWMJitdYbhfxghap8SbZqXMoS" -d ' { "bucketKey":"apptestbucket", "policyKey":"transient" } '
```

### Response

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Content-Type: application/json; charset=utf-8
Date: Sat, 21 May 2016 00:05:30 GMT
Server: Apigee Router
Content-Length: 209
Connection: keep-alive

{
  "bucketKey":"apptestbucket",
  "bucketOwner":"RlKfGlAbb7N8VJwLllOvpfonB1Ex52qG",
  "createdDate":1463785698600,
  "permissions":[
    {
      "authId":"RlKffonB1Ex52GlAbb7N8VJwLllOvpqG",
      "access":"full"
    }
  ],
  "policyKey":"transient"
}
```

Note

Application key is automatically added in the âpermissionsâ array, even if not explicitly included in the POST request.

## Example 2

Create Bucket - Invalid Format (400)

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/buckets" -X POST -H "Content-Type: application/json" -H "Authorization: Bearer kgEJWMJitdYbhfxghap8SbZqXMoS" -d ' { "bucketKey":"bucketExamplekey", "policyKey":"transient" } '
```

### Response

```
HTTP/1.1 400 Bad Request
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Content-Type: application/json; charset=utf-8
Date: Tue, 24 May 2016 20:53:09 GMT
Server: Apigee Router
Content-Length: 76
Connection: keep-alive

{
  "reason":"Valid field 'bucketKey' must be of the form  [-_.a-z0-9]{3,128}"
}
```

## Example 3

Create Bucket - Conflict (409)

Note

Letâs suppose bucket apptestbucket already exists.

### Request

```
curl -v "https://developer.api.autodesk.com/oss/v2/buckets" -X POST -H "Content-Type: application/json" -H "Authorization: Bearer kgEJWMJitdYbhfxghap8SbZqXMoS" -d ' { "bucketKey":"apptestbucket", "policyKey":"transient" } '
```

### Response

```
HTTP/1.1 409 Conflict
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Authorization, Accept-Encoding, Range, Content-Type
Access-Control-Allow-Methods: GET
Access-Control-Allow-Origin: *
Content-Type: application/json; charset=utf-8
Date: Tue, 24 May 2016 20:54:19 GMT
Server: Apigee Router
Content-Length: 34
Connection: keep-alive

{
  "reason":"Bucket already exists"
}
```
