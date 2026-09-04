# contract/:contract_number/enrichment

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/contract-contract_number-enrichment-GET/

---

Information/Metadata

GET

# contract/:contract_number/enrichment

List all customer uploaded enrichment categories.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/tokenflex/v1/contract/:contract_number/enrichment |
| --- | --- |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

## [Request](#request)

### Headers

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |

* Required

## [Request](#id1)

### URI Parameters

| contract_number   string | The contract number to retrieve (see [GET contract](http-contract-GET.md)). |
| --- | --- |

## [Response](#response)

### HTTP Status Code Summary

| 200   OK | Request succeeded. |
| --- | --- |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 500   Internal Server Error | An unknown error occurred on the server. |

## [Response](#id2)

### Body Structure (200)

The response body is an array of strings, where each string is the name of a custom enrichment category available to this contract. Note that elements can be empty or repeat.

## [Examples](#examples)

Successful listing all enrichment categories of a contract (200)

### Request

```
curl  -X GET https://developer.api.autodesk.com/tokenflex/v1/contract/11000000001/enrichment \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1N'

```

### Response

```
[
  "GEO",
  "Department",
  "Team",
  "Team2",
  "Team3",
  "",
  "地理",
  "",
  "",
  ""
]

```

Show More
