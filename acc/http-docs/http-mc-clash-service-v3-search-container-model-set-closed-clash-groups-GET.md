# containers/:containerId/modelsets/:modelSetId/clashes/closed

Source: https://aps.autodesk.com/en/docs/acc/reference/http/mc-clash-service-v3-search-container-model-set-closed-clash-groups-GET/

---

Clash Test: Closed Clash Groups

GET

# containers/:containerId/modelsets/:modelSetId/clashes/closed

Retrieves a list of closed clash groups in a given model set which match the provided search parameters.

The response contains a list of matching closed clash groups, restricted by the number specified by the `pageLimit` property. If set (that is, if there are more results than can be displayed at once), you can provide the `continuationToken` property in the response in a separate call to retrieve additional results.

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/bim360/clash/v3/containers/:containerId/modelsets/:modelSetId/clashes/closed |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-ads-region   enum: string | The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. <br>Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The GUID that uniquely identifies the container. |
| --- | --- |
| modelSetId   string: UUID | The GUID that uniquely identifies the model set. |

### Request

## [Query Parameters](#query-parameters)

| pageLimit   int | The maximum number of closed clash groups to return in a page. If not set, the default page limit is used, as determined by the server. |
| --- | --- |
| continuationToken   string | The token indicating the start of the page. If not set, the first page is retrieved. |
| clashTestId   string: UUID | Filters the returned closed clash groups by the clashTestId property. |
| reason   string | Filters the returned closed clash groups by the reason property. |
| createdBy   string | Filters the returned closed clash groups by the createdBy property. |
| after   datetime: ISO 8601 | Filters the returned closed clash groups to those created or modified after the given time. |
| before   datetime: ISO 8601 | Filters the returned closed clash groups to those created or modified before the given time. |
| sort   enum: string | Defines the sort direction. Possible values: `Asc`, `Desc`. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Success |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource could not be found. |
| 429   Too Many Requests | Rate limit exceeded; wait some time before retrying. The `Retry-After` header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| page   object | Paging information associated with a paging response. |
| --- | --- |
| continuationToken   string | A continuation token to retrieve the next page. |
| groups   array: object | The set of closed clash groups on this page. |
| id   string: UUID | The unique identifier of the closed clash group. |
| clashTestId   string: UUID | The unique identifier of the clash test associated with the closed clash group. |
| title   string | The title of the closed clash group. Max length: 128. |
| description   string | The description of the closed clash group. Max length: 1024. |
| reason   enum: string | The reason for closing this clash group. Possible values: `OTHER`, `VALID_INTERFACE`, `VALID_PENETRATION`, `MINIMAL_OVERLAP`, `ITEM_CAN_FLEX`, `MODEL_INACCURACY`, `FIELD_FIX`. |
| screenShots   array: string: UUID | The unique identifiers of screenshots associated with the closed clash group. Max items: 5. |
| createdBy   string | The unique identifier of the user who created the closed clash group. |
| createdOn   datetime: ISO 8601 | The date and time that the closed clash group was created. |
| clashes   array: int | The clashes included in the closed clash group. Min items: 1 Max items: 1000. |

### Response

## [Body Structure (400)](#body-structure-400)

Expand all

| type   string | The error code. |
| --- | --- |
| title   string | A short title for the error. |
| detail   string | A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. |
| errors   array: object | A set of specific validation errors that need to be fixed. |
| field   string | The field which failed validation. |
| title   string | A short title for the error. |
| detail   string | A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. |
| type   string | The error code. |

## [Example #1 (no query parameters)](#example-1-no-query-parameters)

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/clash/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/modelsets/00fb28a5-e8a4-2755-562a-7c2f0fc87911/clashes/closed' \
     -H 'Authorization: Bearer <token>'

```

## [Example #2 (with all query parameters)](#example-2-with-all-query-parameters)

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/clash/v3/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/modelsets/00fb28a5-e8a4-2755-562a-7c2f0fc87911/clashes/closed?pageLimit=134&continuationToken=10&clashTestId=21469f89-986a-c194-ae45-cefade1c7bde&reason=VALID_INTERFACE&createdBy=PD23PXGV8V3V&after=2015-10-21T16%3a30%3a39Z&before=2015-10-21T16%3a29%3a47Z&sort=Asc' \
     -H 'Authorization: Bearer <token>'

```

### Response (200)

```
{
  "page": {},
  "groups": [
    {
      "id": "74b70bb8-8802-a1fd-f201-890375a60c8f",
      "clashTestId": "21469f89-986a-c194-ae45-cefade1c7bde",
      "title": "Ceiling 2' x 2' grid and 411 other objects.",
      "description": "Objects expected in ceiling.",
      "reason": "OTHER",
      "screenShots": [
        "d98c1dd4-008f-04b2-e980-0998ecf8427e"
      ],
      "createdBy": "PD23PXGV8V3V",
      "createdOn": "2015-10-21T16:32:22Z",
      "clashes": [
        2019963136
      ]
    }
  ]
}

```

Show More

### Response (400)

```
{
  "type": "BadInput",
  "title": "One or more input values in the request were bad",
  "detail": "The following parameters are invalid: containerId",
  "errors": [
    {
      "field": "containerId",
      "title": "Invalid parameter",
      "detail": "The value 'testing' is not valid.",
      "type": "BadInput"
    }
  ]
}

```

Show More
