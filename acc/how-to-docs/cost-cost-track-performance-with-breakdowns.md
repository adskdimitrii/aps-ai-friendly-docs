# Track Budget Performance with Breakdowns

Source: https://aps.autodesk.com/en/docs/acc/tutorials/cost/cost-track-performance-with-breakdowns/

---

# Track Budget Performance with Breakdowns

This tutorial demonstrates how to use the Cost Management API to track the performance of a project budget with breakdowns using timesheets. A performance tracking item (which represents a budget) is tracked by one or more timesheets, each associated with one of the tracking itemâs instances. The tutorial breaks out the tracking data to track each of the timesheets associated with a given budget. The steps include retrieving a tracking item instance, logging and aggregating the instanceâs timesheets, synchronizing the timesheets with Autodesk Cost Management, and adjusting the forecast.

Note that the Cost API timesheets endpoints used in this tutorial are designed only for use with a third party timesheet reporting (tracking) app (e.g. Riskcast, Rhumbix, QuickBooks Time, or ClickUp) that youâve integrated with Cost Management.

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps).
- Acquire a [3-legged OAuth token](/en/docs/oauth/v2/tutorials/get-3-legged-token/) with `data:create`, `data:read`, and `data:write` scopes.
- Verify that you have access to the relevant BIM 360 account and project.
- Retrieve the project ID for your project. To obtain a project ID, use [GET projects](/en/docs/bim360/v1/reference/http/admin-accounts-accountidprojects-GET/).

## [Step 1: Retrieve a Tracking Item Instance from Autodesk Cost Management](#step-1-retrieve-a-tracking-item-instance-from-autodesk-cost-management)

To obtain the ID of the tracking item instance you want to retrieve, use the projectâs cost container ID (`e94b9bc8-1775-4d76-9b1d-c613e120ccff` in this example) to call [GET performance-tracking-item-instances](/en/docs/bim360/v1/reference/http/cost-performance-tracking-item-instances-GET/).

### Request

```
curl -X GET 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/performance-tracking-item-instances?limit=20&offset=0'
\ -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0'

```

### Response

```
{
    "pagination": {
        "limit": 20,
        "offset": 0,
        "totalResults": 1,
        "nextUrl": "..."
    },
    "results": [
        {
        "id": "1df59db0-9484-11e8-a7ec-7ddae203e404",
        "trackingItemId": "c06ab5f6-7015-498b-afc1-572d2d4df44f",
        "budgetCode": "84720010121001FEE",
        "number": "84720010121001FEE-0001",
        "name": "Concrete",
        "inputUnit": "hr",
        "inputQuantity": "100",
        "inputUnitPrice": "100.0000",
        "outputUnit": "cy",
        "outputQuantity": "10",
        "outputUnitPrice": "1000.0000",
        "trackedInputQuantity": "0",
        "trackedOutputQuantity": "0",
        "adjustedOutputQuantity": "0",
        "performanceRatio": "1",
        "locations": "4912f52b-4bf2-4651-a80c-2c30f515c826",
        "creatorId": "GF8XKPKWM38E",
        "changedBy": "GF8XKPKWM38E",
        "createdAt": "2019-01-06T01:24:22.678Z",
        "updatedAt": "2019-09-05T01:00:12.989Z"
        }
    ]
}

```

Show More

Note the tracking item instance ID (`results.id`) â `1df59db0-9484-11e8-a7ec-7ddae203e404`, the budget code (`results.budgetCode`) â `84720010121001FEE`, and the item instance sequence number (`results.number`) â `84720010121001FEE-0001` in the response.

## [Step 2: Log and Aggregate the Timesheets](#step-2-log-and-aggregate-the-timesheets)

A field user uses your integrated tracking app to log their progress in the appâs timesheets against the tracking item instance ID noted in the previous step.

The tracking app aggregates the `inputQuantity` and `outputQuantity` values entered by the user into timesheets by day and tracking instance, distinguished, for example, by location. Assume the unit of measurement of `inputQuantity` to be `hr` (hour).

## [Step 3: Synchronize Timesheets with Autodesk Cost Management](#step-3-synchronize-timesheets-with-autodesk-cost-management)

To capture the timesheet data from your tracking app, use the tracking item instance ID noted in step 1 (`1df59db0-9484-11e8-a7ec-7ddae203e404`) to call [POST time-sheets](/en/docs/bim360/v1/reference/http/cost-time-sheets-POST/) to create a timesheet object for the specified tracking item instance.

You can apply a time range (`startDate` and `endDate`) if the timesheet data covers multiple days, and the required `endDate` will be used to calculate the tracking item instance performance. Also required are `inputQuantity` and `outputQuantity`.

### Request

```
curl -X POST 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/time-sheets'
\ -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0'
\ -H 'Content-Type: application/json'
\ -d '{
        "trackingItemInstanceId": "1df59db0-9484-11e8-a7ec-7ddae203e404",
        "startDate": "2022-05-06",
        "endDate": "2022-05-06",
        "inputQuantity": 100,
        "outputQuantity": 5
      }'

```

Show More

### Response

```
{
    "id": "7896c6b0-b813-11ed-ab16-511fe7f6873f",
    "startDate": "2022-05-06",
    "endDate": "2022-05-06",
    "inputQuantity": 100,
    "inputUnit": "hr",
    "outputQuantity": 5,
    "outputUnit": "ea",
    "trackingItemInstanceId": "1df59db0-9484-11e8-a7ec-7ddae203e404"
}

```

Show More

## [Step 4: Adjust the Forecast](#step-4-adjust-the-forecast)

The cost engineer analyzes the performance by tracking item instance, then creates a forecast adjustment.
