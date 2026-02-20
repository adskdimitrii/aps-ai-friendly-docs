# accounts/{accountId}/jobs

Source: https://aps.autodesk.com/en/docs/acc/reference/http/data-connector-jobs-GET/

---

# accounts/{accountId}/jobs

Returns an array of Data Connector jobs spawned by requests from the authenticated user. The array can contain all jobs associated with a specified project, or all jobs associated with all projects in the userâs account. The user must have project administrator or executive overview permissions:

- Users with project administrator permissions may retrieve jobs for one project.

- Users with executive overview permissions may retrieve jobs for one project or all projects in their account.

Returned information for each job in the array includes the job ID, the ID of its associated request, the ID of the account where the request was created, and the ID and email address of the user who created the request. It also includes information about when the job was created, when it was started and completed (if it has been), its completion status, and its current execution status.

To get request IDs for your requests, use GET requests .

To understand the basics of requests, the jobs they spawn, and the data extracts returned by the jobs, see the Data Connector API Field Guide .

## Resource Information

Method and URI GET https://developer.api.autodesk.com/data-connector/v1/accounts/:accountId/jobs Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow.

### Request

## URI Parameters

accountId string: UUID The account ID. You can derive it from your hub ID if necessary: Use GET hubs in the Data Management API to retrieve your hub ID. Remove the initial âb.â from the hub ID to get your account ID.

### Request

## Query String Parameters

sort string The sort order of returned data connector objects. Possible values: asc ascending by date (earliest to latest date), desc descending by date (latest to earliest date). limit int The number of data connector objects to return. Default value: 20 offset int The number of data objects to skip before starting to starting to collect the result set. Default value: 0 projectId string Project ID of the returned Data Connector objects. sortFields string A string of comma-separated names of the fields by which to sort the returned jobs. The results are sorted by the first field, then by the second field, and so on. Jobs are sorted by each field in ascending order by default; you can prepend any field name with a hyphen ( - ) to sort in descending order. Invalid fields and whitespaces are ignored. Possible values: projectId , createdBy , createdByEmail , createdAt , status , completionStatus , startedAt , completedAt , startDate , endDate . filter[field_to_filter] string Return only the Data Connector jobs in which the specified field has the specified value. Use the following format in the endpoint URL: filter[field_to_filter]=_filter_value_ . Note that you can provide multiple job filters in the URL, but you may not filter on multiple values of the same field. Possible field_to_filter values: projectId , createdAt , status , completionStatus , startedAt , completedAt , startDate , endDate . You can also retrieve all Data Connector jobs in the current account by specifying filter[projectId]=null . For the createdAt , startedAt , and completedAt fields (which accept a date range), specify the range in the form firstdate..lastdate , in ISO 8601 format with the time required. You can alternatively omit the first date (for example, to get everything on or before June 1, 2019 the range would be ..2019-06-01T23:59:59.999Z ). You can also omit the last date (for example, to get everything after June 1, 2019 the range would be 2019-06-01T00:00:00.000Z.. ) Additional notes on using startDate and endDate : If you provide only startDate or endDate (but not both), Data Connector uses that single date for both startDate and endDate . If you request more than the Maximum Date Range Allowed for an extraction, the default date range as documented in the schema documentation is returned. For the activities service group, data replication can be delayed up to 20 minutes, so your requests should account for that delay.

Possible values: projectId , createdBy , createdByEmail , createdAt , status , completionStatus , startedAt , completedAt , startDate , endDate .

Note that you can provide multiple job filters in the URL, but you may not filter on multiple values of the same field.

Possible field_to_filter values: projectId , createdAt , status , completionStatus , startedAt , completedAt , startDate , endDate . You can also retrieve all Data Connector jobs in the current account by specifying filter[projectId]=null .

For the createdAt , startedAt , and completedAt fields (which accept a date range), specify the range in the form firstdate..lastdate , in ISO 8601 format with the time required. You can alternatively omit the first date (for example, to get everything on or before June 1, 2019 the range would be ..2019-06-01T23:59:59.999Z ). You can also omit the last date (for example, to get everything after June 1, 2019 the range would be 2019-06-01T00:00:00.000Z.. )

Additional notes on using startDate and endDate :

- If you provide only startDate or endDate (but not both), Data Connector uses that single date for both startDate and endDate .

- If you request more than the Maximum Date Range Allowed for an extraction, the default date range as documented in the schema documentation is returned.

- For the activities service group, data replication can be delayed up to 20 minutes, so your requests should account for that delay.

### Response

## HTTP Status Code Summary

200 OK Successfully retrieved an array of jobs associated with the specified data request. 400 Bad Request The parameters are invalid. 401 Unauthorized The provided bearer token is invalid. 403 Forbidden Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The resource or endpoint cannot be found. 429 Too Many Requests Rate limited exceeded; wait some time before retrying. 500 Internal Server Error An unexpected error occurred on the server. 503 Service Unavailable Service unavailable.

### Response

## Body Structure (200)

pagination object Information about the pagination used to return the results array. limit int The specified upper limit of results to return. offset int The specified number of results skipped before the results in this array were collected. totalResults int The total number of results returned here. results array: object An array of job records. id string: UUID The job ID. requestId string: UUID The ID of the data request that spawned the job. accountId string: UUID The account ID. projectId string: UUID The project ID. projectIdList array: string The list of project IDs createdBy string The BIM 360 / ACC user ID of the user who created the data request that spawned this job. createdByEmail string The email address of the user who created the data request that spawned this job. createdAt datetime: ISO 8601 The date and time the job was created, presented in ISO 8601 format. status string The current status of the job. Possible values: queued , running , complete . completionStatus string The completion status for completed jobs. Possible values: success , failed , cancelled . startedAt datetime: ISO 8601 The date and time the job was started, presented in ISO 8601 format. If the job has not yet started, the value is null. completedAt datetime: ISO 8601 The date and time the job was completed, presented in ISO 8601 format. If the job has not yet completed, the value is null. sendEmail boolean Send a notification email when the job completes. progress int Job progress indicator (0 to 100 percent) lastDownloadedBy string The ID of the user who last downloaded this job data. lastDownloadedAt datetime: ISO 8601 The last date and time that a user downloaded this job data, in ISO 8601 format. startDate string The start date and time for the data extraction, in ISO 8601 format. This field applies only to schemas that support date range extraction. The detailed schema documentation delivered with each data extract identifies the schemas and tables that support date range extraction. endDate string The end date and time for the data extraction, in ISO 8601 format. This field applies only to schemas that support date range extraction. The detailed schema documentation delivered with each data extract identifies the schemas and tables that support date range extraction.

This field applies only to schemas that support date range extraction. The detailed schema documentation delivered with each data extract identifies the schemas and tables that support date range extraction.

This field applies only to schemas that support date range extraction. The detailed schema documentation delivered with each data extract identifies the schemas and tables that support date range extraction.

## Example

Successfully retrieved an array of jobs associated with the specified data request.

### Request

```
curl -v 'https://developer.api.autodesk.com/data-connector/v1/accounts/:accountId/jobs?sort=asc&limit=20&offset=0&projectId=ffffffff-1f51-4b26-a6b7-6ac0639cb138&sortFields=createdByEmail,-createdAt&filter[field_to_filter]=_filter_value_' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "pagination" : { "limit" : 20 , "offset" : 0 , "totalResults" : 100 }, "results" : [ { "id" : "ce9bc188-1e18-11eb-adc1-0242ac120002" , "requestId" : "a5a8e90f-3dbe-4b08-9b8e-16e8049ce31e" , "accountId" : "f9abf4c8-1f51-4b26-a6b7-6ac0639cb138" , "projectId" : null , "projectIdList" : "[ \"ffffffff-1f51-4b26-a6b7-6ac0639cb138\", \"aaaaaaaa-1f51-4b26-a6b7-6ac0639cb138\" ]" , "createdBy" : "ABCDEFGHI" , "createdByEmail" : "joe.user@mycompany.com" , "createdAt" : "2020-11-06T19:09:40.106Z" , "status" : "complete" , "completionStatus" : "success" , "startedAt" : "2020-11-06T19:10:00.106Z" , "completedAt" : "2020-11-06T19:29:40.106Z" , "sendEmail" : true , "progress" : "" , "lastDownloadedBy" : "joe.user@mycompany.com" , "lastDownloadedAt" : "2021-11-06T19:09:40.106Z" , "startDate" : "2023-06-06T00:00:00.000Z" , "endDate" : "2023-06-06T12:00:00.000Z" } ] }
```
