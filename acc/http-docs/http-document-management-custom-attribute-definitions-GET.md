# projects/{project_id}/folders/{folder_id}/custom-attribute-definitions

Source: https://aps.autodesk.com/en/docs/acc/reference/http/document-management-custom-attribute-definitions-GET/

---

Custom Attributes (beta)

GET

# projects/{project_id}/folders/{folder_id}/custom-attribute-definitions

Retrieves a complete list of custom attribute definitions for all the documents in a specific folder, including custom attributes that have not been assigned a value, as well as the potential drop-down (`array`) values.

To assign values to a documentâs custom attributes or to clear custom attribute values, call [POST custom-attributes:batch-update](http-document-management-custom-attributesbatch-update-POST.md).

To retrieve the values that were assigned to a documentâs custom attributes, call [POST versions:batch-get](http-document-management-versionsbatch-get-POST.md).

For more details about custom attributes, see the [Update Custom Attributes](https://aps.autodesk.com/en/docs/bim360/v1/tutorials/document-management/download-document/update-custom-attribute-values/) tutorial.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/bim360/docs/v1/projects/:project_id/folders/:folder_id/custom-attribute-definitions |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-user-id   string | In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| project_id   string: UUID | The ID of the project. This corresponds to the project ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/). To convert a project ID in the Data Management API to a project ID in the BIM 360 API you need to remove the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |
| folder_id   string | The URL-encoded ID (URN) of the folder. <br>For details about how to find the URN, follow the initial steps (1-3) of the [Download Files](https://aps.autodesk.com/en/docs/bim360/v1/tutorials/document-management/download-document-s3/) tutorial. |

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | The number of results to return in the response. Acceptable values: 1-200. Default value: 10. For example, to limit the response to two custom attributes per page, use `limit=2`. |
| --- | --- |
| offset   int | The item number that you want to begin results from. Default value: 0. For example, to begin the results from item three, use `offset=3`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the list of custom attribute definitions. |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The project or folder does not exist. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | The list of results. |
| --- | --- |
| id   int | The ID of the attribute. |
| name   string | The name of the attribute. |
| type   enum:string | The type of attribute. Possible values: `string` (text field), `date`, `array` (drop-list). |
| arrayValues   array: string | A list of possible values for the attribute. Only relevant for drop-list attributes. |
| pagination   object | Pagination information when data must be returned page by page. |
| limit   int | The number of results to return in the response. |
| offset   int | The item number that the results begin from. |
| totalResults   int | Total number of results. |
| previousUrl   string | The URL for the previous page of results. |
| nextUrl   string | The URL for the next page of results. |

## [Example](#example)

Successfully retrieved the list of custom attribute definitions.

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/docs/v1/projects/c0337487-5b66-422b-a284-c273b424af54/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.9g7HeA2wRqOxLlgLJ40UGQ/custom-attribute-definitions' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "results": [
    {
      "id": 1001,
      "name": "Drawing Stage",
      "type": "string"
    },
    {
      "id": 1002,
      "name": "Publish Date",
      "type": "date"
    },
    {
      "id": 1003,
      "name": "Drawing Type",
      "type": "array",
      "arrayValues": [
        "Details",
        "General",
        "Plans",
        "Schedules"
      ]
    },
    {
      "id": 1004,
      "name": "Original Number",
      "type": "string"
    }
  ],
  "pagination": {
    "limit": 100,
    "offset": 200,
    "totalResults": 500,
    "previousUrl": "",
    "nextUrl": ""
  }
}

```

Show More
