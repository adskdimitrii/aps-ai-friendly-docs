# tokens/@me

Source: https://aps.autodesk.com/en/docs/webhooks/reference/http/tokens/tokens-me-PUT/

---

PUT

# tokens/@me

Update an existing Webhook secret token. Please note that the update can take up to 10 mins before being applied
depending on the latest event delivery attempt which may still utilize the previous secret token. We recommend your callback accept both
secret token values for a period of time to allow all requests to go through.

## [Resource Information](#resource-information)

| Method and URI | PUT https://developer.api.autodesk.com/webhooks/v1/tokens/@me |
| --- | --- |
| Authentication Context | app only/ user context required |
| Required OAuth Scopes | `data:read` `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [OAuth](../../oauth/http-docs/http-gettoken-POST.md) |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| x-ads-region   string | Specifies the geographical location (region) of the server that the request is executed on. Supported values are the following, but the default value is `US`: <br>`US` : (Default) Updates the token that was previously saved in a data center dedicated to serve the United States.`EMEA` : Updates the token that was previously saved in a data center dedicated to serve the European Union, Middle East, and Africa.`AUS` : (Beta) Updates the token that was previously saved in a data center dedicated to serve Australia.`GBR` : Updates the token that was previously saved in a data center dedicated to serve United Kingdom.`JPN` : Updates the token that was previously saved in a data center dedicated to serve Japan.`DEU` : Updates the token that was previously saved in a data center dedicated to serve Germany.`CAN` : Updates the token that was previously saved in a data center dedicated to serve Canada.`IND` : Updates the token that was previously saved in a data center dedicated to serve India. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| region   string | Specifies the geographical location (region) of the server that the request is executed on. Supported values are the following, but the default value is `US`: <br>`US` : (Default) Updates the token that was previously saved in a data center dedicated to serve the United States.`EMEA` : Updates the token that was previously saved in a data center dedicated to serve the European Union, Middle East, and Africa.`AUS` : (Beta) Updates the token that was previously saved in a data center dedicated to serve Australia.`GBR` : Updates the token that was previously saved in a data center dedicated to serve United Kingdom.`JPN` : Updates the token that was previously saved in a data center dedicated to serve Japan.`DEU` : Updates the token that was previously saved in a data center dedicated to serve Germany.`CAN` : Updates the token that was previously saved in a data center dedicated to serve Canada.`IND` : Updates the token that was previously saved in a data center dedicated to serve India.<br>The `x-ads-region` header also specifies the region. If you specify both, `x-ads-region` has precedence. |
| --- | --- |

## [Body Structure](#body-structure)

| token*   string | The new secret token you want to use |
| --- | --- |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 204   NO_CONTENT | Successful request but server is not returning any content. |
| --- | --- |
| 400   BAD REQUEST | The request is invalid. |
| 401   UNAUTHORIZED | Invalid authorization header. |
| 403   FORBIDDEN | Access denied regardless of authorization status. |
| 404   NOT FOUND | Endpoint or secret token does not exist. |
| 500   INTERNAL SERVICE ERROR | Unexpected service interruption. |

## [Example](#example)

Successful Update of a Secret Token (204):

### Request

```
curl -X 'PUT'\
     -v 'https://developer.api.autodesk.com/webhooks/v1/tokens/@me'\
     -H 'Content-Type: application/json'\
     -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZX'\
     -d '{
           "token":"awffbvdb3trf4fvdfbUyt39suHnbe5Mnrks1"
      }'

```

### Response

```
HTTP/1.1 204
Date: Fri, 15 Sep 2017 19:11:00 GMT
Content-Length: 0
Connection: keep-alive

```
