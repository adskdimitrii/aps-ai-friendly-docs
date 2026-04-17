# Retrieve Forms (v2)

Source: https://aps.autodesk.com/en/docs/acc/tutorials/forms/retrieve-forms-v2/

---

# Retrieve Forms (v2)

This tutorial demonstrates how to retrieve a project’s Forms using the v2 API endpoint, which provides enhanced response data including native form values and layout information.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with the `data:read` scope.
- Verify that you have access to the relevant ACC project.

## [Step 1: Find the Form Template IDs](#step-1-find-the-form-template-ids)

Use the project ID (`9ba6681e-1952-4d54-aac4-9de6d9858dd4`) to retrieve the project’s Form Templates, by calling [GET form-templates](../http-docs/http-forms-form-templates-GET.md).

### Request

```
curl "https://developer.api.autodesk.com/construction/forms/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/form-templates" -X GET \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/vnd.api+json"

```

### Response

```
{
  "data": [
    {
      "projectId": "9ba6681e-1952-4d54-aac4-9de6d9858dd4",
      "id": "2f634a22-779d-4930-9f08-8391a41fea05",
      "name": "Daily Report",
      "status": "active",
      "templateType": "pg.template_type.daily_report",
      "userPermissions": [
        {
          "permissions": [
            "submit"
          ],
          "userId": "USER123A"
        }
      ],
      "groupPermissions": [
        {
          "permissions": [
            "manage"
          ],
          "roleKey": "hq_access_level:admin",
          "roleName": "Admin"
        }
      ],
      "createdBy": "USER123A",
      "updatedAt": "2020-11-20T16:13:33.615127+00:00",
      "isPdf": false,
      "pdfUrl": null,
      "forms": {}
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

The response payload includes the Form Template IDs (`data.id`).

## [Step 2: Retrieve Forms Using the v2 API Endpoint](#step-2-retrieve-forms-using-the-v2-api-endpoint)

Use the project ID (`9ba6681e-1952-4d54-aac4-9de6d9858dd4`) and template ID (`2f634a22-779d-4930-9f08-8391a41fea05`) from previous step to retrieve the project’s Forms, by calling [GET v2 forms](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-forms-(New--Beta/)-GET).

The v2 endpoint provides enhanced capabilities including:

- Native form values in the response (`nativeForm.tabularValues` and `nativeForm.customValues`)
- Layout information (`nativeForm.layoutInfo`)
- Additional filtering and sorting options
- Optional inclusion of extra data via the `include` parameter

### Request

```
curl "https://developer.api.autodesk.com/construction/forms/v2/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/forms?templateId=2f634a22-779d-4930-9f08-8391a41fea05&include=nativeValues" -X GET \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json"

```

### Response

```
{
  "data": [
    {
      "status": "draft",
      "id": "932da979-e537-4530-b8aa-18607ac6db37",
      "formTemplateId": "2f634a22-779d-4930-9f08-8391a41fea05",
      "formNum": 1,
      "formDate": "2020-11-20",
      "assigneeId": "USER123A",
      "assigneeType": "user",
      "locationId": "d14ce3a6-e61b-4ab0-a9be-5acf7b5366df",
      "updatedAt": "2020-11-20T16:14:27.615127+00:00",
      "createdAt": "2020-11-20T16:14:00.000000+00:00",
      "createdBy": "USER123A",
      "notes": "Form notes",
      "description": "Form description",
      "name": "Daily Report - Nov 20",
      "nativeForm": {
        "id": "a8f3c2d1-5b6e-4a7f-9c8d-1e2f3a4b5c6d",
        "layoutId": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
        "version": "1.0",
        "layoutInfo": {
          "uid": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
          "type": "form",
          "description": "Daily Report Template",
          "hasSectionAssignees": false
        },
        "tabularValues": [
          {
            "id": "cb95aceb-187a-3a8f-2e5f-502a555c03d5",
            "table": "worklogEntries",
            "schema": "worklogEntries",
            "rank": 0,
            "deleted": false,
            "columns": [
              {
                "formValueId": "1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
                "columnId": "a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d",
                "columnName": "trade",
                "textVal": "Plumbers"
              },
              {
                "formValueId": "2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e",
                "columnId": "b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e",
                "columnName": "timespan",
                "timespanVal": 21600000
              },
              {
                "formValueId": "3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f",
                "columnId": "c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f",
                "columnName": "headcount",
                "numberVal": 4
              },
              {
                "formValueId": "4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a",
                "columnId": "d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a",
                "columnName": "description",
                "textVal": "change pipes"
              }
            ],
            "updatedAt": "2020-11-20T16:14:27.615127+00:00",
            "updatedBy": "USER123A"
          },
          {
            "id": "2f7e534d-d084-594b-8aa6-147cb8fbc060",
            "table": "materialsEntries",
            "schema": "materialsEntries",
            "rank": 0,
            "deleted": false,
            "columns": [
              {
                "formValueId": "5e6f7a8b-9c0d-1e2f-3a4b-5c6d7e8f9a0b",
                "columnId": "e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b",
                "columnName": "item",
                "textVal": "Glue"
              },
              {
                "formValueId": "6f7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1c",
                "columnId": "f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c",
                "columnName": "quantity",
                "numberVal": 3
              },
              {
                "formValueId": "7a8b9c0d-1e2f-3a4b-5c6d-7e8f9a0b1c2d",
                "columnId": "a7b8c9d0-e1f2-3a4b-5c6d-7e8f9a0b1c2d",
                "columnName": "unit",
                "textVal": "qt"
              }
            ],
            "updatedAt": "2020-11-20T16:14:27.615127+00:00",
            "updatedBy": "USER123A"
          }
        ],
        "customValues": [
          {
            "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
            "sectionLabel": "Observation",
            "itemLabel": "Masks / Face Protection",
            "valueName": "toggleVal",
            "toggleVal": "Yes",
            "notes": "Observed Masks and Face Protection"
          },
          {
            "fieldId": "b295bd2a-02c6-361f-54e4-67d74c720063",
            "sectionLabel": "Weather Conditions",
            "itemLabel": "Temperature",
            "valueName": "numberVal",
            "numberVal": 72
          }
        ]
      },
      "pdfFile": null,
      "lastFetchedAt": "2020-11-20T16:14:27.615127+00:00"
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

The response payload includes:

- Form IDs (`data.id`)
- Native form structure (`data.nativeForm`) with:
  * Layout information (`layoutInfo`)
  * Tabular values (`tabularValues`) - data from tables like work log, materials, equipment, and custom tables
  * Custom values (`customValues`) - data from regular form fields
- Form metadata (status, dates, assignees, etc.)

### Understanding the Response Structure

The v2 API response includes the `nativeForm` object which contains:

**Layout Information**

The `layoutInfo` object provides details about the form’s template structure, including whether section assignees are enabled.

**Tabular Values**

The `tabularValues` array contains rows from all tables in the form:

- **Built-in tables**: `worklogEntries`, `materialsEntries`, `equipmentEntries` - includes full column details
- **Custom tables**: Identified by their UUID schema identifier - to get detailed column values for custom tables, use the [GET table values](../http-docs/http-forms-get-table-values-GET.md) endpoint
- Each row includes:
  * `id`: Unique identifier for the row
  * `schema`: Table identifier (built-in alias or UUID for custom tables)
  * `columns`: Array of column values with their types (textVal, numberVal, timespanVal, etc.) - available for built-in tables
  * `rank`: Sort order
  * `deleted`: Whether the row is marked as deleted

**Custom Values**

The `customValues` array contains values from regular form fields (non-tabular):

- `fieldId`: Unique identifier for the field
- `valueName`: Type of value (textVal, numberVal, toggleVal, choiceVal, dateVal, svgVal, arrayVal)
- The actual value in the corresponding field (e.g., `textVal`, `numberVal`)
- `notes`: Optional notes for the field

## [Step 3 (Optional): Filter Forms by Location](#step-3-optional-filter-forms-by-location)

You can filter forms by location using the `locationIds` query parameter. Use the project ID (`9ba6681e-1952-4d54-aac4-9de6d9858dd4`) and location IDs to call the v2 GET forms endpoint.

### Request

```
curl "https://developer.api.autodesk.com/construction/forms/v2/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/forms?locationIds=d14ce3a6-e61b-4ab0-a9be-5acf7b5366df&locationIds=8da1faf2-a72f-421b-89df-00d77e545faf&include=nativeValues" -X GET \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json"

```

### Response

The response will include only forms associated with the specified locations. The structure is the same as shown in Step 2.

### Additional Query Parameters

The v2 API supports additional query parameters for filtering and sorting:

- `statuses`: Filter by form status (draft, inReview, submitted, archived)
- `formDateMin` / `formDateMax`: Filter by form date range
- `updatedAfter` / `updatedBefore`: Filter by update timestamp
- `sort`: Sort results (e.g., `updatedAt desc,formNum asc`)
- `search`: Search for forms containing specific text
- `includeSubLocations`: Include forms from sub-locations
- `include`: Include additional data (nativeValues, tableMetadata, layoutInformation, sublocations, inactiveFormTemplates)

## [Step 4 (Optional): Retrieve Custom Table Values](#step-4-optional-retrieve-custom-table-values)

For custom tables, you need to use the GET table values endpoint to retrieve detailed column data. Use the form ID from Step 2 and the table’s field ID (UID).

To find the table field ID, you can:

1. Call [GET layouts/:layoutId](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-layouts-layoutId-(Beta/)-GET) to get the layout structure
2. Call [GET sections/:sectionId](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-sections-sectionId-(Beta/)-GET) to get the table’s UID from the section items

For this example, assume you have a custom table with field ID `d4b7df4c-24e8-583h-76g6-89f96e94i285`.

### Request

```
curl "https://developer.api.autodesk.com/construction/forms/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/forms/932da979-e537-4530-b8aa-18607ac6db37/table/d4b7df4c-24e8-583h-76g6-89f96e94i285/values?limit=10&offset=0" -X GET \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json"

```

### Response

```
{
  "data": [
    {
      "id": "1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
      "schema": "ec7b2dea-9383-49d4-b22d-52e04659e28b",
      "rank": 0,
      "deleted": false,
      "columns": [
        {
          "formValueId": "3a4b5c6d-7e8f-9a0b-1c2d-3e4f5a6b7c8d",
          "columnId": "e5c8eg5d-35f9-694i-87h7-90ga7fa5j396",
          "columnName": "equipment_name",
          "textVal": "Excavator #12"
        },
        {
          "formValueId": "4b5c6d7e-8f9a-0b1c-2d3e-4f5a6b7c8d9e",
          "columnId": "f6d9fh6e-46ga-7a5j-98i8-01hb8gb6k4a7",
          "columnName": "inspection_date",
          "dateVal": "2020-11-20"
        },
        {
          "formValueId": "5c6d7e8f-9a0b-1c2d-3e4f-5a6b7c8d9e0f",
          "columnId": "g7eagi7f-57hb-8b6k-a9j9-12ic9hc7l5b8",
          "columnName": "status",
          "textVal": "Pass"
        },
        {
          "formValueId": "6d7e8f9a-0b1c-2d3e-4f5a-6b7c8d9e0f1a",
          "columnId": "h8fbhj8g-68ic-9c7l-bak-23jd0id8m6c9",
          "columnName": "inspector_notes",
          "textVal": "All systems operational"
        }
      ],
      "updatedAt": "2020-11-20T16:14:27.615127+00:00",
      "updatedBy": "USER123A"
    },
    {
      "id": "2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e",
      "schema": "ec7b2dea-9383-49d4-b22d-52e04659e28b",
      "rank": 1,
      "deleted": false,
      "columns": [
        {
          "formValueId": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
          "columnId": "e5c8eg5d-35f9-694i-87h7-90ga7fa5j396",
          "columnName": "equipment_name",
          "textVal": "Crane #5"
        },
        {
          "formValueId": "8f9a0b1c-2d3e-4f5a-6b7c-8d9e0f1a2b3c",
          "columnId": "f6d9fh6e-46ga-7a5j-98i8-01hb8gb6k4a7",
          "columnName": "inspection_date",
          "dateVal": "2020-11-20"
        },
        {
          "formValueId": "9a0b1c2d-3e4f-5a6b-7c8d-9e0f1a2b3c4d",
          "columnId": "g7eagi7f-57hb-8b6k-a9j9-12ic9hc7l5b8",
          "columnName": "status",
          "textVal": "Needs Repair"
        },
        {
          "formValueId": "0b1c2d3e-4f5a-6b7c-8d9e-0f1a2b3c4d5e",
          "columnId": "h8fbhj8g-68ic-9c7l-bak-23jd0id8m6c9",
          "columnName": "inspector_notes",
          "textVal": "Hydraulic leak detected"
        }
      ],
      "updatedAt": "2020-11-20T16:14:27.615127+00:00",
      "updatedBy": "USER123A"
    }
  ],
  "pagination": {
    "offset": 0,
    "limit": 10,
    "totalResults": 2,
    "nextUrl": null
  }
}

```

Show More

The response includes:

- **Row metadata**: `id`, `schema` (UUID for custom tables), `rank`, `deleted`
- **Column details**: Each column includes `formValueId`, `columnId`, `columnName`, and the value field (`textVal`, `dateVal`, etc.)
- **Pagination**: Use `offset` and `limit` to page through large tables

Congratulations! You have retrieved Forms using the v2 API with enhanced response data including native form values and layout information, and learned how to retrieve detailed custom table values.
