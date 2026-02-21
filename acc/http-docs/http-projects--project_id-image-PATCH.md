# projects/:project_id/image

Source: https://aps.autodesk.com/en/docs/acc/reference/http/projects-:project_id-image-PATCH/

---

Projects

PATCH

# projects/:project_id/image

Create or update a projectâs image.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/hq/v1/accounts/:account_id/projects/:project_id/image |
| --- | --- |
| Method and URIï¼Legacyï¼ | PATCH https://developer.api.autodesk.com/hq/v1/regions/eu/accounts/:account_id/projects/:project_id/image |
| Authentication Context | app only |
| Required OAuth Scopes | `account:write` |
| Data Formats | JSON |

### Request

## [Headers](#headers)

| Authorization   yes | Must be `Bearer <token>`, where `<token>` is obtained via a [two-legged](/en/docs/oauth/v2/tutorials/get-2-legged-token) OAuth flow. |
| --- | --- |
| Content-Type   yes | Must be `application/json`. |
| Region   no | Specifies the region where the service is located. Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](/en/docs/acc/v1/overview/acc-regions) page. |

### Request

## [URI Parameters](#uri-parameters)

| account_id   string: UUID | The account ID of the project. This corresponds to hub ID in the [Data Management API](/en/docs/data/v2/). To convert a hub ID into an account ID you need to remove the â**b.**" prefix. For example, a hub ID of **b.**c8b0c73d-3ae9 translates to an account ID of c8b0c73d-3ae9. |
| --- | --- |
| project_id   string: UUID | The ID of the project. This corresponds to project ID in the [Data Management API](/en/docs/data/v2/). To convert a project ID in the Data Management API into a project ID in the BIM 360 API you need to remove the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |

### Request

## [Body Structure](#body-structure)

The file to be uploaded as HTTP multipart (chunk) data. Supported MIME types are `image/png`, `image/jpeg`, `image/jpg`, `image/bmp`, and `image/gif`.

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The request has succeeded. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax. |
| 403   Forbidden | Unauthorized |
| 404   Not Found | The resource cannot be found. |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the resource. |
| 422   Unprocessable Entity | The request was unable to be followed due to restrictions. |
| 500   Internal Server Error | An unexpected error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

A successful response is the updated project, a flat JSON object with the following attributes:

| id   string: UUID | Project ID |
| --- | --- |
| account_id   string: UUID | Account ID |
| name   string | Name of the project   Max length: 255 |
| start_date   date | The starting date of a project; must be earlier than `end_date`       Format: `YYYY-MM-DD` |
| end_date   date | The ending date of a project; must be later than `start_date`       Format: `YYYY-MM-DD` |
| project_type   string | The type of project; accepts preconfigured and customized project types       Max length: 255       Refer to the preconfigured `project_type` list in   the [Parameters](/en/docs/bim360/v1/overview/parameters) guide. |
| value   float | Monetary value of the project |
| currency   enum: string | Currency for project value       Refer to the `currency` list in the [Parameters](/en/docs/bim360/v1/overview/parameters) guide. |
| status   enum: string | The status of project.       Possible values:   `active`: project is active with at least one project admin added   `pending`: project has been created but pending becuase no project admin added   `inactive`: project is suspended   `archived`: project is archived and displayed only in the archived list |
| job_number   string | Project job number to connect a BIM 360 project to project or job in a financial or ERP system.       Max length: 100 |
| address_line_1   string | Project address line 1       Max length: 255 |
| address_line_2   string | Project address line 2       Max length: 255 |
| city   string | City in which project is located       Max length: 255 |
| state_or_province   enum: string | State or province in which project is located       Max length: 255       Note that the `state_or_province` value depends on the selected `country` value; see the valid values in the `state_or_province` list in the [Parameters](/en/docs/bim360/v1/overview/parameters) guide. |
| postal_code   string | Postal code for the project location       Max length: 255 |
| country   enum: string | Country for this project       Refer to the `country` list in the [Parameters](/en/docs/bim360/v1/overview/parameters) guide. |
| business_unit_id   string: UUID | The business unit ID of this project |
| timezone   string | Time zone for this project       Refer to the `timezone` list in the [Parameters](/en/docs/bim360/v1/overview/parameters) guide. |
| language   enum: string | Language of the project; applicable to the BIM 360 Field service only       Possible values:   `en`: English   `de`: German |
| construction_type   enum: string | Type of construction       Refer to the `construction_type` list in the [Parameters](/en/docs/bim360/v1/overview/parameters) guide. |
| contract_type   enum: string | Contract Type for your project       Refer to the `contract_type` list in the [Parameters](/en/docs/bim360/v1/overview/parameters) guide. |
| last_sign_in   datetime: ISO 8601 | Timestamp of the last sign in, `YYYY-MM-DDThh:mm:ss.sssZ` format |

## [Example](#example)

Successful Update of Project Image (200)

### Request

```
curl -v 'https://developer.api.autodesk.com/hq/v1/accounts/e3d5ef8d-5c37-4b9d-925d-1e6d24753ace/projects/aca11a7a-bd17-47cd-ab99-6548d0e6fe25/image' \
  -X 'PATCH' \
  -H 'Authorization: Bearer 9ezBnx9Rd5D1xG4KMt6b72T4w0MG' \
  -H 'Content-Type: multipart/form-data' \
  -F 'chunk=@/photo.png; type=image/png'

```

### Response

```
{
  "id": "aca11a7a-bd17-47cd-ab99-6548d0e6fe25",
  "account_id": "e3d5ef8d-5c37-4b9d-925d-1e6d24753ace",
  "name": "construction_project",
  "start_date": "2015-05-02",
  "end_date": "2016-04-03",
  "project_type": "office",
  "value": 3000.0,
  "currency": "USD",
  "status": "pending",
  "job_number": "0219-01",
  "address_line_1": "The Fifth Avenue",
  "address_line_2": "#301",
  "city": "New York",
  "state_or_province": "New York",
  "postal_code": "10011",
  "country": "United States",
  "business_unit_id": "c17e6837-96cd-4839-868e-051a2ad65d28",
  "timezone": "America/New_York",
  "language": "en",
  "construction_type": "Renovation",
  "contract_type": "Design-Bid",
  "last_sign_in": null,
  "created_at": "2016-04-05T07:26:20.858Z",
  "updated_at": "2016-04-05T07:31:26.290Z"
}

```

Show More
