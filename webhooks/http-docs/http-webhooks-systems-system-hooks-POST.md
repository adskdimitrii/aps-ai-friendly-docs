# systems/:system/hooks

Source: https://aps.autodesk.com/en/docs/webhooks/reference/http/webhooks/systems-system-hooks-POST/

---

POST

# systems/:system/hooks

Add new webhooks to receive the notification on all the events.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/webhooks/v1/systems/:system/hooks |
| --- | --- |
| Authentication Context | app only/ user context required |
| Required OAuth Scopes | `data:read` `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [OAuth](../../oauth/http-docs/http-gettoken-POST.md) |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| x-ads-region   string | Specifies the geographical location (region) of the server that the request is executed on. Supported values are the following, but the default value is `US`: <br>`US` : (Default) Register new webhooks in a data center dedicated to serve the United States.`EMEA` : Register new webhooks in a data center dedicated to serve the European Union, Middle East, and Africa.`AUS` : (Beta) Register new webhooks in a data center dedicated to serve Australia.`GBR` : Register new webhooks in a data center dedicated to serve United Kingdom.`JPN` : Register new webhooks in a data center dedicated to serve Japan.`DEU` : Register new webhooks in a data center dedicated to serve Germany.`CAN` : Register new webhooks in a data center dedicated to serve Canada.`IND` : Register new webhooks in a data center dedicated to serve India. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| system   string | A system for example: `data`   for Data Management |
| --- | --- |
| region   string | Optional parameter to specify the region the request will be run in. Supported values are the following, but the default value is `US`: <br>`US` :`EMEA` :`AUS` : (Beta) Australia (Beta)`GBR` : United Kingdom`JPN` : Japan`DEU` : Germany`CAN` : Canada`IND` : India<br>The `x-ads-region` header also specifies the region. If you specify both, `x-ads-region` has precedence. |

### Request

## [Body Structure](#body-structure)

| callbackUrl*   string | Callback URL registered for the webhook |
| --- | --- |
| scope*   object | An object that represents the extent to where the event is monitored. For example, if the scope is folder, the webhooks service generates a notification for the specified event occurring in any sub folder or item within that folder. Please refer to the individual event specification pages for valid scopes. For example, [Data Management events](https://aps.autodesk.com/en/docs/webhooks/v1/reference/events/data_management_events/). |
| hookAttribute   object | A user-defined JSON object, which you can use to store/set some custom information. The maximum size of the JSON object (content) should be less than 1KB |
| filter   string | JsonPath expression that can be used by you to filter the callbacks you receive. |
| hubId   string | Optional field which should be provided if the user is a member of a large number of projects. This hub ID corresponds to an account ID in the BIM 360 API, prefixed by âb.â |
| projectId   string | Optional field which should be provided if the user is a member of a large number of projects. This project ID corresponds to the project ID in the BIM 360 API, prefixed by âb.â |
| tenant   string | The tenant that the event is from. If the tenant is specified on the hook, then either the tenant or the scopeValue of the event must match the tenant of the hook. |
| autoReactivateHook   boolean | Optional. Flag to enable the hook for the automatic reactivation flow. Please see [Event Delivery Guarantees](https://aps.autodesk.com/en/docs/webhooks/v1/developers_guide/event-delivery-guarantees/) for more details. |
| hookExpiry   string | Optional. ISO8601 formatted date and time when the hook should expire and automatically be deleted. Not providing this parameter means the hook never expires. |
| callbackWithEventPayloadOnly   boolean | Optional. If âtrueâ, the callback request payload only contains the event payload, without additional information on the hook. Hook attributes will not be accessible if this is âtrueâ. Defaults to âfalseâ. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   OK | Successful creation of one or more hooks. |
| --- | --- |
| 400   BAD REQUEST | The request is invalid. |
| 401   UNAUTHORIZED | Invalid authorization header. |
| 403   FORBIDDEN | Access denied regardless of authorization status. |
| 404   NOT FOUND | The specified resource was not found. |
| 500   INTERNAL SERVICE ERROR | Unexpected service interruption |

### Response

## [Body Structure (201)](#body-structure-201)

| hooks   array: object | An array of webhook objects created by this request |
| --- | --- |
| hooks.hooks[i]   object | An element of the array. Represents a webhook |
| hooks.hooks[i].hookId   string | Webhook ID |
| hooks.hooks[i].callbackUrl   string | Callback URL registered for the webhook |
| hooks.hooks[i].createdBy   string | Client ID or User ID |
| hooks.hooks[i].createdDate   date | Date and time when webhook was created |
| hooks.hooks[i].event   string | Type of event that is being monitored. Wildcard values can potentially represent more than one event being monitored depending on the matching pattern. |
| hooks.hooks[i].scope   object | An object that represents the extent to where the event is monitored. For example, if the scope is folder, the webhooks service generates a notification for the specified event occurring in any sub folder or item within that folder |
| hooks.hooks[i].scope.folder   string | Data Management event scope, see [here](../how-to-docs/create-a-hook-data-management.md) for more information |
| hooks.hooks[i].scope.workflow   string | Model Derivative event scope, see [here](../how-to-docs/create-a-hook-model-derivative.md) for more information. |
| hooks.hooks[i].status   string | `active` if webhook is active; otherwise `inactive` |
| hooks.hooks[i].urn   string | URN of the webhook |
| hooks.hooks[i].hookExpiry   string | Optional: ISO8601 formatted date and time when the hook should expire and automatically be deleted. `null` or not present means the hook never expires. |
| hooks.hooks[i].__self__   string | Location of this webhook relative to `/webhooks/v1/` |

## [Example](#example)

Successful Creation of a webhook (201):

### Request

```
curl -X 'POST'\
     -v 'https://developer.api.autodesk.com/webhooks/v1/systems/data/hooks'\
     -H 'Content-Type: application/json'\
     -H 'authorization: Bearer bNU4P0trbQKNSzxWksLPTzSbbmUz'\
     -d '{
            "callbackUrl": "http://bf067e05.ngrok.io/callback",
            "scope": {
                 "folder": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ"
            }
      }'

```

Show More

### Response

```
HTTP/1.1 201
Date: Thu, 14 Sep 2017 16:45:05 GMT
Location: https://developer.api.autodesk.com/webhooks/v1/systems/data/hooks
Content-Length: 0
Connection: keep-alive

{
    "hooks": [
        {
            "hookId": "04f1033e-aa58-11e7-abc4-cec278b6b50a",
            "tenant": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ",
            "callbackUrl": "http://bf067e05.ngrok.io/callback",
            "createdBy": "*****",
            "event": "dm.version.added",
            "createdDate": "2017-09-19T18:58:16.636+0000",
            "lastUpdatedDate" : "2020-09-14T17:04:10.444+0000",
            "system": "data",
            "creatorType": "O2User",
            "scope": {
                "folder": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ"
            },
            "status": "active",
            "autoReactivateHook": false,
            "urn": "urn:adsk.webhooks:events.hook:04f1033e-aa58-11e7-abc4-cec278b6b50a",
            "__self__": "/systems/data/events/dm.version.added/hooks/04f1033e-aa58-11e7-abc4-cec278b6b50a"
        },
        {
            "hookId": "04f1092e-aa58-11e7-abc4-cec278b6b50a",
            "tenant": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ",
            "callbackUrl": "http://bf067e05.ngrok.io/callback",
            "createdBy": "*****",
            "event": "dm.version.copied",
            "createdDate": "2017-09-19T18:58:16.312+0000",
            "lastUpdatedDate" : "2020-09-14T17:04:10.444+0000",
            "system": "data",
            "creatorType": "O2User",
            "scope": {
                "folder": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ"
            },
            "status": "active",
            "autoReactivateHook": false,
            "urn": "urn:adsk.webhooks:events.hook:04f1092e-aa58-11e7-abc4-cec278b6b50a",
            "__self__": "/systems/data/events/dm.version.copied/hooks/04f1092e-aa58-11e7-abc4-cec278b6b50a"
        },
        {
            "hookId": "04f10a50-aa58-11e7-abc4-cec278b6b50a",
            "tenant": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ",
            "callbackUrl": "http://bf067e05.ngrok.io/callback",
            "createdBy": "*****",
            "event": "dm.version.deleted",
            "createdDate": "2017-09-19T18:58:16.716+0000",
            "lastUpdatedDate" : "2020-09-14T17:04:10.444+0000",
            "system": "data",
            "creatorType": "O2User",
            "scope": {
                "folder": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ"
            },
            "status": "active",
            "autoReactivateHook": true,
            "urn": "urn:adsk.webhooks:events.hook:04f10a50-aa58-11e7-abc4-cec278b6b50a",
            "__self__": "/systems/data/events/dm.version.deleted/hooks/04f10a50-aa58-11e7-abc4-cec278b6b50a"
        },
        {
            "hookId": "04f10b22-aa58-11e7-abc4-cec278b6b50a",
            "tenant": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ",
            "callbackUrl": "http://bf067e05.ngrok.io/callback",
            "createdBy": "*****",
            "event": "dm.version.modified",
            "createdDate": "2017-09-19T18:58:16.121+0000",
            "lastUpdatedDate" : "2020-09-14T17:04:10.444+0000",
            "system": "data",
            "creatorType": "O2User",
            "scope": {
                "folder": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ"
            },
            "status": "active",
            "autoReactivateHook": false,
            "urn": "urn:adsk.webhooks:events.hook:04f10b22-aa58-11e7-abc4-cec278b6b50a",
            "__self__": "/systems/data/events/dm.version.modified/hooks/04f10b22-aa58-11e7-abc4-cec278b6b50a"
        },
        {
            "hookId": "04f10bea-aa58-11e7-abc4-cec278b6b50a",
            "tenant": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ",
            "callbackUrl": "http://bf067e05.ngrok.io/callback",
            "createdBy": "*****",
            "event": "dm.version.moved",
            "createdDate": "2017-09-19T18:58:16.819+0000",
            "lastUpdatedDate" : "2020-09-14T17:04:10.444+0000",
            "system": "data",
            "creatorType": "O2User",
            "scope": {
                "folder": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ"
            },
            "status": "active",
            "urn": "urn:adsk.webhooks:events.hook:04f10bea-aa58-11e7-abc4-cec278b6b50a",
            "__self__": "/systems/data/events/dm.version.moved/hooks/04f10bea-aa58-11e7-abc4-cec278b6b50a"
        },
        {
            "hookId": "04f10ca8-aa58-11e7-abc4-cec278b6b50a",
            "tenant": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ",
            "callbackUrl": "http://bf067e05.ngrok.io/callback",
            "createdBy": "*****",
            "event": "dm.folder.added",
            "createdDate": "2017-09-19T18:58:16.636+0000",
            "lastUpdatedDate" : "2020-09-14T17:04:10.444+0000",
            "system": "data",
            "creatorType": "O2User",
            "scope": {
                "folder": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ"
            },
            "status": "active",
            "autoReactivateHook": false,
            "urn": "urn:adsk.webhooks:events.hook:04f10ca8-aa58-11e7-abc4-cec278b6b50a",
            "__self__": "/systems/data/events/dm.folder.added/hooks/04f10ca8-aa58-11e7-abc4-cec278b6b50a"
        },
        {
            "hookId": "04f10d70-aa58-11e7-abc4-cec278b6b50a",
            "tenant": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ",
            "callbackUrl": "http://bf067e05.ngrok.io/callback",
            "createdBy": "*****",
            "event": "dm.folder.copied",
            "createdDate": "2017-09-19T18:58:16.215+0000",
            "lastUpdatedDate" : "2020-09-14T17:04:10.444+0000",
            "system": "data",
            "creatorType": "O2User",
            "scope": {
                "folder": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ"
            },
            "status": "active",
            "autoReactivateHook": true,
            "urn": "urn:adsk.webhooks:events.hook:04f10d70-aa58-11e7-abc4-cec278b6b50a",
            "__self__": "/systems/data/events/dm.folder.copied/hooks/04f10d70-aa58-11e7-abc4-cec278b6b50a"
        },
        {
            "hookId": "04f10e2e-aa58-11e7-abc4-cec278b6b50a",
            "tenant": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ",
            "callbackUrl": "http://bf067e05.ngrok.io/callback",
            "createdBy": "*****",
            "event": "dm.folder.deleted",
            "createdDate": "2017-09-19T18:58:16.896+0000",
            "lastUpdatedDate" : "2020-09-14T17:04:10.444+0000",
            "system": "data",
            "creatorType": "O2User",
            "scope": {
                "folder": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ"
            },
            "status": "active",
            "autoReactivateHook": true,
            "urn": "urn:adsk.webhooks:events.hook:04f10e2e-aa58-11e7-abc4-cec278b6b50a",
            "__self__": "/systems/data/events/dm.folder.deleted/hooks/04f10e2e-aa58-11e7-abc4-cec278b6b50a"
        },
        {
            "hookId": "04f10e2e-aa58-11e7-abc4-cec278b6b50a",
            "tenant": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ",
            "callbackUrl": "http://bf067e05.ngrok.io/callback",
            "createdBy": "*****",
            "event": "dm.folder.purged",
            "createdDate": "2017-09-19T18:58:16.896+0000",
            "lastUpdatedDate" : "2020-09-14T17:04:10.444+0000",
            "system": "data",
            "creatorType": "O2User",
            "scope": {
                "folder": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ"
            },
            "status": "active",
            "autoReactivateHook": true,
            "urn": "urn:adsk.webhooks:events.hook:04f10e2e-aa58-11e7-abc4-cec278b6b50a",
            "__self__": "/systems/data/events/dm.folder.purged/hooks/04f10e2e-aa58-11e7-abc4-cec278b6b50a"
        },
        {
            "hookId": "04f112d4-aa58-11e7-abc4-cec278b6b50a",
            "tenant": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ",
            "callbackUrl": "http://bf067e05.ngrok.io/callback",
            "createdBy": "*****",
            "event": "dm.folder.modified",
            "createdDate": "2017-09-19T18:58:16.771+0000",
            "lastUpdatedDate" : "2020-09-14T17:04:10.444+0000",
            "system": "data",
            "creatorType": "O2User",
            "scope": {
                "folder": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ"
            },
            "status": "active",
            "autoReactivateHook": false,
            "urn": "urn:adsk.webhooks:events.hook:04f112d4-aa58-11e7-abc4-cec278b6b50a",
            "__self__": "/systems/data/events/dm.folder.modified/hooks/04f112d4-aa58-11e7-abc4-cec278b6b50a"
        },
        {
            "hookId": "04f113d8-aa58-11e7-abc4-cec278b6b50a",
            "tenant": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ",
            "callbackUrl": "http://bf067e05.ngrok.io/callback",
            "createdBy": "*****",
            "event": "dm.folder.moved",
            "createdDate": "2017-09-19T18:58:16.229+0000",
            "lastUpdatedDate" : "2020-09-14T17:04:10.444+0000",
            "system": "data",
            "creatorType": "O2User",
            "scope": {
                "folder": "urn:adsk.wipprod:fs.folder:co.CHO-BbcmTsigjzymYeRCmQ"
            },
            "status": "active",
            "autoReactivateHook": false,
            "urn": "urn:adsk.webhooks:events.hook:04f113d8-aa58-11e7-abc4-cec278b6b50a",
            "__self__": "/systems/data/events/dm.folder.moved/hooks/04f113d8-aa58-11e7-abc4-cec278b6b50a"
        }
    ]
}

```

Show More
