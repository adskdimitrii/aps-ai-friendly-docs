# appbundles/:id/aliases/:aliasId

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/appbundles-id-aliases-aliasId-GET/

---

# appbundles/:id/aliases/:aliasId

Get alias details.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/da/us-east/v3/appbundles/:id/aliases/:aliasId Authentication Context app only Required OAuth Scopes code:all Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via OAuth

### Request

## URI Parameters

id string Name of AppBundle (unqualified). aliasId string Name of alias.

### Response

## HTTP Status Code Summary

200 OK Successfully get the details of an AppBundleâs alias. 403 Forbidden Unauthorized 404 Not Found Not found. 500 Internal Server Error Unknown error.

### Response

## Body Structure (200)

version int The version that this alias refers to. receiver string or array: string The user(s) to share the alias with. id string The alias id.

## Example

Successfully get the details of an AppBundleâs alias.

### Request

```
curl - v 'https://developer.api.autodesk.com/da/us-east/v3/appbundles/:id/aliases/:aliasId' \ - H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "version" : 1 , "id" : "prod" }
```
