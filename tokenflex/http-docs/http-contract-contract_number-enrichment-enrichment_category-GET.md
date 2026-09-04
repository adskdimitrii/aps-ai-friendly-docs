# contract/:contract_number/enrichment/:enrichment_category

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/contract-contract_number-enrichment-enrichment_category-GET/

---

Information/Metadata

GET

# contract/:contract_number/enrichment/:enrichment_category

Get all the unique values for an enrichment category.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/tokenflex/v1/contract/:contract_number/enrichment/:enrichment_category |
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
| enrichment_category   string | The enrichment category to retrieve (see [GET contract/:contract_number/enrichment](http-contract-contract_number-enrichment-GET.md)). Note that you can also use customField1 to customField10 as aliases to fetch that respective category. |

## [Response](#response)

### HTTP Status Code Summary

| 200   OK | Request succeeded. |
| --- | --- |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 500   Internal Server Error | An unknown error occurred on the server. |

## [Response](#id2)

### Body Structure (200)

The response body is an array of strings, where each string is a value that has been seen in the specified enrichment category and contract.

## [Examples](#examples)

Successful listing all possible values for an enrichment category (200)

### Request

```
curl  -X GET https://developer.api.autodesk.com/tokenflex/v1/contract/11000000001/enrichment/GEO \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1N'

```

### Response

```
[
  "United States",
  "United Kingdom",
  "Germany",
  "Sweden",
  "Philippines",
  "Canada"
]

```

Show More
