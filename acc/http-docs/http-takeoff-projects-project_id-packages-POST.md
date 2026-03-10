# projects/{projectId}/packages

Source: https://aps.autodesk.com/en/docs/acc/reference/http/takeoff-projects-project_id-packages-POST/

---

Packages

POST

# projects/{projectId}/packages

Creates a takeoff package for a project.

Takeoff packages organize and contain all takeoff data related to a scope of work in your project.

For more information about takeoff packages, see the [ACC Takeoff - Working with Packages](https://help.autodesk.com/view/TAKEOFF/ENU/?guid=Work_with_Packages) help documentation.

Note that the Takeoff API does not currently support adding takeoff types and items to a takeoff package. You add takeoff types and items to a takeoff package in the UI.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/takeoff/v1/projects/{projectId}/packages |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| region   string | Specifies the region where the service is located. <br>Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>This corresponds to project ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/), and can be specified in the form of “UUID” or b.”UUID”.<br>To learn how to find the project ID, see the [Retrieve ACC Account and project ID](../how-to-docs/getting-started-retrieve-account-and-project-id.md) tutorial. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

| name*   string | The package name (user defined). <br>Corresponding UI name: `Title`.<br>Max length: 64 |
| --- | --- |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | Successfully created the takeoff package. |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource could not be found. |
| 409   Conflict | The package already exists in the project. |
| 429   Too Many Requests | Rate limit exceeded; wait some time before retrying. The ‘Retry-After’ header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (201)](#body-structure-201)

| name   string | The package name (user defined). <br>Corresponding UI name: `Title`.<br>Max length: 64 |
| --- | --- |
| id   string: UUID | The package ID. |
| createdAt   datetime: ISO 8601 | The date and time when the resource was created, in the following format: `YYYY-MM-DDThh:mm:ssZ`. |
| updatedAt   datetime: ISO 8601 | The date and time when the resource was last updated, in the following format: `YYYY-MM-DDThh:mm:ssZ`. |
| updatedByName   string | The name of the user who last updated the resource. |

## [Example](#example)

Successfully created the takeoff package.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/takeoff/v1/projects/:projectId/packages' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": "Concrete"
      }'

```

### Response

```
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "Concrete",
  "createdAt": "2019-08-24T14:15:22Z",
  "updatedAt": "2020-11-11T12:32:45Z",
  "updatedByName": "Jane Johnson"
}

```
