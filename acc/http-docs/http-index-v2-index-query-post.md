# projects/:projectId/indexes/:indexId/queries

Source: https://aps.autodesk.com/en/docs/acc/reference/http/index-v2-index-query-post/

---

Index

POST

# projects/:projectId/indexes/:indexId/queries

Applies the given query on the given properties index.

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/index/v2/projects/:projectId/indexes/:indexId/queries |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | json |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json`. |
| x-ads-force-regenerate-cache   boolean | If set to true, force regeneration of S3 cache. |
| x-ads-region   enum: string | The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. <br>Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The project ID. |
| --- | --- |
| indexId   string | The index ID. |

### Request

## [Body Structure](#body-structure)

| query*   object | [SQL AST for binary expression/filter](../how-to-docs/model-properties-query-ref.md) |
| --- | --- |
| columns   object | [SQL AST for describing columns/projections](../how-to-docs/model-properties-query-ref.md) |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Success |
| --- | --- |
| 401   Unauthorized | Response in case of an error. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 415   Unsupported Media Type | The `Content-Type` header must be `application/json`. |
| 429   Too Many Requests | Rate limit exceeded. Wait some time before retrying. The `Retry-After` header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| projectId   string | project id. |
| --- | --- |
| indexId   string | index id. |
| queryId   string | query id. |
| type   enum: string | type. <br>Possible values: `INDEX` |
| state   enum: string | job status. <br>Possible values: `PROCESSING`, `FINISHED`, `FAILED` |
| selfUrl   string | unique url for this indexing job status. |
| versionUrns   array: string | list all versions this index depends upon. |
| updatedAt   datetime: ISO 8601 | timestamp. |
| retryAt   datetime: ISO 8601 | timestamp. |
| stats   object | some higher level index statistics. |
| objects   int | number of objects contained in the properties index. |
| manifestUrl   string | url for downloading the index manifest. |
| fieldsUrl   string | url for downloading the index fields. |
| propertiesUrl   string | url for downloading the index properties. |
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

## [Example](#example)

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/index/v2/projects/cd743656-f130-48bd-96e6-948175313637/indexes/da39a3ee5e6b4b0d/queries' \
     -X POST \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "query": {
             " $not ": [
               {
                 " s.p123 ": "17"
               },
               {
                 " s.pabc ": " '\''Hello'\'' "
               }
             ]
           },
           "columns": {
             "a": {
               "$date_add": [
                 "YEAR",
                 "5",
                 "'\''2010-01-01T'\''"
               ]
             },
             "b": {
               "$mul": [
                 {
                   "$add": [
                     "5",
                     "s.p789"
                   ]
                 },
                 "10"
               ]
             },
             "s.svf2Id": "true"
           }
         }'

```

Show More

### Response (200)

```
{
  "projectId": "some_project_id",
  "indexId": "4e34bb65ae12",
  "queryId": "90756abcefd2",
  "type": "INDEX",
  "selfUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/some_project_id/indexes/4e34bb65ae12/queries/90756abcefd2",
  "versionUrns": [
    "some_version_urn"
  ],
  "updatedAt": "2020-09-18T07:44:04.946Z",
  "state": "FINISHED",
  "stats": {
    "objects": "345678"
  },
  "manifestUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/some_project_id/indexes/4e34bb65ae12/manifest",
  "fieldsUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/some_project_id/indexes/4e34bb65ae12/fields",
  "propertiesUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/some_project_id/indexes/4e34bb65ae12/properties",
  "queryResultsUrl": "https://developer.api.autodesk.com/construction/index/v2/projects/some_project_id/indexes/4e34bb65ae12/queries/90756abcefd2/properties"
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
