# activities

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/activities-GET/

---

# activities

Lists all available Activities, including Activities shared with this app.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/da/us-east/v3/activities Authentication Context app only Required OAuth Scopes code:all Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via OAuth

### Request

## Query String Parameters

page string Access an additional âpageâ of data when necessary, based on the âpaginationTokenâ returned from a previous invocation.

### Response

## HTTP Status Code Summary

200 OK Successfully get all available Activities. 400 Bad Request Bad request. 403 Forbidden Unauthorized 500 Internal Server Error Unknown error.

### Response

## Body Structure (200)

paginationToken string data array: string

## Example

Successfully get all available Activities.

### Request

```
curl - v 'https://developer.api.autodesk.com/da/us-east/v3/activities' \ - H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "paginationToken" : "" , "data" : [ "Autodesk.Nop+Latest" , "AutoCAD.AcSvfPublish+prod" , "Revit.RvtIOSandboxTestActivity2018+prod" , "3dsMax.HelloWorld+Latest" , "Revit.RvtIOSketchItActivity2018+prod" , "Inventor.BasicPluginTest+prod" , "3dsMax.bakeToTexture+Latest" , "Inventor.iLogic_Volume2020+prod" , "AutoCAD.AcF2dPublish+prod" , "AutoCAD.AcLMVPublish+prod" , "AutoCAD.PlotToPDF+prod" , "Inventor.Configuration+Beta" , "Inventor.ChangeParams+prod" ] }
```
