# assets V2

Source: https://aps.autodesk.com/en/docs/acc/reference/http/assets-assets-v2-GET/

---

Assets

GET

# assets V2

Searches for and returns all specified assets within a project visible to the authenticated user.

This endpoint accepts a set of optional asset property filters, then uses supplied filters to search for and
return assets within a project that satisfy those filters. If no filters are set, this endpoint returns all
assets within a project.

The endpoint paginates returned assets. If you don’t specify pagination fields, your query will execute using
the default page size. If you want to specify a different a page size, use the `limit` query parameter.

A paginated response to a query includes pagination information that may contain a `nextUrl` field. Use the
URL it provides to request the next page in the query, then use the `nextUrl` field in that subsequent response
to request the next page in the query, and so on until the response contains no `nextUrl` value, which means
the query is finished returning objects. Note that you should not edit the `nextUrl` value to alter filter and
sort values.

If you want to create your own sequence of requests to retrieve all of a query’s pages without using`nextUrl`, you can use the `cursorState` value returned by each request to specify where the next request
should start the next page.

To understand the basics of assets and the Assets settings that define them, see the [Assets Field Guide](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/assets/).

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/assets/v2/projects/{projectId}/assets |
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

| projectId   string | The Forma project ID. Must be a UUID or a project ID of the form “b.{UUID}”. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| cursorState   string | An opaque cursor token that identifies where the next page of paginated results should start. It’s returned in each paginated response so that it can be supplied in the next request to continue paginated results. If a paginated response contains no `cursorState` value, then there are no further pages to return. <br>Omit this field to initiate a paginated request or to restart pagination. |
| --- | --- |
| limit   int | The maximum number of objects that can be returned in a page. A request might return fewer objects than the limit if the Assets service runs out of specified objects to return - at the end of a set of paged results, for example. The maximum limit is `200`; the default limit is `25`. |
| filter[categoryId]   array | An exploded array of category IDs to which all returned objects must belong. For example, `?filter[categoryId]=123&filter[categoryId]=456`. |
| filter[statusLabel]   array | An exploded array of status labels. Each returned object must have one of the statuses bearing any of these labels, case-insensitive. For example, `?filter[statusLabel]=ordered&filter[statusLabel]=delivered`. |
| filter[statusId]   array | An exploded array of status IDs. Each returned object must have one of the statuses specified by the IDs. For example, `?filter[statusId]=84eb6a10-dde3-475f-aaf4-b5df3aebbd0b&filter[statusId]=5ba5c1af-fcd6-4506-b5e4-f20f5321dd69`. |
| filter[locationId]   array | An exploded array of location IDs. Each returned object must be associated with one of the locations specified by the IDs. To specify sub-locations of a location, provide a single location ID here and then set the `includeSubLocations` field in the request to `true`. For example, `?filter[locationId]=826e102a-36de-41e7-8c58-1b1696ccbba8&filter[locationId]=cee49807-fcc4-43ae-80a2-8ca819dfa70d`. |
| filter[customAttributes]   object | A custom attribute and value that each returned object must have. This filter is keyed by the custom attribute’s name field and set equal to the desired value. As an example, `?filter[customAttributes][ca1]=true`. Use this field multiple times to specify more than one custom attribute filter. <br>The value supplied for a custom attribute filter must match the type specified by the attribute. Values can be:  > A single value, or exploded array of values, of string, boolean, or number (for `text`, `numeric`, `date`, `boolean`, `select`, or `multi_select` types). Note that a string value for a `text` data type will perform a case-insensitive, substring match.A range of values (inclusive) in the form: `startValue..endValue` (for `numeric` or `date` Types).Partial ranges (inclusive): `...endValue` or `startValue..` (for `numeric` or `date` Types).<br>Select and Multi-Select filters should use Custom Attribute Value IDs as values.<br>Note that explicit value filters and range filters for a given attribute cannot be used in conjunction.<br>Examples (without URL escaping) >  > Example 1) Filter a `boolean` custom attribute: > :   `?filter[customAttributes][ca1]=true` >  > Example 2) Filter a `numeric` range custom attribute: > :   `?filter[customAttributes][ca2]=1..5` >  > Example 3) Filter a `date` custom attribute to on or before a given date: > :   `?filter[customAttributes][ca3]=..2020-11-01` >  > Example 4) Filter a `select` custom attribute: > :   `?filter[customAttributes][ca4]=b959daad-4d00-4209-9acc-e900ac5832cf` >  > Example 5) Filter a `multi_select` custom attribute to multiple values: > :   `?filter[customAttributes][ca5]=63801bb7-db1f-49bf-9000-a392a5879f22&filter[customAttributes][ca5]=757d0934-a4a0-4af8-821d-64d611e84a56` >  > Example 6) Filter a `text` custom attribute to a given input: > :   `?filter[customAttributes][ca6]=Some text input` |
| filter[searchText]   string | A string that must be contained within any of a returned object’s searchable text fields, including text custom attributes. `searchText` is case-insensitive, and will match substrings as well as full strings. |
| filter[updatedAt]   string | A string that specifies a date and time or a date and time range at which all returned objects mast have been updated. A single date and time takes this format: `YYYY-MM-DDThh:mm:ss.SSSZ`, A date and time range takes this format: `YYYY-MM-DDThh:mm:ss.SSSZ..YYYY-MM-DDThh:mm:ss.SSSZ`. Range queries can be closed or open in either direction: `YYYY-MM-DDThh:mm:ss.SSSZ..` or `..YYYY-MM-DDThh:mm:ss.SSSZ`. |
| sort   string | A string that specifies how to sort returned objects. The string provides a valid API field name with an optional direction, either `asc` (ascending) or `desc` (descending). In the case of custom attributes, use dot notation to specify the attribute by name—for example, `customAttributes.ca3 desc`. The string may contain multiple comma-separated expressions for secondary sorts. The default sort order is `asc` if not provided. |
| includeCustomAttributes   boolean | Specifies whether or not returned assets include custom attributes or not. If `true`, they’re included. If `false`, they’re not. Default is `false`. |
| includeDeleted   boolean | Whether or not soft-deleted object should be included in the response. If `true`, soft-deleted objects are returned. If `false`, they are not. The default is `false`. |
| includeSubLocations   boolean | Specifies whether or not to consider sub-locations when filtering by `locationId`. For this setting to work, the request must contain only a single for `filter[locationId]`. If `true`, the search looks for assets within the specified location and in all the sub-locations of the specified location. If `false`, the search looks for assets only within the specified location(s). Default is `false`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully returned a page of assets. |
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
| cursorState   string | An opaque cursor token that identifies where the next page of paginated results should start. It’s returned in each paginated response so that it can be supplied in the next request to continue paginated results. If a paginated response contains no `cursorState` value, then there are no further pages to return. <br>Omit this field to initiate a paginated request or to restart pagination. |
| nextUrl   string | A URL that requests the next page for this query. |
| results   array: object | Result assets |
| id   string | The ID of the component. |
| createdAt   string | The time when the component was created (ISO8601 Date time format in UTC). |
| createdBy   string | The actor that created the component. This is an Autodesk / Oxygen ID. |
| updatedAt   string | The time when the component was last updated (ISO8601 Date time format in UTC). |
| updatedBy   string | The actor that last updated the component. This is an Autodesk / Oxygen ID. |
| deletedAt   string | The time when the component was deleted at (ISO8601 Date time format in UTC). |
| deletedBy   string | The actor that deleted the component. This is an Autodesk / Oxygen ID. |
| isActive   boolean | A flag indicating whether the component is active or inactive (`isActive` is `true` if-and-only-if `deletedAt` is empty). |
| version   int | A global sequence number that is incremented any time a component of this type is created, updated, or deleted. If you cache components, you can use the version value to compare the cached component to the same component online to see if the component has been updated. If the online component has a higher version value, it has been updated. |
| clientAssetId   string | An identifying name for the asset such as “laundry 220V outlet”. The name need not be unique, and shouldn’t be confused with the asset ‘id’ field, which is created and assigned when the asset is created. This value appears as “Asset ID” in the Assets UI, and may sometimes be called “Name” in asset exports. |
| categoryId   string | The ID of the category to which the asset belongs. |
| statusId   string: UUID | The ID of the status assigned to the asset. The status must belong to the status set specified by the asset’s category. |
| description   string | A brief description of the asset. Currently limited to `1000` characters. |
| locationId   string: UUID | The ID of the location of the asset. This value is supplied through the Locations API. |
| barcode   string | A string that lists a barcode value that may be assigned to the asset. The string uses whatever format your barcode system supports. |
| customAttributes   object | An optional JSON dictionary specifying one or more custom attributes and values to be assigned to the asset. The custom attributes must belong to the set of custom attributes specified by the asset’s category. <br>The dictionary is a set of key:value pairs that each starts with the unique custom attribute name (not to be confused with the custom attribute’s display name) followed by the attribute value. The value must use the data type defined by the attribute:<br>For `text`, the value is a string.<br>For `date`, the value is an ISO8601 date string with no time, for example, “2020-04-10”.<br>For `select`, the value is a valid ID from the list of values defined for this custom attribute.<br>For `multi-select`, the value is an array of valid IDs from the list of values defined for this custom attribute.<br>For `boolean`, the value is a boolean.<br>For `numeric`, the value is a string that parses as a valid floating point number (not localized). |
| *   one of |  |
| 0   string | A String value <br>Max length: 250 |
| 1   array: string | An array of String values |
| 2   boolean | A Boolean value |
| companyId   string: UUID | The ID of the company to which the creating user belongs in the project. |

## [Example](#example)

Successfully returned a page of assets.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/assets/v2/projects/:projectId/assets?cursorState=eyJsaW1pdCI6MjUsIm9mZnNldCI6MjV9&filter[customAttributes]=[object Object]&filter[searchText]=Air Handler&filter[updatedAt]=2020-05-01T06:00:00.000Z..&sort=createdAt asc,clientAssetId desc&includeCustomAttributes=true&includeDeleted=true' \
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
      "clientAssetId": "MVS-3D2",
      "categoryId": "42",
      "statusId": "84eb6a10-dde3-475f-aaf4-b5df3aebbd0b",
      "description": "AC unit for basement",
      "locationId": "826e102a-36de-41e7-8c58-1b1696ccbba8",
      "barcode": "F0086728",
      "customAttributes": {
        "ca1": true,
        "ca2": 6.5,
        "ca4": "688f8cfb-0eb4-4289-9d18-96007875dec3",
        "ca5": [
          "9e653094-8d9e-4050-a97a-24d9c5a3786f",
          "e88357bc-e3dd-4cd8-a9e2-6d659b301e7f"
        ],
        "ca6": "text value"
      },
      "companyId": "07b5f07d-c54a-4236-a086-f84192fabdb3"
    }
  ]
}

```

Show More
