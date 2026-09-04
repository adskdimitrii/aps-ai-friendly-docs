# contract

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/contract-GET/

---

Information/Metadata

GET

# contract

List all the accessible contracts and high level information for each.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/tokenflex/v1/contract |
| --- | --- |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

## [Request](#request)

### Headers

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |

* Required

## [Response](#response)

### HTTP Status Code Summary

| 200   OK | Request succeeded. |
| --- | --- |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 500   Internal Server Error | An unknown error occurred on the server. |

## [Response](#id1)

### Body Structure (200)

Successful requests will return a JSON array, with each element in the array representing a contract.

| contractName   string | Customer name associated with the contract. |
| --- | --- |
| contractNumber   string | Contract number; uniquely identifies the contract. |
| contractStartDate   string | Start date of the contract. |
| contractEndDate   string | End date of the contract. |
| isActive   boolean | True if the contract is currently active; false otherwise. |

## [Examples](#examples)

Successful listing all contracts (200)

### Request

```
curl  -X GET https://developer.api.autodesk.com/tokenflex/v1/contract \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1N'

```

### Response

```
[
  {
      "contractNumber": "110000917988",
      "contractName": "Autodesk Inc",
      "contractStartDate": "2015-04-28",
      "contractEndDate": "2019-03-10",
      "isActive": true
  }
]

```

Show More
