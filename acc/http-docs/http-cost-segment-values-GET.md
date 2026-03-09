# v1/containers/{containerId}/segment-values

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-segment-values-GET/

---

Budget Code Segment Values

GET

# v1/containers/{containerId}/segment-values

Retrieves the defined segment values for the specified budget code segment.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/segment-values |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

- Authorization*string Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow.
- regionstring Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.Possible values: country or region codes such as `US` or `EMEA`. For the full list of supported regions, see the [ACC Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page.To verify your projectâs region, refer to the *Working with BIM 360 Services in Different Regions* section on the [API Basics](https://aps.autodesk.com/en/docs/bim360/v1/overview/basics/#bim-360-account-admin) page.

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see [GET projects](http-admin-accounts-accountidprojects-GET.md). |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| filter[segmentId]   array: string: uuid | The budget code segment ID. Separate multiple IDs with commas. For example, `filter[segmentId]=id1,id2`. |
| --- | --- |
| filter[code]   array: string | Returns only items that are identified by the specified codes (separated by commas). For example, `filter[code]="2703,2704"`. <br>Note that even single codes in number format must be enclosed in double quotes:`filter[code]="1"` or `filter[code]="122. 221"`. |
| filter[originalCode]   array: string | Returns only the values of segments with the specified original codes, including delimiters. For example, `filter[originalCode]=27-03,27-04`. |
| filter[id]   array: string: uuid | Returns only the items that are identified by the provided list of item IDs. Separate multiple IDs with commas. For example, `filter[id]=id1,id2`. |
| filter[parentId]   array: string: uuid | Returns only the values of segments with the specified IDs of parent segments. Separate multiple parent IDs with commas. For example, `filter[parentId]=parentId1,parentId2`. You can also return the values of segments that have no parent by including `filter[parentId]=blank`. |
| filter[lastModifiedSince]   string | Returns only items that were modified since the specified date and time, in ISO 8601 format. For example, `filter[lastModifiedSince]=2020-03-01T13:00:00Z`. |
| limit   int | The maximum number of records returned per page. Default: `100`. A page may contain fewer records than the limit if there are fewer matching items or if it is the last page of results. |
| sort   string | Defines the sort order for the results. Each attribute can be sorted in `asc` (default) or `desc` order. For example, `sort=name desc` sorts the results by name in descending order. |
| cursorState   string | A cursor token used for paginating results. <br>This value is returned in the response when additional pages of data are available. Pass the returned cursorState into a subsequent request to retrieve the next page of results.<br>The cursor token is an opaque string. Do not modify or parse its contents. |

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

| pagination   object | Pagination metadata for the current response. |
| --- | --- |
| limit   int | The number of records returned in this page of results. |
| totalResults   int | The total number of matching records. |
| cursorState   string | The cursor value used to retrieve this page. |
| nextUrl   string | A URL to retrieve the next page of results. <br>Max length: 2000 |
| results   array: object | The detailed segment definition values |
| id   string: UUID | The ID of the code. |
| segmentId   string: UUID | The ID of the segment this code belongs to. |
| parentId   string,null | The parent ID of this code if it is the sub item of another code. |
| code   string | The display code. <br>Max length: 255 |
| originalCode   string | The original value of the code before the delimiters are removed. <br>Max length: 255 |
| description   string | The description of the code. <br>Max length: 2048 |
| createdAt   datetime: ISO 8601 | The date and time that the item was created, in ISO 8601 format. |
| updatedAt   datetime: ISO 8601 | The date and time that the item was last updated, in ISO 8601 format. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/segment-values?filter[lastModifiedSince]=2020-03-01T13:00:00Z&limit=100&sort=name,createdAt desc&cursorState=AMMAEACAtgALYWRzay53aXBkZXYNZnMuZmlsZS5hZGRlZAZmb2xk' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 20,
    "totalResults": 1,
    "cursorState": "",
    "nextUrl": ""
  },
  "results": [
    {
      "id": "229d3420-9481-11e8-87fb-215990a8aeb3",
      "segmentId": "87256c07-5c03-42cd-b4dc-e9d06411c0cc",
      "parentId": "null",
      "code": 6656,
      "originalCode": "01 50 00",
      "description": "Temporary Facilities and Controls",
      "createdAt": "2019-01-06T01:24:22.678Z",
      "updatedAt": "2019-09-05T01:00:12.989Z"
    }
  ]
}

```

Show More
