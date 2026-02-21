# projects/{project_id}/versions/{version_id}/custom-attributes:batch-update

Source: https://aps.autodesk.com/en/docs/acc/reference/http/document-management-custom-attributesbatch-update-POST/

---

Custom Attributes (beta)

POST

# projects/{project_id}/versions/{version_id}/custom-attributes:batch-update

Assigns values to custom attributes for multiple documents. This endpoint also clears custom attribute values.

For information about custom attributes, see the [Help documentation](http://help.autodesk.com/view/BIM360D/ENU/?guid=GUID-244FAB32-8E3B-4D1B-A1EB-C982DB93ABB3).

To retrieve values that were assigned to a documentâs custom attributes, call [POST versions:batch-get](/en/docs/bim360/v1/reference/http/document-management-versionsbatch-get-POST/).

To retrieve the full list of the documentâs custom attributes including custom attributes that have not been assigned a value, call [GET custom-attribute-definitions](/en/docs/bim360/v1/reference/http/document-management-custom-attribute-definitions-GET/).

For more details about custom attributes, see the [Update Custom Attributes](/en/docs/bim360/v1/tutorials/document-management/download-document/update-custom-attribute-values) tutorial.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/bim360/docs/v1/projects/:project_id/versions/:version_id/custom-attributes:batch-update |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](/en/docs/oauth/v2/tutorials/get-2-legged-token) or [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| x-user-id   string | In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| project_id   string: UUID | The ID of the project. This corresponds to the project ID in the [Data Management API](/en/docs/data/v2/). To convert a project ID in the Data Management API to a project ID in the BIM 360 API you need to remove the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |
| version_id   string | The URL-encoded ID (URN) of the version. To find the version ID of a document follow the initial steps of the [Download Files](/en/docs/bim360/v1/tutorials/document-management/download-document-s3/) tutorial. |

### Request

## [Body Structure](#body-structure)

| id*   string | The ID of the custom attribute. To find the ID, call [GET custom-attribute-definitions](/en/docs/bim360/v1/reference/http/document-management-custom-attribute-definitions-GET/). |
| --- | --- |
| value*   string | The value of the custom attribute. If you are assigning a value to a drop-list attribute, call [GET custom-attribute-definitions](/en/docs/bim360/v1/reference/http/document-management-custom-attribute-definitions-GET/) to retrieve a list of possible values. If you are clearing a custom attribute value, assign a `null` value to the attribute. <br>For text field (`string`) attributes, the max length is 255.Date attributes need to be compliant with ISO8601. Milliseconds are discarded. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully updated the custom attribute values. |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The project or version does not exist. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | The list of results. |
| --- | --- |
| id   int | The ID of the attribute. |
| type   enum:string | The data type of the attribute. Possible values: `string` (text field), `date`, `array` (drop-list). |
| name   string | The name of the attribute. |
| value   string | The value of the attribute. |

## [Example](#example)

Successfully updated the custom attribute values.

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/docs/v1/projects/c0337487-5b66-422b-a284-c273b424af54/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.AS3XD9MzQvu4MakMF-w7vQ%3Fversion%3D1/custom-attributes:batch-update' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '[
        {
          "id": 1001,
          "value": "checked"
        },
        {
          "id": 1002,
          "value": "2020-03-31T16:00:00.000Z"
        },
        {
          "id": 1003,
          "value": "v2"
        }
      ]'

```

Show More

### Response

```
{
  "results": [
    {
      "id": 1001,
      "name": "column1",
      "type": "string",
      "value": "checked"
    },
    {
      "id": 1002,
      "name": "column2",
      "type": "date",
      "value": "2020-03-31T16:00:00.000Z"
    },
    {
      "id": 1003,
      "name": "column3",
      "type": "array",
      "value": "v2"
    },
    {
      "id": 1004,
      "name": "column4",
      "type": "string",
      "value": "anything"
    }
  ]
}

```

Show More
