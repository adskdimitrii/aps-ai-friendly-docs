# projects/:projectId/diffs/:diffId/queries/:queryId/properties

Source: https://aps.autodesk.com/en/docs/acc/reference/http/index-v2-diff-query-properties-get/

---

Diff

GET

# projects/:projectId/diffs/:diffId/queries/:queryId/properties

Retrieve the query specific properties of the given diff. Since the diff properties, once created, are immutable, the response will set a long expiration HTTP header for efficient client side caching.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/index/v2/projects/:projectId/diffs/:diffId/queries/:queryId/properties |
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
| diffId   string | The diff ID. |
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

Expand all

| lmvId   int | Object database id from the original seed file property database (_objects_id.id). |
| --- | --- |
| dbId   string | Property database id (the property database the object originated from). |
| props   object | Property database property keyed values. |
| propsHash   string | Hash used to determine whether object properties have changed between different versions. |
| propsIgnored   object | Property database property values that are not considered for property change tracking. |
| geomHash   string | Hash used to determine whether the object geometry has changed between different versions. |
| bboxMin   object | Minimum [x, y, z]-coords of the 3D-bbox. |
| bboxMax   object | Maximum [x, y, z]-coords of the 3D-bbox. |
| views   array: string | List of corresponding view IDs in the index manifest that this object is visible in. |
| svf2Id   int | The stable SVF2 ID of the object. |
| lineageId   string | The lineage ID of the object; the (svf2Id, lineageId)-pair allows to track a specific object across several versions. |
| externalId   string | The external ID of the object. |
| type   enum: string | object change type. <br>Possible values: `OBJECT_ADDED`, `OBJECT_REMOVED`, `OBJECT_CHANGED` |
| prev   object | common properties index properties. |
| lmvId   int | Object database id from the original seed file property database (_objects_id.id). |
| dbId   string | Property database id (the property database the object originated from). |
| props   object | Property database property keyed values. |
| propsHash   string | Hash used to determine whether object properties have changed between different versions. |
| propsIgnored   object | Property database property values that are not considered for property change tracking. |
| geomHash   string | Hash used to determine whether the object geometry has changed between different versions. |
| bboxMin   array: int | minimum [x, y, z]-coords of the 3D-bbox. |
| bboxMax   array: int | maximum [x, y, z]-coords of the 3D-bbox. |
| views   array: string | List of corresponding view IDs in the index manifest that this object is visible in. |

### Response

## [Body Structure (303)](#body-structure-303)

Expand all

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
| type   enum: string | object change type. <br>Possible values: `OBJECT_ADDED`, `OBJECT_REMOVED`, `OBJECT_CHANGED` |
| prev   object | common properties index properties. |
| lmvId   int | Object database id from the original seed file property database (_objects_id.id). |
| dbId   string | Property database id (the property database the object originated from). |
| props   object | Property database property keyed values. |
| propsHash   string | Hash used to determine whether object properties have changed between different versions. |
| propsIgnored   object | Property database property values that are not considered for property change tracking. |
| geomHash   string | Hash used to determine whether the object geometry has changed between different versions. |
| bboxMin   array: int | minimum [x, y, z]-coords of the 3D-bbox. |
| bboxMax   array: int | maximum [x, y, z]-coords of the 3D-bbox. |
| views   array: string | List of corresponding view IDs in the index manifest that this object is visible in. |

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
curl -v 'https://developer.api.autodesk.com/construction/index/v2/projects/cd743656-f130-48bd-96e6-948175313637/diffs/3fe13864aecfe0a5/queries/0a2bef712ffee30a/properties' \
     -H 'Authorization: Bearer <token>'

```

### Response (200)

```
[
  {
    "type": "OBJECT_REMOVED",
    "svf2Id": "1510",
    "lineageId": "ad425719",
    "externalId": "546a5f5b-1aeb-43f9-b1f2-530ebe1e4c4a-0032d24c",
    "lmvId": null,
    "dbId": null,
    "props": null,
    "propsHash": null,
    "prev": {
      "lmvId": "182",
      "dbId": "be53682a",
      "props": {
        "p10c1a84a": "false",
        "p114b1425": "false",
        "p121ac73d": "Show Original",
        "p153cb174": "New Construction",
        "p21b83ee9": "1000",
        "p24044fbb": "false",
        "p30015eee": "Fine",
        "p31561b85": "None",
        "p326e867f": "71.36222284862842",
        "p345273d1": "false",
        "p43766fd1": "96",
        "p52413328": "By Discipline",
        "p532f0ad6": "New Construction",
        "p5eddc473": "Revit View",
        "p79f5f88c": "LMV",
        "p90dddb61": "false",
        "p93e93af5": "1",
        "p9ced1273": "New Construction",
        "pa5fef29f": "all",
        "pa7275c45": "-2000279",
        "paea62326": "Adjusting",
        "pb940b1a4": "Architectural",
        "pc2252206": "1/8\" = 1'-0\"",
        "pd0d53a26": "false",
        "pe01bd7ef": "None",
        "pe73257b1": "Independent",
        "pf2c65ab9": "329.87844072436667",
        "pfa32ecb1": "Orthographic",
        "pfa463ea8": "false"
      },
      "propsHash": "d8d14133",
      "propsIgnored": null,
      "geomHash": "ceffb260",
      "bbox": {
        "min": [
          "-43.302825927734375",
          "-58.94974899291992",
          "-5.971645355224609"
        ],
        "max": [
          "-40.30475997924805",
          "-58.570899963378906",
          "1.0283546447753906"
        ]
      },
      "views": []
    }
  },
  {
    "type": "OBJECT_CHANGED",
    "svf2Id": "757",
    "lineageId": "344b06a3",
    "externalId": "5466a680-ad75-4568-9ba3-2e48a29f7367-000f1fa9",
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
    ],
    "prev": {
      "lmvId": "5721",
      "props": {
        "p10f4572e": "504.2436739987414",
        "p78f04c1e": "103.79644577473447"
      },
      "propsHash": "8f50272f",
      "propsIgnored": {
        "p93e93af5": "5599"
      },
      "geomHash": "70435f8c",
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
  },
  {
    "type": "OBJECT_ADDED",
    "svf2Id": "38866",
    "lineageId": "344b06a3",
    "externalId": "acee946f-3e4f-4f67-9837-4c3fac19de9b-0032d267",
    "lmvId": "38816",
    "dbId": "455c17b4",
    "props": {
      "p00723fa6": "Main Model",
      "p01bbdcf2": "FIRST FLOOR",
      "p09faf620": "19\"H Seat",
      "p13b6b3a0": "19\"H Seat",
      "p153cb174": "Toilet-Commercial-Wall-3D [3330663]",
      "p16233090": "0",
      "p20d8441e": "Plumbing Fixtures",
      "p30db51f9": "Toilet-Commercial-Wall-3D",
      "p36ee6bc3": "MEN'S TOILET",
      "p3c57b64e": "New Construction",
      "p4fd45709": "Porcelain - Ivory",
      "p54217060": "D2010110",
      "p5eddc473": "Revit Plumbing Fixtures",
      "p63ed81bb": "Water Closets - Single",
      "p69a73bfb": "1.5833333333333335",
      "p6a81eafd": "5842",
      "p75c61d00": "Metal - Steel, Polished",
      "p75d0aa84": "Laminate - Ivory,Matte",
      "p8d70f1c5": "109",
      "p93e93af5": "5843",
      "p9482d58a": "136",
      "pa7275c45": "-2001160",
      "pab5862eb": "Undefined",
      "pc8d7966e": "0",
      "pcbcd5bb4": "0",
      "pe4b74447": "4.075315959131618",
      "pe61a57c3": "0",
      "pee815a7f": "None",
      "pf65f749b": "3.2988707985541077"
    },
    "propsHash": "db9bfcdb",
    "propsIgnored": null,
    "geomHash": "89981bb6",
    "bbox": {
      "min": [
        "124.14583587646484",
        "10.525434494018555",
        "-5.388311862945557"
      ],
      "max": [
        "126.5625",
        "12.192100524902344",
        "-3.429264783859253"
      ]
    },
    "views": [
      "cf7900d3",
      "7ca0051c"
    ],
    "prev": null
  }
]

```

Show More

### Response (303)

```
[
  {
    "type": "OBJECT_REMOVED",
    "svf2Id": "1510",
    "lineageId": "ad425719",
    "externalId": "546a5f5b-1aeb-43f9-b1f2-530ebe1e4c4a-0032d24c",
    "lmvId": null,
    "dbId": null,
    "props": null,
    "propsHash": null,
    "prev": {
      "lmvId": "182",
      "dbId": "be53682a",
      "props": {
        "p10c1a84a": "false",
        "p114b1425": "false",
        "p121ac73d": "Show Original",
        "p153cb174": "New Construction",
        "p21b83ee9": "1000",
        "p24044fbb": "false",
        "p30015eee": "Fine",
        "p31561b85": "None",
        "p326e867f": "71.36222284862842",
        "p345273d1": "false",
        "p43766fd1": "96",
        "p52413328": "By Discipline",
        "p532f0ad6": "New Construction",
        "p5eddc473": "Revit View",
        "p79f5f88c": "LMV",
        "p90dddb61": "false",
        "p93e93af5": "1",
        "p9ced1273": "New Construction",
        "pa5fef29f": "all",
        "pa7275c45": "-2000279",
        "paea62326": "Adjusting",
        "pb940b1a4": "Architectural",
        "pc2252206": "1/8\" = 1'-0\"",
        "pd0d53a26": "false",
        "pe01bd7ef": "None",
        "pe73257b1": "Independent",
        "pf2c65ab9": "329.87844072436667",
        "pfa32ecb1": "Orthographic",
        "pfa463ea8": "false"
      },
      "propsHash": "d8d14133",
      "propsIgnored": null,
      "geomHash": "ceffb260",
      "bbox": {
        "min": [
          "-43.302825927734375",
          "-58.94974899291992",
          "-5.971645355224609"
        ],
        "max": [
          "-40.30475997924805",
          "-58.570899963378906",
          "1.0283546447753906"
        ]
      },
      "views": []
    }
  },
  {
    "type": "OBJECT_CHANGED",
    "svf2Id": "757",
    "lineageId": "344b06a3",
    "externalId": "5466a680-ad75-4568-9ba3-2e48a29f7367-000f1fa9",
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
    ],
    "prev": {
      "lmvId": "5721",
      "props": {
        "p10f4572e": "504.2436739987414",
        "p78f04c1e": "103.79644577473447"
      },
      "propsHash": "8f50272f",
      "propsIgnored": {
        "p93e93af5": "5599"
      },
      "geomHash": "70435f8c",
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
  },
  {
    "type": "OBJECT_ADDED",
    "svf2Id": "38866",
    "lineageId": "344b06a3",
    "externalId": "acee946f-3e4f-4f67-9837-4c3fac19de9b-0032d267",
    "lmvId": "38816",
    "dbId": "455c17b4",
    "props": {
      "p00723fa6": "Main Model",
      "p01bbdcf2": "FIRST FLOOR",
      "p09faf620": "19\"H Seat",
      "p13b6b3a0": "19\"H Seat",
      "p153cb174": "Toilet-Commercial-Wall-3D [3330663]",
      "p16233090": "0",
      "p20d8441e": "Plumbing Fixtures",
      "p30db51f9": "Toilet-Commercial-Wall-3D",
      "p36ee6bc3": "MEN'S TOILET",
      "p3c57b64e": "New Construction",
      "p4fd45709": "Porcelain - Ivory",
      "p54217060": "D2010110",
      "p5eddc473": "Revit Plumbing Fixtures",
      "p63ed81bb": "Water Closets - Single",
      "p69a73bfb": "1.5833333333333335",
      "p6a81eafd": "5842",
      "p75c61d00": "Metal - Steel, Polished",
      "p75d0aa84": "Laminate - Ivory,Matte",
      "p8d70f1c5": "109",
      "p93e93af5": "5843",
      "p9482d58a": "136",
      "pa7275c45": "-2001160",
      "pab5862eb": "Undefined",
      "pc8d7966e": "0",
      "pcbcd5bb4": "0",
      "pe4b74447": "4.075315959131618",
      "pe61a57c3": "0",
      "pee815a7f": "None",
      "pf65f749b": "3.2988707985541077"
    },
    "propsHash": "db9bfcdb",
    "propsIgnored": null,
    "geomHash": "89981bb6",
    "bbox": {
      "min": [
        "124.14583587646484",
        "10.525434494018555",
        "-5.388311862945557"
      ],
      "max": [
        "126.5625",
        "12.192100524902344",
        "-3.429264783859253"
      ]
    },
    "views": [
      "cf7900d3",
      "7ca0051c"
    ],
    "prev": null
  }
]

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
