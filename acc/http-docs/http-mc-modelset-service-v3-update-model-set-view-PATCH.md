# containers/:containerId/modelsets/:modelSetId/views/:viewId

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-modelset-service-v3-update-model-set-view-PATCH/

---

Model Set: Views

PATCH

# containers/:containerId/modelsets/:modelSetId/views/:viewId

Updates a specific model set view.

- If `oldName` and `newName` are supplied, the name is updated (both must be supplied, the name cannot be null)
- If `oldDescription` or `newDescription` is supplied, the description is updated (one can be null or omitted, description can be set to null)
- If `oldIsPrivate` and `newIsPrivate` are supplied, the privacy of the view is updated (both must be supplied)
- If `oldDefinition` and `newDefinition` are supplied, the view definition is updated (both must be supplied)

If no property changes are supplied, an error is returned.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/bim360/modelset/v3/containers/:containerId/modelsets/:modelSetId/views/:viewId |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token/) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| x-ads-region   enum: string | The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. <br>Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](/en/docs/acc/v1/overview/acc-regions) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The GUID that uniquely identifies the container. |
| --- | --- |
| modelSetId   string: UUID | The GUID that uniquely identifies the model set. |
| viewId   string: UUID | The GUID that uniquely identifies the view. |

### Request

## [Body Structure](#body-structure)

Expand all

| oldName   string | The current name of the view. Min length: 1 Max length: 64. |
| --- | --- |
| newName   string | The new name of the view. Min length: 1 Max length: 64. |
| oldDescription   string | The current description of the view. Min length: 1 Max length: 1024. |
| newDescription   string | The new description of the view. Min length: 1 Max length: 1024. |
| oldIsPrivate   boolean | Determines whether the view is only accessible to its creator. |
| newIsPrivate   boolean | Determines whether the view is only accessible to its creator. |
| oldDefinition   array: object | The old definition of models in a model set view, which is used to track the same models through time. Min items: 1 Max items: 1000. |
| lineageUrn*   string | The lineage URN of the seed file or document lineage to track with this view. Min length: 1 Max length: 80. |
| viewableName   string | The name of the viewable in the Model Derivative manifest to track along the seed file lineage. This value is ignored if `lineageUrn` is the URN of a BIM360 Docs Plans folder document. Min length: 1 Max length: 430. |
| newDefinition   array: object | The new definition of models in a model set view, which is used to track the same models through time. Min items: 1 Max items: 1000. |
| lineageUrn*   string | The lineage URN of the seed file or document lineage to track with this view. Min length: 1 Max length: 80. |
| viewableName   string | The name of the viewable in the Model Derivative manifest to track along the seed file lineage. This value is ignored if `lineageUrn` is the URN of a BIM360 Docs Plans folder document. Min length: 1 Max length: 430. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 202   Accepted | The request has been accepted for processing, but the processing has not been completed. |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource could not be found. |
| 415   Unsupported Media Type | The `Content-Type` header must be `application/json`. |
| 429   Too Many Requests | Rate limit exceeded; wait some time before retrying. The `Retry-After` header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (202)](#body-structure-202)

Expand all

| jobId   string: UUID | The GUID that uniquely identifies the job. |
| --- | --- |
| viewId   string: UUID | The GUID that uniquely identifies the view associated with the job. |
| status   enum: string | The current job status. Possible values: `Failed`, `Running`, `Succeeded`, `Archived`. |
| job   object | A job. |
| operation   string | The operation associated with the job. |
| seed   object | The JSON payload which seeded the job. |

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
     -X PATCH \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "oldIsPrivate": true,
           "newIsPrivate": false
         }'

```

Show More

### Response (202)

```
{
  "jobId": "49244371-ee08-9afa-01f8-26fcd8ecb03d",
  "viewId": "7ed27144-ac06-4b72-5dd6-76bee05854be",
  "status": "Succeeded",
  "job": {
    "operation": "OperationName",
    "seed": {}
  }
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
