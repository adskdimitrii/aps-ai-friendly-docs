# projects/{projectId}/reviews/{reviewId}/progress

Source: https://aps.autodesk.com/en/docs/acc/reference/http/reviews-getreviewprogress-GET/

---

List Review Progress

GET

# projects/{projectId}/reviews/{reviewId}/progress

Retrieves the progress of a specific review in the specified project.

This endpoint tracks the current state of each step in the review’s approval workflow, showing the assigned candidates, whether steps have been claimed or submitted, and who performed each action. Results are returned in reverse chronological order (most recent action first).

Note that this endpoint only returns data for the current round of the review.

To retrieve the review’s configuration and metadata, call [GET reviews/:reviewId](http-reviews-getreview-GET.md).

For more details about reviews, see the [Help documentation](https://help.autodesk.com/view/DOCS/ENU/?guid=Reviews).
> Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/reviews/v1/projects/{projectId}/reviews/{reviewId}/progress |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-user-id   string | The ID of a user on whose behalf the request is made. Your application has access to all users specified by the administrator in the SaaS Integrations UI. Use this header to specify which user should be affected by the request. <br>This header is only required when using two-legged authentication. It is not needed for three-legged authentication.<br>Only user’s Autodesk ID (`autodeskId`) can be accepted. |

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring: UUID The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You can provide the project ID with or without the “**b.**" prefix.

- Example with prefix: **b.563a4c30-e30d-4869-ac02-2a18b6447abe**
- Example without prefix: **563a4c30-e30d-4869-ac02-2a18b6447abe**
- reviewIdstring: UUID The unique ID of the review. This must be the UUID, not the numeric sequence ID shown in the Reviews UI.To find the review ID, call [GET reviews](en/docs/acc/v1/reference/http/reviews-reviews-GET/).

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | The maximum number of review-progress records to return. Valid range: `1–50`. Default: `50`. For example: `limit=2`. |
| --- | --- |
| offset   int | The zero-based index of the first record to return. Use with `limit` for pagination. Default: `0`. For example: `offset=10`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The review progress was retrieved successfully. |
| --- | --- |
| 400   Bad Request | Bad request. The input parameters were invalid. |
| 403   Forbidden | Forbidden. The user does not have permission to access this resource. |
| 404   Not Found | Not found. The resource does not exist or is inaccessible. |
| 500   Internal Server Error | An unexpected server error occurred. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | The list of review-progress records, returned in reverse chronological order. |
| --- | --- |
| stepId   string | The ID of the review step this progress record relates to. |
| stepName   string | The name of the review step this progress record relates to. |
| claimedBy   object | Information about the user who claimed the step. |
| autodeskId   string | The Autodesk ID of the user. To find details about the user, call [GET users/:Id](http-admin-projectsprojectId-users-userId-GET.md). |
| name   string | The name of the user. |
| actionBy   object | Information about the user recorded when the step status is `SUBMITTED` or `VOID`. In the Reviews UI, these statuses occur when a participant submits their decision or when a step is voided. |
| autodeskId   string | The Autodesk ID of the user. To find details about the user, call [GET users/:Id](http-admin-projectsprojectId-users-userId-GET.md). |
| name   string | The name of a user. |
| candidates   object | Information about the users, roles, and companies who are eligible to take the next action in this step. |
| roles   array: object | Project roles that can act in this step. |
| autodeskId   string | The Autodesk ID of the role. |
| name   string | The name of the role. |
| users   array: object | Individual users who can act in this step. |
| autodeskId   string | The Autodesk ID of the user. |
| name   string | The name of the user. |
| companies   array: object | Companies that can act in this step. |
| autodeskId   string | The Autodesk ID of the company. |
| name   string | The name of the company. |
| endTime   datetime: ISO 8601 | The date and time when the step ended. This value is set when the step is completed, either by being submitted or voided. |
| notes   string | Additional information recorded for this step in the review’s progress. |
| status   enum:string | The current status of the step. Possible values: <br>`CLAIMED`: A user has claimed the step.`UNCLAIMED`: No user has claimed the step.`SUBMITTED`: A user submitted the step (e.g., approved/rejected/custom).`VOID`: The step was voided. |
| pagination   object | Metadata about the paginated results. |
| limit   int | The maximum number of results returned per page. |
| offset   int | The number of results skipped before the current page. Zero-based index. |
| totalResults   int | The total number of results that match the query, regardless of pagination. |
| nextUrl   string | The URL for the next page of results. If omitted, there are no more pages. |

## [Example](#example)

The review progress was retrieved successfully.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/reviews/v1/projects/563a4c30-e30d-4869-ac02-2a18b6447abe/reviews/73c8b3ec-eea2-4240-9c69-f9563e2fec0c/progress?limit=2&offset=10' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "results": [
    {
      "stepId": "Lane_uJtTI3vjaF",
      "stepName": "Reviewer",
      "claimedBy": {
        "autodeskId": "HWUBNU689CRU",
        "name": "James Smith"
      },
      "actionBy": {
        "autodeskId": "HWUBNU689CRU",
        "name": "James Smith"
      },
      "candidates": {
        "roles": [
          {
            "autodeskId": "1473817",
            "name": "Architect"
          }
        ],
        "users": [
          {
            "autodeskId": "HWUBNU689CRU",
            "name": "James Smith"
          }
        ],
        "companies": [
          {
            "autodeskId": "26980302",
            "name": "Autodesk Co. Ltd."
          }
        ]
      },
      "endTime": "2024-11-19T01:38:27.306Z",
      "notes": "Please check all rebar annotations before approving. Include markup if changes are required.",
      "status": "CLAIMED"
    }
  ],
  "pagination": {
    "limit": 10,
    "offset": 0,
    "totalResults": 100,
    "nextUrl": "https://developer.api.autodesk.com/construction/reviews/v1/projects/497f6eca-6276-4993-bfeb-53cbbbba6f08/reviews/73c8b3ec-eea2-4240-9c69-f9563e2fec0c/progress?limit=10&offset=10"
  }
}

```

Show More
