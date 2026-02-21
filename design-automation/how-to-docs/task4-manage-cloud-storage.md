# Task 4 -  Prepare Cloud Storage

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/3dsmax/task4-manage-cloud-storage/

---

# Task 4 - Prepare Cloud Storage

In Task 5 you use a WorkItem to execute the Activity you created in the previous task. At that time the Automation Service takes a 3ds Max scene file from cloud storage as input, processes it, and uploads the resulting output file back to cloud storage.
The Automation Service does not retain the inputs or outputs. It simply downloads the input files, processes them, and saves the output files back to cloud storage. After that it discards the local copies of the files.

While you can use any cloud storage service for this purpose, in this task, you will use the Object Storage Service (OSS) using the Data Management API. In this task you will upload the input files to OSS and create place holders for the output file.

By the end of this task, you will be able to:
> - Create a Bucket to store the input and output files.
> - Upload a file to a Bucket.
> - Obtain a temporary signed URL that enables the Automation Service to download or upload a file.

You will use the following operations in this task:

| HTTP Request | Description |
| --- | --- |
| [POST /buckets](/en/docs/data/v2/reference/http/buckets-POST) | Creates an OSS Bucket. |
| [GET /buckets/{bucketKey}/objects/{objectKey}/signeds3upload](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-GET) | Requests an S3 signed URL with which to upload an object. |
| [POST /buckets/{bucketKey}/objects/{objectKey}/signeds3upload](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-POST) | Instructs OSS to complete the object creation process after the bytes have been uploaded directly to S3. |

## [Step 1 - Create Bucket](#step-1-create-bucket)

The first step when using the OSS service is to create a Bucket. Once a Bucket is created, you will be able to store Objects inside of it.

### Request

```
curl -X POST \
    'https://developer.api.autodesk.com/oss/v2/buckets' \
    -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
    -H 'Content-Type: application/json' \
    -H 'x-ads-region: US' \
        -d '{
            "bucketKey": "<YOUR_BUCKET_KEY>",
            "access": "full",
            "policyKey": "transient"
        }'

```

Show More

**Notes:**

- You must specify a name for your Bucket. Replace `<YOUR_BUCKET_KEY>` with the name you chose.
- The Bucket name must be unique throughout all of the OSS service. If the Bucket name is already in use (even by another user) APS returns a `409 Conflict` error. In such a case, retry with another Bucket name.
- Bucket keys must consist of only lower case characters, numbers 0-9, and the underscore (_) character.

### Response

```
{
    "bucketKey": "<YOUR_BUCKET_KEY>",
    "bucketOwner": "YOUR_APP_CLIENT_ID",
    "createdDate": 156095829931,
    "permissions": [
        {
            "authId": "T05H372IE11Kmkksdh73ndj0qie2f6nib",
            "access": "full"
        }
    ],
    "policyKey": "transient"
}

```

Show More

Once you create the OSS bucket, you must upload the zip file that contains the 3ds Max files (*input.zip*) to process and the MaxScript file (*TwistIt.ms*) to OSS. Uploading a file is a multi-step process, which is illustrated in steps 2 through 4 and steps 5 through 7. However, before you can upload the file:

- Download the following files from <https://github.com/autodesk-platform-services/aps-tutorial-postman/tree/master/DA43dsMax/walkthrough_data>.
  1. *input.zip*
  2. *TwistIt.ms*

## [Step 2: Obtain signed URL to upload the input zip file](#step-2-obtain-signed-url-to-upload-the-input-zip-file)

Before you upload a file to OSS, you must obtain a signed S3 upload URL from OSS. You need to specify an Object Key for the file (an ID for the file), which is typically the file name of the file to upload.

**Note:**

- The endpoint used in this step supports generating multiple signed URLs to allow parallel upload of chunks of the same file. For this walkthrough we will use a single S3 URL. Please refer to the documentation of this endpoint for more information.

### Request

```
curl -X GET \
    "https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<OBJECT_KEY_4_INPUT_ZIP_FILE>/signeds3upload"
    -H "Authorization: Bearer <YOUR_ACCESS_TOKEN>"

```

### Response

```
{
  "uploadKey": "<YOUR_UPLOAD_KEY>",
  "uploadExpiration": "2023-10-08T00:00:00Z",
  "urlExpiration": "2023-10-05T03:46:50Z",
  "urls": [
      "<SIGNED_UPLOAD_URL_4_INPUT_ZIP_FILE>"
  ]
}

```

Show More

| Attribute | Description |
| --- | --- |
| `uploadKey` | An ID to uniquely identify the upload session. You must use this ID in Step 4. |
| `urls` | Contains the URL you must use to upload the file to OSS. You must use this URL in Step 3. |

## [Step 3: Upload the input zip file to OSS](#step-3-upload-the-input-zip-file-to-oss)

The file itself can then be uploaded to the signed url as per the following example.

**Note:** This upload is directly to S3 and doesnât need an `Authorization` header.

### Request

```
curl -X PUT \
     "<SIGNED_UPLOAD_URL_4_INPUT_ZIP_FILE>" \
     --data-binary '@<PATH_TO_FILE_TO_UPLOAD>/input.zip'

```

## [Step 4: Complete uploading the input zip file](#step-4-complete-uploading-the-input-zip-file)

To make the uploaded file available for download, you must explicitly complete the upload.

**Note:** The value to be used for `uploadkey` for this request was returned in the response of step 2.

### Request

```
curl -X POST \
     "https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<OBJECT_KEY_4_INPUT_ZIP_FILE>/signeds3upload" \
      -H "Authorization: Bearer <YOUR_ACCESS_TOKEN>" \
      -d '{
            "uploadKey": "<YOUR_UPLOAD_KEY>"
        }'

```

### Response

```
{
    "bucketKey": "<YOUR_BUCKET_KEY>",
    "objectId": "urn:adsk.objects:os.object:<YOUR_BUCKET_KEY>/<OBJECT_KEY_4_INPUT_FILE>",
    "objectKey": "<OBJECT_KEY_4_INPUT_ZIP_FILE>",
    "size": 55998,
    "contentType": "application/octet-stream",
    "location": "https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<OBJECT_KEY_4_INPUT_ZIP_FILE>"
}

```

Show More

## [Step 5: Obtain signed URL to upload the input MaxScript file](#step-5-obtain-signed-url-to-upload-the-input-maxscript-file)

Before you upload a file to OSS, you must obtain a signed S3 upload URL from OSS. You need to specify an Object Key for the file (an ID for the file), which is typically the file name of the file to upload.

**Note:**

- The endpoint used in this step supports generating multiple signed URLs to allow parallel upload of chunks of the same file. For this walkthrough we will use a single S3 URL. Please refer to the documentation of this endpoint for more information.

### Request

```
curl -X GET \
    "https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<OBJECT_KEY_4_MAXSCRIPT_FILE>/signeds3upload"
    -H "Authorization: Bearer <YOUR_ACCESS_TOKEN>"

```

### Response

```
{
  "uploadKey": "<YOUR_UPLOAD_KEY>",
  "uploadExpiration": "2023-10-08T00:00:00Z",
  "urlExpiration": "2023-10-05T03:54:19Z",
  "urls": [
      "<SIGNED_UPLOAD_URL_4_MAXSCRIPT_FILE>"
  ]
}

```

Show More

| Attribute | Description |
| --- | --- |
| `uploadKey` | An ID to uniquely identify the upload session. You must use this ID in Step 4. |
| `urls` | Contains the URL you must use to upload the file to OSS. You must use this URL in Step 3. |

## [Step 6: Upload the input MaxScript file](#step-6-upload-the-input-maxscript-file)

The file itself can then be uploaded to the signed url as per the following example.

**Note:** This upload is directly to S3 and doesnât need an `Authorization` header.

### Request

```
curl -X PUT \
     "<SIGNED_UPLOAD_URL_4_MAXSCRIPT_FILE>" \
     --data-binary '@<PATH_TO_FILE_TO_UPLOAD>/TwistIt.ms'

```

## [Step 7: Complete uploading the MaxScript file](#step-7-complete-uploading-the-maxscript-file)

To make the uploaded file available for download, you must explicitly complete the upload.

**Note:** The value to be used for `uploadkey` for this request was returned in the response of step 2.

### Request

```
curl -X POST \
     "https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<OBJECT_KEY_4_MAXSCRIPT_FILE>/signeds3upload" \
      -H "Authorization: Bearer <YOUR_ACCESS_TOKEN>" \
      -d '{
            "uploadKey": "<YOUR_UPLOAD_KEY>"
        }'

```

### Response

```
{
    "bucketKey": "<YOUR_BUCKET_KEY>",
    "objectId": "urn:adsk.objects:os.object:<YOUR_BUCKET_KEY>/<OBJECT_KEY_4_INPUT_FILE>",
    "objectKey": "<OBJECT_KEY_4_INPUT_ZIP_FILE>",
    "size": 525,
    "contentType": "application/octet-stream",
    "location": "https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<OBJECT_KEY_4_INPUT_ZIP_FILE>"
}

```

Show More

## [Step 8: Define an Object Key for resulting text file](#step-8-define-an-object-key-for-resulting-text-file)

The Activity `executeScript` you created in the previous task, generates a zip file as an output. To enable the Automation Service to save this file in OSS, you must provide/define an Object Key for the file. To illustrate the requests and responses of this walkthrough in subsequent tasks, code blocks use `<OBJECT_KEY_4_OUTPUT_FILE>` as the Object Key of the generated text file.
