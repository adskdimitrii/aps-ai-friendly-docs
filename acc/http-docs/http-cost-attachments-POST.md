# v1/containers/{containerId}/attachments

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-attachments-POST/

---

Attachments

POST

# v1/containers/{containerId}/attachments

Creates an attachment in a specific project.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/cost/v1/containers/:containerId/attachments |
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

### Request

## [Body Structure](#body-structure)

The `Attachment`

| id   string: UUID | The ID of the attachment |
| --- | --- |
| type   enum:string | The type of attachment. Possible values: <br>`Upload`: is a locally uploaded file.<br>`DocsFile` is a file referenced from BIM 360 Docs.<br>`Reference` is a file referenced form report.<br>`Document` is for document generation .<br>Max length: 64 |
| name*   string | The name of the attachment. <br>Max length: 255 |
| folderId   string: UUID | The folder ID retrieved from `attachment-folder`. |
| urn   string | The version URN from BIM 360 Docs after the attachment is uploaded. |
| templateId   string | The documentTemplate Id to generate an attachment |
| associationId*   string: UUID | The object ID of the item associated with the actions, such as a budget, contract, or cost item. |
| associationType*   enum:string | The type of item to which it is associated. Possible values: `Budget`, `Contract`, `ScheduleOfValue`, `FormInstance`, `CostItem`, `Payment`, `MainContract`, `BudgetPayment`, `Expense`, `CostPayment`, `ExpenseItem`, `PaymentItem`, `OCO`, `RCO`, `SCO`, `PCO`, `RFQ`, `DistributionItem`, `BudgetTransfer`, `Fee` |

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

| id   string: UUID | The unique auto-generated identifier of the attachment. |
| --- | --- |
| folderId   string: UUID | The unique identifier (UUID) of the folder named `attachment-folder` where the attachment is stored. This ID is automatically retrieved by the backend and returned in the response. |
| urn   string | The object version URN of the attachment in the Autodesk Data Management service. |
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
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/attachments' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "id": "F2D2ED17-C763-465B-8FAB-251C5A35D42F",
        "type": "Upload",
        "name": "Architecture",
        "folderId": "8E34872D-A56F-4096-B675-476F50F4EF51",
        "urn": "urn:adsk.wipqa:dm.lineage:dekqaSc4SRK7AJ9YLVLCeg",
        "templateId": "8E34872D-A56F-4096-B675-476F50F4EF51",
        "associationId": "EDC42DF6-277A-436A-A50D-EF57F35E1248",
        "associationType": "Budget"
      }'

```

Show More

### Response

```
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

```

Show More
