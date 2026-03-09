# v1/containers/{containerId}/performance-tracking-item-instances

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-performance-tracking-item-instances-POST/

---

Performance Tracking Item Instance

POST

# v1/containers/{containerId}/performance-tracking-item-instances

Creates a performance tracking item instance based on the specified tracking item in the given project. You can create multiple instances to track the performance of the underlying budget at each of its associated locations. For more information about performance tracking, see the [Cost Management API Field Guide](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/cost-management/).

Note that a default tracking item instance is automatically generated when a tracking item is created, so use this endpoint only to create additional tracking item instances.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/cost/v1/containers/:containerId/performance-tracking-item-instances |
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

### Request

## [Body Structure](#body-structure)

The tracking item instance

| number   string | The user-provided or system generated code representing the tracking item instance. |
| --- | --- |
| name   string | The user-provided name of the tracking item instance. |
| budgetId*   string: UUID | The unique identifier of the budget to which the performance tracking item instance belongs. |
| inputUnit   string | The input unit of measurement of the tracking item instance. This value should always be `hr`. |
| inputQuantity*   number | The input quantity of the tracking item instance. You can multiply this by the value of `inputUnitPrice` to determine the planned total for this instance. |
| inputUnitPrice*   number,string,null | The input unit price of the tracking item instance. You can multiply this by the value of `inputQuantity` to determine the planned total for this instance. |
| outputUnit   string | The output unit of measurement of the tracking item instance. |
| outputQuantity*   number | The output quantity of the tracking item instance. You can multiply this by the value of `outputUnitPrice` to determine the planned total for this instance. |
| outputUnitPrice*   number,string,null | The output unit price of the tracking item instance. You can multiply this by the value of `outputQuantity` to determine the planned total for this instance. |
| trackedInputQuantity   number,null | The reported hours worked so far on the tracking item instance. |
| trackedOutputQuantity   number,null | The reported quantity of material used so far on the tracking item instance |
| adjustedOutputQuantity   number,null | The overriding output quantity that you specified to reflect a change (if any) in the scope of the tracking item instance. This value will be used instead of the value of `outputQuantity` in future performance tracking and forecasting for this tracking item instance. |
| locations   array,null | A list of the IDs of the project locations where this item applies. <br>For more information, see the Locations [Help documentation](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/locations-nodes-GET/) help. |

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

| id   string: UUID | The ID of the tracking item instance. |
| --- | --- |
| containerId   string: UUID | The ID of the cost container for the project that contains the tracking item instance. |
| number   string | The user-provided or system generated code representing the tracking item instance. |
| name   string | The user-provided name of the tracking item instance. |
| budgetId   string: UUID | The unique identifier of the budget to which the performance tracking item instance belongs. |
| budgetCode   string | The code of the budget to which the tracking item instance belongs. |
| inputUnit   string | The input unit of measurement of the tracking item instance. This value should always be `hr`. |
| inputQuantity   number | The input quantity of the tracking item instance. You can multiply this by the value of `inputUnitPrice` to determine the planned total for this instance. |
| inputUnitPrice   number,string,null | The input unit price of the tracking item instance. You can multiply this by the value of `inputQuantity` to determine the planned total for this instance. |
| outputUnit   string | The output unit of measurement of the tracking item instance. |
| outputQuantity   number | The output quantity of the tracking item instance. You can multiply this by the value of `outputUnitPrice` to determine the planned total for this instance. |
| outputUnitPrice   number,string,null | The output unit price of the tracking item instance. You can multiply this by the value of `outputQuantity` to determine the planned total for this instance. |
| trackedInputQuantity   number,null | The reported hours worked so far on the tracking item instance. |
| trackedOutputQuantity   number,null | The reported quantity of material used so far on the tracking item instance |
| adjustedOutputQuantity   number,null | The overriding output quantity that you specified to reflect a change (if any) in the scope of the tracking item instance. This value will be used instead of the value of `outputQuantity` in future performance tracking and forecasting for this tracking item instance. |
| performanceRatio   number,null | The tracking item instanceâs planned productivity rate (`inputQuantity`/`outputQuantity`) divided by its tracked productivity rate (`trackedInputQuantity`/`trackedOutputQuantity`). |
| creatorId   string,null | The BIM 360/ACC ID of the user who created the tracking item instance. |
| changedBy   string,null | The BIM 360/ACC ID of the user who made the last change to the tracking item instance. |
| locations   array,null | A list of the IDs of the project locations where this item applies. <br>For more information, see the Locations [Help documentation](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/locations-nodes-GET/) help. |
| locationPaths   array,null | A list of the IDs of the project locations where this item applies, along with the node paths of these locations in the projectâs locations tree. <br>For more information, see the Locations [Help documentation](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/locations-nodes-GET/) help. |
| createdAt   datetime: ISO 8601 | The date and time that the item was created, in ISO 8601 format. |
| updatedAt   datetime: ISO 8601 | The date and time that the item was last updated, in ISO 8601 format. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/performance-tracking-item-instances' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "number": "84720010121001FEE-01",
        "name": "Concrete",
        "budgetId": "1df59db0-9484-11e8-a7ec-7ddae203e404",
        "inputUnit": "hr",
        "inputQuantity": "100",
        "inputUnitPrice": "1000.0000",
        "outputUnit": "cy",
        "outputQuantity": "100",
        "outputUnitPrice": "1000.0000",
        "trackedInputQuantity": "100",
        "trackedOutputQuantity": "100",
        "adjustedOutputQuantity": "100",
        "locations": [
          "683904a0-47ce-4146-ac2d-a3840f00e0f4"
        ]
      }'

```

Show More

### Response

```
{
  "id": "1df59db0-9484-11e8-a7ec-7ddae203e404",
  "containerId": "1df59db0-9484-11e8-a7ec-7ddae203e404",
  "number": "84720010121001FEE-01",
  "name": "Concrete",
  "budgetId": "1df59db0-9484-11e8-a7ec-7ddae203e404",
  "budgetCode": "84720010121001FEE",
  "inputUnit": "hr",
  "inputQuantity": "100",
  "inputUnitPrice": "1000.0000",
  "outputUnit": "cy",
  "outputQuantity": "100",
  "outputUnitPrice": "1000.0000",
  "trackedInputQuantity": "100",
  "trackedOutputQuantity": "100",
  "adjustedOutputQuantity": "100",
  "performanceRatio": "1.00",
  "creatorId": "CED9LVTLHNXV",
  "changedBy": "CED9LVTLHNXV",
  "locations": [
    "683904a0-47ce-4146-ac2d-a3840f00e0f4"
  ],
  "locationPaths": [
    "683904a0-47ce-4146-ac2d-a3840f00e0f4"
  ],
  "createdAt": "2019-01-06T01:24:22.678Z",
  "updatedAt": "2019-09-05T01:00:12.989Z"
}

```

Show More
