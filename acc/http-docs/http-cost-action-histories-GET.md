# v1/containers/{containerId}/workflows/action-histories

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-action-histories-GET/

---

Workflow

GET

# v1/containers/{containerId}/workflows/action-histories

Retrieves the action history records associated with specified cost items, such as contracts, budget payments, or RFQs. These records track user actions taken during workflow execution, including approvals and status changes

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/workflows/action-histories |
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

| limit   int | The maximum number of records returned per page. Default: `100`. A page may contain fewer records than the limit if there are fewer matching items or if it is the last page of results. |
| --- | --- |
| sort   string | Defines the sort order for the results. Each attribute can be sorted in `asc` (default) or `desc` order. For example, `sort=name desc` sorts the results by name in descending order. |
| cursorState   string | A cursor token used for paginating results. <br>This value is returned in the response when additional pages of data are available. Pass the returned cursorState into a subsequent request to retrieve the next page of results.<br>The cursor token is an opaque string. Do not modify or parse its contents. |
| associationId*   array: string | The object ID of the item is associated to. For example, ID of the budget, contract or cost item. Use comma separated string for multiple IDs. |
| associationType*   enum:string | The type of the item is associated to. Possible values `Contract`, `Payment`, `BudgetPayment`, `CostPayment`, `Expense`, `PCO`, `OCO`, `SCO`, `RCO`, `RFQ`, `DistributionItem`. |
| filter[type]   string | Filters the results by action history type. <br>Possible values:<br>`Approval` â actions related to approval workflows (e.g., approve, reject).<br>`Normal` â other types of non-approval actions (e.g., created, updated).<br>If not specified, both types are included.<br>Values are case-sensitive. |

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

Expand all

| pagination   object | Pagination metadata for the current response. |
| --- | --- |
| limit   int | The number of records returned in this page of results. |
| totalResults   int | The total number of matching records. |
| cursorState   string | The cursor value used to retrieve this page. |
| nextUrl   string | A URL to retrieve the next page of results. <br>Max length: 2000 |
| results   array: object | A list of action history records. |
| associationId   string | The ID of the object associated with the action history. |
| associationType   string | The type of object associated with the action history (e.g., `Contract`, `SCO`) |
| type   string | The category of the action history. Possible values: `Approval`, `Normal`. |
| action   string | The specific action that occurred (e.g., `review:proceed`, `submitted`, `rejected`). |
| operator   object | Information about the user who performed the action. |
| name   string | The full name of the user who performed the action. |
| email   string | The email address of the user who performed the action. |
| autodeskId   string | The Autodesk ID of the user who performed the action. |
| options   object | Additional context for the action. The fields present in this object depend on the action history type. <br>For Approval workflows, the object includes:<br>`stepName` â the name of the workflow step.<br>`taskDefinitionKey` â the key that identifies the workflow task.<br>`workflowInstanceId` â the ID of the workflow instance.<br>These fields provide task-level process information.<br>For Normal workflows, the object may include fields such as to and from that indicate a change in status. |
| stepName   string | The name of the workflow step where the action occurred. |
| taskDefinitionKey   string | The key that identifies the specific workflow task. |
| workflowInstanceId   string | The ID of the workflow instance the action belongs to. |
| createdAt   datetime: ISO 8601 | The timestamp when the action occurred. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/workflows/action-histories?limit=100&sort=name,createdAt desc&cursorState=AMMAEACAtgALYWRzay53aXBkZXYNZnMuZmlsZS5hZGRlZAZmb2xk&associationId=18d97ae0-9484-11e8-a7ec-7ddae203e404&associationType=Contract' \
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
      "associationId": "1df59db0-9484-11e8-a7ec-7ddae203e404",
      "associationType": "SCO",
      "type": "Approval",
      "action": "review:proceed",
      "operator": {
        "name": "DB cooper",
        "email": "db.cooper@autodesk.com",
        "autodeskId": "FRFNX5QYF6J"
      },
      "options": {
        "stepName": "Internal Review 1",
        "taskDefinitionKey": "UserTask_0",
        "workflowInstanceId": "bff6aa50-2ba4-11f0-92d9-e512a84c9bbc"
      },
      "createdAt": "2019-09-04T01:45:24.582Z"
    }
  ]
}

```

Show More
