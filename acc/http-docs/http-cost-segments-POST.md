# v1/containers/{containerId}/templates/{templateId}/segments

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-segments-POST/

---

Budget Code Segments

POST

# v1/containers/{containerId}/templates/{templateId}/segments

Creates a new segment in the budget code template.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/cost/v1/containers/:containerId/templates/:templateId/segments |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| region   string | Specifies the region where the project data resides. <br>By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.<br>Possible values: country or region codes such as `US` or `EMEA`. For the full list of supported regions, see the [ACC Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page.<br>To verify your projectâs region, refer to the *Working with BIM 360 Services in Different Regions* section on the [API Basics](https://aps.autodesk.com/en/docs/bim360/v1/overview/basics/#bim-360-account-admin) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see [GET projects](http-admin-accounts-accountidprojects-GET.md). |
| --- | --- |
| templateId   string: UUID | The budget code template ID. To obtain a template ID, use [GET templates](http-cost-templates-GET.md). |

### Request

## [Body Structure](#body-structure)

The `Segment`

| name*   string | The name of the budget code template. <br>Max length: 1024 |
| --- | --- |
| type   string | The segment type. Possible values: `code`, `column`, or `info`. Code segments are displayed as part of the budget code. Column segments are displayed in a separate column. Info segments are not displayed. Default to `code` |
| delimiter   string | The delimiter that follows the segment. Possible values are: `none`, `space`, `point`, `hyphen`, `underscore`, `tab`. Default to `none` |
| length   number | The number of characters allowed in the segment. Minimum length is 1 and maximum is 100. Default to 100. |
| isVariableLength   boolean | Whether the segment is flexible length. Default to `false` |
| position   number | The order of the segment in the budget code template. |
| sampleCode   string | A code sample for the segment used to demonstrate how the segment looks when displayed. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Success |
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

## [Body Structure (201)](#body-structure-201)

| id   string: UUID | The ID of the segment in the budget code template. |
| --- | --- |
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
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/templates/a2a9eb81-052b-4a18-9988-571e8134f98b/segments' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": "Project Code",
        "type": "code",
        "delimiter": "none",
        "length": 6,
        "isVariableLength": false,
        "position": 0,
        "sampleCode": 6656
      }'

```

Show More

### Response

```
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

```

Show More
