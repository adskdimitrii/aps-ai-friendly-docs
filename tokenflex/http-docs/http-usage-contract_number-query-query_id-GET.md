# usage/:contract_number/query/:query_id

Source: https://aps.autodesk.com/en/docs/tokenflex/reference/http/usage-contract_number-query-query_id-GET/

---

Usage

GET

# usage/:contract_number/query/:query_id

Check the status and results for an existing query.

See [POST usage/:contract_number/query](http-usage-contract_number-query-POST.md) on how to make a request.
Note that results from a query are available only for a limited amount of time. The exact time duration depends on system conditions and load, but results are guaranteed for at least 5 minutes after the results are first available.
Once a query result has expired, you must submit the request again.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/tokenflex/v1/usage/:contract_number/query/:query_id |
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

| contract_number   string | Contract under which you are querying. This must match the contract that the original request was submitted against. |
| --- | --- |
| query_id   string | ID of the query to return |

## [Request](#id2)

### Query String Parameters

| offset   integer | Requested offset (starting point) to return a subset of query results; defaults to 0. |
| --- | --- |
| limit   integer | Number of query results to return; defaults to 100. |

## [Response](#response)

### HTTP Status Code Summary

| 200   OK | Request succeeded. |
| --- | --- |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 500   Internal Server Error | An unknown error occurred on the server. |

## [Response](#id3)

### Body Structure (200)

Expand all

| id   string | The query ID |
| --- | --- |
| status   string | The query status (one of QUEUED, PROCESSING, DONE, FAILED, TIMEOUT, EXPIRED) |
| result   object | An object representing the results of the query. |
| columns   array of strings | Array of column names (which can be both Fields and/or Metrics) returned in the results. |
| rows   array of strings | The query results, in the same order as `result.columns` |
| limit   integer | The requested limit |
| offset   integer | The requested offset |
| total   integer | Total number of results returned by this query |

## [Examples](#examples)

Querying usage for a contract (200)

### Request

```
curl  -X GET \
      https://developer.api.autodesk.com/tokenflex/v1/usage/11000000001/query/dd886b5fd8421fb3871d24e39e53967ce4fc80dd348bedbea0109c0e \
      -H 'Authorization: Bearer eyJhbGciOiJIUzI1N'

```

### Response

```
{
    "id": "dd886b5fd8421fb3871d24e39e53967ce4fc80dd348bedbea0109c0e",
    "status": "PROCESSING"
}

```
