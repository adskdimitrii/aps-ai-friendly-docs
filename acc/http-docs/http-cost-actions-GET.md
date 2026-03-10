# v1/containers/{containerId}/workflows/{associationType}/{associationId}/actions

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-actions-GET/

---

Actions

GET

# v1/containers/{containerId}/workflows/{associationType}/{associationId}/actions

List the actions that can execute on the specified item according to the item’s current state.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/workflows/:associationType/:associationId/actions |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

- Authorization*string Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow.
- regionstring Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.Possible values: country or region codes such as `US` or `EMEA`. For the full list of supported regions, see the [ACC Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page.To verify your project’s region, refer to the *Working with BIM 360 Services in Different Regions* section on the [API Basics](https://aps.autodesk.com/en/docs/bim360/v1/overview/basics/#bim-360-account-admin) page.

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see [GET projects](http-admin-accounts-accountidprojects-GET.md). |
| --- | --- |
| associationId   string: UUID | The object ID of the item is associated to. For example, the ID of a budget, contract or cost item. |
| associationType   enum:string | The type of the item with which the actions are associated. Possible values: `FormInstance`, `CostItem`, `OCO`, `PCO`, `RCO`, `RFQ`, `SCO`, `Expense`, `Contract`, `CostPayment`, `BudgetPayment`, `BudgetTransfer`, `MainContract`. |

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

| name   string | The name of the action that you can perform on the item. |
| --- | --- |
| transforms   array: object | The list of changes that you can perform on the associated item. |
| key   string | The name of the attribute that will be changed as a result of performing the action on the item; usually the status of the item. |
| to   string | The new value assigned to the attribute after the action is performed. For example, update `budgetStatus` to `open`. |
| rules   array: object | The list of conditions that are required in order to be able to perform the action. For example, you can only open a PCO’s budgetStatus and costStatus when they are in a draft state. |
| key   string | The name of the attribute on the associated item that will be checked against before performing the action. |
| only   array: string | The value of the attribute that will be checked against before performing the action. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/workflows/FormInstance/18d97ae0-9484-11e8-a7ec-7ddae203e404/actions' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
[
  {
    "name": "open",
    "transforms": [
      {
        "key": "budgetStatus",
        "to": "open"
      }
    ],
    "rules": [
      {
        "key": "budgetStatus",
        "only": "['draft']"
      }
    ]
  }
]

```

Show More
