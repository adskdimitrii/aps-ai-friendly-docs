# v2/projects/{projectId}/forms/{formId}/values

Source: https://aps.autodesk.com/en/docs/acc/reference/http/forms-custom-values-(Beta)-GET/

---

Forms

GET

# v2/projects/{projectId}/forms/{formId}/values

Returns all form field values (custom values / question values) on the form.

This endpoint retrieves values from standard form fields such as text inputs, numbers, dates, toggles, single/multi select choices, and signatures. This excludes tabular values (table row values like work log, materials, equipment, and custom tables).

**Note:** Only questions that have been answered (have a value set) are returned. Unanswered questions will not appear in the response.

Results are sorted by `updatedAt` in ascending order (oldest first).

To retrieve tabular values, use the [GET form tabular values](http-forms-get-table-values-GET.md) endpoint instead.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/forms/v2/projects/:projectId/forms/:formId/values |
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

- projectIdstring The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the Forma API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.
- formIdstring The unique identifier of the form. Use [GET forms](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-forms-(Deprecated/)-GET/) to retrieve the form ID.

### Request

## [Query String Parameters](#query-string-parameters)

| offset   int | The number of records to skip before returning the result records. Defaults to 0. Increase this value in subsequent requests to continue getting results when the number of records exceeds the requested limit. |
| --- | --- |
| limit   int | The number of records to return in a single request. Can be a number between 1 and 50. Defaults to 50. |
| sectionUid   string | Filter by section UID to retrieve values for a specific section only. <br>Use [GET layout](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-layouts-layoutId-(Beta/)-GET/) to retrieve section UIDs from the form’s layout. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Form field values. |
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

| data   array: object | List of form field values (custom values / question values). |
| --- | --- |
| id   string: UUID | Unique identifier for the form value. |
| fieldId   string: UUID | Unique identifier for the field (schema_uid). Use this to correlate the value with its field definition in the form layout. |
| deleted   boolean | Indicates whether this value has been deleted. If `true`, the value was removed from the form. |
| toggleVal   enum:string | Value for toggle/checkbox fields. This endpoint always returns normalized values: `True` (affirmative), `False` (negative), or `NA` (not applicable), regardless of the question’s modifier type (yes/no, pass/fail, plus/minus). To determine the original display format (e.g., Yes/No vs Pass/Fail), check the question’s modifier from the [GET section](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-sections-sectionId-(Beta/)-GET/) endpoint. Possible values: `Yes`, `No`, `False`, `True`, `Minus`, `Plus`, `Fail`, `Pass`, `NA` |
| textVal   string | Value for text input fields. |
| numberVal   number | Value for number input fields. |
| choiceVal   string | Value for single-select dropdown or radio button fields. Contains the selected option value. |
| arrayVal   array: string | Value for multi-select fields. Contains an array of selected option values. |
| dateVal   string | Value for date fields. Date in ISO-8601 format (YYYY-MM-DD). |
| svgVal   string | Value for signature fields. Contains the signature as a base64-encoded SVG string. |
| name   string | Name of the person who provided the signature. Only populated for signature fields. |
| notes   string | Additional notes or comments associated with the field value. |
| updatedAt   datetime: ISO 8601 | The date and time when the value was last updated, in UTC ISO-8601 format. |
| updatedBy   string | The user ID (Oxygen ID) of the user who last updated this value. |
| pagination   object | Request pagination information. |
| offset   int | Number of items skipped. |
| limit   int | Number of items returned per page. |
| totalResults   int | Total number of items that can be returned. |
| nextUrl   string | URL for the next page of items. Next page url is null on the last page. |

## [Example](#example)

Form field values.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/forms/v2/projects/:projectId/forms/:formId/values' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "data": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440001",
      "fieldId": "123e4567-e89b-12d3-a456-426614174000",
      "deleted": false,
      "toggleVal": "True",
      "textVal": "Site inspection completed successfully.",
      "numberVal": 42.5,
      "choiceVal": "Option A",
      "arrayVal": [
        "Option 1",
        "Option 2",
        "Option 3"
      ],
      "dateVal": "2026-01-29",
      "svgVal": "PHN2ZyBoZWlnaHQ9IjIwMCIgd2lkdGg9IjUwMCI+...",
      "name": "John Smith",
      "notes": "Verified by site supervisor.",
      "updatedAt": "2026-01-29T14:30:00.000000+00:00",
      "updatedBy": "USER123ABC"
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
