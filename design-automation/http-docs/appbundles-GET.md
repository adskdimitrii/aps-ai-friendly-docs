# appbundles

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/appbundles-GET/

---

# appbundles

Lists all available AppBundles, including AppBundles shared with this app.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/da/us-east/v3/appbundles Authentication Context app only Required OAuth Scopes code:all Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via OAuth

### Request

## Query String Parameters

page string Access an additional âpageâ of data when necessary, based on the âpaginationTokenâ returned from a previous invocation.

### Response

## HTTP Status Code Summary

200 OK Successfully get all AppBundles. 400 Bad Request Bad request. 403 Forbidden Unauthorized 500 Internal Server Error Unknown error.

### Response

## Body Structure (200)

paginationToken string data array: string

## Example

Successfully get all AppBundles.

### Request

```
curl - v 'https://developer.api.autodesk.com/da/us-east/v3/appbundles' \ - H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "paginationToken" : "" , "data" : [ "AutoCAD.Publish2View22+prod" , "Revit.RVTIOSandboxTestPackage2018+prod" , "Inventor.iLogicSampleAppPackage+prod" , "Inventor.Configuration+Beta" , "AutoCAD.Publish2View23+prod" , "Inventor.ChangeParams+prod" , "3dsMax.bakeToTexture+prod" , "Revit.RVTIOSketchItPackage2018+prod" ] }
```
