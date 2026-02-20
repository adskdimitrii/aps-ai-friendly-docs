# categories/:categoryId/custom-attributes/:customAttributeId

Source: https://aps.autodesk.com/en/docs/acc/reference/http/assets-categories-category-id-custom-attributes-custom-attribute-id-PUT/

---

# categories/:categoryId/custom-attributes/:customAttributeId

Assigns an Asset custom attribute to a category.

This endpoint specifies a category and a custom attribute to assign to that category. It returns an array of
all custom attributes assigned to the category, and can either include or exclude inherited attributes. If it
excludes inherited attributes, it returns only attributes explicitly assigned to the category.

Note that although the endpoint returns pagination fields for API consistency, the endpoint does not support
pagination. All assigned custom attributes, explicit or inherited, will be returned in the first page of
results.

To understand the basics of custom attributes, inheritance, and the Assets settings that define them, see the Assets Field Guide .

## Resource Information

Method and URI PUT https://developer.api.autodesk.com/construction/assets/v1/projects/{projectId}/categories/{categoryId}/custom-attributes/{customAttributeId} Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow.

### Request

## URI Parameters

projectId string The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form âb.{UUID}â. categoryId string The category ID customAttributeId string: UUID Asset custom attribute ID

### Request

## Query String Parameters

includeInherited boolean Specifies whether or not to return custom attributes that were inherited from the specified categoryâs
parent category. If true , then it returns inherited custom attributes. If false , then it returns only custom
attributes explicitly assigned to the specified category. Default is false .

### Response

## HTTP Status Code Summary

200 OK Successfully assigned an Asset custom attribute to a category. 400 Bad Request The request could not be understood by the server due to malformed syntax or missing request header 401 Unauthorized The request was not accepted because it lacked valid authentication credentials 403 Forbidden The request was not accepted because the client is authenticated, but is not authorized to access the target resource 404 Not Found The resource cannot be found 409 Conflict The request could not be completed due to a conflict with the current state of the target resource 429 Too Many Requests The request was not accepted because the rate limit was exceeded due to too many requests being made. 500 Internal Server Error An unexpected error occurred on the server

### Response

## Body Structure (200)

pagination object The pagination object. limit int The maximum number of objects that can be returned in a page. A request might return fewer objects than
the limit if the Assets service runs out of specified objects to return - at the end of a set of paged
results, for example. The maximum limit is 200 ; the default limit is 25 . offset int The offset of the first entry in the pagination results. totalResults int Total number of results available. results array: object Result custom attributes displayName string The human-readable display name for the Asset custom attribute. This name appears when viewing the custom
attribute in the Assets UI, and must be unique within a project. Max length: 100 description string A description of the Asset custom attribute. Max length: 1000 enumValues array: string An array of string values that defines possible values that may be supplied when this custom attributes data
type (defined by dataType ) is set to select or multi_select . This field is required when the data
type is set to select or multi_select . requiredOnIngress boolean Specifies whether or not this custom attribute is required when creating or editing an asset. If true , the
custom attribute is required. If false , it is not required. Setting this field to true does not guarantee
that existing or imported assets will have this custom attribute. maxLengthOnIngress int The maximum length that a text value can be for this custom attribute when creating or editing an asset.
Setting a value for this field does not guarantee that existing or imported assets with this custom
attribute will have this attributeâs value limited to this length. This field only applies when datatype
is set to text . Default is 250 , which is the maximum value this field can be set to. defaultValue one of The default value for this custom attribute if no value is specified on asset creation. If this field is not
specified, the custom attribute does not have a default value. The default value it takes can be any one of
three possible value types, defined below. 0 string A String value, maximum length: 250 Max length: 250 1 array: string An array of string values that are set for a multi_select custom attribute. 2 boolean A Boolean value dataType enum:string The data type that this custom attributeâs value must take. Once set, the data type canât be changed.
Possible values: boolean : true or false text : a string numeric : a string that parses as a valid floating point number (not localized) date : an ISO8601 date string with no time, for example, â2021-04-01â. select : a valid ID from the list of values defined by enumValues . multi_select : an array of valid IDs from the list of values defined by enumValues . id string The ID of the component. createdAt string The time when the component was created (ISO8601 Date time format in UTC). createdBy string The actor that created the component. This is an Autodesk / Oxygen ID. updatedAt string The time when the component was last updated (ISO8601 Date time format in UTC). updatedBy string The actor that last updated the component. This is an Autodesk / Oxygen ID. deletedAt string The time when the component was deleted at (ISO8601 Date time format in UTC). deletedBy string The actor that deleted the component. This is an Autodesk / Oxygen ID. isActive boolean A flag indicating whether the component is active or inactive ( isActive is true if-and-only-if deletedAt is empty). version int A global sequence number that is incremented any time a component of this type is created, updated, or deleted. If you cache components, you can use the version value to compare the cached component to the same component online to see if the component has been updated. If the online component has a higher version value, it has been updated. projectId string: UUID The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form âb.{UUID}â. name string An autogenerated value, created when an Asset custom attribute is created. The name does not change
over the life of the custom attribute. values array: object An array of objects that describe the select values for select and multi_select Asset custom
attributes. id string The ID of the component. createdAt string The time when the component was created (ISO8601 Date time format in UTC). createdBy string The actor that created the component. This is an Autodesk / Oxygen ID. updatedAt string The time when the component was last updated (ISO8601 Date time format in UTC). updatedBy string The actor that last updated the component. This is an Autodesk / Oxygen ID. deletedAt string The time when the component was deleted at (ISO8601 Date time format in UTC). deletedBy string The actor that deleted the component. This is an Autodesk / Oxygen ID. isActive boolean A flag indicating whether the component is active or inactive ( isActive is true if-and-only-if deletedAt is empty). version int A global sequence number that is incremented any time a component of this type is created, updated, or deleted. If you cache components, you can use the version value to compare the cached component to the same component online to see if the component has been updated. If the online component has a higher version value, it has been updated. projectId string: UUID The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form âb.{UUID}â. customAttributeId string: UUID The ID of the custom attribute. displayName string The display name of the value. Must be unique within the custom attribute (case-insensitive). Use to
generate the enumValues field for the custom attribute. inheritedFromCategoryId string The ID of the category from which this custom attribute was inherited - that is, the ancestor category
to which the inherited custom attribute was explicitly assigned. This field is only present when this
endpoint is set to return inherited custom attributes.

Max length: 100

Max length: 1000

Max length: 250

- boolean : true or false

- text : a string

- numeric : a string that parses as a valid floating point number (not localized)

- date : an ISO8601 date string with no time, for example, â2021-04-01â.

- select : a valid ID from the list of values defined by enumValues .

- multi_select : an array of valid IDs from the list of values defined by enumValues .

## Example

Successfully assigned an Asset custom attribute to a category.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/assets/v1/projects/:projectId/categories/123/custom-attributes/3063f212-6ce9-494e-b749-eb73b4445bf0' \ -X 'PUT' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "pagination" : { "limit" : 25 , "offset" : 0 , "totalResults" : 100 }, "results" : [ { "displayName" : "Elevator Speed" , "description" : "The average speed of an elevator in meters per second" , "enumValues" : [ "Custom Select Value" ], "requiredOnIngress" : true , "maxLengthOnIngress" : 100 , "defaultValue" : "2019-01-01" , "dataType" : "multi_select" , "id" : "b302d910-b5e3-46ba-81d8-6b6d30406e14" , "createdAt" : "2020-05-01T06:00:00.000Z" , "createdBy" : "LA7ZL85MU7ML" , "updatedAt" : "2020-05-01T06:00:00.000Z" , "updatedBy" : "LA7ZL85MU7ML" , "deletedAt" : "2020-05-01T06:00:00.000Z" , "deletedBy" : "LA7ZL85MU7ML" , "isActive" : true , "version" : 1 , "projectId" : "f74a012c-62fd-4988-ac2b-c5b4fd937724" , "name" : "ca1" , "values" : [ { "id" : "b302d910-b5e3-46ba-81d8-6b6d30406e14" , "createdAt" : "2020-05-01T06:00:00.000Z" , "createdBy" : "LA7ZL85MU7ML" , "updatedAt" : "2020-05-01T06:00:00.000Z" , "updatedBy" : "LA7ZL85MU7ML" , "deletedAt" : "2020-05-01T06:00:00.000Z" , "deletedBy" : "LA7ZL85MU7ML" , "isActive" : true , "version" : 1 , "projectId" : "f74a012c-62fd-4988-ac2b-c5b4fd937724" , "customAttributeId" : "3063f212-6ce9-494e-b749-eb73b4445bf0" , "displayName" : "Custom Select Value" } ], "inheritedFromCategoryId" : "123" } ] }
```
