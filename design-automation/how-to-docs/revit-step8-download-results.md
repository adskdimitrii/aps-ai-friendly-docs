# Task 8 - Download the Results

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/revit/step8-download-results/

---

# Task 8 - Download the Results

After you submit a WorkItem, you must wait for it to complete and download the results.

By the end of this task, you will be able to:
> - Obtain a signed URL to download files from OSS.
> - Download the results to your local machine.

You will use the following operation in this task:

| HTTP Request | Description |
| --- | --- |
| [GET /buckets/{bucketKey}/objects/{objectKey}/signeds3download](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3download-GET/) | Creates a signed URL to an object in an OSS bucket. |

## [Step 1 - Get a S3 download URL for resulting RVT file](#step-1-get-a-s3-download-url-for-resulting-rvt-file)

### Request

```
curl -X GET \
      'https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<RESULT_FILE_OBJECT_KEY>/signeds3download'
      - H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
      - H 'Content-Type: application/json'

```

### Response

```
{
    "status": "complete",
    "url": "<SIGNED_URL_TO_RESULT_FILE>",
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
| `url` | The signed S3 URL to download the *.rvt* file. |

## [Step 2 - Download resulting RVT file from OSS](#step-2-download-resulting-rvt-file-from-oss)

Now that your WorkItem has finished successfully, the resulting text file should have been uploaded to OSS.
You can now use the Data Management API to download it to your local machine.

### Request

```
curl -X GET \
    '<SIGNED_URL_TO_RESULT_FILE>' \
    -o 'SOME/PATH/ON/YOUR/COMPUTER/result.rvt'

```

**Note:** This download is directly from S3 (or a CDN). So, it doesnât need an `Authorization` header.

### Response

The file should download to your local machine.
