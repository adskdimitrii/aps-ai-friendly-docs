# v1/containers/{containerId}/attachments

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-attachments-GET/

---

Attachments

GET

# v1/containers/{containerId}/attachments

Retrieves all of the attachments associated with an item such as a budget, contract, or cost item. You can also retrieve certain nested resources related to the returned attachments.

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/attachments |
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

| filter[associationId]   array: string: uuid | The ID of the associated item, for example, the ID of a budget, contract, change order or cost item. Separate multiple IDs with commas, for example, `filter[associationId]=id1,id2`. |
| --- | --- |
| filter[associationType]   string | The type of the associated item. Possible values `Budget`, `Contract`, `CostItem`, `FormInstance`, `CostPayment`, `BudgetPayment`, `Expense`, `ExpenseItem`. For example, `filter[associationType]=Budget`. |
| filter[lastModifiedSince]   string | Returns only items that were modified since the specified date and time, in ISO 8601 format. For example, `filter[lastModifiedSince]=2020-03-01T13:00:00Z`. |
| include   array: string | A list of the nested resources related to the attachment to include in the response. For example, `include=complianceRequirement` returns compliance documents related to each attachment. Possible values: `complianceRequirement`. |
| offset   int | The number of records to skip before returning results. Used together with `limit` to paginate through results, where `offset` specifies the starting point and `limit` specifies the number of records to return. |
| limit   int | The maximum number of records returned per page. Default: `100`. A page may contain fewer records than the limit if there are fewer matching items or if it is the last page of results. |
| sort   string | Defines the sort order for the results. Each attribute can be sorted in `asc` (default) or `desc` order. For example, `sort=name desc` sorts the results by name in descending order. |

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
| results   array: object | A list of result objects. |
| id   string: UUID | The unique auto-generated identifier of the attachment. |
| folderId   string: UUID | The unique identifier (UUID) of the folder named `attachment-folder` where the attachment is stored. This ID is automatically retrieved by the backend and returned in the response. |
| urn   string | The object version URN of the attachment in the Autodesk Forma Data Management service. |
| pdfOssUrn   string,null | Not relevant |
| pdfUrn   string,null | Not relevant |
| type   enum:string | The type of attachment. Possible values: <br>`Upload`: is a locally uploaded file.<br>`DocsFile` is a file referenced from BIM 360 Docs.<br>`Reference` is a file referenced form report.<br>`Document` is for document generation.<br>Max length: 64 |
| name   string | The name of the attachment. <br>Max length: 1024 |
| replaceIfExists   boolean | Determines whether an existing attachment with a matching name should be replaced. |
| status   string | The status of the attachment. <br>Max length: 1024 |
| associationId   string: UUID | The object ID of the item associated with the actions, such as a budget, contract, or cost item. |
| associationType   enum:string | The type of item to which it is associated. Possible values: `Budget`, `Contract`, `ScheduleOfValue`, `FormInstance`, `CostItem`, `Payment`, `MainContract`, `BudgetPayment`, `Expense`, `CostPayment`, `ExpenseItem`, `PaymentItem`, `OCO`, `RCO`, `SCO`, `PCO`, `RFQ`, `DistributionItem`, `BudgetTransfer`, `Fee` |
| createdAt   datetime: ISO 8601 | The date and time that the item was created, in ISO 8601 format. |
| updatedAt   datetime: ISO 8601 | The date and time that the item was last updated, in ISO 8601 format. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/attachments?filter[associationType]=Budget&filter[lastModifiedSince]=2020-03-01T13:00:00Z&limit=100&sort=name,createdAt desc' \
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
      "id": "F2D2ED17-C763-465B-8FAB-251C5A35D42F",
      "folderId": "8E34872D-A56F-4096-B675-476F50F4EF51",
      "urn": "urn:adsk.wipprod:fs.file:vf.PMbRnoPZR2mKDhau2uw4SQ?version=1",
      "pdfOssUrn": "urn:adsk.wipprod:fs.file:vf.PMbRnoPZR2mKDhau2uw4SQ?version=1",
      "pdfUrn": "urn:adsk.wipprod:fs.file:vf.PMbRnoPZR2mKDhau2uw4SQ?version=1",
      "type": "Upload",
      "name": "Architecture",
      "replaceIfExists": true,
      "status": "Pending",
      "associationId": "EDC42DF6-277A-436A-A50D-EF57F35E1248",
      "associationType": "Budget",
      "createdAt": "2019-01-06T01:24:22.678Z",
      "updatedAt": "2019-09-05T01:00:12.989Z"
    }
  ]
}

```

Show More
