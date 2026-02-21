# Task 7 - Download the Results

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/autocad/task7-download-results/

---

# Task 7 - Download the Results

After you submit a WorkItem, you must wait for it to complete and download the results.

By the end of this task, you will be able to:

- Generate a signed URL to an object in OSS.

- Download the results to your local machine.

You will use the following operation in this task:

HTTP Request Description POST /buckets/{bucketKey}/objects/{objectKey}/signed Creates a signed URL to an object in an OSS bucket.

## Step 1 - Get a temporary download URL for the result

When the WorkItem in Task 6 was executed, it saved the resulting text file to OSS. You will now get a download URL for that text file.

### Request

```
curl - X POST \ 'https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<OBJECT_KEY_4_OUTPUT_FILE>/signeds3download' - H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \ - H 'Content-Type: application/json'
```

### Response

```
{ "status" : "complete" , "url" : "<SIGNED_DOWNLOAD_URL>" , "params" : { "content-type" : "text/plain" , "content-disposition" : "attachment; filename*=utf-8''layers.txt; filename=layers.txt; creation-date=\"Thu, 05 Oct 2023 03:54:44 GMT\"; modification-date=\"Thu, 05 Oct 2023 03:54:45 GMT\"; read-date=\"Thu, 05 Oct 2023 03:54:45 GMT\"; size=1115" }, "size" : 1115 , "sha1" : "5aa76cb94069146a31b6747f4b212a03aae9ed86" }
```

## Step 2 - Download output from OSS

### Request

```
curl - X GET \ '<SIGNED_URL_TO_OUTPUT_TEXT_FILE>' \ - H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' , \ - H 'Content-Type: application/json' , - o 'SOME/PATH/ON/YOUR/COMPUTER/Result.txt'
```

### Response

The file should download to your local machine.
