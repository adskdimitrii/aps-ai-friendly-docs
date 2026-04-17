# v2/projects/{projectId}/layouts/{layoutId}/sections/{sectionId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/forms-sections-sectionId-(Beta)-GET/

---

Templates

GET

# v2/projects/{projectId}/layouts/{layoutId}/sections/{sectionId}

Returns detailed information about a specific section within a form layout.

Sections contain form fields, tables, and other UI elements that make up the structure of a form.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/forms/v2/projects/:projectId/layouts/:layoutId/sections/:sectionId |
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
| layoutId   string | The unique identifier of the layout. |
| sectionId   string | The unique identifier of the section. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Layout section information. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request header |
| 401   Unauthorized | The request was not accepted because it lacked valid authentication credentials |
| 403   Forbidden | The request was not accepted because the client is authenticated, but is not authorized to access the target resource |
| 404   Not Found | The resource cannot be found |
| 429   Too Many Requests | The request could not be completed due to the rate limit of the target resource |
| 500   Internal Server Error | The request could not be completed due to an internal server error |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| section   object | Metadata about a layout section. |
| --- | --- |
| uid   string: UUID | The unique identifier of the section. |
| layoutUid   string: UUID | The unique identifier of the parent layout. |
| sortIndex   int | The sort order index of the section. |
| displayIndex   int | The display order index of the section. |
| type   enum:string | The type of the section. Will always be: `section` |
| assigneeType   enum:string | The type of assignee for the section. Possible values: `user`, `company`, `role` |
| assigneeId   string | The ID of the assignee for the section. |
| label   string | The label of the section. |
| description   string | The description of the section. |
| sectionItems   array: object | The fields and tables within the section. |
| uid   string: UUID | The unique identifier of the section item. |
| layoutUid   string: UUID | The unique identifier of the parent layout. |
| sectionUid   string: UUID | The unique identifier of the parent section. |
| sortIndex   int | The sort order index of the item within the section. |
| displayIndex   int | The display order index of the item. |
| type   enum:string | What type of UI component should be generated for this element. Possible values: `field`, `table` |
| size   enum:string | On a table column/Free Text field, size:large indicates multi-line text. Possible values: `normal`, `large` |
| label   string | The field label/question text. |
| schema   string | Identifier for the field. For tables, these are aliases. |
| valueName   enum:string | Determines the question type and value name for answering. Possible values: `arrayVal`, `choiceVal`, `dateVal`, `numberVal`, `textVal`, `toggleVal`, `svgVal` |
| description   string | Text displayed with the question for additional context. |
| isRequired   boolean | Determines if the question must be filled before submission. |
| modifier   string | Additional modifier for the field behavior. |
| presets   array: object | Autocomplete or drop-down options. |
| value   string |  |
| tableColumns   object | Map of table UIDs to their column definitions. Only present for sections containing tables. |
| *   array: object |  |
| uid   string: UUID | The unique identifier of the table column. |
| layoutUid   string: UUID | The unique identifier of the parent layout. |
| layoutSectionItemUid   string: UUID | The unique identifier of the parent layout section item. |
| sortIndex   int | The sort order index of the column. |
| type   enum:string | The type of the column. Will always be: `column` |
| presets   array: object | Autocomplete or drop-down options. |
| value   string |  |
| valuesProvider   string | Provider for dropdown values. |
| calc   string | Calculation configuration for the column. |
| columnKey   string | Unique key identifier for the column. This is used in expressions. |
| columnType   enum:string | The data type of the column. Custom tables support multiple column types: <br>`text_val`: Text input`number_val`: Decimal numbers`integer_val`: Whole numbers`array_val`: Dropdown/multi-select (use with `presets` or `valuesProvider`)`uid_val`: Reference fields (companies, roles) - use with `valuesProvider``svg_val`: Signatures (coming soon for custom tables)`date_val`: Date picker`time_val`: Time picker`timespan_val`: Duration/time span<br>Possible values: `text_val`, `number_val`, `integer_val`, `array_val`, `uid_val`, `svg_val`, `date_val`, `time_val`, `timespan_val` |
| expression   string | The expression for the column. |
| label   string | The label for the column. |
| actions   array: object | Conditional logic rules that apply to this section. |
| uid   string: UUID | The unique identifier of the action. |
| layoutUid   string: UUID | The unique identifier of the parent layout. |
| condition   object | The condition which if met will cause the effect (the ‘if’). |
| type   enum:string | Possible values: `and`, `or`, `comparison` |
| operator   enum:string | Possible values: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `not_in`, `contains`, `not_contains` |
| left   object |  |
| right   object |  |
| conditions   array: object |  |
| effect   object | The effect which applies if the condition is met (the ‘then’). |
| type   enum:string | Possible values: `hide`, `show`, `require`, `not_require`, `set_value` |
| target   string |  |
| value   string |  |

## [Example](#example)

Layout section information.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/forms/v2/projects/:projectId/layouts/:layoutId/sections/:sectionId' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "section": {
    "uid": "123e4567-e89b-12d3-a456-426614174001",
    "layoutUid": "123e4567-e89b-12d3-a456-426614174000",
    "sortIndex": 0,
    "displayIndex": 0,
    "type": "section",
    "assigneeType": "user",
    "assigneeId": "",
    "label": "General Information",
    "description": ""
  },
  "sectionItems": [
    {
      "uid": "",
      "layoutUid": "",
      "sectionUid": "",
      "sortIndex": "",
      "displayIndex": "",
      "type": "field",
      "size": "normal",
      "label": "",
      "schema": "",
      "valueName": "arrayVal",
      "description": "",
      "isRequired": "",
      "modifier": "",
      "presets": [
        {
          "value": ""
        }
      ]
    }
  ],
  "tableColumns": {},
  "actions": [
    {
      "uid": "",
      "layoutUid": "",
      "condition": {
        "type": "and",
        "operator": "eq",
        "left": {},
        "right": {},
        "conditions": [
          {}
        ]
      },
      "effect": {
        "type": "hide",
        "target": "",
        "value": ""
      }
    }
  ]
}

```

Show More
