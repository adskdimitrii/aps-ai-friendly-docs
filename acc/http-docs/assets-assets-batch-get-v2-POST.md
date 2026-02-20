# assets:batch-get V2

Source: https://aps.autodesk.com/en/docs/acc/reference/http/assets-assets-batch-get-v2-POST/

---

# assets:batch-get V2

Returns a specified set of assets.

This endpoint accepts an object with an array of one or more asset IDs and returns an array of assets
corresponding to each of those IDs. Invalid asset IDs will simply be omitted from the response and the client
is responsible for identifying missing results.

To understand the basics of assets and the Assets settings that define them, see the Assets Field Guide .

## Resource Information

Method and URI POST https://developer.api.autodesk.com/construction/assets/v2/projects/{projectId}/assets:batch-get Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json

### Request

## URI Parameters

projectId string The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form âb.{UUID}â.

### Request

## Query String Parameters

includeCustomAttributes boolean Specifies whether or not returned assets include custom attributes or not. If true , theyâre included. If false , theyâre not. Default is false . includeDeleted boolean Whether or not soft-deleted object should be included in the response. If true , soft-deleted objects are returned. If false , they are not. The default is false .

### Request

## Body Structure

Request payload for fetching a batch of assets by IDs

ids array: string An array of unique IDs of assets to fetch.

### Response

## HTTP Status Code Summary

200 OK Successfully returned a batch of assets. 400 Bad Request The request could not be understood by the server due to malformed syntax or missing request header 401 Unauthorized The request was not accepted because it lacked valid authentication credentials 403 Forbidden The request was not accepted because the client is authenticated, but is not authorized to access the target resource 404 Not Found The resource cannot be found 429 Too Many Requests The request was not accepted because the rate limit was exceeded due to too many requests being made. 500 Internal Server Error An unexpected error occurred on the server

### Response

## Body Structure (200)

results array: object Returned assets id string The ID of the component. createdAt string The time when the component was created (ISO8601 Date time format in UTC). createdBy string The actor that created the component. This is an Autodesk / Oxygen ID. updatedAt string The time when the component was last updated (ISO8601 Date time format in UTC). updatedBy string The actor that last updated the component. This is an Autodesk / Oxygen ID. deletedAt string The time when the component was deleted at (ISO8601 Date time format in UTC). deletedBy string The actor that deleted the component. This is an Autodesk / Oxygen ID. isActive boolean A flag indicating whether the component is active or inactive ( isActive is true if-and-only-if deletedAt is empty). version int A global sequence number that is incremented any time a component of this type is created, updated, or deleted. If you cache components, you can use the version value to compare the cached component to the same component online to see if the component has been updated. If the online component has a higher version value, it has been updated. clientAssetId string An identifying name for the asset such as âlaundry 220V outletâ. The name need not be unique, and shouldnât be confused with the asset âidâ field, which is created and assigned when the asset is created. This value appears as âAsset IDâ in the Assets UI, and may sometimes be called âNameâ in asset exports. categoryId string The ID of the category to which the asset belongs. statusId string: UUID The ID of the status assigned to the asset. The status must belong to the status set specified by the assetâs category. description string A brief description of the asset. Currently limited to 1000 characters. locationId string: UUID The ID of the location of the asset. This value is supplied through the Locations API. barcode string A string that lists a barcode value that may be assigned to the asset. The string uses whatever format your barcode system supports. customAttributes object An optional JSON dictionary specifying one or more custom attributes and values to be assigned to the
asset. The custom attributes must belong to the set of custom attributes specified by the assetâs category. The dictionary is a set of key:value pairs that each starts with the unique custom attribute name (not to
be confused with the custom attributeâs display name) followed by the attribute value. The value must use
the data type defined by the attribute: For text , the value is a string. For date , the value is an ISO8601 date string with no time, for example, â2020-04-10â. For select , the value is a valid ID from the list of values defined for this custom attribute. For multi-select , the value is an array of valid IDs from the list of values defined for this custom attribute. For boolean , the value is a boolean. For numeric , the value is a string that parses as a valid floating point number (not localized). * one of 0 string A String value Max length: 250 1 array: string An array of String values 2 boolean A Boolean value companyId string: UUID The ID of the company to which the creating user belongs in the project.

The dictionary is a set of key:value pairs that each starts with the unique custom attribute name (not to
be confused with the custom attributeâs display name) followed by the attribute value. The value must use
the data type defined by the attribute:

For text , the value is a string.

For date , the value is an ISO8601 date string with no time, for example, â2020-04-10â.

For select , the value is a valid ID from the list of values defined for this custom attribute.

For multi-select , the value is an array of valid IDs from the list of values defined for this custom attribute.

For boolean , the value is a boolean.

For numeric , the value is a string that parses as a valid floating point number (not localized).

Max length: 250

## Example

Successfully returned a batch of assets.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/assets/v2/projects/:projectId/assets:batch-get?includeCustomAttributes=true&includeDeleted=true' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "ids": [ "6cdd4356-a719-4964-9fd7-0c505e731ac7" ] }'
```

### Response

```
{ "results" : [ { "id" : "b302d910-b5e3-46ba-81d8-6b6d30406e14" , "createdAt" : "2020-05-01T06:00:00.000Z" , "createdBy" : "LA7ZL85MU7ML" , "updatedAt" : "2020-05-01T06:00:00.000Z" , "updatedBy" : "LA7ZL85MU7ML" , "deletedAt" : "2020-05-01T06:00:00.000Z" , "deletedBy" : "LA7ZL85MU7ML" , "isActive" : true , "version" : 1 , "clientAssetId" : "MVS-3D2" , "categoryId" : "42" , "statusId" : "84eb6a10-dde3-475f-aaf4-b5df3aebbd0b" , "description" : "AC unit for basement" , "locationId" : "826e102a-36de-41e7-8c58-1b1696ccbba8" , "barcode" : "F0086728" , "customAttributes" : { "ca1" : true , "ca2" : 6.5 , "ca4" : "688f8cfb-0eb4-4289-9d18-96007875dec3" , "ca5" : [ "9e653094-8d9e-4050-a97a-24d9c5a3786f" , "e88357bc-e3dd-4cd8-a9e2-6d659b301e7f" ], "ca6" : "text value" }, "companyId" : "07b5f07d-c54a-4236-a086-f84192fabdb3" } ] }
```
