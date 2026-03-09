# Update Existing Timesheets

Source: https://aps.autodesk.com/en/docs/acc/tutorials/cost/cost-update-existing-time-sheets/

---

# Update Existing Timesheets

This tutorial demonstrates how to update existing timesheets. The steps include finding the timesheet ID and updating the timesheet.

Note that the Cost API timesheets endpoints used in this tutorial are designed only for use with a third party timesheet reporting (tracking) app (e.g. Riskcast, Rhumbix, QuickBooks Time, or ClickUp) that youâve integrated with Cost Management.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps).
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:create`, `data:read`, and `data:write` scopes.
- Verify that you have access to the relevant BIM 360 account and project.
- Retrieve the project ID for your project. To obtain a project ID, use [GET projects](../http-docs/http-admin-accounts-accountidprojects-GET.md).

## [Step 1: Find the Timesheet ID](#step-1-find-the-timesheet-id)

To retrieve the ID of the timesheet you want to update, call [GET time-sheets](../http-docs/http-cost-time-sheets-GET.md). In this example, assume that the project container ID is `e94b9bc8-1775-4d76-9b1d-c613e120ccff`.

### Request

```
curl -X GET 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/time-sheets?filter[budgetCode]=84720010121001FEE&filter[endDate]=2022-05-06' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0'

```

### Response

```
{
    "pagination": {
        "limit": 20,
        "offset": 0,
        "totalResults": 100,
        "nextUrl": "..."
    },
    "results": [
        {
            "id": "6f7f7780-3867-4aa3-9f37-8ae53532a590",
            "containerId": "e94b9bc8-1775-4d76-9b1d-c613e120ccff",
            "trackingItemInstanceId": "1df59db0-9484-11e8-a7ec-7ddae203e404",
            "startDate": "2020-01-06",
            "endDate": "2020-05-06",
            "inputQuantity": "100",
            "outputQuantity": "50",
            "creatorId": "GF8XKPKWM38E",
            "changedBy": "GF8XKPKWM38E",
            "createdAt": "2020-01-06T01:24:22.678Z",
            "updatedAt": "2020-05-06T01:00:12.989Z"
        }
    ]
}

```

Show More

Find the timesheet you want to update and note the timesheet ID (`6f7f7780-3867-4aa3-9f37-8ae53532a590`).

## [Step 2: Update the Timesheet by ID](#step-2-update-the-timesheet-by-id)

To update the timesheet, use the timesheet ID (`6f7f7780-3867-4aa3-9f37-8ae53532a590`) to call [PATCH time-sheets/:id](../http-docs/http-cost-time-sheets-id-PATCH.md). Provide updated values for any of the endpointâs request payload fields.

### Request

```
curl -X PATCH 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/time-sheets/6f7f7780-3867-4aa3-9f37-8ae53532a590'
\ -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0'
\ -H 'Content-Type: application/json'
\ -d '{
        "inputQuantity": 100,
        "outputQuantity": 2
      }'

```

### Response

```
{
    "id": "6f7f7780-3867-4aa3-9f37-8ae53532a590",
    "startDate": "2022-05-06",
    "endDate": "2022-05-06",
    "inputQuantity": 100,
    "inputUnit": "hr",
    "outputQuantity": 2,
    "outputUnit": "ea",
    "trackingItemInstanceId": "1df59db0-9484-11e8-a7ec-7ddae203e404"
}

```

Show More

Your timesheet has been updated with the new input and output quantities.
