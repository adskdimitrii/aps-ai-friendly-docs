# usage/:contract_number/summary/

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/usage-contract_number-summary-GET/

---

Usage

GET

# usage/:contract_number/summary/

Get usage summary at a monthly aggregate level with the option of some filters. This method is recommended over an ad-hoc query because this API returns data faster.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/tokenflex/v1/usage/:contract_number/summary |
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

| contract_number   string | Contract for which you are querying |
| --- | --- |

## [Request](#id2)

### Query String Parameters

See [Fields and Metrics](https://aps.autodesk.com/en/docs/tokenflex/v1/reference/fields-and-metrics/) for additional descriptions.

| minUsageMonth   datetime: ISO 8601 | The minimum usage date to include. |
| --- | --- |
| maxUsageMonth   datetime: ISO 8601 | The maximum usage date to include. |
| contractYear   int | Limit the results to a particular contract year. |
| usageCategory   string | Limit the results to a particular usage category. |

## [Response](#response)

### HTTP Status Code Summary

| 200   OK | Request succeeded. |
| --- | --- |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 500   Internal Server Error | An unknown error occurred on the server. |

## [Response](#id3)

### Body Structure (200)

An array of objects with the following attributes. See [Fields and Metrics](https://aps.autodesk.com/en/docs/tokenflex/v1/reference/fields-and-metrics/) for attribute descriptions.

| usageMonth   string | The year and month for which usage is being reported. |
| --- | --- |
| contractYear   string | The contract year (not calendar year) for which usage is being reported. |
| usageCategory   string | The type of usage (PRODUCT_CONSUMPTION, CLOUD_CONSUMPTION, MANUAL_ADJUSTMENT, CLOUD_PRODUCT_CONSUMPTION, MANUAL_CONSUMPTION). |
| uniqueUsers   integer | The number of unique users who consumed tokens during this month. |
| tokensConsumed   integer | The total number of tokens consumed. |

## [Examples](#examples)

Successful querying summary usage details for a contract (200)

### Request

```
curl  -X GET https://developer.api.autodesk.com/tokenflex/v1/usage/11000000001/summary \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1N'

```

### Response

```
[
  {
      "usageMonth": "2015-01-01",
      "contractYear": 1,
      "usageCategory": "CLOUD_CONSUMPTION",
      "uniqueUsers": 2,
      "tokensConsumed": 5
  },
  {
      "usageMonth": "2015-02-01",
      "contractYear": 1,
      "usageCategory": "MANUAL_ADJUSTMENT",
      "uniqueUsers": 1,
      "tokensConsumed": 15883
  },
  {
      "usageMonth": "2015-03-01",
      "contractYear": 1,
      "usageCategory": "CLOUD_CONSUMPTION",
      "uniqueUsers": 5,
      "tokensConsumed": 414
  },
  {
      "usageMonth": "2015-04-01",
      "contractYear": 1,
      "usageCategory": "PRODUCT_CONSUMPTION",
      "uniqueUsers": 11499,
      "tokensConsumed": 1155686
  }
]

```

Show More
