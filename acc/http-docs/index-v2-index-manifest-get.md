# projects/:projectId/indexes/:indexId/manifest

Source: https://aps.autodesk.com/en/docs/acc/reference/http/index-v2-index-manifest-get/

---

# projects/:projectId/indexes/:indexId/manifest

Retrieve a specific manifest associated with a properties index. Since the manifest, once created, is immutable, the response will set a long expiration HTTP header for efficient client side caching.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/index/v2/projects/:projectId/indexes/:indexId/manifest Authentication Context user context required Required OAuth Scopes data:read Data Format json

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. x-ads-region enum: string The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

projectId string: UUID The project ID. indexId string The index ID.

### Response

## HTTP Status Code Summary

200 OK Returns the index manifest 401 Unauthorized Response in case of an error. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 429 Too Many Requests Rate limit exceeded. Wait some time before retrying. The Retry-After header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

schema enum: string current schema version. Possible values: 2.0.0 projectId string: UUID project ID. status enum: string manifest status. Possible values: Failed , Running , Succeeded createdAt datetime: ISO 8601 creation timestamp. seedFiles array: object seed files. lineageId string lineage ID. lineageUrn string lineage URN. versionUrn string file version URN. databases array: object databases. id string DB ID. offsets string OSS path for the offsets file. attributes string OSS path for the attributes file. values string OSS path for the values file. mapping string OSS path for the mapping file. ids string OSS path for the IDs file. views array: object views. id string view ID. urn string file version URN. is3d boolean is this a 3D view?. viewableName string viewable name. viewableId string viewable ID. viewableGuid string viewable GUID. errors array: object errors. type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field which failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code. stats array: object High level statistics about the diff index objects int The number of design elements (rows) in this index contentLength int The compressed file size in bytes of the index. This file can be downloaded via the index properties endpoint

Possible values: 2.0.0

Possible values: Failed , Running , Succeeded

### Response

## Body Structure (401)

type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field which failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code.

## Example

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/index/v2/projects/cd743656-f130-48bd-96e6-948175313637/indexes/da39a3ee5e6b4b0d/manifest' \ -H 'Authorization: Bearer <token>'
```

### Response (200)

```
{ "schema" : "2.0.0" , "projectId" : "d88f5314-90c3-4ccd-9460-810097580b12" , "status" : "Succeeded" , "createdAt" : "2020-06-30T06:43:51.391Z" , "seedFiles" : [ { "lineageId" : "344b06a3" , "lineageUrn" : "urn:adsk.wipstg:dm.lineage:-7p38avKTMGWp2vcCW568Q" , "versionUrn" : "urn:adsk.wipstg:fs.file:vf.-7p38avKTMGWp2vcCW568Q?version=2" , "databases" : [ { "id" : "b834bb65" , "offsets" : "urn:adsk.viewing:fs.file:dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuLTdwMzhhdktUTUdXcDJ2Y0NXNTY4UT92ZXJzaW9uPTI/output/Resource/objects_offs.json.gz" , "attributes" : "urn:adsk.viewing:fs.file:dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuLTdwMzhhdktUTUdXcDJ2Y0NXNTY4UT92ZXJzaW9uPTI/output/Resource/objects_attrs.json.gz" , "values" : "urn:adsk.viewing:fs.file:dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuLTdwMzhhdktUTUdXcDJ2Y0NXNTY4UT92ZXJzaW9uPTI/output/Resource/objects_vals.json.gz" , "mapping" : "urn:adsk.viewing:fs.file:dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuLTdwMzhhdktUTUdXcDJ2Y0NXNTY4UT92ZXJzaW9uPTI/output/Resource/objects_avs.json.gz" , "ids" : "urn:adsk.viewing:fs.file:dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuLTdwMzhhdktUTUdXcDJ2Y0NXNTY4UT92ZXJzaW9uPTI/output/Resource/objects_ids.json.gz" } ], "views" : [ { "id" : "cf7900d3" , "urn" : "urn:adsk.wipstg:fs.file:vf.-7p38avKTMGWp2vcCW568Q?version=2" , "is3d" : "true" , "viewableName" : "{3D}" , "viewableId" : "845097d1-c3be-4a6f-9dbe-51582fa6d465-002c2f04" , "viewableGuid" : "5d41dda7-eea1-eff5-77dd-ee1aa81fc3a8" }, { "id" : "7ca0051c" , "urn" : "urn:adsk.wipstg:fs.file:vf.-7p38avKTMGWp2vcCW568Q?version=2" , "is3d" : "false" , "viewableName" : "New Construction" , "viewableId" : "c884ae1b-61e7-4f9d-0001-719e20b22d0b-0032d30d" , "viewableGuid" : "8ac4ddd7-61f9-c4fa-a216-d771f8ed260a" } ] } ], "errors" : [] }
```

### Response (401)

```
{ "type" : "BadInput" , "title" : "One or more input values in the request were bad" , "detail" : "The following parameters are invalid: containerId" , "errors" : [ { "field" : "containerId" , "title" : "Invalid parameter" , "detail" : "The value 'testing' is not valid." , "type" : "BadInput" } ] }
```
