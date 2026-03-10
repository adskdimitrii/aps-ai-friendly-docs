# accounts/{accountId}/users/{userId}/roles

Source: https://aps.autodesk.com/en/docs/acc/reference/http/admin-usersuseridroles-GET/

---

users/:user_id/roles

GET

# accounts/{accountId}/users/{userId}/roles

Returns the roles assigned to a specific user across the projects they belong to.

Only users with account admin permissions can call this endpoint. To verify a user’s permissions, call [GET users](http-admin-projectsprojectId-users-GET.md).
> Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/admin/v1/accounts/:accountId/users/:userId/roles |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `account:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Region   string | Specifies the region where your request should be routed. If not set, the request is routed automatically, which may result in a slight increase in latency. <br>Possible values: `US`, `EMEA`. For a complete list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |
| User-Id   string | The ID of a user on whose behalf your request is acting. <br>Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.<br>You can use either the user’s ACC ID (`id`), or their Autodesk ID (`autodeskId`).<br>Note that this header is required for Account Admin POST, PATCH, and DELETE endpoints if you want to use a 2-legged authentication context. This header is optional for Account Admin GET endpoints. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| accountId   string: UUID | The ID of the ACC account that contains the project being created or the projects being retrieved. This corresponds to the hub ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/). To convert a hub ID into an account ID, remove the “**b.**" prefix. For example, a hub ID of `b.c8b0c73d-3ae9` translates to an account ID of `c8b0c73d-3ae9`. |
| --- | --- |
| userId   string | The ID of the user. To find the ID call [GET users](http-admin-projectsprojectId-users-GET.md). You can use either the ACC ID (`id`) or the Autodesk ID (`autodeskId`). |

### Request

## [Query String Parameters](#query-string-parameters)

| filter[projectId]   array: string: uuid | A list of project IDs. Only results where the user is associated with one or more of the specified projects are returned. |
| --- | --- |
| filter[status]   array: string | Filters roles by their status. Accepts one or more of the following values: <br>`active` – The role is currently in use.<br>`inactive` – The role has been removed or is no longer in use. |
| filter[name]   string | Filters roles by name. <br>By default, this performs a partial match (case-insensitive).<br>You can control how the match behaves by using the `filterTextMatch` parameter. For example, to match only names that start with (startsWith), end with (endsWith), or exactly equal (equals) the provided value. |
| filterTextMatch   enum:string | Specifies how text-based filters should match values in supported fields. <br>This parameter can be used in any endpoint that supports text-based filtering (e.g., `filter[name]`, `filter[jobNumber]`, `filter[companyName]`, etc.).<br>Possible values:<br>`contains` (default) – Matches if the field contains the specified text anywhere<br>`startsWith` – Matches if the field starts with the specified text<br>`endsWith` – Matches if the field ends with the specified text<br>`equals` – Matches only if the field exactly matches the specified text<br>Matching is case-insensitive.<br>Wildcards and regular expressions are not supported. |
| fields   array: string | A comma-separated list of response fields to include. Defaults to all fields if not specified. <br>Use this parameter to reduce the response size by retrieving only the fields you need.<br>Possible values:<br>`projectIds` – Projects where the user holds this role<br>`name` – Role name<br>`status` – Role status (active or inactive)<br>`key` – Internal key used to translate the role name<br>`createdAt` – Timestamp when the role was created<br>`updatedAt` – Timestamp when the role was last updated |
| sort   array: string | Sorts the results by one or more fields. <br>Each field can be followed by a direction modifier:<br>`asc` – Ascending order (default)<br>`desc` – Descending order<br>Possible values: `name`, `createdAt`, `updatedAt`.<br>Default sort: `name asc`<br>Example: `sort=name,updatedAt desc` |
| limit   int | The maximum number of records to return in the response. <br>Default: `20`<br>Minimum: `1`<br>Maximum: `200` (If a larger value is provided, only 200 records are returned) |
| offset   int | The index of the first record to return. <br>Used for pagination in combination with the `limit` parameter.<br>Example: `limit=20` and `offset=40` returns records 41–60. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | A list of requested roles associated with the user |
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
| results   array: object | The requested page of roles associated with the user. |
| id   string: UUID | The unique ID of the role. |
| status   enum:string | The role status. Possible values: active, inactive. |
| name   string | The name of the role. Predefined roles are localized based on the request language. <br>Max length: 255 |
| key   string | The internal key used for translating predefined role names. <br>Max length: 255 |
| createdAt   datetime: ISO 8601 | The timestamp when the role was created. |
| updatedAt   datetime: ISO 8601 | The timestamp when the role was last updated. |
| projectIds   array: string | The list of projects where the user is associated with this role. |

## [Example](#example)

A list of requested roles associated with the user

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/admin/v1/accounts/d73fc742-4538-401c-8d0f-853b49b750b2/users/6cc15635-2fbd-4f73-afbe-abd833408a1d/roles?filter[projectId]=39712a51-bd64-446a-9c72-48c4e43d0a0d,d1163421-e7eb-4862-ac15-b33777ba42de&filter[status]=active&filter[name]=Architect&filterTextMatch=contains&fields=name&sort=name&limit=20' \
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
      "id": "287d5cc2-9008-462c-96e5-c9491db85d97",
      "status": "active",
      "name": "Architect",
      "key": "architect",
      "createdAt": "2018-01-01T12:45:00.000Z",
      "updatedAt": "2019-01-01T12:45:00.000Z",
      "projectIds": [
        "3e354e66-ac8b-41dd-9bc1-93fc182c25dd"
      ]
    }
  ]
}

```

Show More
