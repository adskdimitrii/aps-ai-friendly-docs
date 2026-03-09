# systems/:system/events/:event/hooks/:hook_id

Source: https://aps.autodesk.com/en/docs/webhooks/reference/http/webhooks/systems-system-events-event-hooks-hook_id-DELETE/

---

DELETE

# systems/:system/events/:event/hooks/:hook_id

Deletes a webhook based on webhook ID

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/webhooks/v1/systems/:system/events/:event/hooks/:hook_id |
| --- | --- |
| Authentication Context | app only/ user context required |
| Required OAuth Scopes | `data:read` `data:write` |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [OAuth](../../oauth/http-docs/http-gettoken-POST.md) |
| --- | --- |
| Content-Type*   string | `application/json` |
| x-ads-region   string | Specifies the geographical location (region) of the server that the request is executed on. Supported values are the following, but the default value is `US`: <br>`US` : (Default) Removes the webhook that was previously registered in a data center dedicated to serve the United States.`EMEA` : Removes the webhook that was previously registered in a data center dedicated to serve the European Union, Middle East, and Africa.`AUS` : (Beta) Removes the webhook that was previously registered in a data center dedicated to serve Australia.`GBR` : Removes the webhook that was previously registered in a data center dedicated to serve United Kingdom.`JPN` : Removes the webhook that was previously registered in a data center dedicated to serve Japan.`DEU` : Removes the webhook that was previously registered in a data center dedicated to serve Germany.`CAN` : Removes the webhook that was previously registered in a data center dedicated to serve Canada.`IND` : Removes the webhook that was previously registered in a data center dedicated to serve India. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| system   string | A system for example: `data`   for Data Management |
| --- | --- |
| event   string | Type of event. See [Supported Events](https://aps.autodesk.com/en/docs/webhooks/v1/reference/events/) |
| hook_id   string | Webhook ID to delete |

### Request

## [Query String Parameters](#query-string-parameters)

| region   string | Specifies the geographical location (region) of the server that the request is executed on. Supported values are the following, but the default value is `US`: <br>`US` : (Default) Processes request in a data center dedicated to serve the United States.`EMEA` : Processes request in a data center dedicated to serve the European Union, Middle East, and Africa.`AUS` : (Beta) Processes request in a data center dedicated to serve Australia.<br>The `x-ads-region` header also specifies the region. If you specify both, `x-ads-region` has precedence. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 204   OK | Delete operation is successful. |
| --- | --- |
| 400   BAD REQUEST | The request is invalid. |
| 401   UNAUTHORIZED | Invalid authorization header. |
| 403   FORBIDDEN | Access denied regardless of authorization status. |
| 404   NOT FOUND | The specified resource was not found. |
| 500   INTERNAL SERVICE ERROR | Unexpected service interruption |

## [Examples](#examples)

Successful Deletion of a webhook (204):

### Request

```
curl -X DELETE\
     -v 'https://developer.api.autodesk.com/webhooks/v1/systems/data/events/dm.version.added/hooks/0f60f6a0-996c-11e7-abf3-51d68cff984c'\
     -H 'Authorization: Bearer bNU4P0trbQKNSzxWksLPTzSbbmUz'

```

### Response

```
HTTP/1.1 204
Date: Fri, 15 Sep 2017 16:26:40 GMT
Content-Length: 0
Connection: keep-alive

```
