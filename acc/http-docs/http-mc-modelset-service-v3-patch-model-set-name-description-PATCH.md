# containers/:containerId/modelsets/:modelSetId

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-modelset-service-v3-patch-model-set-name-description-PATCH/

---

Model Set

PATCH

# containers/:containerId/modelsets/:modelSetId

Updates a given model set name and/or description.

- If `oldName` and `newName` are supplied, the name is updated (both must be supplied, the name cannot be null)
- If `oldDescription` or `newDescription` is supplied, the description is updated (one can be null or omitted, description can be set to null)

If no property changes are supplied, an error is returned.

If successful, the response contains information about the created model set job.

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/bim360/modelset/v3/containers/:containerId/modelsets/:modelSetId |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| x-ads-region   enum: string | The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. <br>Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The GUID that uniquely identifies the container. |
| --- | --- |
| modelSetId   string: UUID | The GUID that uniquely identifies the model set. |

### Request

## [Body Structure](#body-structure)

| oldName   string | The current name of the model set. Min length: 1 Max length: 64. |
| --- | --- |
| oldDescription   string | The current description of the model set. Min length: 1 Max length: 1024. |
| newName   string | The new name of the model set. This name must be unique within the specified container. Min length: 1 Max length: 64. |
| newDescription   string | The new description of the model set. Min length: 1 Max length: 1024. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 202   Accepted | OK |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource could not be found. |
| 409   Conflict | A Model Set with the specified newName already exists. |
| 415   Unsupported Media Type | The `Content-Type` header must be `application/json`. |
| 429   Too Many Requests | Rate limit exceeded; wait some time before retrying. The `Retry-After` header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (202)](#body-structure-202)

Expand all

| jobId   string: UUID | The GUID that uniquely identifies the job. |
| --- | --- |
| modelSetId   string: UUID | The GUID that uniquely identifies the model set associated with the job. |
| resource   string | The resource associated with the job. |
| createdIssueIds   array: string: UUID | If this job tracks the creation of model set inspection issues, the IDs of the created issues. |
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

### Response

## [Body Structure (409)](#body-structure-409)

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
curl -v 'https://developer.api.autodesk.com/bim360/modelset/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/modelsets/00fb28a5-e8a4-2755-562a-7c2f0fc87911' \
     -X PATCH \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "oldName": "Formal Coordination",
           "oldDescription": "Space for coordinating al disciplines",
           "newName": "Formal Coordination",
           "newDescription": "Space for coordinating all disciplines"
         }'

```

Show More

### Response (202)

```
{
  "jobId": "49244371-ee08-9afa-01f8-26fcd8ecb03d",
  "modelSetId": "00fb28a5-e8a4-2755-562a-7c2f0fc87911",
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

### Response (409)

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
