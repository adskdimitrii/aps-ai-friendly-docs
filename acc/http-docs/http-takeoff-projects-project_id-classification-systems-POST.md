# projects/{projectId}/classification-systems

Source: https://aps.autodesk.com/en/docs/acc/reference/http/takeoff-projects-project_id-classification-systems-POST/

---

Classification Systems

POST

# projects/{projectId}/classification-systems

Creates a classification system for a project.

A classification system categorizes and organizes construction information in a hierarchical structure, and is used to label items in a takeoff project.

For more information about the classification system, see the [ACC Configure Takeoff Settings](https://help.autodesk.com/view/TAKEOFF/ENU/?guid=Configure_Takeoff_Settings) help documentation.

Note that you can create up to two classification systems for a project.

Note that you can create either an empty, or populated classification system.

To update an existing classification system, call [POST classifications:import](http-takeoff-projects-project_id-classification-systems-system_id-classificationsimport-POST.md).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/takeoff/v1/projects/{projectId}/classification-systems |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| region   string | Specifies the region where the service is located. <br>Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>This corresponds to project ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/), and can be specified in the form of âUUIDâ or b.âUUIDâ.<br>To learn how to find the project ID, see the [Retrieve ACC Account and project ID](../how-to-docs/getting-started-retrieve-account-and-project-id.md) tutorial. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

Expand all

| name*   string | The classification system name. <br>Max length: 200 |
| --- | --- |
| type*   enum:string | The type of classification system. <br>Possible values: `CLASSIFICATION_SYSTEM_1`, `CLASSIFICATION_SYSTEM_2`.<br>See the [Help documentation](https://help.autodesk.com/view/TAKEOFF/ENU/?guid=Configure_Takeoff_Settings) for more details about the classification systems. |
| classifications   array: object | The classification hierarchy. <br>The classification hierarchy is configured as a JSON array in the payload, created from a spreadsheet file.<br>Max size: `30000`.<br>For more details, see the [ACC Configure Takeoff Settings](https://help.autodesk.com/view/TAKEOFF/ENU/?guid=Configure_Takeoff_Settings) help documentation. |
| code*   string | The classification code. <br>Max length: 256 |
| parentCode*   string | The classification parent code. <br>Its value may be `null`, indicating that this classification is at the top level of the hierarchy.<br>Max length: 256 |
| description*   string | A description of the classification. <br>Max length: 256 |
| measurementType   enum:string | **Deprecated. Will be removed on September 15, 2025.**<br>The type of measurement.<br>Possible values: `AREA`, `COUNT`, `DISTANCE`, `VOLUME`. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Successfully created a classification system. |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource could not be found. |
| 409   Conflict | The specified resource already exists. |
| 429   Too Many Requests | Rate limit exceeded; wait some time before retrying. The âRetry-Afterâ header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (201)](#body-structure-201)

| id   string: UUID | The classification system ID. |
| --- | --- |
| name   string | The classification system name. <br>Max length: 200 |
| type   enum:string | The type of classification system. <br>Possible values: `CLASSIFICATION_SYSTEM_1`, `CLASSIFICATION_SYSTEM_2`.<br>See the [Help documentation](https://help.autodesk.com/view/TAKEOFF/ENU/?guid=Configure_Takeoff_Settings) for more details about the classification systems. |

## [Example](#example)

Successfully created a classification system.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/takeoff/v1/projects/:projectId/classification-systems' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": "Smith Construction Classification",
        "type": "CLASSIFICATION_SYSTEM_1",
        "classifications": [
          {
            "code": "A1010",
            "parentCode": null,
            "description": "Concrete",
            "measurementType": "AREA"
          },
          {
            "code": "A1010.10",
            "parentCode": "A1010",
            "description": "Sprayed concrete",
            "measurementType": "AREA"
          },
          {
            "code": "A1010.20",
            "parentCode": "A1010",
            "description": "Foamed concrete",
            "measurementType": "AREA"
          }
        ]
      }'

```

Show More

### Response

```
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "Smith Construction Classification",
  "type": "CLASSIFICATION_SYSTEM_1"
}

```
