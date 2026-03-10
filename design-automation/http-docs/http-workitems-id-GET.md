# workitems/:id

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/workitems-id-GET/

---

GET

# workitems/:id

Gets the status of a specific WorkItem.

Typically used to ‘poll’ for the completion of a WorkItem, but see the use of the ‘onComplete’ argument for
an alternative that does not require ‘polling’.

Limits:

1. Retention period (LimitWorkItemRetentionPeriod). WorkItem status is retained for **3 days** after the WorkItem completes.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/da/us-east/v3/workitems/:id |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `code:all` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| id   string | The GUID used to identify the WorkItem. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully get the status of a WorkItem. |
| --- | --- |
| 403   Forbidden | The user is not authorized to get the WorkItem status. |
| 404   Not Found | The WorkItem status doesn’t exist. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| status   enum:string | Status value of a WorkItem. Possible values: `pending`, `inprogress`, `cancelled`, `failedLimitProcessingTime`, `failedDownload`, `failedInstructions`, `failedUpload`, `failedUploadOptional`, `success` |
| --- | --- |
| progress   string | The current status of the workitem. |
| reportUrl   string | The detailed report about the workitem, report url is valid for 24 hours from first receiving it. |
| stats   object | Basic statistics about workitem processing. |
| timeQueued   datetime: ISO 8601 | The time in UTC when the workitem was queued. |
| timeDownloadStarted   datetime: ISO 8601 | The time in UTC when the system started processing the workitem by transferring input data to the processing node. |
| timeInstructionsStarted   datetime: ISO 8601 | The time in UTC when the system finished downloading input and started processing instructions from the Activity associated with this workitem. |
| timeInstructionsEnded   datetime: ISO 8601 | The time in UTC when the system finished executing instructions and started uploading outputs. |
| timeUploadEnded   datetime: ISO 8601 | The time in UTC when the system finished uploading outputs. |
| timeFinished   datetime: ISO 8601 | The time in UTC when the system finished the workitem and reported the status. |
| bytesDownloaded   int | The file size of bytes the job downloads for input. |
| bytesUploaded   int | The file size of bytes the job uploads for output. |
| id   string |  |
| activityId   string | The activityId the WorkItem posted for. |

## [Example](#example)

Successfully get the status of a WorkItem.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/workitems/:id' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "status": "success",
  "reportUrl": "https://dasprod-store.s3.amazonaws.com/workItem/Revit/wi1234/report.txt?xxxxxxx",
  "stats": {
      "timeQueued": "2022-12-16T05:04:46.8214232Z",
      "timeDownloadStarted": "2022-12-16T05:04:46.994739Z",
      "timeInstructionsStarted": "2022-12-16T05:04:47.7968341Z",
      "timeInstructionsEnded": "2022-12-16T05:04:48.189266Z",
      "timeFinished": "2022-12-16T05:04:48.7960863Z",
      "bytesDownloaded": 169,
      "bytesDownloaded": 2000
  },
  "id": "wi1234",
  "activityId": "mynickname.myactivity+prod"
}

```

Show More
