# containers/:containerId/relationships:intersect

Source: https://aps.autodesk.com/en/docs/acc/reference/http/relationship-service-v2-intersect-relationships-POST/

---

Relationship: Search

POST

# containers/:containerId/relationships:intersect

Retrieves a list of relationships that contain the specified relationship entities.

Also accepts a set of WITH entities, that allow filtering down of the relationships results set to those that have matching entities in the WITH collection.

The response contains a list of relationships that contain entities matching the search criteria.

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/bim360/relationship/v2/containers/:containerId/relationships:intersect |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| x-ads-region   enum: string | The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. <br>Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| containerId   string: UUID | The GUID that uniquely identifies the container. |
| --- | --- |

### Request

## [Query Parameters](#query-parameters)

| includeDeleted   boolean | Whether or not to include deleted relationships in the search. |
| --- | --- |
| onlyDeleted   boolean | Whether or not to only include deleted relationships in the search. |
| pageLimit   int | The maximum number of relationships to return in a page. If not set, the default page limit is used, as determined by the server. |
| continuationToken   string | The token indicating the start of the page. If not set, the first page is retrieved. |

### Request

## [Body Structure](#body-structure)

Expand all

| entities*   array: object | The list of entities to return relationships for. <br>Min items: 1 Max items: 20 |
| --- | --- |
| domain*   string | The domain to which the entity belongs. <br>To learn more about domains and entities, see the [Relationship Service Field Guide](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/relationships/).<br>Max length: 128 |
| type*   string | The type of entity. <br>Max length: 128 |
| id*   string | The unique identifier of the entity. <br>Max length: 512 |
| withEntities   array: object | The optional list of entities to filter returned relationships by. <br>Min items: 1 Max items: 20 |
| domain   string | The domain that the domain entity is a part of (must be supplied if `type` is supplied). <br>Max length: 128 |
| type   string | The type of the domain entity (must be supplied if `id` is supplied). <br>Max length: 128 |
| id   string | The identifier of the domain entity. <br>Max length: 512 |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Success |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource could not be found. |
| 415   Unsupported Media Type | The `Content-Type` header must be `application/json`. |
| 429   Too Many Requests | Rate limit exceeded; wait some time before retrying. The `Retry-After` header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| page   object | Paging information associated with a paging response. |
| --- | --- |
| continuationToken   string | A continuation token to retrieve the next page. |
| syncToken   string | The token that can be used to obtain data via the synchronization endpoint. |
| relationships   array: object | The list of relationships. <br>Max items: 100 |
| id   string: UUID | The UUID that uniquely identifies the relationship. |
| createdOn   datetime: ISO 8601 | The date and time the relationship was created. |
| isReadOnly   boolean | `true` if this relationship is read only for the current caller. <br>`false` if this relationship is not read only for the current caller. |
| isService   boolean | `true` if this relationship was created by a service. <br>`false` if this relationship was not created by a service. |
| isDeleted   boolean | `true` if this relationship is deleted. <br>`false` if this relationship is not deleted. |
| deletedOn   datetime: ISO 8601 | The date and time the relationship was deleted. |
| entities   array: object | The entities contained in the relationship. <br>Min items: 2 Max items: 2 |
| createdOn   datetime: ISO 8601 | The date and time the entity was created. |
| domain   string | The domain to which the entity belongs. <br>To learn more about domains and entities, see the [Relationship Service Field Guide](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/relationships/).<br>Max length: 128 |
| type   string | The type of entity. <br>Max length: 128 |
| id   string | The unique identifier of the entity. <br>Max length: 512 |

### Response

## [Body Structure (400)](#body-structure-400)

Expand all

| type   string | The error code. |
| --- | --- |
| title   string | A short title for the error. |
| detail   string | A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. |
| errors   array: object | A set of specific validation errors that need to be fixed. |
| field   string | The field that failed validation. |
| title   string | A short title for the error. |
| detail   string | A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. |
| type   string | The error code. |

## [Example #1 (no query parameters)](#example-1-no-query-parameters)

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/relationships:intersect' \
     -X POST \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "entities": [
             {
               "domain": "autodesk-bim360-asset",
               "type": "asset",
               "id": "b1d1e7d4-f0ed-11e9-81b4-2a2ae2dbcce4"
             }
           ],
           "withEntities": [
             {
               "domain": "autodesk-example-domain",
               "type": "example-type",
               "id": "b1d1e7d4-f0ed-11e9-81b4-2a2ae2dbcce4"
             }
           ]
         }'

```

Show More

## [Example #2 (with all query parameters)](#example-2-with-all-query-parameters)

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/f0f4f36a-ac64-687f-b132-8efe04b22454/relationships:intersect?includeDeleted=True&onlyDeleted=True&pageLimit=134&continuationToken=10' \
     -X POST \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "entities": [
             {
               "domain": "autodesk-bim360-asset",
               "type": "asset",
               "id": "b1d1e7d4-f0ed-11e9-81b4-2a2ae2dbcce4"
             }
           ],
           "withEntities": [
             {
               "domain": "autodesk-example-domain",
               "type": "example-type",
               "id": "b1d1e7d4-f0ed-11e9-81b4-2a2ae2dbcce4"
             }
           ]
         }'

```

Show More

### Response (200)

```
{
  "page": {
    "continuationToken": "10",
    "syncToken": "eyAibGFzdENoZWNrZWQiOiIyMDE5LTEwLTE4VDEyOjEwOjA3Ljc5NloiIH0="
  },
  "relationships": [
    {
      "id": "74b70bb8-8802-a1fd-f201-890375a60c8f",
      "createdOn": "2015-10-21T16:32:22Z",
      "isReadOnly": true,
      "isService": false,
      "isDeleted": false,
      "entities": [
        {
          "domain": "autodesk-bim360-asset",
          "type": "asset",
          "id": "2b95ba7a-3df5-4e99-a693-9c7cc15ee8c0",
          "createdOn": "2021-07-29T11:39:12+01:00"
        },
        {
          "domain": "autodesk-bim360-documentmanagement",
          "type": "documentlineage",
          "id": "urn:adsk.wipprod:dm.lineage:hC6k4hndRWaeIVhIjvHu8w",
          "createdOn": "2021-07-29T13:39:12+01:00"
        }
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
