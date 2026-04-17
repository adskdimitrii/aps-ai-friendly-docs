# accounts/{accountId}/requests

Source: https://aps.autodesk.com/en/docs/acc/reference/http/data-connector-requests-GET/

---

Requests

GET

# accounts/{accountId}/requests

Returns an array of data requests that the authenticated user has created in the specified hub. The user must have executive overview or project administrator permissions.

Returned information for each request in the array includes the request ID, information about when the request was created, the attribute values defined by the request, and when the last and next job spawned by the request has occurred and will occur.

To understand the basics of requests, the jobs they spawn, and the data extracts returned by the jobs, see the [Data Connector API Field Guide](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/data-connector/).

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/data-connector/v1/accounts/:accountId/requests |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). <br>The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| accountId   string: UUID | The ID of the hub. To obtain the hub ID, call [GET hubs](../../data/http-docs/http-hubs-GET.md) in the Data Management API and remove the “b.” prefix. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| sort   string | The sort order of returned data connector objects. Possible values: `asc` ascending by date (earliest to latest date), `desc` descending by date (latest to earliest date). |
| --- | --- |
| limit   int | The number of data connector objects to return. Default value: 20 |
| offset   int | The number of data objects to skip before starting to starting to collect the result set. Default value: 0 |
| sortFields   string | A string of comma-separated names of the fields by which to sort the returned data requests. The results are sorted by the first field, then by the second field, and so on. Requests are sorted by each field in ascending order by default; you can prepend any field name with a hyphen ( `-` ) to sort in descending order. Invalid fields and whitespaces are ignored. <br>Possible values: `isActive`, `accountId`, `createdBy`, `createdByEmail`, `createdAt`, `updatedBy`, `updatedAt`, `scheduleInterval`, `reoccuringInterval`, `effectiveFrom`, `effectiveTo`, `startDate`, `endDate`. |
| filter[field_to_filter]   string | Return only the data requests in which the specified field has the specified value. Use the following format in the endpoint URL: `filter[field_to_filter]=_filter_value_`. <br>Note that you can provide multiple request filters in the URL, but you may not filter on multiple values of the same field.<br>Possible `field_to_filter` values: `projectId`, `createdAt`, `updatedAt`, `scheduleInterval`, `reocurringInterval`, `effectiveFrom`, `effectiveTo`, `isActive`, `startDate`, `endDate`. You can also retrieve all data requests in the current hub by specifying `filter[projectId]=null`.<br>For the `createdAt` and `updatedAt` fields (which accept a date range), specify the range in the form *firstdate..lastdate*, in ISO 8601 format with the time required. You can alternatively omit the first date (for example, to get everything on or before June 1, 2019 the range would be `..2019-06-01T23:59:59.999Z`). You can also omit the last date (for example, to get everything after June 1, 2019 the range would be `2019-06-01T00:00:00.000Z..`)<br>Additional notes on using `startDate` and `endDate`:<br>If you provide only `startDate` or `endDate` (but not both), Data Connector uses that single date for both `startDate` and `endDate`.If you request more than the Maximum Date Range Allowed for an extraction, the default date range as documented in the schema documentation is returned.For the `activities` service group, data replication can be delayed up to 20 minutes, so your requests should account for that delay. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved an array of data requests. |
| --- | --- |
| 400   Bad Request | The parameters are invalid. |
| 401   Unauthorized | The provided bearer token is invalid. |
| 403   Forbidden | Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The resource or endpoint cannot be found. |
| 429   Too Many Requests | Rate limited exceeded; wait some time before retrying. |
| 500   Internal Server Error | An unexpected error occurred on the server. |
| 503   Service Unavailable | Service unavailable. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| pagination   object | Information about the pagination used to return the results array. |
| --- | --- |
| limit   int | The specified upper limit of results to return. |
| offset   int | The specified number of results skipped before the results in this array were collected. |
| totalResults   int | The total number of results returned here. |
| results   array: object | The returned array of data request records. |
| id   string: UUID | The ID of the data request. |
| description   string | The user-entered description of this data request. If not supplied, the default value is a null string. |
| isActive   boolean | The data request’s active/inactive status. Possible values: `true` the request is active; `false` the request is inactive. |
| accountId   string: UUID | The hub ID. |
| projectId   string: UUID | (Legacy): A single project ID for the data request. Superseded by `projectIdList`. |
| projectIdList   array: string | A list of up to 50 project IDs included in the data request. This field contains the project IDs for which data is being extracted. If both `projectId` and `projectIdList` were included in the request, this field contains the values from `projectIdList`. |
| createdBy   string | The BIM 360 / Forma user ID of the user who created the data request. |
| createdByEmail   string | The email address of the user who created the data request. |
| createdAt   datetime: ISO 8601 | The date and time the data request was created, presented in ISO 8601 format. |
| updatedBy   string | The BIM 360 / Forma user ID of the user who last updated the data request. |
| updatedAt   datetime: ISO 8601 | The date and time the data request was last updated, presented in ISO 8601 format. |
| scheduleInterval   string | The scheduling interval unit for jobs spawned by this data request. This value is multiplied by the `reoccurringInterval` attribute to specify the length of the recurring interval at which jobs run. Possible values: <br>`ONE_TIME`: Run the job only once`DAY`: Set the recurring job interval in days`WEEK`: Set the recurring job interval in weeks`MONTH`: Set the recurring job interval in months`YEAR`: Set the recurring job interval in years |
| reoccuringInterval   int | The number of `scheduleInterval` units to wait between job execution for the request. For example, a `scheduleInterval` value of `WEEK` and a `reoccuringInterval` value of `2` means the job will run every two weeks. |
| effectiveFrom   datetime: ISO 8601 | The date and time when a one-time job execution or a recurring interval schedule begins, presented in ISO 8601 format. |
| effectiveTo   datetime: ISO 8601 | The date and time when the recurring interval schedule ends, presented in ISO 8601 format. |
| lastQueuedAt   datetime: ISO 8601 | The date and time the last job for this data request was scheduled to execute, presented in ISO 8601 format. |
| serviceGroups   array: string | The service groups from which data has been extracted, separated by commas. <br>Possible values: `all`, `activities`, `admin`, `assets`, `checklists`, `cost`, `dailylogs`, `forms`, `iq`, `issues`, `locations`, `markups`, `meetingminutes`, `photos`, `relationships`, `reviews`, `rfis`, `schedule`, `sheets`, `submittals`, `submittalsacc`, `transmittals`.<br>Note that the `admin` service includes both project and hub admin, and `all` indicates that the extract contains all currently available service groups. |
| callbackUrl   string | The callback URL specified for the data request. If specified, the Data Connection service calls the URL each time a job executes for the request. The service sends a POST request that provides job execution information. The JSON payload in the POST request contains the following: `{ "accountId": "account_id", "requestId": "request_id", "jobId": "data_connector_job_id", "state": "complete", "success": true or false }`. |
| sendEmail   boolean | Send a notification email to the user upon job completion. Values: true or false (default is true) |
| startDate   string | The start date and time for the data extraction, in ISO 8601 format. <br>This field applies only to schemas supporting date range extraction. The detailed schema documentation delivered with each data extract identifies the schemas and tables that support date range extraction.<br>Additional notes on using `startDate` and `endDate`:<br>If you provide only `startDate` or `endDate` (but not both), Data Connector uses that single date for both `startDate` and `endDate`.If you request more than the Maximum Date Range Allowed for an extraction, the default date range as documented in the schema documentation is returned.For the `activities` service group, data replication can be delayed up to 20 minutes, so your requests should account for that delay. |
| endDate   string | The end date and time for the data extraction, in ISO 8601 format. <br>This field applies only to schemas supporting date range extraction. The detailed schema documentation delivered with each data extract identifies the schemas and tables that support date range extraction.<br>Additional notes on using `startDate` and `endDate`:<br>If you provide only `startDate` or `endDate` (but not both), Data Connector uses that single date for both `startDate` and `endDate`.If you request more than the Maximum Date Range Allowed for an extraction, the default date range as documented in the schema documentation is returned.For the `activities` service group, data replication can be delayed up to 20 minutes, so your requests should account for that delay. |
| dateRange   string | The timeframe used for extracting data in the request. Currently, it is applicable only to the Activities service. This field contains the value specified in the request, indicating the range of data included in the response. Possible values: <br>`TODAY`: Data for the current day (from 00:00 UTC to the time the request was made).`YESTERDAY`: Data for the previous calendar day (from 00:00 UTC to 23:59 UTC).`PAST_7_DAYS`: Data for the last 7 days, including the current day.`MONTH_TO_DATE`: Data from the start of the current calendar month (00:00 UTC on the 1st) to the time the request was made.`LAST_MONTH`: Data for the entire previous calendar month (00:00 UTC on the 1st to 23:59 UTC on the last day). |
| projectStatus   string | The types of projects to be included in a request. The possible values are: <br>`all`: - all projects (default)`archived`: archived projects only`active`: active project only |

## [Example](#example)

Successfully retrieved an array of data requests.

### Request

```
curl -v 'https://developer.api.autodesk.com/data-connector/v1/accounts/:accountId/requests?sort=asc&limit=20&offset=0&sortFields=createdByEmail,-createdAt&filter[field_to_filter]=_filter_value_' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 20,
    "offset": 0,
    "totalResults": 100
  },
  "results": [
    {
      "id": "ce9bc188-1e18-11eb-adc1-0242ac120002",
      "description": "My Company Data Extract",
      "isActive": true,
      "accountId": "f9abf4c8-1f51-4b26-a6b7-6ac0639cb138",
      "projectId": null,
      "projectIdList": "[ \"ffffffff-1f51-4b26-a6b7-6ac0639cb138\", \"aaaaaaaa-1f51-4b26-a6b7-6ac0639cb138\" ]",
      "createdBy": "ABCDEFGHI",
      "createdByEmail": "joe.user@mycompany.com",
      "createdAt": "2020-11-06T19:09:40.106Z",
      "updatedBy": "ABCDEFGHI",
      "updatedAt": "2020-11-06T19:09:40.106Z",
      "scheduleInterval": "ONE_TIME",
      "reoccuringInterval": null,
      "effectiveFrom": "2020-11-06T19:09:40.106Z",
      "effectiveTo": "2020-11-12T19:09:40.106Z",
      "lastQueuedAt": null,
      "serviceGroups": [
        "admin",
        "issues"
      ],
      "callbackUrl": "https://api.mycompany.com/autodesk/jobinfo",
      "sendEmail": true,
      "startDate": "2023-06-06T00:00:00.000Z",
      "endDate": "2023-06-06T12:00:00.000Z",
      "dateRange": "LAST_MONTH",
      "projectStatus": "active"
    }
  ]
}

```

Show More
