# companies

Source: https://aps.autodesk.com/en/docs/acc/reference/http/companies-POST/

---

Companies

POST

# companies

Create a new partner company.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/hq/v1/accounts/:account_id/companies |
| --- | --- |
| Method and URI (Legacy) | POST https://developer.api.autodesk.com/hq/v1/regions/eu/accounts/:account_id/companies |
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

| account_id   string: UUID | The account ID of the company. This corresponds to hub ID in the [Data Management API](/en/docs/data/v2/). To convert a hub ID into an account ID you need to remove the â**b.**" prefix. For example, a hub ID of **b.**c8b0c73d-3ae9 translates to an account ID of c8b0c73d-3ae9. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

The POST body is a flat JSON object with the following attributes:

| name*   string | Company name should be unique under an account       Max length: 255 |
| --- | --- |
| trade*   string | Trade type based on specialization       Refer to the `trade` list in the [Parameters](/en/docs/bim360/v1/overview/parameters) guide. |
| address_line_1   string | Company address line 1       Max length: 255 |
| address_line_2   string | Company address line 2       Max length: 255 |
| city   string | City in which company is located       Max length: 255 |
| state_or_province   enum: string | State or province in which company is located       Max length: 255       Note that the `state_or_province` value depends on the selected `country` value; see the valid values in the `state_or_province` list in the [Parameters](/en/docs/bim360/v1/overview/parameters) guide. |
| postal_code   string | Postal code for the company location       Max length: 255 |
| country   enum: string | Country for this company       Refer to the `country` list in the [Parameters](/en/docs/bim360/v1/overview/parameters) guide. |
| phone   string | Business phone number for the company       Max length: 255 |
| website_url   string | Company website       Max length: 255 |
| description   string | Short description or overview for company       Max length: 255 |
| erp_id   string | Used to associate a company in BIM 360 with the company data in an ERP system |
| tax_id   string | Used to associate a company in BIM 360 with the company data from public and industry sources |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | A new resource has been successfully created. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax. |
| 403   Forbidden | Unauthorized |
| 404   Not Found | The resource cannot be found. |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the resource. |
| 422   Unprocessable Entity | The request was unable to be followed due to restrictions. |
| 500   Internal Server Error | An unexpected error occurred on the server. |

### Response

## [Body Structure (201)](#body-structure-201)

A successful response is the created company, a flat JSON object with the following attributes:

| id   string: UUID | Company ID |
| --- | --- |
| account_id   string: UUID | Account ID |
| name   string | Company name should be unique under an account       Max length: 255 |
| trade   string | Trade type based on specialization       Refer to the `trade` list in the [Parameters](/en/docs/bim360/v1/overview/parameters) guide. |
| address_line_1   string | Company address line 1       Max length: 255 |
| address_line_2   string | Company address line 2       Max length: 255 |
| city   string | City in which company is located       Max length: 255 |
| state_or_province   enum: string | State or province in which company is located       Max length: 255       Note that the `state_or_province` value depends on the selected `country` value; see the valid values in the `state_or_province` list in the [Parameters](/en/docs/bim360/v1/overview/parameters) guide. |
| postal_code   string | Postal code for the company location       Max length: 255 |
| country   enum: string | Country for this company       Refer to the `country` list in the [Parameters](/en/docs/bim360/v1/overview/parameters) guide. |
| phone   string | Business phone number for the company       Max length: 255 |
| website_url   string | Company website       Max length: 255 |
| description   string | Short description or overview for company       Max length: 255 |
| erp_id   string | Used to associate a company in BIM 360 with the company data in an ERP system |
| tax_id   string | Used to associate a company in BIM 360 with the company data from public and industry sources |

## [Example](#example)

Successful Company Creation (201)

### Request

```
curl -v 'https://developer.api.autodesk.com/hq/v1/accounts/80793a28-f9b1-4888-9533-5f00cddcd6fb/companies' \
-X 'POST' \
-H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
-H 'Content-Type: application/json' \
-d '{
  "name": "Jaguars",
  "trade": "Concrete",
  "address_line_1": "The Fifth Avenue",
  "address_line_2": "#303",
  "city": "New York",
  "postal_code": "10011",
  "state_or_province": "New York",
  "country": "United States",
  "phone": "(634)329-2353",
  "website_url": "http://www.autodesk.com",
  "description":"Jaguars is the world\"s largest aerospace company.",
  "erp_id":"c79bf096-5a3e-41a4-aaf8-a771ed329047",
  "tax_id":"413-07-5767"
}'

```

Show More

### Response

```
{
  "id":"d36fbce5-01bc-418b-80b9-71d552fec792",
  "account_id":"80793a28-f9b1-4888-9533-5f00cddcd6fb",
  "name":"Jaguars",
  "trade":"Concrete",
  "address_line_1":"The Fifth Avenue",
  "address_line_2":"#303",
  "city":"New York",
  "postal_code":"10011",
  "state_or_province":"New York",
  "country":"United States",
  "phone":"(634)329-2353",
  "website_url":"http://www.autodesk.com",
  "description":"Jaguars is the world\"s largest aerospace company.",
  "created_at":"2016-05-20T07:16:36.633Z",
  "updated_at":"2016-05-20T07:16:36.633Z",
  "erp_id":"c79bf096-5a3e-41a4-aaf8-a771ed329047",
  "tax_id":"413-07-5767"
}

```

Show More
