# Task 7 - Download the Results

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/inventor/task7-download-results/

---

# Task 7 - Download the Results

After you submit a WorkItem, you must wait for it to complete and download the results.

By the end of this task, you will be able to:
> - Obtain a signed URL to download files from OSS.
> - Download the results to your local machine.

You will use the following operation in this task:

| HTTP Request | Description |
| --- | --- |
| [GET /buckets/{bucketKey}/objects/{objectKey}/signeds3download](../../data/http-docs/http-buckets--bucketKey-objects--objectKey-signeds3download-GET.md) | Creates a signed URL to an object in an OSS bucket. |

## [Step 1 - Get a S3 download URL for resized IPT file](#step-1-get-a-s3-download-url-for-resized-ipt-file)

### Request

```
curl -X GET \
      'https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<RESIZED_IPT_FILENAME>/signeds3download'
      - H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
      - H 'Content-Type: application/json'

```

### Response

```
{
    "status": "complete",
    "url": "<SIGNED_URL_TO_RESIZED_IPT_FILE>",
    "params": {
        "content-type": "application/octet-stream",
        "content-disposition": "attachment; filename*=utf-8''ResultSmall.ipt; filename=ResultSmall.ipt; creation-date=\"Wed, 27 Sep 2023 08:52:52 GMT\"; modification-date=\"Wed, 27 Sep 2023 08:52:52 GMT\"; read-date=\"Wed, 27 Sep 2023 08:52:52 GMT\"; size=240128"
    },
    "size": 240128,
    "sha1": "064db8ddbfc3779335518f496ca232b140783201"
}

```

Show More

| Attribute | Description |
| --- | --- |
| `url` | The signed S3 URL to download the *.ipt* file. |

## [Step 2 - Download resized IPT file from OSS](#step-2-download-resized-ipt-file-from-oss)

Now that your WorkItem has finished successfully, the resulting IPT file should have been uploaded to OSS.
You can now use the Data Management API to download it to your local machine.

### Request

```
curl -X GET \
    '<SIGNED_URL_TO_RESIZED_IPT_FILE>' \
    -o 'SOME/PATH/ON/YOUR/COMPUTER/ResultSmall.ipt'

```

**Note:** This download is directly from S3 (or a CDN). So, it doesnât need an `Authorization` header.

### Response

The file should download to your local machine.

## [Step 3 - Get a download URL for BMP file](#step-3-get-a-download-url-for-bmp-file)

### Request

```
curl -X POST \
      'https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<GENERATED_BMP_FILENAME>/signeds3download'
      - H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
      - H 'Content-Type: application/json'

```

### Response

```
{
    "status": "complete",
    "url": "<SIGNED_URL_TO_GENERATED_BMP_FILE>",
    "params": {
        "content-type": "image/bmp",
        "content-disposition": "attachment; filename*=utf-8''ResultSmall.bmp; filename=ResultSmall.bmp; creation-date=\"Wed, 27 Sep 2023 08:52:52 GMT\"; modification-date=\"Wed, 27 Sep 2023 08:52:52 GMT\"; read-date=\"Wed, 27 Sep 2023 08:52:52 GMT\"; size=120054"
    },
    "size": 120054,
    "sha1": "f1d0315b84657702f928b265f3c474d11b52fad7"
}

```

Show More

## [Step 4 - Download generated BMP file from OSS](#step-4-download-generated-bmp-file-from-oss)

### Request

```
curl -X GET \
    '<SIGNED_URL_TO_GENERATED_BMP_FILE>' \
    -o 'SOME/PATH/ON/YOUR/COMPUTER/ResultSmall.bmp'

```

**Note:** This download is directly from S3 (or a CDN). So, it doesnât need an `Authorization` header.

### Response

The file should download to your local machine.
