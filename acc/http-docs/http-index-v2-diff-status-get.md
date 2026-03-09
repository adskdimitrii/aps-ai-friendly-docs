# projects/:projectId/diffs/:diffId

Source: https://aps.autodesk.com/en/docs/acc/reference/http/index-v2-diff-status-get/

---

Diff

GET

# projects/:projectId/diffs/:diffId

Retrieve the diff status for the given diff ID. Depending on the state different properties might be present or missing. E.g., if the diff job is not finished yet, the manifest, fields, and properties links might be missing, but the retryAt property will be present. If the processing failed for some reason, the errors property will contain some information. Once the final result of the diff job has been determined (either finished or failed), the status is assumed to be immutable and the response will set a long expiration HTTP header for efficient client side caching.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/index/v2/projects/:projectId/diffs/:diffId |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | json |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-ads-region   enum: string | The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. <br>Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The project ID. |
| --- | --- |
| diffId   string | The diff ID. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Success |
| --- | --- |
| 401   Unauthorized | Response in case of an error. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | Response in case of an not found error. |
| 429   Too Many Requests | Rate limit exceeded. Wait some time before retrying. The `Retry-After` header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| projectId   string | project id. |
| --- | --- |
| diffId   string | diff id. |
| queryId   string | query id. |
| type   enum: string | type. <br>Possible values: `DIFF` |
| state   enum: string | job status. <br>Possible values: `PROCESSING`, `FINISHED`, `FAILED` |
| selfUrl   string | unique url for this job status. |
| prevVersionUrns   array: string | The previous file versions used in this index. |
| curVersionUrns   array: string | The current file versions used in this index. |
| updatedAt   datetime: ISO 8601 | timestamp. |
| retryAt   datetime: ISO 8601 | timestamp. |
| stats   object | some higher level diff statistics. |
| added   int | number of objects added. |
| removed   int | number of objects removed. |
| modified   int | number of objects modified. |
| manifestUrl   string | url for downloading the diff manifest. |
| fieldsUrl   string | url for downloading the diff fields. |
| propertiesUrl   string | url for downloading the diff properties. |
| queryResultsUrl   string | url for downloading the query result. |
| errors   array: object | errors. |
| type   string | The error code. |
| title   string | A short title for the error. |
| detail   string | A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. |
| errors   array: object | A set of specific validation errors that need to be fixed. |
| field   string | The field which failed validation. |
| title   string | A short title for the error. |
| detail   string | A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. |
| type   string | The error code. |

### Response

## [Body Structure (401)](#body-structure-401)

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

### Response

## [Body Structure (404)](#body-structure-404)

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

## [Example](#example)

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/index/v2/projects/cd743656-f130-48bd-96e6-948175313637/diffs/3fe13864aecfe0a5' \
     -H 'Authorization: Bearer <token>'

```

### Response (200)

```
{
  "projectId": "some_project_id",
  "diffId": "fe34bb65aeef",
  "queryId": "4af40764ae14",
  "type": "DIFF",
  "selfUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/some_project_id/diffs/fe34bb65aeef/queries/4af40764ae14",
  "prevVersionUrns": [
    "some_version_urn_1"
  ],
  "curVersionUrns": [
    "some_version_urn_2"
  ],
  "updatedAt": "2020-09-18T07:44:04.946Z",
  "state": "FINISHED",
  "stats": {
    "added": "15",
    "removed": "10",
    "modified": "42"
  },
  "manifestUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/some_project_id/diffs/fe34bb65aeef/manifest",
  "fieldsUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/some_project_id/diffs/fe34bb65aeef/fields",
  "propertiesUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/some_project_id/diffs/fe34bb65aeef/properties",
  "queryResultsUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/some_project_id/diffs/fe34bb65aeef/queries/4af40764ae14/properties"
}

```

Show More

### Response (401)

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

### Response (404)

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
