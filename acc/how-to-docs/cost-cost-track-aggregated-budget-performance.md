# Track Aggregated Budget Performance

Source: https://aps.autodesk.com/en/docs/acc/tutorials/cost/cost-track-aggregated-budget-performance/

---

# Track Aggregated Budget Performance

This tutorial demonstrates how to use the Cost Management API to track the performance of a project budget based on its budget code. The performance tracking item that represents a budget is tracked by one or more timesheets, each of which is linked to one of the tracking itemâs instances. The tutorial aggregates the tracking data from all of the timesheets associated with a given budget. The steps include retrieving the budget code, logging and aggregating timesheets, synchronizing the timesheets with Autodesk Cost Management, and adjusting the forecast.

Budget codes are synchronized from Autodesk Cost Management or other external systems e.g. ERP/accounting system (assume theyâre always synchronized).

Note that the Cost API timesheets endpoints used in this tutorial are designed only for use with a third party timesheet reporting (tracking) app (e.g. Riskcast, Rhumbix, QuickBooks Time, or ClickUp) that youâve integrated with Cost Management.

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps).
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:create`, `data:read`, and `data:write` scopes.
- Verify that you have access to the relevant BIM 360 account and project.
- Retrieve the project ID for your project. To obtain a project ID, use [GET projects](../http-docs/http-admin-accounts-accountidprojects-GET.md).

## [Step 1: Retrieve the Budget Code](#step-1-retrieve-the-budget-code)

To retrieve the budget code of the budget you want to track, use the value of `containerId` to call [GET budgets](../http-docs/http-cost-budgets-GET.md) with the appropriate filter criteria.

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/budgets?filter[lastModifiedSince]=2020-03-01T13:00:00Z&limit=100&sort=name,createdAt desc'
\ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
    "pagination": {
        "limit": 20,
        "offset": 0,
        "totalResults": 1,
        "nextUrl": ""
    },
    "results": [
        {
        "id": "683904a0-47ce-4146-ac2d-a3840f00e0f4",
        "parentId": "null",
        "code": "84720010130000GEN",
        "scope": "budgetAndCost",
        "subItems": "",
        "budgetCode": "84720010121001FEE",
        "name": "Contingency",
        "description": "Reserved for contingency",
        "quantity": 50,
        "inputQuantity": 50,
        "ratio": 1,
        "unitPrice": "1000.0000",
        "unit": "LS",
        "originalAmount": 1000,
        "milestoneId": "227e1360-9481-11e8-87fb-215990a8aeb3",
        "internalAdjustment": 1000,
        "approvedOwnerChanges": 1000,
        "pendingOwnerChanges": 1000,
        "originalCommitment": 1000,
        "approvedChangeOrders": 1000,
        "approvedInScopeChangeOrders": 1000,
        "pendingChangeOrders": 1000,
        "reserves": 1000,
        "actualQuantity": 50,
        "actualUnitPrice": "1000.0000",
        "actualCost": 1000,
        "mainContractId": "f6445638-ca68-4e3c-9160-15864de6b818",
        "locations": "",
        "locationPaths": "",
        "plannedStartDate": "2019-01-06",
        "plannedEndDate": "2020-01-06",
        "actualStartDate": "2019-01-06",
        "actualEndDate": "2020-02-10",
        "durationDays": 90,
        "uncommitted": 1000,
        "revised": 1000,
        "projectedCost": 1000,
        "projectedBudget": 1000,
        "forecastFinalCost": 1000,
        "forecastVariance": 1000,
        "forecastCostComplete": 1000,
        "varianceTotal": 1000,
        "externalId": "10010-99-AB",
        "externalSystem": "Sage300",
        "externalMessage": "Success",
        "lastSyncTime": "2019-09-05T01:00:12.989Z",
        "integrationState": "locked",
        "integrationStateChangedAt": "2019-09-05T01:00:12.989Z",
        "integrationStateChangedBy": "CED9LVTLHNXV",
        "createdAt": "2019-01-06T01:24:22.678Z",
        "updatedAt": "2019-09-05T01:00:12.989Z"
        }
    ]
}

```

Show More

Note the budget code (`results.budgetCode`) â `84720010121001FEE`.

## [Step 2: Log and Aggregate the Timesheets](#step-2-log-and-aggregate-the-timesheets)

A field user uses your integrated tracking app to log their progress in the appâs timesheets against the budget code noted in the previous step.

The tracking app aggregates the `inputQuantity` and `outputQuantity` values entered by the user into timesheets by day and budget code. Assume the unit of measurement of `inputQuantity` to be `hr` (hour).

## [Step 3: Synchronize Timesheets with Autodesk Cost Management](#step-3-synchronize-timesheets-with-autodesk-cost-management)

To capture the aggregated timesheet data from your tracking app, use the budget code noted in step 1 (`84720010121001FEE`) to call [POST time-sheets](../http-docs/http-cost-time-sheets-POST.md) to create a timesheet object for the specified budget.

### Request

```
curl -X POST 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/time-sheets'
\-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0'
\-H 'Content-Type: application/json' \
-d '{
        "budgetCode": "84720010121001FEE",
        "startDate": "2020-01-06",
        "endDate": "2020-01-06",
        "inputQuantity": 100,
        "outputQuantity": 5
    }

```

Show More

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
        "outputQuantity": "5",
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

The new timesheet object is associated with the first (default) tracking item instance of the budgetâs performance tracking item.

## [Step 4: Adjust the Forecast](#step-4-adjust-the-forecast)

The cost engineer analyzes the performance by tracking item instance and creates a forecast adjustment.
