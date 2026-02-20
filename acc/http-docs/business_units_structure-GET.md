# business_units_structure

Source: https://aps.autodesk.com/en/docs/acc/reference/http/business_units_structure-GET/

---

# business_units_structure

Query all the business units in a specific BIM 360 account.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/hq/v1/accounts/:account_id/business_units_structure Method and URIï¼Legacyï¼ GET https://developer.api.autodesk.com/hq/v1/regions/eu/accounts/:account_id/business_units_structure Authentication Context app only Required OAuth Scopes account:read Data Formats JSON

### Request

## Headers

Authorization yes Must be Bearer <token> , where <token> is obtained via a two-legged OAuth flow. Region no Specifies the region where the service is located.                                                                                                        Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

account_id string: UUID The account ID of the business unit. This corresponds to hub ID in the Data Management API . To convert a hub ID into an account ID you need to remove the â b. " prefix. For example, a hub ID of b. c8b0c73d-3ae9 translates to an account ID of c8b0c73d-3ae9.

### Response

## HTTP Status Code Summary

200 OK The request has succeeded 400 Bad Request The request could not be understood by the server due to malformed syntax 403 Forbidden Unauthorized 404 Not Found The resource cannot be found 409 Conflict The request could not be completed due to a conflict with the current state of the resource. 422 Unprocessable Entity The request was unable to be followed due to restrictions 500 Internal Server Error An unexpected error occurred on the server

### Response

## Body Structure (200)

A successful response is a business unit, a flat JSON object with the following attributes:

business_units array:object id string: UUID Business unit ID account_id string: UUID Account ID parent_id string: UUID The ID of the parent business unit; used to configure the tree structure of business units name string The name of the business unit path string The path of the business unit in the tree structure description string The description of the business unit created_at updated_at

## Example

Successful Listing of Account Business Units (200)

### Request

```
curl -v 'https://developer.api.autodesk.com/hq/v1/accounts/e3d5ef8d-5c37-4b9d-925d-1e6d24753ace/business_units_structure' \ -H 'Authorization: Bearer 9ezBnx9Rd5D1xG4KMt6b72T4w0MG'
```

### Response

```
{ "business_units" :[ { "id" : "933df8fd-abb2-4e4e-8f79-95ba2afebc6c" , "account_id" : "e3d5ef8d-5c37-4b9d-925d-1e6d24753ace" , "parent_id" : null , "name" : "North America" , "description" : "USA, Canada" , "path" : null , "created_at" : "2016-04-11T03:49:09.176Z" , "updated_at" : "2016-04-11T03:49:09.176Z" }, { "id" : "fda4ab9e-ab82-4ba9-8d6c-ae7dbd7cee31" , "account_id" : "e3d5ef8d-5c37-4b9d-925d-1e6d24753ace" , "parent_id" : "933df8fd-abb2-4e4e-8f79-95ba2afebc6c" , "name" : "USA Western Region" , "description" : "California, Nevada, Washington" , "path" : "North America" , "created_at" : "2016-04-11T03:49:09.176Z" , "updated_at" : "2016-04-11T03:49:09.176Z" } ] }
```
