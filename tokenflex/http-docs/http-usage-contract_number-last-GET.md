# usage/:contract_number/last

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/usage-contract_number-last-GET/

---

Usage

GET

# usage/:contract_number/last

Get last updated details for the contract.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/tokenflex/v1/usage/:contract_number/last |
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

An array of the following objects with the following attributes. Note some usage categories or charge categories might be missing if there is no usage for that criteria.

| usageCategory   string | The usage category (e.g. DESKTOP_PRODUCT) |
| --- | --- |
| chargeCategory   string | The charge category (e.g. CHARGED, FREE) |
| lastUsageDate   date | The most recent usage date (YYYY-MM-DD) that is present for the usage category and charge category. |
| lastProcessDate   date | The last time any usage data for the usage category and charge category was processed. For Desktop and Cloud Products, this is when the payload or event was received. For Manual Adjustments and Consumptions, this is when the entry was made. |

## [Examples](#examples)

Successful querying last updated dates for a contract (200)

### Request

```
curl  -X GET https://developer.api.autodesk.com/tokenflex/v1/usage/11000000001/last \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1N'

```

### Response

```
[
  {
      "usageCategory": "CLOUD_PRODUCT",
      "chargeCategory": "CASUAL",
      "lastUsageDate": "2018-09-10",
      "lastProcessDate": "2018-09-10"
  },
  {
      "usageCategory": "CLOUD_PRODUCT",
      "chargeCategory": "CHARGED",
      "lastUsageDate": "2018-09-05",
      "lastProcessDate": "2018-09-05"
  },
  {
      "usageCategory": "CLOUD_PRODUCT",
      "chargeCategory": "FREE",
      "lastUsageDate": "2018-09-05",
      "lastProcessDate": "2018-09-05"
  },
  {
      "usageCategory": "CLOUD_SERVICE",
      "chargeCategory": "N/A",
      "lastUsageDate": "2018-06-18",
      "lastProcessDate": "2018-06-18"
  },
  {
      "usageCategory": "DESKTOP_PRODUCT",
      "chargeCategory": "CASUAL",
      "lastUsageDate": "2018-04-28",
      "lastProcessDate": "2018-04-28"
  },
  {
      "usageCategory": "DESKTOP_PRODUCT",
      "chargeCategory": "CHARGED",
      "lastUsageDate": "2018-09-13",
      "lastProcessDate": "2018-06-01"
  },
  {
      "usageCategory": "DESKTOP_PRODUCT",
      "chargeCategory": "FREE",
      "lastUsageDate": "2018-09-13",
      "lastProcessDate": "2018-06-01"
  },
  {
      "usageCategory": "MANUAL_ADJUSTMENT",
      "chargeCategory": "N/A",
      "lastUsageDate": "2018-07-18",
      "lastProcessDate": "2018-07-18"
  },
  {
      "usageCategory": "MANUAL_CONSUMPTION",
      "chargeCategory": "N/A",
      "lastUsageDate": "2018-07-09",
      "lastProcessDate": "2018-07-09"
  }
]

```

Show More
