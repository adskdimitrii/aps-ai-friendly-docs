# /export/:contract_number/requests/markRead

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/export-contract_number-requests.markRead-POST/

---

Export

POST

# /export/:contract_number/requests/markRead

Mark export requests as read. Marking a request as read also affects the export UI in Autodesk Account.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/tokenflex/v1/export/:contract_number/requests/markRead |
| --- | --- |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

## [Request](#request)

### Headers

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

## [Request](#id1)

### URI Parameters

| contract_number   string | The contract number to retrieve (see [GET contract](http-contract-GET.md)). |
| --- | --- |

## [Request](#id2)

### Body Structure

The POST body is a JSON array of requestKey strings.

## [Response](#response)

### HTTP Status Code Summary

| 200   OK | Request succeeded. |
| --- | --- |
| 400   Bad Request | The requested body was empty or otherwise invalid |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 500   Internal Server Error | An unknown error occurred on the server. |

## [Response](#id3)

### Body Structure (200)

A string array of requestKeys for which the flag was successfully updated. Note that if the flag was already “Y”, it is not considered a success and will not be included in the response.

## [Example](#example)

Successful readFlag update for all requested requestKeys (200)

### Request

```
curl  -X POST \
      https://developer.api.autodesk.com/tokenflex/v1/export/110000917988/requests/markRead \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1N' \
      -d '["2018-10-16T21:22:43#8ab025dc-aa44-4695-b9dd-a0c1694d4917", "2018-10-16T22:19:49#94307b1f-363d-46ce-984c-ce97307d1b26", "2018-10-16T22:45:35#bd765291-abde-4972-bb0d-77ba9d245cbd"]'

```

### Response

```
[
    "2018-10-16T21:22:43#8ab025dc-aa44-4695-b9dd-a0c1694d4917",
    "2018-10-16T22:19:49#94307b1f-363d-46ce-984c-ce97307d1b26",
    "2018-10-16T22:45:35#bd765291-abde-4972-bb0d-77ba9d245cbd"
]

```
