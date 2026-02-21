# containers/:containerId/modelsets/:modelSetId/versions

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-modelset-service-v3-get-model-set-versions-GET/

---

Model Set: Versions

GET

# containers/:containerId/modelsets/:modelSetId/versions

Retrieves a list of versions of a given model set.

The response contains a list of model set versions, restricted by the number specified by the `pageLimit` property. If set (that is, if there are more results than can be displayed at once), you can provide the `continuationToken` property in the response in a separate call to retrieve additional results.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/bim360/modelset/v3/containers/:containerId/modelsets/:modelSetId/versions |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token/) OAuth flow. |
| --- | --- |
| x-ads-region   enum: string | The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. <br>Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](/en/docs/acc/v1/overview/acc-regions) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The GUID that uniquely identifies the container. |
| --- | --- |
| modelSetId   string: UUID | The GUID that uniquely identifies the model set. |

### Request

## [Query Parameters](#query-parameters)

| status   array: enum: string | The statuses to filter the model set versions. |
| --- | --- |
| pageLimit   int | The maximum number of model set versions to return in a page. If not set, the default page limit is used, as determined by the server. |
| continuationToken   string | The token indicating the start of the page. If not set, the first page is retrieved. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Success |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource could not be found. |
| 429   Too Many Requests | Rate limit exceeded; wait some time before retrying. The `Retry-After` header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| page   object | Paging information associated with a paging response. |
| --- | --- |
| continuationToken   string | A continuation token to retrieve the next page. |
| modelSetVersions   array: object | List of model set version summaries. |
| version   int | The model set version number. |
| createTime   datetime: ISO 8601 | The date and time that the model set version was created. |
| status   enum: string | The creation status of the model set version. Possible values: `Pending`, `Processing`, `Successful`, `Partial`, `Failed`. |

### Response

## [Body Structure (400)](#body-structure-400)

Expand all

| type   string | The error code. |
| --- | --- |
| title   string | A short title for the error. |
| detail   string | A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. |
| errors   array: object | A set of specific validation errors that need to be fixed. |
| field   string | The field which failed validation. |
| title   string | A short title for the error. |
| detail   string | A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. |
| type   string | The error code. |

## [Example #1 (no query parameters)](#example-1-no-query-parameters)

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/modelsets/00fb28a5-e8a4-2755-562a-7c2f0fc87911/versions' \
     -H 'Authorization: Bearer <token>'

```

## [Example #2 (with all query parameters)](#example-2-with-all-query-parameters)

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/modelsets/00fb28a5-e8a4-2755-562a-7c2f0fc87911/versions?status=Successful&pageLimit=134&continuationToken=10' \
     -H 'Authorization: Bearer <token>'

```

### Response (200)

```
{
  "page": {
    "continuationToken": "10"
  },
  "modelSetVersions": [
    {
      "version": 42,
      "createTime": "2015-10-21T16:29:30Z",
      "status": "Successful"
    }
  ]
}

```

Show More

### Response (400)

```
{
  "type": "BadInput",
  "title": "One or more input values in the request were bad",
  "detail": "The following parameters are invalid: containerId",
  "errors": [
    {
      "field": "containerId",
      "title": "Invalid parameter",
      "detail": "The value 'testing' is not valid.",
      "type": "BadInput"
    }
  ]
}

```

Show More
