# appbundles/:id/aliases/:aliasId

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/appbundles-id-aliases-aliasId-PATCH/

---

# appbundles/:id/aliases/:aliasId

Modify alias details.

## Resource Information

Method and URI PATCH https://developer.api.autodesk.com/da/us-east/v3/appbundles/:id/aliases/:aliasId Authentication Context app only Required OAuth Scopes code:all Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via OAuth Content-Type * string Must be application/json

### Request

## URI Parameters

id string Name of AppBundle (unqualified). aliasId string Name of alias.

### Request

## Body Structure

receiver string or array: string The user(s) to share the alias with. version int The version that this alias refers to.

### Response

## HTTP Status Code Summary

200 OK Successfully modify an AppBundleâs alias. 400 Bad Request The request is invalid. 403 Forbidden Maximum number of items exceeded. 404 Not Found Not found. 409 Conflict An item with this name already exists. 500 Internal Server Error Unknown error.

### Response

## Body Structure (200)

version int The version that this alias refers to. receiver string or array: string The user(s) to share the alias with. id string The alias id.

## Example

Successfully modify an AppBundleâs alias.

### Request

```
curl - v 'https://developer.api.autodesk.com/da/us-east/v3/appbundles/:id/aliases/:aliasId' \ - X 'PATCH' \ - H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ - H 'Content-Type: application/json' \ - d '{ "version": 1 }'
```

### Response

```
{ "version" : 1 , "id" : "prod" }
```
