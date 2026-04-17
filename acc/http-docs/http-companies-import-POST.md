# companies/import

Source: https://aps.autodesk.com/en/docs/acc/reference/http/companies-import-POST/

---

Companies

POST

# companies/import

Bulk import partner companies to the company directory in a specific BIM 360 account. (50 companies maximum can be included in each call.)

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/hq/v1/accounts/:account_id/companies/import |
| --- | --- |
| Method and URI (Legacy) | POST https://developer.api.autodesk.com/hq/v1/regions/eu/accounts/:account_id/companies/import |
| Authentication Context | app only |
| Required OAuth Scopes | `account:write` |
| Data Formats | JSON |

### Request

## [Headers](#headers)

| Authorization   yes | Must be `Bearer <token>`, where `<token>` is obtained via a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type   yes | Must be `application/json`. |
| Region   no | Specifies the region where the service is located. Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |

### Request

## [URI Parameters](#uri-parameters)

| account_id   string: UUID | The account/hub ID of the company. This corresponds to the hub ID used in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/), with the “**b.**" prefix removed. For example, **b.**c8b0c73d-3ae9 becomes c8b0c73d-3ae9. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

The POST body is an array of flat JSON objects with the following attributes:

| name*   string | Company name should be unique under an account/hub       Max length: 255 |
| --- | --- |
| trade*   string | Trade type based on specialization       Refer to the `trade` list in the [Parameters](https://aps.autodesk.com/en/docs/bim360/v1/overview/parameters/) guide. |
| address_line_1   string | Company address line 1       Max length: 255 |
| address_line_2   string | Company address line 2       Max length: 255 |
| city   string | City in which company is located       Max length: 255 |
| state_or_province   enum: string | State or province in which company is located       Max length: 255       Note that the `state_or_province` value depends on the selected `country` value; see the valid values in the `state_or_province` list in the [Parameters](https://aps.autodesk.com/en/docs/bim360/v1/overview/parameters/) guide. |
| postal_code   string | Postal code for the company location       Max length: 255 |
| country   enum: string | Country for this company       Refer to the `country` list in the [Parameters](https://aps.autodesk.com/en/docs/bim360/v1/overview/parameters/) guide. |
| phone   string | Business phone number for the company       Max length: 255 |
| website_url   string | Company website       Max length: 255 |
| description   string | Short description or overview for company       Max length: 255 |
| erp_id   string | Used to associate a company in BIM 360 with the company data in an ERP system |
| tax_id   string | Used to associate a company in BIM 360 with the company data from public and industry sources |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | A new resource has been successfully created |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax |
| 403   Forbidden | Unauthorized |
| 404   Not Found | The resource cannot be found |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the resource |
| 422   Unprocessable Entity | The request was unable to be followed due to restrictions |
| 500   Internal Server Error | An unexpected error occurred on the server |

### Response

## [Body Structure (201)](#body-structure-201)

A successful response returns a JSON object envelope for the import task with the following attributes:

Expand all

| success   int | Import success company count |
| --- | --- |
| failure   int | Import failure company count |
| success_items   array:object | Array of [company objects](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/) that were successfully imported |
| id |  |
| account_id |  |
| name |  |
| trade |  |
| address_line_1 |  |
| address_line_2 |  |
| city |  |
| postal_code |  |
| state_or_province |  |
| country |  |
| phone |  |
| website_url |  |
| description |  |
| created_at |  |
| updated_at |  |
| erp_id |  |
| tax_id |  |
| failure_items   array:object | Array of [company objects](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/) that failed to import, along with content and error information |

## [Example](#example)

Successful Import of Two Companies (201)

### Request

```
curl -v 'https://developer.api.autodesk.com/hq/v1/accounts/80793a28-f9b1-4888-9533-5f00cddcd6fb/companies/import' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '[
    {
      "name":"Maybach",
      "trade": "mh-trade",
      "website_url": "http://www.autodesk.com",
      "city": "Shanghai",
      "country": "China",
      "address_line_1": "Pudian Road",
      "address_line_2": "Pudian Road",
      "postal_code": "200012",
      "erp_id":"cf87ce66-6cab-481c-97ae-079efce98ac2",
      "tax_id":"675-16-6587",
      "phone": "021-78665544",
      "description": "nothing here"
    },
    {
      "name":"Lincoln",
      "trade": "mh-trade",
      "website_url": "http://www.autodesk.com",
      "city": "Shanghai",
      "country": "China",
      "address_line_1": "Pudian Road",
      "address_line_2": "Pudian Road",
      "postal_code": "200012",
      "erp_id":"6e28dfb9-7f4e-4c33-a500-cf2c87e447c5",
      "tax_id":"508-65-7386",
      "phone": "021-77336644",
      "description": "nothing here"
    }
  ]'

```

Show More

### Response

```
{
  "success": 2,
  "failure": 0,
  "success_items": [
    {
      "id": "681587f9-4de4-461a-99ca-5649e848555b",
      "account_id": "80793a28-f9b1-4888-9533-5f00cddcd6fb",
      "name": "Maybach",
      "trade": "mh-trade",
      "address_line_1": "Pudian Road",
      "address_line_2": "Pudian Road",
      "city": "Shanghai",
      "postal_code": "200012",
      "state_or_province": null,
      "country": "China",
      "phone": "021-78665544",
      "website_url": "http://www.autodesk.com",
      "description": "nothing here",
      "created_at": "2016-05-20T06:55:16.190Z",
      "updated_at": "2016-05-20T06:55:16.190Z",
      "erp_id": "cf87ce66-6cab-481c-97ae-079efce98ac2",
      "tax_id": "675-16-6587"
    },
    {
      "id": "f54dc236-0b52-4a49-b502-69538441d257",
      "account_id": "80793a28-f9b1-4888-9533-5f00cddcd6fb",
      "name": "Lincoln",
      "trade": "mh-trade",
      "address_line_1": "Pudian Road",
      "address_line_2": "Pudian Road",
      "city": "Shanghai",
      "postal_code": "200012",
      "state_or_province": null,
      "country": "China",
      "phone": "021-77336644",
      "website_url": "http://www.autodesk.com",
      "description": "nothing here",
      "created_at": "2016-05-20T06:55:16.283Z",
      "updated_at": "2016-05-20T06:55:16.283Z",
      "erp_id": "6e28dfb9-7f4e-4c33-a500-cf2c87e447c5",
      "tax_id": "508-65-7386"
    }
  ],
  "failure_items": []
}

```

Show More
