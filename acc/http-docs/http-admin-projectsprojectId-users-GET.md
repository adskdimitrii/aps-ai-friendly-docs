# projects/{projectId}/users

Source: https://aps.autodesk.com/en/docs/acc/reference/http/admin-projectsprojectId-users-GET/

---

projects/:project_id/users

GET

# projects/{projectId}/users

Retrieves information about a filtered subset of users in the specified project.

There are two primary reasons to do this:

- To verify that all users assigned to the project have been activated as members of the project.
- To check other information about users, such as their project user ID, roles, and products.

Note that if you want to retrieve information about users associated with a particular Autodesk account, call the [GET users](http-users-GET.md) endpoint.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/admin/v1/projects/:projectId/users |
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

| projectId   string: UUID | The ID of the project. This corresponds to project ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/). To convert a project ID in the Data Management API into a project ID in the ACC API you need to remove the “**b.**" prefix. For example, a project ID of `b.a4be0c34a-4ab7` translates to a project ID of `a4be0c34a-4ab7`. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| filter[products]   array: string | A comma-separated list of the products that the returned users must have access to in the specified project. Only users that have access to one or more of the specified products are returned. <br>Note that every product in the same account as the project is activated for the project, and a separate subset of these products is active for each user. This endpoint can retrieve users from ACC or BIM 360 projects.<br>Some products are exclusive to ACC or to BIM 360, others are available on both platforms. Specify only the products on the appropriate platform for the users you want to retrieve.<br>Possible ACC values: `accountAdministration`, `autoSpecs`, `build`, `buildingConnected`, `capitalPlanning`, `cloudWorksharing`, `cost`, `designCollaboration`, `docs`, `financials`, `insight`, `modelCoordination`, `projectAdministration`, `takeoff`, and `workshopxr`.<br>Possible BIM 360 values: `accountAdministration`, `assets`, `cloudWorksharing`, `costManagement`, `designCollaboration`, `documentManagement`, `field`, `fieldManagement`, `glue`, `insight`, `modelCoordination`, `plan`, `projectAdministration`, `projectHome`, `projectManagement`, and `quantification`. |
| --- | --- |
| filter[name]   string | A user name or name pattern that the returned users must have. Can be a partial match based on the value of `filterTextMatch` that you provide. <br>For example:<br>`filter[name]=Sample filterTextMatch=startsWith`<br>Max length: 255 |
| filter[email]   string | A user email address or address pattern that the returned users must have. This can be a partial match based on the value of `filterTextMatch` that you provide. <br>For example:<br>`filter[email]=sample filterTextMatch=startsWith`<br>Max length: 255 |
| filter[accessLevels]   array: string | A list of user access levels that the returned users must have. <br>Possible values: `accouantAdmin`, `projectAdmin`, `executive`.<br>Max length: 255 |
| filter[companyId]   string | The ID of a company that the returned users must represent. <br>Max length: 255 |
| filter[companyName]   string | The name of a company that returned users must be associated with. Can be a partial match based on the value of `filterTextMatch` that you provide. <br>For example: `filter[companyName]=Sample filterTextMatch=startsWith`<br>Max length: 255 |
| filter[autodeskId]   array: string | A list of the Autodesk IDs of users to retrieve. |
| filter[id]   array: string: uuid | A list of the ACC IDs of users to retrieve. |
| filter[roleId]   string: UUID | The ID of a user role that the returned users must have. <br>To obtain a role ID for this filter, you can inspect the `roleId` field in previous responses to this endpoint or to the [GET projects/:projectId/users/:userId](https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-projects-projectId-users-userId-GET/) endpoint.<br>Max length: 255 |
| filter[roleIds]   array: string: uuid | A list of the IDs of user roles that the returned users must have. <br>To obtain a role ID for this filter, you can inspect the `roleId` field in previous responses to this endpoint or to the [GET projects/:projectId/users/:userId](https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-projects-projectId-users-userId-GET/) endpoint. |
| filter[status]   array: string | A list of statuses that the returned project users must be in. The default values are `active` and `pending`. <br>Possible values: `active`, `pending`, and `deleted`. |
| sort   array: string | A list of fields to sort the returned users by. Multiple sort fields are applied in sequence order - each sort field produces groupings of projects with the same values of that field; the next sort field applies within the groupings produced by the previous sort field. <br>Each property can be followed by a direction modifier of either `asc` (ascending) or `desc` (descending). The default is `asc`.<br>Possible values: `name`, `email`, `firstName`, `lastName`, `addressLine1`, `addressLine2`, `city`, `companyName`, `stateOrProvince`, `status`, `phone`, `postalCode`, `country` and `addedOn`. Default value: `name`. |
| fields   array: string | A list of the project fields to include in the response. Default value: all fields. <br>Possible values: `name`, `email`, `firstName`, `lastName`, `autodeskId`, `analyticsId`, `addressLine1`, `addressLine2`, `city`, `stateOrProvince`, `postalCode`, `country`, `imageUrl`, `phone`, `jobTitle`, `industry`, `aboutMe`, `companyId`, `accessLevels`, `roleIds`, `roles`, `status`, `addedOn` and `products`. |
| orFilters   array: string | A list of user fields to combine with the SQL *OR* operator for filtering the returned project users. The *OR* is automatically incorporated between the fields; any one of them can produce a valid match. <br>Possible values: `id`, `name`, `email`, `autodeskId`, `status` and `accessLevels`. |
| filterTextMatch   enum:string | Specifies how text-based filters should match values in supported fields. <br>This parameter can be used in any endpoint that supports text-based filtering (e.g., `filter[name]`, `filter[jobNumber]`, `filter[companyName]`, etc.).<br>Possible values:<br>`contains` (default) – Matches if the field contains the specified text anywhere<br>`startsWith` – Matches if the field starts with the specified text<br>`endsWith` – Matches if the field ends with the specified text<br>`equals` – Matches only if the field exactly matches the specified text<br>Matching is case-insensitive.<br>Wildcards and regular expressions are not supported. |
| limit   int | The maximum number of records to return in the response. <br>Default: `20`<br>Minimum: `1`<br>Maximum: `200` (If a larger value is provided, only 200 records are returned) |
| offset   int | The index of the first record to return. <br>Used for pagination in combination with the `limit` parameter.<br>Example: `limit=20` and `offset=40` returns records 41–60. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | A list of requested project users. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax. |
| 401   Unauthorized | Request has not been applied because it lacks valid authentication credentials for the target resource. |
| 403   Forbidden | The server understood the request but refuses to authorize it. |
| 404   Not Found | The resource could not be found. |
| 406   Not Acceptable | The server cannot produce a response matching the list of acceptable values defined in the request. |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the resource. |
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
| results   array: object | The requested page of project users. |
| email   string | The email of the user. <br>Max length: 255 |
| id   string: UUID | The ACC ID of the user. |
| name   string | The full name of the user. <br>Max length: 255 |
| firstName   string | The user’s first name. This data syncs from the user’s Autodesk profile. <br>Max length: 255 |
| lastName   string | The user’s last name. This data syncs from the user’s Autodesk profile. <br>Max length: 255 |
| autodeskId   string | The ID of the user’s Autodesk profile. <br>Max length: 255 |
| analyticsId   string | Not relevant |
| addressLine1   string | The user’s address line 1. This data syncs from the user’s Autodesk profile. <br>Max length: 255 |
| addressLine2   string | The user’s address line 2. This data syncs from the user’s Autodesk profile. <br>Max length: 255 |
| city   string | The User’s city. This data syncs from the user’s Autodesk profile. <br>Max length: 255 |
| stateOrProvince   string | The state or province of the user. The accepted values here change depending on which country is provided. This data syncs from the user’s Autodesk profile. <br>Max length: 255 |
| postalCode   string | The zip or postal code of the user. This data syncs from the user’s Autodesk profile. <br>Max length: 255 |
| country   string | The user’s country. This data syncs from the user’s Autodesk profile. <br>Max length: 255 |
| imageUrl   string | The URL of the user’s avatar. This data syncs from the user’s Autodesk profile. <br>Max length: 255 |
| phone   object | The user’s phone number. This data syncs from the user’s Autodesk profile. |
| number   string | User’s phone number |
| phoneType   enum:string | The user’s phone type. <br>Possible values: `home`, `mobile`, or `office`. Default value: `mobile`. |
| extension   string | User’s phone extension. |
| jobTitle   string | The user’s job title. This data syncs from the user’s Autodesk profile. <br>Max length: 255 |
| industry   string | The industry the user works in. This data syncs from the user’s Autodesk profile. <br>Max length: 255 |
| aboutMe   string | A short bio about the user. This data syncs from the user’s Autodesk profile. <br>Max length: 255 |
| accessLevels   object | Flags that identify a returned user’s access levels in the account or project. |
| accountAdmin   boolean | Indicates whether the user is an account administrator for the account. Possible values: <br>`true`: The user is an account administrator.`false`: The user is not an account administrator. |
| projectAdmin   boolean | Indicates whether the user is a project administrator for the project. Possible values: <br>`true`: The user is a project administrator.`false`: The user is not a project administrator. |
| executive   boolean | Indicates whether the user is an executive in the account. Possible values: <br>`true`: The user is an executive.`false`: The user is not an executive. |
| addedOn   datetime: ISO 8601 | The timestamp when the user was first given access to any product on the project. |
| updatedAt   datetime: ISO 8601 | The timestamp when the project user was last updated, in ISO 8601 format. |
| companyId   null,string | The ID of the company that the user is representing in the project. To obtain a list of all company IDs associated with a project, call [GET projects/:projectId/companies](http-projects--project_id-companies-GET.md). |
| companyName   null,string | The name of the company to which the user belongs. <br>Max length: 255 |
| roleIds   array: string | A list of IDs of the roles that the user belongs to in the project. |
| roles   array: object | A list of the role IDs and names that are associated with the user in the project. |
| id   string: UUID | The ID of a role that the user belongs to in the project. |
| name   string | The name of a role that the user belongs to in the project. |
| status   string | The status of the user in the project. A pending user could be waiting for their products to activate, or the user hasn’t accepted an email to create an account with Autodesk. <br>Possible values:<br>`active`: The user has been added to the project.`pending`: The user is in the process of being added to the project.`disabled`: The user has been temporarily suspended from the project.`deleted`: The user has been removed from the project. |
| products   array: object | Information about the products activated in the specified project for this user. |
| key   enum:string | A machine-readable identifier for the product (e.g., docs, build). <br>Each product has a unique key used throughout the API for identification, filtering, and integration logic (e.g., in query parameters like `filter[key]`).<br>Possible values: ACC - `autoSpecs`, `build`, `cost`, `designCollaboration`, `docs`, `insight`, `modelCoordination`, `projectAdministration`, and `takeoff`.<br>BIM 360 - `assets`, `costManagement`, `designCollaboration`, `documentManagement`, `field`, `fieldManagement`, `glue`, `insight`, `modelCoordination`, `plan`, `projectAdministration`, `projectHome`, `projectManagement`, and `quantification`.<br>Note that this endpoint returns only ACC products. Other endpoints, such as [GET projects](https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-accountsaccountidprojects-GET/) and [GET projects/:projectId](https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-projects-projectId-GET/), may return both ACC and BIM 360 projects. In those responses, product keys may include BIM 360 values. |
| access   enum:string | The user’s type of access to the product identified by `key`. Possible values: <br>`administrator``member``none`<br>Note that when you’re using a POST or PATCH endpoint to set this value, you must adhere to the following guidelines:<br>If you set a product’s `key` to `projectAdministration` and you set `access` to `none`, all other products should be set to `member` access for the user.If you set a product’s `key` to `projectAdministration` and you set `access` to `administrator`, all other products should be set to `administrator` access for the user.You cannot set a product’s `key` to `projectAdministration` and set `access` to `member`. |

## [Example](#example)

A list of requested project users.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/admin/v1/projects/367d5cc2-9008-462c-96e5-c9491db85d93/users?filter[products]=build,cost&filter[name]=Sample User&filter[email]=sampleUser1@autodesk.com&filter[accessLevels]=accountAdmin,executive&filter[companyId]=d1163421-e7eb-4862-ac15-b33777ba42de&filter[companyName]=Sample Company&filter[autodeskId]=User123,User124&filter[id]=39712a51-bd64-446a-9c72-48c4e43d0a0d,d1163421-e7eb-4862-ac15-b33777ba42de&filter[roleId]=cda845af-05f0-4c46-9108-71b993946c35&filter[roleIds]=cda845af-05f0-4c46-9108-71b993946c35,b8e84a73-7506-4d3f-b221-93691df2a359&filter[status]=active,pending&sort=name&fields=name,email&orFilters=id,name&filterTextMatch=contains&limit=20' \
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
      "email": "sampleUser1@autodesk.com",
      "id": "39712a51-bd64-446a-9c72-48c4e43d0a0d",
      "name": "Bob Smith",
      "firstName": "Bob",
      "lastName": "Smith",
      "autodeskId": "USER123A",
      "analyticsId": "SOMEID123",
      "addressLine1": "123 Main Street",
      "addressLine2": "Suite 2",
      "city": "San Francisco",
      "stateOrProvince": "California",
      "postalCode": "94001",
      "country": "United States",
      "imageUrl": "https://s3.amazonaws.com:443/com.autodesk.storage.public.dev/oxygen/USER123A/profilepictures/x20.jpg",
      "phone": {
        "number": "123-345-1234",
        "phoneType": "mobile",
        "extension": "10"
      },
      "jobTitle": "Owner",
      "industry": "Architecture & Construction Service Providers",
      "aboutMe": "Bob has been in construction for 25 years.",
      "accessLevels": {
        "accountAdmin": true,
        "projectAdmin": true,
        "executive": true
      },
      "addedOn": "2018-01-01T12:45:00.000Z",
      "updatedAt": "2018-01-01T12:45:00.000Z",
      "companyId": "c32ffb13-83f8-43fb-bddf-3e5c0c2dda24",
      "companyName": "Sample Company",
      "roleIds": [
        "cda845af-05f0-4c46-9108-71b993946c35",
        "b8e84a73-7506-4d3f-b221-93691df2a359"
      ],
      "roles": [
        {
          "id": "cda845af-05f0-4c46-9108-71b993946c35",
          "name": "Architect"
        },
        {
          "id": "b8e84a73-7506-4d3f-b221-93691df2a359",
          "name": "Engineer"
        }
      ],
      "status": "active",
      "products": [
        {
          "key": "projectAdministration",
          "access": "administrator"
        },
        {
          "key": "designCollaboration",
          "access": "administrator"
        },
        {
          "key": "build",
          "access": "administrator"
        },
        {
          "key": "cost",
          "access": "administrator"
        },
        {
          "key": "modelCoordination",
          "access": "administrator"
        },
        {
          "key": "docs",
          "access": "administrator"
        },
        {
          "key": "insight",
          "access": "administrator"
        },
        {
          "key": "takeoff",
          "access": "administrator"
        }
      ]
    }
  ]
}

```

Show More
