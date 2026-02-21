# projects/{projectId}/uploads/{uploadId}/thumbnails:batch-get

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-thumbnailsbatch-get-POST/

---

Uploads

POST

# projects/{projectId}/uploads/{uploadId}/thumbnails:batch-get

Retrieves a list of thumbnails for the specified review sheets.

Note that the thumbnails are stored in AWS S3 and will expire after 30 days (the count starts from the time that the upload was created).
When the thumbnails expire you will get a `404 (NotFound)` error when you try to access the S3 signed URL.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/uploads/{uploadId}/thumbnails:batch-get |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](/en/docs/oauth/v2/tutorials/get-2-legged-token) or [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| x-user-id   string | The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. <br>When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.<br>You can use either the userâs ACC ID (id), or their Autodesk ID (autodeskId). |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring: UUID The ID of the project. Use the [Data Management API](/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/). You can use a project ID either with a âb.â prefix or without a âb.â prefix. For instance, a project ID of âb.a4be0c34a-4ab7â can also be referred to as âa4be0c34a-4ab7â.
- uploadIdstring The ID of the upload. The upload ID is generated when you [create an upload object](/en/docs/acc/v1/reference/http/sheets-uploads-POST/).

### Request

## [Body Structure](#body-structure)

| reviewSheetIds*   array: string | The IDs of the review sheets you want to get the thumbnails from. To find the review sheet IDs, call [GET review-sheets](/en/docs/acc/v1/reference/http/sheets-review-sheets-GET/). <br>The max number of items is 100. |
| --- | --- |
| type*   enum:string | The size type of the thumbnails. Possible values: <br>`big`: the max size will be 512 pixels.`small`: the max size will be 256 pixels.`tiny`: the max size will be 64 pixels. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the thumbnails. |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 403   Forbidden | The user or client represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource cannot be found. |
| 429   Too Many Requests | The server has received too many requests. |
| 500   Internal Server Error | An unexpected error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | The list of results. |
| --- | --- |
| reviewSheetId   string | The ID of the review sheet the thumbnail belongs to. |
| size   array: integer | The width and height of the thumbnail. |
| signedUrl   string | The URL of the thumbnail. It is an AWS S3 signed URL and will expire in 1 hour. |

## [Example](#example)

Successfully retrieved the thumbnails.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/uploads/5cb5d9da-060e-421e-bca9-97dd8b5cd800/thumbnails:batch-get' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "reviewSheetIds": [
          "0d7a5883-1694-3078-a06d-ad24413f8b06"
        ],
        "type": "big"
      }'

```

Show More

### Response

```
{
  "results": [
    {
      "reviewSheetId": "0d7a5883-1694-3078-a06d-ad24413f8b06",
      "size": [
        512,
        256
      ],
      "signedUrl": "https://s3.us-east-1.amazonaws.com/rnd-shredder-buckets-sheetprocessing-1elowz1cchtl4/6e2cc934-709b-4f2e-81f8-727ab9a6c799.png?AWSAccessKeyId=ASIAZ6NF4RTV3JEBINXH&Signature=enZvg1McCp1GK%2BOL0ufG2aaCoAc%3D&x-amz-security-token=FwoGZXIvYXdzEAsaDEbuDLTNK4D8HPMr2yKtATOjYhoq23UUeFwdbTZ2T463lprZrvjK5eIdQ0o6OpyHkRDK%2FwEe5Dw67P9qyGc97q3Kw6zKlva3j88TENeN%2BJY0MOEYglhTrkgj3KnelyNm8ymhXwpmZZaa94ezy9Se707MvQsWueHQnzy%2BR%2BycRzE84C%2FxjlRAoG5REonzsHylkS8NJzvmbAwV9SxuUD4xXgHnnjfbnWbwXk8xf31v%2BkyHvoGb0EFQz4WoU9%2FvKOm12IEGMi2I6v0durq5t7Hl81SbiAMXDtzA%2F4tgFhnct9pn9kEqVrUDGzGntnW%2BV5GfUlM%3D&Expires=1614162667"
    }
  ]
}

```

Show More
