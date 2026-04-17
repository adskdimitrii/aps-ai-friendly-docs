# projects/{projectId}/issue-attribute-definitions

Source: https://aps.autodesk.com/en/docs/acc/reference/http/issues-issue-attribute-definitions-GET/

---

Issue Attribute Definitions

GET

# projects/{projectId}/issue-attribute-definitions

Retrieves information about issue custom attributes (custom fields) for a project, including the custom attribute title, description and type.

For example, the possible values for a dropdown list, the IDs, the names and whether the attribute is visible.

Note that custom attributes are known as **custom fields** in the Forma UI.

For information about creating issue custom attributes for a project, see the [help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Issues_Custom_Fields).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/issues/v1/projects/{projectId}/issue-attribute-definitions |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

- Authorization*string Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context.
- x-ads-regionstring The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: `US`, `EMEA`.For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page.

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the Forma API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | The number of custom attribute definitions to return in the response payload. For example, `limit=2`. Acceptable values: `1-200`. Default value: `200`. |
| --- | --- |
| offset   int | The number of custom attribute definitions you want to begin retrieving results from. |
| filter[createdAt]   datetime: ISO 8601 | Retrieves items that were created at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03` or `2022-02-28T22:00:00.000Z..2022-03-28T22:00:00.000Z`Specific day: e.g., `2022-03-02` or `2022-02-28T22:00:00.000Z`Specific start date: e.g., `2022-03-02..` or `2022-02-28T22:00:00.000Z..`Specific end date: e.g., `..2022-03-02` or `..2022-02-28T22:00:00.000Z`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[updatedAt]   datetime: ISO 8601 | Retrieves items that were last updated at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03` or `2022-02-28T22:00:00.000Z..2022-03-28T22:00:00.000Z`Specific day: e.g., `2022-03-02` or `2022-02-28T22:00:00.000Z`Specific start date: e.g., `2022-03-02..` or `2022-02-28T22:00:00.000Z..`Specific end date: e.g., `..2022-03-02` or `..2022-02-28T22:00:00.000Z`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[deletedAt]   datetime: ISO 8601 | Retrieves types that were deleted at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03` or `2022-02-28T22:00:00.000Z..2022-03-28T22:00:00.000Z`Specific day: e.g., `2022-03-02` or `2022-02-28T22:00:00.000Z`Specific start date: e.g., `2022-03-02..` or `2022-02-28T22:00:00.000Z..`Specific end date: e.g., `..2022-03-02` or `..2022-02-28T22:00:00.000Z`<br>To include non-deleted items in the response, add `null` to the filter: `filter[deletedAt]=null,YYYY-MM-DDThh:mm:ss.sz...YYYY-MM-DDThh:mm:ss.sz`.<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[dataType]   enum:string | Retrieves issue custom attribute definitions with the specified data type. Possible values: `list` (this corresponds to `dropdown` in the UI), `text`, `paragraph`, `numeric`. For example, `filter[dataType]=text,numeric`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | List of issue attribute definitions |
| --- | --- |
| 400   Bad Request | Invalid input |
| 403   Forbidden | Unauthorized |
| 404   Not Found | Project not found |
| 500   Internal Server Error | Internal server error |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| pagination   object | The pagination object. |
| --- | --- |
| limit   int | The number of items per page. |
| offset   int | The page number that the results begin from. |
| totalResults   int | The number of items in the response. |
| results   array: object | A list of issue attribute definitions (custom fields). |
| id   string: UUID | The ID of the custom attribute. |
| containerId   string: UUID | Not relevant |
| title   string | The title of the custom attribute. <br>Max length: 100 |
| description   string | The description of the custom attribute. <br>Max length: 500 |
| dataType   enum:string | The type of custom attribute. Possible values: `list`, `text`, `paragraph`, `numeric`. |
| metadata   object | The metadata object; only relevant for `list` custom attributes. |
| list   object | The list object. |
| options   array: object | The options object. |
| id   string: UUID | The id of the list option. |
| value   string | The value of the list item. |
| permittedActions   array: string | Not relevant |
| permittedAttributes   array: string | Not relevant |
| createdAt   datetime: ISO 8601 | The date and time the custom attribute was created, in the following format: YYYY-MM-DDThh:mm:ss.sz. |
| createdBy   string | The Autodesk ID of the user who created the custom attribute. |
| updatedAt   datetime: ISO 8601 | The last date and time the custom attribute was updated, in the following format: YYYY-MM-DDThh:mm:ss.sz. |
| updatedBy   string | The Autodesk ID of the user who last updated the custom attribute. |
| deletedAt   datetime: ISO 8601 | The date and time the custom attribute was deleted, in the following format: YYYY-MM-DDThh:mm:ss.sz. |
| deletedBy   string | The Autodesk ID of the user who deleted the custom attribute. |

## [Example](#example)

List of issue attribute definitions

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/:projectId/issue-attribute-definitions' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 10,
    "offset": 100,
    "totalResults": 25
  },
  "results": [
    {
      "id": "1110f111-6c54-4b01-90e6-d701748f1111",
      "containerId": "2220f222-6c54-4b01-90e6-d701748f0222",
      "title": "Velocity",
      "description": "How long will it take for this issue to be resolved.",
      "dataType": "list",
      "metadata": {
        "list": {
          "options": [
            {
              "id": "802b87e0-60f6-4b1b-9cdf-37b53c731f17",
              "value": "option a"
            },
            {
              "id": "999b77e0-60f6-4b1b-9cdf-37b53c431f22",
              "value": "option b"
            }
          ]
        }
      },
      "permittedActions": [
        "edit"
      ],
      "permittedAttributes": [
        "title"
      ],
      "createdAt": "2018-07-22T15:05:58.033Z",
      "createdBy": "A3RGM375QTZ7",
      "updatedAt": "2018-07-22T15:05:58.033Z",
      "updatedBy": "A3RGM375QTZ7",
      "deletedAt": "2018-07-22T15:05:58.033Z",
      "deletedBy": "A3RGM375QTZ7"
    }
  ]
}

```

Show More
