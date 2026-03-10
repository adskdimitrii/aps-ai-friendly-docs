# projects/{projectId}/packages

Source: https://aps.autodesk.com/en/docs/acc/reference/http/packages-list-packages-GET/

---

List packages

GET

# projects/{projectId}/packages

Retrieves a list of all packages within a specified ACC project.

With two-legged authentication, returns all packages in the project. With two-legged authentication and the `x-user-id` header, or with three-legged authentication, returns only the packages that the specified or current user has permission to access.

For information about creating packages, see the [Create Packages](https://help.autodesk.com/view/BUILD/ENU/?guid=Create_Packages) documentation.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/packages/v1/projects/{projectId}/packages |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-user-id   string | The Autodesk ID of the user on whose behalf the request is made. <br>This header is required only when using two-legged authentication. It is not needed for three-legged authentication.<br>Your application can access only those users who are assigned to it in the SaaS Integrations UI.<br>Only user Autodesk IDs (`autodeskId`) are supported. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>You can retrieve the project ID using the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/). For more details, see the [Retrieve a Project ID](../how-to-docs/getting-started-retrieve-account-and-project-id.md) tutorial.<br>You may provide the project ID with or without the `b.` prefix:<br>With prefix: `b.657a5565-09b7-48e0-bd03-acacfe42efaf`Without prefix: `657a5565-09b7-48e0-bd03-acacfe42efaf` |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | The number of packages to return in the response payload. <br>Possible values: `1-200`. Default: `200`. For example: `limit=2`. |
| --- | --- |
| offset   int | The number of packages that you want to begin retrieving results from. <br>Default: `0`. For example: `offset=10` |
| filter[createdBy]   string | Filters results by the Autodesk ID of the users who created the packages. <br>You can provide a single Autodesk ID or a comma-separated list of IDs. |
| filter[updatedBy]   string | Filters results by the Autodesk ID of the users who last updated the packages. <br>You can provide a single Autodesk ID or a comma-separated list of IDs.<br>To find the IDs call [GET users](http-admin-projectsprojectId-users-GET.md) |
| filter[createdAt]   string | Filter packages by their creation time. Use an ISO 8601 date-time range in the format `startDate..endDate`. <br>Either date may be omitted to specify an open-ended range.<br>Examples:<br>After a specific time: `2025-03-26T16:00:00.000Z..`Before a specific time: `..2025-03-28T15:59:59.999Z`Between two times: `2025-03-26T16:00:00.000Z..2025-03-28T15:59:59.999Z` |
| filter[updatedAt]   string | Filter packages by their last update time. Use an ISO 8601 date-time range in the format `startDate..endDate`. <br>Either date may be omitted to specify an open-ended range.<br>Examples:<br>After a specific time: `2025-03-26T16:00:00.000Z..`Before a specific time: `..2025-03-28T15:59:59.999Z`Between two times: `2025-03-26T16:00:00.000Z..2025-03-28T15:59:59.999Z` |
| sort   enum:string | Sorts the results by a supported field. <br>By default, results are sorted in ascending (`asc`) order. To sort in descending order, add `desc` after the field name.<br>Format: `sort=fieldName [desc]`<br>Possible values: `name`, `createdAt`, `updatedAt`, `displayId`,<br>Examples:<br>Sort by name (ascending): `sort=name`Sort by creation time (descending): `sort=createdAt desc` |
| filter[versionType]   enum:string | Filters results by the version type of the packages. <br>Possible values:<br>`FIXED` – Files in the package remain fixed at selected versions.`CURRENT` – Files in the package automatically update to the latest current versions.<br>For more details, see the [Flexible Package Types](https://help.autodesk.com/view/BUILD/ENU/?guid=File_Packages_Docs) documentation. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved a list of packages |
| --- | --- |
| 400   Bad Request | Bad request. The input parameters were invalid. |
| 403   Forbidden | Forbidden. The user does not have permission to access this resource. |
| 404   Not Found | Not found. The resource does not exist or is inaccessible. |
| 500   Internal Server Error | An unexpected server error occurred. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | The list of results. |
| --- | --- |
| id   string: UUID | The unique identifier (UUID) of the package. |
| displayId   int | The display ID of the package. |
| name   string | The name of the package. <br>Max length: 255 |
| description   string | The description of the package. <br>Max length: 2048 |
| createdAt   datetime: ISO 8601 | The time the package was created. |
| createdBy   string | The Autodesk ID of the user who created the package. For details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md). |
| updatedAt   datetime: ISO 8601 | The time the package was last updated. |
| updatedBy   string | The Autodesk ID of the user who last updated the package. For details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md). |
| locked   boolean | `true`: The package is locked. Its contents cannot be modified until it is unlocked. <br>`false`: The package is not locked. Files and resources can still be added, removed, or updated. |
| lockedBy   string | The Autodesk ID of the user who locked the package. For details about the user, call [GET users](http-admin-projectsprojectId-users-GET.md). |
| lockedAt   datetime: ISO 8601 | The time the package was locked. |
| resourceCount   int | The number of resources in the package. |
| versionType   object | The version type of the package. <br>Possible values:  > `FIXED` – The files in the package remain fixed at the selected versions.`CURRENT` – The files in the package automatically update to the latest current versions.`CHANGING` – The package is temporarily changing from one version type to another. This state usually lasts only a few seconds and cannot be used as a filter.<br>For more details, see the [Change Package Version Type](https://help.autodesk.com/view/BUILD/ENU/?guid=View_Manage_Packages#change-package-version-type) documentation. |
| pagination   object | The pagination information for the response. This object is included when results are returned in multiple pages. |
| limit   int | The maximum number of objects that may be returned in the page. |
| offset   int | The offset from the start of the collection to the first entry in the page. It is zero-based. |
| nextUrl   string | The URL to retrieve the next page of results. If not included, this is the last page of results. |
| totalResults   int | The total number of results that match the query, regardless of the `limit` value. |

## [Example](#example)

Successfully retrieved a list of packages

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/packages/v1/projects/657a5565-09b7-48e0-bd03-acacfe42efaf/packages?limit=200&filter[createdBy]=L9VDREARJ7X2,9NGKQKPXAUHG&filter[updatedBy]=L9VDREARJ7X2,9NGKQKPXAUHG&filter[createdAt]=2025-03-26T16:00:00.000Z..2025-03-28T15:59:59.999Z&filter[updatedAt]=2025-03-26T16:00:00.000Z..2025-03-28T15:59:59.999Z&sort=name&filter[versionType]=FIXED' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "results": [
    {
      "id": "c25d1273-41e3-4e04-be1e-f4c1ba809d14",
      "displayId": 8642,
      "name": "Milestones",
      "description": "This package contains all the files related to the milestones.",
      "createdAt": "2025-03-27T01:28:28.272Z",
      "createdBy": "L9VDREARJ7X2",
      "updatedAt": "2025-03-27T03:25:48.884Z",
      "updatedBy": "L9VDREARJ7X2",
      "locked": true,
      "lockedBy": "L9VDREARJ7X2",
      "lockedAt": "2025-03-27T03:25:48.884Z",
      "resourceCount": 2,
      "versionType": "FIXED"
    }
  ],
  "pagination": {
    "limit": 200,
    "offset": 0,
    "nextUrl": "https://developer.api.autodesk.com/construction/packages/v1/projects/657a5565-09b7-48e0-bd03-acacfe42efaf/packages?limit=200&offset=400",
    "totalResults": 8618
  }
}

```

Show More
