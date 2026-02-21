# Task 5 â Submit a WorkItem

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/fusion/task5-post-workitem/

---

# Task 5 â Submit a WorkItem

When you post a WorkItem to the Automation Service, you are instructing the service to execute an Activity.

The relationship between an Activity and a WorkItem can be thought of as the relationship between a âfunction definitionâ and âfunction callâ.
Named parameters of the Activity have corresponding named arguments of the WorkItem.
Like in function calls, optional parameters of the Activity can be skipped and left unspecified while posting a WorkItem.

By the end of this task, you will be able to:
> - Create a WorkItem to execute an Activity.
> - Check if execution succeeded or failed.
> - Get the URL to the execution log file.

You will use the following operations to work with WorkItems in this task:

| HTTP Request | Description |
| --- | --- |
| [POST /workitems](/en/docs/design-automation/v3/reference/http/workitems-POST) | Creates a new WorkItem and queues it for processing. |
| [GET /workitems/{id}](/en/docs/design-automation/v3/reference/http/workitems-id-GET) | Gets the status of a specific WorkItem. |

## [Step 1 - Generate a Personal Access Token](#step-1-generate-a-personal-access-token)

To get a personal access token (PAT), simply access your autodesk profile via the following link: <https://profile.autodesk.com/security> and follow the instructions. Generate a PAT for product scope âFusion Automation APIâ or âProject Alpineâ. Either product scope will work.

The table below describes the different options for authentication and authorization for submitting Fusion WorkItems to the Automation Service.

| Option | OAuth Type | Required Body Content | Notes | Use Case |
| --- | --- | --- | --- | --- |
| Submit for your activity on behalf of yourself as Fusion user | 2LO | PAT of Fusion user | The owner of the app of the 2LO token must be same as the user that has created the PAT. | Access is needed for a âservice userâsâ data that is aggregated from customers into one account |
| Submit for your activity on behalf of a different Fusion user | 3LO | PAT of Fusion user + Signed Activity ID | 3LO token must be for the same user as the PAT | Access is needed for direct customer data that logs in and allows it |

## [Step 2 - Create a WorkItem](#step-2-create-a-workitem)

To create a WorkItem to execute the Activity ConfigureDesignActivity:

### Request
> ```
> curl -X POST \
> 'https://developer.api.autodesk.com/da/us-east/v3/workitems' \
> -H 'Content-Type: application/json' \
> -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
> -d '{
> "activityId": "<YOUR_NICKNAME>.ConfigureDesignActivity+my_current_version", \
> "arguments": {
> "PersonalAccessToken": "<YOUR_PERSONAL_ACCESSTOKEN>",
> "TaskParameters": "{\n  \"fileURN\": \"urn:adsk.wipprod:dm.lineage:shuH8zKvThW_4Tdu-m22sw\",\n  \"parameters\": {\n    \"d3\": \"40mm\"\n  }\n}"
> }
> }'
>
> ```
>
>
> Show More

**Note**
> | Attribute | Description |
> | --- | --- |
> | `activityId` | The fully qualified id of the activity (owner.activity+alias) this WorkItem will execute. |
> | `arguments` | Contains all the parameters that need to be passed to the Activity specified by activityId. They must match the parameters you specified in Task 5, when you created the Activity. In this case we send over the PAT so DA4Fusion can access files on Fusion teams, aswell as âd3â: â40mmâ as in a map of parameters to change the height of the nut to 40mm, additonal to the fileURN of the design we want to change. |
>
> The response contains the `id` of the posted WorkItem:
>
> ```
> {
> "status": "pending",
> "stats": {
> "timeQueued": "2023-09-27T08:52:30.7161306Z"
> },
> "id": "<YOUR_WORKITEM_ID>"
> }
>
> ```

## [Step 3 - Check status of the WorkItem](#step-3-check-status-of-the-workitem)

WorkItems are queued before they are processed.
A WorkItemâs processing time will vary depending on the size and complexity of the input files, the type of processing done by the AppBundle, and the size of the output files.

In this walkthrough, you will be checking the WorkItem status to see if it has completed.
However, the best practice is to use the `onComplete` argument when submitting a WorkItem.
The onComplete argument lets you specify a callback URL, which will be called once the WorkItem is completed.
For more information see the documentation on callbacks [here](/en/docs/design-automation/v3/developers_guide/callbacks/).

You can check the status of a WorkItem by calling `[GET] /workitems/{id}`:

### Request

```
curl -X GET \
  'https://developer.api.autodesk.com/da/us-east/v3/workitems/<YOUR_WORKITEM_ID> \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

```

### Response

```
{
    "status": "success",
    "reportUrl": "https://dasprod-store.s3.amazonaws.com/workItem/<YOUR_NICKNAME>/<YOUR_WORKITEM_ID>/report.txt?..(Truncated)",
    "stats": {
        "timeQueued": "2023-09-27T08:52:30.7161306Z",
        "timeDownloadStarted": "2023-09-27T08:52:30.882113Z",
        "timeInstructionsStarted": "2023-09-27T08:52:31.6418619Z",
        "timeInstructionsEnded": "2023-09-27T08:52:55.0320553Z",
        "timeUploadEnded": "2023-09-27T08:52:55.4675607Z",
        "timeFinished": "2023-09-27T08:52:55.9182974Z",
        "bytesDownloaded": 134691,
        "bytesUploaded": 360182
    },
    "id": "<YOUR_WORKITEM_ID>"
}

```

Show More

| Attribute | Description |
| --- | --- |
| `status` | Indicates if execution is pending, successful, failed or cancelled. |
| `reportUrl` | The URL to get the report log for this WorkItemâs execution. |
