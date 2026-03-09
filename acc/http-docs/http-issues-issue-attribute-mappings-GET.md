# projects/{projectId}/issue-attribute-mappings

Source: https://aps.autodesk.com/en/docs/acc/reference/http/issues-issue-attribute-mappings-GET/

---

Issue Attribute Mappings

GET

# projects/{projectId}/issue-attribute-mappings

Retrieves information about the issue custom attributes (custom fields) that are assigned to issue categories and issue types.

We do not currently support adding custom fields to issues. For information about adding custom fields to issues categories and types, see the [help documentation](https://help.autodesk.com/view/DOCS/ENU/?guid=Issues_Types_Categories).

Note that by default, this endpoint only retrieves custom attributes that were directly assigned to the issue category or issue type. It does not retrieve inherited custom attributes.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/issues/v1/projects/{projectId}/issue-attribute-mappings |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-ads-region   string | The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. <br>Possible values: `US`, `EMEA`.<br>For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | The number of custom attribute mappings to return in the response payload. For example, `limit=2`. Acceptable values: `1-200`. Default value: `200`. |
| --- | --- |
| offset   int | The number of custom attribute mappings you want to begin retrieving results from. |
| filter[createdAt]   datetime: ISO 8601 | Retrieves items that were created at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03` or `2022-02-28T22:00:00.000Z..2022-03-28T22:00:00.000Z`Specific day: e.g., `2022-03-02` or `2022-02-28T22:00:00.000Z`Specific start date: e.g., `2022-03-02..` or `2022-02-28T22:00:00.000Z..`Specific end date: e.g., `..2022-03-02` or `..2022-02-28T22:00:00.000Z`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[updatedAt]   datetime: ISO 8601 | Retrieves items that were last updated at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03` or `2022-02-28T22:00:00.000Z..2022-03-28T22:00:00.000Z`Specific day: e.g., `2022-03-02` or `2022-02-28T22:00:00.000Z`Specific start date: e.g., `2022-03-02..` or `2022-02-28T22:00:00.000Z..`Specific end date: e.g., `..2022-03-02` or `..2022-02-28T22:00:00.000Z`<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[deletedAt]   datetime: ISO 8601 | Retrieves types that were deleted at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas. We support the following filtering options: <br>Date range: e.g., `2022-03-02..2022-03-03` or `2022-02-28T22:00:00.000Z..2022-03-28T22:00:00.000Z`Specific day: e.g., `2022-03-02` or `2022-02-28T22:00:00.000Z`Specific start date: e.g., `2022-03-02..` or `2022-02-28T22:00:00.000Z..`Specific end date: e.g., `..2022-03-02` or `..2022-02-28T22:00:00.000Z`<br>To include non-deleted items in the response, add `null` to the filter: `filter[deletedAt]=null,YYYY-MM-DDThh:mm:ss.sz...YYYY-MM-DDThh:mm:ss.sz`.<br>For more details, see [JSON API Filtering](http://jsonapi.org/format/#fetching-filtering). |
| filter[attributeDefinitionId]   string | Retrieves issue custom attribute mappings associated with the specified issue custom attribute definitions. Separate multiple values with commas. For example: `filter[attributeDefinitionId]=18ee5858-cbf1-451a-a525-7c6ff8156775`. |
| filter[mappedItemId]   string | Retrieves issue custom attribute mappings associated with the specified items (project, type, or subtype). Separate multiple values with commas. For example: `filter[mappedItemId]=18ee5858-cbf1-451a-a525-7c6ff8156775`. Note that this does not retrieve inherited custom attribute mappings or custom attribute mappings of descendants. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | List of issue attribute mappings |
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
| results   array: object | A list of issue attribute mappings. |
| id   string: UUID | The ID of the custom attribute mapping. |
| attributeDefinitionId   string: UUID | The ID of the custom attribute definition. |
| containerId   string: UUID | Not relevant |
| mappedItemType   enum:string | The type of item the custom attribute is mapped to. Possible values: `issueType` - this corresponds to `Issue Category` in the UI. `issueSubtype` - this corresponds to `Issue Type` in the UI. Note that `issueSubtype`'s inherit `issueType`'s. |
| mappedItemId   string: UUID | The ID of the item (type, or subtype) the custom attribute is mapped to. |
| order   int | The order that the custom attributes were mapped to the item (type, subtype). This is only relevant to non-inherited mappings. |
| permittedActions   array: string | Not relevant |
| permittedAttributes   array: string | Not relevant |
| createdAt   datetime: ISO 8601 | The date and time the custom attribute mapping was created, in the following format: YYYY-MM-DDThh:mm:ss.sz. |
| createdBy   string | The Autodesk ID of the user who created the custom attribute mapping. |
| updatedAt   datetime: ISO 8601 | The last date and time the custom attribute mapping was updated, in the following format: YYYY-MM-DDThh:mm:ss.sz. |
| updatedBy   string | The Autodesk ID of the user who last updated the custom attribute mapping. |
| deletedAt   datetime: ISO 8601 | The date and time the custom attribute mapping was deleted, in the following format: YYYY-MM-DDThh:mm:ss.sz. |
| deletedBy   string | The Autodesk ID of the user who deleted the custom attribute mapping. |

## [Example](#example)

List of issue attribute mappings

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/:projectId/issue-attribute-mappings' \
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
      "attributeDefinitionId": "1110f111-6c54-4b01-90e6-d701748f1333",
      "containerId": "2220f222-6c54-4b01-90e6-d701748f0222",
      "mappedItemType": "issueType",
      "mappedItemId": "2220f222-6c54-4b01-90e6-d701748f0222",
      "order": 2,
      "permittedActions": [
        "delete"
      ],
      "permittedAttributes": [
        ""
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
