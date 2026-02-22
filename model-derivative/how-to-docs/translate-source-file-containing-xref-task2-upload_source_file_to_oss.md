# Task 2 â Upload Source File to OSS

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/translate-source-file-containing-xref/task2-upload_source_file_to_oss/

---

# Task 2 â Upload Source File to OSS

The Object Storage Service (OSS) is a generic Cloud Storage Service that is part of the Data Management API. In this task, you upload an Inventor Assembly file (a *.iam* file) and also the three Part files (*.ipt* files) it references. The following image shows the folder structure that must be maintained between the Assembly file and Part files.

![../../../../_images/tutorial_03_scissors_files.png](../../../../_images/tutorial_03_scissors_files.png)

You can download these files from the *walkthrough_data* folder of the GitHub repository containing the Postman Collection for this walkthrough.

By the end of this task you will be able to:

- Create a Bucket to store the files.
- Obtain a signed URL to upload a file to the bucket.
- Upload a file to the Bucket.
- Obtain the URN of the uploaded file.
- Convert the URN to a Base64-encoded URN.

You will use the following operations in this task:

| Operation | HTTP Request |
| --- | --- |
| [Create a Bucket](/en/docs/data/v2/reference/http/buckets-POST/) | POST /buckets |
| [Get a Signed URL to Upload a File](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-GET) | GET /buckets/{bucketKey}/objects/{objectKey}/signeds3upload |
| [Finalize File Upload](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-POST) | POST /buckets/{bucketKey}/objects/{objectKey}/signeds3upload |

## [Step 1 - Create a Bucket](#step-1-create-a-bucket)

The first thing to do when using the OSS service is to create a Bucket. Once a Bucket is created, you can store files in it as Objects.

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

- You must specify a name for your Bucket. Replace `<YOUR_BUCKET_KEY>` with a name for the Bucket.
- Bucket keys must consist of only lower case characters, numbers 0-9, and the underscore (_) character
- The Bucket key must be unique throughout all of the OSS service. If the Bucket name is already in use (even by another user) the system returns a `409 Conflict` error. In such a case, retry with another Bucket name.

### Response

```
{
    "bucketKey": "<YOUR_BUCKET_KEY>",
    "bucketOwner": "<YOUR_CLIENT_ID>",
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

## [Step 2 - Obtain Signed URL for Assembly File](#step-2-obtain-signed-url-for-assembly-file)

To upload a file to an OSS bucket, you need to have a signed upload URL. To obtain a signed URL:

### Request

```
curl -X GET \
    'https://developer.api.autodesk.com/oss/v2/buckets/YOUR_BUCKET_KEY/objects/YOUR_OBJECT_KEY/signeds3upload?minutesExpiration=LIFESPAN_OF_URL' \
    -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
    -H 'Content-Type: application/json'

```

- Replace <YOUR_ACCESS_TOKEN> with the access token you obtained in Task 1.
- Replace <LIFESPAN_OF_URL> with 10. This will ensure that the signed URL that is returned will be valid for 10 minutes.
- Replace <YOUR_OBJECT_KEY> with *scissors.iam*, which is the name of the file we recommend that you upload.

### Response

```
{
    "uploadKey": "<YOUR_UPLOAD_KEY>",
    "uploadExpiration": "2022-04-08T00:00:00Z",
    "urlExpiration": "2022-04-06T17:59:46Z",
    "urls": ["<SIGNED_UPLOAD_URL>"],
    "location": "https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<YOUR_OBJECT_KEY>"
}

```

- Note down the values returned for `uploadKey` <YOUR_UPLOAD_KEY> and `urls` <SIGNED_UPLOAD_URL>. You will use these values in subsequent requests.

## [Step 3 - Upload the Assembly file](#step-3-upload-the-assembly-file)

1. Download the file *scissors.iam* from <https://github.com/autodesk-platform-services/aps-tutorial-postman/tree/master/ModelDerivative_03/walkthrough_data>.
2. Send a request to upload the file to the Bucket.

### Request

```
curl -X PUT \
    '<SIGNED_UPLOAD_URL>'\
    --data-binary '@<PATH_TO_YOUR_FILE_TO_UPLOAD>'

```

## [Step 4 - Finalize Upload](#step-4-finalize-upload)

To make the uploaded file available for download, you must finalize the upload. To complete the upload:

### Request

```
curl -X POST \
    'https://developer.api.autodesk.com/oss/v2/buckets/ossBucketKey/objects/ossSourceFileObjectKey/signeds3upload' \
    -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
    -H 'Content-Type: application/json' \
    -d '{
        "ossbucketKey": "<YOUR_BUCKET_KEY>",
        "ossSourceFileObjectKey": "<YOUR_OBJECT_KEY>",
        "access": "full",
        "uploadKey": "<YOUR_UPLOAD_KEY>"
        }'

```

Show More

### Response

```
{
    "bucketKey": "<YOUR_BUCKET_KEY>",
    "objectId": "<YOUR_OBJECT_ID>",
    "objectKey": "<YOUR_OBJECT_KEY>",
    "size": "140800"
    "contentType": "application/octet-stream",
    "location": "https://developer.api.autodesk.com/oss/v2/buckets/bucketKey/objects/inputfile"
    "permissions": [
        {
            "authId": "<YOUR_ACCESS_TOKEN>",
            "access": "full"
        }
    ],
    "policyKey": "transient"
}

```

Show More

- Note down the value of the `objectId` parameter in the response. This is the URN of the Assembly file. You will need it for the next task.

## [Step 5 - Convert the Assembly File URN to a Base64-encoded URN](#step-5-convert-the-assembly-file-urn-to-a-base64-encoded-urn)

Most Model Derivative requests require the URN of the source file to be a Base64-encoded URN.

- Use [this online tool](http://www.freeformatter.com/base64-encoder.html) to convert the URN of the source file (The value of `objectId` you obtained in the previous step).

For further information, see the full list of [Base64 variants](https://en.wikipedia.org/wiki/Base64#Variants_summary_table).

We recommend using the unpadded option (RFC 6920), since it uses URL-safe alphabets. The following example shows a URN, its Base64-encoded form, and its URL safe Base64-encoded form:

| raw | `urn:adsk.objects:os.object:md_tute_01/Tuner.zip` |
| --- | --- |
| Base64 | `dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bWRfdHV0ZV8wMS9UdW5lci56aXA=` |
| URL-safe Base64 (no padding) | `dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bWRfdHV0ZV8wMS9UdW5lci56aXA` |

## [Step 6 - Obtain Signed URL for First Part File](#step-6-obtain-signed-url-for-first-part-file)

To upload a file to an OSS bucket, you need to have a signed upload URL. To obtain a signed URL:

### Request

```
curl -X GET \
    'https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<YOUR_OBJECT_KEY>/signeds3upload?minutesExpiration=<LIFESPAN_OF_URL>' \
    -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
    -H 'Content-Type: application/json'

```

**Notes:**

- Replace <YOUR_ACCESS_TOKEN> with the access token you obtained in Task 1.
- Replace <LIFESPAN_OF_URL> with 10. This will ensure that the signed URL that is returned will be valid for 10 minutes.
- Replace <YOUR_OBJECT_KEY> with *blade_main.ipt*, which is the name of the file we recommend that you upload.

### Response

```
{
    "uploadKey": "<YOUR_UPLOAD_KEY>",
    "uploadExpiration": "2022-04-08T00:00:00Z",
    "urlExpiration": "2022-04-06T17:59:46Z",
    "urls": ["<SIGNED_UPLOAD_URL>"],
    "location": "https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<YOUR_OBJECT_KEY>"
}

```

- Note down the values returned for `uploadKey` <YOUR_UPLOAD_KEY> and `urls` <SIGNED_UPLOAD_URL>. You will use these values in subsequent requests.

## [Step 7 - Upload the First Part file](#step-7-upload-the-first-part-file)

1. Download the file *blade_main.ipt* file from <https://github.com/autodesk-platform-services/aps-tutorial-postman/tree/master/ModelDerivative_03/walkthrough_data/Components>.
2. Send a request to upload the file to the Bucket.

### Request

```
curl -X PUT \
    '<SIGNED_UPLOAD_URL>'\
    --data-binary '@<PATH_TO_YOUR_FILE_TO_UPLOAD>'

```

## [Step 8 - Finalize Upload](#step-8-finalize-upload)

To make the uploaded file available for download, you must finalize the upload. To complete the upload:

### Request

```
curl -X POST \
    'https://developer.api.autodesk.com/oss/v2/buckets/ossBucketKey/objects/ossSourceFileObjectKey/signeds3upload' \
    -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
    -H 'Content-Type: application/json' \
    -d '{
        "ossbucketKey": "<YOUR_BUCKET_KEY>",
        "ossSourceFileObjectKey": "<YOUR_OBJECT_KEY>",
        "access": "full",
        "uploadKey": "<YOUR_UPLOAD_KEY>"
        }'

```

Show More

### Response

```
{
    "bucketKey": "<YOUR_BUCKET_KEY>",
    "objectId": "<YOUR_OBJECT_ID>",
    "objectKey": "<YOUR_OBJECT_KEY>",
    "size": "246272",
    "contentType": "application/octet-stream",
    "location": "https://developer.api.autodesk.com/oss/v2/buckets/bucketKey/objects/inputfile",
    "permissions": [
        {
            "authId": "<YOUR_ACCESS_TOKEN>",
            "access": "full"
        }
    ],
    "policyKey": "transient"
}

```

Show More

- Note down the value of the `objectId` parameter of the Part file. This is the URN of the Part file. You will need the URNs of all 3 Part files for the next task.

## [Step 9 - Obtain Signed URL for Second Part File](#step-9-obtain-signed-url-for-second-part-file)

To upload a file to an OSS bucket, you need to have a signed upload URL. To obtain a signed URL:

### Request

```
curl -X GET \
    'https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<YOUR_OBJECT_KEY>/signeds3upload?minutesExpiration=<LIFESPAN_OF_URL>' \
    -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
    -H 'Content-Type: application/json'

```

**Notes:**

- Replace <YOUR_ACCESS_TOKEN> with the access token you obtained in Task 1.
- Replace <LIFESPAN_OF_URL> with 10. This will ensure that the signed URL that is returned will be valid for 10 minutes.
- Replace <YOUR_OBJECT_KEY> with *blade_top.ipt*, which is the name of the file we recommend that you upload.

### Response

```
{
    "uploadKey": "<YOUR_UPLOAD_KEY>",
    "uploadExpiration": "2022-04-08T00:00:00Z",
    "urlExpiration": "2022-04-06T17:59:46Z",
    "urls": ["<SIGNED_UPLOAD_URL>"],
    "location": "https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<YOUR_OBJECT_KEY>"
}

```

- Note down the values returned for `uploadKey` <YOUR_UPLOAD_KEY> and `urls` <SIGNED_UPLOAD_URL>. You will use these values in subsequent requests.

## [Step 10 - Upload the Second Part file](#step-10-upload-the-second-part-file)

1. Download the file *blade_top.ipt* file from <https://github.com/autodesk-platform-services/aps-tutorial-postman/tree/master/ModelDerivative_03/walkthrough_data/Components>.
2. Send a request to upload the file to the Bucket.

### Request

```
curl -X PUT \
    '<SIGNED_UPLOAD_URL>'\
    --data-binary '@<PATH_TO_YOUR_FILE_TO_UPLOAD>'

```

## [Step 11 - Finalize Upload](#step-11-finalize-upload)

To make the uploaded file available for download, you must finalize the upload. To complete the upload:

### Request

```
curl -X POST \
    'https://developer.api.autodesk.com/oss/v2/buckets/ossBucketKey/objects/ossSourceFileObjectKey/signeds3upload' \
    -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
    -H 'Content-Type: application/json' \
    -d '{
        "ossbucketKey": "<YOUR_BUCKET_KEY>",
        "ossSourceFileObjectKey": "<YOUR_OBJECT_KEY>",
        "access": "full",
        "uploadKey": "<YOUR_UPLOAD_KEY>"
        }'

```

Show More

### Response

```
{
    "bucketKey": "<YOUR_BUCKET_KEY>",
    "objectId": "<YOUR_OBJECT_ID>",
    "objectKey": "<YOUR_OBJECT_KEY>",
    "size": "227840",
    "contentType": "application/octet-stream",
    "location": "https://developer.api.autodesk.com/oss/v2/buckets/bucketKey/objects/inputfile",
    "permissions": [
        {
            "authId": "<YOUR_ACCESS_TOKEN>",
            "access": "full"
        }
    ],
    "policyKey": "transient"
}

```

Show More

- Note down the value of the `objectId` parameter of the Part file. This is the URN of the Part file. You will need the URNs of all 3 Part files for the next task.

## [Step 12 - Obtain Signed URL for Third Part File](#step-12-obtain-signed-url-for-third-part-file)

To upload a file to an OSS bucket, you need to have a signed upload URL. To obtain a signed URL:

### Request

```
curl -X GET \
    'https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<YOUR_OBJECT_KEY>/signeds3upload?minutesExpiration=<LIFESPAN_OF_URL>' \
    -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
    -H 'Content-Type: application/json'

```

**Notes:**

- Replace <YOUR_ACCESS_TOKEN> with the access token you obtained in Task 1.
- Replace <LIFESPAN_OF_URL> with 10. This will ensure that the signed URL that is returned will be valid for 10 minutes.
- Replace <YOUR_OBJECT_KEY> with *scissor_spring.ipt*, which is the name of the file we recommend that you upload.

### Response

```
{
    "uploadKey": "<YOUR_UPLOAD_KEY>",
    "uploadExpiration": "2022-04-08T00:00:00Z",
    "urlExpiration": "2022-04-06T17:59:46Z",
    "urls": ["<SIGNED_UPLOAD_URL>"],
    "location": "https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<YOUR_OBJECT_KEY>"
}

```

- Note down the values returned for `uploadKey` <YOUR_UPLOAD_KEY> and `urls` <SIGNED_UPLOAD_URL>. You will use these values in subsequent requests.

## [Step 13 - Upload the Third Part file](#step-13-upload-the-third-part-file)

1. Download the file *scissor_spring.ipt* file from <https://github.com/autodesk-platform-services/aps-tutorial-postman/tree/master/ModelDerivative_03/walkthrough_data/Components>.
2. Send a request to upload the file to the Bucket.

### Request

```
curl -X PUT \
    '<SIGNED_UPLOAD_URL>'\
    --data-binary '@<PATH_TO_YOUR_FILE_TO_UPLOAD>'

```

## [Step 14 - Finalize Upload](#step-14-finalize-upload)

To make the uploaded file available for download, you must finalize the upload. To complete the upload:

### Request

```
curl -X POST \
    'https://developer.api.autodesk.com/oss/v2/buckets/ossBucketKey/objects/ossSourceFileObjectKey/signeds3upload' \
    -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
    -H 'Content-Type: application/json' \
    -d '{
        "ossbucketKey": "<YOUR_BUCKET_KEY>",
        "ossSourceFileObjectKey": "<YOUR_OBJECT_KEY>",
        "access": "full",
        "uploadKey": "<YOUR_UPLOAD_KEY>"
        }'

```

Show More

### Response

```
{
    "bucketKey": "<YOUR_BUCKET_KEY>",
    "objectId": "<YOUR_OBJECT_ID>",
    "objectKey": "<YOUR_OBJECT_KEY>",
    "size": "154624",
    "contentType": "application/octet-stream",
    "location": "https://developer.api.autodesk.com/oss/v2/buckets/bucketKey/objects/inputfile",
    "permissions": [
        {
            "authId": "<YOUR_ACCESS_TOKEN>",
            "access": "full"
                        }
                    ],
                    "policyKey": "transient"
                }

```

Show More

- Note down the value of the `objectId` parameter of the Part file. This is the URN of the Part file. You will need the URNs of all 3 Part files for the next task.
