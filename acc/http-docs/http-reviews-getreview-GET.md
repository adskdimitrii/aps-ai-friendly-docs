# projects/{projectId}/reviews/{reviewId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/reviews-getreview-GET/

---

Get a Review

GET

# projects/{projectId}/reviews/{reviewId}

Retrieves a specific review in the specified project by review ID.

It includes basic information such as review ID, name, status, initiator, and current step information.

For more details about reviews, see the [Help documentation](https://help.autodesk.com/view/DOCS/ENU/?guid=Reviews).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/reviews/v1/projects/{projectId}/reviews/{reviewId} |
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
- reviewIdstring: UUID The unique ID of the review.
It must be in UUID format — not the numeric sequence ID shown in the Reviews UI. To find the review ID, call [GET reviews](http-reviews-reviews-GET.md).

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the review. |
| --- | --- |
| 400   Bad Request | Bad request. The input parameters were invalid. |
| 403   Forbidden | Forbidden. The user does not have permission to access this resource. |
| 404   Not Found | Not found. The resource does not exist or is inaccessible. |
| 500   Internal Server Error | An unexpected server error occurred. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| id   string: UUID | The unique identifier of the review. |
| --- | --- |
| sequenceId   int | A unique, auto-incrementing number assigned to the review when it is first submitted. <br>This ID does not change, even if the review is sent back to the initiator and goes through multiple rounds. It identifies the review within the project and reflects the order in which reviews were created. |
| name   string | The name of the review. |
| status   enum:string | The current status of the review. <br>Possible values: `OPEN`, `CLOSED`, `VOID`, `FAILED`. |
| currentStepId   string | The ID of the current step in the review. |
| currentStepDueDate   datetime: ISO 8601 | The due date of the current step. |
| createdBy   object | Information about the user who initiated the review. |
| autodeskId   string | The Autodesk ID of the initiator. |
| name   string | The name of the initiator. |
| createdAt   datetime: ISO 8601 | The date time when the review was initiated. |
| updatedAt   datetime: ISO 8601 | The date time when the review was last updated. |
| finishedAt   datetime: ISO 8601 | The date time when the review was completed. |
| archived   boolean | Indicates whether the review has been archived. <br>`true`: the review is archived.<br>`false`: (default) the review is active. |
| archivedBy   object | Information about the user who archived the review. |
| autodeskId   string | The Autodesk ID of the archiver. |
| name   string | The name of the archiver. |
| archivedAt   datetime: ISO 8601 | The date and time when the review was archived. If the review has not been archived, this value is `null`. |
| workflowId   string: UUID | The unique identifier (UUID) of the approval workflow used to create this review. |
| nextActionBy   object | Information about the claimers and candidates responsible for the current step. |
| claimedBy   array: object | A list of users who have already claimed the current step. |
| autodeskId   string | The Autodesk ID of the user. |
| name   string | The name of the user. |
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

## [Example](#example)

Successfully retrieved the review.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/reviews/v1/projects/563a4c30-e30d-4869-ac02-2a18b6447abe/reviews/73c8b3ec-eea2-4240-9c69-f9563e2fec0c' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "id": "37d5145b-c634-407c-b0b4-a65197e43fce",
  "sequenceId": 23,
  "name": "3rd Floor Design Review",
  "status": "OPEN",
  "currentStepId": "Lane_uJtTI3vjaF",
  "currentStepDueDate": "2024-11-09T01:42:16.600Z",
  "createdBy": {
    "autodeskId": "HWUBNU689CRU",
    "name": "James Smith"
  },
  "createdAt": "2024-11-06T01:42:17.476Z",
  "updatedAt": "2024-11-07T12:33:36.421Z",
  "finishedAt": "2024-11-10T02:33:17.336Z",
  "archived": false,
  "archivedBy": {
    "autodeskId": "TTFMLCMCRG5F",
    "name": "Tim Hudson"
  },
  "archivedAt": "2024-11-19T01:38:27.306Z",
  "workflowId": "0b43cedf-5c02-462b-8166-7dfbb13d3476",
  "nextActionBy": {
    "claimedBy": [
      {
        "autodeskId": "HWUBNU689CRU",
        "name": "James Smith"
      }
    ],
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
    }
  }
}

```

Show More
