# projects/{projectId}/sheets

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-sheets-GET/

---

Sheets

GET

# projects/{projectId}/sheets

Retrieves information about the sheets in a project.

By default, this endpoint only returns sheets with the newest issuance date (this includes future issuance dates).

To return all the sheets in a project, set the `currentOnly` filter to `false`.

To return sheets from a specific version set, use the version set ID filter (`filter[versionSetId]`).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/sheets |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-user-id   string | The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. <br>When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.<br>You can use either the user’s ACC ID (id), or their Autodesk ID (autodeskId). |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](../how-to-docs/getting-started-retrieve-account-and-project-id.md). You can use a project ID either with a “b.” prefix or without a “b.” prefix. For instance, a project ID of “b.a4be0c34a-4ab7” can also be referred to as “a4be0c34a-4ab7”. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| currentOnly   boolean | `true` to only return versions of the sheets with the newest issuance date (this includes future issuance dates). This is only relevant if you uploaded multiple versions of the same sheet that were assigned the same number identifier. If you do not assign a value to the version set ID filter (`filter[versionSetId]`) this defaults to `true`.`false` to return all sheets in the project.<br>If you specify a value for the version set ID filter (`filter[versionSetId]`) this defaults to `false`. If you do not specify a version set, the default is `true`. |
| --- | --- |
| filter[versionSetId]   string | Filter sheets by the version set ID. If you assign a value to this filter, `currentOnly` defaults to `false`. If you do not assign a value, `currentOnly` default to `true`. |
| filter[tags]   string | Filter sheets by tags. You can filter by multiple tags. For example, `filter[tags]=architecture&filter[tags]=structure` returns sheets that include both `architecture` and `structure` tags. <br>Use `filter[tags]=__UNTAGGED` to only return sheets without any tags. |
| fields   string | Specify which attributes you want to appear in the response. You can specify multiple attributes. For example, to only return the sheet ID and sheet number in the response, use `fields=id&fields=number`. |
| searchText   string | Search for sheets with the specified text. The API only searches in the `number` and `title` attributes. You can specify a string or part of a string. The search is case sensitive. You can only use one search string per call. For example, `searchText=kitchen`. |
| withAllTags   boolean | `true` to return sheets that contain all search tags.`false` to return sheets that contain at least one tag.<br>If `filter[tags]=__UNTAGGED` is already in query parameters, `withAllTags` does not work. |
| isDeleted   boolean | `true` to only return deleted sheets.`false` to only return non-deleted sheets.<br>The default value is `false`. You cannot retrieve both deleted and non-deleted sheets in one call. |
| offset   int | The starting point for the results, specified by item number. The default value is `0`. For example, use `offset=3` to start the results from the third item. |
| limit   int | The number of results to return in the response. Acceptable values: `1`-`100`. Default value: `100`. |
| collectionId   string | Filter by sheet collection. If not provided, only results in the ungrouped collection are returned. <br>Possible values:<br>The UUID of an existing collection: Returns only the results within that collection.`*` Returns results from all collections. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the list of sheets. |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 403   Forbidden | The user or client represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource cannot be found. |
| 429   Too Many Requests | The server has received too many requests. |
| 500   Internal Server Error | An unexpected error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | The list of results. |
| --- | --- |
| id   string: UUID | The ID of the sheet. |
| number   string | The number of the sheet. |
| versionSet   object | Basic version set data. For a complete collection of version set data, call [GET version-sets](http-sheets-version-sets-GET.md). |
| id   string: UUID | The ID of the version set. |
| name   string | The name of the version set. <br>Max length: 255 |
| issuanceDate   datetime: ISO 8601 | The issuance date of the version set in ISO-8601 format (YYYY-MM-DD). |
| deleted   boolean | `true` if the version set has been deleted.`false` if the version set has not been deleted. |
| createdAt   datetime: ISO 8601 | The time when the sheet was created, in ISO-8601 format (YYYY-MM-DDTHH:mm:ss.SSSZ). |
| createdBy   string | The ID of the user who created the sheet. |
| createdByName   string | The name of the user who created the sheet. |
| updatedAt   datetime: ISO 8601 | The time when the sheet was last updated, in ISO-8601 format (YYYY-MM-DDTHH:mm:ss.SSSZ). |
| updatedBy   string | The ID of the user who last updated the sheet. |
| updatedByName   string | The name of the user who last updated the sheet. |
| title   string | The title of the sheet. |
| uploadFileName   string | The name of the source file from which the sheet was generated. |
| uploadId   string: UUID | The ID of the upload that generated the sheet. |
| tags   array: string | The tags of the sheet. |
| paperSize   array: number | The size of the sheet in pixels. |
| isCurrent   boolean | `true` if the sheet is the version with the most recent issuance date. This is only relevant if you uploaded multiple versions of the same sheet that were assigned the same number. The `current` sheet is the sheet with the most recent issuance date.`false` if the sheet is not the version with the most recent issuance date. |
| deleted   boolean | `true` if the sheet has been deleted.`false` if the sheet has not been deleted. |
| deletedAt   datetime: ISO 8601 | The time when the sheet was deleted, in ISO-8601 format (YYYY-MM-DDTHH:mm:ss.SSSZ). |
| deletedBy   string | The ID of the user who deleted the sheet. |
| deletedByName   string | The name of the user who deleted the sheet. |
| viewable   object | Information about the sheet relevant for loading the sheet to the Viewer. See [Add Viewer to an HTML Page](https://forge.autodesk.com/en/docs/viewer/v7/developers_guide/viewer_basics/) for more information. |
| urn   string | The URN of the viewable resources. Multiple sheets created by the same original file may share the same viewable URN. <br>When loading the sheet to the viewer, this URN should be used as the documentId to get the manifest. |
| guid   string | The GUID of the viewable resources. <br>When loading the sheet to the viewer, this GUID should be used to find the related geometry node of the sheet. |
| collection   object | The collection object, if assigned. If no collection is assigned, this value is `null`. |
| id   string: UUID | The unique identifier of the collection. |
| name   string | The name of the collection. This corresponds to the Name column in the ACC Sheets Collections Settings UI. <br>Max length: 255 |
| pagination   object | Pagination information for paged data. |
| limit   int | The number of results to return in the response. |
| offset   int | The item number from which the results begin. |
| previousUrl   string | The URL for the previous page of results. |
| nextUrl   string | The URL for the next page of results. |
| totalResults   int | The total number of results available. |

## [Example](#example)

Successfully retrieved the list of sheets.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/sheets?currentOnly=true&filter[versionSetId]=7c2ecde0-2406-49f9-9199-50176848a0b7&filter[tags]=floor' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "results": [
    {
      "id": "0d7a5883-1694-3078-a06d-ad24413f8b06",
      "number": "A-01",
      "versionSet": {
        "id": "7c2ecde0-2406-49f9-9199-50176848a0b7",
        "name": "one set",
        "issuanceDate": "2021-07-01",
        "deleted": false
      },
      "createdAt": "2021-07-01T05:21:05.391Z",
      "createdBy": "45GPJ4KAX789",
      "createdByName": "John Smith",
      "updatedAt": "2021-07-01T05:21:05.391Z",
      "updatedBy": "45GPJ4KAX789",
      "updatedByName": "John Smith",
      "title": "Floor One",
      "uploadFileName": "example.pdf",
      "uploadId": "5cb5d9da-060e-421e-bca9-97dd8b5cd800",
      "tags": [
        "april",
        "floor"
      ],
      "paperSize": [
        1000,
        600
      ],
      "isCurrent": true,
      "deleted": false,
      "deletedAt": "",
      "deletedBy": "",
      "deletedByName": "",
      "viewable": {
        "urn": "urn:adsk.bimdocs:seed:207edb73-69c2-43d2-ba0e-e2ffe9fdcb56",
        "guid": "cc3eb847-737f-3408-bdbd-e2628a02b8de"
      },
      "collection": {
        "id": "619ef887-974f-45e4-9775-461e6a62d784",
        "name": "Group 1"
      }
    }
  ],
  "pagination": {
    "limit": 100,
    "offset": 0,
    "previousUrl": "",
    "nextUrl": "",
    "totalResults": 1
  }
}

```

Show More
