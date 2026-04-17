# v1/containers/{containerId}/templates/{templateId}/segments

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-templates-templateId-segments-GET/

---

Budget Code Segments

GET

# v1/containers/{containerId}/templates/{templateId}/segments

Retrieves all of the segments in a budget code template.

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/templates/:templateId/segments |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

- Authorization*string Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context.
- regionstring Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.Possible values: country or region codes such as `US` or `EMEA`. For the full list of supported regions, see the [Forma Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page.To verify your project’s region, refer to the *Working with BIM 360 Services in Different Regions* section on the [API Basics](https://aps.autodesk.com/en/docs/bim360/v1/overview/basics/#bim-360-account-admin) page.

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see [GET projects](http-admin-accounts-accountidprojects-GET.md). |
| --- | --- |
| templateId   string: UUID | The budget code template ID. To obtain a template ID, use [GET templates](http-cost-templates-GET.md). |

### Request

## [Query String Parameters](#query-string-parameters)

| filter[name]   string | Returns only items with the specified name. For example, `filter[name]=Labor`. <br>Max length: 255 |
| --- | --- |
| filter[lastModifiedSince]   string | Returns only items that were modified since the specified date and time, in ISO 8601 format. For example, `filter[lastModifiedSince]=2020-03-01T13:00:00Z`. |
| offset   int | The number of records to skip before returning results. Used together with `limit` to paginate through results, where `offset` specifies the starting point and `limit` specifies the number of records to return. |
| limit   int | The maximum number of records returned per page. Default: `100`. A page may contain fewer records than the limit if there are fewer matching items or if it is the last page of results. |
| sort   string | Defines the sort order for the results. Each attribute can be sorted in `asc` (default) or `desc` order. For example, `sort=name desc` sorts the results by name in descending order. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Success |
| --- | --- |
| 400   Bad Request | The parameters are invalid. |
| 401   Unauthorized | The provided bearer token is invalid. |
| 403   Forbidden | Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The resource or endpoint cannot be found. |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the resource. |
| 429   Too Many Requests | Rate limit exceeded. Retry your request after a few minutes. |
| 500   Internal Server Error | An unexpected error occurred on the server. |
| 503   Service Unavailable | Service unavailable. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| pagination   object | Contains pagination information when data is returned page by page. |
| --- | --- |
| limit   int | The maximum number of records returned in the response. |
| offset   int | The number of records skipped before returning the page of results. |
| totalResults   int | The total number of records that matched the request criteria. |
| nextUrl   string | The URL for the next request to retrieve the next page of results. Max length: 2000. <br>Max length: 2000 |
| results   array: object | The detailed segment definition values |
| id   string: UUID | The ID of the segment in the budget code template. |
| templateId   string: UUID | The ID of the budget code template. |
| name   string | The name of the segment in budget code template. <br>Max length: 1024 |
| type   string | The segment type. Possible values: `code`, `column`, or `info`. Code segments are displayed as part of the budget code. Column segments are displayed in a separate column. Info segments are not displayed. |
| delimiter   string | The delimiter that follows the segment. Possible values are: `none`, `space`, `point`, `hyphen`, `underscore`, `tab`. |
| delimiterChar   string | The delimiter char after the segment. For example, `.`, `-`, `_`. |
| length   number | The number of characters allowed in the segment. |
| isVariableLength   boolean | Whether the segment is variable length. |
| position   number | The order of the segment in the budget code template. |
| sampleCode   string | A code sample for the segment used to demonstrate how the segment looks when displayed. |
| isLocked   boolean,null | The lock status of segment. |
| createdAt   datetime: ISO 8601 | The date and time that the item was created, in ISO 8601 format. |
| updatedAt   datetime: ISO 8601 | The date and time that the item was last updated, in ISO 8601 format. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/templates/a2a9eb81-052b-4a18-9988-571e8134f98b/segments?filter[lastModifiedSince]=2020-03-01T13:00:00Z&limit=100&sort=name,createdAt desc' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 20,
    "offset": 0,
    "totalResults": 1,
    "nextUrl": ""
  },
  "results": [
    {
      "id": "87256c07-5c03-42cd-b4dc-e9d06411c0cc",
      "templateId": "a2a9eb81-052b-4a18-9988-571e8134f98b",
      "name": "CSI",
      "type": "code",
      "delimiter": "none",
      "delimiterChar": "",
      "length": 6,
      "isVariableLength": false,
      "position": 0,
      "sampleCode": 6656,
      "isLocked": false,
      "createdAt": "2019-01-06T01:24:22.678Z",
      "updatedAt": "2019-09-05T01:00:12.989Z"
    }
  ]
}

```

Show More
