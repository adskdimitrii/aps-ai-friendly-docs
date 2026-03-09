# accounts/{accountId}/jobs/{jobId}/data-listing

Source: https://aps.autodesk.com/en/docs/acc/reference/http/data-connector-jobs-jobId-data-listing-GET/

---

Data

GET

# accounts/{accountId}/jobs/{jobId}/data-listing

Returns an array of information about the files contained within the data extract created by a specified job. The job must be spawned by a data request that was created by the authenticated user. The user must have executive overview or project administrator permissions.

The array provides a name, creation date, and size for each file in the data extract. You can retrieve any or all of the files using [GET jobs/:jobId/data/:name](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/data-connector-jobs-jobid-data-name-GET/). Its reference page describes the file types within a data extract.

If the job was cancelled or otherwise failed to create a data extract, this endpoint returns a 404 error âThe requested resource does not exist.â

To get job IDs for a request, use [GET requests/:requestId/jobs](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/data-connector-requests-requestid-jobs-GET/).

To understand the basics of requests, the jobs they spawn, and the data extracts returned by the jobs, see the [Data Connector API Field Guide](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/data-connector/).

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/data-connector/v1/accounts/:accountId/jobs/:jobId/data-listing |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
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

| 200   OK | Successfully returned an array of information about data extract files for the specified job. |
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

| name   string | The name of the file. |
| --- | --- |
| createdAt   datetime: ISO 8601 | The date and time the file was created, presented in ISO 8601 format. |
| size   int | The size of the file in bytes. |

## [Example](#example)

Successfully returned an array of information about data extract files for the specified job.

### Request

```
curl -v 'https://developer.api.autodesk.com/data-connector/v1/accounts/:accountId/jobs/:jobId/data-listing' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
[
  {
    "name": "admin_companies.csv",
    "createdAt": "2020-11-06T19:09:40.106Z",
    "size": "123456"
  }
]

```
