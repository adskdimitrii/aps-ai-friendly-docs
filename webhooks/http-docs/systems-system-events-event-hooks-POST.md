# systems/:system/events/:event/hooks

Source: https://aps.autodesk.com/en/docs/webhooks/reference/http/webhooks/systems-system-events-event-hooks-POST/

---

POST

# systems/:system/events/:event/hooks

Add new webhook to receive the notification on a specified event.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/webhooks/v1/systems/:system/events/:event/hooks |
| --- | --- |
| Authentication Context | app only/ user context required |
| Required OAuth Scopes | `data:read` `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [OAuth](/en/docs/oauth/v2/reference/http/gettoken-POST) |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| x-ads-region   string | Specifies the geographical location (region) of the server that the request is executed on. Supported values are the following, but the default value is `US`: <br>`US` : (Default) Register a new webhook in a data center dedicated to serve the United States.`EMEA` : Register a new webhook in a data center dedicated to serve the European Union, Middle East, and Africa.`AUS` : (Beta) Register a new webhook in a data center dedicated to serve Australia.`GBR` : Register a new webhook in a data center dedicated to serve United Kingdom.`JPN` : Register a new webhook in a data center dedicated to serve Japan.`DEU` : Register a new webhook in a data center dedicated to serve Germany.`CAN` : Register a new webhook in a data center dedicated to serve Canada.`IND` : Register a new webhook in a data center dedicated to serve India. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| system   string | A system for example: `data`   for Data Management |
| --- | --- |
| event   string | Type of event. See [Supported Events](/en/docs/webhooks/v1/reference/events) |

### Request

## [Query String Parameters](#query-string-parameters)

| region   string | Specifies the geographical location (region) of the server that the request is executed on. Supported values are the following, but the default value is `US`: <br>`US` : (Default) Processes request in a data center dedicated to serve the United States.`EMEA` : Processes request in a data center dedicated to serve the European Union, Middle East, and Africa.`AUS` : (Beta) Processes request in a data center dedicated to serve Australia.<br>The `x-ads-region` header also specifies the region. If you specify both, `x-ads-region` has precedence. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

| callbackUrl*   string | Callback URL registered for the webhook |
| --- | --- |
| scope*   object | An object that represents the extent to where the event is monitored. For example, if the scope is folder, the webhooks service generates a notification for the specified event occurring in any sub folder or item within that folder. Please refer to the individual event specification pages for valid scopes. For example, [Data Management events](/en/docs/webhooks/v1/reference/events/data_management_events). |
| hookAttribute   object | A user-defined JSON object, which you can use to store/set some custom information. The maximum size of the JSON object (content) should be less than 1KB |
| filter   string | JsonPath expression that can be used by you to filter the callbacks you receive. |
| hubId   string | Optional field which should be provided if the user is a member of a large number of projects. This hub ID corresponds to an account ID in the BIM 360 API, prefixed by âb.â |
| projectId   string | Optional field which should be provided if the user is a member of a large number of projects. This project ID corresponds to the project ID in the BIM 360 API, prefixed by âb.â |
| tenant   string | The tenant that the event is from. If the tenant is specified on the hook, then either the tenant or the scopeValue of the event must match the tenant of the hook. |
| autoReactivateHook   boolean | Optional. Flag to enable the hook for the automatic reactivation flow. Please see [Event Delivery Guarantees](/en/docs/webhooks/v1/developers_guide/event-delivery-guarantees) for more details. |
| hookExpiry   string | Optional. ISO8601 formatted date and time when the hook should expire and automatically be deleted. Not providing this parameter means the hook never expires. |
| callbackWithEventPayloadOnly   boolean | Optional. If âtrueâ, the callback request payload only contains the event payload, without additional information on the hook. Hook attributes will not be accessible if this is âtrueâ. Defaults to âfalseâ. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   OK | Successful. |
| --- | --- |
| 400   BAD REQUEST | The request is invalid. |
| 401   UNAUTHORIZED | Invalid authorization header. |
| 403   FORBIDDEN | Access denied regardless of authorization status. |
| 404   NOT FOUND | The specified resource was not found. |
| 409   CONFLICT | The specified webhook already exists. |
| 500   INTERNAL SERVICE ERROR | Unexpected service interruption |

## [Example](#example)

### Successful Creation of a webhook (201)

### Request

```
curl -X 'POST'\
     -v 'https://developer.api.autodesk.com/webhooks/v1/systems/data/events/dm.version.added/hooks'\
     -H 'Content-Type: application/json'\
     -H 'authorization: Bearer bNU4P0trbQKNSzxWksLPTzSbbmUz'\
     -d '{
            "callbackUrl": "http://bf067e05.ngrok.io/callback",
            "autoReactivateHook": false,
            "scope": {
                 "folder": "urn:adsk.wipprod:fs.folder:co.wT5lCWlXSKeo3razOfHJAw"
            },
            "hookAttribute": {
                 /* Custom metadata */
                 "myfoo": 33,
                 "projectId": "someURN",
                 "myobject": {
                      "nested": true
                 }
            },
            "hookExpiry": "2017-09-21T17:04:10.444Z"
      }'

```

Show More

### Response

```
HTTP/1.1 201
Date: Thu, 14 Sep 2017 16:45:05 GMT
Location: https://developer.api.autodesk.com/webhooks/v1/systems/data/events/dm.version.added/hooks/0f60f6a0-996c-11e7-abf3-51d68cff984c
Content-Length: 0
Connection: keep-alive

```
