# projects/{projectId}/users

Source: https://aps.autodesk.com/en/docs/acc/reference/http/admin-projects-project-Id-users-POST/

---

projects/:project_id/users

POST

# projects/{projectId}/users

Assigns a user to the specified project.

Note that the `Authorization` header token can be obtained either via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow, or via a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) Oauth flow *with user impersonation*, for which the `User-Id` header is required.

Note that if you want to add multiple users at once, you can call [POST projects/:projectId/users:import](https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-projects-projectId-users-POST/).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/admin/v1/projects/:projectId/users |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `account:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| Region   string | Specifies the region where your request should be routed. If not set, the request is routed automatically, which may result in a slight increase in latency. <br>Possible values: `US`, `EMEA`. For a complete list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |
| User-Id   string | The ID of a user on whose behalf your request is acting. <br>Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.<br>You can use either the userâs ACC ID (`id`), or their Autodesk ID (`autodeskId`).<br>Note that this header is required for Account Admin POST, PATCH, and DELETE endpoints if you want to use a 2-legged authentication context. This header is optional for Account Admin GET endpoints. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. This corresponds to project ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/). To convert a project ID in the Data Management API into a project ID in the ACC API you need to remove the â**b.**" prefix. For example, a project ID of `b.a4be0c34a-4ab7` translates to a project ID of `a4be0c34a-4ab7`. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

User fields to add to the project. Required fields are `email` and `products`.

Expand all

| email*   string | The email address of the user. <br>Max length: 255 |
| --- | --- |
| companyId   null,string | The ID of the company that the user is representing in the project. To obtain a list of all company IDs associated with a project, call [GET projects/:projectId/companies](http-projects--project_id-companies-GET.md). |
| roleIds   array: string | A list of IDs of the roles that the user belongs to in the project. |
| products*   array: object | Information about the products activated in the specified project for this user. |
| key*   enum:string | A machine-readable identifier for the product (e.g., docs, build). <br>Each product has a unique key used throughout the API for identification, filtering, and integration logic (e.g., in query parameters like `filter[key]`).<br>Possible values: ACC - `autoSpecs`, `build`, `cost`, `designCollaboration`, `docs`, `insight`, `modelCoordination`, `projectAdministration`, and `takeoff`.<br>BIM 360 - `assets`, `costManagement`, `designCollaboration`, `documentManagement`, `field`, `fieldManagement`, `glue`, `insight`, `modelCoordination`, `plan`, `projectAdministration`, `projectHome`, `projectManagement`, and `quantification`.<br>Note that this endpoint returns only ACC products. Other endpoints, such as [GET projects](https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-accountsaccountidprojects-GET/) and [GET projects/:projectId](https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-projects-projectId-GET/), may return both ACC and BIM 360 projects. In those responses, product keys may include BIM 360 values. |
| access*   enum:string | The userâs type of access to the product identified by `key`. Possible values: <br>`administrator``member``none`<br>Note that when youâre using a POST or PATCH endpoint to set this value, you must adhere to the following guidelines:<br>If you set a productâs `key` to `projectAdministration` and you set `access` to `none`, all other products should be set to `member` access for the user.If you set a productâs `key` to `projectAdministration` and you set `access` to `administrator`, all other products should be set to `administrator` access for the user.You cannot set a productâs `key` to `projectAdministration` and set `access` to `member`. |
| suppressAdministrativeEmails   boolean | Suppresses project invite emails to the invited users. Defaults to false. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Successfully added the user to the project. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax. |
| 401   Unauthorized | Request has not been applied because it lacks valid authentication credentials for the target resource. |
| 403   Forbidden | The server understood the request but refuses to authorize it. |
| 404   Not Found | The resource could not be found. |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the resource. |
| 410 | Access to the target resource is no longer available. |
| 412 | The server refuses to accept the request because a pre-condition failed. |
| 415 | The server refuses to accept the request because the payload format is in an unsupported format. |
| 429   Too Many Requests | User has sent too many requests in a given amount of time. |
| 500   Internal Server Error | An unexpected error occurred on the server. |
| 503   Service Unavailable | Server is not ready to handle the request. |

### Response

## [Body Structure (201)](#body-structure-201)

Expand all

| email   string | The email of the user. <br>Max length: 255 |
| --- | --- |
| id   string: UUID | The ACC ID of the user. |
| name   string | The full name of the user. <br>Max length: 255 |
| firstName   string | The userâs first name. This data syncs from the userâs Autodesk profile. <br>Max length: 255 |
| lastName   string | The userâs last name. This data syncs from the userâs Autodesk profile. <br>Max length: 255 |
| autodeskId   string | The ID of the userâs Autodesk profile. <br>Max length: 255 |
| analyticsId   string | Not relevant |
| addressLine1   string | The userâs address line 1. This data syncs from the userâs Autodesk profile. <br>Max length: 255 |
| addressLine2   string | The userâs address line 2. This data syncs from the userâs Autodesk profile. <br>Max length: 255 |
| city   string | The Userâs city. This data syncs from the userâs Autodesk profile. <br>Max length: 255 |
| stateOrProvince   string | The state or province of the user. The accepted values here change depending on which country is provided. This data syncs from the userâs Autodesk profile. <br>Max length: 255 |
| postalCode   string | The zip or postal code of the user. This data syncs from the userâs Autodesk profile. <br>Max length: 255 |
| country   string | The userâs country. This data syncs from the userâs Autodesk profile. <br>Max length: 255 |
| imageUrl   string | The URL of the userâs avatar. This data syncs from the userâs Autodesk profile. <br>Max length: 255 |
| phone   object | The userâs phone number. This data syncs from the userâs Autodesk profile. |
| number   string | Userâs phone number |
| phoneType   enum:string | The userâs phone type. <br>Possible values: `home`, `mobile`, or `office`. Default value: `mobile`. |
| extension   string | Userâs phone extension. |
| jobTitle   string | The userâs job title. This data syncs from the userâs Autodesk profile. <br>Max length: 255 |
| industry   string | The industry the user works in. This data syncs from the userâs Autodesk profile. <br>Max length: 255 |
| aboutMe   string | A short bio about the user. This data syncs from the userâs Autodesk profile. <br>Max length: 255 |
| accessLevels   object | Flags that identify a returned userâs access levels in the account or project. |
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
| status   string | The status of the user in the project. A pending user could be waiting for their products to activate, or the user hasnât accepted an email to create an account with Autodesk. <br>Possible values:<br>`active`: The user has been added to the project.`pending`: The user is in the process of being added to the project.`disabled`: The user has been temporarily suspended from the project.`deleted`: The user has been removed from the project. |
| products   array: object | Information about the products activated in the specified project for this user. |
| key   enum:string | A machine-readable identifier for the product (e.g., docs, build). <br>Each product has a unique key used throughout the API for identification, filtering, and integration logic (e.g., in query parameters like `filter[key]`).<br>Possible values: ACC - `autoSpecs`, `build`, `cost`, `designCollaboration`, `docs`, `insight`, `modelCoordination`, `projectAdministration`, and `takeoff`.<br>BIM 360 - `assets`, `costManagement`, `designCollaboration`, `documentManagement`, `field`, `fieldManagement`, `glue`, `insight`, `modelCoordination`, `plan`, `projectAdministration`, `projectHome`, `projectManagement`, and `quantification`.<br>Note that this endpoint returns only ACC products. Other endpoints, such as [GET projects](https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-accountsaccountidprojects-GET/) and [GET projects/:projectId](https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-projects-projectId-GET/), may return both ACC and BIM 360 projects. In those responses, product keys may include BIM 360 values. |
| access   enum:string | The userâs type of access to the product identified by `key`. Possible values: <br>`administrator``member``none`<br>Note that when youâre using a POST or PATCH endpoint to set this value, you must adhere to the following guidelines:<br>If you set a productâs `key` to `projectAdministration` and you set `access` to `none`, all other products should be set to `member` access for the user.If you set a productâs `key` to `projectAdministration` and you set `access` to `administrator`, all other products should be set to `administrator` access for the user.You cannot set a productâs `key` to `projectAdministration` and set `access` to `member`. |
| jobId   string: UUID | Not relevant - we donât currently support this field. |

## [Example](#example)

Successfully added the user to the project.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/admin/v1/projects/367d5cc2-9008-462c-96e5-c9491db85d93/users' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "email": "sampleUser1@autodesk.com",
        "companyId": "c32ffb13-83f8-43fb-bddf-3e5c0c2dda24",
        "roleIds": [
          "cda845af-05f0-4c46-9108-71b993946c35",
          "b8e84a73-7506-4d3f-b221-93691df2a359"
        ],
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
        ],
        "suppressAdministrativeEmails": true
      }'

```

Show More

### Response

```
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
  ],
  "jobId": "5d3bc131-c0dc-4222-9a2a-351363f437fa"
}

```

Show More
