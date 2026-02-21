# Task 5 â Prepare Cloud Storage

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/autocad/task5-prepare_cloud_storage/

---

# Task 5 â Prepare Cloud Storage

In Task 6 you use a WorkItem to execute the Activity you created in the previous task. At that time, the Automation Service takes a drawing file from a cloud storage repository as input, processes it, and uploads the text file containing layer names back to cloud storage.
The Automation Service does not retain the inputs or outputs. It simply downloads the input files, processes them, and saves the output files back to cloud storage. After that it discards the local copies of the files.

While you can use any cloud storage service, in this task. you use the Data Management API to access the Object Storage Service (OSS) to store the input drawing file as well as define a placeholder for the output text file.

The OSS is a cloud storage service that uses âBucketsâ as containers of data. The input and output files are stored as âObjectsâ in a Bucket.
For more information on the OSS, refer the [Data Management API documentation](/en/docs/data/v2/reference/http/).

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
| [POST /buckets/{bucketKey}/objects/{objectKey}/signed](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signed-POST) | Creates a signed URL to an object in an OSS bucket. |

## [Step 1 - Create a Bucket](#step-1-create-a-bucket)

The first thing to do when using the OSS service is to create a Bucket. Once a Bucket is created, you can store the input and output files inside of it as Objects.

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

- You must specify a name for your Bucket. Replace `<YOUR_BUCKET_KEY>` with a Bucket name.
- The Bucket name must be unique throughout all of the OSS service. If the Bucket name is already in use (even by another user) APS returns a `409 Conflict` error. In such a case, retry with another Bucket name.
- Bucket keys must consist of only lower case characters, numbers 0-9, and the underscore (_) character

### Response

```
{
    "bucketKey": "<YOUR_BUCKET_KEY>",
    "bucketOwner": "<YOUR_APP_CLIENT_ID>",
    "createdDate": 1571296694595,
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

Once you create the OSS bucket, you must upload the input file *Mechanical - Multileaders.dwg* to it. Uploading the file is a multi-step process, which is illustrated in steps 2 through 5. However, before you can upload the file:

1. Download the file *Mechanical - Multileaders.dwg* from <https://github.com/autodesk-platform-services/aps-tutorial-postman/tree/master/DA4ACAD/walkthrough_data>.

## [Step 2: Obtain signed URL to upload the input file](#step-2-obtain-signed-url-to-upload-the-input-file)

Before you upload a file to OSS, you must obtain a signed upload URL from OSS. You need to specify an Object Key for the file (an ID for the file), which is typically the file name of the file to upload.

**Note:**

- The endpoint used in this step supports generating multiple signed URLs to allow parallel upload of chunks of the same file. For this walkthrough we will use a single S3 URL. Please refer to the documentation of this endpoint for more information.

### Request

```
curl -X GET \
    "https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<OBJECT_KEY_4_INPUT_FILE>/signeds3upload"
    -H "Authorization: Bearer <YOUR_ACCESS_TOKEN>"

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
| `urls` | Contains the URL you must use to upload the file to OSS. You must use this URL in Step 3. |

## [Step 3: Upload the input file to OSS](#step-3-upload-the-input-file-to-oss)

The file itself can then be uploaded to the signed url as per the following example.

**Note:** This upload is directly to S3 and doesnât need an `Authorization` header.

### Request

```
curl -X PUT \
     "<SIGNED_UPLOAD_URL>" \
     --data-binary '@<PATH_TO_FILE_TO_UPLOAD>/Mechanical - Multileaders.dwg'

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
    "size": 88612,
    "contentType": "application/octet-stream",
    "location": "https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<YOUR_OBJECT_KEY>"
}

```

Show More

## [Step 5: Define an Object Key for resulting text file](#step-5-define-an-object-key-for-resulting-text-file)

The Activity `ListLayersActivity` you created in the previous task, generates a text file containing layer names as an output. To enable the Automation Service to save this file in OSS, you must provide/define the Object Key of the file. To illustrate the requests and responses of this walkthrough in subsequent tasks, code blocks use `<OBJECT_KEY_4_OUTPUT_FILE>` as the Object Key of the generated text file.

**Notes:**

- The access token should allow reading/writing from/to the object in the bucket.
- The OSS buckets and ACC/BIM360 buckets both work, you need to provide the correct token accordingly, such as providing 3-legged token for buckets owned by ACC/BIM360.
