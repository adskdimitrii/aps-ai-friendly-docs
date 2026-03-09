# systems/:system/events/:event/hooks/:hook_id

Source: https://aps.autodesk.com/en/docs/webhooks/reference/http/webhooks/systems-system-events-event-hooks-hook_id-GET/

---

GET

# systems/:system/events/:event/hooks/:hook_id

Get details of a webhook based on its webhook ID

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/webhooks/v1/systems/:system/events/:event/hooks/:hook_id |
| --- | --- |
| Authentication Context | app only/ user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [OAuth](../../oauth/http-docs/http-gettoken-POST.md) |
| --- | --- |
| Content-Type*   string | `application/json` |
| x-ads-region   string | Specifies the geographical location (region) of the server that the request is executed on. Supported values are the following, but the default value is `US`: <br>`US` : (Default) Retrieves information regarding the specified webhook that was previously registered in a data center dedicated to serve the United States.`EMEA` : Retrieves information regarding the specified webhook that was previously registered in a data center dedicated to serve the European Union, Middle East, and Africa.`AUS` : (Beta) Retrieves information regarding the specified webhook that was previously registered in a data center dedicated to serve Australia.`GBR` : Retrieves information regarding the specified webhook that was previously registered in a data center dedicated to serve United Kingdom.`JPN` : Retrieves information regarding the specified webhook that was previously registered in a data center dedicated to serve Japan.`DEU` : Retrieves information regarding the specified webhook that was previously registered in a data center dedicated to serve Germany.`CAN` : Retrieves information regarding the specified webhook that was previously registered in a data center dedicated to serve Canada.`IND` : Retrieves information regarding the specified webhook that was previously registered in a data center dedicated to serve India. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| system   string | A system for example: `data`   for Data Management |
| --- | --- |
| event   string | Type of event. See [Supported Events](https://aps.autodesk.com/en/docs/webhooks/v1/reference/events/) |
| hook_id   string | Id of the webhook to retrieve |

### Request

## [Query String Parameters](#query-string-parameters)

| region   string | Specifies the geographical location (region) of the server that the request is executed on. Supported values are the following, but the default value is `US`: <br>`US` : (Default) Processes request in a data center dedicated to serve the United States.`EMEA` : Processes request in a data center dedicated to serve the European Union, Middle East, and Africa.`AUS` : (Beta) Processes request in a data center dedicated to serve Australia.<br>The `x-ads-region` header also specifies the region. If you specify both, `x-ads-region` has precedence. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful. |
| --- | --- |
| 400   BAD REQUEST | The request is invalid. |
| 401   UNAUTHORIZED | Invalid authorization header. |
| 403   FORBIDDEN | Access denied regardless of authorization status. |
| 404   NOT FOUND | The specified resource was not found. |
| 500   INTERNAL SERVICE ERROR | Unexpected service interruption |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| hookID   string | Webhook ID |
| --- | --- |
| callbackUrl   string | Callback URL registered for the webhook |
| createdBy   string | Client ID or User ID |
| createdDate   date | Date and time when webhook was created |
| event   string | Type of event |
| hookAttribute   object | Custom metadata which will be less than 1KB in size. |
| scope   object | An object that represents the extent to where the event is monitored. For example, if the scope is folder, the webhooks service generates a notification for the specified event occurring in any sub folder or item within that folder |
| folder   string | Data Management event scope, see [here](../how-to-docs/create-a-hook-data-management.md) for more information |
| workflow   string | Model Derivative event scope, see [here](../how-to-docs/create-a-hook-model-derivative.md) for more information. |
| status   string | `active` if webhook is active; otherwise `inactive` |
| hubId   string | Optional: account ID in the BIM 360 API (if supplied upon hook creation) |
| projectId   string | Optional: project ID in the BIM 360 API (if supplied upon hook creation) |
| hookExpiry   string | Optional: ISO8601 formatted date and time when the hook should expire and automatically be deleted. `null` or not present means the hook never expires. |
| urn   string | URN of the webhook |
| __self__   string | Location of this webhook relative to `/webhooks/v1/` |

## [Example](#example)

Successful Retrieval of a webhook (200):

### Request

```
curl -X 'GET'\
     -v 'https://developer.api.autodesk.com/webhooks/v1/systems/data/events/dm.version.added/hooks/05f10350-991a-11e7-8cd7-91969336b9c2'\
     -H 'Authorization: Bearer 0X6mpTyg5IbH6YI8Okz2XJGpEDeK'

```

### Response

```
HTTP/1.1 200
Date: Thu, 14 Sep 2017 06:57:51 GMT
Location: https://developer.api.autodesk.com/webhooks/v1/systems/data/events/dm.version.added/hooks/0f60f6a0-996c-11e7-abf3-51d68cff984c
Content-Length: 665
Connection: keep-alive
{
  "hookId": "05f10350-991a-11e7-8cd7-91969336b9c2",
  "tenant": "urn:adsk.wipprod:fs.folder:co.VsFvE6y5SNKnhSnogSeqcg",
  "callbackUrl": "http://cf069e23.ngrok.io/callback_test",
  "createdBy": "********",
  "event": "dm.version.added",
  "createdDate": "2017-09-14T06:57:50.597+0000",
  "lastUpdatedDate" : "2020-09-14T17:04:10.444+0000",
  "system": "data",
  "creatorType": "Application",
  "status" : "active",
  "autoReactivateHook": false,
  "hookExpiry": "2017-09-21T17:04:10.444Z",
  "scope": {
      "folder": "urn:adsk.wipprod:fs.folder:co.VsFvE6y5SNKnhSnogSeqcg"
  },
  "urn": "urn:adsk.webhooks:events.hook:05f10350-991a-11e7-8cd7-91969336b9c2",
  "__self__": "/systems/data/events/dm.version.added/hooks/05f10350-991a-11e7-8cd7-91969336b9c2"
}

```

Show More
