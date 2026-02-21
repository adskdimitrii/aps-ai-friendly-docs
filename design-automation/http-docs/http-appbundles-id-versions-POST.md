# appbundles/:id/versions

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/appbundles-id-versions-POST/

---

POST

# appbundles/:id/versions

Creates a new version of the AppBundle.
:   Limit:

    1. Number of versions (LimitVersions).

    2. Size of AppBundle.

    This method creates new AppBundle returned in response value.

    POST upload is required to limit upload size. The endpoint url and all form fields are retrieved in AppBundle.UploadParameters.

    After this request, you need to upload the AppBundle zip.

    Use data received in the response to create multipart/form-data request. An example:

    curl <https://bucketname.s3.amazonaws.com/>

    -F key = apps/myApp/myfile.zip

    -F content-type = application/octet-stream

    -F policy = eyJleHBpcmF0aW9uIjoiMjAxOC0wNi0yMVQxMzoâ¦(trimmed)

    -F x-amz-signature = 800e52d73579387757e1c1cd88762â¦(trimmed)

    -F x-amz-credential = AKIAIOSFODNN7EXAMPLE/20180621/us-east-1/s3/aws4_request/

    -F x-amz-algorithm = AWS4-HMAC-SHA256

    -F x-amz-date = 20180621T091656Z

    -F file=@E:myfile.zip

    The âfileâ field must be at the end, all fields after âfileâ will be ignored.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/da/us-east/v3/appbundles/:id/versions |
| --- | --- |
| Authentication Context | app only |
| Required OAuth Scopes | `code:all` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [OAuth](/en/docs/oauth/v2/reference/http/gettoken-POST) |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| id   string | Name of AppBundle (unqualified). |
| --- | --- |

### Request

## [Body Structure](#body-structure)

| engine*   string | The actual processing engine that runs the WorkItem job and processes the Activity. |
| --- | --- |
| description   string | Human readable description of the object. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully create a new version of an AppBundle. |
| --- | --- |
| 400   Bad Request | The request is invalid. |
| 403   Forbidden | Limit for number of version exceeded. |
| 404   Not Found | Could not find the item. |
| 409   Conflict | The item version already exist. (this might happen if 2 requests are done in parallel to create the same version). |
| 500   Internal Server Error | Internal error. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

- uploadParametersobject The parameters needed to POST an AppBundle.
- endpointURLstring The URL to upload the AppBundle package to.
- formDataobject FormData parameters to be used in the body of the AppBundle package upload request.
Must be followed by a âfileâ parameter indicating the package file location.
- *string Type: dictionary<string, [*](#id4)>
- idstring Name of AppBundle, see the example section.
- enginestring The actual processing engine that runs the WorkItem job and processes the Activity.
- appbundlesarray: string A module referenced by an Activity in order to perform specific functions. Typically this is a DLL or some other form of custom code.
- settingsobject The url/string Settings for a given set of AppBundles.
- *any of Type: dictionary<string, [*](#id6)>
- StringSettingobject
- valuestring
- isEnvironmentVariableboolean
- UrlSettingobject
- urlstring Url.
- headersobject Headers.
- *string Type: dictionary<string, [*](#id8)>
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
- *object Type: dictionary<string, [*](#id10)>
- descriptionstring Human readable description of the object.
- versionint The version created.

## [Example](#example)

Successfully create a new version of an AppBundle.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/appbundles/ChangeParams/versions' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "engine": "Autodesk.Inventor+23",
        "description": "Changes parameters in ipt or asm file"
      }'

```

Show More

### Response

```
{
  "uploadParameters": {
    "endpointURL": "https://bucketname.s3.amazonaws.com",
    "formData": {
      "key": "apps/myApp",
      "content-type": "application/octet-stream",
      "policy": "eyJleHBpcmF0aW9uIjoiMjAxOC0wNi0yMVQxMzo...(trimmed)",
      "success_action_status": "200",
      "success_action_redirect": "",
      "x-amz-signature": "800e52d73579387757e1c1cd88762...(trimmed)",
      "x-amz-credential": "AKIAIOSFODNN7EXAMPLE/20180621/us-east-1/s3/aws4_request/",
      "x-amz-algorithm": "AWS4-HMAC-SHA256",
      "x-amz-date": "20180621T091656Z",
      "x-amz-server-side-encryption": "AES256",
      "x-amz-security-token": "FQoGZXIvYXdzEHYaDDi93QcZJ...(trimmed)"
    }
  },
  "id": "owner.ChangeParams",
  "engine": "Autodesk.Inventor+23",
  "description": "Changes parameters in ipt or asm file",
  "version": 2
}

```

Show More
