# users/:user_id

Source: https://aps.autodesk.com/en/docs/acc/reference/http/users-:user_id-PATCH/

---

Hub Users

PATCH

# users/:user_id

Update a specific user’s status or default company.

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/hq/v1/accounts/:account_id/users/:user_id |
| --- | --- |
| Method and URI (Legacy) | PATCH https://developer.api.autodesk.com/hq/v1/regions/eu/accounts/:account_id/users/:user_id |
| Authentication Context | app only |
| Required OAuth Scopes | `account:write` |
| Data Formats | JSON |

### Request

## [Headers](#headers)

| Authorization   yes | Must be `Bearer <token>`, where `<token>` is obtained via a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type   yes | Must be `application/json` |
| Region   no | Specifies the region where the service is located. Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |

### Request

## [URI Parameters](#uri-parameters)

| account_id   string: UUID | The account/hub ID of the user. This corresponds to hub ID in the Data Management API. To obtain hub ID you need to remove the “b.” prefix. For example: b.c8b0c73d-3ae9 becomes c8b0c73d-3ae9. |
| --- | --- |
| user_id   string: UUID | User ID |

### Request

## [Body Structure](#body-structure)

The PATCH body is a flat JSON object with the following attributes:

| status   string | New status to set the user to (only if not currently `pending` or `not_invited`)       Possible values:   `active`: user is active and has logged into the system sucessfully   `inactive`: user is disabled |
| --- | --- |
| company_id   string: UUID | The user’s default company ID in BIM 360 |
| default_role   string | The user’s default role       Max length: 255 |

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

A successful response is the modified user, a flat JSON object with the following attributes:

| id   string: UUID | User ID |
| --- | --- |
| account_id   string: UUID | Account/Hub ID |
| role   string | The role of the user in the account/hub       Possible values:   `account_admin`: user has BIM 360 account administration access   `account_user` : normal project user   `project_admin`: user has Project administration privileges at a service level |
| status   string | Status of the user in the system       Possible values:   `active`: user is active and has logged into the system sucessfully   `inactive`: user is disabled   `pending`: user is invited and is yet to accept the invitation   `not_invited`: user is not invited |
| company_id   string: UUID | The user’s default company ID in BIM 360 |
| company_name   string | The name of the user’s default company name in BIM 360 |
| last_sign_in   datetime: ISO 8601 | The time and date of the user’s most recent sign-in, in ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sssZ`). Note that this field is not supported by Forma Unified products. The value is updated only when the user logs into one of the following services associated with the specified BIM 360 account: BIM 360 Account Admin, BIM 360 Project Admin, BIM 360 Document Management, BIM 360 Field (Classic), or BIM 360 Plan. |
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
| about_me   string | Short description about the user       Max length: 255 |
| default_role   string | The user’s default role. |
| default_role_id   string | The ID of the default role. |
| created_at   datetime: ISO 8601 | `YYYY-MM-DDThh:mm:ss.sssZ` format |
| updated_at   datetime: ISO 8601 | `YYYY-MM-DDThh:mm:ss.sssZ` format |

## [Example](#example)

Successful Updating of User’s Status and Company (200)

### Request

```
curl -v 'https://developer.api.autodesk.com/hq/v1/accounts/9dbb160e-b904-458b-bc5c-ed184687592d/users/a75e8769-621e-40b6-a524-0cffdd2f784e' \
  -X 'PATCH' \
  -H 'Authorization: Bearer XZvCJNhdxESsBRIH28MfLf2hKL5O' \
  -H 'Content-Type: application/json' \
  -d '{
    "status": "inactive",
    "company_id": "14e95a5e-02eb-49aa-a39a-447d90544873",
    "default_role": "BIM Manager"
  }'

```

Show More

### Response

```
{
  "id": "a75e8769-621e-40b6-a524-0cffdd2f784e",
  "account_id": "9dbb160e-b904-458b-bc5c-ed184687592d",
  "status": "inactive",
  "role": "account_admin",
  "company_id": "14e95a5e-02eb-49aa-a39a-447d90544873",
  "company_name": "Autodesk",
  "last_sign_in": "2016-04-07 08:00:24.020422",
  "email": "john.smith@mail.com",
  "name": "John Smith",
  "nickname": "Johnny",
  "first_name": "John",
  "last_name": "Smith",
  "uid": "L9EBJKCGCXBB",
  "image_url": "http://static-dc.autodesk.net/etc/designs/v201412151200/autodesk/adsk-design/images/autodesk_header_logo_140x23.png",
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
  "created_at": "2015-06-26T14:47:39.458Z",
  "updated_at": "2016-04-07T08:00:24.027Z"
}

```

Show More
