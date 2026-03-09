# custom-attributes

Source: https://aps.autodesk.com/en/docs/acc/reference/http/rfis-attributes-GET/

---

Custom Attributes

GET

# custom-attributes

Retrieves all custom attribute definitions for a project.

Use this endpoint to list available attributes and their allowed values when creating or updating RFIs.

For more information on setting up custom attributes, see the [Custom RFI Fields](https://help.autodesk.com/view/BUILD/ENU/?guid=Custom_RFI_Fields) help topic.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/attributes |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | The number of RFIs to return in the response. Acceptable values: `1â200`. Default: `10`. For example, to limit the response to two items per page, use `limit=2` |
| --- | --- |
| offset   int | The number of items to skip before starting to return results. <br>For example, to begin the results from the fourth item, use `offset=3`. |
| filter[status]   array: string | Filters the response to only include custom attributes with the specified status. Possible values: `active`, `inactive`, `hidden`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Success |
| --- | --- |
| 400   Bad Request | The parameters are invalid |
| 401   Unauthorized | The provided bearer token is not valid |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation |
| 500   Internal Server Error | An unknown error occurred on the server |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | The list of custom attributes. |
| --- | --- |
| id   string: UUID | The ID of the custom attribute definition. |
| name   string | The name of the custom attribute as displayed in the UI. <br>Max length: 50 |
| type   enum:string | The type of the attribute. Possible values: `text`, `numeric` |
| description   string | The description of the attribute as shown in the UI. <br>Max length: 1000 |
| status   enum:string | The display status of the attribute in the UI. Possible values: `active`, `inactive`, `hidden`. |
| multipleChoice   boolean | `true`: users can select more than one value for this attribute. <br>`false`: (default) users can select only one value. |
| possibleValues   array: object | A list of possible values for the attribute. |
| id   string: UUID | The unique ID of the attribute value. |
| name   string,integer,null | The name of the attribute value as shown in the UI. <br>Max length: 100 |
| pagination   object | The pagination object. |
| limit   int | The number of items returned per page. |
| offset   int | The number of items skipped before this page of results. |
| totalResults   int | The total number of items matching the request. |

## [Example](#example)

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/rfis/v3/projects/:projectId/attributes' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "results": [
    {
      "id": "c911852d-5957-4145-9c8d-e7cfe9d564df",
      "name": "Attribute 1",
      "type": "text",
      "description": "This is a description of the attribute",
      "status": "active",
      "multipleChoice": false,
      "possibleValues": [
        {
          "id": "c911852d-5957-4145-9c8d-e7cfe9d564df",
          "name": "Value 1"
        }
      ]
    }
  ],
  "pagination": {
    "limit": 10,
    "offset": 0,
    "totalResults": 97
  }
}

```

Show More
