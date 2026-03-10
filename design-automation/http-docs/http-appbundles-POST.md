# appbundles

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/appbundles-POST/

---

POST

# appbundles

Creates a new AppBundle.

It is highly recommended to [create nickname](http-forgeapps-id-PATCH.md) before creating AppBundle. The nickname is used as a clearer alternative name when identifying AppBundles and Activities, as compared to using the Client ID.
> Limits: (varies by Engine)
>
> 1. Number of AppBundle that can be created. See [Activity and AppBundle Quotas](https://aps.autodesk.com/en/docs/design-automation/v3/developers_guide/rate-limits/da-rate-limits/).
>
> 2. Size of AppBundle. See [Activity and AppBundle Quotas](https://aps.autodesk.com/en/docs/design-automation/v3/developers_guide/rate-limits/da-rate-limits/).
>
> This method creates new AppBundle returned in response value.
>
> POST upload is required to limit upload size.
>
>
> After this request, you need to upload the AppBundle zip.
>
> To upload the AppBundle package, create a multipart/form-data request using data received in reponse uploadParameters:
>
> - endpointURL is the URL to make the upload package request against,
>
> - formData are the parameters that need to be put into the upload package request body.
>
> They must be followed by an extra ‘file’ parameter indicating the location of the package file.
>
> An example:
>
>
> curl <https://bucketname.s3.amazonaws.com/>
>
> -F key = apps/myApp/myfile.zip
>
> -F content-type = application/octet-stream
>
> -F policy = eyJleHBpcmF0aW9uIjoiMjAxOC0wNi0yMVQxMzo…(trimmed)
>
> -F x-amz-signature = 800e52d73579387757e1c1cd88762…(trimmed)
>
> -F x-amz-credential = AKIAIOSFODNN7EXAMPLE/20180621/us-east-1/s3/aws4_request/
>
> -F x-amz-algorithm = AWS4-HMAC-SHA256
>
> -F x-amz-date = 20180621T091656Z
>
> -F file=@E:myfile.zip
>
> The ‘file’ field must be at the end, all fields after ‘file’ will be ignored.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/da/us-east/v3/appbundles |
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

- packagestring The URL that points to the zip package for the AppBundle or Engine.
- idstring Name of AppBundle, see the example section. Only alphanumeric characters and _ (underscore) are allowed.
- engine*string The actual processing engine that runs the WorkItem job and processes the Activity.
- appbundlesarray: string A module referenced by an Activity in order to perform specific functions. Typically this is a DLL or some other form of custom code.
- settingsobject The url/string Settings for a given set of AppBundles.
- *any of Type: dictionary<string, [*](#id3)>
- StringSettingobject
- valuestring
- isEnvironmentVariableboolean
- UrlSettingobject
- url*string Url.
- headersobject Headers.
- *string Type: dictionary<string, [*](#id5)>
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
- *object Type: dictionary<string, [*](#id7)>
- descriptionstring Human readable description of the object.

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully create a new AppBundle. |
| --- | --- |
| 400   Bad Request | The request is invalid. |
| 403   Forbidden | Maximum number of items exceeded. |
| 409   Conflict | An item with this name already exists. |
| 413 | Maximum size of the item exceeded. |
| 500   Internal Server Error | Unknown error. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

- packagestring The URL that points to the zip package for the AppBundle or Engine.
- uploadParametersobject The parameters needed to POST an AppBundle.
- endpointURLstring The URL to upload the AppBundle package to.
- formDataobject FormData parameters to be used in the body of the AppBundle package upload request.
Must be followed by a ‘file’ parameter indicating the package file location.
- *string Type: dictionary<string, [*](#id10)>
- idstring Name of AppBundle, see the example section.
- enginestring The actual processing engine that runs the WorkItem job and processes the Activity.
- appbundlesarray: string A module referenced by an Activity in order to perform specific functions. Typically this is a DLL or some other form of custom code.
- settingsobject The url/string Settings for a given set of AppBundles.
- *any of Type: dictionary<string, [*](#id12)>
- StringSettingobject
- valuestring
- isEnvironmentVariableboolean
- UrlSettingobject
- urlstring Url.
- headersobject Headers.
- *string Type: dictionary<string, [*](#id14)>
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
- *object Type: dictionary<string, [*](#id20)>
- descriptionstring Human readable description of the object.
- versionint

## [Example](#example)

Successfully create a new AppBundle.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/appbundles' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "id": "ChangeParams",
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
  "version": 1
}

```

Show More
