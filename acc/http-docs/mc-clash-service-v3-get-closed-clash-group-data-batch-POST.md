# containers/:containerId/tests/:testId/clashes/closed

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-clash-service-v3-get-closed-clash-group-data-batch-POST/

---

Clash Test: Closed Clash Groups

POST

# containers/:containerId/tests/:testId/clashes/closed

Retrieves the state of the specified closed clash groups, relative to a specified clash test.

This endpoint takes the clashes contained within each specified closed clash group, and intersects them with the results of the specified clash test. Clashes that were present when the clash group was first defined may have been resolved in this clash test.

The response contains a list of closed clash groups.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/bim360/clash/v3/containers/:containerId/tests/:testId/clashes/closed |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
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
| testId   string: UUID | The GUID that uniquely identifies the clash test. |

### Request

## [Body Structure](#body-structure)

| array: string: UUID*   array: string: UUID | The array of clash group IDs to find the detail for. Min items: 1 Max items: 20. |
| --- | --- |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Success |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource could not be found. |
| 415   Unsupported Media Type | The `Content-Type` header must be `application/json`. |
| 429   Too Many Requests | Rate limit exceeded; wait some time before retrying. The `Retry-After` header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| id   string: UUID | The unique identifier of the closed clash group. |
| --- | --- |
| clashTestId   string: UUID | The unique identifier of the clash test associated with the closed clash group. |
| title   string | The title of the closed clash group. Max length: 128. |
| description   string | The description of the closed clash group. Max length: 1024. |
| reason   enum: string | The reason for closing this clash group. Possible values: `OTHER`, `VALID_INTERFACE`, `VALID_PENETRATION`, `MINIMAL_OVERLAP`, `ITEM_CAN_FLEX`, `MODEL_INACCURACY`, `FIELD_FIX`. |
| screenShots   array: string: UUID | The unique identifiers of screenshots associated with the closed clash group. Max items: 5. |
| createdBy   string | The unique identifier of the user who created the closed clash group. |
| createdOn   datetime: ISO 8601 | The date and time that the closed clash group was created. |
| clashData   object | The clash data associated with a clash group. |
| documents   array: object | The documents associated with the clash groups supplied. |
| id   int | The document index ID. |
| urn   string | The document URN. |
| viewableName   string | The viewable name of the document in the model set version. |
| clashes   array: object | The clashes associated with the clash groups supplied. |
| id   int | The clash index ID. |
| clash   array: int | The clash instance index ID. Min items: 2 Max items: 2. |
| dist   int | The clash distance. |
| status   string | The status of the clash. |
| clashInstances   array: object | The clash instances associated with the clash groups supplied. |
| cid   int | The clash ID in the model set version. |
| ldid   int | The left-hand-side document ID. |
| loid   int | The left-hand-side object ID. |
| lvid   int | The left-hand-side viewable ID. |
| rdid   int | The right-hand-side document ID. |
| roid   int | The right-hand-side object ID. |
| rvid   int | The left-hand-side viewable ID. |

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
curl -v 'https://developer.api.autodesk.com/bim360/clash/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/tests/c40b4498-1baa-405d-4fe9-423514bbbf10/clashes/closed' \
     -X POST \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: application/json' \
     -d '[
           "d98c1dd4-008f-04b2-e980-0998ecf8427e"
         ]'

```

### Response (200)

```
[
  {
    "id": "74b70bb8-8802-a1fd-f201-890375a60c8f",
    "clashTestId": "21469f89-986a-c194-ae45-cefade1c7bde",
    "title": "Ceiling 2' x 2' grid and 411 other objects.",
    "description": "Objects expected in ceiling.",
    "reason": "OTHER",
    "screenShots": [
      "d98c1dd4-008f-04b2-e980-0998ecf8427e"
    ],
    "createdBy": "PD23PXGV8V3V",
    "createdOn": "2015-10-21T16:32:22Z",
    "clashData": {
      "documents": [
        {
          "id": 184,
          "urn": "urn:adsk.wipprod:fs.file:vf.jvMF7mrHR7OwG_DToKsJUA?version=1",
          "viewableName": "Level 1"
        }
      ],
      "clashes": [
        {
          "id": 184,
          "clash": [
            212
          ],
          "dist": 114.1678367952799,
          "status": "New"
        }
      ],
      "clashInstances": [
        {
          "cid": 75,
          "ldid": 1,
          "loid": 91,
          "lvid": 69,
          "rdid": 147,
          "roid": 246,
          "rvid": 243
        }
      ]
    }
  }
]

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
