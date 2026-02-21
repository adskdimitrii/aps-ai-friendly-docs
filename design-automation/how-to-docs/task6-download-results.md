# Task 6 - Download the Results

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/3dsmax/task6-download-results/

---

# Task 6 - Download the Results

After you submit a WorkItem, you must wait for it to complete and download the results.

By the end of this task, you will be able to:

- Check the execution status of the WorkItem.

- Download the results to your local machine.

You will use the following operations to check the WorkItemâs status and download the result.

HTTP Request Description GET /workitems/{id} Gets the status of a specific WorkItem. POST /buckets/{bucketKey}/objects/{objectKey}/signed Creates a signed URL to an object in an OSS bucket.

## Step 1 - Check status of the WorkItem

The time to complete a WorkItem mostly depends on what is executed by the WorkItem.
However, execution time may be longer when the Automation Service experiences heavy traffic.

In this walkthrough, you will be waiting for the WorkItem to finish by querying the WorkItem status.
However, the best practice is to use the onComplete argument when submitting WorkItem.
This onComplete argument enables you tp specify a callback URL that will be called once the WorkItem is completed.
The onComplete argument can be specified when sending a WorkItem and doesnât need to be defined within an activity.
For more information see the documentation on callbacks here .

For now, send this request periodically until the value of the response body parameter status is something other than pending or inprogress .
If everything goes as expected, the status should reach the success status. Otherwise, you might see one of the many potential failure statuses.
If you end up with a failure status, you can download the report file by using the url contained in the response body parameter reportUrl to help you diagnose what might have gone wrong.

### Request

```
curl - i - X GET \ https : // developer . api . autodesk . com / da / us - east / v3 / workitems /< YOUR_WORKITEM_ID > \ - H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \ - H 'Content-Type: application/json' \ - H 'cache-control: no-cache'
```

Notes:

- Replace the <YOUR_WORKITEM_ID> value in the url with the id of your WorkItem obtained from Task 5 .

### Response

```
{ "status" : "success" , "reportUrl" : "Some temporary url to download your report file" , "stats" : { "timeQueued" : "2019-06-19T19:29:19.2116634Z" , "timeDownloadStarted" : "2019-06-19T19:29:19.8867532Z" , "timeInstructionsStarted" : "2019-06-19T19:29:20.1055176Z" , "timeInstructionsEnded" : "2019-06-19T19:29:42.4372923Z" , "timeUploadEnded" : "2019-06-19T19:29:42.7341647Z" , "timeFinished" : "2019-06-19T19:29:42.892238Z" , "bytesDownloaded" : 56546 , "bytesUploaded" : 97471 }, "id" : "c19fd1a1236541bea1235fae6dcd281b" }
```

## Step 2 - Get S3 download URL for output

Now that your WorkItem has finished successfully, the resulting zip file should have been uploaded to OSS.
You can now use the Data Management API to download it to our local machine.

### Request

```
curl - X POST \ 'https://developer.api.autodesk.com/oss/v2/buckets/<YOUR_BUCKET_KEY>/objects/<OBJECT_KEY_4_OUTPUT_FILE>/signeds3download' - H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \ - H 'Content-Type: application/json'
```

### Response

```
{ "status" : "complete" , "url" : "<SIGNED_DOWNLOAD_URL>" , "params" : { "content-type" : "application/zip" , "content-disposition" : "attachment; filename*=utf-8''workingFolder.zip; filename=workingFolder.zip; creation-date=\"Thu, 05 Oct 2023 03:54:44 GMT\"; modification-date=\"Thu, 05 Oct 2023 03:54:45 GMT\"; read-date=\"Thu, 05 Oct 2023 03:54:45 GMT\"; size=76917" }, "size" : 76917 , "sha1" : "ff038df8fcbbcb5547e9fcdebea9e2d0a2babfd2" }
```

Attribute Description url The signed S3 URL to download the .zip file.

## Step 3 - Download resulting zip file from OSS

### Request

```
curl - X GET \ '<SIGNED_DOWNLOAD_URL>' \ - o 'SOME/PATH/ON/YOUR/COMPUTER/workingFolder.zip'
```

Note: This download is directly from S3 (or a CDN). So, it doesnât need an Authorization header.

### Response

The file should download to your local machine.
