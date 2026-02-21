# v1/containers/{containerId}/taxes

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-taxes-GET/

---

Tax

GET

# v1/containers/{containerId}/taxes

Retrieves a list of tax formulas associated with specific cost objects in the given project.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/taxes |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

- Authorization*string Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow.
- regionstring Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.Possible values: country or region codes such as `US` or `EMEA`. For the full list of supported regions, see the [ACC Regions](/en/docs/acc/v1/overview/acc-regions) page.To verify your projectâs region, refer to the *Working with BIM 360 Services in Different Regions* section on the [API Basics](/en/docs/bim360/v1/overview/basics/#bim-360-account-admin) page.

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see [GET projects](/en/docs/bim360/v1/reference/http/admin-accounts-accountidprojects-GET/). |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| offset   int | The number of records to skip before returning results. Used together with `limit` to paginate through results, where `offset` specifies the starting point and `limit` specifies the number of records to return. |
| --- | --- |
| limit   int | The maximum number of records returned per page. Default: `100`. A page may contain fewer records than the limit if there are fewer matching items or if it is the last page of results. |
| sort   string | Defines the sort order for the results. Each attribute can be sorted in `asc` (default) or `desc` order. For example, `sort=name desc` sorts the results by name in descending order. |
| associationId*   array: string | The object ID of the item is associated to. For example, ID of the budget, contract or cost item. Use comma separated string for multiple IDs. |
| associationType*   enum:string | Specifies the category of the object the tax is associated with. Possible values: - `Contract` - `MainContract` - `BudgetPayment` - `CostPayment` - `OCO` (Owner Change Order) - `SCO` (Subcontractor Change Order) - `PCO` (Potential Change Order) - `RFQ` (Request for Quote) - `RCO` (Request for Change Order) |

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

| pagination   object | Contains pagination information when data is returned page by page. |
| --- | --- |
| limit   int | The maximum number of records returned in the response. |
| offset   int | The number of records skipped before returning the page of results. |
| totalResults   int | The total number of records that matched the request criteria. |
| nextUrl   string | The URL for the next request to retrieve the next page of results. Max length: 2000. <br>Max length: 2000 |
| results   array: object |  |
| id   string: UUID | The unique identifier of the tax. |
| containerId   string: UUID | Not relevant |
| name   string | The name of the tax. <br>Max length: 1024 |
| taxFormulaId   string: UUID | Not relevant |
| associationId   string: UUID | The unique identifier (UUID) of the object the tax is associated with. |
| associationType   string | The type of object the tax is associated with. |
| needUpdate   boolean | Indicates whether the tax needs to be recalculated because the associated item was updated after the tax was applied. |
| options   object | Not relevant |
| summary   array: object | A consolidated report of all taxes applied within a specific project. |
| name   string | The name of the applied tax (e.g., Sales Tax, VAT, State Tax, City Tax, Local Tax). |
| amount   number | The total amount of the applied tax. |
| type   string | The type of tax applied, such as `rate`. |
| rate   string | (optional) The rate of the tax applied. |
| createdAt   datetime: ISO 8601 | The date and time that the item was created, in ISO 8601 format. |
| updatedAt   datetime: ISO 8601 | The date and time that the item was last updated, in ISO 8601 format. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/taxes?limit=100&sort=name,createdAt desc&associationId=18d97ae0-9484-11e8-a7ec-7ddae203e404&associationType=Contract' \
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
      "id": "769305a0-96d4-11e8-b53f-f98b28ca3295",
      "containerId": "1df59db0-9484-11e8-a7ec-7ddae203e404",
      "name": "Sales Tax",
      "taxFormulaId": "18d97ae0-9484-11e8-a7ec-7ddae203e404",
      "associationId": "18d97ae0-9484-11e8-a7ec-7ddae203e404",
      "associationType": "Contract",
      "needUpdate": true,
      "options": {
        "isTaxBeforeRetention": true
      },
      "summary": [
        {
          "name": "State Tax",
          "amount": 300,
          "type": "rate",
          "rate": "0.10"
        }
      ],
      "createdAt": "2019-01-06T01:24:22.678Z",
      "updatedAt": "2019-09-05T01:00:12.989Z"
    }
  ]
}

```

Show More
