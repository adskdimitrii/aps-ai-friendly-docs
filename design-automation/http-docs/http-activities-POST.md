# activities

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/activities-POST/

---

POST

# activities

Creates a new Activity.

It is highly recommended to [create nickname](http-forgeapps-id-PATCH.md) before creating Activity. The nickname is used as a clearer alternative name when identifying AppBundles and Activities, as compared to using the Client ID.
> Limits (varies by Engine):
>
> 1. Number of Activities that can be created. See [Activity and AppBundle Quotas](https://aps.autodesk.com/en/docs/design-automation/v3/developers_guide/rate-limits/da-rate-limits/).

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/da/us-east/v3/activities |
| --- | --- |
| Authentication Context | app only |
| Required OAuth Scopes | `code:all` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [OAuth](../../oauth/http-docs/http-gettoken-POST.md) |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [Body Structure](#body-structure)

Expand all

- commandLine*array: string Path to Engine executable with arguments. [Activity command line](https://aps.autodesk.com/en/docs/design-automation/v3/developers_guide/field-guide/#command-lines).
- parametersobject Each parameter represents an input or output file. Inputs can be files or simply values to be read (string or json), if the read verb is used. Named parameters of an Activity have corresponding named arguments of a WorkItem.
- *object Type: dictionary<string, [*](#id2)>
- zipboolean This attribute together with the XrefTreeArgumentBase.PathInZip attribute determine how zip files are handled.
Default is false.
For onDemand=’true’ the Zip file is just downloaded, not unzipped.
- localNamestring Provides default name of the file or folder on the processing server for this parameter. Note this name may be overriden in various ways.
- ondemandboolean The parameter will be accessed by the appbundle on demand and should not be used by the system. Default is false.
When onDemand=’true’, the next parameter’s ‘verb’s only valid values are `get` or `head`.
- verb*enum:string Defines the operation for a parameter. get, put, post, patch imply an HTTP operation on the url in the parameter. read implies that the string or json value of parameter should be read. get and read imply input parameters all others are output.
Possible values: `get`, `head`, `put`, `post`, `patch`, `read`
- descriptionstring The description of the parameter.
- requiredboolean Specifies whether the corresponding WorkItem Argument is required. Default is false.
- idstring Name of Activity, see the example section. Only alphanumeric characters and _ (underscore) are allowed.
- engine*string The actual processing engine that runs the WorkItem job and processes the Activity.
- appbundlesarray: string A module referenced by an Activity in order to perform specific functions. Typically this is a DLL or some other form of custom code.
- settingsobject The url/string Settings for a given set of AppBundles.
- *any of Type: dictionary<string, [*](#id4)>
- StringSettingobject
- valuestring
- isEnvironmentVariableboolean
- UrlSettingobject
- url*string Url.
- headersobject Headers.
- *string Type: dictionary<string, [*](#id6)>
- verbenum:string Defines the operation for a parameter. get, put, post, patch imply an HTTP operation on the url in the parameter. read implies that the string value of parameter should be read. get and read imply input parameters all others are output.
Possible values: `get`, `head`, `put`, `post`, `patch`, `read`
- multipartsobject Provide [multipart post](http://hc.apache.org/httpclient-3.x/methods/multipartpost.html) method to upload the results and multiparts can be empty if there is no “parameter” to provide. It supports [Box](https://developer.box.com/reference#upload), [Google Drive](https://developers.google.com/drive/api/v3/manage-uploads#multipart) and [Amazon Simple Storage Service (S3)](https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html) services.Examples of using argument “multiparts”:Box:

| “multiparts”: | {“attributes”: {“name”: “result.txt”, “parent”: {“id”: “xxxxx”}}, “mydata”: “xxxxx”} |
| --- | --- |
Google Drive:

| “multiparts”: | {“keys”: {“name”: “result.txt”, “parent” :[“xxxxx”]}} |
| --- | --- |
Amazon Simple Storage Service (S3):

| “multiparts”: | {“key”: “result.txt”, “policy”: “xxxxx”, “x-amz-signature”: “xxxxx”, “x-amz-credential”: “xxxxx”, “x-amz-algorithm”: “AWS4-HMAC-SHA256”, “x-amz-date”: “20190820T000000Z”, “bucket”: “xxxxx”} |
| --- | --- |
- *object Type: dictionary<string, [*](#id8)>
- descriptionstring Human readable description of the object.

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully create a new Activity. |
| --- | --- |
| 400   Bad Request | The request is invalid. |
| 403   Forbidden | Maximum number of Activities exceeded. |
| 409   Conflict | An Activity with this name already exists. |
| 413 | Maximum size of the item exceeded. |
| 500   Internal Server Error | Unknown error. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

- commandLinearray: string Path to Engine executable with arguments. [Activity command line](https://aps.autodesk.com/en/docs/design-automation/v3/developers_guide/field-guide/#command-lines).
- parametersobject Each parameter represents an input or output file. Named parameters of an Activity have corresponding named arguments of a WorkItem.
- *object Type: dictionary<string, [*](#id12)>
- zipboolean This attribute together with the XrefTreeArgumentBase.PathInZip attribute determine how zip files are handled.
Default is false.
For onDemand=’true’ the Zip file is just downloaded, not unzipped.
- localNamestring Provides default name of the file or folder on the processing server for this parameter. Note this name may be overridden in various ways.
- ondemandboolean The parameter will be accessed by the appbundle on demand and should not be used by the system. Default is false.
When onDemand=’true’, the next parameter’s ‘verb’s only valid values are `get` or `head`.
- verbenum:string Defines the operation for a parameter. get, put, post, patch imply an HTTP operation on the url in the parameter. read implies that the string value of parameter should be read. get and read imply input parameters all others are output.
Possible values: `get`, `head`, `put`, `post`, `patch`, `read`
- descriptionstring The description of the parameter.
- requiredboolean Specifies whether the corresponding WorkItem Argument is required. Default is false.
- idstring Name of Activity, see the example section.
- enginestring The actual processing engine that runs the WorkItem job and processes the Activity.
- appbundlesarray: string A module referenced by an Activity in order to perform specific functions. Typically this is a DLL or some other form of custom code.
- settingsobject The url/string Settings for a given set of AppBundles.
- *any of Type: dictionary<string, [*](#id14)>
- StringSettingobject
- valuestring
- isEnvironmentVariableboolean
- UrlSettingobject
- urlstring Url.
- headersobject Headers.
- *string Type: dictionary<string, [*](#id16)>
- verbenum:string Defines the operation for a parameter. get, put, post, patch imply an HTTP operation on the url in the parameter. read implies that the string value of parameter should be read. get and read imply input parameters all others are output.
Possible values: `get`, `head`, `put`, `post`, `patch`, `read`
- multipartsobject Provide [multipart post](http://hc.apache.org/httpclient-3.x/methods/multipartpost.html) method to upload the results and multiparts can be empty if there is no “parameter” to provide. It supports [Box](https://developer.box.com/reference#upload), [Google Drive](https://developers.google.com/drive/api/v3/manage-uploads#multipart) and [Amazon Simple Storage Service (S3)](https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html) services.Examples of using argument “multiparts”:Box:

| “multiparts”: | {“attributes”: {“name”: “result.txt”, “parent”: {“id”: “xxxxx”}}, “mydata”: “xxxxx”} |
| --- | --- |
Google Drive:

| “multiparts”: | {“keys”: {“name”: “result.txt”, “parent” :[“xxxxx”]}} |
| --- | --- |
Amazon Simple Storage Service (S3):

| “multiparts”: | {“key”: “result.txt”, “policy”: “xxxxx”, “x-amz-signature”: “xxxxx”, “x-amz-credential”: “xxxxx”, “x-amz-algorithm”: “AWS4-HMAC-SHA256”, “x-amz-date”: “20190820T000000Z”, “bucket”: “xxxxx”} |
| --- | --- |
- *object Type: dictionary<string, [*](#id22)>
- descriptionstring Human readable description of the object.
- versionint

## [Remarks](#remarks)

You can use `adskusereportzip` key in the `settings` section of the request body to use a zip file for the workitem report. For example:

```
"settings": {
  "adskusereportzip": true
}

```

The service automatically zips all files in the working directory (top level only) that match the pattern `report*.log` and makes resulting zip file available for download via the `reportUrl` that is returned in [GET workitems/:id](https://aps.autodesk.com/en/docs/design-automation/v3/reference/workitems-id-GET/)

## [Example](#example)

Successfully create a new Activity.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/activities' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
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
        "id": "SampleActivity",
        "engine": "Autodesk.Inventor+23",
        "appbundles": [
          "owner.ChangeParams+prod"
        ],
        "description": "Human readable description of the object."
      }'

```

Show More

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
  "id": "owner.SampleActivity",
  "engine": "Autodesk.Inventor+23",
  "appbundles": [
    "owner.ChangeParams+prod"
  ],
  "description": "Human readable description of the object.",
  "version": 1
}

```

Show More
