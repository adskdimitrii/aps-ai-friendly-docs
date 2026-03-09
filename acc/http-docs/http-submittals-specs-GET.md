# projects/{projectId}/specs

Source: https://aps.autodesk.com/en/docs/acc/reference/http/submittals-specs-GET/

---

Specs

GET

# projects/{projectId}/specs

Retrieve all the spec sections for the specified project. For information about spec sections, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Submittal_Spec_Sections).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/submittals/v2/projects/:projectId/specs |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | The maximum number of results per page. Possible values: `1`- `50`. Default value: `20`. For example, to limit the response to two results per page, use `limit=2`. |
| --- | --- |
| offset   int | The number of results to skip before starting to return data. For example, to skip the first 20 results, include `offset=20` in the query string. For more details, see the [JSON API Paging Help documentation](https://jsonapi.org/format/#fetching-pagination). |
| search   string | Search for spec sections by querying a specified string within specific fields (`identifier`, `title`), and retrieve the associated items that match the search criteria. This includes spec sections where the string matches part of a field. For example, search=1. |
| sort   string | Sort spec sections by specified fields. Separate multiple values with commas. To sort in descending or ascending order, add `desc` or `asc` after the sort criteria. For example, `identifier asc`. Possible values: `identifier`, `title`. |
| filter[identifier]   string | Filter spec sections with the specified spec section ID (the spec section ID in the UI). You can specify multiple values. Separate multiple values with commas. For example, `filter[identifier]=2.` |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful retrieval of spec sections |
| --- | --- |
| 403   Forbidden | Unauthorized |

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
| results   array: object | The list of spec sections. |
| id   string: UUID | The internal, globally unique identifier (UUID) for the spec section. |
| title   string | The title of the spec section. |
| identifier   string | The unique ID assigned to the spec section within the UI. |
| createdBy   string | The Autodesk ID of the user who created the spec section. |
| createdAt   datetime: ISO 8601 | The time and date when the spec section was created. |
| updatedBy   string | The Autodesk ID of the user who last updated the spec section. |
| updatedAt   datetime: ISO 8601 | The time and date when spec section was last updated. |

## [Example](#example)

Successful retrieval of spec sections

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/submittals/v2/projects/9eae7d59-1469-4389-bfb2-4114e2ba5545/specs' \
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
      "id": "e6111f96-8437-491e-a1ae-16fd53f0cbef",
      "title": "Materials",
      "identifier": "500",
      "createdBy": "WD43ZJGKDFLFH",
      "createdAt": "2018-02-01T12:09:24.198466Z",
      "updatedBy": "WD43ZJGKDFLFH",
      "updatedAt": "2018-02-01T12:09:24.198466Z"
    }
  ]
}

```

Show More
