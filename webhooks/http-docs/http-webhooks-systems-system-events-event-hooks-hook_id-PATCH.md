# systems/:system/events/:event/hooks/:hook_id

Source: https://aps.autodesk.com/en/docs/webhooks/reference/http/webhooks/systems-system-events-event-hooks-hook_id-PATCH/

---

PATCH

# systems/:system/events/:event/hooks/:hook_id

Partially update a webhook based on its webhook ID. The only fields that may be updated are: status, filter, hookAttribute, and hookExpiry.

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/webhooks/v1/systems/:system/events/:event/hooks/:hook_id |
| --- | --- |
| Authentication Context | app only/ user context required |
| Required OAuth Scopes | `data:read` `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [OAuth](/en/docs/oauth/v2/reference/http/gettoken-POST) |
| --- | --- |
| Content-Type*   string | `application/json` |
| x-ads-region   string | Specifies the geographical location (region) of the server that the request is executed on. Supported values are the following, but the default value is `US`: <br>`US` : (Default) Updates information for the webhook that was previously registered in a data center dedicated to serve the United States.`EMEA` : Updates information for the webhook that was previously registered in a data center dedicated to serve the European Union, Middle East, and Africa.`AUS` : (Beta) Updates information for the webhook that was previously registered in a data center dedicated to serve Australia.`GBR` : Updates information for the webhook that was previously registered in a data center dedicated to serve United Kingdom.`JPN` : Updates information for the webhook that was previously registered in a data center dedicated to serve Japan.`DEU` : Updates information for the webhook that was previously registered in a data center dedicated to serve Germany.`CAN` : Updates information for the webhook that was previously registered in a data center dedicated to serve Canada.`IND` : Updates information for the webhook that was previously registered in a data center dedicated to serve India. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| system   string | A system for example: `data`   for Data Management |
| --- | --- |
| event   string | Type of event. See [Supported Events](/en/docs/webhooks/v1/reference/events) |
| hook_id   string | Id of the webhook to modify |

### Request

## [Body Structure](#body-structure)

| status   string | `active` if webhook is active; otherwise `inactive` |
| --- | --- |
| filter   string | JsonPath expression that can be used by you to filter the callbacks you receive. |
| hookAttribute   object | A user-defined JSON object, which you can use to store/set some custom information. The maximum size of the JSON object (content) should be less than 1KB |
| token   string | A secret token that is used to generate a hash signature, which is passed along with notification requests to the callback URL |
| autoReactivateHook   boolean | Flag to enable the hook for the automatic reactivation flow. Please see [webhook field guide](/en/docs/webhooks/v1/developers_guide/field-guide/#webhook) for more details. |
| hookExpiry   string | ISO8601 formatted date and time when the hook should expire and automatically be deleted. Providing `null` or an empty string updates the hook so that it never expires. |

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

## [Example 1](#example-1)

Successful Patch of a webhook:

### Request

```
curl -X 'PATCH'
     -v 'https://developer.api.autodesk.com/webhooks/v1/systems/data/events/dm.version.added/hooks/05f10350-991a-11e7-8cd7-91969336b9c2'
     -H 'Content-Type: application/json'
     -H 'Authorization: Bearer 0X6mpTyg5IbH6YI8Okz2XJGpEDeK'
     -d '{
            "status": "active",
            "autoReactivateHook": false,
            "filter": "$[?(@.ext=='txt')]",
            "hookAttribute": {
                 /* Custom metadata */
                 "myfoo": 34,
                 "projectId": "someURN",
                 "myobject": {
                      "nested": true
                 }
            }
      }'

```

Show More

### Response

```
HTTP/1.1 204
Date: Fri, 15 Sep 2017 19:11:00 GMT
Content-Length: 0
Connection: keep-alive

```

## [Example 2](#example-2)

Successful deactivation of a webhook:

### Request

```
curl -X 'PATCH'
     -v 'https://developer.api.autodesk.com/webhooks/v1/systems/data/events/dm.version.added/hooks/05f10350-991a-11e7-8cd7-91969336b9c2'
     -H 'Content-Type: application/json'
     -H 'Authorization: Bearer 0X6mpTyg5IbH6YI8Okz2XJGpEDeK'
     -d '{
            "status": "inactive"
      }'

```

### Response

```
HTTP/1.1 204
Date: Fri, 15 Sep 2017 19:11:00 GMT
Content-Length: 0
Connection: keep-alive

```

## [Example 3](#example-3)

Successful removal of existing filter and hook attributes:

### Request

```
curl -X 'PATCH'
     -v 'https://developer.api.autodesk.com/webhooks/v1/systems/data/events/dm.version.added/hooks/05f10350-991a-11e7-8cd7-91969336b9c2'
     -H 'Content-Type: application/json'
     -H 'Authorization: Bearer 0X6mpTyg5IbH6YI8Okz2XJGpEDeK'
     -d '{
            "filter": null,
            "hookAttribute": null
      }'

```

Show More

### Response

```
HTTP/1.1 204
Date: Fri, 15 Sep 2017 19:11:00 GMT
Content-Length: 0
Connection: keep-alive

```

## [Example 4](#example-4)

Successful update of hook expiry to a later date and time:

### Request

```
curl -X 'PATCH'
     -v 'https://developer.api.autodesk.com/webhooks/v1/systems/data/events/dm.version.added/hooks/05f10350-991a-11e7-8cd7-91969336b9c2'
     -H 'Content-Type: application/json'
     -H 'Authorization: Bearer 0X6mpTyg5IbH6YI8Okz2XJGpEDeK'
     -d '{
            "hookExpiry": ""2017-09-22T17:04:10.444Z""
      }'

```

### Response

```
HTTP/1.1 204
Date: Fri, 15 Sep 2017 19:11:00 GMT
Content-Length: 0
Connection: keep-alive

```
