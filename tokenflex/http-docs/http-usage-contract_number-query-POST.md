# usage/:contract_number/query

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/usage-contract_number-query-POST/

---

Usage

POST

# usage/:contract_number/query

Launches a new ad-hoc query.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/tokenflex/v1/usage/:contract_number/query |
| --- | --- |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

## [Request](#request)

### Headers

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

## [Request](#id1)

### URI Parameters

| contract_number   string | Contract number for which you are querying. (see [GET contract](http-contract-GET.md)). |
| --- | --- |

## [Request](#id2)

### Body Structure

The body of the request is a JSON document describing the fields and metrics to use in the query, as well as an optional `where` clause providing criteria used to limit the
scope of the query. Queries must include either metrics or fields, or both metrics and fields. See [Fields and Metrics](https://aps.autodesk.com/en/docs/tokenflex/v1/reference/fields-and-metrics/) for all available Fields and Metrics.
The basic structure of the JSON document is as follows:

| fields   List of fields to use in the query. | `[ "userName", "productName" ]` |
| --- | --- |
| metrics   List of metrics to use in the query. | `[ "uniqueUsers", "tokensConsumed" ]` |
| usageCategory   Optional; list of categories to filter by. | `[ "MANUAL_ADJUSTMENT", "MANUAL_CONSUMPTION" ]` |
| where   Optional; criteria used to limit the query. | `contractYear >= 2 and userName LIKE 'admin%'` |

### Usage limitations

- The keyword `not` is not allowed in the `where` clause. Use `!=` for not equals.

- Wildcard values (`%`) must contain at least three non-wildcard characters (for example, `bob%` is allowed but `b%` is not).

- Wildcard values are not allowed for the enum fields tokenPool, usageCategory, chargeCategory, usageType.

- When requesting fields present only in session/transactional level details, usage categories cannot be mixed, and you must explicitly specify the appropriate usage category(s) in the usageCategory **attribute**.
    For example, reasonComment is only applicable for MANUAL_ADJUSTMENT or MANUAL_ADJUSTMENT. Therefore, you must include these in your usageCategory **attribute** when querying with this Field. It is not sufficient to have them in the `where` clause (although the effect will be the same).

- Due to large volumes, querying desktop or cloud product session level data is not available, use [Export API](http-export-contract_number-requests-POST.md) instead.

### Example ad-hoc query

The below request would yield results describing usage for each desktop product, the unique user count and total usage duration in minutes during contract year 2 with a username that starts with ‘admin’.

```
{
  "fields": [
    "productName"
  ],
  "metrics": [
    "uniqueUsers",
    "usageMinutes"
  ],
  "usageCategory":[
    "DESKTOP_PRODUCT"
  ],
  "where": "contractYear = 2 and userName LIKE 'admin%'"
}

```

Show More

The optional where clause uses standard SQL syntax on any of the possible fields.

## [Response](#response)

### HTTP Status Code Summary

| 200   OK | Request succeeded. |
| --- | --- |
| 400   Bad Request | The provided data was invalid or incorrect. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 500   Internal Server Error | An unknown error occurred on the server. |

## [Response](#id3)

### Body Structure (200)

Note that if the query was previously completed and cached, you may get the results immediately via the `result` object just as you would via [GET usage/:contract_id/query/:query_id](https://aps.autodesk.com/en/docs/tokenflex/v1/reference/http/usage-contract_id-query-query_id-GET/) with a status of `DONE`.

| id   string | The query ID |
| --- | --- |
| detail_uri   string | The URI used in subsequent calls to obtain query status/results; see [GET usage/:contract_id/query/:query_id](https://aps.autodesk.com/en/docs/tokenflex/v1/reference/http/usage-contract_id-query-query_id-GET/) |

## [Examples](#examples)

Querying usage for a contract (200)

### Request

```
curl  -X POST https://developer.api.autodesk.com/tokenflex/v1/usage/11000000001/query \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1N' \
      -H 'Content-Type: application/json' \
      -d '{
              "fields":[
                  "usageCategory",
                  "productName"
              ],
              "metrics":[
                  "tokensConsumed"
              ],
              "where": "contractYear >= 1 AND contractYear<=3 AND productName IN ('Revit Live', 'Vault Office', 'Moldflow Adviser Ultimate', 'ReMake')"
          }'

```

Show More

### Response

```
{
    "status": "QUEUED",
    "id": "dd886b5fd8421fb3871d24e39e53967ce4fc80dd348bedbea0109c0e",
    "detail_uri": "/tokenflex/v1/usage/11000000001/query/dd886b5fd8421fb3871d24e39e53967ce4fc80dd348bedbea0109c0e"
}

```
