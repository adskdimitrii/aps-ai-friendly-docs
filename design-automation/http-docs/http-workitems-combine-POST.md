# workitems/combine

Source: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/workitems-combine-POST/

---

POST

# workitems/combine

The allows users to create a simple fan-in workflow where 1-N workitems (parts) must complete before the final workitem (combinator) is processed.

The following limits apply:

Per-engine. These limits are enforced when the engine processes the workitem.

1. Processing time (LimitProcessingTime)
2. Total size of uncompressed bits for all referenced appbundles (LimitTotalUncompressedAppsSizePerActivity).

Service wide. These limits are enforced during workitem submission.

3. Total processing time per month (LimitMonthlyProcessingTimeInHours).
4. Maximum number of WorkItem of parts in the request is **100**.
5. Activity has to be the same for all WorkItems of parts.

More explanation is at [WorkItem Combine API Reference](/en/docs/design-automation/v3/reference/combinator).

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/da/us-east/v3/workitems/combine |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `code:all` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](/en/docs/oauth/v2/tutorials/get-2-legged-token) or [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [Body Structure](#body-structure)

| parts*   array: object | The WorkItems that must complete before the final workitem. |
| --- | --- |
| combinator*   object | The final WorkItem that start only after the parts are finished. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully create a new WorkItem. |
| --- | --- |
| 400   Bad Request | The request is invalid. |
| 403   Forbidden | The user is not authorized to create the WorkItem. |
| 413 | Payload is too large. |

### Response

## [Body Structure (200)](#body-structure-200)

| parts   array: object | The WorkItem status of parts WorkItems. |
| --- | --- |
| combinator   object | The WorkItem status of the combinator WorkItem. |

## [Example](#example)

Successfully create a new WorkItem.

### Request

```
curl -v 'https://developer.api.autodesk.com/da/us-east/v3/workitems/combine' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "parts": [
          {
            "activityId": "mynickname.part+prod",
            "arguments": {
            "HostDwg": {
              "url": "https://s3.amazonaws.com/TestDwg/host.dwg",
              "verb": "get"
            },
            "Result": {
              "url": "das://intermediate/vararg_page1.pdf",
               "verb":  "put"
              }
            }
          },
          {
            "activityId": "mynickname.part+prod",
            "arguments": {
            "HostDwg": {
              "url": "https://s3.amazonaws.com/TestDwg/1/xref.dwg",
              "verb": "get"
            },
            "Result": {
              "url": "das://intermediate/vararg_page2.pdf",
              "verb":  "put"
            }
            }
          }
        ],
        "combinator": {
          "activityId" : "mynickname.combinator+prod",
          "arguments" : {
            "result" : {
              "url": "https://cdn.us.oss.api.autodesk.com/oss/v2/signedresources/123?region=US",
              "verb": "put"
            }
          }
        }
      }'

```

Show More

### Response

```
{
  "parts": [
      {
          "status": "pending",
          "activityId": "mynickname.part+prod",
          "stats": {
              "timeQueued": "2024-03-09T16:56:05.6688164Z"
          },
          "id": "f9d2d97059cd4febbe13728bbcda4858"
      },
      {
          "status": "pending",
          "activityId": "mynickname.part+prod",
          "stats": {
              "timeQueued": "2024-03-09T16:56:05.6688164Z"
          },
          "id": "2619e594c0ce447d8086518d1b140639"
      }
  ],
  "combinator": {
      "status": "pending",
      "activityId": "mynickname.combinator+prod",
      "stats": {},
      "id": "e19765fe17194839bc52eb6091065dcc"
  }
}

```

Show More
