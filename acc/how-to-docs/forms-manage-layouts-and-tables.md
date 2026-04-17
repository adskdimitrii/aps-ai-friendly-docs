# Work with Form Layouts and Custom Tables

Source: https://aps.autodesk.com/en/docs/acc/tutorials/forms/manage-layouts-and-tables/

---

# Work with Form Layouts and Custom Tables

This tutorial demonstrates the complete workflow for working with form templates, including retrieving layout information, creating forms, and updating both regular fields and custom table values. You will learn how to work with native tables (work log, materials, equipment) as well as custom tables defined in your form templates.

For more information about Forms, see the [Forms help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Build_Forms_about_forms_html).

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps), and select Autodesk Construction Cloud API
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:read` and `data:write` scopes.
- Find the relevant project ID, by following the [Retrieve a Project ID](getting-started-retrieve-account-and-project-id.md) tutorial. In this example, assume the project ID is `9ba6681e-1952-4d54-aac4-9de6d9858dd4`.
- Verify that you have access to the relevant ACC project.
- Verify that you were added as a contributor to the form templates in that project, see the [Forms help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Build_Forms_about_forms_html) for information about creating and configuring templates.

## [Step 1: Get Form Template and Layout Information](#step-1-get-form-template-and-layout-information)

First, retrieve the form templates available in your project by calling [GET form-templates](../http-docs/http-forms-form-templates-GET.md).

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
      "layoutId": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
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

Note the template ID (`2f634a22-779d-4930-9f08-8391a41fea05`) and layout ID (`7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b`).

### Get Layout Structure

Now retrieve the layout structure by calling [GET layouts/:layoutId](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-layouts-layoutId-(Beta/)-GET). This returns the layout metadata and a list of sections. To get detailed information about fields and tables within each section, you’ll need to call GET sections (shown in the next step).

#### Request

```
curl "https://developer.api.autodesk.com/construction/forms/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/layouts/7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b" -X GET \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json"

```

#### Response

```
{
  "layout": {
    "uid": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
    "type": "form",
    "description": "Daily Report Template",
    "hasSectionAssignees": false
  },
  "sections": [
    {
      "uid": "3a4b5c6d-7e8f-9a0b-1c2d-3e4f5a6b7c8d",
      "layoutUid": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
      "id": "e2a506cf-0a27-47b1-9776-ebe2bdb8042c",
      "sortIndex": 0,
      "displayIndex": 0,
      "type": "section",
      "label": "General Information",
      "description": "Basic form details"
    },
    {
      "uid": "4b5c6d7e-8f9a-0b1c-2d3e-4f5a6b7c8d9e",
      "layoutUid": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
      "id": "f3b617dg-1b38-58c2-a887-fcf6cec9153d",
      "sortIndex": 1,
      "displayIndex": 1,
      "type": "section",
      "label": "Equipment Inspection",
      "description": "Custom equipment inspection table"
    }
  ]
}

```

Show More

### Understanding the Layout Response

The layout response contains basic information about the form template structure:

**Layout**

The `layout` object provides the layout UID, type, and description.

**Sections**

The `sections` array lists all sections in the form. Each section has:

- `uid`: Section unique identifier
- `id`: Section ID
- `label`: Section name
- `description`: Section description

Note the section UIDs as you’ll need them in the next step to retrieve detailed section information including fields and tables.

### Get Section Details

To get the fields and tables within a section, call [GET sections/:sectionId](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-sections-sectionId-(Beta/)-GET) for each section. Let’s retrieve the “Equipment Inspection” section which contains a custom table.

#### Request

```
curl "https://developer.api.autodesk.com/construction/forms/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/layouts/7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b/sections/4b5c6d7e-8f9a-0b1c-2d3e-4f5a6b7c8d9e" -X GET \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json"

```

#### Response

```
{
  "section": {
    "uid": "4b5c6d7e-8f9a-0b1c-2d3e-4f5a6b7c8d9e",
    "layoutUid": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
    "id": "f3b617dg-1b38-58c2-a887-fcf6cec9153d",
    "sortIndex": 1,
    "displayIndex": 1,
    "type": "section",
    "label": "Equipment Inspection",
    "description": "Custom equipment inspection table"
  },
  "sectionItems": [
    {
      "uid": "d4b7df4c-24e8-583h-76g6-89f96e94i285",
      "layoutUid": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
      "sectionUid": "4b5c6d7e-8f9a-0b1c-2d3e-4f5a6b7c8d9e",
      "sortIndex": 0,
      "displayIndex": 0,
      "type": "table",
      "schema": "ec7b2dea-9383-49d4-b22d-52e04659e28b",
      "isRequired": false
    }
  ],
  "tableColumns": {
    "d4b7df4c-24e8-583h-76g6-89f96e94i285": [
      {
        "uid": "e5c8eg5d-35f9-694i-87h7-90ga7fa5j396",
        "layoutUid": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
        "layoutSectionItemUid": "d4b7df4c-24e8-583h-76g6-89f96e94i285",
        "sortIndex": 0,
        "type": "column",
        "columnKey": "equipment_name",
        "columnType": "text_val",
        "label": "Equipment Name"
      },
      {
        "uid": "f6d9fh6e-46ga-7a5j-98i8-01hb8gb6k4a7",
        "layoutUid": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
        "layoutSectionItemUid": "d4b7df4c-24e8-583h-76g6-89f96e94i285",
        "sortIndex": 1,
        "type": "column",
        "columnKey": "inspection_date",
        "columnType": "date_val",
        "label": "Inspection Date"
      },
      {
        "uid": "g7eagi7f-57hb-8b6k-a9j9-12ic9hc7l5b8",
        "layoutUid": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
        "layoutSectionItemUid": "d4b7df4c-24e8-583h-76g6-89f96e94i285",
        "sortIndex": 2,
        "type": "column",
        "columnKey": "status",
        "columnType": "text_val",
        "label": "Status",
        "presets": [
          {"value": "Pass"},
          {"value": "Fail"},
          {"value": "Needs Repair"}
        ]
      },
      {
        "uid": "h8fbhj8g-68ic-9c7l-bak-23jd0id8m6c9",
        "layoutUid": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
        "layoutSectionItemUid": "d4b7df4c-24e8-583h-76g6-89f96e94i285",
        "sortIndex": 3,
        "type": "column",
        "columnKey": "inspector_notes",
        "columnType": "text_val",
        "label": "Inspector Notes"
      }
    ]
  }
}

```

Show More

### Understanding Section Details

The section details response includes:

**Section Object**

The `section` object contains basic information about the section (uid, label, description, etc.).

**Section Items**

The `sectionItems` array contains the fields and tables within the section. Items can be:

- **Fields** (`type: "field"`): Regular form fields with a `valueName` indicating the value type (textVal, numberVal, choiceVal, toggleVal, dateVal, svgVal, arrayVal)
- **Tables** (`type: "table"`): Tabular data with a `schema` identifier (UUID format)

**Table Columns**

The `tableColumns` object maps table UIDs to their column definitions. Each column has:

- `uid`: Column identifier (use this for custom tables)
- `columnKey`: Column key name
- `columnType`: Data type (text_val, number_val, date_val, etc.)
- `label`: Display label

**Identifying Native vs Custom Tables**

- **Native tables**: Have schema values `worklogEntries`, `materialsEntries`, or `equipmentEntries`
- **Custom tables**: Have UUID schema identifiers (e.g., `ec7b2dea-9383-49d4-b22d-52e04659e28b`)

## [Step 2: Create a Form](#step-2-create-a-form)

Use the project ID (`9ba6681e-1952-4d54-aac4-9de6d9858dd4`) and template ID (`2f634a22-779d-4930-9f08-8391a41fea05`) to create a form by calling [POST forms](../http-docs/http-forms-forms-POST.md).

### Request

```
curl "https://developer.api.autodesk.com/construction/forms/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/form-templates/2f634a22-779d-4930-9f08-8391a41fea05/forms" -X POST \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json" \
  -d '{
    "formDate": "2024-01-15",
    "name": "Daily Report - Jan 15",
    "description": "Daily construction report"
  }'

```

Show More

### Response

```
{
  "status": "draft",
  "id": "932da979-e537-4530-b8aa-18607ac6db37",
  "formTemplateId": "2f634a22-779d-4930-9f08-8391a41fea05",
  "formNum": 42,
  "formDate": "2024-01-15",
  "name": "Daily Report - Jan 15",
  "description": "Daily construction report",
  "createdBy": "USER123A",
  "createdAt": "2024-01-15T10:30:00.000000+00:00",
  "updatedAt": "2024-01-15T10:30:00.000000+00:00",
  "nativeForm": {
    "id": "a8f3c2d1-5b6e-4a7f-9c8d-1e2f3a4b5c6d",
    "layoutId": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
    "version": "1.0"
  }
}

```

Show More

Note the form ID (`932da979-e537-4530-b8aa-18607ac6db37`) which you’ll use in the following steps.

## [Step 3: Update Regular Form Fields (Non-Tabular)](#step-3-update-regular-form-fields-non-tabular)

Now update the regular form fields using the v2 batch update endpoint. Use the field IDs (`uid` values) from the section items you retrieved in Step 1 by calling GET sections.

For this example, assume your form has a “General Information” section with the following fields (retrieved via GET sections):
- Weather Condition field (uid: `a184ac19-01b5-250e-43d3-56c63b61f952`)
- Temperature field (uid: `b295bd2a-02c6-361f-54e4-67d74c72g063`)
- Safety Check Complete field (uid: `c3a6ce3b-13d7-472g-65f5-78e85d83h174`)

Call [PUT v2 values:batch-update](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-valuesbatch-update-(New--Beta/)-PUT) with the form ID (`932da979-e537-4530-b8aa-18607ac6db37`).

### Request

```
curl "https://developer.api.autodesk.com/construction/forms/v2/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/forms/932da979-e537-4530-b8aa-18607ac6db37/values:batch-update" -X PUT \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json" \
  -d '{
    "customValues": [
      {
        "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
        "choiceVal": "Sunny",
        "notes": "Clear skies all day"
      },
      {
        "fieldId": "b295bd2a-02c6-361f-54e4-67d74c72g063",
        "numberVal": 72
      },
      {
        "fieldId": "c3a6ce3b-13d7-472g-65f5-78e85d83h174",
        "toggleVal": "Yes"
      }
    ]
  }'

```

Show More

### Response

```
{
  "status": "draft",
  "id": "932da979-e537-4530-b8aa-18607ac6db37",
  "formTemplateId": "2f634a22-779d-4930-9f08-8391a41fea05",
  "formNum": 42,
  "formDate": "2024-01-15",
  "name": "Daily Report - Jan 15",
  "description": "Daily construction report",
  "updatedAt": "2024-01-15T10:35:00.000000+00:00",
  "createdBy": "USER123A",
  "nativeForm": {
    "id": "a8f3c2d1-5b6e-4a7f-9c8d-1e2f3a4b5c6d",
    "layoutId": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
    "version": "1.0",
    "customValues": [
      {
        "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
        "sectionLabel": "General Information",
        "itemLabel": "Weather Condition",
        "valueName": "choiceVal",
        "choiceVal": "Sunny",
        "notes": "Clear skies all day"
      },
      {
        "fieldId": "b295bd2a-02c6-361f-54e4-67d74c72g063",
        "sectionLabel": "General Information",
        "itemLabel": "Temperature (°F)",
        "valueName": "numberVal",
        "numberVal": 72
      },
      {
        "fieldId": "c3a6ce3b-13d7-472g-65f5-78e85d83h174",
        "sectionLabel": "General Information",
        "itemLabel": "Safety Check Complete",
        "valueName": "toggleVal",
        "toggleVal": "Yes"
      }
    ]
  }
}

```

Show More

### Field Value Types

When updating form fields, use the appropriate value type based on the field’s `valueName` from the section details (GET sections):

- `textVal`: Text fields
- `numberVal`: Number fields
- `choiceVal`: Single-select dropdowns
- `arrayVal`: Multi-select fields
- `toggleVal`: Preconfigured responses (Yes/No, Pass/Fail, etc.)
- `dateVal`: Date fields (format: YYYY-MM-DD)
- `svgVal`: Signature fields (base64 encoded SVG)

## [Step 4: Update Native Table Values](#step-4-update-native-table-values)

Now add data to the native tables (work log, materials, and equipment). Use the v2 batch update endpoint with `tabularValues`.

### Request

```
curl "https://developer.api.autodesk.com/construction/forms/v2/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/forms/932da979-e537-4530-b8aa-18607ac6db37/values:batch-update" -X PUT \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json" \
  -d '{
    "tabularValues": [
      {
        "id": "cb95aceb-187a-3a8f-2e5f-502a555c03d5",
        "schema": "worklogEntries",
        "columns": [
          {
            "columnName": "trade",
            "textVal": "Electricians"
          },
          {
            "columnName": "timespan",
            "timespanVal": 28800000
          },
          {
            "columnName": "headcount",
            "numberVal": 5
          },
          {
            "columnName": "description",
            "textVal": "Install lighting fixtures"
          }
        ]
      },
      {
        "id": "2f7e534d-d084-594b-8aa6-147cb8fbc060",
        "schema": "materialsEntries",
        "columns": [
          {
            "columnName": "item",
            "textVal": "LED Light Fixtures"
          },
          {
            "columnName": "quantity",
            "numberVal": 24
          },
          {
            "columnName": "unit",
            "textVal": "units"
          },
          {
            "columnName": "description",
            "textVal": "60W equivalent LED bulbs"
          }
        ]
      },
      {
        "id": "84a32af6-b2b1-c3ae-c186-caef48fe4ffd",
        "schema": "equipmentEntries",
        "columns": [
          {
            "columnName": "item",
            "textVal": "Scissor Lift"
          },
          {
            "columnName": "timespan",
            "timespanVal": 14400000
          },
          {
            "columnName": "quantity",
            "numberVal": 1
          },
          {
            "columnName": "description",
            "textVal": "20ft reach"
          }
        ]
      }
    ]
  }'

```

Show More

### Response

```
{
  "status": "draft",
  "id": "932da979-e537-4530-b8aa-18607ac6db37",
  "formTemplateId": "2f634a22-779d-4930-9f08-8391a41fea05",
  "formNum": 42,
  "updatedAt": "2024-01-15T10:40:00.000000+00:00",
  "nativeForm": {
    "id": "a8f3c2d1-5b6e-4a7f-9c8d-1e2f3a4b5c6d",
    "layoutId": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
    "version": "1.0",
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
            "textVal": "Electricians"
          },
          {
            "formValueId": "2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e",
            "columnId": "b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e",
            "columnName": "timespan",
            "timespanVal": 28800000
          },
          {
            "formValueId": "3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f",
            "columnId": "c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f",
            "columnName": "headcount",
            "numberVal": 5
          },
          {
            "formValueId": "4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a",
            "columnId": "d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a",
            "columnName": "description",
            "textVal": "Install lighting fixtures"
          }
        ],
        "updatedAt": "2024-01-15T10:40:00.000000+00:00",
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
            "textVal": "LED Light Fixtures"
          },
          {
            "formValueId": "6f7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1c",
            "columnId": "f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c",
            "columnName": "quantity",
            "numberVal": 24
          },
          {
            "formValueId": "7a8b9c0d-1e2f-3a4b-5c6d-7e8f9a0b1c2d",
            "columnId": "a7b8c9d0-e1f2-3a4b-5c6d-7e8f9a0b1c2d",
            "columnName": "unit",
            "textVal": "units"
          },
          {
            "formValueId": "8b9c0d1e-2f3a-4b5c-6d7e-8f9a0b1c2d3e",
            "columnId": "b8c9d0e1-f2a3-4b5c-6d7e-8f9a0b1c2d3e",
            "columnName": "description",
            "textVal": "60W equivalent LED bulbs"
          }
        ],
        "updatedAt": "2024-01-15T10:40:00.000000+00:00",
        "updatedBy": "USER123A"
      },
      {
        "id": "84a32af6-b2b1-c3ae-c186-caef48fe4ffd",
        "table": "equipmentEntries",
        "schema": "equipmentEntries",
        "rank": 0,
        "deleted": false,
        "columns": [
          {
            "formValueId": "9c0d1e2f-3a4b-5c6d-7e8f-9a0b1c2d3e4f",
            "columnId": "c9d0e1f2-a3b4-5c6d-7e8f-9a0b1c2d3e4f",
            "columnName": "item",
            "textVal": "Scissor Lift"
          },
          {
            "formValueId": "0d1e2f3a-4b5c-6d7e-8f9a-0b1c2d3e4f5a",
            "columnId": "d0e1f2a3-b4c5-6d7e-8f9a-0b1c2d3e4f5a",
            "columnName": "timespan",
            "timespanVal": 14400000
          },
          {
            "formValueId": "1e2f3a4b-5c6d-7e8f-9a0b-1c2d3e4f5a6b",
            "columnId": "e1f2a3b4-c5d6-7e8f-9a0b-1c2d3e4f5a6b",
            "columnName": "quantity",
            "numberVal": 1
          },
          {
            "formValueId": "2f3a4b5c-6d7e-8f9a-0b1c-2d3e4f5a6b7c",
            "columnId": "f2a3b4c5-d6e7-8f9a-0b1c-2d3e4f5a6b7c",
            "columnName": "description",
            "textVal": "20ft reach"
          }
        ],
        "updatedAt": "2024-01-15T10:40:00.000000+00:00",
        "updatedBy": "USER123A"
      }
    ]
  }
}

```

Show More

### Understanding Native Tables

**Work Log Table (worklogEntries)**

Tracks labor on the project:

- `trade` (textVal): Crew or trade name
- `timespan` (timespanVal): Total hours in milliseconds (e.g., 28800000 = 8 hours)
- `headcount` (numberVal): Number of workers
- `description` (textVal): Work performed

**Materials Table (materialsEntries)**

Tracks materials used:

- `item` (textVal): Material name
- `quantity` (numberVal): Quantity used
- `unit` (textVal): Unit of measurement
- `description` (textVal): Additional details

**Equipment Table (equipmentEntries)**

Tracks equipment usage:

- `item` (textVal): Equipment name
- `timespan` (timespanVal): Hours used in milliseconds
- `quantity` (numberVal): Number of units
- `description` (textVal): Additional details

**Important Notes**

- Each row must have a unique `id` (UUID format). Generate a new UUID for each row.
- For native tables, you can use either `columnName` or `columnId` to identify columns.
- The `schema` field identifies which table you’re updating (worklogEntries, materialsEntries, or equipmentEntries).
- Time values use `timespanVal` in milliseconds (1 hour = 3,600,000 milliseconds).

### Using columnId for Native Tables

As an alternative to `columnName`, you can use `columnId` to reference columns in native tables. This is useful if you have the column UIDs from the section details (GET sections).

Here’s an example using `columnId` instead of `columnName` for the work log table:

```
curl "https://developer.api.autodesk.com/construction/forms/v2/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/forms/932da979-e537-4530-b8aa-18607ac6db37/values:batch-update" -X PUT \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json" \
  -d '{
    "tabularValues": [
      {
        "id": "9a8b7c6d-5e4f-3a2b-1c0d-9e8f7a6b5c4d",
        "schema": "worklogEntries",
        "columns": [
          {
            "columnId": "a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d",
            "textVal": "Carpenters"
          },
          {
            "columnId": "b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e",
            "timespanVal": 32400000
          },
          {
            "columnId": "c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f",
            "numberVal": 3
          },
          {
            "columnId": "d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a",
            "textVal": "Frame interior walls"
          }
        ]
      }
    ]
  }'

```

Show More

Both approaches (`columnName` and `columnId`) work for native tables, so you can choose whichever is more convenient for your implementation.

## [Step 5: Review Custom Table Layout from Step 1](#step-5-review-custom-table-layout-from-step-1)

Custom tables are defined in the form layout. From Step 1, when we called GET sections, we identified a custom table in the “Equipment Inspection” section with:

- **Table UID**: `d4b7df4c-24e8-583h-76g6-89f96e94i285`
- **Schema**: `ec7b2dea-9383-49d4-b22d-52e04659e28b` (UUID format)
- **Columns**:
  * Equipment Name (uid: `e5c8eg5d-35f9-694i-87h7-90ga7fa5j396`, type: text_val)
  * Inspection Date (uid: `f6d9fh6e-46ga-7a5j-98i8-01hb8gb6k4a7`, type: date_val)
  * Status (uid: `g7eagi7f-57hb-8b6k-a9j9-12ic9hc7l5b8`, type: text_val)
  * Inspector Notes (uid: `h8fbhj8g-68ic-9c7l-bak-23jd0id8m6c9`, type: text_val)

### Key Differences from Native Tables

- Custom tables use a UUID as the `schema` identifier (not a predefined name like worklogEntries)
- Must use `columnId` (the column’s UID) to identify columns - `columnName` is not supported for custom tables
- Column types map to value fields:
  * `text_val` → `textVal`
  * `number_val` → `numberVal`
  * `integer_val` → `integerVal`
  * `date_val` → `dateVal`
  * `time_val` → `timeVal`
  * `timespan_val` → `timespanVal`
  * `array_val` → `arrayVal`
  * `uid_val` → `uidVal`

## [Step 6: Update Custom Table Values](#step-6-update-custom-table-values)

Now add data to the custom equipment inspection table using the UUID schema and column UIDs from the section details (retrieved in Step 1).

### Request

```
curl "https://developer.api.autodesk.com/construction/forms/v2/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/forms/932da979-e537-4530-b8aa-18607ac6db37/values:batch-update" -X PUT \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json" \
  -d '{
    "tabularValues": [
      {
        "id": "1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
        "schema": "ec7b2dea-9383-49d4-b22d-52e04659e28b",
        "columns": [
          {
            "columnId": "e5c8eg5d-35f9-694i-87h7-90ga7fa5j396",
            "textVal": "Excavator #12"
          },
          {
            "columnId": "f6d9fh6e-46ga-7a5j-98i8-01hb8gb6k4a7",
            "dateVal": "2024-01-15"
          },
          {
            "columnId": "g7eagi7f-57hb-8b6k-a9j9-12ic9hc7l5b8",
            "textVal": "Pass"
          },
          {
            "columnId": "h8fbhj8g-68ic-9c7l-bak-23jd0id8m6c9",
            "textVal": "All systems operational"
          }
        ]
      },
      {
        "id": "2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e",
        "schema": "ec7b2dea-9383-49d4-b22d-52e04659e28b",
        "columns": [
          {
            "columnId": "e5c8eg5d-35f9-694i-87h7-90ga7fa5j396",
            "textVal": "Crane #5"
          },
          {
            "columnId": "f6d9fh6e-46ga-7a5j-98i8-01hb8gb6k4a7",
            "dateVal": "2024-01-15"
          },
          {
            "columnId": "g7eagi7f-57hb-8b6k-a9j9-12ic9hc7l5b8",
            "textVal": "Needs Repair"
          },
          {
            "columnId": "h8fbhj8g-68ic-9c7l-bak-23jd0id8m6c9",
            "textVal": "Hydraulic leak detected, scheduled for repair"
          }
        ]
      }
    ]
  }'

```

Show More

### Response

```
{
  "status": "draft",
  "id": "932da979-e537-4530-b8aa-18607ac6db37",
  "formTemplateId": "2f634a22-779d-4930-9f08-8391a41fea05",
  "formNum": 42,
  "updatedAt": "2024-01-15T10:45:00.000000+00:00",
  "nativeForm": {
    "id": "a8f3c2d1-5b6e-4a7f-9c8d-1e2f3a4b5c6d",
    "layoutId": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
    "version": "1.0",
    "tabularValues": [
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
            "dateVal": "2024-01-15"
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
        "updatedAt": "2024-01-15T10:45:00.000000+00:00",
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
            "dateVal": "2024-01-15"
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
            "textVal": "Hydraulic leak detected, scheduled for repair"
          }
        ],
        "updatedAt": "2024-01-15T10:45:00.000000+00:00",
        "updatedBy": "USER123A"
      }
    ]
  }
}

```

Show More

## [Step 7: Retrieve Table Values](#step-7-retrieve-table-values)

You can retrieve values from a specific table using [GET table values](../http-docs/http-forms-get-table-values-GET.md). Use the table’s UID from the section details you retrieved in Step 1 (GET sections).

For the custom equipment inspection table, use the table UID `d4b7df4c-24e8-583h-76g6-89f96e94i285`.

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
          "dateVal": "2024-01-15"
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
      "updatedAt": "2024-01-15T10:45:00.000000+00:00",
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
          "dateVal": "2024-01-15"
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
          "textVal": "Hydraulic leak detected, scheduled for repair"
        }
      ],
      "updatedAt": "2024-01-15T10:45:00.000000+00:00",
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

This endpoint is useful for:

- Retrieving large tables with pagination
- Getting the current state of a table without fetching the entire form
- Working with tables that have many rows

## [Step 8: Delete Table Values](#step-8-delete-table-values)

To delete rows from tables, use the v2 batch delete endpoint. You can delete rows from both native and custom tables.

Call [POST v2 values:batch-delete](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-valuesbatch-delete-(Beta/)-POST) with the row IDs and schema identifiers.

### Request

```
curl "https://developer.api.autodesk.com/construction/forms/v2/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/forms/932da979-e537-4530-b8aa-18607ac6db37/values:batch-delete" -X POST \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json" \
  -d '{
    "tabularValues": [
      {
        "id": "2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e",
        "schema": "ec7b2dea-9383-49d4-b22d-52e04659e28b"
      },
      {
        "id": "84a32af6-b2b1-c3ae-c186-caef48fe4ffd",
        "schema": "equipmentEntries"
      }
    ]
  }'

```

Show More

### Response

The default response returns the updated form metadata without the detailed table values:

```
{
  "status": "draft",
  "id": "932da979-e537-4530-b8aa-18607ac6db37",
  "formTemplateId": "2f634a22-779d-4930-9f08-8391a41fea05",
  "formNum": 42,
  "formDate": "2024-01-15",
  "name": "Daily Report - Jan 15",
  "description": "Daily construction report",
  "createdBy": "USER123A",
  "createdAt": "2024-01-15T10:30:00.000000+00:00",
  "updatedAt": "2024-01-15T10:50:00.000000+00:00",
  "updatedBy": "USER123A",
  "nativeForm": {
    "id": "a8f3c2d1-5b6e-4a7f-9c8d-1e2f3a4b5c6d",
    "layoutId": "7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b",
    "version": "1.0"
  }
}

```

Show More

The specified rows have been deleted. To include the full form values in the response, add `includeNativeFormValues=true` to the query parameters.

### Optional Response Parameters

You can control the response using query parameters:

- `excludeFormResponse=true`: Returns HTTP 204 with no body (faster for bulk operations)
- `includeNativeFormValues=true`: Includes the full native form values in the response

Example with no response body:

```
curl "https://developer.api.autodesk.com/construction/forms/v2/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/forms/932da979-e537-4530-b8aa-18607ac6db37/values:batch-delete?excludeFormResponse=true" -X POST \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json" \
  -d '{
    "tabularValues": [
      {
        "id": "row-id-to-delete",
        "schema": "table-schema"
      }
    ]
  }'

```

Show More

This returns HTTP 204 No Content with no response body.

## [Congratulations!](#congratulations)

You have successfully completed the workflow for working with form layouts and custom tables. You learned how to:

- Retrieve form template and layout information
- Identify custom tables and their column structures
- Create a new form instance
- Update regular form fields with different value types
- Add data to native tables (work log, materials, equipment)
- Add data to custom tables using column IDs
- Retrieve table values with pagination
- Delete rows from both native and custom tables

### Next Steps

- Explore the [Forms API reference documentation](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-forms-(Deprecated/)-GET) for more details on available endpoints
- Learn about [form submission workflows](forms-create-update-forms.md)
- Review the [Forms help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Build_Forms_about_forms_html) for information about template configuration and permissions
