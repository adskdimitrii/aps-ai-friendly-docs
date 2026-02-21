# tokens/@me

Source: https://aps.autodesk.com/en/docs/webhooks/reference/http/tokens/tokens-me-DELETE/

---

DELETE

# tokens/@me

Delete a Webhook secret token. Please note that the secret token can still be available for up to 10 mins
depending on the latest event delivery attempt.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/webhooks/v1/tokens/@me |
| --- | --- |
| Authentication Context | app only/ user context required |
| Required OAuth Scopes | `data:read` `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [OAuth](/en/docs/oauth/v2/reference/http/gettoken-POST) |
| --- | --- |
| Content-Type*   string | `application/json` |
| x-ads-region   string | Specifies the geographical location (region) of the server that the request is executed on. Supported values are the following, but the default value is `US`: <br>`US` : (Default) Deletes the token that was previously saved in a data center dedicated to serve the United States.`EMEA` : Deletes the token that was previously saved in a data center dedicated to serve the European Union, Middle East, and Africa.`AUS` : (Beta) Deletes the token that was previously saved in a data center dedicated to serve Australia.`GBR` : Deletes the token that was previously saved in a data center dedicated to serve United Kingdom.`JPN` : Deletes the token that was previously saved in a data center dedicated to serve Japan.`DEU` : Deletes the token that was previously saved in a data center dedicated to serve Germany.`CAN` : Deletes the token that was previously saved in a data center dedicated to serve Canada.`IND` : Deletes the token that was previously saved in a data center dedicated to serve India. |

* Required

## [URI Parameters](#uri-parameters)

| region   string | Specifies the geographical location (region) of the server that the request is executed on. Supported values are the following, but the default value is `US`: <br>`US` : (Default) Deletes the token that was previously saved in a data center dedicated to serve the United States.`EMEA` : Deletes the token that was previously saved in a data center dedicated to serve the European Union, Middle East, and Africa.`AUS` : (Beta) Deletes the token that was previously saved in a data center dedicated to serve Australia.`GBR` : Deletes the token that was previously saved in a data center dedicated to serve United Kingdom.`JPN` : Deletes the token that was previously saved in a data center dedicated to serve Japan.`DEU` : Deletes the token that was previously saved in a data center dedicated to serve Germany.`CAN` : Deletes the token that was previously saved in a data center dedicated to serve Canada.`IND` : Deletes the token that was previously saved in a data center dedicated to serve India.<br>The `x-ads-region` header also specifies the region. If you specify both, `x-ads-region` has precedence. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 204   NO CONTENT | Successful deletion of secret token. |
| --- | --- |
| 400   BAD REQUEST | The request is invalid. |
| 401   UNAUTHORIZED | Invalid authorization header. |
| 403   FORBIDDEN | Access denied regardless of authorization status. |
| 404   NOT FOUND | Endpoint or secret token does not exist. |
| 500   INTERNAL SERVICE ERROR | Unexpected service interruption. |

## [Example](#example)

Successful Deletion of a Secret Token (204)

### Request

```
curl -X 'DELETE'\
     -v 'https://developer.api.autodesk.com/webhooks/v1/tokens/@me'\
     -H 'Content-Type: application/json'\
     -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZX'

```

### Response

```
HTTP/1.1 204
Date: Fri, 15 Sep 2017 19:11:00 GMT
Content-Length: 0
Connection: keep-alive

```
