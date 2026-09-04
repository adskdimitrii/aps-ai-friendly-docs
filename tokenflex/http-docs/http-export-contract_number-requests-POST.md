# /export/:contract_number/requests

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/export-contract_number-requests-POST/

---

Export

POST

# /export/:contract_number/requests

Create a new export request. This call allows you to perform a custom query to later retrieve the results as a CSV file.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/tokenflex/v1/export/:contract_number/requests |
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

The body of the request is functionally similar to the one for the [Query API](http-usage-contract_number-query-POST.md).
The body is a JSON document describing the fields and metrics to use in the query, as well as an optional `where` clause providing criteria used to limit the
scope of the query. Queries must include either metrics or fields, or both metrics and fields. See [Fields and Metrics](https://aps.autodesk.com/en/docs/tokenflex/v1/reference/fields-and-metrics/) for all available Fields and Metrics. The basic structure of the JSON document is as follows:

| fields   List of fields to use in the query. | `[ "userName", "productName" ]` |
| --- | --- |
| metrics   List of metrics to use in the query. | `[ "uniqueUsers", "tokensConsumed" ]` |
| usageCategory   Optional; list of categories to filter by. | `[ "MANUAL_ADJUSTMENT", "MANUAL_CONSUMPTION" ]` |
| where   Optional; criteria used to limit the query. | `contractYear >= 2 and userName LIKE 'admin%'` |
| downloadFileName   Optional; output filename (no extension). | `myExportFile` |

### Usage limitations

All limitations from the [Query API](http-usage-contract_number-query-POST.md) still apply except for the cap on 5 minute execution time.
However, you are allowed to export desktop and cloud product usage data at a session level. Note you cannot mix usage from different usage categories when exporting at a session level.

You can queue up at most 50 export requests at a time (i.e. requests in the Requested status).

#### Usage limitations specific to desktop session level export

Please note the following limitations when **exporting specifically at a desktop session level**. An export is a desktop session level export if it includes any session level fields and the usageCategory attribute is DESKTOP_PRODUCT.
These restrictions may be lifted in the future. **These restrictions do not affect other usage categories or desktop exports not at a session level.**

- You must include usageCategory separately in the request’s usageCategory attribute and it must be DESKTOP_PRODUCT.

#### Example desktop session level export with all available fields

The below request yields results for all your desktop usage at a session level in the month of January 2018. Note the inclusion of specific fields such as chargedItemID which makes this a session level export. This is the full set of fields and metrics available for export at a destkop session level. Including any other fields or metrics while attempting a session level desktop export will cause the request to be rejected.

```
{
    "fields": [
        "usageMonth",
        "usageDate",
        "contractYear",
        "productName",
        "productLineCode",
        "productVersion",
        "productFeatureCode",
        "userName",
        "machineName",
        "sessionStartDate",
        "sessionEndDate",
        "licenseServerTimeZoneOffset",
        "chargedItemID",
        "chargeCategory",
        "licenseServerName",
        "usageType",
        "usageCategory",
        "customField1",
        "customField2",
        "customField3",
        "customField4",
        "customField5",
        "customField6",
        "customField7",
        "customField8",
        "customField9",
        "customField10"
    ],
    "metrics": [
        "tokensConsumed",
        "usageMinutes",
        "usageHours"
    ],
    "usageCategory": [
      "DESKTOP_PRODUCT"
    ],
    "where": "usageDate >= '2018-01-01' and usageDate < '2018-02-01'",
    "downloadFileName": "myDesktopSessionLevelExport"
}

```

Show More

## [Response](#response)

### HTTP Status Code Summary

| 200   OK | Request succeeded. |
| --- | --- |
| 400   Bad Request | The provided data was invalid or incorrect. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 429   Too Many Requests | Too many pending export requests. Try again later when currently processing requests have completed. |
| 500   Internal Server Error | An unknown error occurred on the server. |

## [Response](#id4)

### Body Structure (200)

The export request that was submitted. See [GET export request](http-export-contract_number-requests-request_key-GET.md) for a description of fields contained in the response body.

## [Example](#example)

Successful creating an export request for desktop usage for the month October in 2017. (200)

### Request

```
curl  -X POST \
      'https://developer.api.autodesk.com/tokenflex/v1/export/110000917988/requests' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1N' \
      -d '{
        "fields": [
            "productLineCode",
            "productName",
            "productVersion",
            "productFeatureCode",
            "userName",
            "usageDate",
            "usageMonth",
            "contractYear",
            "machineName",
            "licenseServerName",
            "usageType",
            "usageCategory"
        ],
        "metrics": [
            "uniqueProducts",
            "uniqueUsers",
            "tokensConsumed",
            "usageMinutes",
            "useCount"
        ],
        "usageCategory": [
          "DESKTOP_PRODUCT"
        ],
        "where": "usageMonth = '\''2017-10-01'\''",
        "downloadFileName": "DesktopUsage Oct 2017"
    }'

```

Show More

### Response

```
{
    "requestKey": "2018-10-29T03:25:31#4d16aed0-9de2-40c1-9e91-22e3e83c6ce3",
    "requestStatus": "Requested",
    "downloadFileName": "DesktopUsage Oct 2017.csv",
    "exportRequestDate": "2018-10-29T03:25:31.408219Z"
}

```
