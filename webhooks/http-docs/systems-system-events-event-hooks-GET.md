# systems/:system/events/:event/hooks

Source: https://aps.autodesk.com/en/docs/webhooks/reference/http/webhooks/systems-system-events-event-hooks-GET/

---

GET

# systems/:system/events/:event/hooks

Retrieves a paginated list of all the webhooks for a specified event. If the pageState query string is not specified, the first page is returned.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/webhooks/v1/systems/:system/events/:event/hooks |
| --- | --- |
| Authentication Context | app only/ user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [OAuth](/en/docs/oauth/v2/reference/http/gettoken-POST) |
| --- | --- |
| x-ads-region   string | Specifies the geographical location (region) of the server that the request is executed on. Supported values are the following, but the default value is `US`: <br>`US` : (Default) Retrieves the webhooks that were registered in a data center dedicated to serve the United States.`EMEA` : Retrieves the webhooks that were registered in a data center dedicated to serve the European Union, Middle East, and Africa.`AUS` : (Beta) Retrieves the webhooks that were registered in a data center dedicated to serve Australia.`GBR` : Retrieves the webhooks that were registered in a data center dedicated to serve United Kingdom.`JPN` : Retrieves the webhooks that were registered in a data center dedicated to serve Japan.`DEU` : Retrieves the webhooks that were registered in a data center dedicated to serve Germany.`CAN` : Retrieves the webhooks that were registered in a data center dedicated to serve Canada.`IND` : Retrieves the webhooks that were registered in a data center dedicated to serve India. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| system   string | System for example: `data` |
| --- | --- |
| event   string | Type of event. See [Supported Events](/en/docs/webhooks/v1/reference/events) |

### Request

## [Query String Parameters](#query-string-parameters)

| region   string | Specifies the geographical location (region) of the server that the request is executed on. Supported values are the following, but the default value is `US`: <br>`US` : (Default) Processes request in a data center dedicated to serve the United States.`EMEA` : Processes request in a data center dedicated to serve the European Union, Middle East, and Africa.`AUS` : (Beta) Processes request in a data center dedicated to serve Australia.<br>The `x-ads-region` header also specifies the region. If you specify both, `x-ads-region` has precedence. |
| --- | --- |

### Request

## [Query String Parameters](#id4)

| scopeName   String | Scope name used to create hook. For example : folder |
| --- | --- |
| scopeValue   String | Scope value used to create hook. If scopeValue is present then scopeName must be present, otherwise scopeValue would be ignored. |
| pageState   String | Base64 encoded string used to return the next page of the list of webhooks. This can be obtained from the `next` field of the previous page. PagingState instances are not portable and implementation is subject to change across versions. Default page size is 200. |
| status   String | Status of the hooks. Options: â*active*â, â*inactive*â |
| region   string | Specifies the geographical location (region) of the server that the request is executed on. Supported values are the following, but the default value is `US`: <br>`US` : (Default) Retrieves the webhooks that were registered in a data center dedicated to serve the United States.`EMEA` : Retrieves the webhooks that were registered in a data center dedicated to serve the European Union, Middle East, and Africa.`AUS` : (Beta) Retrieves the webhooks that were registered in a data center dedicated to serve Australia.`GBR` : Retrieves the webhooks that were registered in a data center dedicated to serve United Kingdom.`JPN` : Retrieves the webhooks that were registered in a data center dedicated to serve Japan.`DEU` : Retrieves the webhooks that were registered in a data center dedicated to serve Germany.`CAN` : Retrieves the webhooks that were registered in a data center dedicated to serve Canada.`IND` : Retrieves the webhooks that were registered in a data center dedicated to serve India.<br>The `x-ads-region` header also specifies the region. If you specify both, `x-ads-region` has precedence. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Success. |
| --- | --- |
| 204   EMPTY | No webhooks exist. |
| 400   BAD REQUEST | The request is invalid. |
| 401   UNAUTHORIZED | Invalid authorization header. |
| 403   FORBIDDEN | Access denied regardless of authorization status. |
| 404   NOT FOUND | The specified resource was not found. |
| 500   INTERNAL SERVICE ERROR | Unexpected service interruption |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| links   object | An object containing links to other pages of the paginated list of webhooks |
| --- | --- |
| next   string | A Base64 encoded string that returns the next page of the list of webhooks |
| data   array: object | An array of webhook objects |
| data[i]   object | An element of the array; a webhook object |
| hookId   string | Webhook ID |
| callbackUrl   string | Callback URL registered for the webhook |
| createdBy   string | Client ID or User ID |
| createdDate   date | Date and time when webhook was created |
| lastUpdatedDate   date | Date and time when webhook was last updated |
| event   string | Type of event that is being monitored |
| scope   object | An object that represents the extent to where the event is monitored. For example, if the scope is a folder, the webhooks service generates a notification for the specified event occurring in any sub folder or item within that folder. Please refer to the individual event specification pages for valid scopes. For example, [Data Management events](/en/docs/webhooks/v1/reference/events/data_management_events). |
| status   string | `active` if webhook is active; otherwise `inactive` |
| urn   string | URN of the webhook |
| autoReactivateHook   boolean | Flag to indicate if the hook can be automatically reactivated. |
| hubId   string | Optional: account ID in the BIM 360 API (if supplied upon hook creation) |
| projectId   string | Optional: project ID in the BIM 360 API (if supplied upon hook creation) |
| hookExpiry   string | Optional: ISO8601 formatted date and time when the hook should expire and automatically be deleted. `null` or not present means the hook never expires. |
| __self__   string | Location of this webhook relative to `/webhooks/v1/` |

## [Example](#example)

Successful Retrieval of webhooks (200):

### Request

```
curl -v 'https://developer.api.autodesk.com/webhooks/v1/systems/data/events/dm.version.added/hooks?scopeName=folder&scopeValue=urn:adsk.wipprod:fs.folder:co.wT5lCWlXSKeo3razOfHJAw&pageState=BNNBEACAtgALYWRzay53aXBkZXYNZnMuZmlsZS5hZGRlZAZmb2xkZXIydXJuOmFkc2sud2lwcWE6ZnMuZm9sZGVyOmNvLlRSM253QUtoVFNDQ0x0azY0VE52Q2cydXJuOmFkc2sud2lwcWE6ZnMuZm9sZGVyOmNvLlRSM253QUtoVFNDQ0x0azY0VE52Q2ctaHR0cDovL2FwaS53ZWJob29raW5ib3guY29tL2kvM0l6eGlLZndmL2luL3gy8H____3wf____Twpc5_2RqlBtCsLMPJlT9kABA=='\
     -H 'Authorization: Bearer bNU4P0trbQKNSzxWksLPTzSbbmUz'

```

### Response

```
HTTP/1.1 200
Content-Type: application/json
Date: Fri, 14 Sep 2017 17:14:09 GMT
Content-Length: 662
Connection: keep-alive
{
  "links": {
    "next": "/systems/data/events/dm.version.added/hooks?pageState=AMMAEACAtgALYWRzay53aXBkZXYNZnMuZmlsZS5hZGRlZAZmb2xkZXIydXJuOmFkc2sud2lwcWE6ZnMuZm9sZGVyOmNvLlRSM253QUtoVFNDQ0x0azY0VE52Q2cydXJuOmFkc2sud2lwcWE6ZnMuZm9sZGVyOmNvLlRSM253QUtoVFNDQ0x0azY0VE52Q2ctaHR0cDovL2FwaS53ZWJob29raW5ib3guY29tL2kvM0l6eGlLZndmL2luL3gy8H____3wf____Twpc5_2RqlBtCsLMPJlT9kABA=="
  },
  "data": [{
    "hookId" : "0f60f6a0-996c-11e7-abf3-51d68cff984c",
    "tenant" : "urn:adsk.wipprod:fs.folder:co.wT5lCWlXSKeo3razOfHJAw",
    "callbackUrl" : "http://bf067e05.ngrok.io/callback",
    "createdBy" : "*********",
    "event" : "dm.version.added",
    "createdDate" : "2017-09-14T17:04:10.444+0000",
    "lastUpdatedDate" : "2020-09-14T17:04:10.444+0000",
    "system" : "data",
    "creatorType": "Application",
    "status" : "active",
    "autoReactivateHook": false,
    "scope" : {
      "folder" : "urn:adsk.wipprod:fs.folder:co.wT5lCWlXSKeo3razOfHJAw"
    },
    "urn" : "urn:adsk.webhooks:events.hook:0f60f6a0-996c-11e7-abf3-51d68cff984c",
    "__self__" : "/systems/data/events/dm.version.added/hooks/0f60f6a0-996c-11e7-abf3-51d68cff984c"
  }]
}

```

Show More
