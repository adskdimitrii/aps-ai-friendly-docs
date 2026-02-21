# activities/:id/aliases

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/activities-id-aliases-POST/

---

# activities/:id/aliases

Creates a new alias for this Activity.

Limit:

- Number of aliases (LimitAliases).

## Resource Information

Method and URI POST https://developer.api.autodesk.com/da/us-east/v3/activities/:id/aliases Authentication Context app only Required OAuth Scopes code:all Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via OAuth Content-Type * string Must be application/json

### Request

## URI Parameters

id string Name of Activity (unqualified).

### Request

## Body Structure

version int The version that this alias refers to. receiver string or array: string The user(s) to share the alias with. id string The alias id. Only alphanumeric characters and _ (underscore) are allowed.

### Response

## HTTP Status Code Summary

200 OK Successfully create a new Activity alias. 400 Bad Request The request is invalid. 403 Forbidden Maximum number of items exceeded. 404 Not Found Not found. 409 Conflict An item with this name already exists. 500 Internal Server Error Unknown error.

### Response

## Body Structure (200)

version int The version that this alias refers to. receiver string or array: string The user(s) to share the alias with. id string The alias id.

## Example

Successfully create a new Activity alias.

### Request

```
curl - v 'https://developer.api.autodesk.com/da/us-east/v3/activities/:id/aliases' \ - X 'POST' \ - H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ - H 'Content-Type: application/json' \ - d '{ "version": 1, "id": "prod" }'
```

### Response

```
{ "version" : 1 , "id" : "prod" }
```
