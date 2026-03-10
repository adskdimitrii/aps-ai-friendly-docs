# projects/{projectId}/classification-systems

Source: https://aps.autodesk.com/en/docs/acc/reference/http/takeoff-projects-project_id-classification-systems-GET/

---

Classification Systems

GET

# projects/{projectId}/classification-systems

Retrieves high-level details of the classification systems for a project.

A classification system categorizes and organizes construction information in a hierarchical structure, and is used to label items in a takeoff project.

For more information about the classification system, see the [ACC Configure Takeoff Settings](https://help.autodesk.com/view/TAKEOFF/ENU/?guid=Configure_Takeoff_Settings) help documentation.

To find the hierarchy of a specific classification system, call [GET classifications](http-takeoff-projects-project_id-classification-systems-system_id-classifications-GET.md).

To learn how this endpoint is used, see the [Takeoff Extract Inventory](../how-to-docs/takeoff-takeoff-extract-inventory.md) tutorial.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/takeoff/v1/projects/{projectId}/classification-systems |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| region   string | Specifies the region where the service is located. <br>Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>This corresponds to project ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/), and can be specified in the form of “UUID” or b.”UUID”.<br>To learn how to find the project ID, see the [Retrieve ACC Account and project ID](../how-to-docs/getting-started-retrieve-account-and-project-id.md) tutorial. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| offset   int | The classification system index from which the pagination starts. This is zero-based. |
| --- | --- |
| limit   int | The maximum number of classification systems per page. <br>Acceptable values: `1-200`.<br>Default value: `200`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the classification systems. |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource could not be found. |
| 429   Too Many Requests | Rate limit exceeded; wait some time before retrying. The ‘Retry-After’ header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| pagination   object | The pagination object. |
| --- | --- |
| limit   int | The maximum number of objects per page. |
| nextUrl   string | The URL path that returns the next page of data. |
| offset   int | The object number from which the pagination starts. This is zero-based. |
| results   array: object | A list of classification systems for the project. |
| id   string: UUID | The classification system ID. |
| name   string | The classification system name. <br>Max length: 200 |
| type   enum:string | The type of classification system. <br>Possible values: `CLASSIFICATION_SYSTEM_1`, `CLASSIFICATION_SYSTEM_2`.<br>See the [Help documentation](https://help.autodesk.com/view/TAKEOFF/ENU/?guid=Configure_Takeoff_Settings) for more details about the classification systems. |

## [Example](#example)

Successfully retrieved the classification systems.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/takeoff/v1/projects/:projectId/classification-systems?limit=10' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 100,
    "nextUrl": "https://developer.api.autodesk.com/construction/takeoff/v1/resources?limit=100&offset=200",
    "offset": 100
  },
  "results": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "Smith Construction Classification",
      "type": "CLASSIFICATION_SYSTEM_1"
    }
  ]
}

```

Show More
