# v1/containers/{containerId}/property-values:batch-update

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-property-valuesbatch-update-POST/

---

Attribute Values

POST

# v1/containers/{containerId}/property-values:batch-update

Updates the existing values of multiple custom attributes associated with an item such as a Budget, Contract, Cost Item, PCO, and so on.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/cost/v1/containers/:containerId/property-values:batch-update |
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

The values of the properties.

| associationId*   string: UUID | The object ID of the item associated with the actions, such as a budget, contract, or cost item. |
| --- | --- |
| associationType*   enum:string | The type of item to which it is associated. Possible values: `Budget`, `Contract`, `ScheduleOfValue`, `FormInstance`, `CostItem`, `Payment`, `MainContract`, `BudgetPayment`, `Expense`, `CostPayment`, `ExpenseItem`, `PaymentItem`, `OCO`, `RCO`, `SCO`, `PCO`, `RFQ`, `DistributionItem`, `BudgetTransfer`, `Fee` |
| propertyDefinitionId*   string: UUID | ID of the custom attribute definition. |
| value*   string,null,number,boolean | Value of the custom attribute associated to an item. |

* Required

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

| name   string | Name of the custom attribute. Inherited from the custom attribute definition. |
| --- | --- |
| builtIn   boolean | A flag to indicate whether this is a pre-defined attribute or not. Inherited from the custom attribute definition. |
| position   number | The order of the custom attribute displayed in the BIM 360 Cost Management. Inherited from the custom attribute definition. |
| propertyDefinitionId   string: UUID | The ID of the custom attribute definition. This is the ID from `/properties`. |
| type   string | The type of the custom attribute. Inherited from the custom attribute definition. |
| value   string | The value of the custom attribute. |

## [Example](#example)

The resource is updated successfully.

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/property-values:batch-update' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '[
        {
          "associationId": "EDC42DF6-277A-436A-A50D-EF57F35E1248",
          "associationType": "Budget",
          "propertyDefinitionId": "229d3420-9481-11e8-87fb-215990a8aeb3",
          "value": "2018-10-1"
        }
      ]'

```

Show More

### Response

```
[
  {
    "name": "Source Type",
    "builtIn": true,
    "position": 0,
    "propertyDefinitionId": "fc4a7581-7838-11e8-a467-7de33c3af32d",
    "type": "options",
    "value": "RFI"
  }
]

```

Show More
