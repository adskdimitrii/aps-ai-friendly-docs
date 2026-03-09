# projects/{projectId}/uploads

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-uploads-POST/

---

Uploads

POST

# projects/{projectId}/uploads

Creates an ACC upload object. This endpoint splits the files into separate sheets.
It is typically used during the process of uploading files to [ACC Sheets tool](https://help.autodesk.com/view/BUILD/ENU/?guid=Upload_And_Publish_Sheets).

Note that before uploading the file, you need to create a version set and create a storage object.

This endpoint is asynchronous and initiates a job that runs in the background rather than halting execution of your program. You can track the progress of the upload by using the [GET uploads/:id](http-sheets-uploads-uploadId-GET.md) endpoint.

For more details about uploading sheets, see the [Upload Sheets](https://aps.autodesk.com/en/docs/acc/v1/tutorials/upload-sheets/) tutorial.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/uploads |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-user-id   string | The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. <br>When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.<br>You can use either the userâs ACC ID (id), or their Autodesk ID (autodeskId). |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](../how-to-docs/getting-started-retrieve-account-and-project-id.md). You can use a project ID either with a âb.â prefix or without a âb.â prefix. For instance, a project ID of âb.a4be0c34a-4ab7â can also be referred to as âa4be0c34a-4ab7â. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

Expand all

| versionSetId*   string | The ID of the version set you want to upload the sheets to. To create a new version set, call [POST version-sets](http-sheets-version-sets-POST.md). To find the ID of an existing version set, call [GET version-sets](http-sheets-version-sets-GET.md). |
| --- | --- |
| files*   array: object | The list of files to be processed by the upload. |
| storageType*   enum:string | The storage type of the file. Will always be `OSS`. |
| storageUrn*   string | The storage URN of the file. |
| name*   string | The name of the file. <br>Currently the Sheets tool only supports PDF files.<br>To create a storage URN, call [POST storage](http-sheets-storage-POST.md).<br>Max length: 255 |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Successfully started the upload. |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 403   Forbidden | The user or client represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource cannot be found. |
| 429   Too Many Requests | The server has received too many requests. |
| 500   Internal Server Error | An unexpected error occurred on the server. |

### Response

## [Body Structure (201)](#body-structure-201)

| id   string: UUID | The ID of the upload. |
| --- | --- |
| versionSetId   string: UUID | The ID of the version set where the upload creates sheets to. |
| status   enum:string | The status of the upload. Possible values: <br>`PENDING`: the uploaded files are waiting for to be processed.`PROCESSING`: the uploaded files are being processed.`IN_REVIEW`: the file upload process is complete. The sheets are ready for review. You can now call [GET review-sheets](http-sheets-review-sheets-GET.md), [PATCH review-sheets](http-sheets-review-sheets-PATCH.md), or [POST review-sheets:publish](http-sheets-review-sheetspublish-POST.md).`FAILED`: the file upload process failed. One of the final status of an upload.`UPDATING_VERSION_SET`: the target version set is being updated.`PUBLISHING`: the review sheets are being published.`PUBLISHED`: the review sheets have been published. |
| createdAt   datetime: ISO 8601 | The time when the upload was created, in ISO-8601 format (YYYY-MM-DDTHH:mm:ss.SSSZ). |
| createdBy   string | The ID of the user who created the upload. |
| createdByName   string | The name of the user who created the upload. |
| updatedAt   datetime: ISO 8601 | The time when the upload was last updated, in ISO-8601 format (YYYY-MM-DDTHH:mm:ss.SSSZ). |
| updatedBy   string | The ID of the user who last updated the upload. |
| updatedByName   string | The name of the user who last updated the upload. |
| publishedAt   datetime: ISO 8601 | The time when all the review sheets of the upload were published, in ISO-8601 format (YYYY-MM-DDTHH:mm:ss.SSSZ). |
| publishedBy   string | The ID of the user who published all the review sheets of the upload. |
| publishedByName   string | The name of the user who published all the review sheets of the upload. |
| publishedCount   int | The number of files that have been published by the upload. |

## [Example](#example)

Successfully started the upload.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/uploads' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "versionSetId": "7c2ecde0-2406-49f9-9199-50176848a0b7",
        "files": [
          {
            "storageType": "OSS",
            "storageUrn": "urn:adsk.objects:os.object:bimdocs.9ba6681e-1952-4d54-aac4-9de6d9858dd4/67a2d96a-b1d7-474f-86ba-9e01a5c0f5be.pdf",
            "name": "example.pdf"
          }
        ]
      }'

```

Show More

### Response

```
{
  "id": "5cb5d9da-060e-421e-bca9-97dd8b5cd800",
  "versionSetId": "7c2ecde0-2406-49f9-9199-50176848a0b7",
  "status": "PENDING",
  "createdAt": "2021-07-01T05:21:05.391Z",
  "createdBy": "45GPJ4KAX789",
  "createdByName": "John Smith",
  "updatedAt": "2021-07-01T05:21:05.391Z",
  "updatedBy": "45GPJ4KAX789",
  "updatedByName": "John Smith",
  "publishedAt": "2021-07-01T05:21:05.391Z",
  "publishedBy": "45GPJ4KAX789",
  "publishedByName": "John Smith",
  "publishedCount": 1
}

```

Show More
