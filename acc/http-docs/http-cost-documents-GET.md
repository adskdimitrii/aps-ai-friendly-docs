# v1/containers/{containerId}/documents

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-documents-GET/

---

Documents

GET

# v1/containers/{containerId}/documents

Gets generated documents.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/cost/v1/containers/:containerId/documents |
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

| associationId*   array: string | The object ID of the item is associated to. For example, ID of the budget, contract or cost item. Use comma separated string for multiple IDs. |
| --- | --- |
| associationType*   enum:string | The type of the item is associated to. Possible values `Budget`, `Contract`, `CostItem`, `FormInstance`, `Payment`, `BudgetPayment`, `Expense`, `OCO`, `SCO`. |
| filter[latest]   boolean | Filter to get only the latest version of a document if it has been generated multiple times. For example, filter[latest]=true. This is deprecated as weâll always response the latest document. |
| filter[signed]   boolean | Filter to get only documents that have been signed. For example, filter[signed]=true. This is deprecated. |

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

| id   string: UUID | Unique auto-generated identifier of the generated document. |
| --- | --- |
| recipientId   string | Autodesk ID of the recipient, who is a project user inside BIM 360 Admin. |
| signedBy   string | Not relevant |
| urn   string | The version URN of the document with docx format in the Autodesk Data Management service. |
| pdfUrn   string | Not relevant |
| status   enum:string | Current status of the document. Possible values: `Pending`, `Started`, `Completed`, `Failed`, `PendingSign`, `Signed`. |
| jobId   number | Not relevant |
| errorInfo   object | Error information if this document failed to be generated from the template. |
| code   string | Error code for this document. |
| message   string | Error message to describe this error. |
| detail   string | Provides detailed information about the error. |
| associationId   string: UUID | The object ID of the item associated with the actions, such as a budget, contract, or cost item. |
| associationType   enum:string | The type of item to which it is associated. Possible values: `Budget`, `Contract`, `ScheduleOfValue`, `FormInstance`, `CostItem`, `Payment`, `MainContract`, `BudgetPayment`, `Expense`, `CostPayment`, `ExpenseItem`, `PaymentItem`, `OCO`, `RCO`, `SCO`, `PCO`, `RFQ`, `DistributionItem`, `BudgetTransfer`, `Fee` |
| createdAt   datetime: ISO 8601 | The date and time that the item was created, in ISO 8601 format. |
| updatedAt   datetime: ISO 8601 | The date and time that the item was last updated, in ISO 8601 format. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/documents?associationId=18d97ae0-9484-11e8-a7ec-7ddae203e404&associationType=Budget&filter[latest]=true&filter[signed]=true' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
[
  {
    "id": "1df59db0-9484-11e8-a7ec-7ddae203e404",
    "recipientId": "GF8XKPKWM38E",
    "signedBy": "CED9LVTLHNXV",
    "urn": "urn:adsk.wipprod:fs.file:vf.PMbRnoPZR2mKDhau2uw4SQ?version=1",
    "pdfUrn": "urn:adsk.wipprod:fs.file:vf.PMbRnoPZR2mKDhau2uw4SQ?version=1",
    "status": "Completed",
    "jobId": 1,
    "errorInfo": {
      "code": "missingTemplate",
      "message": "Couldn't generate the document because the template is invalid.",
      "detail": "Got timeout for POST upload URL."
    },
    "associationId": "EDC42DF6-277A-436A-A50D-EF57F35E1248",
    "associationType": "Budget",
    "createdAt": "2019-01-06T01:24:22.678Z",
    "updatedAt": "2019-09-05T01:00:12.989Z"
  }
]

```

Show More
