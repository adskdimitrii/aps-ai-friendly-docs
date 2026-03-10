# Find and Update a Data Request

Source: https://aps.autodesk.com/en/docs/acc/tutorials/data-connector/dc-tutorial-find-update-data-request/

---

# Find and Update a Data Request

This tutorial shows how to find and update an existing data request stored by the Data Connector service. For this example, we’ll change the description of the data request created in the last tutorial. We’ll start by retrieving all your currently saved data requests so that we can find the appropriate data request and its data request ID. We’ll then examine the data request’s current settings, and change its description.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:create`, `data:read`, and `data:write` scopes. The token’s authenticated user must have executive overview permissions.
- Verify that you have access to a relevant BIM 360 account that contains at least one project. If you don’t know your account ID, you can derive it from your hub ID: Use [GET hubs](../../data/http-docs/http-hubs-GET.md) in the Data Management API to retrieve your hub ID. Remove the initial “b.” from the hub ID to get your account ID. For example, a hub ID of `b.c8b0c73d-3ae9` translates to an account ID of `c8b0c73d-3ae9`.

## [Step 1: Get a List of Saved Requests](#step-1-get-a-list-of-saved-requests)

Use [GET requests](../http-docs/http-data-connector-requests-GET.md) to retrieve a list of your saved data requests. This endpoint retrieves a list that is restricted to the requester’s saved data requests, so it won’t list any data requests created by other users. If you have many saved data requests, you can set request parameters to limit the number of returned requests, offset the point where you start returning requests, and set sort order. We won’t specify any of this, so the endpoint will use default settings of ascending sort order, a limit of 20 requests, and no offset.

### Request

```
curl -X GET 'https://developer.api.autodesk.com/data-connector/v1/accounts/<accountId>/requests?limit=20&sort=desc' \
-H 'Authorization: Bearer <authToken>'

```

### Response

```
{
    "pagination": {
        "limit": 20,
        "offset": 0,
        "totalResults": 1
    },
    "results": [
        {
            "id": "55e410c5-4294-44ce-becf-68e1cfd6738c",
            "description": "My Weekly Extract",
            "isActive": true,
            "accountId": "872264f8-2433-498d-8d36-16649ecb13fe",
            "projectId": "ffffffff-1f51-4b26-a6b7-6ac0639cb138",
            "createdBy": "73f00c25-a5f9-4c05-861d-ce56d54fa649",
            "createdByEmail": "your.name@autodesk.com",
            "updatedBy": "73f00c25-a5f9-4c05-861d-ce56d54fa649",
            "scheduleInterval": "WEEK",
            "reoccuringInterval": 1,
            "effectiveFrom": "2020-11-19T16:00:00.000Z",
            "effectiveTo": "2021-11-19T16:00:00.000Z",
            "lastQueuedAt": "2020-11-19T16:32:54.725Z",
            "nextExecAt": "2020-11-26T16:00:00.000Z",
            "serviceGroups": [
                "admin",
                "issues",
                "locations",
                "submittals",
                "cost",
                "rfis"
            ],
            "callbackUrl": null,
            "createdAt": "2020-11-19T16:32:13.545Z",
            "updatedAt": "2020-11-19T16:32:54.728Z",
            "deletedAt": null
        }
    ]
}

```

Show More

The results returned by this endpoint report the ID, settings, and status of each data request (in this case just the single data request we created in the last tutorial). We’ll use the ID of the data request in the next step when we update the data request.

Note that if you have the ID of a single data request for which you want to see status, you can use the [GET requests/:requestId](../http-docs/http-data-connector-requests-requestId-GET.md) endpoint instead of this endpoint to retrieve the request’s status without having to list other data requests.

## [Step 2: Change Your Request’s Active Status](#step-2-change-your-request-s-active-status)

To update your data request’s description, use the [PATCH requests](../http-docs/http-data-connector-requests-requestId-PATCH.md) endpoint. It accepts a set of parameter settings that you want to change in the data request. You don’t need to specify all the parameters settings, just the one you want to change. In this example, it’s description. We’ll change it to “My Updated Weekly Extract”.

### Request

```
curl -X PATCH 'https://developer.api.autodesk.com/data-connector/v1/accounts/<accountId>/requests/<requestId>' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer <authToken>' \
-d '{
    "description": "My Updated Weekly Extract"
}'

```

### Response

```
{
    "id": "55e410c5-4294-44ce-becf-68e1cfd6738c",
    "description": "My Updated Weekly Extract",
    "isActive": true,
    "accountId": "872264f8-2433-498d-8d36-16649ecb13fe",
    "projectId": "ffffffff-1f51-4b26-a6b7-6ac0639cb138",
    "createdBy": "73f00c25-a5f9-4c05-861d-ce56d54fa649",
    "createdByEmail": "your.name@autodesk.com",
    "updatedBy": "73f00c25-a5f9-4c05-861d-ce56d54fa649",
    "scheduleInterval": "WEEK",
    "reoccuringInterval": 1,
    "effectiveFrom": "2020-11-19T16:00:00.000Z",
    "effectiveTo": "2021-11-19T16:00:00.000Z",
    "lastQueuedAt": "2020-11-19T16:32:54.725Z",
    "nextExecAt": "2020-11-26T16:00:00.000Z",
    "callbackUrl": null,
    "createdAt": "2020-11-19T16:32:13.545Z",
    "updatedAt": "2020-11-19T16:35:13.912Z",
    "deletedAt": null,
    "serviceGroups": [
        "admin",
        "issues",
        "locations",
        "submittals",
        "cost",
        "rfis"
    ]
}

```

Show More

The response contains the updated parameter settings for your specified data request.
