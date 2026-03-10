# projects/{projectId}/packages/{packageId}/takeoff-types

Source: https://aps.autodesk.com/en/docs/acc/reference/http/takeoff-projects-project_id-packages-package_id-takeoff-types-GET/

---

Takeoff Types

GET

# projects/{projectId}/packages/{packageId}/takeoff-types

Retrieves the takeoff types for a package.

You need to create the types in the UI. For more information, see the [ACC Takeoff Types](https://help.autodesk.com/view/TAKEOFF/ENU/?guid=Takeoff_Types) help documentation.

To find the takeoff packages for a project, call [GET packages](en/docs/acc/v1/reference/http/takeoff-projects-project_id-packages-GET/).

To learn how this endpoint is used, see the [Takeoff Extract Inventory](../how-to-docs/takeoff-takeoff-extract-inventory.md) tutorial.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/takeoff/v1/projects/{projectId}/packages/{packageId}/takeoff-types |
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

- projectIdstring: UUID The ID of the project. This corresponds to project ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/), and can be specified in the form of “UUID” or b.”UUID”.To learn how to find the project ID, see the [Retrieve ACC Account and project ID](../how-to-docs/getting-started-retrieve-account-and-project-id.md) tutorial.
- packageIdstring: UUID The takeoff package ID. To find the ID, call [GET packages](http-takeoff-projects-project_id-packages-GET.md).

### Request

## [Query String Parameters](#query-string-parameters)

| offset   int | The takeoff type index from which the pagination starts. This is zero-based. |
| --- | --- |
| limit   int | The maximum number of takeoff types per page. <br>Accepatble values: `1-10000`.<br>Default value: `1000`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the takeoff types. |
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
| results   array: object | A list of takeoff types. |
| id   string: UUID | The takeoff type ID. |
| name   string | The takeoff type name. <br>Max length: 64 |
| description   string | A description of the takeoff type. <br>Max length: 256 |
| color   string | The color of the takeoff type as it appears on the sheet or model. <br>A color is represented by a value consisting of 6 or 8 hexadecimal digits, prefixed with a hash (#) symbol. In the 6-digit notation, the first pair of digits represent the red channel, the middle pair of digits represent the green channel and the last pair of digits represent the blue channel. The color is completely opaque.<br>The 8-digit notation follows the structure of the 6-digit notation, where the additional last 2-digits represent the alpha channel (`00` is transparent and `ff` is fully opaque). |
| borderColor   string | The color of the takeoff type as it appears on the sheet or model. <br>A color is represented by a value consisting of 6 or 8 hexadecimal digits, prefixed with a hash (#) symbol. In the 6-digit notation, the first pair of digits represent the red channel, the middle pair of digits represent the green channel and the last pair of digits represent the blue channel. The color is completely opaque.<br>The 8-digit notation follows the structure of the 6-digit notation, where the additional last 2-digits represent the alpha channel (`00` is transparent and `ff` is fully opaque). |
| shapeType   enum:string | The shape of the count marker. <br>A count marker is one of the takeoff tool type options that is selected in the UI when creating a takeoff type.<br>Possible values: `CIRCLE`, `TRIANGLE`, `SQUARE`, `DIAMOND`, `CHECKMARK`. |
| countMarkerSize   number | The size of the count marker. <br>You must set this value in the UI. |
| tool   enum:string | The type of tool used to create takeoff items of this takeoff type. <br>Possible values: `COUNT`, `DISTANCE`, `AREA`, `SELECT`.<br>Corresponding UI names: `COUNT`, `LINEAR`, `AREA`, `BIM`. |
| propertyDefinitions   array: object | A list of additional, user provided parameters associated with a 2D takeoff type. |
| name   string | The name of the property. <br>Max length: 256 |
| unitOfMeasure   enum:string | The unit of measurement. <br>Possible values: `EA`, `IN`, `LF`, `YD`, `SI`, `SF`, `SY`, `CI`, `CF`, `CY`, `LBS`, `TON`, `MM`, `M`, `M2`, `M3`, `KG`, `T`. |
| value   number | The value of the property. |
| valueLocation   enum:string | The location of the value. <br>For properties Length, Width, Height, Depth and Thickness: `valueLocation` is `INSTANCE_WITH_TAKEOFF_TYPE_DEFAULT`.<br>For properties WeightByLength, WeightByArea and WeightByVolume: `valueLocation` is `TAKEOFF_TYPE`. Possible values: `TAKEOFF_TYPE`, `INSTANCE_WITH_TAKEOFF_TYPE_DEFAULT` |
| modelMappings   array: object | A list of model properties used to calculate output. <br>Only relevant for 3D models. |
| name   string | The name of the mapping. <br>Max length: 256 |
| mappingExpression   string | The mapping formula. |
| primaryQuantityDefinition   object | The classification quantity details. |
| outputName   string | A custom output name from the user. |
| classificationCodeOne   string | The classification code selected from the first classification system. |
| classificationCodeTwo   string | The classification code selected from the second classification system. |
| expression   string | The formula to calculate the quantity. |
| unitOfMeasure   enum:string | The unit of measurement. <br>Possible values: `EA`, `IN`, `LF`, `YD`, `SI`, `SF`, `SY`, `CI`, `CF`, `CY`, `LBS`, `TON`, `MM`, `M`, `M2`, `M3`, `KG`, `T`. |
| secondaryQuantityDefinitions   array: object | A list of secondary classification quantity details. |
| outputName   string | A custom output name from the user. |
| classificationCodeOne   string | The classification code selected from the first classification system. |
| classificationCodeTwo   string | The classification code selected from the second classification system. |
| expression   string | The formula to calculate the quantity. |
| unitOfMeasure   enum:string | The unit of measurement. <br>Possible values: `EA`, `IN`, `LF`, `YD`, `SI`, `SF`, `SY`, `CI`, `CF`, `CY`, `LBS`, `TON`, `MM`, `M`, `M2`, `M3`, `KG`, `T`. |
| createdAt   datetime: ISO 8601 | The date and time when the resource was created, in the following format: `YYYY-MM-DDThh:mm:ssZ`. |
| updatedAt   datetime: ISO 8601 | The date and time when the resource was last updated, in the following format: `YYYY-MM-DDThh:mm:ssZ`. |
| updatedByName   string | The name of the user who last updated the resource. |

## [Example](#example)

Successfully retrieved the takeoff types.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/takeoff/v1/projects/:projectId/packages/:packageId/takeoff-types?limit=100' \
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
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "Foundation Slab",
      "description": "Slab in the garage",
      "color": "#11ff11",
      "borderColor": "#11ff11",
      "shapeType": "SQUARE",
      "countMarkerSize": 1.5,
      "tool": "DISTANCE",
      "propertyDefinitions": [
        {
          "name": "Height",
          "unitOfMeasure": "LF",
          "value": 2.5,
          "valueLocation": "INSTANCE_WITH_TAKEOFF_TYPE_DEFAULT"
        },
        {
          "name": "Width",
          "unitOfMeasure": "LF",
          "value": 1,
          "valueLocation": "INSTANCE_WITH_TAKEOFF_TYPE_DEFAULT"
        }
      ],
      "modelMappings": [
        {
          "name": "Area",
          "mappingExpression": "Sill_Height*Width"
        }
      ],
      "primaryQuantityDefinition": {
        "classificationCodeOne": "037000",
        "classificationCodeTwo": "044000",
        "outputName": "Exterior Wall",
        "expression": "Distance*Width*Height*1.1",
        "unitOfMeasure": "CY"
      },
      "secondaryQuantityDefinitions": [
        {
          "classificationCodeOne": "CustomAreaCode1",
          "classificationCodeTwo": "CustomAreaCode2",
          "outputName": "Custom Flooring",
          "expression": "Distance*Width",
          "unitOfMeasure": "SF"
        }
      ],
      "createdAt": "2019-08-24T14:15:22Z",
      "updatedAt": "2020-11-11T12:32:45Z",
      "updatedByName": "Jane Johnson"
    }
  ]
}

```

Show More
