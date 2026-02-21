# Task 6 â Prepare Cloud Storage

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/revit/step6-prepare-cloud-storage/

---

# Task 6 â Prepare Cloud Storage

In Task 7 you use a WorkItem to execute the Activity you created in the previous task. At that time, the Automation Service takes a Revit file as input, processes it, and uploads the result back to cloud storage.
The Automation Service does not retain the inputs or outputs. It simply downloads the input files, processes them, and saves the output files back to cloud storage. After that, it discards the local copies of the files.

While you can use any cloud storage service, in this task. you use the Data Management API to access the Object Storage Service (OSS) to store the input Revit file as well as define a placeholder for the output Revit file.

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

## [Step 1 - Create a Bucket](#step-1-create-a-bucket)

The first thing to do when using the OSS service is to create a Bucket. Once a Bucket is created, you can store the input and output files inside of it as objects.

### Request

```
curl -X POST \
    'https://developer.api.autodesk.com/oss/v2/buckets' \
    -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
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
- The Bucket Key must be unique throughout all of the OSS service. If the Bucket Key is already in use (even by another user) APS returns a `409 Conflict` error. In such a case, retry with another name.
- Bucket Keys must consist of only lower case characters, numbers 0-9, and the underscore (_) character

### Response

```
{
    "bucketKey": "<YOUR_BUCKET_KEY>",
    "bucketOwner": "<YOUR_APP_CLIENT_ID>",
    "createdDate": 156095829931,
    "permissions": [
        {
            "authId": "<YOUR_APP_CLIENT_ID>",
            "access": "full"
        }
    ],
    "policyKey": "transient"
}

```

Show More

Once you create the OSS bucket, you must upload the input file *DeleteWalls.rvt* to it. Uploading the file is a multi-step process, which is illustrated in steps 2 through 5. However, before you can upload the file:

1. Download the file *DeleteWalls.rvt* from <https://github.com/autodesk-platform-services/aps-tutorial-postmanblob/master/DA4Revit/walkthrough_data>.

**Notes:**

- Pay special attention to the URI where you will need to replace <YOUR_BUCKET_KEY> with the Bucket Key you selected when you created your Bucket in the previous step.
- You will also need to specify an Object Key for every item you upload and replace YOUR_OBJECT_KEY with the key you selected.

## [Step 2: Obtain signed URL to upload the input file](#step-2-obtain-signed-url-to-upload-the-input-file)

Before you upload a file to OSS, you must obtain a signed upload URL from OSS. You need to specify an Object Key for the file (an ID for the file), which is typically the file name of the file to upload.

**Note:**

- The endpoint used in this step supports generating multiple signed URLs to allow parallel upload of chunks of the same file. For this walkthrough we will use a single S3 URL. Please refer to the documentation of this endpoint for more information.

### Request

```
curl -X GET \
     "https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/YOUR_OBJECT_KEY/signeds3upload"
     -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT"

```

### Response

```
{
  "uploadKey": "<YOUR_UPLOAD_KEY>",
  "uploadExpiration": "2022-02-05T00:00:00Z",
  "urlExpiration": "2022-02-03T05:23:29Z",
  "urls": [
      "<SIGNED_UPLOAD_URL>"
  ]
}

```

Show More

| Attribute | Description |
| --- | --- |
| `uploadKey` | An ID to uniquely identify the upload session. You must use this ID in Step 4. |
| `urls` | Contains the URL you must use to upload the file to. You must use this URL in Step 3. |

## [Step 3: Upload a file to the signed url](#step-3-upload-a-file-to-the-signed-url)

The file itself can then be uploaded to the signed url as per the following example.

**Note:** This upload is directly to S3 and doesnât need an `Authorization` header.

### Example

```
curl -X PUT \
     "<SIGNED_UPLOAD_URL>"
     -H --data-binary '@<PATH_TO_FILE_TO_UPLOAD>/deleteWalls.rvt'

```

## [Step 4: Complete the upload](#step-4-complete-the-upload)

To make the uploaded file available for download, you must explicitly complete the upload.

**Note:** The value to be used for `uploadkey` for this request was returned in the response of step 2.

### Request

```
curl -X POST \
     "https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<OBJECT_KEY_4_INPUT_FILE>/signeds3upload" \
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
    "objectKey": "<OBJECT_KEY_4_INPUT_FILE>",
    "size": 55998,
    "contentType": "text/plain",
    "location": "https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<OBJECT_KEY_4_INPUT_FILE>"
}

```

Show More

## [Step 5: Define an Object Key for resulting RVT file](#step-5-define-an-object-key-for-resulting-rvt-file)

The Revit Add-in deletes the walls in the input file and produces an *.rvt* file that contains all other objects. To illustrate the requests and responses in the subsequent tasks of this walkthrough, code blocks use `<RESULT_FILE_OBJECT_KEY>` as the Object key of the resulting *.rvt* file.
