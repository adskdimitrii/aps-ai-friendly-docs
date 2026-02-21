# appbundles/:id/aliases/:aliasId

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/appbundles-id-aliases-aliasId-DELETE/

---

# appbundles/:id/aliases/:aliasId

Deletes the alias.

## Resource Information

Method and URI DELETE https://developer.api.autodesk.com/da/us-east/v3/appbundles/:id/aliases/:aliasId Authentication Context app only Required OAuth Scopes code:all Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via OAuth

### Request

## URI Parameters

id string Name of AppBundle (unqualified). aliasId string Name of alias to delete.

### Response

## HTTP Status Code Summary

204 No Content OK. 400 Bad Request The request is invalid. 403 Forbidden Unauthorized 500 Internal Server Error Unknown error.

## Example

OK.

### Request

```
curl - v 'https://developer.api.autodesk.com/da/us-east/v3/appbundles/:id/aliases/:aliasId' \ - X 'DELETE' \ - H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
204 No Content
```
