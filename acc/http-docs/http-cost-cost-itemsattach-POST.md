# v1/containers/{containerId}/cost-items:attach

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-cost-itemsattach-POST/

---

Change Order and Cost Items

POST

# v1/containers/{containerId}/cost-items:attach

Add existing cost items to a change order

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/cost/v1/containers/:containerId/cost-items:attach |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| region   string | Specifies the region where the project data resides. <br>By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.<br>Possible values: country or region codes such as `US` or `EMEA`. For the full list of supported regions, see the [ACC Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page.<br>To verify your project’s region, refer to the *Working with BIM 360 Services in Different Regions* section on the [API Basics](https://aps.autodesk.com/en/docs/bim360/v1/overview/basics/#bim-360-account-admin) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see [GET projects](http-admin-accounts-accountidprojects-GET.md). |
| --- | --- |

### Request

## [Body Structure](#body-structure)

List of change order and cost item IDs.

| changeOrderId*   string: UUID | The ID of the change order to which the cost item will be attached. |
| --- | --- |
| costItemId*   string: UUID | The ID of the cost item to attach. |

* Required

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

| changeOrderId   string: UUID | The ID of the change order to which the cost item will be attached. |
| --- | --- |
| costItemId   string: UUID | The ID of the cost item to attach. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/cost-items:attach' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '[
        {
          "changeOrderId": "20982940-85c3-11e8-b1f7-b981d6e78764",
          "costItemId": "27ace7c0-85c3-11e8-b1f7-b981d6e78764"
        }
      ]'

```

Show More

### Response

```
[
  {
    "changeOrderId": "20982940-85c3-11e8-b1f7-b981d6e78764",
    "costItemId": "27ace7c0-85c3-11e8-b1f7-b981d6e78764"
  }
]

```
