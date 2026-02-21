# appbundles

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/appbundles-POST/

---

# appbundles

Creates a new AppBundle.

It is highly recommended to create nickname before creating AppBundle. The nickname is used as a clearer alternative name when identifying AppBundles and Activities, as compared to using the Client ID.

The âfileâ field must be at the end, all fields after âfileâ will be ignored.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/da/us-east/v3/appbundles Authentication Context app only Required OAuth Scopes code:all Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via OAuth Content-Type * string Must be application/json

### Request

## Body Structure

package string The URL that points to the zip package for the AppBundle or Engine. id string Name of AppBundle, see the example section. Only alphanumeric characters and _ (underscore) are allowed. engine * string The actual processing engine that runs the WorkItem job and processes the Activity. appbundles array: string A module referenced by an Activity in order to perform specific functions. Typically this is a DLL or some other form of custom code. settings object The url/string Settings for a given set of AppBundles. * any of Type: dictionary<string, * > StringSetting object value string isEnvironmentVariable boolean UrlSetting object url * string Url. headers object Headers. * string Type: dictionary<string, * > verb enum:string Defines the operation for a parameter. get , put , post , patch imply an HTTP operation on the url in the parameter. read implies that the string value of parameter should be read. get and read imply input parameters all others are output.
Possible values: get , head , put , post , patch , read multiparts object Provide multipart post method to upload the results and multiparts can be empty if there is no âparameterâ to provide. It supports Box , Google Drive and Amazon Simple Storage Service (S3) services. Examples of using argument âmultipartsâ: Box: âmultipartsâ: {âattributesâ: {ânameâ: âresult.txtâ, âparentâ: {âidâ: âxxxxxâ}}, âmydataâ: âxxxxxâ} Google Drive: âmultipartsâ: {âkeysâ: {ânameâ: âresult.txtâ, âparentâ :[âxxxxxâ]}} Amazon Simple Storage Service (S3): âmultipartsâ: {âkeyâ: âresult.txtâ, âpolicyâ: âxxxxxâ, âx-amz-signatureâ: âxxxxxâ, âx-amz-credentialâ: âxxxxxâ, âx-amz-algorithmâ: âAWS4-HMAC-SHA256â, âx-amz-dateâ: â20190820T000000Zâ, âbucketâ: âxxxxxâ} * object Type: dictionary<string, * > description string Human readable description of the object.

It supports Box , Google Drive and Amazon Simple Storage Service (S3) services.

Examples of using argument âmultipartsâ:

Box:

âmultipartsâ: {âattributesâ: {ânameâ: âresult.txtâ, âparentâ: {âidâ: âxxxxxâ}}, âmydataâ: âxxxxxâ}

Google Drive:

âmultipartsâ: {âkeysâ: {ânameâ: âresult.txtâ, âparentâ :[âxxxxxâ]}}

Amazon Simple Storage Service (S3):

âmultipartsâ: {âkeyâ: âresult.txtâ, âpolicyâ: âxxxxxâ, âx-amz-signatureâ: âxxxxxâ, âx-amz-credentialâ: âxxxxxâ, âx-amz-algorithmâ: âAWS4-HMAC-SHA256â, âx-amz-dateâ: â20190820T000000Zâ, âbucketâ: âxxxxxâ}

### Response

## HTTP Status Code Summary

200 OK Successfully create a new AppBundle. 400 Bad Request The request is invalid. 403 Forbidden Maximum number of items exceeded. 409 Conflict An item with this name already exists. 413 Maximum size of the item exceeded. 500 Internal Server Error Unknown error.

### Response

## Body Structure (200)

package string The URL that points to the zip package for the AppBundle or Engine. uploadParameters object The parameters needed to POST an AppBundle. endpointURL string The URL to upload the AppBundle package to. formData object FormData parameters to be used in the body of the AppBundle package upload request.
Must be followed by a âfileâ parameter indicating the package file location. * string Type: dictionary<string, * > id string Name of AppBundle, see the example section. engine string The actual processing engine that runs the WorkItem job and processes the Activity. appbundles array: string A module referenced by an Activity in order to perform specific functions. Typically this is a DLL or some other form of custom code. settings object The url/string Settings for a given set of AppBundles. * any of Type: dictionary<string, * > StringSetting object value string isEnvironmentVariable boolean UrlSetting object url string Url. headers object Headers. * string Type: dictionary<string, * > verb enum:string Defines the operation for a parameter. get , put , post , patch imply an HTTP operation on the url in the parameter. read implies that the string value of parameter should be read. get and read imply input parameters all others are output.
Possible values: get , head , put , post , patch , read multiparts object Provide multipart post method to upload the results and multiparts can be empty if there is no âparameterâ to provide. It supports Box , Google Drive and Amazon Simple Storage Service (S3) services. Examples of using argument âmultipartsâ: Box: âmultipartsâ: {âattributesâ: {ânameâ: âresult.txtâ, âparentâ: {âidâ: âxxxxxâ}}, âmydataâ: âxxxxxâ} Google Drive: âmultipartsâ: {âkeysâ: {ânameâ: âresult.txtâ, âparentâ :[âxxxxxâ]}} Amazon Simple Storage Service (S3): âmultipartsâ: {âkeyâ: âresult.txtâ, âpolicyâ: âxxxxxâ, âx-amz-signatureâ: âxxxxxâ, âx-amz-credentialâ: âxxxxxâ, âx-amz-algorithmâ: âAWS4-HMAC-SHA256â, âx-amz-dateâ: â20190820T000000Zâ, âbucketâ: âxxxxxâ} * object Type: dictionary<string, * > description string Human readable description of the object. version int

It supports Box , Google Drive and Amazon Simple Storage Service (S3) services.

Examples of using argument âmultipartsâ:

Box:

âmultipartsâ: {âattributesâ: {ânameâ: âresult.txtâ, âparentâ: {âidâ: âxxxxxâ}}, âmydataâ: âxxxxxâ}

Google Drive:

âmultipartsâ: {âkeysâ: {ânameâ: âresult.txtâ, âparentâ :[âxxxxxâ]}}

Amazon Simple Storage Service (S3):

âmultipartsâ: {âkeyâ: âresult.txtâ, âpolicyâ: âxxxxxâ, âx-amz-signatureâ: âxxxxxâ, âx-amz-credentialâ: âxxxxxâ, âx-amz-algorithmâ: âAWS4-HMAC-SHA256â, âx-amz-dateâ: â20190820T000000Zâ, âbucketâ: âxxxxxâ}

## Example

Successfully create a new AppBundle.

### Request

```
curl - v 'https://developer.api.autodesk.com/da/us-east/v3/appbundles' \ - X 'POST' \ - H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ - H 'Content-Type: application/json' \ - d '{ "id": "ChangeParams", "engine": "Autodesk.Inventor+23", "description": "Changes parameters in ipt or asm file" }'
```

### Response

```
{ "uploadParameters" : { "endpointURL" : "https://bucketname.s3.amazonaws.com" , "formData" : { "key" : "apps/myApp" , "content-type" : "application/octet-stream" , "policy" : "eyJleHBpcmF0aW9uIjoiMjAxOC0wNi0yMVQxMzo...(trimmed)" , "success_action_status" : "200" , "success_action_redirect" : "" , "x-amz-signature" : "800e52d73579387757e1c1cd88762...(trimmed)" , "x-amz-credential" : "AKIAIOSFODNN7EXAMPLE/20180621/us-east-1/s3/aws4_request/" , "x-amz-algorithm" : "AWS4-HMAC-SHA256" , "x-amz-date" : "20180621T091656Z" , "x-amz-server-side-encryption" : "AES256" , "x-amz-security-token" : "FQoGZXIvYXdzEHYaDDi93QcZJ...(trimmed)" } }, "id" : "owner.ChangeParams" , "engine" : "Autodesk.Inventor+23" , "description" : "Changes parameters in ipt or asm file" , "version" : 1 }
```
