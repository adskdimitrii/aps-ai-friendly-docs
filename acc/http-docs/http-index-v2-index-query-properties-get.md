# projects/:projectId/indexes/:indexId/queries/:queryId/properties

Source: https://aps.autodesk.com/en/docs/acc/reference/http/index-v2-index-query-properties-get/

---

Index

GET

# projects/:projectId/indexes/:indexId/queries/:queryId/properties

Retrieve the query specific properties index. Since the properties index, once created, is immutable, the response will set a long expiration HTTP header for efficient client side caching.

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/index/v2/projects/:projectId/indexes/:indexId/queries/:queryId/properties |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | json.gz |

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
| indexId   string | The index ID. |
| queryId   string | The query ID. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The response is provided in the [line-delimited JSON streaming format (LDJSON)](<https://de.wikipedia.org/wiki/JSON_streaming>) with the properties of one object per line. |
| --- | --- |
| 303   Redirect Method | The response is provided in the [line-delimited JSON streaming format (LDJSON)](<https://de.wikipedia.org/wiki/JSON_streaming>) with the properties of one object per line. |
| 401   Unauthorized | Response in case of an error. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 429   Too Many Requests | Rate limit exceeded. Wait some time before retrying. The `Retry-After` header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

| lmvId   int | Object database id from the original seed file property database (_objects_id.id). |
| --- | --- |
| dbId   string | Property database id (the property database the object originated from). |
| props   object | Property database property keyed values. |
| propsHash   string | Hash used to determine whether object properties have changed between different versions. |
| propsIgnored   object | Property database property values that are not considered for property change tracking. |
| geomHash   string | Hash used to determine whether the object geometry has changed between different versions. |
| bboxMin   object | minimum [x, y, z]-coords of the 3D-bbox. |
| bboxMax   object | maximum [x, y, z]-coords of the 3D-bbox. |
| views   array: string | List of corresponding view IDs in the index manifest that this object is visible in. |
| svf2Id   int | The stable SVF2 ID of the object. |
| lineageId   string | The lineage ID of the object; the (svf2Id, lineageId)-pair allows to track a specific object across several versions. |
| externalId   string | The external ID of the object. |

### Response

## [Body Structure (303)](#body-structure-303)

| lmvId   int | Object database id from the original seed file property database (_objects_id.id). |
| --- | --- |
| dbId   string | Property database id (the property database the object originated from). |
| props   object | Property database property keyed values. |
| propsHash   string | Hash used to determine whether object properties have changed between different versions. |
| propsIgnored   object | Property database property values that are not considered for property change tracking. |
| geomHash   string | Hash used to determine whether the object geometry has changed between different versions. |
| bboxMin   object | minimum [x, y, z]-coords of the 3D-bbox. |
| bboxMax   object | maximum [x, y, z]-coords of the 3D-bbox. |
| views   array: string | List of corresponding view IDs in the index manifest that this object is visible in. |
| svf2Id   int | The stable SVF2 ID of the object. |
| lineageId   string | The lineage ID of the object; the (svf2Id, lineageId)-pair allows to track a specific object across several versions. |
| externalId   string | The external ID of the object. |

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
curl -v 'https://developer.api.autodesk.com/construction/index/v2/projects/cd743656-f130-48bd-96e6-948175313637/indexes/da39a3ee5e6b4b0d/queries/0a2bef712ffee30a/properties' \
     -H 'Authorization: Bearer <token>'

```

### Response (200)

```
{
  "svf2Id": "1510",
  "lineageId": "344b06a3",
  "externalId": "546a5f5b-1aeb-43f9-b1f2-530ebe1e4c4a-0032d24c",
  "lmvId": "5721",
  "dbId": "455c17b4",
  "props": {
    "p00723fa6": "Main Model",
    "p01bbdcf2": "FIRST FLOOR",
    "p08bc1e88": "0",
    "p10f4572e": "505.527528165408",
    "p153cb174": "CONCESSION/ NATURE STORE 115 [991729]",
    "p188478f2": "0",
    "p1d45bc4f": "4",
    "p20d8441e": "Rooms",
    "p29ff6f58": "115",
    "p5264cd49": "1",
    "p532f0ad6": "New Construction",
    "p562c91d5": "8",
    "p5eddc473": "Revit Rooms",
    "p6ab86626": "FIRST FLOOR",
    "p78f04c1e": "99.54644577473422",
    "pa7275c45": "-2000160",
    "pb2959cb7": "0",
    "pc838ff15": "OCCUPANCY",
    "pdf772b6f": "CONCESSION/ NATURE STORE",
    "pe2ac2e1d": "8",
    "pef87fde6": "0"
  },
  "propsHash": "46681c9a",
  "propsIgnored": {
    "p93e93af5": "5599"
  },
  "geomHash": "c9f2684f",
  "bbox": {
    "min": [
      "-54.80051040649414",
      "1.0369148254394531",
      "-5.971645355224609"
    ],
    "max": [
      "-33.66492462158203",
      "31.324600219726562",
      "2.0283546447753906"
    ]
  },
  "views": [
    "7ca0051c"
  ]
}

```

Show More

### Response (303)

```
{
  "svf2Id": "1510",
  "lineageId": "344b06a3",
  "externalId": "546a5f5b-1aeb-43f9-b1f2-530ebe1e4c4a-0032d24c",
  "lmvId": "5721",
  "dbId": "455c17b4",
  "props": {
    "p00723fa6": "Main Model",
    "p01bbdcf2": "FIRST FLOOR",
    "p08bc1e88": "0",
    "p10f4572e": "505.527528165408",
    "p153cb174": "CONCESSION/ NATURE STORE 115 [991729]",
    "p188478f2": "0",
    "p1d45bc4f": "4",
    "p20d8441e": "Rooms",
    "p29ff6f58": "115",
    "p5264cd49": "1",
    "p532f0ad6": "New Construction",
    "p562c91d5": "8",
    "p5eddc473": "Revit Rooms",
    "p6ab86626": "FIRST FLOOR",
    "p78f04c1e": "99.54644577473422",
    "pa7275c45": "-2000160",
    "pb2959cb7": "0",
    "pc838ff15": "OCCUPANCY",
    "pdf772b6f": "CONCESSION/ NATURE STORE",
    "pe2ac2e1d": "8",
    "pef87fde6": "0"
  },
  "propsHash": "46681c9a",
  "propsIgnored": {
    "p93e93af5": "5599"
  },
  "geomHash": "c9f2684f",
  "bbox": {
    "min": [
      "-54.80051040649414",
      "1.0369148254394531",
      "-5.971645355224609"
    ],
    "max": [
      "-33.66492462158203",
      "31.324600219726562",
      "2.0283546447753906"
    ]
  },
  "views": [
    "7ca0051c"
  ]
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
