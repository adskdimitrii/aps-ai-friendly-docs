# status-step-sets

Source: https://aps.autodesk.com/en/docs/acc/reference/http/assets-status-step-sets-GET/

---

Status-Sets

GET

# status-step-sets

Searches for and returns all specified status sets.

This endpoint accepts a set of optional status set query parameters (described below), then uses those
parameters to search for and return status sets within a project that satisfy those parameters. If no
parameters are set, this endpoint returns all active status sets within a project.

The endpoint paginates returned status sets. If you donât specify pagination fields, your query will execute
using the default page size. If you want to specify a different a page size, use the `limit` query parameter.

A paginated response to a query includes pagination information that may contain a `nextUrl` field. Use the
URL it provides to request the next page in the query, then use the `nextUrl` field in that subsequent response
to request the next page in the query, and so on until the response contains no `nextUrl` value, which means
the query is finished returning objects. Note that you should not edit the `nextUrl` value to alter filter and
sort values.

If you want to create your own sequence of requests to retrieve all of a queryâs pages without using`nextUrl`, you can use the `cursorState` value returned by each request to specify where the next request
should start the next page.

To understand the basics of status sets, and the Assets settings that define them, see the [Assets Field Guide](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/assets/).

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/assets/v1/projects/{projectId}/status-step-sets |
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

| projectId   string | The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form âb.{UUID}â. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | The maximum number of objects that can be returned in a page. A request might return fewer objects than the limit if the Assets service runs out of specified objects to return - at the end of a set of paged results, for example. The maximum limit is `200`; the default limit is `25`. |
| --- | --- |
| cursorState   string | An opaque cursor token that identifies where the next page of paginated results should start. Itâs returned in each paginated response so that it can be supplied in the next request to continue paginated results. If a paginated response contains no `cursorState` value, then there are no further pages to return. <br>Omit this field to initiate a paginated request or to restart pagination. |
| includeDeleted   boolean | Whether or not soft-deleted object should be included in the response. If `true`, soft-deleted objects are returned. If `false`, they are not. The default is `false`. |
| filter[updatedAt]   string | A string that specifies a date and time or a date and time range at which all returned objects mast have been updated. A single date and time takes this format: `YYYY-MM-DDThh:mm:ss.SSSZ`, A date and time range takes this format: `YYYY-MM-DDThh:mm:ss.SSSZ..YYYY-MM-DDThh:mm:ss.SSSZ`. Range queries can be closed or open in either direction: `YYYY-MM-DDThh:mm:ss.SSSZ..` or `..YYYY-MM-DDThh:mm:ss.SSSZ`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully returned a page of status sets. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request header |
| 401   Unauthorized | The request was not accepted because it lacked valid authentication credentials |
| 403   Forbidden | The request was not accepted because the client is authenticated, but is not authorized to access the target resource |
| 404   Not Found | The resource cannot be found |
| 429   Too Many Requests | The request was not accepted because the rate limit was exceeded due to too many requests being made. |
| 500   Internal Server Error | An unexpected error occurred on the server |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| pagination   object |  |
| --- | --- |
| limit   int | The maximum number of objects that can be returned in a page. A request might return fewer objects than the limit if the Assets service runs out of specified objects to return - at the end of a set of paged results, for example. The maximum limit is `200`; the default limit is `25`. |
| cursorState   string | An opaque cursor token that identifies where the next page of paginated results should start. Itâs returned in each paginated response so that it can be supplied in the next request to continue paginated results. If a paginated response contains no `cursorState` value, then there are no further pages to return. <br>Omit this field to initiate a paginated request or to restart pagination. |
| nextUrl   string | A URL that requests the next page for this query. |
| results   array: object | Result status sets |
| id   string | The ID of the component. |
| createdAt   string | The time when the component was created (ISO8601 Date time format in UTC). |
| createdBy   string | The actor that created the component. This is an Autodesk / Oxygen ID. |
| updatedAt   string | The time when the component was last updated (ISO8601 Date time format in UTC). |
| updatedBy   string | The actor that last updated the component. This is an Autodesk / Oxygen ID. |
| deletedAt   string | The time when the component was deleted at (ISO8601 Date time format in UTC). |
| deletedBy   string | The actor that deleted the component. This is an Autodesk / Oxygen ID. |
| isActive   boolean | A flag indicating whether the component is active or inactive (`isActive` is `true` if-and-only-if `deletedAt` is empty). |
| version   int | A global sequence number that is incremented any time a component of this type is created, updated, or deleted. If you cache components, you can use the version value to compare the cached component to the same component online to see if the component has been updated. If the online component has a higher version value, it has been updated. |
| projectId   string: UUID | The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form âb.{UUID}â. |
| name   string | The display name for the status set. This name appears in the Assets UI when viewing status sets. <br>Max length: 100 |
| description   string | A description of the status set. <br>Max length: 500 |
| isDefault   boolean | Specifies if this is the status set that is assigned to categories by default - that is, this is the status set that will be assigned to categories if no other status set has been assigned, either explicitly or through inheritance. If `true`, itâs the default status set. If `false`, itâs not. |
| values   array: object | An array of statuses that belong to this status set. |
| label   string | The display label of the status. This label appears in the Assets UI when viewing statuses. The label must be unique within this status set, but does not need to be unique within the project (in other words, the same label can be used in multiple status sets in the same project). âUniquenessâ in this context means case-insensitive. |
| description   string | A description of the status. |
| color   string | The color of the status as the status appears in the Assets UI. <br>This field is not restricted as it is primarily a tool for the Assets UI to use.<br>However, there are only certain colors that the Autodesk Construction Cloud Assets UI knows how to operate with. Understood color values are: `adsk-black`, `adsk-white`, `adsk-charcoal-900`, `adsk-charcoal-800`, `adsk-charcoal-700`, `adsk-charcoal-600`, `adsk-charcoal-500`, `adsk-charcoal-400`, `adsk-charcoal-300`, `adsk-charcoal-200`, `adsk-charcoal-100`, `adsk-charcoal-050`, `adsk-blue-700`, `adsk-blue-500`, `adsk-blue-300`, `adsk-blue-100`, `adsk-red-700`, `adsk-red-500`, `adsk-red-300`, `adsk-green-700`, `adsk-green-500`, `adsk-green-300`, `adsk-yellow-orange-700`, `adsk-yellow-orange-500`, `adsk-yellow-orange-300`, `adsk-dark-blue-700`, `adsk-dark-blue-500`, `adsk-dark-blue-300`, `adsk-pink-700`, `adsk-pink-500`, `adsk-pink-300`, `adsk-turquoise-700`, `adsk-turquoise-500`, `adsk-turquoise-300`, `adsk-purple-700`, `adsk-purple-500`, `adsk-purple-300`, `adsk-salmon-700`, `adsk-salmon-500`, `adsk-salmon-300`, `adsk-brown-700`, `adsk-brown-500`, `adsk-brown-300`.<br>Using colors other than those specified here is not disallowed, but may result in unexpected behavior in<br>the Assets UI. |
| statusStepSetId   string: UUID | The ID of the status set to which the new status belongs. |
| id   string | The ID of the component. |
| createdAt   string | The time when the component was created (ISO8601 Date time format in UTC). |
| createdBy   string | The actor that created the component. This is an Autodesk / Oxygen ID. |
| updatedAt   string | The time when the component was last updated (ISO8601 Date time format in UTC). |
| updatedBy   string | The actor that last updated the component. This is an Autodesk / Oxygen ID. |
| deletedAt   string | The time when the component was deleted at (ISO8601 Date time format in UTC). |
| deletedBy   string | The actor that deleted the component. This is an Autodesk / Oxygen ID. |
| isActive   boolean | A flag indicating whether the component is active or inactive (`isActive` is `true` if-and-only-if `deletedAt` is empty). |
| version   int | A global sequence number that is incremented any time a component of this type is created, updated, or deleted. If you cache components, you can use the version value to compare the cached component to the same component online to see if the component has been updated. If the online component has a higher version value, it has been updated. |
| projectId   string: UUID | The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form âb.{UUID}â. |
| bucket   string | An immutable string assigned to a status on its creation, typically created by incorporating the statusâs label into a larger string that is guaranteed to be unique within a project. The bucket name remains the same for the life of the status, and doesnât change even if the label does. The bucket value is a useful tool for semantic identification. |
| sortOrder   int | A value that indicates the order of a status within its status set. Each status in the set has a sort order value that indicates its order relative to other statuses in the set. A status setâs sort order values donât necessarily start at 1, and may not be sequential. The only way to know a statusâs order within a set is to compare its sort order value with the sort order values of other statuses. |

## [Example](#example)

Successfully returned a page of status sets.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/assets/v1/projects/:projectId/status-step-sets?cursorState=eyJsaW1pdCI6MjUsIm9mZnNldCI6MjV9&includeDeleted=true&filter[updatedAt]=2020-05-01T06:00:00.000Z..' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 25,
    "cursorState": "eyJsaW1pdCI6MjUsIm9mZnNldCI6MjV9",
    "nextUrl": "https://developer.api.autodesk.com/construction/assets/v1/projects/04605b7a-0c53-421e-8e11-c743e75ac10a/assets?cursorState=eyJsaW1pdCI6MjUsIm9mZnNldCI6MjV9"
  },
  "results": [
    {
      "id": "b302d910-b5e3-46ba-81d8-6b6d30406e14",
      "createdAt": "2020-05-01T06:00:00.000Z",
      "createdBy": "LA7ZL85MU7ML",
      "updatedAt": "2020-05-01T06:00:00.000Z",
      "updatedBy": "LA7ZL85MU7ML",
      "deletedAt": "2020-05-01T06:00:00.000Z",
      "deletedBy": "LA7ZL85MU7ML",
      "isActive": true,
      "version": 1,
      "projectId": "f74a012c-62fd-4988-ac2b-c5b4fd937724",
      "name": "Spatiotemporal Status Set",
      "description": "My really cool status step set",
      "isDefault": false,
      "values": [
        {
          "label": "Functional-Testing",
          "description": "Custom Functional Testing Status",
          "color": "green",
          "statusStepSetId": "6eb35939-e5fb-453a-98ed-e2e11f326e73",
          "id": "b302d910-b5e3-46ba-81d8-6b6d30406e14",
          "createdAt": "2020-05-01T06:00:00.000Z",
          "createdBy": "LA7ZL85MU7ML",
          "updatedAt": "2020-05-01T06:00:00.000Z",
          "updatedBy": "LA7ZL85MU7ML",
          "deletedAt": "2020-05-01T06:00:00.000Z",
          "deletedBy": "LA7ZL85MU7ML",
          "isActive": true,
          "version": 1,
          "projectId": "f74a012c-62fd-4988-ac2b-c5b4fd937724",
          "bucket": "custom_functional_testing_status_1582935184385",
          "sortOrder": 1
        }
      ]
    }
  ]
}

```

Show More
