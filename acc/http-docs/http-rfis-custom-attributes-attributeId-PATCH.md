# custom-attributes/:attributeId

Source: https://aps.autodesk.com/en/docs/acc/reference/http/rfis-custom-attributes-attributeId-PATCH/

---

Custom Attributes

PATCH

# custom-attributes/:attributeId

Updates an existing custom attribute definition for a project.

Use this endpoint to change the attribute’s name, description, status, or possible values.
The attribute can be used when creating or updating RFIs.

For more information on custom attributes, see the [Custom RFI Fields](https://help.autodesk.com/view/BUILD/ENU/?guid=Custom_RFI_Fields) help topic.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/attributes/:attributeId |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` `data:create` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |
| attributeId   string | The ID of the custom attribute. |

### Request

## [Body Structure](#body-structure)

Expand all

| name   string | The name of the custom attribute as displayed in the UI. <br>Max length: 50 |
| --- | --- |
| description   string | The description of the attribute as shown in the UI. <br>Max length: 1000 |
| status   enum:string | The display status of the attribute in the UI. Possible values: `active`, `inactive`, `hidden`. |
| multipleChoice   boolean | `true`: users can select more than one value for this attribute. <br>`false`: (default) users can select only one value. |
| possibleValues   object | Updates the list of possible values for the attribute. <br>To overwrite an existing possible value, specify both `newAttributes` (the new value name) and `deletedAttributes` (the ID of the value to remove). |
| newAttributes   array: string,null | Adds new possible values to the attribute. <br>Each item is the name of a new possible value as shown in the UI. |
| updatedAttributes   array: object | Updates the names of existing possible values. |
| id   string: UUID | The unique ID of the attribute value. |
| name*   string,integer,null | The name of the attribute value as shown in the UI. <br>Max length: 100 |
| deletedAttributes   array: string | Deletes possible values from the attribute. Each item is the ID of a possible value to delete. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Updated |
| --- | --- |
| 400   Bad Request | The parameters are invalid |
| 401   Unauthorized | The provided bearer token is not valid |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation |
| 500   Internal Server Error | An unknown error occurred on the server |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| id   string: UUID | The ID of the custom attribute definition. |
| --- | --- |
| name   string | The name of the custom attribute as displayed in the UI. <br>Max length: 50 |
| type   enum:string | The type of the attribute. Possible values: `text`, `numeric` |
| description   string | The description of the attribute as shown in the UI. <br>Max length: 1000 |
| status   enum:string | The display status of the attribute in the UI. Possible values: `active`, `inactive`, `hidden`. |
| multipleChoice   boolean | `true`: users can select more than one value for this attribute. <br>`false`: (default) users can select only one value. |
| possibleValues   array: object | A list of possible values for the attribute. |
| id   string: UUID | The unique ID of the attribute value. |
| name   string,integer,null | The name of the attribute value as shown in the UI. <br>Max length: 100 |

## [Example](#example)

Updated

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/attributes/:attributeId' \
  -X 'PATCH' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": "Attribute 1",
        "description": "This is a description of the attribute",
        "status": "active",
        "multipleChoice": false,
        "possibleValues": {
          "newAttributes": [
            "Plaster"
          ],
          "updatedAttributes": [
            {
              "id": "c911852d-5957-4145-9c8d-e7cfe9d564df",
              "name": "Value 1"
            }
          ],
          "deletedAttributes": [
            "3ff28f60-33ae-4b90-a55f-53ab305c9591"
          ]
        }
      }'

```

Show More

### Response

```
{
  "id": "c911852d-5957-4145-9c8d-e7cfe9d564df",
  "name": "Attribute 1",
  "type": "text",
  "description": "This is a description of the attribute",
  "status": "active",
  "multipleChoice": false,
  "possibleValues": [
    {
      "id": "c911852d-5957-4145-9c8d-e7cfe9d564df",
      "name": "Value 1"
    }
  ]
}

```

Show More
