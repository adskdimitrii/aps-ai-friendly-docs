# tokens

Source: https://aps.autodesk.com/en/docs/webhooks/reference/http/tokens/tokens-POST/

---

POST

# tokens

Add a new Webhook secret token

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/webhooks/v1/tokens |
| --- | --- |
| Authentication Context | app only/ user context required |
| Required OAuth Scopes | `data:read` `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [OAuth](../../oauth/http-docs/http-gettoken-POST.md) |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| x-ads-region   string | Specifies the geographical location (region) of the server that the request is executed on. Supported values are the following, but the default value is `US`: <br>`US` : (Default) Save the token in a data center dedicated to serve the United States.`EMEA` : Save the token in a data center dedicated to serve the European Union, Middle East, and Africa.`AUS` : (Beta) Save the token in a data center dedicated to serve Australia.`GBR` : Save the token in a data center dedicated to serve United Kingdom.`JPN` : Save the token in a data center dedicated to serve Japan.`DEU` : Save the token in a data center dedicated to serve Germany.`CAN` : Save the token in a data center dedicated to serve Canada.`IND` : Save the token in a data center dedicated to serve India. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| region   string | Specifies the geographical location (region) of the server that the request is executed on. Supported values are the following, but the default value is `US`: <br>`US` : (Default) Save the token in a data center dedicated to serve the United States.`EMEA` : Save the token in a data center dedicated to serve the European Union, Middle East, and Africa.`AUS` : (Beta) Save the token in a data center dedicated to serve Australia.`GBR` : Save the token in a data center dedicated to serve United Kingdom.`JPN` : Save the token in a data center dedicated to serve Japan.`DEU` : Save the token in a data center dedicated to serve Germany.`CAN` : Save the token in a data center dedicated to serve Canada.`IND` : Save the token in a data center dedicated to serve India.<br>The `x-ads-region` header also specifies the region. If you specify both, `x-ads-region` has precedence. |
| --- | --- |

## [Body Structure](#body-structure)

| token*   string | A secret token that is used to generate a hash signature, which is passed along with notification requests to the callback URL |
| --- | --- |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful. |
| --- | --- |
| 400   BAD REQUEST | The request is invalid. Secret token already exists. |
| 401   UNAUTHORIZED | Invalid authorization header. |
| 403   FORBIDDEN | Access denied regardless of authorization status. |
| 404   NOT FOUND | Endpoint does not exist. |
| 500   INTERNAL SERVICE ERROR | Unexpected service interruption. |

### Response

## [Body Structure (200)](#body-structure-200)

| status   integer | A repititon of the response http status code |
| --- | --- |
| detail   array:string | An array of strings that provide a human readable description of the response |

## [Example](#example)

Successful Creation of a Secret Token (200):

### Request

```
curl -X 'POST'\
     -v 'https://developer.api.autodesk.com/webhooks/v1/tokens'\
     -H 'Content-Type: application/json'\
     -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZX'\
     -d '{
         "token":"awffbvdb3trf4fvdfbUyt39suHnbe5Mnrks3"
         }'

```

### Response

```
HTTP/1.1 200
Date: Fri, 15 Sep 2017 19:11:00 GMT
Content-Length: 0
Connection: keep-alive

{
  "status": 200,
  "detail": [
      "Token created successfully for client: *****"
  ]
}

```

Show More
