# projects/{projectId}/reviews/{reviewId}/versions

Source: https://aps.autodesk.com/en/docs/acc/reference/http/reviews-getreviewversions-GET/

---

List Review Versions

GET

# projects/{projectId}/reviews/{reviewId}/versions

Retrieves the file versions included in the latest round of the specified review.

A review may go through multiple rounds when the “Back to initiator” feature is used. This endpoint only returns data from the most recent round.

The response includes approval statuses, file version names, copied version URNs (if applicable), and any custom attributes captured during the review.

For more details about reviews, see the [Help documentation](https://help.autodesk.com/view/DOCS/ENU/?guid=Reviews).

Note that to export reviewing files using these version URNs, see [Step 3 in the PDF File Export](../how-to-docs/files-export-pdf-files.md#step-3-export-the-files) tutorial.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/reviews/v1/projects/{projectId}/reviews/{reviewId}/versions |
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

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | The number of file versions to return in the response. Possible values: `1-50`. Maximum: `50`. Default: `50`. For example: `limit=2`. |
| --- | --- |
| offset   int | The index of the first result to return (zero-based). Default: `0`. For example: `offset=10`. |
| filter[approveStatus]   array | Filters the results based on the approval status assigned to each file during the review. It should be URL-encoded. <br>The filter applies to the `label` of the approval status, as defined in the workflow — not the internal value.<br>For example, if your workflow includes a status labeled `Approved with comments`, you would filter using that label:<br>`filter[approveStatus]=Approved with comments`.<br>This is especially useful when a workflow includes multiple approval options with customized labels.<br>Note: It supports multiple values.<br>For example, if you want to filter with 2 labels: both `Approved` and `Rejected`, you could filter with the query string:<br>`filter[approveStatus]=Approved&filter[approveStatus]=Rejected` |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the file versions in the latest review round |
| --- | --- |
| 400   Bad Request | Bad request. The input parameters were invalid. |
| 403   Forbidden | Forbidden. The user does not have permission to access this resource. |
| 404   Not Found | Not found. The resource does not exist or is inaccessible. |
| 500   Internal Server Error | An unexpected server error occurred. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | A list of file versions included in the latest round of the review. |
| --- | --- |
| urn   string | The URN of the file version currently under review. <br>This value is used when retrieving the full approval and review history of a specific version. See [GET approval-statuses](http-reviews-getversionapprovalstatuses-GET.md) for more details. |
| itemUrn   string | The URN of the file item this version belongs to. |
| approveStatus   object | The approval status assigned to the file during the review. |
| id   string | The ID of the approval status. |
| label   string | The custom label assigned to the approval status. <br>Max length: 255 |
| value   enum:string | The internal value representing the approval status outcome. Possible values: `APPROVED`, `REJECTED`. |
| reviewContent   object | Review-specific metadata related to the file version. |
| name   string | The pending file name assigned during the review. <br>If the review is approved, this becomes the official version name. In most cases, this value is automatically generated according to the naming standard configured on the folder. |
| customAttributes   array: object | A list of custom attributes applied to the file during the review. |
| id   int | The ID of the attribute. |
| type   enum:string | The data type of the attribute. Possible values: `string` (text field), `date`, `array` (drop-list). |
| name   string | The name of the attribute. |
| value   string | The value of the attribute. |
| copiedFileVersionUrn   string | The URN of the version copied to the target folder after the file was approved. <br>This field is only present if the workflow includes a copy action and the file was approved. |
| name   string | The name of the resulting file version. |
| pagination   object | Metadata about the paginated results. |
| limit   int | The maximum number of results returned per page. |
| offset   int | The number of results skipped before the current page. Zero-based index. |
| totalResults   int | The total number of results that match the query, regardless of pagination. |
| nextUrl   string | The URL to retrieve the next page of file versions results, if any. If not included, this is the last page. |

## [Example](#example)

Successfully retrieved the file versions in the latest review round

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/reviews/v1/projects/563a4c30-e30d-4869-ac02-2a18b6447abe/reviews/73c8b3ec-eea2-4240-9c69-f9563e2fec0c/versions?limit=2&offset=10&filter[approveStatus]=Approved' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "results": [
    {
      "urn": "urn:adsk.wipprod:fs.file:vf.Zvg8qMkjQ26MBJjIA2ZjeU?version=1",
      "itemUrn": "urn:adsk.wipprod:dm.lineage:Zvg8qMkjQ26MBJjIA2ZjeU",
      "approveStatus": {
        "id": "f44e623d-f04f-47fe-8195-efc43d1d985b",
        "label": "Approved",
        "value": "APPROVED"
      },
      "reviewContent": {
        "name": "3rd Floor 3D Models (shared).pdf",
        "customAttributes": [
          {
            "id": 1001,
            "type": "string",
            "name": "Reference Document Number",
            "value": "X-3910-3DWA"
          }
        ]
      },
      "copiedFileVersionUrn": "urn:adsk.wipprod:fs.file:vf.Zvg8qMkjQ26MBJjIA2ZjeK?version=3",
      "name": "3rd Floor 3D Models.pdf"
    }
  ],
  "pagination": {
    "limit": 10,
    "offset": 0,
    "totalResults": 100,
    "nextUrl": "https://developer.api.autodesk.com/construction/reviews/v1/projects/497f6eca-6276-4993-bfeb-53cbbbba6f08/reviews/73c8b3ec-eea2-4240-9c69-f9563e2fec0c/versions?limit=10&offset=10"
  }
}

```

Show More
