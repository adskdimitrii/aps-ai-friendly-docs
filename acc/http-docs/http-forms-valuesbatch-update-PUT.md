# v1/projects/{projectId}/forms/{formId}/values:batch-update

Source: https://aps.autodesk.com/en/docs/acc/reference/http/forms-valuesbatch-update-PUT/

---

Forms

PUT

# v1/projects/{projectId}/forms/{formId}/values:batch-update

Updates a formâs main form fields, both tabular and non-tabular. Note that we do not currently support updating PDF forms.

To edit form values, the form needs to be in draft status and the user must have permissions to edit the form. See the [Forms help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Build_Forms_templates_html) for information about template configuration.

To update non-tabular fields you need to use the relevant value type. For example, to update a number field you need to use `numberVal`. To find the value type for the field, call GET forms and check the `valueName`.

See the [Manage Forms tutorial](../how-to-docs/forms-create-update-forms.md) for more details about how to update forms.

To update the formâs details, use [PATCH forms/:formId API](http-forms-forms-formId-PATCH.md).

Note that we do not currently support adding issues or photos.

## [Resource Information](#resource-information)

| Method and URI | PUT https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.
- formIdstring The unique identifier of the form. Use [GET forms](http-forms-forms-GET.md) to retrieve the form ID.

### Request

## [Body Structure](#body-structure)

Expand all

| customValues   array: object | The list of non-tabular fields. |
| --- | --- |
| fieldId*   string: UUID | The unique identifier of the field. |
| notes   string | Text for the fieldâs notes section. This is relevant for all fields. <br>Max length: 8000 |
| textVal   string | The attribute used for updating text value fields, For example, `textVal: This is my response!`. <br>Each non-tabular field is assigned a specific value type, which you need to specify when updating the field. `textVal` is only relevant for updating text value fields. To verify whether the field you want to update is a text value field, call GET forms and check the fieldâs `valueName`.<br>Max length: 8000 |
| choiceVal   string | The attribute used for updating single-select and dropdown fields. For example, `choiceVal: Answer 3`. <br>Each non-tabular field is assigned a specific value type, which you need to specify when updating the field. `choiceVal` is only relevant for updating single-select and dropdown fields. To verify whether the field you want to update is a single-select or dropdown field, call GET forms and check the fieldâs `valueName`. |
| arrayVal   array: string | The attribute used for updating multi-select fields. For example, `arrayVal:` `["Answer 1", "Answer 2"]`. <br>Each non-tabular field is assigned a specific value type, which you need to specify when updating the field. `arrayVal` is only relevant for updating multi-select fields. To verify whether the field you want to update is a multi-select field, call GET forms and check the fieldâs `valueName`. |
| dateVal   string | The attribute used for updating date fields, in the following format `(YYYY-MM-DD)`. For example, `"dateVal": "1999-12-31"`. <br>Each non-tabular field is assigned a specific value type, which you need to specify when updating the field. `dateVal` is only relevant for updating date fields. To verify whether the field you want to update is a date field, call GET forms and check the fieldâs `valueName`. |
| numberVal   number | The attribute used for updating number fields. For example, `"numberVal": "42"`. <br>Each non-tabular field is assigned a specific value type, which you need to specify when updating the field. `numberVal` is only relevant for updating number fields. To verify whether the field you want to update is a number field, call GET forms and check the fieldâs `valueName`. |
| toggleVal   enum:string | The attribute used for updating preconfigured fields. For example, âtoggleValâ: âYesâ. <br>Each non-tabular field is assigned a specific value type, which you need to specify when updating the field. `toggleVal` is only relevant for updating preconfigured fields. To verify whether the field you want to update is a preconfigured field, call GET forms and check the fieldâs `valueName`. Possible values: `Yes`, `No`, `False`, `True`, `Minus`, `Plus`, `Fail`, `Pass`, `NA` |
| svgVal   string | The attribute used for updating signature fields. <br>Each non-tabular field is assigned a specific value type, which you need to specify when updating the field. `svgVal` is only relevant for updating signature fields. To verify whether the field you want to update is a signature field, call GET forms and check the fieldâs `valueName`.<br>The signature needs to be in SVG format and it needs to be base64 encoded. |
| name   string | The name of the person who signed the form. By default, it is the name of the logged in user. It is only relevant for signature fields. To update the name you need to use the signature field ID. |
| tabularValues   array: object | The list of tabular fields. |
| id*   string: UUID | The ID of the table row. You need to generarte the ID (UUID) for the row. |
| table*   enum:string | The table to update. Possible values: `worklogEntries`, `materialsEntries`, `equipmentEntries` |
| columns   array: object | The set of values for the columns in the row. |
| columnName   enum:string | The name of the column to update. Possible values: <br>For the Work Log table:<br>`trade` (Crew) - use `textVal`, `timespan` (Total hours) - use `timespanVal`, `headcount` (workers) - use `numberVal`, `description` (work performed) - use `textVal`<br>For the Equipment table:<br>`item` (equipment) - use `textVal`, `timespan` (Hours used) - use `timespanVal`, `quantity` (Quantity) - use `numberVal`, `description` (comment) - use `textVal`<br>For the Materials table:<br>`item` (Material) - use `textVal`, `quantity` (Quantity) - use `numberVal`, `unit` (Unit) - use `textVal`, `description` (Comment) - use `textVal`. |
| numberVal   number | The attribute used for updating number columns. For example, `"numberVal": "42"`. <br>Each tabular field is assigned a specific value type, which you need to specify when updating the field. `numberVal` is relevant for updating the following columns: `headcount` (Workers) and `quantity` (Quantity). |
| textVal   string | The attribute used for updating text value columns. <br>Each tabular field is assigned a specific value type, which you need to specify when updating the field. `textVal` is relevant for updating the following columns: `description` (Work performed), `description` (comment), `item` (Equipment), `item` (Material), `trade` (Crew), and `unit` (Unit).<br>Max length: 8000 |
| timespanVal   number | The attribute used for updating time-related columns. <br>Each tabular field is assigned a specific value type, which you need to specify when updating the field. `timespanVal` is relevant for updating the following columns: `timespan` (Total hours), `timespan` (Hours used). |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The updated Form |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request header |
| 401   Unauthorized | The request was not accepted because it lacked valid authentication credentials |
| 403   Forbidden | The request was not accepted because the client is authenticated, but is not authorized to access the target resource |
| 404   Not Found | The resource cannot be found |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the target resource |
| 429   Too Many Requests | The request could not be completed due to a conflict with the current state of the target resource |
| 500   Internal Server Error | The request could not be completed due to a conflict with the current state of the target resource |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| status   enum:string | The current status of the form. Note that forms are created in `draft` status. Possible values: <br>`draft`: you can edit forms.<br>`inReview`: you cannot edit forms, however, they can be approved by form reviewers.<br>`submitted`: forms are closed and no longer editable.<br>`archived` forms are not edtiable and hidden in the UI. |
| --- | --- |
| id   string | The unique identifier of the form. |
| projectId   string | The unique identifier of the project the form belongs to. |
| formNum   int | A chronological user-fiendly identifier of the form within the project e.g. form #5. |
| formDate   string | Date the form pertains to. |
| assigneeId   string | The unique identifier of the user, role, or company the form is assigned to. |
| assigneeType   enum:string | Type of entity the form is assigned to. Possible values: `company`, `role`, `user` |
| locationId   string | Location identifier associated with the form. For more information about the location, see [GET nodes](http-locations-nodes-GET.md). |
| updatedAt   datetime: ISO 8601 | When form was last updated, UTC date and time in ISO-8601 format. |
| createdBy   string | The unique identifier of the user who created the form. |
| notes   string | Text for the formâs notes section. |
| description   string | Text for the formâs description section. |
| name   string | The name of the form instance. <br>Max length: 100 |
| formTemplate   object | Information about the formâs template. |
| status   enum:string | Possible values: `active`, `inactive`, `deleted` |
| id   string | The unique identifier of the template. |
| projectId   string | Unique indentifier of the project the template belongs to. |
| name   string | Name of the form template. |
| templateType   string | User defined type of the form template. |
| pdfValues   array: object | For PDF forms, values extracted from fields in the PDF. |
| name   string | The name of the PDF field. |
| value   string | The value of the PDF field. |
| pdfUrl   string | For PDF forms, the URL to download the formâs PDF. |
| weather   object | Weather forecast captured on the form. |
| summaryKey   string | A code describing the the weather (e.g. Clear, PartlyCloudy). |
| precipitationAccumulation   number | Amount of precipitation accumulated throughout the day. |
| precipitationAccumulationUnit   string | Indicates the measurement unit of the `precipitationAccumulation`. |
| temperatureMin   number | Minimum temperature during the day. |
| temperatureMax   number | Maximum temperature during the day. |
| temperatureUnit   string | Indicates the measurement unit of the temperature values e.g. `temperatureMin`, `temperatureMax`, `temp`. |
| humidity   number | A percentage value indicating the humidity over the course of the day. |
| windSpeed   number | Average wind speed observed throughout the day. |
| windGust   number | Maximum wind speed observed throughout the day. |
| speedUnit   string | Indicates the measurement unit of the `windSpeed` and `windGust`. |
| windBearing   number | Direction of the wind, in degrees. |
| hourlyWeather   array: object | Weather information for specific hours (07:00:00, 12:00:00, 16:00:00). |
| id   int | Unique identifier. |
| hour   string | Hour of the day for this forecast. |
| temp   number | Temperature during specified hour. |
| windSpeed   number | Average wind speed. |
| windBearing   int | Direction of the wind, in degrees. |
| humidity   number | A percentage value indicating the humidity. |
| fetchedAt   datetime: ISO 8601 | Date when weather was fetched from weather API. |
| createdAt   datetime: ISO 8601 | Date when weather was first fetched. |
| updatedAt   datetime: ISO 8601 | When the weather was last updated. |
| provider   enum:string | Indicates the source of the weather data. Possible values: `darksky`, `weatherkit` |
| tabularValues   object | For non-PDF forms, data stored in the tables on the form. |
| worklogEntries   array: object | Entries associated with work log table in a Form. |
| id   string | Unique identifier for the work log row. |
| deleted   boolean | Indicates if the work log row has been deleted. |
| trade   string | A text field indicating the workerâs trade. |
| timespan   int | Total duration of work performed (in milliseconds). |
| headcount   int | Number of workers. |
| description   string | A text description of the work performed. |
| materialsEntries   array: object | Entries associated with materials table in a Form. |
| id   string | Unique identifier for the material log row. |
| deleted   boolean | Indicates if the material log row has been deleted. |
| item   string | Text indicating the material used. |
| quantity   number | The quantity of material that was used. |
| unit   string | The unit of measure for the quantity specified. |
| description   string | Additional description of the materials. |
| equipmentEntries   array: object | Entries associated with equipment table in a Form. |
| id   string | Unique identifier for the equipment log row. |
| deleted   boolean | Indicates if the equipment log row has been deleted. |
| item   string | Text indicating the equipment utilized. |
| timespan   int | The total time all equipment was utilized (in milliseconds). |
| quantity   number | The amount of equipment utilized. |
| description   string | Text describing the equipment utilized. |
| customValues   array: object | For non-PDF forms, data stored in the form fields. |
| fieldId   string | The unique identifier of the field. |
| sectionLabel   string | Name of the section containing this field. |
| itemLabel   string | The fieldâs label or question text. |
| valueName   enum:string | Indicates the type of value used for this item. Possible values: `textVal`, `toggleVal`, `arrayVal`, `numberVal`, `choiceVal`, `dateVal`, `svgVal` |
| toggleVal   enum:string | A boolean like enum value. Possible values: `Yes`, `No`, `False`, `True`, `Minus`, `Plus`, `Fail`, `Pass`, `NA` |
| textVal   string | A text value. |
| arrayVal   string | Multi select values. |
| numberVal   number | A numeric value. |
| choiceVal   string | A single select value. |
| dateVal   string | A date value. |
| svgVal   string | A signature value (base64 encoded SVG). |
| notes   string | Text for the fieldâs notes section. <br>Max length: 8000 |
| lastReopenedBy   string | Unique identifier for the user that last re-opened the Form (if applicable). |
| lastSubmitterSignature   string | Signature of the reviewer who last submitted the Form (if applicable). Signature value (base64 encoded SVG). |
| userCreatedAt   datetime: ISO 8601 | When form was created on the client, UTC date and time in ISO-8601 format. |
| createdAt   datetime: ISO 8601 | When form was created on the server, UTC date and time in ISO-8601 format. |

## [Examples](#examples)

You can update the main form fields in a number of ways. We will describe the following options:

1. Update a preconfigured response field
2. Update a text response field
3. Update a number response field
4. Update a dropdown response field
5. Update a multiple-select response field
6. Update a date field
7. Update the work log table
8. Update the equipment log table
9. Update the materials log table

### Option 1: Update a preconfigured response field

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
    "customValues": [
      {
        "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
        "toggleVal": "Yes"
      }
    ],
  }'

```

Show More

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "toggleVal": "Yes",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "sectionLabel": "All question types",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "sectionLabel": "All question types",
          "valueName": "svgVal"
      }
  ],
  "name": "Daily Safety Inspection",
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [],
      "materialsEntries": [],
      "worklogEntries": []
  },
  "updatedAt": "2023-03-10T22:24:50.201013+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

### Option 2: Update a text response field

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
    "customValues": [
      {
        "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
        "textVal": "This is my response!"
      }
    ]
  }'

```

Show More

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "textVal": "This is my response!",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "sectionLabel": "All question types",
          "valueName": "svgVal"
      }
  ],
  "name": "Daily Safety Inspection",
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [],
      "materialsEntries": [],
      "worklogEntries": []
  },
  "updatedAt": "2023-03-10T22:27:35.202321+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

### Option 3: Update a number response field

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
    "customValues": [
      {
        "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
        "numberVal": "42"
      }
    ]
  }'

```

Show More

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "notes": null,
          "numberVal": 42.0,
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "sectionLabel": "All question types",
          "valueName": "svgVal"
      }
  ],
  "name": "Daily Safety Inspection",
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [],
      "materialsEntries": [],
      "worklogEntries": []
  },
  "updatedAt": "2023-03-10T22:29:04.053634+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

### Option 4: Update a dropdown response field

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
    "customValues": [
      {
        "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
        "choiceVal": "Answer 3"
      }
    ]
  }'

```

Show More

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "choiceVal": "Answer 2",
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "choiceVal": "Answer 3",
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "sectionLabel": "All question types",
          "valueName": "svgVal"
      }
  ],
  "name": "Daily Safety Inspection",
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [],
      "materialsEntries": [],
      "worklogEntries": []
  },
  "updatedAt": "2023-03-10T22:31:43.644546+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

### Option 5: Update a multiple-select response field

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
    "customValues": [
      {
        "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
        "arrayVal": ["Answer 2", "Answer 3"]
      }
    ]
  }'

```

Show More

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "arrayVal": "['Answer 2', 'Answer 3']",
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "sectionLabel": "All question types",
          "valueName": "svgVal"
      }
  ],
  "name": "Daily Safety Inspection",
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [],
      "materialsEntries": [],
      "worklogEntries": []
  },
  "updatedAt": "2023-03-10T22:33:29.619130+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

### Option 6: Update a date field

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
    "customValues": [
      {
        "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
        "dateVal": "1999-12-31"
      }
    ]
  }'

```

Show More

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "dateVal": "1999-12-31",
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "sectionLabel": "All question types",
          "valueName": "svgVal"
      }
  ],
  "name": "Daily Safety Inspection",
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [],
      "materialsEntries": [],
      "worklogEntries": []
  },
  "updatedAt": "2023-03-10T22:35:09.886283+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

### Option 7: Update the work log table

Create a new UUID to identify each new row, for this example we will use `` e76fe3f4-f587-4309-92c4-6a6f14b9e1bd` ``

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
  "tabularValues": [
      {
          "table": "worklogEntries",
          "id": "e76fe3f4-f587-4309-92c4-6a6f14b9e1bd",
          "columns": [
              {
                  "columnName": "trade",
                  "textVal": "Electrical"
              },
              {
                  "columnName": "timespan",
                  "timespanVal": 7200000
              },
              {
                  "columnName": "headcount",
                  "numberVal": 1
              },
              {
                  "columnName": "description",
                  "textVal": "Room 302 lights"
              }
          ]
      }
  ]
}'

```

Show More

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "svgVal"
      }
  ],
  "name": "Daily Safety Inspection",
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [],
      "materialsEntries": []
      "worklogEntries": [
          {
              "deleted": false,
              "description": "Room 302 lights",
              "headcount": 1,
              "id": "e76fe3f4-f587-4309-92c4-6a6f14b9e1bd",
              "timespan": 7200000,
              "trade": "Electrical"
          }
      ],
  },
  "updatedAt": "2023-03-10T23:08:09.543333+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

### Option 8: Update the equipment log table

Create a new UUID to identify each new row, for this example we will use `` d237d262-e5a6-4251-bc06-37f516dbed5c` ``

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
  "tabularValues": [
      {
          "table": "equipmentEntries",
          "id": "d237d262-e5a6-4251-bc06-37f516dbed5c",
          "columns": [
              {
                  "columnName": "item",
                  "textVal": "Forklift"
              },
              {
                  "columnName": "timespan",
                  "timespanVal": 7200000
              },
              {
                  "columnName": "quantity",
                  "numberVal": 1
              },
              {
                  "columnName": "description",
                  "textVal": "Toyota 8FGCU25"
              }
          ]
      }
  ]
}'

```

Show More

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "svgVal"
      }
  ],
  "name": "Daily Safety Inspection",
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [
          {
              "deleted": false,
              "description": "Toyota 8FGCU25",
              "id": "d237d262-e5a6-4251-bc06-37f516dbed5c",
              "item": "Forklift",
              "quantity": 1.0,
              "timespan": 7200000
          }
      ],
      "materialsEntries": [],
      "worklogEntries": [],
  },
  "updatedAt": "2023-03-10T23:12:45.627778+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

### Option 9: Update the materials log table

Create a new UUID to identify each new row, for this example we will use `` 5b4fe828-fd45-4a9e-a660-6b70cb47c39f` ``

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
  "tabularValues": [
      {
          "table": "materialsEntries",
          "id": "5b4fe828-fd45-4a9e-a660-6b70cb47c39f",
          "columns": [
              {
                  "columnName": "item",
                  "textVal": "Sand"
              },
              {
                  "columnName": "quantity",
                  "numberVal": 2
              },
              {
                  "columnName": "unit",
                  "textVal": "tons"
              },
              {
                  "columnName": "description",
                  "textVal": "fill for pool area"
              }
          ]
      }
  ]
}'

```

Show More

### response

```
{{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "svgVal"
      }
  ],
  "name": "Daily Safety Inspection",
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [],
      "materialsEntries": [
          {
              "deleted": false,
              "description": "fill for pool area",
              "id": "5b4fe828-fd45-4a9e-a660-6b70cb47c39f",
              "item": "Sand",
              "quantity": 2.0,
              "unit": "tons"
          }
      ],
      "worklogEntries": []
  },
  "updatedAt": "2023-03-10T23:16:20.758371+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More
