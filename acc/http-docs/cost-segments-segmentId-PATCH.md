# v1/containers/{containerId}/templates/{templateId}/segments/{segmentId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-segments-segmentId-PATCH/

---

Budget Code Segments

PATCH

# v1/containers/{containerId}/templates/{templateId}/segments/{segmentId}

Updates a segment by ID.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/cost/v1/containers/:containerId/templates/:templateId/segments/:segmentId |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| region   string | Specifies the region where the project data resides. <br>By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.<br>Possible values: country or region codes such as `US` or `EMEA`. For the full list of supported regions, see the [ACC Regions](/en/docs/acc/v1/overview/acc-regions) page.<br>To verify your projectâs region, refer to the *Working with BIM 360 Services in Different Regions* section on the [API Basics](/en/docs/bim360/v1/overview/basics/#bim-360-account-admin) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see [GET projects](/en/docs/bim360/v1/reference/http/admin-accounts-accountidprojects-GET/). |
| --- | --- |
| templateId   string: UUID | The budget code template ID. To obtain a template ID, use [GET templates](/en/docs/bim360/v1/reference/http/cost-templates-GET/). |
| segmentId   string: UUID | The segment ID. To obtain a segment ID, use [GET templates/:templateId/segments](/en/docs/bim360/v1/reference/http/cost-segments-GET/). |

### Request

## [Query String Parameters](#query-string-parameters)

| force   boolean | Force delete segment values when the segment length changes. <br>`true`: force delete,<br>`false`: not force delete. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

The segment to update.

| name   string | The name of the segment in budget code template. <br>Max length: 1024 |
| --- | --- |
| type   string | The segment type. Possible values: `code`, `column`, or `info`. Code segments are displayed as part of the budget code. Column segments are displayed in a separate column. Info segments are not displayed. |
| delimiter   string | The delimiter that follows the segment. Possible values are: `none`, `space`, `point`, `hyphen`, `underscore`, `tab`. |
| length   number | The number of characters allowed in the segment. |
| sampleCode   string | A code sample for the segment used to demonstrate how the segment looks when displayed. |
| isLocked   boolean,null | `true` Lock the segment. <br>`false` Do not lock the segment. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The resource is updated successfully. |
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

The resource is updated successfully.

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/templates/a2a9eb81-052b-4a18-9988-571e8134f98b/segments/87256c07-5c03-42cd-b4dc-e9d06411c0cc' \
  -X 'PATCH' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": "CSI",
        "type": "code",
        "delimiter": "none",
        "length": 6,
        "sampleCode": 6656,
        "isLocked": false
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
