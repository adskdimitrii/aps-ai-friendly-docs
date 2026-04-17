# projects/{projectId}/packages/{packageId}/takeoff-items/{takeoffItemId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/takeoff-projects-project_id-packages-package_id-takeoff-items-takeoff_item_id-GET/

---

Takeoff Items

GET

# projects/{projectId}/packages/{packageId}/takeoff-items/{takeoffItemId}

Retrieves a specified takeoff item for a package.

For more information about takeoff items, see the [Forma Takeoff](https://help.autodesk.com/view/TAKEOFF/ENU/?guid=Takeoff_Types) help documentation.

To find the takeoff packages for a project, call [GET packages](http-takeoff-projects-project_id-packages-GET.md).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/takeoff/v1/projects/{projectId}/packages/{packageId}/takeoff-items/{takeoffItemId} |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

- Authorization*string Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context.
- regionstring Specifies the region where the service is located. Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page.

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>This corresponds to project ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/), and can be specified in the form of “UUID” or b.”UUID”.<br>To learn how to find the project ID, see the [Retrieve Forma hub and project ID](../how-to-docs/getting-started-retrieve-account-and-project-id.md) tutorial. |
| --- | --- |
| packageId   string: UUID | The takeoff package ID. <br>To find the ID, call [GET packages](http-takeoff-projects-project_id-packages-GET.md). |
| takeoffItemId   string: UUID | The takeoff item ID. <br>To find the ID, call [GET takeoff-items](http-takeoff-projects-project_id-packages-package_id-takeoff-items-GET.md). |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the takeoff item. |
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

| id   string: UUID | The takeoff item ID. |
| --- | --- |
| takeoffTypeId   string: UUID | The takeoff type ID. |
| type   enum:string | The takeoff type method. <br>Possible values: `COUNT`, `DISTANCE`, `AREA`, `SELECT`.<br>Corresponding UI names: `COUNT`, `LINEAR`, `AREA`, `BIM`. |
| objectName   string | The name of the takeoff type that the item is derived from. |
| geometry   string | The geometry of a 2D takeoff item specified in SVG. This property is not returned for a 3D takeoff item. |
| objectId   int | The ID of the selected BIM model element in the viewing model. |
| propertyValues   array: object | A list of takeoff item properties used to calculate quantity. |
| name   string | Name of the property. |
| unitOfMeasure   enum:string | The unit of measurement. <br>Possible values: `EA`, `IN`, `LF`, `YD`, `SI`, `SF`, `SY`, `CI`, `CF`, `CY`, `LBS`, `TON`, `MM`, `M`, `M2`, `M3`, `KG`, `T`. |
| source   enum:string | Specifies how a takeoff property value was obtained. Possible values: `MANUAL_ENTRY`, `BIM_PROPERTY`, `MEASUREMENT` |
| value | The value of a takeoff instance. |
| anyOf | The value of a takeoff instance. |
| Number   number | A number representation of the property value. |
| String   string | A string representation of the property value. |
| primaryQuantity   object | The quantity of a takeoff. |
| outputName   string | A custom output name from the user. |
| classificationCodeOne   string | The classification code selected from the first classification system. |
| classificationCodeTwo   string | The classification code selected from the second classification system. |
| quantity   number | The quantity of the takeoff. |
| unitOfMeasure   enum:string | The unit of measurement. <br>Possible values: `EA`, `IN`, `LF`, `YD`, `SI`, `SF`, `SY`, `CI`, `CF`, `CY`, `LBS`, `TON`, `MM`, `M`, `M2`, `M3`, `KG`, `T`. |
| secondaryQuantities   array: object | A list of secondary takeoff quantities. |
| outputName   string | A custom output name from the user. |
| classificationCodeOne   string | The classification code selected from the first classification system. |
| classificationCodeTwo   string | The classification code selected from the second classification system. |
| quantity   number | The quantity of the takeoff. |
| unitOfMeasure   enum:string | The unit of measurement. <br>Possible values: `EA`, `IN`, `LF`, `YD`, `SI`, `SF`, `SY`, `CI`, `CF`, `CY`, `LBS`, `TON`, `MM`, `M`, `M2`, `M3`, `KG`, `T`. |
| contentView   object | The content view reference that this item is associated with. |
| id   string: UUID | The content view ID. |
| version   one of | The content view version. |
| Model identifier   string | The 3D model ID. |
| Sheet identifier   string: UUID | The 2D sheet ID. |
| locationId   string: UUID | The location ID associated with the takeoff item. <br>For more information about the location, see [GET nodes](http-locations-nodes-GET.md). |
| createdAt   datetime: ISO 8601 | The date and time when the resource was created, in the following format: `YYYY-MM-DDThh:mm:ssZ`. |
| updatedAt   datetime: ISO 8601 | The date and time when the resource was last updated, in the following format: `YYYY-MM-DDThh:mm:ssZ`. |
| updatedByName   string | The name of the user who last updated the resource. |

## [Example](#example)

Successfully retrieved the takeoff item.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/takeoff/v1/projects/:projectId/packages/:packageId/takeoff-items/:takeoffItemId' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "takeoffTypeId": "b9380176-9ac2-454d-acdd-fdfd988b9702",
  "type": "COUNT",
  "objectName": "36\" x 48\"",
  "geometry": "<path fill=\"none\" stroke=\"red\" d=\"M 10,10 h 10 m 0,10 h 10 m 0,10 h 10\">",
  "objectId": 1,
  "propertyValues": [
    {
      "name": "Perimeter",
      "unitOfMeasure": "LF",
      "source": "MEASUREMENT",
      "value": 3
    }
  ],
  "primaryQuantity": {
    "outputName": "Bedroom Wall",
    "classificationCodeOne": "015113",
    "classificationCodeTwo": "011223",
    "quantity": 15,
    "unitOfMeasure": "EA"
  },
  "secondaryQuantities": [
    {
      "outputName": "Wall Paint",
      "classificationCodeOne": "016732",
      "classificationCodeTwo": "011665",
      "quantity": 45,
      "unitOfMeasure": "LF"
    }
  ],
  "contentView": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "version": "urn:adsk.wipstg:fs.file:vf.oeSywgLpSkONo9O6CUZvkQ?version=3"
  },
  "locationId": "ff7f6eb4-6276-4993-bfeb-34cbbbba3a17",
  "createdAt": "2019-08-24T14:15:22Z",
  "updatedAt": "2020-11-11T12:32:45Z",
  "updatedByName": "Jane Johnson"
}

```

Show More
