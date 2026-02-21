# Upload Files to ACC Sheets

Source: https://aps.autodesk.com/en/docs/acc/tutorials/sheets/upload-sheets/

---

# Upload Files to ACC Sheets

This tutorial demonstrates how to upload files to the ACC Sheets tool, which extracts and splits the file into individual sheets. The steps include, creating a version set, creating a storage object, generating a signed URL, uploading the file, extracting and splitting the file into individual sheets, checking the status of the upload, reviewing the sheets, and publishing them.

For more information about sheets, see the [Sheets Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Upload_And_Publish_Sheets).

Note the Sheets API currently only supports adding PDF files to ACC sheets. We will be supporting more files types in the future.

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps), and select Autodesk Construction Cloud API.
- [Provision your app](/en/docs/bim360/v1/tutorials/getting-started/manage-access-to-docs/) to acquire access to your ACC account.
- Acquire a [3-legged OAuth token](/en/docs/oauth/v2/tutorials/get-3-legged-token/) with `data:read` and `data:write` scopes.
- Find the relevant project ID for the project you want to upload the sheets to by following the [Retrieve a Project ID](/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. In this example, assume the project ID is `9ba6681e-1952-4d54-aac4-9de6d9858dd4`.
- Verify that you have access to the relevant ACC project.

## [Step 1: Create a Version Set](#step-1-create-a-version-set)

Version sets are used by document managers to group specific versions of sheets together. When adding sheets you need to either add them to an existing version set or to a new version set. In this tutorial we will create a new version set. Note that you are required to select an issuance date (`issuanceDate`) in ISO-8601 format when creating a version set.

Create a version set by calling [POST version-sets](/en/docs/acc/v1/reference/http/sheets-version-sets-POST) using the project ID (`9ba6681e-1952-4d54-aac4-9de6d9858dd4`) and an issuance date (`2021-04-26`).

### request

```
curl 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/version-sets' \
  -X POST \
  -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "First Set",
    "issuanceDate": "2021-04-26"
  }'

```

Show More

### response

```
{
  "id": "7c2ecde0-2406-49f9-9199-50176848a0b7",
  "name": "First Set",
  "issuanceDate": "2021-04-26",
  "createdAt": "2021-04-26T05:49:38.318Z",
  "createdBy": "KPN8P8P65K",
  "createdByName": "John Smith",
  "updatedAt": "2021-04-26T05:49:38.318Z",
  "updatedBy": "KPN8P8P65K",
  "updatedByName": "John Smith"
}

```

Show More

Note the ID (`7c2ecde0-2406-49f9-9199-50176848a0b7`) of the version set.

## [Step 2: Create a Storage Object](#step-2-create-a-storage-object)
> To create a storage object for the upload, call [POST storage](/en/docs/acc/v1/reference/http/sheets-storage-POST) using the project ID (`9ba6681e-1952-4d54-aac4-9de6d9858dd4`) and a filename (`example.pdf`).

### request

```
curl 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/storage' \
  -X POST \
  -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
  -H 'Content-Type: application/json' \
  -d '{
    "fileName": "example.pdf"
  }'

```

### response

```
{
  "urn": "urn:adsk.objects:os.object:bimdocs.9ba6681e-1952-4d54-aac4-9de6d9858dd4/67a2d96a-b1d7-474f-86ba-9e01a5c0f5be.pdf"
}

```

The storage URN includes the following sections: `<urn:adsk.objects:os.object>:<bucket_key>/<object_key>`. In the above response, the bucket key is `bimdocs.9ba6681e-1952-4d54-aac4-9de6d9858dd4` and the object key is `67a2d96a-b1d7-474f-86ba-9e01a5c0f5be.pdf`.

Note that although this endpoint is similar to the Data Management endpoint [Data Management POST storage](/en/docs/data/v2/reference/http/projects-project_id-storage-POST), you can only use Data Management storage objects for uploading ACC files. You can only use the [ACC POST storage](/en/docs/acc/v1/reference/http/sheets-storage-POST) endpoint for uploading sheets.

## [Step 3: Generate a Signed S3 URL](#step-3-generate-a-signed-s3-url)

To generate a signed S3 URL for the storage object, call [GET buckets/:bucketKey/objects/:objectKey/signeds3upload](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-GET) using the bucket key (`bimdocs.9ba6681e-1952-4d54-aac4-9de6d9858dd4`) and the object key (`67a2d96a-b1d7-474f-86ba-9e01a5c0f5be.pdf`).

This endpoint supports generating multiple signed URLs, which allows you to upload multiple chunks of the same file in parallel. For more information, see [GET signeds3upload](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-GET).

### request

```
curl 'https://developer.api.autodesk.com/oss/v2/buckets/bimdocs.9ba6681e-1952-4d54-aac4-9de6d9858dd4/objects/67a2d96a-b1d7-474f-86ba-9e01a5c0f5be.pdf/signeds3upload' \
  -X GET \
  -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT'

```

### response

```
{
  "uploadKey": "AQICAHifrJ6-BSHUmjAat4..........QWI-fuvghN23akgePMdmykV",
  "uploadExpiration": "2021-04-28T00:00:00Z",
  "urlExpiration": "2021-04-26T05:50:32Z",
  "urls": [
      "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/26668812-6bb1-4f80-bab2-09776f24fd98?uploadId=[UPLOAD_ID]&partNumber=1&X-Amz-Security-Token=[AMZ_TOKEN]%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220203T052230Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=[AMZ_CREDENTIAL]%2F20220203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=[AMZ_SIGNATURE]"
  ]
}

```

Show More

Note the `urls` attribute.

## [Step 4: Upload a File to the Signed URL](#step-4-upload-a-file-to-the-signed-url)

To upload the file to the signed URL, use a PUT method and the `urls` attribute as the URI.

Note that you should not use a bearer token with this call.

### Request

```
curl 'https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/26668812-6bb1-4f80-bab2-09776f24fd98?uploadId=[UPLOAD_ID]&partNumber=1&X-Amz-Security-Token=[AMZ_TOKEN]%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220203T052230Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=[AMZ_CREDENTIAL]%2F20220203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=[AMZ_SIGNATURE]' \
  -X PUT \
  --data-binary @D:\example.pdf

```

Note that a successful call (`200`) returns an empty response.

## [Step 5: Complete the Upload](#step-5-complete-the-upload)

Use the bucket key (`bimdocs.9ba6681e-1952-4d54-aac4-9de6d9858dd4`), the object key (`67a2d96a-b1d7-474f-86ba-9e01a5c0f5be.pdf`) and the upload key (`AQICAHifrJ6-BSHUmjAat4..........QWI-fuvghN23akgePMdmykV`) to call [POST buckets/:bucket_key/objects/:object_key/signeds3upload](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-POST) to complete the upload.

This endpoint needs to be called within 24 hours from the time you began uploading the file.

### Request

```
curl 'https://developer.api.autodesk.com/oss/v2/buckets/bimdocs.9ba6681e-1952-4d54-aac4-9de6d9858dd4/objects/67a2d96a-b1d7-474f-86ba-9e01a5c0f5be.pdf/signeds3upload' \
  -X POST \
  -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
  -d '{
    "uploadKey": "AQICAHifrJ6-BSHUmjAat4..........QWI-fuvghN23akgePMdmykV"
  }'

```

### Repsonse

```
{
  "bucketKey" : "bimdocs.9ba6681e-1952-4d54-aac4-9de6d9858dd4",
  "objectId" : "urn:adsk.objects:os.object:bimdocs.9ba6681e-1952-4d54-aac4-9de6d9858dd4/67a2d96a-b1d7-474f-86ba-9e01a5c0f5be.pdf",
  "objectKey" : "67a2d96a-b1d7-474f-86ba-9e01a5c0f5be.pdf",
  "size" : 1879394,
  "contentType" : "application/octet-stream",
  "location" : "https://developer.api.autodesk.com/oss/v2/buckets/bimdocs.9ba6681e-1952-4d54-aac4-9de6d9858dd4/objects/67a2d96a-b1d7-474f-86ba-9e01a5c0f5be.pdf"
}

```

Show More

## [Step 6: Extract and Split the File into Sheets](#step-6-extract-and-split-the-file-into-sheets)

Extract and split the files into individual sheets by calling [POST uploads](/en/docs/acc/v1/reference/http/sheets-uploads-POST). Use the version set ID created in step 1 (`7c2ecde0-2406-49f9-9199-50176848a0b7`), and the storage URN created in step 2 (`urn:adsk.objects:os.object:bimdocs.9ba6681e-1952-4d54-aac4-9de6d9858dd4/67a2d96a-b1d7-474f-86ba-9e01a5c0f5be.pdf`).

Note that you cannot not start extracting and splitting the file into sheets before generating a signed URL.

### request

```
curl 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/uploads' \
  -X POST \
  -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
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

### response

```
{
  "id": "5cb5d9da-060e-421e-bca9-97dd8b5cd800",
  "versionSetId": "7c2ecde0-2406-49f9-9199-50176848a0b7",
  "status": "PROCESSING",
  "createdAt": "2021-04-26T05:51:16.233Z",
  "createdBy": "KPN8P8P65K",
  "createdByName": "John Smith",
  "updatedAt": "2021-04-26T05:51:16.233Z",
  "updatedBy": "KPN8P8P65K",
  "updatedByName": "John Smith",
  "publishedAt": null,
  "publishedBy": null,
  "publishedByName": null
}

```

Show More

Note the upload ID (`5cb5d9da-060e-421e-bca9-97dd8b5cd800`).

Once the file is extracted and split into individual sheets, you will be able to find the sheets displayed in the Publish Log tab in the Sheets tool.

Note that this endpoint is asynchronous and initiates a job that runs in the background rather than halting execution of your program. The next step shows you how to check when the job is complete.

## [Step 7: Check the Upload Status](#step-7-check-the-upload-status)

Check the asynchronous job that was initiated in the previous step is complete by using the upload ID (`5cb5d9da-060e-421e-bca9-97dd8b5cd800`) to call [GET uploads/:uploadId](/en/docs/acc/v1/reference/http/sheets-uploads-uploadId-GET) to get the status of the upload.

### request

```
curl 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/uploads/5cb5d9da-060e-421e-bca9-97dd8b5cd800' \
  -X GET \
  -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT'

```

### response

```
{
  "id": "5cb5d9da-060e-421e-bca9-97dd8b5cd800",
  "versionSetId": "7c2ecde0-2406-49f9-9199-50176848a0b7",
  "status": "IN_REVIEW",
  "createdAt": "2021-04-26T05:51:16.233Z",
  "createdBy": "KPN8P8P65K",
  "createdByName": "John Smith",
  "updatedAt": "2021-04-26T05:51:16.233Z",
  "updatedBy": "KPN8P8P65K",
  "updatedByName": "John Smith",
  "publishedAt": null,
  "publishedBy": null,
  "publishedByName": null
}

```

Show More

Note the status. In order to review the sheets, the processing needs have been completed. You can verify this by checking that the status has changed to `IN_REVIEW`. Initially, the status of the upload is `PROCESSING`.

## [Step 8: Review the Sheets](#step-8-review-the-sheets)

Before reviewing the sheets the status of the upload needs to be `IN_REVIEW`. See previous step.

To review the sheets, use the upload ID (`5cb5d9da-060e-421e-bca9-97dd8b5cd800`) to call [GET uploads/:uploadId/review-sheets](/en/docs/acc/v1/reference/http/sheets-review-sheets-GET).

The review sheets are only available when the upload is in `IN_REVIEW` status. To check the status, call GET uploads/:uploadId.

### request

```
curl 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/uploads/5cb5d9da-060e-421e-bca9-97dd8b5cd800/review-sheets' \
  -X GET \
  -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT'

```

### response

```
{
  "results": [
    {
      "id": "0d7a5883-1694-3078-a06d-ad24413f8b06",
      "page": 1,
      "fileName": "example.pdf",
      "number": "A-01",
      "title": "Floor One",
      "deleted": false,
      "tags": [],
      "rotation": 0,
      "processingState": "PROCESSING"
    },
    {
      "id": "8451263f-b22f-3a21-8ce4-721f67c98dd0",
      "page": 2,
      "fileName": "example.pdf",
      "number": "A-02",
      "title": "Floor Two",
      "deleted": false,
      "tags": [],
      "rotation": 0,
      "processingState": "PROCESSING"
    }
  ],
  "pagination": {
    "limit": 100,
    "offset": 0,
    "previousUrl": null
  }
}

```

Show More

Note the IDs of the sheets (`results.[id]`).

## [Step 9: Get the Thumbnails of the Review Sheets](#step-9-get-the-thumbnails-of-the-review-sheets)

Thumbnails provide more viewable information about the review sheets.
It is recommended to review the thumbnails before you make any updates to the review sheets.

Use the upload ID and review sheet IDs to call [POST thumbnails:batch-get](/en/docs/acc/v1/reference/http/sheets-thumbnailsbatch-get-POST) to get the thumbnails.

### request

```
curl 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/uploads/5cb5d9da-060e-421e-bca9-97dd8b5cd800/thumbnails:batch-get' \
  -X POST \
  -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
  -H 'Content-Type: application/json' \
  -d '{
    "reviewSheetsIds": [
      "0d7a5883-1694-3078-a06d-ad24413f8b06",
      "8451263f-b22f-3a21-8ce4-721f67c98dd0"
    ],
    "type": "small"
  }'

```

Show More

### response

```
{
  "results": [
    {
      "reviewSheetId": "0d7a5883-1694-3078-a06d-ad24413f8b06",
      "size": [
        256,
        128
      ],
      "signedUrl": "https://plangrid-shredder-buckets-pro-sheetprocessingprod-ahxn8ipd4aos.s3.amazonaws.com/a1428dce-8c10-41e1-90af-13f80db6d3f1.png?AWSAccessKeyId=ASIA2QXZWG5ODHIRNP72&Signature=%2Bnmjn89t5aKLxPPrETUQ5ZscwNA%3D&x-amz-security-token=FwoGZXIvYXdzENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDKAlYsecmyrQAQbF3CKtAeqzPkIdiFeovwUW%2FQfSs%2FQmrG5CmrfoJUqczF6%2FUQBF5P0DaF6juE6K4qwtc84cPzCRcoM7ki3ClORC%2BpDEN5M4uYGB6KUiw%2B32U3YFtSvZ7p4xj8Flnj7CNM0Nkj%2FlC8df2mxxjJtw0mpUR5OfKFS6D0G95KKCnOu3kgAtoJ4IZ1M%2F%2B31zwujd%2B%2F2zfCP3x9Tk28D004ljZ42hpXYRWjjxYf8TkXngI5zz25qGKOPlnoQGMi1gkVjihKmq4x%2B3y5NPEs36jEcY1FcIje7g5JVo4XFlfXYH%2BsvlghVDe00LrqU%3D&Expires=1619391679"
    },
    {
      "reviewSheetId": "8451263f-b22f-3a21-8ce4-721f67c98dd0",
      "size": [
        256,
        128
      ],
      "signedUrl": "https://plangrid-shredder-buckets-pro-sheetprocessingprod-ahxn8ipd4aos.s3.amazonaws.com/ba20bede-8c0d-4150-8c7c-871a48c71746.png?AWSAccessKeyId=ASIA2QXZWG5ODJKBUBE7&Signature=rSRmGdB05%2BY9cI5EJSazPQOcryQ%3D&x-amz-security-token=FwoGZXIvYXdzEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDFsZ%2F%2FNUJ48uGGNQ2yKtAVmdPptfTb%2FNj2947WtD0gAZAaiME%2BP2znNoQ%2FuoaH2Y3ZnQ4SxfsMIT%2BVVd1SUm74cXV6RQhR1peITk5MSMwlYJzqzg0xcoIbmy%2FbX08o06%2F62bGp1XxrMhLtlP%2F94HAKUW2r5cedSpFcVmzA1%2FjZw0SfKrlHXrfK8R0agX1jGQZ2x4GxZc1o85VMIpZSnKy2PNxt41KxrV2EYSA1O0KRrnxWxXD24y9RsvBQG2KPnZo4QGMi0pzN6XdDRMIqswIbwuYVlbg1zLCPzhwz70QwHj44dq0j%2BlYedYDWu0fqfS6ko%3D&Expires=1619391679"
    }
  ]
}

```

Show More

## [Step 10: Update the Review Sheets](#step-10-update-the-review-sheets)

You can update the number, title, and tags for each sheet. The updated information will appear in the sheets after you publish them.

For a PDF file, the initial number and title of the review sheets are determined by the OCR scan.

To update the sheets they need to have a `READY` status. To check the status, call GET uploads/:uploadId.

Use the upload ID and review sheet IDs to call [PATCH uploads/:uploadId/review-sheets](/en/docs/acc/v1/reference/http/sheets-review-sheets-PATCH) to update the review sheets. In this example, we are updating the number and the tags.

### request

```
curl 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/uploads/5cb5d9da-060e-421e-bca9-97dd8b5cd800/review-sheets' \
  -X PATCH \
  -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
  -H 'Content-Type: application/json' \
  -d '[
    {
      "id": "0d7a5883-1694-3078-a06d-ad24413f8b06",
      "number": "A-01X",
      "tags": [
        "april",
        "floor"
      ]
    }
  ]'

```

Show More

### response

```
{
  "results": [
    {
      "id": "0d7a5883-1694-3078-a06d-ad24413f8b06",
      "page": 1,
      "fileName": "example.pdf",
      "number": "A-01X",
      "title": "Floor One",
      "deleted": false,
      "tags": [
        "april",
        "floor"
      ],
      "rotation": 0,
      "processingState": "PROCESSING"
    }
  ]
}

```

Show More

Note that there are some limitations for the number, title, and tag values. See [PATCH uploads/:uploadId/review-sheets](/en/docs/acc/v1/reference/http/sheets-review-sheets-PATCH) for more details.

## [Step 11: Publish the Review Sheets](#step-11-publish-the-review-sheets)

Call [POST uploads/:uploadId/review-sheets:publish](/en/docs/acc/v1/reference/http/sheets-review-sheetspublish-POST) to publish the review sheets.

In order to publish the sheets they need to have either a `READY` status or a `FAILED` status. To check the statuses, call [GET review-sheets](/en/docs/acc/v1/reference/http/sheets-review-sheets-GET).

### request

```
curl 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/uploads/5cb5d9da-060e-421e-bca9-97dd8b5cd800/review-sheets:publish' \
  -X POST \
  -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT'

```

To check the publishing state, call [GET uploads/:uploadId](/en/docs/acc/v1/reference/http/sheets-uploads-uploadId-GET). When publishing is initiated it has a `PUBLISHING` status. When the publishing is complete it has a `COMPLETE` status.

### response

```

```

## [Step 12: Retrieve the Published Sheets](#step-12-retrieve-the-published-sheets)

To retrieve the published sheets, use the version set ID to call [GET sheets](/en/docs/acc/v1/reference/http/sheets-sheets-GET).

Note that in this tutorial because we uploaded the sheets to a new version set it only contains the sheets from this upload. If you upload sheets to an existing version set, it may contain multiple sets of sheets.

### request

```
curl 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/sheets?filter[versionSetId]=7c2ecde0-2406-49f9-9199-50176848a0b7' \
  -X GET \
  -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT'

```

### response

```
{
  "results": [
    {
      "id": "0d7a5883-1694-3078-a06d-ad24413f8b06",
      "number": "A-01X",
      "title": "Floor One",
      "versionSet": {
        "id": "7c2ecde0-2406-49f9-9199-50176848a0b7",
        "name": "First Set",
        "issuanceDate": "2021-04-26"
      },
      "tags": [
        "april",
        "floor"
      ],
      "isCurrent": true,
      "uploadFileName": "example.pdf",
      "uploadId": "5cb5d9da-060e-421e-bca9-97dd8b5cd800",
      "createdAt": "2021-04-26T06:05:16.233Z",
      "createdBy": "KPN8P8P65K",
      "createdByName": "John Smith",
      "updatedAt": "2021-04-26T05:51:16.233Z",
      "updatedBy": "KPN8P8P65K",
      "updatedByName": "John Smith",
      "deleted": false,
      "deletedAt": null,
      "deletedBy": null,
      "deletedByName": null,
      "viewable": {
        "urn": "urn:adsk.bimdocs:seed:207edb73-69c2-43d2-ba0e-e2ffe9fdcb56",
        "guid": "cc3eb847-737f-3408-bdbd-e2628a02b8de"
      }
    },
    {
      "id": "8451263f-b22f-3a21-8ce4-721f67c98dd0",
      "number": "A-02",
      "title": "Floor Two",
      "versionSet": {
        "id": "7c2ecde0-2406-49f9-9199-50176848a0b7",
        "name": "First Set",
        "issuanceDate": "2021-04-26"
      },
      "tags": [],
      "isCurrent": true,
      "uploadFileName": "example.pdf",
      "uploadId": "5cb5d9da-060e-421e-bca9-97dd8b5cd800",
      "createdAt": "2021-04-26T06:05:16.233Z",
      "createdBy": "KPN8P8P65K",
      "createdByName": "John Smith",
      "updatedAt": "2021-04-26T05:51:16.233Z",
      "updatedBy": "KPN8P8P65K",
      "updatedByName": "John Smith",
      "deleted": false,
      "deletedAt": null,
      "deletedBy": null,
      "deletedByName": null,
      "viewable": {
        "urn": "urn:adsk.bimdocs:seed:207edb73-69c2-43d2-ba0e-e2ffe9fdcb56",
        "guid": "4ca3ab9f-aa9d-1ac7-0936-c1badd85e3a7"
      }
    }
  ],
  "pagination": {
    "limit": 100,
    "offset": 0,
    "previousUrl": null,
    "nextUrl": null,
    "totalResults": 2
  }
}

```

Show More
