# Task 6 â Submit a WorkItem

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/autocad/task6-post-workitem/

---

# Task 6 â Submit a WorkItem

When you post a WorkItem to the Automation Service, you are instructing the service to execute an Activity.

The relationship between an Activity and a WorkItem can be thought of as the relationship between a âfunction definitionâ and âfunction callâ.
Named parameters of the Activity have corresponding named arguments of the WorkItem.
Like in function calls, optional parameters of the Activity can be skipped and left unspecified while posting a WorkItem.

By the end of this task, you will be able to:

- Create a WorkItem to execute an Activity.

- Check if execution succeeded or failed.

- Get the URL to the execution log file.

You will use the following operations to work with WorkItems in this task:

HTTP Request Description POST /workitems Creates a new WorkItem and queues it for processing. GET /workitems/{id} Gets the status of a specific WorkItem.

## Step 1 - Send a WorkItem

To create a WorkItem to execute the Activity ListLayersActivity:

### Request

```
curl - X POST \ 'https://developer.api.autodesk.com/da/us-east/v3/workitems' \ - H 'Content-Type: application/json' \ - H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \ - d '{ "activityId": "<YOUR_APP_NICKNAME>.ListLayersActivity+my_current_version", "arguments": { "InputDwg": { "url": "urn:adsk.objects:os.object:<YOUR_BUCKET_KEY>/<OBJECT_KEY_4_INPUT_FILE>", "verb": "get", "headers": { "Authorization": "Bearer <YOUR_ACCESS_TOKEN>" } }, "result": { "url": "urn:adsk.objects:os.object:<YOUR_BUCKET_KEY>/<OBJECT_KEY_4_OUTPUT_FILE>", "verb": "put", "headers": { "Authorization": "Bearer <YOUR_ACCESS_TOKEN>" } } } }'
```

Note

Attribute Description activityId The target Activity defined by âowner.activity+aliasâ this WorkItem will execute. arguments The argument list that is required by the Activity ( ListLayersActivity ): - InputDwg - Details of the input file that must be downloaded from OSS and then processed by the WorkItem. - result - Details of the output that must be âputâ (uploaded) to OSS.

The response contains the id of the posted WorkItem:

### Response

```
{ "status" : "pending" , "stats" : { "timeQueued" : "2019-10-17T11:21:50.5619735Z" }, "id" : "<YOUR_WORKITEM_ID>" }
```

## Step 2 - Check status of a WorkItem

WorkItems are queued before they are processed.
A WorkItemâs processing time will vary depending on the size and complexity of the input files, the type of processing done by the AppBundle, and the size of the output files.

In this walkthrough, you will be checking the WorkItem status to see if it has completed.
However, the best practice is to use the onComplete argument when submitting a WorkItem.
The onComplete argument enables you to specify a callback URL, which will be called once the WorkItem is completed.
For more information see the documentation on callbacks here .

You can check the status of a WorkItem by calling `GET /v3/workitems/{id}`_ :

### Request

```
curl - X GET \ https : // developer . api . autodesk . com / da / us - east / v3 / workitems /< YOUR_WORKITEM_ID > \ - H 'Content-Type: application/json' \ - H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'
```

### Response

```
{ "status" : "success" , "reportUrl" : "https://dasprod-store.s3.amazonaws.com/workItem/<YOUR_APP_NICKNAME>/2ea96495c..{Truncated}" , "stats" : { "timeQueued" : "2019-10-17T11:21:50.5619735Z" , "timeDownloadStarted" : "2019-10-17T11:21:42.5827646Z" , "timeInstructionsStarted" : "2019-10-17T11:21:43.3796462Z" , "timeInstructionsEnded" : "2019-10-17T11:21:45.3952874Z" , "timeUploadEnded" : "2019-10-17T11:21:45.5515369Z" , "timeFinished" : "2019-10-17T11:21:54.1463701Z" , "bytesDownloaded" : 88612 , "bytesUploaded" : 1115 }, "id" : "2ea96495c30d432b84797d7e71262772" }
```

Attribute Description status Indicates if execution is pending, successful, failed or cancelled. reportUrl The URL to get the report log for this WorkItemâs execution.
