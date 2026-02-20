# accounts/{accountId}/requests

Source: https://aps.autodesk.com/en/docs/acc/reference/http/data-connector-requests-POST/

---

# accounts/{accountId}/requests

Creates a data request for an authenticated user. The user can optionally limit the request to one project. The user must have executive overview or project administrator permissions.

As a successfully created data request spawns jobs, those jobs will send status email to the data request creator when completed. If the data request contains a callback URL, jobs will also call that URL when completed. Data Connector requests and their resulting jobs are subject to rate limits: an account can create a maximum of 24 jobs within a 24-hour period, and an individual user can create up to 24 jobs within the same timeframe. For more details, see the Rate Limits page.

To understand the basics of requests, the jobs they spawn, and the data extracts returned by the jobs, see the Data Connector API Field Guide .

## Resource Information

Method and URI POST https://developer.api.autodesk.com/data-connector/v1/accounts/:accountId/requests Authentication Context user context required Required OAuth Scopes data:create Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json

### Request

## URI Parameters

accountId string: UUID The account ID. You can derive it from your hub ID if necessary: Use GET hubs in the Data Management API to retrieve your hub ID. Remove the initial âb.â from the hub ID to get your account ID.

### Request

## Body Structure

description string The user-entered description of this data request. isActive boolean The data requestâs active/inactive status. Possible values: true the request is active; false the request is inactive. If not supplied, the default value is true . scheduleInterval string The scheduling interval unit for jobs spawned by this data request. This value is multiplied by the reoccurringInterval attribute to specify the length of the recurring interval at which jobs run. Possible values: ONE_TIME : Run the job only once DAY : Set the recurring job interval in days WEEK : Set the recurring job interval in weeks MONTH : Set the recurring job interval in months YEAR : Set the recurring job interval in years Note that recurring jobs start at the day and time when the request first spawns a job. This may be at the date and time specified in the attribute effectiveFrom . reoccuringInterval int The number of scheduleInterval units to wait between job execution for the request. For example, a scheduleInterval value of WEEK and a reoccuringInterval value of 2 means the job will run every two weeks. This value is required and must be a non-zero integer for all values of scheduleInterval except for a scheduleInterval value of ONE_TIME , in which case this value is ignored. effectiveFrom datetime: ISO 8601 The date and time when a one-time job execution or a recurring interval schedule begins, presented in ISO 8601 format. If the date and time is before the current time, execution of scheduling begins immediately. This value is required. effectiveTo datetime: ISO 8601 The date and time when the recurring interval schedule ends, presented in ISO 8601 format. This value must not be supplied for scheduleInterval values of ONE_TIME , but is required for all other scheduleInterval values. serviceGroups array: string The service groups from which to extract data, separated by commas. This required value must identify at least one service group. Possible values: all , activities , admin , assets , checklists , cost , dailylogs , forms , iq , issues , locations , markups , meetingminutes , photos , relationships , reviews , rfis , schedule , sheets , submittals , submittalsacc , transmittals . Note that the admin service includes both project and account admin, and all produces an extract containing all currently available service groups. callbackUrl string The callback URL specified for the data request. If specified, the Data Connection service calls the URL each time a job executes for the request. The service sends a POST request that provides job execution information. The JSON payload in the POST request contains the following: { "accountId": "account_id", "requestId": "request_id", "jobId": "data_connector_job_id", "state": "complete", "success": true or false } . If not specified, the Data Connection service does not provide a callback. sendEmail boolean Send a notification email to the user upon job completion. Values: true or false (default is true) projectId string (Legacy): A single project ID for the data request. Superseded by projectIdList . projectIdList array: string A list of up to 50 project IDs for the data request, which can include a single project or multiple projects. If projectId is also included, projectIdList takes precedence. Required for users with project admin permissions. Optional for users with executive overview permissions, who by default receive data for all projects unless projectIdList is provided. startDate string The start date and time for the data extraction, in ISO 8601 format. This field applies only to schemas supporting date range extraction. The detailed schema documentation delivered with each data extract identifies the schemas and tables that support date range extraction. Additional notes on using startDate and endDate : If you provide only startDate or endDate (but not both), Data Connector uses that single date for both startDate and endDate . If you request more than the Maximum Date Range Allowed for an extraction, the default date range as documented in the schema documentation is returned. For the activities service group, data replication can be delayed up to 20 minutes, so your requests should account for that delay. endDate string The end date and time for the data extraction, in ISO 8601 format. This field applies only to schemas supporting date range extraction. The detailed schema documentation delivered with each data extract identifies the schemas and tables that support date range extraction. Additional notes on using startDate and endDate : If you provide only startDate or endDate (but not both), Data Connector uses that single date for both startDate and endDate . If you request more than the Maximum Date Range Allowed for an extraction, the default date range as documented in the schema documentation is returned. For the activities service group, data replication can be delayed up to 20 minutes, so your requests should account for that delay. dateRange string Specifies the timeframe for extracting data in a scheduled request (DAY, WEEK, MONTH, YEAR). Currently, it is applicable only to the Activities service. Possible values: TODAY : The current calendar day, from 00:00 UTC to the time the request is made. YESTERDAY : The entire previous calendar day (00:00 UTC to 23:59 UTC). PAST_7_DAYS : The last 7 days, including the current day. MONTH_TO_DATE : From the start of the current calendar month (00:00 UTC on the 1st) to the time the request is made. LAST_MONTH : The entire previous calendar month (00:00 UTC on the 1st to 23:59 UTC on the last day). projectStatus string The types of projects to be included in a request. The possible values are: all : - all projects (default) archived : archived projects only active : active project only

- ONE_TIME : Run the job only once

- DAY : Set the recurring job interval in days

- WEEK : Set the recurring job interval in weeks

- MONTH : Set the recurring job interval in months

- YEAR : Set the recurring job interval in years

Note that recurring jobs start at the day and time when the request first spawns a job. This may be at the date and time specified in the attribute effectiveFrom .

This value is required and must be a non-zero integer for all values of scheduleInterval except for a scheduleInterval value of ONE_TIME , in which case this value is ignored.

Possible values: all , activities , admin , assets , checklists , cost , dailylogs , forms , iq , issues , locations , markups , meetingminutes , photos , relationships , reviews , rfis , schedule , sheets , submittals , submittalsacc , transmittals .

Note that the admin service includes both project and account admin, and all produces an extract containing all currently available service groups.

If not specified, the Data Connection service does not provide a callback.

This field applies only to schemas supporting date range extraction. The detailed schema documentation delivered with each data extract identifies the schemas and tables that support date range extraction.

Additional notes on using startDate and endDate :

- If you provide only startDate or endDate (but not both), Data Connector uses that single date for both startDate and endDate .

- If you request more than the Maximum Date Range Allowed for an extraction, the default date range as documented in the schema documentation is returned.

- For the activities service group, data replication can be delayed up to 20 minutes, so your requests should account for that delay.

This field applies only to schemas supporting date range extraction. The detailed schema documentation delivered with each data extract identifies the schemas and tables that support date range extraction.

Additional notes on using startDate and endDate :

- If you provide only startDate or endDate (but not both), Data Connector uses that single date for both startDate and endDate .

- If you request more than the Maximum Date Range Allowed for an extraction, the default date range as documented in the schema documentation is returned.

- For the activities service group, data replication can be delayed up to 20 minutes, so your requests should account for that delay.

- TODAY : The current calendar day, from 00:00 UTC to the time the request is made.

- YESTERDAY : The entire previous calendar day (00:00 UTC to 23:59 UTC).

- PAST_7_DAYS : The last 7 days, including the current day.

- MONTH_TO_DATE : From the start of the current calendar month (00:00 UTC on the 1st) to the time the request is made.

- LAST_MONTH : The entire previous calendar month (00:00 UTC on the 1st to 23:59 UTC on the last day).

- all : - all projects (default)

- archived : archived projects only

- active : active project only

### Response

## HTTP Status Code Summary

201 Created Successfully created a data request that is described in the response. 400 Bad Request The parameters are invalid. 401 Unauthorized The provided bearer token is invalid. 403 Forbidden Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The resource or endpoint cannot be found. 429 Too Many Requests Rate limited exceeded; wait some time before retrying. 500 Internal Server Error An unexpected error occurred on the server. 503 Service Unavailable Service unavailable.

### Response

## Body Structure (201)

id string: UUID The ID of the data request. description string The user-entered description of this data request. If not supplied, the default value is a null string. isActive boolean The data requestâs active/inactive status. Possible values: true the request is active; false the request is inactive. accountId string: UUID The account ID. projectId string: UUID (Legacy): A single project ID for the data request. Superseded by projectIdList . projectIdList array: string A list of up to 50 project IDs included in the data request. This field contains the project IDs for which data is being extracted. If both projectId and projectIdList were included in the request, this field contains the values from projectIdList . createdBy string The BIM 360 / ACC user ID of the user who created the data request. createdByEmail string The email address of the user who created the data request. createdAt datetime: ISO 8601 The date and time the data request was created, presented in ISO 8601 format. updatedBy string The BIM 360 / ACC user ID of the user who last updated the data request. updatedAt datetime: ISO 8601 The date and time the data request was last updated, presented in ISO 8601 format. scheduleInterval string The scheduling interval unit for jobs spawned by this data request. This value is multiplied by the reoccurringInterval attribute to specify the length of the recurring interval at which jobs run. Possible values: ONE_TIME : Run the job only once DAY : Set the recurring job interval in days WEEK : Set the recurring job interval in weeks MONTH : Set the recurring job interval in months YEAR : Set the recurring job interval in years reoccuringInterval int The number of scheduleInterval units to wait between job execution for the request. For example, a scheduleInterval value of WEEK and a reoccuringInterval value of 2 means the job will run every two weeks. effectiveFrom datetime: ISO 8601 The date and time when a one-time job execution or a recurring interval schedule begins, presented in ISO 8601 format. effectiveTo datetime: ISO 8601 The date and time when the recurring interval schedule ends, presented in ISO 8601 format. lastQueuedAt datetime: ISO 8601 The date and time the last job for this data request was scheduled to execute, presented in ISO 8601 format. serviceGroups array: string The service groups from which data has been extracted, separated by commas. Possible values: all , activities , admin , assets , checklists , cost , dailylogs , forms , iq , issues , locations , markups , meetingminutes , photos , relationships , reviews , rfis , schedule , sheets , submittals , submittalsacc , transmittals . Note that the admin service includes both project and account admin, and all indicates that the extract contains all currently available service groups. callbackUrl string The callback URL specified for the data request. If specified, the Data Connection service calls the URL each time a job executes for the request. The service sends a POST request that provides job execution information. The JSON payload in the POST request contains the following: { "accountId": "account_id", "requestId": "request_id", "jobId": "data_connector_job_id", "state": "complete", "success": true or false } . sendEmail boolean Send a notification email to the user upon job completion. Values: true or false (default is true) startDate string The start date and time for the data extraction, in ISO 8601 format. This field applies only to schemas supporting date range extraction. The detailed schema documentation delivered with each data extract identifies the schemas and tables that support date range extraction. Additional notes on using startDate and endDate : If you provide only startDate or endDate (but not both), Data Connector uses that single date for both startDate and endDate . If you request more than the Maximum Date Range Allowed for an extraction, the default date range as documented in the schema documentation is returned. For the activities service group, data replication can be delayed up to 20 minutes, so your requests should account for that delay. endDate string The end date and time for the data extraction, in ISO 8601 format. This field applies only to schemas supporting date range extraction. The detailed schema documentation delivered with each data extract identifies the schemas and tables that support date range extraction. Additional notes on using startDate and endDate : If you provide only startDate or endDate (but not both), Data Connector uses that single date for both startDate and endDate . If you request more than the Maximum Date Range Allowed for an extraction, the default date range as documented in the schema documentation is returned. For the activities service group, data replication can be delayed up to 20 minutes, so your requests should account for that delay. dateRange string The timeframe used for extracting data in the request. Currently, it is applicable only to the Activities service. This field contains the value specified in the request, indicating the range of data included in the response. Possible values: TODAY : Data for the current day (from 00:00 UTC to the time the request was made). YESTERDAY : Data for the previous calendar day (from 00:00 UTC to 23:59 UTC). PAST_7_DAYS : Data for the last 7 days, including the current day. MONTH_TO_DATE : Data from the start of the current calendar month (00:00 UTC on the 1st) to the time the request was made. LAST_MONTH : Data for the entire previous calendar month (00:00 UTC on the 1st to 23:59 UTC on the last day). projectStatus string The types of projects to be included in a request. The possible values are: all : - all projects (default) archived : archived projects only active : active project only

- ONE_TIME : Run the job only once

- DAY : Set the recurring job interval in days

- WEEK : Set the recurring job interval in weeks

- MONTH : Set the recurring job interval in months

- YEAR : Set the recurring job interval in years

Possible values: all , activities , admin , assets , checklists , cost , dailylogs , forms , iq , issues , locations , markups , meetingminutes , photos , relationships , reviews , rfis , schedule , sheets , submittals , submittalsacc , transmittals .

Note that the admin service includes both project and account admin, and all indicates that the extract contains all currently available service groups.

This field applies only to schemas supporting date range extraction. The detailed schema documentation delivered with each data extract identifies the schemas and tables that support date range extraction.

Additional notes on using startDate and endDate :

- If you provide only startDate or endDate (but not both), Data Connector uses that single date for both startDate and endDate .

- If you request more than the Maximum Date Range Allowed for an extraction, the default date range as documented in the schema documentation is returned.

- For the activities service group, data replication can be delayed up to 20 minutes, so your requests should account for that delay.

This field applies only to schemas supporting date range extraction. The detailed schema documentation delivered with each data extract identifies the schemas and tables that support date range extraction.

Additional notes on using startDate and endDate :

- If you provide only startDate or endDate (but not both), Data Connector uses that single date for both startDate and endDate .

- If you request more than the Maximum Date Range Allowed for an extraction, the default date range as documented in the schema documentation is returned.

- For the activities service group, data replication can be delayed up to 20 minutes, so your requests should account for that delay.

- TODAY : Data for the current day (from 00:00 UTC to the time the request was made).

- YESTERDAY : Data for the previous calendar day (from 00:00 UTC to 23:59 UTC).

- PAST_7_DAYS : Data for the last 7 days, including the current day.

- MONTH_TO_DATE : Data from the start of the current calendar month (00:00 UTC on the 1st) to the time the request was made.

- LAST_MONTH : Data for the entire previous calendar month (00:00 UTC on the 1st to 23:59 UTC on the last day).

- all : - all projects (default)

- archived : archived projects only

- active : active project only

## Example

Successfully created a data request that is described in the response.

### Request

```
curl -v 'https://developer.api.autodesk.com/data-connector/v1/accounts/:accountId/requests' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "description": "My Company Data Extract", "isActive": true, "scheduleInterval": "ONE_TIME", "reoccuringInterval": null, "effectiveFrom": "2020-11-06T19:09:40.106Z", "effectiveTo": "2020-11-12T19:09:40.106Z", "serviceGroups": [ "admin", "issues" ], "callbackUrl": "https://api.mycompany.com/autodesk/jobinfo", "sendEmail": true, "projectId": null, "projectIdList": "[ \"ffffffff-1f51-4b26-a6b7-6ac0639cb138\", \"aaaaaaaa-1f51-4b26-a6b7-6ac0639cb138\" ]", "startDate": "2023-06-06T00:00:00.000Z", "endDate": "2023-06-06T12:00:00.000Z", "dateRange": "LAST_MONTH", "projectStatus": "active" }'
```

### Response

```
{ "id" : "ce9bc188-1e18-11eb-adc1-0242ac120002" , "description" : "My Company Data Extract" , "isActive" : true , "accountId" : "f9abf4c8-1f51-4b26-a6b7-6ac0639cb138" , "projectId" : null , "projectIdList" : "[ \"ffffffff-1f51-4b26-a6b7-6ac0639cb138\", \"aaaaaaaa-1f51-4b26-a6b7-6ac0639cb138\" ]" , "createdBy" : "ABCDEFGHI" , "createdByEmail" : "joe.user@mycompany.com" , "createdAt" : "2020-11-06T19:09:40.106Z" , "updatedBy" : "ABCDEFGHI" , "updatedAt" : "2020-11-06T19:09:40.106Z" , "scheduleInterval" : "ONE_TIME" , "reoccuringInterval" : null , "effectiveFrom" : "2020-11-06T19:09:40.106Z" , "effectiveTo" : "2020-11-12T19:09:40.106Z" , "lastQueuedAt" : null , "serviceGroups" : [ "admin" , "issues" ], "callbackUrl" : "https://api.mycompany.com/autodesk/jobinfo" , "sendEmail" : true , "startDate" : "2023-06-06T00:00:00.000Z" , "endDate" : "2023-06-06T12:00:00.000Z" , "dateRange" : "LAST_MONTH" , "projectStatus" : "active" }
```
