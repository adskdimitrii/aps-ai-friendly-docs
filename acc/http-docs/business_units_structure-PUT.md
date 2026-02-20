# business_units_structure

Source: https://aps.autodesk.com/en/docs/acc/reference/http/business_units_structure-PUT/

---

# business_units_structure

Creates or redefines the business units of a specific BIM 360 account.

## Resource Information

Method and URI PUT https://developer.api.autodesk.com/hq/v1/accounts/:account_id/business_units_structure Method and URIï¼Legacyï¼ PUT https://developer.api.autodesk.com/hq/v1/regions/eu/accounts/:account_id/business_units_structure Authentication Context app only Required OAuth Scopes account:write Data Formats JSON

### Request

## Headers

Authorization yes Must be Bearer <token> , where <token> is obtained via a two-legged OAuth flow. Content-Type yes Must be application/json . Region no Specifies the region where the service is located.                                                                                                        Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

account_id string: UUID The account ID of the business unit. This corresponds to hub ID in the Data Management API . To convert a hub ID into an account ID you need to remove the â b. " prefix. For example, a hub ID of b. c8b0c73d-3ae9 translates to an account ID of c8b0c73d-3ae9.

### Request

## Body Structure

The PUT body is a single business_units attribute that holds an array of business units, JSON objects with the following attributes:

business_units array:object id string: UUID Business unit ID If specified and already existing, the existing business unit will be replaced with the provided attributes. If specified and not already existing, a new business unit will be created with the id . If unspecified, a new business unit will be created with a server-generated id . parent_id string: UUID The ID of the parent business unit Note that an entire business unit hierarchy can be created by manually specifying the id attribute for each business unit and using it as appropriate in other parent_id attributes. name * string The name of the business unit description string The description of the business unit

### Response

## HTTP Status Code Summary

200 OK The request has succeeded. 400 Bad Request The request could not be understood by the server due to malformed syntax. 403 Forbidden Unauthorized. 404 Not Found The resource cannot be found. 409 Conflict The request could not be completed due to a conflict with the current state of the resource. 422 Unprocessable Entity The request was unable to be followed due to restrictions. 500 Internal Server Error An unexpected error occurred on the server.

### Response

## Body Structure (200)

A successful response is an array of the created or modified business units, of flat JSON objects with the following attributes:

business_units array:object id string: UUID Business unit ID account_id string: UUID Account ID parent_id string: UUID The ID of the parent business unit name string The name of the business unit path string The path of the business unit in the tree structure description string The description of the business unit created_at updated_at

## Example

Successful Updating Account Business Units (200)

### Request

```
curl -v 'https://developer.api.autodesk.com/hq/v1/accounts/e3d5ef8d-5c37-4b9d-925d-1e6d24753ace/business_units_structure' \ -X 'PUT' \ -H 'Content-Type: application/json' \ -H 'Authorization: Bearer 9ezBnx9Rd5D1xG4KMt6b72T4w0MG' \ -d '{ "business_units": [ { "id": "933df8fd-abb2-4e4e-8f79-95ba2afebc6c", "parent_id": null, "name": "North America", "description": "USA, Canada" }, { "id": "fda4ab9e-ab82-4ba9-8d6c-ae7dbd7cee31", "parent_id": "933df8fd-abb2-4e4e-8f79-95ba2afebc6c", "name": "USA Western Region", "description": "California, Nevada, Washington" } ] }'
```

### Response

```
{ "business_units" : [ { "id" : "933df8fd-abb2-4e4e-8f79-95ba2afebc6c" , "account_id" : "e3d5ef8d-5c37-4b9d-925d-1e6d24753ace" , "parent_id" : null , "name" : "North America" , "description" : "USA, Canada" , "path" : null , "created_at" : "2016-04-11T03:49:09.176Z" , "updated_at" : "2016-04-11T03:49:09.176Z" }, { "id" : "fda4ab9e-ab82-4ba9-8d6c-ae7dbd7cee31" , "account_id" : "e3d5ef8d-5c37-4b9d-925d-1e6d24753ace" , "parent_id" : "933df8fd-abb2-4e4e-8f79-95ba2afebc6c" , "name" : "USA Western Region" , "description" : "California, Nevada, Washington" , "path" : "North America" , "created_at" : "2016-04-11T03:49:09.176Z" , "updated_at" : "2016-04-11T03:49:09.176Z" } ] }
```
