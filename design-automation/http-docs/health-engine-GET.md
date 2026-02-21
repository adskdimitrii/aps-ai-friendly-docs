# health/:engine

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/health-engine-GET/

---

# health/:engine

Gets the health status by Engine or for all Engines (Inventor, AutoCAD â¦).

## Resource Information

Method and URI GET https://developer.api.autodesk.com/da/us-east/v3/health/:engine Authentication Context app only Required OAuth Scopes code:all Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via OAuth

### Request

## URI Parameters

engine string engine name, e.g. AutoCAD

### Response

## HTTP Status Code Summary

200 OK Successfully get the health status. 403 Forbidden Unauthorized 404 Not Found Not found. 500 Internal Server Error Unknown error.

## Example

Successfully get the health status.

### Request

```
curl - v 'https://developer.api.autodesk.com/da/us-east/v3/health/:engine'
```

### Response

```
{ "Status" : "Fully Operational" }
```
