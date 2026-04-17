# v1/containers/{containerId}/attachment-folders

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-attachment-folders-POST/

---

Attachments

POST

# v1/containers/{containerId}/attachment-folders

Find or create an attachment folder in BIM 360 Docs for a given item. That folder will save local files as attachments to the item. Files are saved using the Storage service.

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/cost/v1/containers/:containerId/attachment-folders |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). <br>The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| region   string | Specifies the region where the project data resides. <br>By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.<br>Possible values: country or region codes such as `US` or `EMEA`. For the full list of supported regions, see the [Forma Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page.<br>To verify your project’s region, refer to the *Working with BIM 360 Services in Different Regions* section on the [API Basics](https://aps.autodesk.com/en/docs/bim360/v1/overview/basics/#bim-360-account-admin) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see [GET projects](http-admin-accounts-accountidprojects-GET.md). |
| --- | --- |

### Request

## [Body Structure](#body-structure)

The associated item of the folder.

| associationId*   string: UUID | The object ID of the item is associated to. For example, ID of the budget, contract or cost item. |
| --- | --- |
| associationType*   string | The type of the item with which the attachment is associated. Possible values: `Budget`, `Contract`, `FormInstance`, `CostItem`, `Payment`, `MainContract`, `BudgetPayment`. |

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

| id   string: UUID | System identifier of the folder. |
| --- | --- |
| creatorId   string | The user who created the folder. This is the ID of a user managed by BIM 360 Admin. |
| scope   string | Scope of the folder’s use. For example, Attachment, Template, and so on. |
| urn   string | Object URN of the folder in the Autodesk Forma Data Management service. |
| createdAt   datetime: ISO 8601 | The date and time that the item was created, in ISO 8601 format. |
| updatedAt   datetime: ISO 8601 | The date and time that the item was last updated, in ISO 8601 format. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/attachment-folders' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "associationId": "269F7D1E-2343-48E8-9B8E-45C45C976DC6",
        "associationType": "Budget"
      }'

```

Show More

### Response

```
{
  "id": "3A7432BB-8CA5-444A-B327-EE010E1D89DF",
  "creatorId": "CED9LVTLHNXV",
  "scope": "Contract-00000000-0000-0000-0000-000000000000",
  "urn": "urn:adsk.wipprod:fs.file:vf.PMbRnoPZR2mKDhau2uw4SQ?version=1",
  "createdAt": "2019-01-06T01:24:22.678Z",
  "updatedAt": "2019-09-05T01:00:12.989Z"
}

```

Show More
