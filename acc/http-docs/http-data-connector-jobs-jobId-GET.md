# accounts/{accountId}/jobs/{jobId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/data-connector-jobs-jobId-GET/

---

Jobs

GET

# accounts/{accountId}/jobs/{jobId}

Returns information about a specified job that was spawned by a data request created by the authenticated user. The user must have project administrator or executive overview permissions.

Returned information includes the job ID, the ID of its request, the ID of the account where the request was created, and the ID and email address of the user who created the request. It also includes information about when the job was created, when it was started and completed (if it has been), its completion status, and its current execution status.

To get job IDs for a request, use [GET requests/:requestId/jobs](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/data-connector-requests-requestid-jobs-GET/).

To understand the basics of requests, the jobs they spawn, and the data extracts returned by the jobs, see the [Data Connector API Field Guide](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/data-connector/).

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/data-connector/v1/accounts/:accountId/jobs/:jobId |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| accountId   string: UUID | The account ID. You can derive it from your hub ID if necessary: Use [GET hubs](../../data/http-docs/http-hubs-GET.md) in the Data Management API to retrieve your hub ID. Remove the initial âb.â from the hub ID to get your account ID. |
| --- | --- |
| jobId   string: UUID | The job ID |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved information about the specified job. |
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

| id   string: UUID | The job ID. |
| --- | --- |
| requestId   string: UUID | The ID of the data request that spawned the job. |
| accountId   string: UUID | The account ID. |
| projectId   string: UUID | The project ID. |
| projectIdList   array: string | The list of project IDs |
| createdBy   string | The BIM 360 / ACC user ID of the user who created the data request that spawned this job. |
| createdByEmail   string | The email address of the user who created the data request that spawned this job. |
| createdAt   datetime: ISO 8601 | The date and time the job was created, presented in ISO 8601 format. |
| status   string | The current status of the job. Possible values: `queued`, `running`, `complete`. |
| completionStatus   string | The completion status for completed jobs. Possible values: `success`, `failed`, `cancelled`. |
| startedAt   datetime: ISO 8601 | The date and time the job was started, presented in ISO 8601 format. If the job has not yet started, the value is null. |
| completedAt   datetime: ISO 8601 | The date and time the job was completed, presented in ISO 8601 format. If the job has not yet completed, the value is null. |
| sendEmail   boolean | Send a notification email when the job completes. |
| progress   int | Job progress indicator (0 to 100 percent) |
| lastDownloadedBy   string | The ID of the user who last downloaded this job data. |
| lastDownloadedAt   datetime: ISO 8601 | The last date and time that a user downloaded this job data, in ISO 8601 format. |
| startDate   string | The start date and time for the data extraction, in ISO 8601 format. <br>This field applies only to schemas that support date range extraction. The detailed schema documentation delivered with each data extract identifies the schemas and tables that support date range extraction. |
| endDate   string | The end date and time for the data extraction, in ISO 8601 format. <br>This field applies only to schemas that support date range extraction. The detailed schema documentation delivered with each data extract identifies the schemas and tables that support date range extraction. |

## [Example](#example)

Successfully retrieved information about the specified job.

### Request

```
curl -v 'https://developer.api.autodesk.com/data-connector/v1/accounts/:accountId/jobs/:jobId' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "id": "ce9bc188-1e18-11eb-adc1-0242ac120002",
  "requestId": "a5a8e90f-3dbe-4b08-9b8e-16e8049ce31e",
  "accountId": "f9abf4c8-1f51-4b26-a6b7-6ac0639cb138",
  "projectId": null,
  "projectIdList": "[ \"ffffffff-1f51-4b26-a6b7-6ac0639cb138\", \"aaaaaaaa-1f51-4b26-a6b7-6ac0639cb138\" ]",
  "createdBy": "ABCDEFGHI",
  "createdByEmail": "joe.user@mycompany.com",
  "createdAt": "2020-11-06T19:09:40.106Z",
  "status": "complete",
  "completionStatus": "success",
  "startedAt": "2020-11-06T19:10:00.106Z",
  "completedAt": "2020-11-06T19:29:40.106Z",
  "sendEmail": true,
  "progress": "",
  "lastDownloadedBy": "joe.user@mycompany.com",
  "lastDownloadedAt": "2021-11-06T19:09:40.106Z",
  "startDate": "2023-06-06T00:00:00.000Z",
  "endDate": "2023-06-06T12:00:00.000Z"
}

```

Show More
