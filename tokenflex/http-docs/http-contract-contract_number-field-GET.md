# contract/:contract_number/:field

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/contract-contract_number-field-GET/

---

Information/Metadata

GET

# contract/:contract_number/:field

List the unique values for a specified Field. Values are listed only if the Field has associated usage.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/tokenflex/v1/contract/:contract_number/:field |
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
| field   string | The Field to retrieve. Must be one of [‘productName’, ‘userName’, ‘machineName’, ‘licenseServerName’] (see [Fields and Metrics](https://aps.autodesk.com/en/docs/tokenflex/v1/reference/fields-and-metrics/)). |

### Query String Parameters

| usageCategory   string | Limit the results to a particular usage category. |
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

The response body is an array of strings, where each string is a value that has been seen in the specified Field and contract.

## [Examples](#examples)

Successful listing all the productName with usage for a contract (200)

### Request

```
curl  -X GET https://developer.api.autodesk.com/tokenflex/v1/contract/11000000001/productName \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1N'

```

### Response

```
[
  "Bridge Design for InfraWorks 360",
  "Autodesk BIM 360 Team - Single User",
  "Autodesk Collaboration for Revit - Single User",
  "Drainage Design for InfraWorks 360",
  "FormIt Pro",
  "Fusion Team - Single User",
  "InfraWorks"
]

```

Show More
