# v1/containers/{containerId}/properties

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-properties-GET/

---

Attribute Definitions

GET

# v1/containers/{containerId}/properties

Lists all the attribute definitions created to define custom attributes for a given module.

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/properties |
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

### Request

## [Query String Parameters](#query-string-parameters)

| filter[name]   string | Returns only items with the specified name. For example, `filter[name]=Labor`. <br>Max length: 255 |
| --- | --- |
| filter[associationId]   array: string: uuid | The ID of the associated item, for example, the ID of a budget, contract, change order or cost item. Separate multiple IDs with commas, for example, `filter[associationId]=id1,id2`. |
| filter[associationType]   string | The type of the associated item. Possible values: `Budget`, `Contract`, `CostItem`, `FormDefinition`, `Payment`, `BudgetPayment`, `Expense`, `ExpenseItem`. For example, `filter[associationType]=Budget`. |
| filter[lastModifiedSince]   string | Returns only items that were modified since the specified date and time, in ISO 8601 format. For example, `filter[lastModifiedSince]=2020-03-01T13:00:00Z`. |

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

| id   string: UUID | Unique identifier (UUID) of the attribute definition. |
| --- | --- |
| name   string | Name of a attribute definition. <br>Max length: 1024 |
| type   enum:string | Type of the attribute definition. Possible values: `text`, `multiline`, `richtext`, `options`, `boolean`, `integer`, `percent`, `currency`, `number`, `datetime` |
| defaultValue   string,null | Default value of the attribute definition. |
| position   number | The position of the attribute definition as displayed in BIM 360 Cost Management. |
| category   string | Not relevant |
| defaultVisibility   boolean | A true/false flag to indicate whether this attribute should be shown in the BIM 360 Cost Management or generated documents by default. |
| builtIn   boolean | A true/false flag to indicate whether this is a pre-defined attribute or not. |
| componentTemplateId   string,null | Custom attribute belongs to the component template |
| options   array: string,object | List of items for an `options` type attribute. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/properties?filter[associationType]=Budget&filter[lastModifiedSince]=2020-03-01T13:00:00Z' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
[
  {
    "id": "229d3420-9481-11e8-87fb-215990a8aeb3",
    "name": "Scope",
    "type": "text",
    "defaultValue": "tbd",
    "position": 0,
    "category": "pco",
    "defaultVisibility": false,
    "builtIn": true,
    "componentTemplateId": "229d3420-9481-11e8-87fb-215990a8aeb3",
    "options": [
      "Back Charge"
    ]
  }
]

```

Show More
