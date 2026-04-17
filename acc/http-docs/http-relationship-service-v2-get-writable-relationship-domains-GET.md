# utility/relationships:writable

Source: https://aps.autodesk.com/en/docs/acc/reference/http/relationship-service-v2-get-writable-relationship-domains-GET/

---

Relationship: Utilities

GET

# utility/relationships:writable
> Retrieves a list of entity types that are compatible with each other, to establish whether you can create relationships between them or to delete those relationships. For example, between an asset and a document.

Note that some entity types belong to a `bim360` domain, and others to a `construction` domain.

To learn how this endpoint is used, see the [Create a Relationship tutorial](../how-to-docs/relationships-relationships-create.md).

  Note that this endpoint is compatible with both BIM 360 and Forma projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/bim360/relationship/v2/utility/relationships:writable |
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

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Success |
| --- | --- |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 429   Too Many Requests | Rate limit exceeded; wait some time before retrying. The `Retry-After` header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| domain   string | The domain to which the entity types belong. <br>For example: `autodesk-bim360-asset`<br>To learn more about domains and entities, see the [Relationship Service Field Guide](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/relationships/). |
| --- | --- |
| entityTypes   array: object | The list of entity types in the domain. |
| entityType   string | An individual entity type. <br>For example: `asset`. |
| allow   array: object | The allow list for the entity type. |
| domain   string | The domain containing the allowed entity types. |
| entityTypes   array: string | The allowed entity types. |

## [Example](#example)

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/utility/relationships:writable' \
     -H 'Authorization: Bearer <token>'

```

### Response (200)

```
[
  {
    "domain": "autodesk-bim360-asset",
    "entityTypes": [
      {
        "entityType": "asset",
        "allow": [
          {
            "domain": "autodesk-bim360-documentmanagement",
            "entityTypes": [
              "documentlineage"
            ]
          }
        ]
      }
    ]
  }
]

```

Show More
