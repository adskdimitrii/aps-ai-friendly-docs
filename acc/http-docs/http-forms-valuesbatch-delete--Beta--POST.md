# v2/projects/{projectId}/forms/{formId}/values:batch-delete

Source: https://aps.autodesk.com/en/docs/acc/reference/http/forms-valuesbatch-delete-(Beta)-POST/

---

Forms

POST

# v2/projects/{projectId}/forms/{formId}/values:batch-delete

This API currently only deletes form values from tabular fields. The form needs to be in draft status and the user must have permissions to edit the form.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/forms/v2/projects/:projectId/forms/:formId/values:batch-delete |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). <br>The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the Forma API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.
- formIdstring The unique identifier of the form. Use [GET forms](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-forms-(Deprecated/)-GET/) to retrieve the form ID.

### Request

## [Query String Parameters](#query-string-parameters)

| excludeFormResponse   boolean | Exclude the updated form in the response. |
| --- | --- |
| includeNativeFormValues   boolean | Include the form values in the response. |

### Request

## [Body Structure](#body-structure)

Expand all

| tabularValues   array: object | The list of tabular fields to delete values from. Maximum 10 items per request. |
| --- | --- |
| id*   string: UUID | Unique identifier for the table row to delete. |
| schema*   string | Table identifier or built-in table alias. For built-in tables, use `worklogEntries`, `materialsEntries`, or `equipmentEntries`. For custom tables, use the table’s schema identifier. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The updated Form |
| --- | --- |
| 204   No Content | No content (when excludeFormResponse is true) |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request header |
| 401   Unauthorized | The request was not accepted because it lacked valid authentication credentials |
| 403   Forbidden | The request was not accepted because the client is authenticated, but is not authorized to access the target resource |
| 404   Not Found | The resource cannot be found |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the target resource |
| 429   Too Many Requests | The request could not be completed due to the rate limit of the target resource |
| 500   Internal Server Error | The request could not be completed due to an internal server error |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| formTemplateId   string: UUID | Unique identifier of template the form belongs to. |
| --- | --- |
| id   string: UUID | Unique identifier of the form. |
| status   enum:string | Current state of the form e.g. inProgress Possible values: `draft`, `inReview`, `submitted`, `archived` |
| formNum   int | Unique identifier of form, autoincremental, unique per project. |
| formDate   string | Date the Form is created for. |
| assigneeId   string | ID of the entity form is assigned to. |
| assigneeType   enum:string | Type of the entity form is assigned to. Possible values: `company`, `role`, `user` |
| dueDate   string | Date the Form is due. |
| locationId   string: UUID | The unique identifier of the Form’s location |
| createdBy   string | User ID that created the Form. |
| createdAt   datetime: ISO 8601 | Timestamp when the form was received and stored on the server. UTC date and time in ISO-8601 format. |
| userCreatedAt   datetime: ISO 8601 | Timestamp when the form was created on the client device or external system. This may differ from createdAt if the form was created offline and synced later. UTC date and time in ISO-8601 format. |
| notes   string | Form notes. |
| description   string | Form description. |
| name   string | Form name |
| updatedAt   datetime: ISO 8601 | When form was last updated, UTC date and time in ISO-8601 format. |
| updatedBy   string | User ID that last updated the Form. |
| weatherId   int | Unique identifier of weather associated with this form. |
| lastSubmitterSignature   string | Signature of the reviewer who last submitted the Form (if applicable). Signature value (base64 encoded SVG). |
| lastSubmittedBy   string | User ID that last submitted the Form. |
| lastSubmittedAt   datetime: ISO 8601 | When form was last submitted (if applicable), UTC date and time in ISO-8601 format. |
| lastReopenedBy   string | User ID that re-opened the Form (if applicable). |
| lastStatusChanges   object | Contains the last transition into each status. Since a form can transition between statuses multiple times (e.g., reopened from closed back to inProgress), this shows the most recent transition for each status the form has been in. |
| previousStatus   string | The status the form was in before the current status. |
| inProgress   object | The last time the form transitioned into inProgress status. |
| by   string | User ID who made the status change. |
| at   string | When the status change occurred, UTC date and time in ISO-8601 format. |
| inReview   object | The last time the form transitioned into inReview status. |
| by   string | User ID who made the status change. |
| at   string | When the status change occurred, UTC date and time in ISO-8601 format. |
| closed   object | The last time the form transitioned into closed status. |
| by   string | User ID who made the status change. |
| at   string | When the status change occurred, UTC date and time in ISO-8601 format. |
| archived   object | The last time the form transitioned into archived status. |
| by   string | User ID who made the status change. |
| at   string | When the status change occurred, UTC date and time in ISO-8601 format. |
| discarded   object | The last time the form transitioned into discarded status. |
| by   string | User ID who made the status change. |
| at   string | When the status change occurred, UTC date and time in ISO-8601 format. |
| nativeForm   object | Native form data including layout and values. |
| id   string: UUID | The form’s unique identifier. This is the same value as the top-level form id. |
| layoutId   string: UUID | Unique identifier of the layout. |
| version   string | Semantic version indicating the feature set available for this form’s template. Clients can use this to determine which features are supported. For example, version 13.0 or higher is required for custom tables support. The Forms App typically uses the highest available version. |
| layoutInfo   object | Information about the layout of this form. |
| description   string | The description of the layout. |
| hasSectionAssignees   boolean | Determines if section assignment is enabled. |
| customValues   array: object | Custom form values for Form. |
| fieldId   string | The unique identifier of the field. |
| sectionLabel   string | Name of the section containing this field. |
| itemLabel   string | The field’s label or question text. |
| valueName   enum:string | Indicates the type of value used for this item. Possible values: `textVal`, `toggleVal`, `arrayVal`, `numberVal`, `choiceVal`, `dateVal`, `svgVal` |
| toggleVal   enum:string | A boolean like enum value. Possible values: `Yes`, `No`, `False`, `True`, `Minus`, `Plus`, `Fail`, `Pass`, `NA` |
| textVal   string | A text value. |
| arrayVal   string | Multi select values. |
| numberVal   number | A numeric value. |
| choiceVal   string | A single select value. |
| dateVal   string | A date value. |
| svgVal   string | A signature value (base64 encoded SVG). |
| notes   string | Text for the field’s notes section. <br>Max length: 8000 |
| pdfFile   object | PDF file information for the form. |
| id   string | Unique identifier of the PDF file. |
| fileName   string | Name of the PDF file. |
| pdfUrl   string | URL to download the PDF file. |
| lastFetchedAt   datetime: ISO 8601 | When form was retrieved from the API, UTC date and time in ISO-8601 format. |

### Response

## [Body Structure (204)](#body-structure-204)

Response for 204 has no body.

## [Example](#example)

The updated Form

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/forms/v2/projects/:projectId/forms/:formId/values:batch-delete' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "tabularValues": [
          {
            "id": "28a31f14-d963-42a3-bf98-d38b73e7aba3",
            "schema": "worklogEntries"
          }
        ]
      }'

```

Show More

### Response

```
{
  "formTemplateId": "2f634a22-779d-4930-9f08-8391a41fea05",
  "id": "932da979-e537-4530-b8aa-18607ac6db37",
  "status": "draft",
  "formNum": 1,
  "formDate": "2020-11-20",
  "assigneeId": "fc830fd8-f1ef-4cd6-9163-fb115dc698d7",
  "assigneeType": "company",
  "dueDate": "2020-11-25",
  "locationId": "d14ce3a6-e61b-4ab0-a9be-5acf7b5366df",
  "createdBy": "USER123A",
  "createdAt": "2019-01-20T12:14:28.000000+00:00",
  "userCreatedAt": "2019-01-20T12:14:27.615127+00:00",
  "notes": "Form notes",
  "description": "Form description",
  "name": "Form name",
  "updatedAt": "2020-11-20T16:14:27.615127+00:00",
  "updatedBy": "USER123A",
  "weatherId": 12345,
  "lastSubmitterSignature": "PHN2ZyBoZWlnaHQ9IjIwMCIgd2lkdGg9IjUwMCI+PHBvbHlsaW5lIHBvaW50cz0iMjAsMjAgNDAsMjUgNjAsNDAgODAsMTIwIDEyMCwxNDAgMjAwLDE4MCIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2U6YmxhY2s7c3Ryb2tlLXdpZHRoOjMiIC8+PC9zdmc+",
  "lastSubmittedBy": "USER123A",
  "lastSubmittedAt": "2020-11-20T18:14:27.615127+00:00",
  "lastReopenedBy": "USER123A",
  "lastStatusChanges": {
    "previousStatus": "inProgress",
    "inProgress": {
      "by": "USER123A",
      "at": "2020-11-20T16:14:27.615127+00:00"
    },
    "inReview": {
      "by": "USER123A",
      "at": "2020-11-20T16:14:27.615127+00:00"
    },
    "closed": {
      "by": "USER123A",
      "at": "2020-11-20T16:14:27.615127+00:00"
    },
    "archived": {
      "by": "USER123A",
      "at": "2020-11-20T16:14:27.615127+00:00"
    },
    "discarded": {
      "by": "USER123A",
      "at": "2020-11-20T16:14:27.615127+00:00"
    }
  },
  "nativeForm": {
    "id": "932da979-e537-4530-b8aa-18607ac6db37",
    "layoutId": "123e4567-e89b-12d3-a456-426614174001",
    "version": "13.0",
    "layoutInfo": {
      "description": "",
      "hasSectionAssignees": false
    },
    "customValues": [
      {
        "fieldId": "151eedb2-5be1-4ebc-899d-7ff8eda4d76d",
        "sectionLabel": "Observation",
        "itemLabel": "Was everyone wearing masks / face protection?",
        "valueName": "textVal",
        "toggleVal": "Yes",
        "textVal": "Yes",
        "arrayVal": [
          "A",
          "B"
        ],
        "numberVal": 1,
        "choiceVal": "A",
        "dateVal": "Yes",
        "svgVal": "PHN2ZyB4bWxucz0iaHR0cDov...",
        "notes": "Observed Masks and Face Protection"
      }
    ]
  },
  "pdfFile": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "fileName": "form_report.pdf",
    "pdfUrl": "https://example.com/form_report.pdf"
  },
  "lastFetchedAt": "2020-11-20T16:14:27.615127+00:00"
}

```

Show More

## [Example](#id8)

No content (when excludeFormResponse is true)

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/forms/v2/projects/:projectId/forms/:formId/values:batch-delete' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "tabularValues": [
          {
            "id": "28a31f14-d963-42a3-bf98-d38b73e7aba3",
            "schema": "worklogEntries"
          }
        ]
      }'

```

Show More

### Response

```
204 No Content

```
