# users

Source: https://aps.autodesk.com/en/docs/acc/reference/http/users-POST/

---

Account Users

POST

# users

Create a new user in the BIM 360 member directory.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/hq/v1/accounts/:account_id/users |
| --- | --- |
| Method and URI (Legacy) | POST https://developer.api.autodesk.com/hq/v1/regions/eu/accounts/:account_id/users |
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

| account_id   string: UUID | The account ID of the user. This corresponds to hub ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/). To convert a hub ID into an account ID you need to remove the â**b.**" prefix. For example, a hub ID of **b.**c8b0c73d-3ae9 translates to an account ID of c8b0c73d-3ae9. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

The POST body is a flat JSON object with the following attributes:

| company_id   string: UUID | The userâs default company ID in BIM 360 |
| --- | --- |
| email*   string | Userâs email       Max length: 255 |
| nickname   string | Nick name for user       Max length: 255 |
| first_name   string | Userâs first name       Max length: 255 |
| last_name   string | Userâs last name       Max length: 255 |
| image_url   string | URL for userâs profile image       Max length: 255 |
| address_line_1   string | Userâs address line 1       Max length: 255 |
| address_line_2   string | Userâs address line 2       Max length: 255 |
| city   string | City in which user is located       Max length: 255 |
| state_or_province   enum: string | State or province in which user is located       Max length: 255       Note that the `state_or_province` value depends on the selected `country` value; see the valid values in the `state_or_province` list in the [Parameters](https://aps.autodesk.com/en/docs/bim360/v1/overview/parameters/) guide. |
| postal_code   string | Postal code for the userâs location       Max length: 255 |
| country   enum: string | Country for this user       Refer to the `country` list in the [Parameters](https://aps.autodesk.com/en/docs/bim360/v1/overview/parameters/) guide. |
| phone   string | Contact phone number for the user       Max length: 255 |
| company   string | Company information from the Autodesk user profile       Max length: 255       Note that this is different from company in BIM 360. |
| job_title   string | Userâs job title       Max length: 255 |
| industry   string | Industry information for user       Max length: 255 |
| about_me   string | Short description about the user       Max length: 255 |
| default_role   string | The userâs default role       Max length: 255 |

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

A successful response is the created user, a flat JSON object with the following attributes:

| id   string: UUID | User ID |
| --- | --- |
| account_id   string: UUID | Account ID |
| role   string | The role of the user in the account       New user should be `account_user` only. |
| status   string | Status of the user in the system       A new account user is always `not_invited`. |
| company_id   string: UUID | The userâs default company ID in BIM 360 |
| company_name   string | The name of the userâs default company name in BIM 360 |
| last_sign_in   datetime: ISO 8601 | The time and date of the userâs most recent sign-in, in ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sssZ`). Note that this field is not supported by ACC Unified products. The value is updated only when the user logs into one of the following services associated with the specified BIM 360 account: BIM 360 Account Admin, BIM 360 Project Admin, BIM 360 Document Management, BIM 360 Field (Classic), or BIM 360 Plan. |
| email   string | Userâs email       Max length: 255 |
| name   string | Default display name       Max length: 255 |
| nickname   string | Nick name for user       Max length: 255 |
| first_name   string | Userâs first name       Max length: 255 |
| last_name   string | Userâs last name       Max length: 255 |
| uid   string | Userâs Autodesk ID |
| image_url   string | URL for userâs profile image       Max length: 255 |
| address_line_1   string | Userâs address line 1       Max length: 255 |
| address_line_2   string | Userâs address line 2       Max length: 255 |
| city   string | City in which user is located       Max length: 255 |
| state_or_province   enum: string | State or province in which user is located       Max length: 255       Note that the `state_or_province` value depends on the selected `country` value; see the valid values in the `state_or_province` list in the [Parameters](https://aps.autodesk.com/en/docs/bim360/v1/overview/parameters/) guide. |
| postal_code   string | Postal code for the userâs location       Max length: 255 |
| country   enum: string | Country for this user       Refer to the `country` list in the [Parameters](https://aps.autodesk.com/en/docs/bim360/v1/overview/parameters/) guide. |
| phone   string | Contact phone number for the user       Max length: 255 |
| company   string | Company information from the Autodesk user profile       Max length: 255       Note that this is different from company in BIM 360. |
| job_title   string | Userâs job title       Max length: 255 |
| industry   string | Industry information for user       Max length: 255 |
| about_me   string | Short description about the user |
| default_role   string | The userâs default role. |
| default_role_id   string | The ID of the default role.       Max length: 255 |
| created_at   datetime: ISO 8601 | `YYYY-MM-DDThh:mm:ss.sssZ` format |
| updated_at   datetime: ISO 8601 | `YYYY-MM-DDThh:mm:ss.sssZ` format |

## [Example](#example)

Successful User Creation (201)

### Request

```
curl -v 'https://developer.api.autodesk.com/hq/v1/accounts/9dbb160e-b904-458b-bc5c-ed184687592d/users' \
  -X 'POST' \
  -H 'Authorization: Bearer XZvCJNhdxESsBRIH28MfLf2hKL5O' \
  -H 'Content-Type: application/json' \
  -d '{
    "email": "john.smith@mail.com",
    "company_id": "14e95a5e-02eb-49aa-a39a-447d90544873",
    "nickname": "Johnny",
    "first_name": "John",
    "last_name": "Smith",
    "image_url": "/image/johnsmith.jpeg",
    "address_line_1": "The Fifth Avenue",
    "address_line_2": "#301",
    "city": "shanghai",
    "postal_code": "20000",
    "state_or_province": "Shanghai",
    "country": "China",
    "phone": "1234567",
    "company": "Autodesk",
    "job_title": "software developer",
    "industry": "IT",
    "about_me": "Nothing here",
    "default_role": "BIM Manager"
    }'

```

Show More

### Response

```
{
  "id": "79b51334-1127-4313-a0e1-4986b3e96c47",
  "account_id": "9dbb160e-b904-458b-bc5c-ed184687592d",
  "status": "not_invited",
  "role": "account_user",
  "company_id": "14e95a5e-02eb-49aa-a39a-447d90544873",
  "company_name": "Autodesk",
  "last_sign_in": null,
  "email": "john.smith@mail.com",
  "name": "John Smith",
  "nickname": "Johnny",
  "first_name": "John",
  "last_name": "Smith",
  "uid": "L9EBJKCGCXBB",
  "image_url": "http://static-dc.autodesk.net/etc/designs/v201412151200/autodesk/adsk-design/images/autodesk_header_logo_140x23.png",
  "address_line_1": "The Fifth Avenue",
  "address_line_2": "#301",
  "city": "Shanghai",
  "postal_code": "10010",
  "state_or_province": "New York",
  "country": "United States",
  "phone": "(634)329-2353",
  "company": "Autodesk",
  "job_title": "Software Developer",
  "industry": "IT",
  "about_me": "Nothing here",
  "default_role": "BIM Manager",
  "default_role_id": "4e7e02ae-2994-4210-9153-84bfb9a23a63",
  "created_at": "2016-04-07T08:45:51.050Z",
  "updated_at": "2016-04-07T08:45:51.050Z"
}

```

Show More
