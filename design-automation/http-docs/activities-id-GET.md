# activities/:id

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/activities-id-GET/

---

GET

# activities/:id

Gets the details of the specified Activity. Note that the {id} parameter must be a QualifiedId (owner.name+label).

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/da/us-east/v3/activities/:id |
| --- | --- |
| Authentication Context | app only |
| Required OAuth Scopes | `code:all` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [OAuth](/en/docs/oauth/v2/reference/http/gettoken-POST) |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| id   string | Full qualified id of the Activity (owner.name+label). |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully get the details of an Activity. |
| --- | --- |
| 400   Bad Request | The request is invalid. |
| 403   Forbidden | Forbidden. |
| 404   Not Found | Resource cannot be found. Note that the server will return this result if a valid but unqualified id is passed. |
| 500   Internal Server Error | Unknown error. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

- commandLinearray: string Path to Engine executable with arguments. [Activity command line](/en/docs/design-automation/v3/developers_guide/field-guide#command-lines).
- parametersobject Each parameter represents an input or output file. Named parameters of an Activity have corresponding named arguments of a WorkItem.
- *object Type: dictionary<string, [*](#id3)>
- zipboolean This attribute together with the XrefTreeArgumentBase.PathInZip attribute determine how zip files are handled.
Default is false.
For onDemand=âtrueâ the Zip file is just downloaded, not unzipped.
- localNamestring Provides default name of the file or folder on the processing server for this parameter. Note this name may be overriden in various ways.
- ondemandboolean The parameter will be accessed by the appbundle on demand and should not be used by the system. Default is false.
When onDemand=âtrueâ, the next parameterâs âverbâs only valid values are `get` or `head`.
- verbenum:string Defines the operation for a parameter. get, put, post, patch imply an HTTP operation on the url in the parameter. read implies that the string value of parameter should be read. get and read imply input parameters all others are output.
Possible values: `get`, `head`, `put`, `post`, `patch`, `read`
- descriptionstring The description of the parameter.
- requiredboolean Specifies whether the corresponding WorkItem Argument is required. Default is false.
- idstring Name of Activity, see the example section.
- enginestring The actual processing engine that runs the WorkItem job and processes the Activity.
- appbundlesarray: string A module referenced by an Activity in order to perform specific functions. Typically this is a DLL or some other form of custom code.
- settingsobject The url/string Settings for a given set of AppBundles.
- *any of Type: dictionary<string, [*](#id5)>
- StringSettingobject
- valuestring
- isEnvironmentVariableboolean
- UrlSettingobject
- urlstring Url.
- headersobject Headers.
- *string Type: dictionary<string, [*](#id7)>
- verbenum:string Defines the operation for a parameter. get, put, post, patch imply an HTTP operation on the url in the parameter. read implies that the string value of parameter should be read. get and read imply input parameters all others are output.
Possible values: `get`, `head`, `put`, `post`, `patch`, `read`
- multipartsobject Provide [multipart post](http://hc.apache.org/httpclient-3.x/methods/multipartpost.html) method to upload the results and multiparts can be empty if there is no âparameterâ to provide. It supports [Box](https://developer.box.com/reference#upload), [Google Drive](https://developers.google.com/drive/api/v3/manage-uploads#multipart) and [Amazon Simple Storage Service (S3)](https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html) services.Examples of using argument âmultipartsâ:Box:

| âmultipartsâ: | {âattributesâ: {ânameâ: âresult.txtâ, âparentâ: {âidâ: âxxxxxâ}}, âmydataâ: âxxxxxâ} |
| --- | --- |
Google Drive:

| âmultipartsâ: | {âkeysâ: {ânameâ: âresult.txtâ, âparentâ :[âxxxxxâ]}} |
| --- | --- |
Amazon Simple Storage Service (S3):

| âmultipartsâ: | {âkeyâ: âresult.txtâ, âpolicyâ: âxxxxxâ, âx-amz-signatureâ: âxxxxxâ, âx-amz-credentialâ: âxxxxxâ, âx-amz-algorithmâ: âAWS4-HMAC-SHA256â, âx-amz-dateâ: â20190820T000000Zâ, âbucketâ: âxxxxxâ} |
| --- | --- |
- *object Type: dictionary<string, [*](#id9)>
- descriptionstring Human readable description of the object.
- versionint

## [Example](#example)

Successfully get the details of an Activity.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/activities/:id' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "commandLine": [
    "$(engine.path)\\InventorCoreConsole.exe /i \"$(args[InventorDoc].path)\" /al \"$(appbundles[ChangeParams].path)\" \"$(args[InventorParams].path)\""
  ],
  "parameters": {
    "InventorDoc": {
      "verb": "get"
    },
    "InventorParams": {
      "localName": "params.json",
      "verb": "get"
    },
    "OutputIpt": {
      "localName": "Result.ipt",
      "verb": "post"
    },
    "OutputIam": {
      "localName": "Result.zip",
      "verb": "post"
    },
    "OutputBmp": {
      "localName": "Result.bmp",
      "verb": "post"
    }
  },
  "id": "owner.SampleActivity+test",
  "engine": "Autodesk.Inventor+23",
  "appbundles": [
    "owner.ChangeParams+prod"
  ],
  "description": "Human readable description of the object.",
  "version": 1
}

```

Show More
