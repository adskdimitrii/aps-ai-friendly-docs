# projects/{projectId}/content-views

Source: https://aps.autodesk.com/en/docs/acc/reference/http/takeoff-projects-project_id-content-views-GET/

---

Content Views

GET

# projects/{projectId}/content-views

Retrieves the content views for a project.

For more information about content views, see the [ACC Takeoff - File Management Tools](https://help.autodesk.com/view/TAKEOFF/ENU/?guid=File_Mgt_Tools) help documentation.

To learn how this endpoint is used, see the [Takeoff Extract Inventory](../how-to-docs/takeoff-takeoff-extract-inventory.md) tutorial.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/takeoff/v1/projects/{projectId}/content-views |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| region   string | Specifies the region where the service is located. <br>Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>This corresponds to project ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/), and can be specified in the form of “UUID” or b.”UUID”.<br>To learn how to find the project ID, see the [Retrieve ACC Account and project ID](../how-to-docs/getting-started-retrieve-account-and-project-id.md) tutorial. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| offset   int | The content view object number from which the pagination starts. This is zero-based. |
| --- | --- |
| limit   int | The maximum number of content view objects per page. <br>Acceptable values: `1-200`.<br>Default value: `200`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the content views. |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource could not be found. |
| 429   Too Many Requests | Rate limit exceeded; wait some time before retrying. The ‘Retry-After’ header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| pagination   object | The pagination object. |
| --- | --- |
| limit   int | The maximum number of objects per page. |
| nextUrl   string | The URL path that returns the next page of data. |
| offset   int | The object number from which the pagination starts. This is zero-based. |
| results   array: object | A list of content views for the project. |
| id   string: UUID | The content view ID. |
| type   enum:string | The content view type. <br>Possible values: `SHEET` (2D Sheet), `FILE_MODEL` (3D Model). |
| view   one of | The content view. |
| Model View   object | The 3D model view. |
| lineageUrn   string | The URN of the 3D model view. <br>To learn how to use this attribute to retrieve details of the 3D model, see the [Takeoff Extract Inventory](../how-to-docs/takeoff-takeoff-extract-inventory.md) tutorial. |
| viewName   string | The name of the 3D model view. |
| Sheet View   object | The 2D sheet view. |
| sheetName   string | The sheet view name. |
| calibration   object | The sheet view calibration details. |
| scaleFactor   number | The scale used in the sheet view calibration. |
| units   enum:string | The units used in the sheet view calibration. <br>Possible values: `FT_AND_DECIMAL_IN`, `FT_AND_FRACTIONAL_IN`, `M`, `CM`, `MM`. |

## [Example](#example)

Successfully retrieved the content views.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/takeoff/v1/projects/:projectId/content-views?limit=10' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 100,
    "nextUrl": "https://developer.api.autodesk.com/construction/takeoff/v1/resources?limit=100&offset=200",
    "offset": 100
  },
  "results": [
    [
      {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "type": "FILE_MODEL",
        "view": {
          "lineageUrn": "urn:adsk.wipqa:dm.lineage:TCBw0V-GQX2aAWWSSrhQmQ",
          "viewName": "3D"
        }
      },
      {
        "id": "95451383-ee38-44da-b06c-2d5266e726d2",
        "type": "SHEET",
        "view": {
          "sheetName": "A09.05",
          "calibration": {
            "scaleFactor": 0.987,
            "units": "FT_AND_FRACTIONAL_IN"
          }
        }
      }
    ]
  ]
}

```

Show More
