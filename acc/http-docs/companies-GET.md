# accounts/{accountId}/companies

Source: https://aps.autodesk.com/en/docs/acc/reference/http/companies-GET/

---

accounts/:accountId/companies

GET

# accounts/{accountId}/companies

Returns a list of companies in an account.

You can also use this endpoint to filter out the list of companies by setting the filter parameters.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/admin/v1/accounts/:accountId/companies |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `account:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](/en/docs/oauth/v2/tutorials/get-2-legged-token) or [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| Region   string | Specifies the region where your request should be routed. If not set, the request is routed automatically, which may result in a slight increase in latency. <br>Possible values: `US`, `EMEA`. For a complete list of supported regions, see the [Regions](/en/docs/acc/v1/overview/acc-regions/) page. |
| User-Id   string | The ID of a user on whose behalf your request is acting. <br>Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.<br>You can use either the userâs ACC ID (`id`), or their Autodesk ID (`autodeskId`).<br>Note that this header is required for Account Admin POST, PATCH, and DELETE endpoints if you want to use a 2-legged authentication context. This header is optional for Account Admin GET endpoints. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| accountId   string: UUID | The ID of the ACC account that contains the project being created or the projects being retrieved. This corresponds to the hub ID in the [Data Management API](/en/docs/data/v2/). To convert a hub ID into an account ID, remove the â**b.**" prefix. For example, a hub ID of `b.c8b0c73d-3ae9` translates to an account ID of `c8b0c73d-3ae9`. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| filter[name]   string | Filter companies by name. Can be a partial match based on the value of filterTextMatch provided. <br>Max length: 255 |
| --- | --- |
| filter[trade]   string | Filter companies by trade. Can be a partial match based on the value of filterTextMatch provided. <br>Max length: 255 |
| filter[erpId]   string | Filter companies by ERP Id. Can be a partial match based on the value of filterTextMatch provided. <br>Max length: 255 |
| filter[taxId]   string | Filter companies by tax Id. Can be a partial match based on the value of filterTextMatch provided. <br>Max length: 255 |
| filter[updatedAt]   string | Filter companies by updated at date range. The range must be specified with dates in an ISO-8601 format with time required. The start and end dates of the range should be separated by .. One of the dates in the range may be omitted. For example, to get everything on or before June 1, 2019 the range would be ..2019-06-01T23:59:59.999Z. To get everything after June 1, 2019 the range would be 2019-06-01T00:00:00.000Z... <br>Max length: 100 |
| orFilters   array: string | List of filtered fields to apply an âorâ operator. Valid list of fields are erpId, name, taxId, trade, updatedAt. |
| filterTextMatch   enum:string | Specifies how text-based filters should match values in supported fields. <br>This parameter can be used in any endpoint that supports text-based filtering (e.g., `filter[name]`, `filter[jobNumber]`, `filter[companyName]`, etc.).<br>Possible values:<br>`contains` (default) â Matches if the field contains the specified text anywhere<br>`startsWith` â Matches if the field starts with the specified text<br>`endsWith` â Matches if the field ends with the specified text<br>`equals` â Matches only if the field exactly matches the specified text<br>Matching is case-insensitive.<br>Wildcards and regular expressions are not supported. |
| sort   array: string | The list of fields to sort by. When multiple fields are listed the later property is used to sort the resources where the previous fields have the same value. Each property can be followed by a direction modifier of either asc (ascending) or desc (descending). If no direction is specified then asc is assumed. Valid fields for sorting are name, trade, erpId, taxId, status, createdAt, updatedAt, projectSize and userSize. Default sort is name. |
| fields   array: string | List of fields to return in the response. Defaults to all fields. Valid list of fields are accountId, name, trade, addresses, websiteUrl, description, erpId, taxId, imageUrl, status, createdAt, updatedAt, projectSize, userSize and originalName. |
| limit   int | The maximum number of records to return in the response. <br>Default: `20`<br>Minimum: `1`<br>Maximum: `200` (If a larger value is provided, only 200 records are returned) |
| offset   int | The index of the first record to return. <br>Used for pagination in combination with the `limit` parameter.<br>Example: `limit=20` and `offset=40` returns records 41â60. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The list of requested companies. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax. |
| 401   Unauthorized | Request has not been applied because it lacks valid authentication credentials for the target resource. |
| 403   Forbidden | The server understood the request but refuses to authorize it. |
| 404   Not Found | The resource could not be found. |
| 406   Not Acceptable | The server cannot produce a response matching the list of acceptable values defined in the request. |
| 410 | Access to the target resource is no longer available. |
| 429   Too Many Requests | User has sent too many requests in a given amount of time. |
| 500   Internal Server Error | An unexpected error occurred on the server. |
| 503   Service Unavailable | Server is not ready to handle the request. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| pagination   object | Contains pagination details for the records returned by the endpoint. |
| --- | --- |
| limit   int | The maximum number of records returned per page. The last page may contain fewer records than the specified limit. |
| offset   int | The index of the first record in the returned page. Used for pagination. |
| totalResults   int | The total number of records matching the request. |
| nextUrl   string | The URL for the next page of records, if more results are available. Max length: 2000 characters. <br>Max length: 2000 |
| previousUrl   string | The URL for the previous page of records, if applicable. Max length: 2000 characters. <br>Max length: 2000 |
| results   array: object | The requested page of companies. |
| id   string: UUID | Id of the company. |
| accountId   string: UUID | The identifier of the account this company is associated with. |
| name   string | The name of the company. The company name should be unique under an account. <br>Max length: 255 |
| trade   string | Trade or company type based on specialization. <br>Max length: 255 |
| addresses   array: object | The company addresses. |
| type   enum:string | The address type. Will always be: `Main` |
| addressLine1   string | The street address line 1. <br>Max length: 255 |
| addressLine2   string | The street address line 2. <br>Max length: 255 |
| city   string | City. <br>Max length: 255 |
| stateOrProvince   null,string | The state or province location. Only valid state/province names and ISO 3166-1 alpha-2 codes will be accepted. The provided state or province must exist in the provided country. <br>Max length: 255 |
| postalCode   string | The zip or postal code in which this address is located. <br>Max length: 255 |
| country   null,string | Only valid country names and ISO 3166-1 alpha-2 codes will be accepted. <br>Max length: 255 |
| phone   string | Phone Number. <br>Max length: 255 |
| websiteUrl   string | The URL of the company website. <br>Max length: 255 |
| description   string | The description of the company. <br>Max length: 255 |
| erpId   string | The ERP Partner Company ID. <br>Max length: 255 |
| taxId   string | The Tax ID. <br>Max length: 255 |
| imageUrl   string | The URL of the image associated to the company. <br>Max length: 255 |
| status   enum:string | The status of the company. Possible values: `deleted`, `active` |
| createdAt   datetime: ISO 8601 | The timestamp when this company was created. |
| updatedAt   datetime: ISO 8601 | The timestamp when this company was last updated. This will only reflect changes to the company fields and not changes to any resources in the company. |
| originalName   null,string | Original name of the company. Only returned when a company is deleted, since, in this case, the company ânameâ will be updated to âremoved at MMDDYYYYâ. |
| projectSize   int | The number of projects associated with the company. |
| userSize   int | The number of users that are associated with the company. |

## [Example](#example)

The list of requested companies.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/admin/v1/accounts/d73fc742-4538-401c-8d0f-853b49b750b2/companies?filter[name]=Plumbing unlimited&filter[trade]=Plumbing&filter[erpId]=companyErpId&filter[taxId]=434920482-22&filter[updatedAt]=2019-06-01T00:00:00.000Z..&orFilters=name,trade&filterTextMatch=contains&sort=name&fields=name&limit=20' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 20,
    "offset": 10,
    "totalResults": 121,
    "nextUrl": "https://resource?limit=20&offset=30",
    "previousUrl": "https://resource?limit=20&offset=0"
  },
  "results": [
    {
      "id": "d1163421-e7eb-4862-ac15-b33777ba42de",
      "accountId": "d73fc742-4538-401c-8d0f-853b49b750b2",
      "name": "Plumbing Unlimited",
      "trade": "Plumbing",
      "addresses": [
        {
          "type": "Main",
          "addressLine1": "123 Main Street",
          "addressLine2": "Suite 2",
          "city": "San Francisco",
          "stateOrProvince": "California",
          "postalCode": "94001",
          "country": "US",
          "phone": "555-555-5555"
        }
      ],
      "websiteUrl": "https://www.plumbingunlimited.com",
      "description": "Plumbing subcontractor in southern California",
      "erpId": "12345678",
      "taxId": "87654321",
      "imageUrl": "https://images.acc.autodesk.com/plumbingunlimited.png",
      "status": "active",
      "createdAt": "2018-01-01T12:45:00.000Z",
      "updatedAt": "2018-01-01T12:45:00.000Z",
      "originalName": "",
      "projectSize": 3,
      "userSize": 12
    }
  ]
}

```

Show More
