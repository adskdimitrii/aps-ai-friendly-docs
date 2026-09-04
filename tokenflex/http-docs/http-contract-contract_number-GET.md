# contract/:contract_number

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/contract-contract_number-GET/

---

Information/Metadata

GET

# contract/:contract_number

Query details of a contract.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/tokenflex/v1/contract/:contract_number |
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

| contractName   string | Customer name associated with the contract. |
| --- | --- |
| contractNumber   string | Contract number; uniquely identifies the contract. |
| contractStartDate   string | Date at which the contract was first valid. |
| contractEndDate   string | Last date at which the contract will be valid. |
| isActive   boolean | True if the contract is valid; false otherwise. |
| multiyearProvisionedTokens   integer | Total number of multiyear tokens assigned to this contract. |
| contractYears   array | An array of contractYear objects containing details for each year of the contract. |
| contractYears.contractYears[i]   object | A conractYear object |
| contractYears.contractYears[i].consumedTokens   integer | The number of tokens consumed during this contract year (excluding any multiyear tokens that may have been consumed). **Note this is a snapshot value and may not match totals from usage endpoints.** |
| contractYears.contractYears[i].multiyearConsumedTokens   integer | The number of multiyear tokens consumed during this contract year. **Note this is a snapshot value and may not match totals from usage endpoints.** |
| contractYears.contractYears[i].multiyearTokensAtStart   integer | The number of multiyear tokens available at the start of this contract year. |
| contractYears.contractYears[i].provisionedTokens   integer | The number of tokens assigned to this contract year. |
| contractYears.contractYears[i].remainingTokens   integer | The number of tokens remaining for this contract year. **Note this is a snapshot value and may not match totals from usage endpoints.** |
| contractYears.contractYears[i].startDate   string | Start date for this contract year. |
| contractYears.contractYears[i].endDate   string | End date for this contract year. |
| contractYears.contractYears[i].year   integer | The year of the contract that this entry represents. |

## [Examples](#examples)

Successful querying details for a contract (200)

### Request

```
curl  -X GET https://developer.api.autodesk.com/tokenflex/v1/contract/11000000001 \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1N'

```

### Response

```
{
  "contractNumber": "11000000001",
  "contractName": "Autodesk Inc",
  "contractStartDate": "2015-04-28",
  "contractEndDate": "2019-03-10",
  "isActive": true,
  "multiyearProvisionedTokens": 25000,
  "contractYears": [
      {
          "year": 1,
          "startDate": "2015-04-28",
          "endDate": "2016-04-27",
          "provisionedTokens": 344000,
          "consumedTokens": 146226,
          "remainingTokens": 197774,
          "multiyearTokensAtStart": 25000,
          "multiyearConsumedTokens": 3217
      },
      {
          "year": 2,
          "startDate": "2016-04-28",
          "endDate": "2017-04-27",
          "provisionedTokens": 344000,
          "consumedTokens": 149799,
          "remainingTokens": 194201,
          "multiyearTokensAtStart": 21783,
          "multiyearConsumedTokens": 0
      },
      {
          "year": 3,
          "startDate": "2017-04-28",
          "endDate": "2018-04-27",
          "provisionedTokens": 344000,
          "consumedTokens": 142073,
          "remainingTokens": 201927,
          "multiyearTokensAtStart": 21783,
          "multiyearConsumedTokens": 0
      },
      {
          "year": 4,
          "startDate": "2018-04-28",
          "endDate": "2019-03-10",
          "provisionedTokens": 0,
          "consumedTokens": 0,
          "remainingTokens": 0,
          "multiyearTokensAtStart": 21783,
          "multiyearConsumedTokens": 0
      }
  ]
}

```

Show More
