# workitems?startAfterTime=:epochSecondsInUTC

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/workitems-startAfterTime-GET/

---

GET

# workitems?startAfterTime=:epochSecondsInUTC

Get all WorkItem ids that have been updated after a specified time in the epoch seconds of UTC.

Limits:

1. Retention period (LimitWorkItemRetentionPeriod). WorkItem status is retained for **3 days** after the WorkItem completes.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/da/us-east/v3/workitems?startAfterTime=:epochSecondsInUTC |
| --- | --- |
| Authentication Context |  |
| Required OAuth Scopes | `code:all` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) OAuth flow. |
| --- | --- |

* Required

### Request

## [Query String Parameters](#query-string-parameters)

| startAfterTime*   integer | The epoch seconds of UTC time. |
| --- | --- |
| page   string | Access an additional page of data when necessary, based on the `paginationToken` returned from a previous invocation. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully get the Ids of a WorkItem. |
| --- | --- |
| 400   BadRequest | three-legged token is disallowed. Or `startAfterTime` is not provided or it is **5 days older than Utc.Now** |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| paginationToken   string |  |
| --- | --- |
| data   array: object |  |
| id   string | The WorkItem id. |
| lastModifiedInUTCEpochSecond   integer | The last modified time stamp of the WorkItem id in the epoch seconds of UTC. |

## [Example 1](#example-1)

Successfully get the WorkItem ids updated after a specified time in the epoch seconds of UTC.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/workitems?startAfterTime=1709780574000' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "paginationToken": "eyJTdGFydEFmdGVyVGltZSI6",
  "data": [
      {
          "id": "00365ed602d64d669c3121ef0b6e90eb",
          "lastModifiedInUTCEpochSecond": 1709702768
      },
      {
          "id": "0134b3d6dbf245ce82d8a2707d2e6128",
          "lastModifiedInUTCEpochSecond": 1709702768
      },
      {
          "id": "00eeabf6731d403f973d27856d822cc4",
          "lastModifiedInUTCEpochSecond": 1709703379
      },
      {
          "id": "007c0424fcb944349b7098b1ecdca663",
          "lastModifiedInUTCEpochSecond": 1709704867
      },
      {
          "id": "01d5e5ea71f14815a65c3ea7012b821d",
          "lastModifiedInUTCEpochSecond": 1709713268
      }
  ]
}

```

Show More

## [Example 2](#example-2)

Successfully get the WorkItem Ids updated after a specified time in the additional page using a paginationToken.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/workitems?startAfterTime=1709780574000&page=eyJTdGFydEFmdGVyVGltZSI6' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "paginationToken": "eyJTdGFydEFmdGVyVGltZSI6MTcwOTY5N",
  "data": [
      {
          "id": "03d65402faeb4409ac672f341462f689",
          "lastModifiedInUTCEpochSecond": 1709694967
      },
      {
          "id": "032a3a8e25b3409584194e7221a40019",
          "lastModifiedInUTCEpochSecond": 1709697966
      }
  ]
}

```

Show More
