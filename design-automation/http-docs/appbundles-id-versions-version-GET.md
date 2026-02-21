# appbundles/:id/versions/:version

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/appbundles-id-versions-version-GET/

---

# appbundles/:id/versions/:version

Gets the details of the specified version of the AppBundle.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/da/us-east/v3/appbundles/:id/versions/:version Authentication Context app only Required OAuth Scopes code:all Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via OAuth

### Request

## URI Parameters

id string Name of AppBundle (unqualified). version int Version to retrieve (as integer).

### Response

## HTTP Status Code Summary

200 OK Successfully get the details of an AppBundleâs version. 403 Forbidden Unauthorized 404 Not Found Could not find the item. 500 Internal Server Error Unknown error.

### Response

## Body Structure (200)

package string The URL that points to the zip package for the AppBundle or Engine. uploadParameters object The parameters needed to POST an AppBundle. endpointURL string The URL to upload the AppBundle package to. formData object FormData parameters to be used in the body of the AppBundle package upload request.
Must be followed by a âfileâ parameter indicating the package file location. * string Type: dictionary<string, * > id string Name of AppBundle, see the example section. engine string The actual processing engine that runs the WorkItem job and processes the Activity. appbundles array: string A module referenced by an Activity in order to perform specific functions. Typically this is a DLL or some other form of custom code. settings object The url/string Settings for a given set of AppBundles. * any of Type: dictionary<string, * > StringSetting object value string isEnvironmentVariable boolean UrlSetting object url string Url. headers object Headers. * string Type: dictionary<string, * > verb enum:string Defines the operation for a parameter. get , put , post , patch imply an HTTP operation on the url in the parameter. read implies that the string value of parameter should be read. get and read imply input parameters all others are output.
Possible values: get , head , put , post , patch , read multiparts object Provide multipart post method to upload the results and multiparts can be empty if there is no âparameterâ to provide. It supports Box , Google Drive and Amazon Simple Storage Service (S3) services. Examples of using argument âmultipartsâ: Box: âmultipartsâ: {âattributesâ: {ânameâ: âresult.txtâ, âparentâ: {âidâ: âxxxxxâ}}, âmydataâ: âxxxxxâ} Google Drive: âmultipartsâ: {âkeysâ: {ânameâ: âresult.txtâ, âparentâ :[âxxxxxâ]}} Amazon Simple Storage Service (S3): âmultipartsâ: {âkeyâ: âresult.txtâ, âpolicyâ: âxxxxxâ, âx-amz-signatureâ: âxxxxxâ, âx-amz-credentialâ: âxxxxxâ, âx-amz-algorithmâ: âAWS4-HMAC-SHA256â, âx-amz-dateâ: â20190820T000000Zâ, âbucketâ: âxxxxxâ} * object Type: dictionary<string, * > description string Human readable description of the object. version int The verison retrieved.

It supports Box , Google Drive and Amazon Simple Storage Service (S3) services.

Examples of using argument âmultipartsâ:

Box:

âmultipartsâ: {âattributesâ: {ânameâ: âresult.txtâ, âparentâ: {âidâ: âxxxxxâ}}, âmydataâ: âxxxxxâ}

Google Drive:

âmultipartsâ: {âkeysâ: {ânameâ: âresult.txtâ, âparentâ :[âxxxxxâ]}}

Amazon Simple Storage Service (S3):

âmultipartsâ: {âkeyâ: âresult.txtâ, âpolicyâ: âxxxxxâ, âx-amz-signatureâ: âxxxxxâ, âx-amz-credentialâ: âxxxxxâ, âx-amz-algorithmâ: âAWS4-HMAC-SHA256â, âx-amz-dateâ: â20190820T000000Zâ, âbucketâ: âxxxxxâ}

## Example

Successfully get the details of an AppBundleâs version.

### Request

```
curl - v 'https://developer.api.autodesk.com/da/us-east/v3/appbundles/:id/versions/:version' \ - H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "id" : "ChangeParams" , "engine" : "Autodesk.Inventor+23" , "version" : 10 }
```
