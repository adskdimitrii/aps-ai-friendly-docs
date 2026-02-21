# workitems/status

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/workitems-status-POST/

---

POST

# workitems/status

Get WorkItem status for an array of WorkItem Ids.

Limits:

1. Retention period (LimitWorkItemRetentionPeriod). WorkItem status is retained for **3 days** after the WorkItem completes.
2. Maximum number of WorkItem Ids in the request is **50**.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/da/us-east/v3/workitems/status |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `code:all` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](/en/docs/oauth/v2/tutorials/get-2-legged-token) or [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |

* Required

### Request

## [Body Structure](#body-structure)

| ids*   array: object | Array of WorkItem Ids. |
| --- | --- |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully get the status for the array of WorkItem Ids. |
| --- | --- |
| 400   BadRequest | The request is invalid. |

### Response

## [Body Structure (200)](#body-structure-200)

| results   array: object | Array of WorkItem status. |
| --- | --- |
| errors   map: object | Map of errors for WorkItem ids faling to get status. |

## [Example](#example)

Successfully get the status of a WorkItem.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/workitems/status' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '[
        "03d65402faeb4409ac672f341462f689",
        "032a3a8e25b3409584194e7221a40059",
        "1230059b3409584194e7221230059000",
        "02d6d69106b14946b319ab68d68cc04f"
      ]'

```

Show More

### Response

```
 {
  "results": [
      {
          "status": "success",
          "reportUrl": "https://dasprod-store.s3.amazonaws.com/workItem/mynickname/03d65402faeb4409ac672f341462f689/report.txt",
          "activityId": "mynickname.myApp1+prod",
          "stats": {
              "timeQueued": "2024-03-06T03:11:09.1510699Z",
              "timeDownloadStarted": "2024-03-06T03:11:09.2898279Z",
              "timeInstructionsStarted": "2024-03-06T03:11:09.4473947Z",
              "timeInstructionsEnded": "2024-03-06T03:11:12.9289128Z",
              "timeUploadEnded": "2024-03-06T03:11:12.9633762Z",
              "timeFinished": "2024-03-06T03:11:13.3608607Z",
              "bytesDownloaded": 87040,
              "bytesUploaded": 3
          },
          "id": "03d65402faeb4409ac672f341462f689"
      },
      {
          "status": "success",
          "reportUrl": "https://dasprod-store.s3.amazonaws.com/workItem/mynickname/02d6d69106b14946b319ab68d68cc04f/report.txt",
          "activityId": "mynickname.myApp1+prod",
          "stats": {
              "timeQueued": "2024-03-06T04:07:34.6920266Z",
              "timeDownloadStarted": "2024-03-06T04:07:36.0231791Z",
              "timeInstructionsStarted": "2024-03-06T04:07:39.9518961Z",
              "timeInstructionsEnded": "2024-03-06T04:08:15.9285096Z",
              "timeUploadEnded": "2024-03-06T04:08:16.1572555Z",
              "timeFinished": "2024-03-06T04:08:17.0213784Z",
              "bytesDownloaded": 113,
              "bytesUploaded": 352256
          },
          "id": "02d6d69106b14946b319ab68d68cc04f"
      }
  ],
  "errors": {
      "032a3a8e25b3409584194e7221a40059": "Not found",
      "1230059b3409584194e7221230059000": "Not found"
  }
}

```

Show More
