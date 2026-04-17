# v1/projects/{projectId}/forms/{formId}/table/{fieldId}/values

Source: https://aps.autodesk.com/en/docs/acc/reference/http/forms-get-table-values-GET/

---

Get table values

GET

# v1/projects/{projectId}/forms/{formId}/table/{fieldId}/values

Returns all row values from a specific table in a form.

This endpoint allows you to retrieve tabular data from forms, including work log entries, materials entries, equipment entries, and custom tables.

The `fieldId` path parameter is the table’s schema identifier (UUID). Each row in the response will include both `schema` and `fieldId` fields that match this identifier.

**Column Types**

Custom tables support multiple column types. Each cell value uses a type-specific field:
- `textVal`: Text values
- `numberVal`: Decimal numbers
- `integerVal`: Whole numbers
- `arrayVal`: Dropdown/multi-select choices
- `uidVal`: Reference IDs (companies, roles)
- `svgVal`: Signatures (base64 SVG)
- `dateVal`: Dates (YYYY-MM-DD)
- `timeVal`: Times (HH:MM:SS)
- `timespanVal`: Duration in milliseconds

Use [GET section](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-sections-sectionId-(Beta/)-GET/) to see each column’s `columnType` and determine which value field to read.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/table/:fieldId/values |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). <br>The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the Forma API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |
| formId   string | The unique identifier of the form. <br>Use [GET forms](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-forms-(Deprecated/)-GET/) to retrieve the form ID. |
| fieldId   string | The table’s schema identifier (UUID). This corresponds to the `schema` and `fieldId` fields returned in each row of the response. <br>For built-in tables, use the following UUIDs: - Work Log: `6c8055d5-1301-46f6-9d18-8a2a208a277e` - Materials: `2adf5ad9-d9d3-ee42-6fd8-015c34ce474d` - Equipment: `8af6c450-dd2a-32ae-0090-5493a9cc884e`<br>For custom tables, the schema identifier can be found in the section detail. Use [GET section](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-sections-sectionId-(Beta/)-GET/) to retrieve the section, then look for `schema` fields on table section items. |

### Request

## [Query String Parameters](#query-string-parameters)

| offset   int | The number of records to skip before returning the result records. Defaults to 0. Increase this value in subsequent requests to continue getting results when the number of records exceeds the requested limit. |
| --- | --- |
| limit   int | The number of records to return in a single request. Can be a number between 1 and 50. Defaults to 50. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Table values from the form. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request header |
| 401   Unauthorized | The request was not accepted because it lacked valid authentication credentials |
| 403   Forbidden | The request was not accepted because the client is authenticated, but is not authorized to access the target resource |
| 404   Not Found | The resource cannot be found. This is returned when the form does not exist, the `fieldId` does not correspond to a valid table in the form’s layout, or the user does not have access to the form. |
| 429   Too Many Requests | The request could not be completed due to the rate limit of the target resource |
| 500   Internal Server Error | The request could not be completed due to an internal server error |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| data   array: object | List of table rows. |
| --- | --- |
| id   string: UUID | Unique identifier for this table row. Each column value in the `columns` array references this ID via its `formValueId` field. |
| table   enum:string | Built-in table identifier. If it is not provided, the table will be a custom table identified by the `schema` field. Possible values: `worklogEntries`, `materialsEntries`, `equipmentEntries` |
| schema   string: UUID | The table’s schema identifier (UUID). This is the legacy field name, retained for backwards compatibility. Use `fieldId` for new integrations. <br>This value corresponds to the `fieldId` path parameter used to query this table. |
| fieldId   string: UUID | The table’s schema identifier (UUID). This is the preferred field name that matches the `fieldId` path parameter. <br>Historically, tables were identified by a field called `schema`, which caused confusion with database schema concepts. The `fieldId` field provides a clearer name while `schema` is retained for backwards compatibility. Both fields contain the same UUID value. |
| rank   int | The sort order in the table. |
| deleted   boolean | Whether the table row has been deleted or not. |
| columns   array: object | The list of cell values in this row. Each item represents the value at the intersection of this row and a specific column (i.e., a table cell). Each cell contains `formValueId` (matching this row’s `id`) and `columnId` (identifying which column). |
| formValueId   string: UUID | The row identifier (matches the parent `TabularValueRow.id`). This is repeated in each cell to enable independent cell storage and sparse table support. Think of it as the ‘rowId’ portion of a cell’s coordinate. |
| columnId   string: UUID | The column identifier from the form’s layout. Think of it as the ‘columnId’ portion of a cell’s coordinate. This corresponds to the `uid` of a column in the table’s `columns` array in the section detail. <br>Use [GET section](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-sections-sectionId-(Beta/)-GET/) to retrieve the section and find column definitions with their `uid`, `columnKey`, `label`, and `columnType`. |
| columnName   string | The name (columnKey) of the column. For built-in tables, this is one of the predefined column keys (e.g., `trade`, `headcount`, `description`). For custom tables, this is the user-defined column key. |
| textVal   string | Text value. |
| numberVal   number | Number value. |
| integerVal   int | Integer value. |
| arrayVal   array: string | Array value. |
| timespanVal   int | Amount of time in milliseconds. |
| svgVal   string | SVG value. |
| uidVal   string | UUID value. |
| datetimeLocalVal   string | Datetime value in local time. |
| datetimeUtcVal   string | Datetime value in UTC. |
| timezoneVal   string | Timezone identifier. |
| timezoneRulesVal   string | Timezone rules data. |
| lngVal   number | Longitude value. |
| latVal   number | Latitude value. |
| dateVal   string | Date without timezone. |
| timeVal   string | Time without timezone. |
| updatedAt   datetime: ISO 8601 | The date when the table row was last updated, UTC date and time in ISO-8601 format. |
| updatedBy   string | User ID that last updated the table row. |
| pagination   object | Request pagination information. |
| offset   int | Number of items skipped. |
| limit   int | Number of items returned per page. |
| totalResults   int | Total number of items that can be returned. |
| nextUrl   string | URL for the next page of items. Next page url is null on the last page. |

## [Example](#example)

Table values from the form.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/table/:fieldId/values' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "data": [
    {
      "id": "28a31f14-d963-42a3-bf98-d38b73e7aba3",
      "table": "worklogEntries",
      "schema": "6c8055d5-1301-46f6-9d18-8a2a208a277e",
      "fieldId": "6c8055d5-1301-46f6-9d18-8a2a208a277e",
      "rank": 1,
      "deleted": false,
      "columns": [
        {
          "formValueId": "550e8400-e29b-41d4-a716-446655440001",
          "columnId": "123e4567-e89b-12d3-a456-426614174000",
          "columnName": "trade",
          "textVal": "Plumber",
          "numberVal": 42.5,
          "integerVal": 10,
          "arrayVal": [
            "Option 1",
            "Option 2"
          ],
          "timespanVal": 21600000,
          "svgVal": "PHN2ZyBoZWlnaHQ9IjIwMCIgd2lkdGg9IjUwMCI+...",
          "uidVal": "550e8400-e29b-41d4-a716-446655440000",
          "datetimeLocalVal": "2023-06-15T14:30:00",
          "datetimeUtcVal": "2023-06-15T21:30:00Z",
          "timezoneVal": "America/Los_Angeles",
          "timezoneRulesVal": "",
          "lngVal": -122.4194,
          "latVal": 37.7749,
          "dateVal": "2023-06-15",
          "timeVal": "14:30:00"
        }
      ],
      "updatedAt": "2020-11-20T16:14:27.615127+00:00",
      "updatedBy": "USER123A"
    }
  ],
  "pagination": {
    "offset": 0,
    "limit": 50,
    "totalResults": 1,
    "nextUrl": null
  }
}

```

Show More
