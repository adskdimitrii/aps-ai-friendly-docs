# activities

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/activities-POST/

---

# activities

Creates a new Activity.

It is highly recommended to create nickname before creating Activity. The nickname is used as a clearer alternative name when identifying AppBundles and Activities, as compared to using the Client ID.

Limits (varies by Engine):

- Number of Activities that can be created. See Activity and AppBundle Quotas .

## Resource Information

Method and URI POST https://developer.api.autodesk.com/da/us-east/v3/activities Authentication Context app only Required OAuth Scopes code:all Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via OAuth Content-Type * string Must be application/json

### Request

## Body Structure

commandLine * array: string Path to Engine executable with arguments. Activity command line . parameters object Each parameter represents an input or output file. Inputs can be files or simply values to be read (string or json), if the read verb is used. Named parameters of an Activity have corresponding named arguments of a WorkItem. * object Type: dictionary<string, * > zip boolean This attribute together with the XrefTreeArgumentBase.PathInZip attribute determine how zip files are handled.
Default is false.
For onDemand=âtrueâ the Zip file is just downloaded, not unzipped. localName string Provides default name of the file or folder on the processing server for this parameter. Note this name may be overriden in various ways. ondemand boolean The parameter will be accessed by the appbundle on demand and should not be used by the system. Default is false.
When onDemand=âtrueâ, the next parameterâs âverbâs only valid values are get or head . verb * enum:string Defines the operation for a parameter. get , put , post , patch imply an HTTP operation on the url in the parameter. read implies that the string or json value of parameter should be read. get and read imply input parameters all others are output.
Possible values: get , head , put , post , patch , read description string The description of the parameter. required boolean Specifies whether the corresponding WorkItem Argument is required. Default is false. id string Name of Activity, see the example section. Only alphanumeric characters and _ (underscore) are allowed. engine * string The actual processing engine that runs the WorkItem job and processes the Activity. appbundles array: string A module referenced by an Activity in order to perform specific functions. Typically this is a DLL or some other form of custom code. settings object The url/string Settings for a given set of AppBundles. * any of Type: dictionary<string, * > StringSetting object value string isEnvironmentVariable boolean UrlSetting object url * string Url. headers object Headers. * string Type: dictionary<string, * > verb enum:string Defines the operation for a parameter. get , put , post , patch imply an HTTP operation on the url in the parameter. read implies that the string value of parameter should be read. get and read imply input parameters all others are output.
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

200 OK Successfully create a new Activity. 400 Bad Request The request is invalid. 403 Forbidden Maximum number of Activities exceeded. 409 Conflict An Activity with this name already exists. 413 Maximum size of the item exceeded. 500 Internal Server Error Unknown error.

### Response

## Body Structure (200)

commandLine array: string Path to Engine executable with arguments. Activity command line . parameters object Each parameter represents an input or output file. Named parameters of an Activity have corresponding named arguments of a WorkItem. * object Type: dictionary<string, * > zip boolean This attribute together with the XrefTreeArgumentBase.PathInZip attribute determine how zip files are handled.
Default is false.
For onDemand=âtrueâ the Zip file is just downloaded, not unzipped. localName string Provides default name of the file or folder on the processing server for this parameter. Note this name may be overridden in various ways. ondemand boolean The parameter will be accessed by the appbundle on demand and should not be used by the system. Default is false.
When onDemand=âtrueâ, the next parameterâs âverbâs only valid values are get or head . verb enum:string Defines the operation for a parameter. get , put , post , patch imply an HTTP operation on the url in the parameter. read implies that the string value of parameter should be read. get and read imply input parameters all others are output.
Possible values: get , head , put , post , patch , read description string The description of the parameter. required boolean Specifies whether the corresponding WorkItem Argument is required. Default is false. id string Name of Activity, see the example section. engine string The actual processing engine that runs the WorkItem job and processes the Activity. appbundles array: string A module referenced by an Activity in order to perform specific functions. Typically this is a DLL or some other form of custom code. settings object The url/string Settings for a given set of AppBundles. * any of Type: dictionary<string, * > StringSetting object value string isEnvironmentVariable boolean UrlSetting object url string Url. headers object Headers. * string Type: dictionary<string, * > verb enum:string Defines the operation for a parameter. get , put , post , patch imply an HTTP operation on the url in the parameter. read implies that the string value of parameter should be read. get and read imply input parameters all others are output.
Possible values: get , head , put , post , patch , read multiparts object Provide multipart post method to upload the results and multiparts can be empty if there is no âparameterâ to provide. It supports Box , Google Drive and Amazon Simple Storage Service (S3) services. Examples of using argument âmultipartsâ: Box: âmultipartsâ: {âattributesâ: {ânameâ: âresult.txtâ, âparentâ: {âidâ: âxxxxxâ}}, âmydataâ: âxxxxxâ} Google Drive: âmultipartsâ: {âkeysâ: {ânameâ: âresult.txtâ, âparentâ :[âxxxxxâ]}} Amazon Simple Storage Service (S3): âmultipartsâ: {âkeyâ: âresult.txtâ, âpolicyâ: âxxxxxâ, âx-amz-signatureâ: âxxxxxâ, âx-amz-credentialâ: âxxxxxâ, âx-amz-algorithmâ: âAWS4-HMAC-SHA256â, âx-amz-dateâ: â20190820T000000Zâ, âbucketâ: âxxxxxâ} * object Type: dictionary<string, * > description string Human readable description of the object. version int

It supports Box , Google Drive and Amazon Simple Storage Service (S3) services.

Examples of using argument âmultipartsâ:

Box:

âmultipartsâ: {âattributesâ: {ânameâ: âresult.txtâ, âparentâ: {âidâ: âxxxxxâ}}, âmydataâ: âxxxxxâ}

Google Drive:

âmultipartsâ: {âkeysâ: {ânameâ: âresult.txtâ, âparentâ :[âxxxxxâ]}}

Amazon Simple Storage Service (S3):

âmultipartsâ: {âkeyâ: âresult.txtâ, âpolicyâ: âxxxxxâ, âx-amz-signatureâ: âxxxxxâ, âx-amz-credentialâ: âxxxxxâ, âx-amz-algorithmâ: âAWS4-HMAC-SHA256â, âx-amz-dateâ: â20190820T000000Zâ, âbucketâ: âxxxxxâ}

## Remarks

You can use adskusereportzip key in the settings section of the request body to use a zip file for the workitem report. For example:

```
"settings" : { "adskusereportzip" : true }
```

The service automatically zips all files in the working directory (top level only) that match the pattern report*.log and makes resulting zip file available for download via the reportUrl that is returned in GET workitems/:id

## Example

Successfully create a new Activity.

### Request

```
curl - v 'https://developer.api.autodesk.com/da/us-east/v3/activities' \ - X 'POST' \ - H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ - H 'Content-Type: application/json' \ - d '{ "commandLine": [ "$(engine.path) \\ InventorCoreConsole.exe /i \" $(args[InventorDoc].path) \" /al \" $(appbundles[ChangeParams].path) \" \" $(args[InventorParams].path) \" " ], "parameters": { "InventorDoc": { "verb": "get" }, "InventorParams": { "localName": "params.json", "verb": "get" }, "OutputIpt": { "localName": "Result.ipt", "verb": "post" }, "OutputIam": { "localName": "Result.zip", "verb": "post" }, "OutputBmp": { "localName": "Result.bmp", "verb": "post" } }, "id": "SampleActivity", "engine": "Autodesk.Inventor+23", "appbundles": [ "owner.ChangeParams+prod" ], "description": "Human readable description of the object." }'
```

### Response

```
{ "commandLine" : [ "$(engine.path)\\InventorCoreConsole.exe /i \"$(args[InventorDoc].path)\" /al \"$(appbundles[ChangeParams].path)\" \"$(args[InventorParams].path)\"" ], "parameters" : { "InventorDoc" : { "verb" : "get" }, "InventorParams" : { "localName" : "params.json" , "verb" : "get" }, "OutputIpt" : { "localName" : "Result.ipt" , "verb" : "post" }, "OutputIam" : { "localName" : "Result.zip" , "verb" : "post" }, "OutputBmp" : { "localName" : "Result.bmp" , "verb" : "post" } }, "id" : "owner.SampleActivity" , "engine" : "Autodesk.Inventor+23" , "appbundles" : [ "owner.ChangeParams+prod" ], "description" : "Human readable description of the object." , "version" : 1 }
```
