# custom-attributes

Source: https://aps.autodesk.com/en/docs/acc/reference/http/assets-custom-attributes-POST/

---

Custom-Attributes

POST

# custom-attributes

Creates a new Asset custom attribute.

This endpoint defines the custom attributeâs name and the value type that it must take. It may also define
further value parameters that depend on the specified value type. These parameters include whether or not the
custom attribute is required when the asset is being updated, what possible values are valid, and what default
values are set if no value is provided.

To understand the basics of custom attributes, and the Assets settings that define them, see the [Assets Field Guide](/en/docs/acc/v1/overview/field-guide/assets/).

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/assets/v1/projects/{projectId}/custom-attributes |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` `data:create` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string | The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form âb.{UUID}â. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| renameConflicting   boolean | Specifies that any inactive (deleted) entity with a conflicting name should be automatically renamed to avoid a conflict. Only supported by specific APIs. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

Expand all

| displayName*   string | The human-readable display name for the Asset custom attribute. This name appears when viewing the custom attribute in the Assets UI, and must be unique within a project. <br>Max length: 100 |
| --- | --- |
| description   string | A description of the Asset custom attribute. <br>Max length: 1000 |
| enumValues   array: string | An array of string values that defines possible values that may be supplied when this custom attributes data type (defined by `dataType`) is set to `select` or `multi_select`. This field is required when the data type is set to `select` or `multi_select`. |
| requiredOnIngress*   boolean | Specifies whether or not this custom attribute is required when creating or editing an asset. If `true`, the custom attribute is required. If `false`, it is not required. Setting this field to `true` does not guarantee that existing or imported assets will have this custom attribute. |
| maxLengthOnIngress   int | The maximum length that a text value can be for this custom attribute when creating or editing an asset. Setting a value for this field does not guarantee that existing or imported assets with this custom attribute will have this attributeâs value limited to this length. This field only applies when datatype is set to `text`. Default is `250`, which is the maximum value this field can be set to. |
| defaultValue   one of | The default value for this custom attribute if no value is specified on asset creation. If this field is not specified, the custom attribute does not have a default value. The default value it takes can be any one of three possible value types, defined below. |
| 0   string | A String value, maximum length: 250 <br>Max length: 250 |
| 1   array: string | An array of string values that are set for a `multi_select` custom attribute. |
| 2   boolean | A Boolean value |
| dataType*   enum:string | The data type that this custom attributeâs value must take. Once set, the data type canât be changed. Possible values: <br>`boolean`: `true` or `false``text`: a string`numeric`: a string that parses as a valid floating point number (not localized)`date`: an ISO8601 date string with no time, for example, â2021-04-01â.`select`: a valid ID from the list of values defined by `enumValues`.`multi_select`: an array of valid IDs from the list of values defined by `enumValues`. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Successfully created a new Asset custom attribute. |
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

| displayName   string | The human-readable display name for the Asset custom attribute. This name appears when viewing the custom attribute in the Assets UI, and must be unique within a project. <br>Max length: 100 |
| --- | --- |
| description   string | A description of the Asset custom attribute. <br>Max length: 1000 |
| enumValues   array: string | An array of string values that defines possible values that may be supplied when this custom attributes data type (defined by `dataType`) is set to `select` or `multi_select`. This field is required when the data type is set to `select` or `multi_select`. |
| requiredOnIngress   boolean | Specifies whether or not this custom attribute is required when creating or editing an asset. If `true`, the custom attribute is required. If `false`, it is not required. Setting this field to `true` does not guarantee that existing or imported assets will have this custom attribute. |
| maxLengthOnIngress   int | The maximum length that a text value can be for this custom attribute when creating or editing an asset. Setting a value for this field does not guarantee that existing or imported assets with this custom attribute will have this attributeâs value limited to this length. This field only applies when datatype is set to `text`. Default is `250`, which is the maximum value this field can be set to. |
| defaultValue   one of | The default value for this custom attribute if no value is specified on asset creation. If this field is not specified, the custom attribute does not have a default value. The default value it takes can be any one of three possible value types, defined below. |
| 0   string | A String value, maximum length: 250 <br>Max length: 250 |
| 1   array: string | An array of string values that are set for a `multi_select` custom attribute. |
| 2   boolean | A Boolean value |
| dataType   enum:string | The data type that this custom attributeâs value must take. Once set, the data type canât be changed. Possible values: <br>`boolean`: `true` or `false``text`: a string`numeric`: a string that parses as a valid floating point number (not localized)`date`: an ISO8601 date string with no time, for example, â2021-04-01â.`select`: a valid ID from the list of values defined by `enumValues`.`multi_select`: an array of valid IDs from the list of values defined by `enumValues`. |
| id   string | The ID of the component. |
| createdAt   string | The time when the component was created (ISO8601 Date time format in UTC). |
| createdBy   string | The actor that created the component. This is an Autodesk / Oxygen ID. |
| updatedAt   string | The time when the component was last updated (ISO8601 Date time format in UTC). |
| updatedBy   string | The actor that last updated the component. This is an Autodesk / Oxygen ID. |
| deletedAt   string | The time when the component was deleted at (ISO8601 Date time format in UTC). |
| deletedBy   string | The actor that deleted the component. This is an Autodesk / Oxygen ID. |
| isActive   boolean | A flag indicating whether the component is active or inactive (`isActive` is `true` if-and-only-if `deletedAt` is empty). |
| version   int | A global sequence number that is incremented any time a component of this type is created, updated, or deleted. If you cache components, you can use the version value to compare the cached component to the same component online to see if the component has been updated. If the online component has a higher version value, it has been updated. |
| projectId   string: UUID | The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form âb.{UUID}â. |
| name   string | An autogenerated value, created when an Asset custom attribute is created. The name does not change over the life of the custom attribute. |
| values   array: object | An array of objects that describe the select values for `select` and `multi_select` Asset custom attributes. |
| id   string | The ID of the component. |
| createdAt   string | The time when the component was created (ISO8601 Date time format in UTC). |
| createdBy   string | The actor that created the component. This is an Autodesk / Oxygen ID. |
| updatedAt   string | The time when the component was last updated (ISO8601 Date time format in UTC). |
| updatedBy   string | The actor that last updated the component. This is an Autodesk / Oxygen ID. |
| deletedAt   string | The time when the component was deleted at (ISO8601 Date time format in UTC). |
| deletedBy   string | The actor that deleted the component. This is an Autodesk / Oxygen ID. |
| isActive   boolean | A flag indicating whether the component is active or inactive (`isActive` is `true` if-and-only-if `deletedAt` is empty). |
| version   int | A global sequence number that is incremented any time a component of this type is created, updated, or deleted. If you cache components, you can use the version value to compare the cached component to the same component online to see if the component has been updated. If the online component has a higher version value, it has been updated. |
| projectId   string: UUID | The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form âb.{UUID}â. |
| customAttributeId   string: UUID | The ID of the custom attribute. |
| displayName   string | The display name of the value. Must be unique within the custom attribute (case-insensitive). Use to generate the `enumValues` field for the custom attribute. |

## [Example](#example)

Successfully created a new Asset custom attribute.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/assets/v1/projects/:projectId/custom-attributes?renameConflicting=true' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "displayName": "Elevator Speed",
        "description": "The average speed of an elevator in meters per second",
        "enumValues": [
          "Custom Select Value"
        ],
        "requiredOnIngress": true,
        "maxLengthOnIngress": 100,
        "defaultValue": "2019-01-01",
        "dataType": "multi_select"
      }'

```

Show More

### Response

```
{
  "displayName": "Elevator Speed",
  "description": "The average speed of an elevator in meters per second",
  "enumValues": [
    "Custom Select Value"
  ],
  "requiredOnIngress": true,
  "maxLengthOnIngress": 100,
  "defaultValue": "2019-01-01",
  "dataType": "multi_select",
  "id": "b302d910-b5e3-46ba-81d8-6b6d30406e14",
  "createdAt": "2020-05-01T06:00:00.000Z",
  "createdBy": "LA7ZL85MU7ML",
  "updatedAt": "2020-05-01T06:00:00.000Z",
  "updatedBy": "LA7ZL85MU7ML",
  "deletedAt": "2020-05-01T06:00:00.000Z",
  "deletedBy": "LA7ZL85MU7ML",
  "isActive": true,
  "version": 1,
  "projectId": "f74a012c-62fd-4988-ac2b-c5b4fd937724",
  "name": "ca1",
  "values": [
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
      "projectId": "f74a012c-62fd-4988-ac2b-c5b4fd937724",
      "customAttributeId": "3063f212-6ce9-494e-b749-eb73b4445bf0",
      "displayName": "Custom Select Value"
    }
  ]
}

```

Show More
