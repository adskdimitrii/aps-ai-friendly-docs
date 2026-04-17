# accounts/{accountId}/jobs/{jobId}/data/{name}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/data-connector-jobs-jobId-data-name-GET/

---

Data

GET

# accounts/{accountId}/jobs/{jobId}/data/{name}

Returns a signed URL that you can contact to retrieve a single specified file from a specified job’s data extract. You can examine a data extract’s available files, their names, and their sizes using [GET jobs/:jobId/data-listing](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/data-connector-jobs-jobid-data-listing-GET/). The information it returns can help you plan what you would like to retrieve using this endpoint, useful if you want to retrieve only part of a data extract to avoid downloading large but unnecessary files. The user must have executive overview or project administrator permissions.

Each data extract contains three types of files:

- One CSV file for each service group specified for the data extract. Each CSV file contains all the data returned for that service group. The data is in CSV format.
- A README file that lists the CSV files and describes in detail the schema used for each CSV file.
- A master ZIP file that contains all of the CSV files and the accompanying README file.

To retrieve the entire data extract, use this endpoint to retrieve the ZIP file. If you don’t know the schema for the CSV files in the data extract, retrieve the README file for detailed schema descriptions. You can also use this endpoint to retrieve a single CSV file without retrieving the rest of the data extract’s CSV files.

The secure signed URL this endpoint returns is valid for 60 seconds. If you don’t request data from the URL within that time, the URL no longer works. Once you’ve requested data, though, the download can take as long as necessary.

To get job IDs for a request, use [GET requests/:requestId/jobs](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/data-connector-requests-requestid-jobs-GET/).

To understand the basics of requests, the jobs they spawn, and the data extracts returned by the jobs, see the [Data Connector API Field Guide](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/data-connector/).

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/data-connector/v1/accounts/:accountId/jobs/:jobId/data/:name |
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
| jobId   string: UUID | The job ID |
| name   string: UUID | Name of the file to retrieve |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully set up a job extract file for retrieval from a returned signed URL |
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

| size   int | The size of the file in bytes. |
| --- | --- |
| name   string | The name of the file. |
| signedUrl   string | The signed URL to contact to download the specified file. Note that this URL will be valid for 60 seconds from the time of this response. |

## [Example](#example)

Successfully set up a job extract file for retrieval from a returned signed URL

### Request

```
curl -v 'https://developer.api.autodesk.com/data-connector/v1/accounts/:accountId/jobs/:jobId/data/:name' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "size": "123456",
  "name": "admin_companies.csv",
  "signedUrl": "https://bim360dc-p-ue1-extracts.s3.amazonaws.com/data/9be6b2cd-e9e8-4861-aa45-c96668a9f6bd/d023d0cf-b603-4de9-b240-a0e8a85bbf8d/autodesk_data_extract.zip?AWSAccessKeyId=ASIAWZ7KRFT5TZSCKIYO&Expires=1604690406&Signature=cb5HR%2FthOATYIAqW41ojbfptMsM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIHQdYa9Z%2BhS3u5EmRfEoz1KFwm2xCvLK6pH1Go2q88%2BWAiEAy7KMbb%2FKBww1XWxR0B%2FepB0Syt6jOhXTahznLrCWKcYq2gEIHBACGgw0NjgxMDY0MjM1NDciDHewqYuFoS8GY2PlZCq3AZG8jsIKx5egqYARC2N%2F7%2B72nkATTV6PwomhMOsAb9eZhIBCR%2F861wvtM1%2B4gEfu8LN9gWMNI%2BvmHcWC92kC1lujXM1Klpq8KksSxN8%2Bt5aurFPwZ465iespRnEHKB7jX2KUzCVDPCpZ7NDTvcsy0TdqLU82L0p%2Bw6fTT0QhGuykRuhn%2FURLbtzVHvx4wi3R2kSEJ9DWGkAaWR96h76vCFDaC9o2VmLEjKww88YunnYKQcAqIhGEBTD2vpb9BTrgAVGy7Cavc8LDgwuoS7LBt%2FmE6iPohyfILcksPL5NYl3yvaUhYW%2FX9w1mgLgpnuEt4rcdcrUOTcOdjRFmqvA9%2FVPFXD%2FCWxzDRU6V3U%2BC1dZi5Y4lV3AfodZyhsJI9aSkX2D0xDMpuV%2FDiX0HyCCVk3awuCQDfPtlWqbMVzW9zzO5d6JBThIIxdEGq1Nwe677anh1WQGY%2Fuemcc4fyZRTx%2Br0i%2B8Z35YtR0pEKfvp7GQhV7d%2FSfh%2FYL58QMvvciH4yBqkcMba8SwDJQQV03Q%2FrQX2vqVOq%2BSFCijaXalvPjQp"
}

```
