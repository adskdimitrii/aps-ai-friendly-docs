# containers/:containerId/tests/:testId/clashes:close

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-clash-service-v3-add-closed-clash-group-batch-POST/

---

Clash Test: Closed Clash Groups

POST

# containers/:containerId/tests/:testId/clashes:close

Adds a batch of new closed clash groups to the given clash test.

Clash groups that are closed are not presented should they occur in subsequent clash tests. The clash is still present in the model; it is not necessary to remove it.

The response contains information about the created clash group job.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/bim360/clash/v3/containers/:containerId/tests/:testId/clashes:close |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:create`, `data:write` |
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
| testId   string: UUID | The GUID that uniquely identifies the clash test. |

### Request

## [Body Structure](#body-structure)

| id   string: UUID | The unique identifier of the new closed clash group. |
| --- | --- |
| title*   string | The title of the new closed clash group. Max length: 128. |
| description   string | The description of the new closed clash group. Max length: 1024. |
| reason*   enum: string | The reason that the clash group is being closed. Possible values: `OTHER`, `VALID_INTERFACE`, `VALID_PENETRATION`, `MINIMAL_OVERLAP`, `ITEM_CAN_FLEX`, `MODEL_INACCURACY`, `FIELD_FIX`. |
| screenShots   array: string: UUID | The unique identifiers of screenshots to be associated with the new closed clash group. Max items: 5. |
| clashes*   array: int | The clashes to be included in the new closed clash group. Min items: 1 Max items: 1000. |

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
| groups   array: string: UUID | The GUIDs that uniquely identify the clash groups associated with the job. |
| createdIssueIds   array: string: UUID | If this job tracks the creation of assigned clashes, the IDs of the created issues. |
| status   enum: string | The current job status. Possible values: `Failed`, `Running`, `Succeeded`, `Archived`. |
| job   object | A job. |
| operation   string | The operation associated with the job. |
| seed   object | The JSON payload that seeded the job. |

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
curl -v 'https://developer.api.autodesk.com/bim360/clash/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/tests/c40b4498-1baa-405d-4fe9-423514bbbf10/clashes:close' \
     -X POST \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: application/json' \
     -d '[
           {
             "title": "Ceiling 2'\'' x 2'\'' grid and 411 other objects.",
             "description": "Objects expected in ceiling.",
             "reason": "OTHER",
             "screenShots": [
               "d98c1dd4-008f-04b2-e980-0998ecf8427e"
             ],
             "clashes": [
               2019963136
             ]
           }
         ]'

```

Show More

### Response (202)

```
{
  "jobId": "49244371-ee08-9afa-01f8-26fcd8ecb03d",
  "groups": [
    "d98c1dd4-008f-04b2-e980-0998ecf8427e"
  ],
  "status": "Succeeded",
  "job": {
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
