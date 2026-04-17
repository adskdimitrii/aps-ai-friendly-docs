# companies

Source: https://aps.autodesk.com/en/docs/acc/reference/http/companies-GET-legacy/

---

Companies

GET

# companies

Query all the partner companies in a specific BIM 360 account.

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/hq/v1/accounts/:account_id/companies |
| --- | --- |
| Method and URI (Legacy) | GET https://developer.api.autodesk.com/hq/v1/regions/eu/accounts/:account_id/companies |
| Authentication Context | app only |
| Required OAuth Scopes | `account:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization   yes | Must be `Bearer <token>`, where `<token>` is obtained via a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) OAuth flow. |
| --- | --- |
| Region   no | Specifies the region where the service is located. Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |

### Request

## [URI Parameters](#uri-parameters)

| account_id   string: UUID | The account/hub ID of the company. This corresponds to the hub ID used in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/), with the “**b.**" prefix removed. For example, **b.**c8b0c73d-3ae9 becomes c8b0c73d-3ae9. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | Response array’s size   Default value: `10`   Max limit: `100` |
| --- | --- |
| offset   int | Offset of response array   Default value: `0` |
| sort   string | Comma-separated fields to sort by in ascending order       Prepending a field with `-` sorts in descending order   Invalid fields and whitespaces will be ignored |
| field   string | Comma-separated fields to include in response       `id` will always be returned   Invalid fields will be ignored |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The request has succeeded |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax |
| 403   Forbidden | Unauthorized |
| 404   Not Found | The resource cannot be found |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the resource |
| 422   Unprocessable Entity | The request was unable to be followed due to restrictions |
| 500   Internal Server Error | An unexpected error occurred on the server |

### Response

## [Body Structure (200)](#body-structure-200)

A successful response is an array of companies, flat JSON objects with the following attributes:

| id   string: UUID | Company ID |
| --- | --- |
| account_id   string: UUID | Account/Hub ID |
| name   string | Company name should be unique under a hub       Max length: 255 |
| trade   string | Trade type based on specialization       Refer to the `trade` list in the [Parameters](https://aps.autodesk.com/en/docs/bim360/v1/overview/parameters/) guide. |
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

## [Example](#example)

Successful Listing of Companies in an Account/Hub (200)

### Request

```
curl -v 'https://developer.api.autodesk.com/hq/v1/accounts/80793a28-f9b1-4888-9533-5f00cddcd6fb/companies?limit=1&offset=0' \
  -H 'Authorization: Bearer 07YyCEjv3qs8FA7ysntmsuErYXHv'

```

### Response

```
[
  {
    "id": "fc830fd8-f1ef-4cd6-9163-fb115dc698d7",
    "account_id": "80793a28-f9b1-4888-9533-5f00cddcd6fb",
    "name": "Autodesk",
    "trade": "Concrete",
    "address_line_1": "The Fifth Avenue",
    "address_line_2": "#301",
    "city": "New York",
    "postal_code": "10011",
    "state_or_province": "New York",
    "country": "United States",
    "phone": "(503)623-1525",
    "website_url": "http://www.autodesk.com",
    "description": "Autodesk, Inc., is a leader in 3D design, engineering and entertainment software.",
    "created_at": "2016-05-20T02:24:21.400Z",
    "updated_at": "2016-05-20T02:24:21.400Z",
    "erp_id": "c79bf096-5a3e-41a4-aaf8-a771ed329047",
    "tax_id": "213-73-8867"
  }
]

```

Show More
