# projects/{projectId}/versions/{versionId}/approval-statuses

Source: https://aps.autodesk.com/en/docs/acc/reference/http/reviews-getversionapprovalstatuses-GET/

---

List Approval Statuses of a Version

GET

# projects/{projectId}/versions/{versionId}/approval-statuses

Retrieves the full approval records and review references of a specific file version.

This includes all reviews the version has participated in, along with each review’s status (e.g., `OPEN`, `CLOSED`) and the file’s approval status (e.g., `APPROVED`, `REJECTED`) within that review.

The results are sorted in reverse chronological order within each group: those in the “In Review” status and those in the “Finished Review” status (Approved or Rejected), based on the review’s `sequenceId`.

This endpoint is typically used in the Files tool, where you can view the file’s activity across multiple reviews.

For more context, see the [Help documentation](https://help.autodesk.com/view/DOCS/ENU/?guid=BIM360D_Document_Management_About_Reviews_Reviews_FAQs_Reference_html).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/reviews/v1/projects/{projectId}/versions/{versionId}/approval-statuses |
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
- versionIdstring The URL-encoded unique identifier (URN) of the file version whose review and approval history you want to retrieve. For example, encode `urn:adsk.wipprod:fs.file:vf.Ibsc4cPuQEqBHRJdBjhr6w?version=2``as ``urn%3Aadsk.wipprod%3Afs.file%3Avf.Ibsc4cPuQEqBHRJdBjhr6w%3Fversion%3D2`.To find the latest version, call [GET versions](http-reviews-getreviewversions-GET.md) and check the `urn` field.

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | The maximum number of results to return in the response. Possible values: `1–50`. Maximum: `50`. Default: `50`. For example: `limit=2`. |
| --- | --- |
| offset   int | The number of results to skip from the beginning of the list. Used for pagination. Default: `0`. For example: `offset=10`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the review and approval history for the file version |
| --- | --- |
| 400   Bad Request | Bad request. The input parameters were invalid. |
| 403   Forbidden | Forbidden. The user does not have permission to access this resource. |
| 404   Not Found | Not found. The resource does not exist or is inaccessible. |
| 500   Internal Server Error | An unexpected server error occurred. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | A list of approval statuses and related review information for the specified file version. |
| --- | --- |
| approvalStatus   object | The file’s approval status within a specific review. |
| id   string | The ID of the approval status option. |
| label   string | The custom text used to describe the approval status. <br>Max length: 255 |
| value   enum:string | The value of the approval status. Possible values: `APPROVED`, `REJECTED`, `IN_REVIEW`. |
| review   object | Metadata about the review in which this file version was included. |
| id   string: UUID | The ID of the review. |
| sequenceId   int | A unique, auto-incrementing number assigned to the review when it is first submitted. <br>This ID does not change, even if the review is sent back to the initiator and goes through multiple rounds. It identifies the review within the project and reflects the order in which reviews were created. |
| status   enum:string | The current status of the review. <br>Possible values: `OPEN`, `CLOSED`, `VOID`, `FAILED`. |
| pagination   object | Metadata about the paginated results. |
| limit   int | The maximum number of results returned per page. |
| offset   int | The number of results skipped before the current page. Zero-based index. |
| totalResults   int | The total number of results that match the query, regardless of pagination. |
| nextUrl   string | The URL to retrieve the next page of file approval statuses results, if any. If not included, this is the last page. |

## [Example](#example)

Successfully retrieved the review and approval history for the file version

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/reviews/v1/projects/563a4c30-e30d-4869-ac02-2a18b6447abe/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.Ibsc4cPuQEqBHRJdBjhr6w%3Fversion%3D2/approval-statuses?limit=2&offset=10' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "results": [
    {
      "approvalStatus": {
        "id": "f44e623d-f04f-47fe-8195-efc43d1d985b",
        "label": "Approved",
        "value": "APPROVED"
      },
      "review": {
        "id": "37d5145b-c634-407c-b0b4-a65197e43fce",
        "sequenceId": 23,
        "status": "OPEN"
      }
    }
  ],
  "pagination": {
    "limit": 10,
    "offset": 0,
    "totalResults": 100,
    "nextUrl": "https://developer.api.autodesk.com/construction/reviews/v1/projects/497f6eca-6276-4993-bfeb-53cbbbba6f08/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.Ibsc4cPuQEqBHRJdBjhr6w%3Fversion%3D2/approval-statuses?limit=50&offset=50"
  }
}

```

Show More
