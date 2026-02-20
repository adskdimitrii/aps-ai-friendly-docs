# Submit a Data Request

Source: https://aps.autodesk.com/en/docs/acc/tutorials/data-connector/dc-tutorial-submit-data-request/

---

# Submit a Data Request

This phase of the tutorial demonstrates how to submit a data request that extracts service data from within a BIM 360/ACC account. In this tutorial, your data request will be a recurring request that spawns a job once every week, and returns extracted data for seven different services.

## Before You Begin

- Register an app

- Acquire a 3-legged OAuth token with data:create , data:read , and data:write scopes. The tokenâs authenticated user must have executive overview permissions or project administrator permissions.

- Verify that you have access to a relevant BIM 360/ACC account that contains at least one project. If you donât know your account ID, you can derive it from your hub ID: Use GET hubs in the Data Management API to retrieve your hub ID. Remove the initial âb.â from the hub ID to get your account ID. For example, a hub ID of b.c8b0c73d-3ae9 translates to an account ID of c8b0c73d-3ae9 .

## Step 1: Determine Your Data Parameters

To make a data request, youâll have to provide request parameter values that correctly specify the type of data extraction you want the Data Connector service to perform and to provide other useful information stored with the request:

- description contains a text string describing the data request, in this case "My Weekly Extract" .

- scheduleInterval specifies the interval unit weâll use for scheduling. In this case we measure in weeks, so the value is WEEK .

- reoccuringInterval specifies the number of units to wait between job spawns. Because we want this request to spawn a job once every week, the value is 1 .

- effectiveFrom and effectiveTo define the starting and ending times for the recurring jobs. Itâs during this time that the jobs spawn and execute, starting on the effectiveFrom time and ending on the effectiveTo time. These two values define date and time in ISO 8601 format. For this example, weâll set a one-year interval. Our example values: 2020-11-19T16:00:00Z start time, 2021-11-19T16:00:00Z end time.

- serviceGroups defines the scope of the data extraction for this data request: the services for which we want to examine data. In this case, we look at admin, issues, locations, submittals, cost, and rfis. You can also specify all to extract data for all service groups. Note that the admin service covers both project and account administration.

- projectId specifies which project to extract data from. Usage depends on the permissions level of the authenticated user: Executive Overview permissions â (optional) If neither projectId or projectIdList is specified, the request will apply to all projects in the userâs account. Project Administrator permissions â (required) If neither projectId or `` projectIdList` is specified, the request will fail.

- Executive Overview permissions â (optional) If neither projectId or projectIdList is specified, the request will apply to all projects in the userâs account.

- Project Administrator permissions â (required) If neither projectId or `` projectIdList` is specified, the request will fail.

- projectIdList â¯specifies the list of projects to extract data from. projectId â¯can be omitted if projectIdList â¯is used. If both are provided, projectIdList â¯takes precedence. The user needs to have either Executive Overview permission, or Project Administrator permission in all the projects provided in the list. Otherwise, the request will fail.

- projectStatus â¯specifies the scope of the projects based on the project status. Use active if only data extraction from active projects is required.

## Step 2: Create a Data Request

Create a data request using the POST requests endpoint, specifying the account ID of your account. This tutorial demonstrates recurring data requests for two scenarios:

- Retrieving data for a specific list of projects using projectIdList .

- Retrieving data for all active projects in the account using projectStatus .

### Scenario 1: Requesting Data for Specific Projects

If the user wants to extract data for specific projects, include the projectIdList field in the request payload. This field specifies up to 50 project IDs.

### Request

```
curl -X POST 'https://developer.api.autodesk.com/data-connector/v1/accounts/<accountId>/requests' \ -H 'Content-Type: application/json' \ -H 'Authorization: Bearer <authToken>' \ -d ' { "description": "My Weekly Extract", "scheduleInterval": "WEEK", "reoccuringInterval": 1, "effectiveFrom": "2020-11-19T16:00:00Z", "effectiveTo": "2021-11-19T16:00:00Z", "serviceGroups": ["admin", "issues", "locations", "submittals", "cost", "rfis"], "projectIdList": [ "ffffffff-1f51-4b26-a6b7-6ac0639cb138", "aaaaaaaa-1f51-4b26-a6b7-6ac0639cb138"        ] }'
```

### Response

```
{ "id" : "55e410c5-4294-44ce-becf-68e1cfd6738c" , "isActive" : true , "accountId" : "872264f8-2433-498d-8d36-16649ecb13fe" , "projectId" : null , "projectIdList" : [ "ffffffff-1f51-4b26-a6b7-6ac0639cb138" , "aaaaaaaa-1f51-4b26-a6b7-6ac0639cb138" ], "description" : "My Weekly Extract" , "createdBy" : "73f00c25-a5f9-4c05-861d-ce56d54fa649" , "createdByEmail" : "your.name@autodesk.com" , "updatedBy" : "73f00c25-a5f9-4c05-861d-ce56d54fa649" , "scheduleInterval" : "WEEK" , "reoccuringInterval" : 1 , "effectiveFrom" : "2020-11-19T16:00:00.000Z" , "effectiveTo" : "2021-11-19T16:00:00.000Z" , "nextExecAt" : "2020-11-19T16:00:00.000Z" , "serviceGroups" : [ "admin" , "issues" , "locations" , "submittals" , "cost" , "rfis" ], "callbackUrl" : null , "lastQueuedAt" : null , "updatedAt" : "2020-11-19T16:32:13.545Z" , "createdAt" : "2020-11-19T16:32:13.545Z" , "deletedAt" : null }
```

### Scenario 2: Requesting Data for Active Projects

If the user has executive overview permissions and wants to retrieve data for all active projects in the account, use the projectStatus field.

### Request

```
curl -X POST 'https://developer.api.autodesk.com/data-connector/v1/accounts/<accountId>/requests' \ -H 'Content-Type: application/json' \ -H 'Authorization: Bearer <authToken>' \ -d ' { "description": "My Weekly Extract", "scheduleInterval": "WEEK", "reoccuringInterval": 1, "effectiveFrom": "2020-11-19T16:00:00Z", "effectiveTo": "2021-11-19T16:00:00Z", "serviceGroups": ["admin", "issues", "locations", "submittals", "cost", "rfis"], "projectStatus": "active" }'
```

### Response

```
{ "id" : "55e410c5-4294-44ce-becf-68e1cfd6738c" , "isActive" : true , "accountId" : "872264f8-2433-498d-8d36-16649ecb13fe" , "description" : "My Weekly Extract" , "createdBy" : "73f00c25-a5f9-4c05-861d-ce56d54fa649" , "createdByEmail" : "your.name@autodesk.com" , "updatedBy" : "73f00c25-a5f9-4c05-861d-ce56d54fa649" , "scheduleInterval" : "WEEK" , "reoccuringInterval" : 1 , "effectiveFrom" : "2020-11-19T16:00:00.000Z" , "effectiveTo" : "2021-11-19T16:00:00.000Z" , "nextExecAt" : "2020-11-19T16:00:00.000Z" , "serviceGroups" : [ "admin" , "issues" , "locations" , "submittals" , "cost" , "rfis" ], "callbackUrl" : null , "lastQueuedAt" : null , "updatedAt" : "2020-11-19T16:32:13.545Z" , "createdAt" : "2020-11-19T16:32:13.545Z" , "deletedAt" : null , "projectStatus" : "active"
```

The response reports the data request settings and status, and includes an id value that provides the data request ID. Use the data request ID to specify this data request when calling other Data Connector API endpoints. If you donât save the ID, you can query the API (as weâll do in the next example) for the data request IDs of your data requests currently stored by the Data Connector service.

Notice that optional field values not set in the request get set to default values.
