# assets:batch-create V2

Source: https://aps.autodesk.com/en/docs/acc/reference/http/assets-assets-batch-create-POST-v2/

---

Assets

POST

# assets:batch-create V2

Creates a set of new assets.

This endpoint accepts an array of asset definitions, one definition for each asset. Each definition specifies a
category for the asset. The status and any custom attributes assigned to the asset must come from the status
set and the custom attributes assigned to the category.

To find the status set assigned to a category, use [POST category-status-step-sets/status-step-sets:batch-get](http-assets-category-status-step-sets-status-step-sets-batch-get-POST.md).

To find the custom attributes assigned to a category, use [GET categories/:categoryId/custom-attributes](http-assets-categories-category-id-custom-attributes-GET.md).

To understand the basics of assets and the Assets settings that define them, see the [Assets Field Guide](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/assets/).

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/assets/v2/projects/{projectId}/assets:batch-create |
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

| projectId   string | The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form “b.{UUID}”. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

An array of `NewAssetV2` objects for batch creating many Assets

Expand all

| clientAssetId*   string | An identifying name for the asset such as “laundry 220V outlet”. The name need not be unique, and shouldn’t be confused with the asset ‘id’ field, which is created and assigned when the asset is created. This value appears as “Asset ID” in the Assets UI, and may sometimes be called “Name” in asset exports. |
| --- | --- |
| categoryId*   string | The ID of the category to which the asset belongs. |
| statusId*   string: UUID | The ID of the status assigned to the asset. The status must belong to the status set specified by the asset’s category. |
| description   string | A brief description of the asset. Currently limited to `1000` characters. |
| locationId   string: UUID | The ID of the location of the asset. This value is supplied through the Locations API. |
| barcode   string | A string that lists a barcode value that may be assigned to the asset. The string uses whatever format your barcode system supports. |
| customAttributes   object | An optional JSON dictionary specifying one or more custom attributes and values to be assigned to the asset. The custom attributes must belong to the set of custom attributes specified by the asset’s category. <br>The dictionary is a set of key:value pairs that each starts with the unique custom attribute name (not to be confused with the custom attribute’s display name) followed by the attribute value. The value must use the data type defined by the attribute:<br>For `text`, the value is a string.<br>For `date`, the value is an ISO8601 date string with no time, for example, “2020-04-10”.<br>For `select`, the value is a valid ID from the list of values defined for this custom attribute.<br>For `multi-select`, the value is an array of valid IDs from the list of values defined for this custom attribute.<br>For `boolean`, the value is a boolean.<br>For `numeric`, the value is a string that parses as a valid floating point number (not localized). |
| *   one of |  |
| 0   string | A String value <br>Max length: 250 |
| 1   array: string | An array of String values |
| 2   boolean | A Boolean value |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Successfully created new assets. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request header |
| 401   Unauthorized | The request was not accepted because it lacked valid authentication credentials |
| 403   Forbidden | The request was not accepted because the client is authenticated, but is not authorized to access the target resource |
| 404   Not Found | The resource cannot be found |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the target resource |
| 429   Too Many Requests | The request was not accepted because the rate limit was exceeded due to too many requests being made. |
| 500   Internal Server Error | An unexpected error occurred on the server |

### Response

## [Body Structure (201)](#body-structure-201)

Expand all

| results   array: object | Returned assets |
| --- | --- |
| id   string | The ID of the component. |
| createdAt   string | The time when the component was created (ISO8601 Date time format in UTC). |
| createdBy   string | The actor that created the component. This is an Autodesk / Oxygen ID. |
| updatedAt   string | The time when the component was last updated (ISO8601 Date time format in UTC). |
| updatedBy   string | The actor that last updated the component. This is an Autodesk / Oxygen ID. |
| deletedAt   string | The time when the component was deleted at (ISO8601 Date time format in UTC). |
| deletedBy   string | The actor that deleted the component. This is an Autodesk / Oxygen ID. |
| isActive   boolean | A flag indicating whether the component is active or inactive (`isActive` is `true` if-and-only-if `deletedAt` is empty). |
| version   int | A global sequence number that is incremented any time a component of this type is created, updated, or deleted. If you cache components, you can use the version value to compare the cached component to the same component online to see if the component has been updated. If the online component has a higher version value, it has been updated. |
| clientAssetId   string | An identifying name for the asset such as “laundry 220V outlet”. The name need not be unique, and shouldn’t be confused with the asset ‘id’ field, which is created and assigned when the asset is created. This value appears as “Asset ID” in the Assets UI, and may sometimes be called “Name” in asset exports. |
| categoryId   string | The ID of the category to which the asset belongs. |
| statusId   string: UUID | The ID of the status assigned to the asset. The status must belong to the status set specified by the asset’s category. |
| description   string | A brief description of the asset. Currently limited to `1000` characters. |
| locationId   string: UUID | The ID of the location of the asset. This value is supplied through the Locations API. |
| barcode   string | A string that lists a barcode value that may be assigned to the asset. The string uses whatever format your barcode system supports. |
| customAttributes   object | An optional JSON dictionary specifying one or more custom attributes and values to be assigned to the asset. The custom attributes must belong to the set of custom attributes specified by the asset’s category. <br>The dictionary is a set of key:value pairs that each starts with the unique custom attribute name (not to be confused with the custom attribute’s display name) followed by the attribute value. The value must use the data type defined by the attribute:<br>For `text`, the value is a string.<br>For `date`, the value is an ISO8601 date string with no time, for example, “2020-04-10”.<br>For `select`, the value is a valid ID from the list of values defined for this custom attribute.<br>For `multi-select`, the value is an array of valid IDs from the list of values defined for this custom attribute.<br>For `boolean`, the value is a boolean.<br>For `numeric`, the value is a string that parses as a valid floating point number (not localized). |
| *   one of |  |
| 0   string | A String value <br>Max length: 250 |
| 1   array: string | An array of String values |
| 2   boolean | A Boolean value |
| companyId   string: UUID | The ID of the company to which the creating user belongs in the project. |

## [Example](#example)

Successfully created new assets.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/assets/v2/projects/:projectId/assets:batch-create' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '[
        {
          "clientAssetId": "MVS-3D2",
          "categoryId": "42",
          "statusId": "84eb6a10-dde3-475f-aaf4-b5df3aebbd0b",
          "description": "AC unit for basement",
          "locationId": "826e102a-36de-41e7-8c58-1b1696ccbba8",
          "barcode": "F0086728",
          "customAttributes": {
            "ca1": true,
            "ca2": 6.5,
            "ca4": "688f8cfb-0eb4-4289-9d18-96007875dec3",
            "ca5": [
              "9e653094-8d9e-4050-a97a-24d9c5a3786f",
              "e88357bc-e3dd-4cd8-a9e2-6d659b301e7f"
            ],
            "ca6": "text value"
          }
        }
      ]'

```

Show More

### Response

```
{
  "results": [
    {
      "id": "b302d910-b5e3-46ba-81d8-6b6d30406e14",
      "createdAt": "2020-05-01T06:00:00.000Z",
      "createdBy": "LA7ZL85MU7ML",
      "updatedAt": "2020-05-01T06:00:00.000Z",
      "updatedBy": "LA7ZL85MU7ML",
      "deletedAt": "2020-05-01T06:00:00.000Z",
      "deletedBy": "LA7ZL85MU7ML",
      "isActive": true,
      "version": 1,
      "clientAssetId": "MVS-3D2",
      "categoryId": "42",
      "statusId": "84eb6a10-dde3-475f-aaf4-b5df3aebbd0b",
      "description": "AC unit for basement",
      "locationId": "826e102a-36de-41e7-8c58-1b1696ccbba8",
      "barcode": "F0086728",
      "customAttributes": {
        "ca1": true,
        "ca2": 6.5,
        "ca4": "688f8cfb-0eb4-4289-9d18-96007875dec3",
        "ca5": [
          "9e653094-8d9e-4050-a97a-24d9c5a3786f",
          "e88357bc-e3dd-4cd8-a9e2-6d659b301e7f"
        ],
        "ca6": "text value"
      },
      "companyId": "07b5f07d-c54a-4236-a086-f84192fabdb3"
    }
  ]
}

```

Show More
