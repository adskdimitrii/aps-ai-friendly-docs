# users/search

Source: https://aps.autodesk.com/en/docs/acc/reference/http/users-search-GET/

---

Account Users

GET

# users/search

Search users in the master member directory of a specific BIM 360 account by specified fields.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/hq/v1/accounts/:account_id/users/search |
| --- | --- |
| Method and URI (Legacy) | GET https://developer.api.autodesk.com/hq/v1/regions/eu/accounts/:account_id/users/search |
| Authentication Context | app only |
| Required OAuth Scopes | `account:read` |
| Data Formats | JSON |

### Request

## [Headers](#headers)

| HTTP Headers | Type | Required | Description |
| --- | --- | --- | --- |
| Authorization | string | yes | Must be `Bearer <token>`, where `<token>` is obtained via a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) OAuth flow. |
| Region | string | no | Specifies the region where the service is located. Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |

### Request

## [URI Parameters](#uri-parameters)

| account_id   string: UUID | The account ID of the users. This corresponds to hub ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/). To convert a hub ID into an account ID you need to remove the “**b.**" prefix. For example, a hub ID of **b.**c8b0c73d-3ae9 translates to an account ID of c8b0c73d-3ae9. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| name   string | User name to match   Max length: 255 |
| --- | --- |
| email   string | User email to match   Max length: 255 |
| company_name   string | User company to match   Max length: 255 |
| operator   enum: string | Boolean operator to use: `OR` (default) or `AND` |
| partial   bool | If `true` (default), perform a fuzzy match |
| limit   int | Response array’s size   Default value: `10`   Max limit: `100` |
| offset   int | Offset of response array   Default value: `0` |
| sort   string | Comma-separated fields to sort by in ascending order       Prepending a field with `-` sorts in descending order.   Invalid fields and whitespaces will be ignored. |
| field   string | Comma-separated fields to include in response       `id` will always be returned.   Invalid fields will be ignored. |

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

A successful response is an array of users, flat JSON objects with the following attributes:

| id   string: UUID | User ID |
| --- | --- |
| account_id   string: UUID | Account ID |
| role   string | The role of the user in the account       Possible values:   `account_admin`: user has BIM 360 account administration access   `account_user` : normal project user   `project_admin`: user has Project administration privileges at a service level |
| status   string | Status of the user in the system       Possible values:   `active`: user is active and has logged into the system sucessfully   `inactive`: user is disabled   `pending`: user is invited and is yet to accept the invitation   `not_invited`: user is not invited |
| company_id   string: UUID | The user’s default company ID in BIM 360 |
| company_name   string | The name of the user’s default company name in BIM 360 |
| last_sign_in   datetime: ISO 8601 | The time and date of the user’s most recent sign-in, in ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sssZ`). Note that this field is not supported by ACC Unified products. The value is updated only when the user logs into one of the following services associated with the specified BIM 360 account: BIM 360 Account Admin, BIM 360 Project Admin, BIM 360 Document Management, BIM 360 Field (Classic), or BIM 360 Plan. |
| email   string | User’s email       Max length: 255 |
| name   string | Default display name       Max length: 255 |
| nickname   string | Nick name for user       Max length: 255 |
| first_name   string | User’s first name       Max length: 255 |
| last_name   string | User’s last name       Max length: 255 |
| uid   string | User’s Autodesk ID |
| image_url   string | URL for user’s profile image       Max length: 255 |
| address_line_1   string | User’s address line 1       Max length: 255 |
| address_line_2   string | User’s address line 2       Max length: 255 |
| city   string | City in which user is located       Max length: 255 |
| state_or_province   enum: string | State or province in which user is located       Max length: 255       Note that the `state_or_province` value depends on the selected `country` value; see the valid values in the `state_or_province` list in the [Parameters](https://aps.autodesk.com/en/docs/bim360/v1/overview/parameters/) guide. |
| postal_code   string | Postal code for the user’s location       Max length: 255 |
| country   enum: string | Country for this user       Refer to the `country` list in the [Parameters](https://aps.autodesk.com/en/docs/bim360/v1/overview/parameters/) guide. |
| phone   string | Contact phone number for the user       Max length: 255 |
| company   string | Company information from the Autodesk user profile       Max length: 255       Note that this is different from company in BIM 360. |
| job_title   string | User’s job title       Max length: 255 |
| industry   string | Industry information for user       Max length: 255 |
| about_me   string | Short description about the user       Max length: 25 |
| default_role   string | The user’s default role. |
| default_role_id   string | The ID of the default role. |
| created_at   datetime: ISO 8601 | `YYYY-MM-DDThh:mm:ss.sssZ` format |
| updated_at   datetime: ISO 8601 | `YYYY-MM-DDThh:mm:ss.sssZ` format |

## [Example](#example)

Successful Search for Users by Email Address (200)

### Request

```
curl -v 'https://developer.api.autodesk.com/hq/v1/accounts/efec10ec-a367-49fd-ab92-c70185fbb660/users/search?email=john.smith2%40gamil.com&limit=1' \
  -H 'Authorization: Bearer XZvCJNhdxESsBRIH28MfLf2hKL5O'

```

### Response

```
[
  {
    "id": "579d4408-39a4-4b3a-9474-6e781e68ab94",
    "account_id": "9dbb160e-b904-458b-bc5c-ed184687592d",
    "status": "pending",
    "role": "account_admin",
    "company_id": "14e95a5e-02eb-49aa-a39a-447d90544873",
    "company_name": "Autodesk",
    "email": "john.smith@mail.com",
    "name": "John Smith",
    "nickname": "Johnny",
    "first_name": "John",
    "last_name": "Smith",
    "uid": "L9EBJKCGCXBB",
    "image_url": "http://static-dc.autodesk.net/etc/designs/v201412151200/autodesk/adsk-design/images/autodesk_header_logo_140x23.png",
    "last_sign_in": null,
    "address_line_1": "The Fifth Avenue",
    "address_line_2": "#301",
    "city": "New York",
    "postal_code": "10011",
    "state_or_province": "New York",
    "country": "United States",
    "phone": "(634)329-2353",
    "company": "Autodesk",
    "job_title": "Software Developer",
    "industry": "IT",
    "about_me": "Nothing here",
    "default_role": "BIM Manager",
    "default_role_id": "4e7e02ae-2994-4210-9153-84bfb9a23a63",
    "created_at": "2015-04-29T06:59:05.582Z",
    "updated_at": "2015-04-29T06:59:05.582Z"
  }
]

```

Show More
