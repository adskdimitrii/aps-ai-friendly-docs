# projects/{projectId}/packages

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-packages-GET/

---

Packages

GET

# projects/{projectId}/packages

Retrieve all the packages for the specified project. For information about packages, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittal_Packages).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/packages |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | The maximum number of results per page. Possible values: `1`- `50`. Default value: `20`. For example, to limit the response to two results per page, use `limit=2`. |
| --- | --- |
| offset   int | The number of results to skip before starting to return data. For example, to skip the first 20 results, include `offset=20` in the query string. For more details, see the [JSON API Paging Help documentation](https://jsonapi.org/format/#fetching-pagination). |
| sort   string | Sort packages by specified fields. Separate multiple values with commas. To sort in descending or ascending order, add `desc` or `asc` after the sort criteria. For example, `spec asc`. <br>Possible values: `id`, `identifier`, `title`, `description`, `spec`, `spec.identifier`. |
| filter[identifier]   string | Filter packages with the specified package ID (the package ID in the UI). You can specify multiple values. Separate multiple values with commas. For example, `filter[identifier]=2`. |
| filter[title]   string | Filter packages with the specified title. You can specify multiple values. Separate multiple values with commas. For example, `filter[title]=Structural Steel`. |
| filter[specId]   string | Filter packages with the associated specified spec section internal, globally unique ID (UUID). You can specify multiple values. Separate multiple values with commas. For example, `filter[specId]=b4aa3864-5706-4a7b-b06c-a792e8b2df23`. |
| filter[spec.identifier]   string | Filter packages with the associated specified section ID (the spec section ID in the UI). You can specify multiple values. Separate multiple values with commas. For example, `filter[identifier]=2`. |
| search   string | Search for packages by querying a specified string within specific fields (`identifier`, `title`, `spec.identifier`), and retrieve the associated packages that match the search criteria. This includes packages where the string matches part of a field. For example, `search=1`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful retrieval of packages |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request headers. |
| 401   Unauthorized | Invalid or missing authorization header. Verify the Bearer token and try again. |
| 403   Forbidden | The user is not authorized to perform this action. |
| 404   Not Found | The specified resource was not found. |
| 500   Internal Server Error | An unexpected error occurred on the server while processing the request. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| pagination   object | Describes pagination details for the response, including information about the current page and navigation to other pages. |
| --- | --- |
| limit   int | The maximum number of results to be displayed on each page. |
| offset   int | The number of results skipped before starting the current page. |
| totalResults   int | The overall count of results available across all pages. |
| previousUrl   string | The URL to retrieve the preceding page of results, if applicable. Not returned on the first page of results. |
| nextUrl   string | The URL to retrieve the subsequent page of results, if available. If not included, this is the last page of data. |
| results   array: object | The list of packages. |
| id   string: UUID | The internal, globally unique identifier (UUID) for the package. |
| specId   string: UUID | The internal, globally unique identifier (UUID) of the spec associated with the package. |
| title   string | The title of the package. |
| identifier   int | The unique ID assigned to the package within the UI. |
| description   string | The description of the package. |
| specIdentifier   string | The unique ID of the spec assigned to the package in the UI, specific to each project. |
| permittedActions   array: object | The list of actions the user is allowed to perform on the submittal item. |
| id   string | The ID of the action in the format `type_of_object::action`. For example, `Item::retrieve`. |
| fields   object | A list of field names for which values must be provided when performing the action. An empty array indicates no specific set of values. |
| mandatoryFields   array: string | Lists the fields that are required when updating a submittal item. <br>The required fields depend on the action being performed, the itemâs current state, and the userâs role.<br>For example:<br>To transition the state of a submittal item, `stateId` and `responseId` are required. To reassign the manager, `manager` and `managerType` are required. To modify the spec section, `specId` is required. |
| transitions   array: object | The list of possible state transitions for a submittal item within the review workflow. |
| id   string | The ID of the transition in the format `from-state::to-state`. For example, `create::mgr-1`, `mgr-1::mgr-2`, `rev::void`. |
| name   string | The descriptive name of the transition. For example, `Create`, `Send to Manager`, `Send to void`. |
| stateFrom   object | The starting state of the transition, representing the current position of the submittal item in the workflow. |
| id   string | The unique ID of the starting state. For example, `create`, `mgr-1`, `rev`. The `rev` state indicates that the submittal item is currently under review. |
| name   string | The name of the starting state. For example, `Create`, `Manager Review`, `Review`. |
| stateTo   object | The target state of the transition, indicating the next position of the submittal item in the workflow. |
| id   string | The unique ID of the target state. For example, `mgr-1`, `mgr-2`, `void`. |
| name   string | The name of the target state. For example, `Manager Review`, `Manager Final Review`, `Void`. |
| transitionFields   array: string | Fields that are used in the transition. For example, [`subcontractor`, `subcontractorType`, `watchers`, `responseId`]. |
| mandatoryFields   array: string | A list of required fields for the transition. For example, [`responseId`]. |
| actionId   string | Not relevant |

## [Example](#example)

Successful retrieval of packages

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/packages' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 10,
    "offset": 100,
    "totalResults": 25,
    "previousUrl": "https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/settings/mappings?offset=10&limit=100",
    "nextUrl": null
  },
  "results": [
    {
      "id": "e8302552-fc5a-42ac-ba4b-e9de9760c356",
      "specId": "e6111f96-8437-491e-a1ae-16fd53f0cbef",
      "title": "my package1",
      "identifier": 222,
      "description": "Electrical specifications",
      "specIdentifier": "A-500",
      "permittedActions": [
        {
          "id": "Item::update",
          "fields": {
            "subcontractor": [],
            "manager": []
          },
          "mandatoryFields": [
            ""
          ],
          "transitions": [
            {
              "id": "rev::void",
              "name": "Send to void",
              "stateFrom": {
                "id": "rev",
                "name": "Review"
              },
              "stateTo": {
                "id": "void",
                "name": "Void"
              },
              "transitionFields": [
                "subcontractor",
                "subcontractorType",
                "watchers",
                "responseId"
              ],
              "mandatoryFields": [
                "responseId"
              ],
              "actionId": "ITEM_TRANSITION_REV_VOID"
            }
          ]
        }
      ]
    }
  ]
}

```

Show More
