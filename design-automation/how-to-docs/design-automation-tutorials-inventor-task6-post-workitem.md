# Task 6 â Submit a WorkItem

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/inventor/task6-post-workitem/

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

## Step 1 - Create a WorkItem

To create a WorkItem to execute the Activity ChangeParamActivity:

### Request

```
curl - X POST \ 'https://developer.api.autodesk.com/da/us-east/v3/workitems' \ - H 'Content-Type: application/json' \ - H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \ - d '{ "activityId": "<YOUR_APP_NICKNAME>.ChangeParamActivity+my_current_version", "arguments": { "InventorDoc": { "url": "urn:adsk.objects:os.object:<YOUR_BUCKET_KEY>/<OBJECT_KEY_4_INPUT_FILE>", "verb": "get", "headers": { "Authorization": "Bearer <YOUR_ACCESS_TOKEN>" } }, "InventorParams": { "url": "data:application/json,{ \" height \" : \" 16 in \" , \" width \" : \" 10 in \" }" }, "OutputIpt": { "url": "urn:adsk.objects:os.object:<YOUR_BUCKET_KEY>/<RESIZED_IPT_FILENAME>", "verb": "put", "headers": { "Authorization": "Bearer <YOUR_ACCESS_TOKEN>" } }, "OutputBmp": { "url": "urn:adsk.objects:os.object:<YOUR_BUCKET_KEY>/<GENERATED_BMP_FILENAME>", "verb": "put", "headers": { "Authorization": "Bearer <YOUR_ACCESS_TOKEN>" } } } }'
```

Note

The response contains the id of the posted WorkItem:

```
{ "status" : "pending" , "stats" : { "timeQueued" : "2023-09-27T08:52:30.7161306Z" }, "id" : "<YOUR_WORKITEM_ID>" }
```

## Step 2 - Check status of the WorkItem

WorkItems are queued before they are processed.
A WorkItemâs processing time will vary depending on the size and complexity of the input files, the type of processing done by the AppBundle, and the size of the output files.

In this walkthrough, you will be checking the WorkItem status to see if it has completed.
However, the best practice is to use the onComplete argument when submitting a WorkItem.
The onComplete argument lets you specify a callback URL, which will be called once the WorkItem is completed.
For more information see the documentation on callbacks here .

You can check the status of a WorkItem by calling [GET] /workitems/{id} :

### Request

```
curl - X GET \ 'https://developer.api.autodesk.com/da/us-east/v3/workitems/<YOUR_WORKITEM_ID> \ -H ' Content - Type : application / json ' \ -H ' Authorization : Bearer < YOUR_ACCESS_TOKEN > '
```

### Response

```
{ "status" : "success" , "reportUrl" : "https://dasprod-store.s3.amazonaws.com/workItem/<YOUR_APP_NICKNAME>/<YOUR_WORKITEM_ID>/report.txt?..(Truncated)" , "stats" : { "timeQueued" : "2023-09-27T08:52:30.7161306Z" , "timeDownloadStarted" : "2023-09-27T08:52:30.882113Z" , "timeInstructionsStarted" : "2023-09-27T08:52:31.6418619Z" , "timeInstructionsEnded" : "2023-09-27T08:52:55.0320553Z" , "timeUploadEnded" : "2023-09-27T08:52:55.4675607Z" , "timeFinished" : "2023-09-27T08:52:55.9182974Z" , "bytesDownloaded" : 134691 , "bytesUploaded" : 360182 }, "id" : "<YOUR_WORKITEM_ID>" }
```

Attribute Description status Indicates if execution is pending, successful, failed or cancelled. reportUrl The URL to get the report log for this WorkItemâs execution.
