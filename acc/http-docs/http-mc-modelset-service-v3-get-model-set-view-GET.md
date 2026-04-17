# containers/:containerId/modelsets/:modelSetId/views/:viewId

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-modelset-service-v3-get-model-set-view-GET/

---

Model Set: Views

GET

# containers/:containerId/modelsets/:modelSetId/views/:viewId

Retrieves a specific model set view based on the view ID.

Returns the requested model set view object.

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/bim360/modelset/v3/containers/:containerId/modelsets/:modelSetId/views/:viewId |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-ads-region   enum: string | The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. <br>Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The GUID that uniquely identifies the container. |
| --- | --- |
| modelSetId   string: UUID | The GUID that uniquely identifies the model set. |
| viewId   string: UUID | The GUID that uniquely identifies the view. |

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

| name   string | The name of the model set view. Min length: 1 Max length: 64. |
| --- | --- |
| description   string | The description of the model set view. Min length: 1 Max length: 1024. |
| isPrivate   boolean | Determines whether the view is only accessible to its creator. |
| definition   array: object | The definition of models in a model set view, which is used to track the same models through time. Min items: 1 Max items: 1000. |
| lineageUrn   string | The lineage URN of the seed file or document lineage to track with this view. Min length: 1 Max length: 80. |
| viewableName   string | The name of the viewable in the Model Derivative manifest to track along the seed file lineage. This value is ignored if `lineageUrn` is the URN of a BIM360 Docs Plans folder document. Min length: 1 Max length: 430. |
| viewId   string: UUID | The GUID that uniquely identifies the view. |
| createdBy   string | The ID of the user or service that created the view. |
| createdTime   datetime: ISO 8601 | The date and time that the view was created. |
| modifiedBy   string | The ID of the user or service that last modified the view. |
| modifiedTime   datetime: ISO 8601 | The date and time that the view was last modified. |

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

## [Example](#example)

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/modelsets/00fb28a5-e8a4-2755-562a-7c2f0fc87911/views/7ed27144-ac06-4b72-5dd6-76bee05854be' \
     -H 'Authorization: Bearer <token>'

```

### Response (200)

```
{
  "name": "L1 - All disciplines",
  "description": "All discipline models for Level 1",
  "isPrivate": false,
  "definition": [
    {
      "lineageUrn": "urn:adsk.wipprod:dm.lineage:jvMF7mrHR7OwG_DToKsJUA",
      "viewableName": "Level 1"
    }
  ],
  "viewId": "7ed27144-ac06-4b72-5dd6-76bee05854be",
  "createdBy": "PD23PXGV8V3V",
  "createdTime": "2015-10-21T16:31:44Z"
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
