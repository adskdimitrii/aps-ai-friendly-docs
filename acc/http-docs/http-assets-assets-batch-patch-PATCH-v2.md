# assets:batch-patch V2

Source: https://aps.autodesk.com/en/docs/acc/reference/http/assets-assets-batch-patch-PATCH-v2/

---

Assets

PATCH

# assets:batch-patch V2

Updates a set of one or more assets.

This endpoint accepts a set of key:value pairs. Each pair specifies an asset and then provides one or more
asset attribute updates for the asset.

Each attribute revision is a key:value pair that specifies an attribute and the value to assign to the
attribute.

To understand the basics of assets and the Assets settings that define them, see the [Assets Field Guide](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/assets/).

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/construction/assets/v2/projects/{projectId}/assets:batch-patch |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` `data:create` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string | The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form “b.{UUID}”. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

An object keyed by Asset IDs with values that are PatchAssetV2 entities

| object | The request payload for updating an asset V2. The payload is a set of key:value pairs. The key is the asset ID of the asset to revise. The value is a set of one or more asset attributes to revise. <br>Each attribute revision is itself a key:value pair. The key is the attribute name (one of the asset fields supplied in a request to [POST assets:batch-create V2](http-assets-assets-batch-create-POST-v2.md)).<br>The value is any permissible defined value for the field as described in [POST assets:batch-create V2](http-assets-assets-batch-create-POST-v2.md). |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully updated specified assets and returned properties of updated assets. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request header |
| 401   Unauthorized | The request was not accepted because it lacked valid authentication credentials |
| 403   Forbidden | The request was not accepted because the client is authenticated, but is not authorized to access the target resource |
| 404   Not Found | The resource cannot be found |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the target resource |
| 429   Too Many Requests | The request was not accepted because the rate limit was exceeded due to too many requests being made. |
| 500   Internal Server Error | An unexpected error occurred on the server |

### Response

## [Body Structure (200)](#body-structure-200)

| object | The response is a set of key:value pairs. The key is the asset ID of the asset that was revised. The value is the fully revised asset. |
| --- | --- |

## [Example](#example)

Successfully updated specified assets and returned properties of updated assets.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/assets/v2/projects/:projectId/assets:batch-patch' \
  -X 'PATCH' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "286c1ef7-70f6-4ebd-8f87-e7f591ec6b1f": {
          "clientAssetId": "AH-1000",
          "categoryId": "42",
          "statusId": "5cd53aeb-6657-4fb3-a077-f700fb29e644",
          "customAttributes": {
            "ca1": true,
            "ca5": [
              "f3a084e3-3531-40a7-9dce-3a17012443c7",
              "b5ee90c1-6e5d-41f2-83da-e54bf4331a8a"
            ],
            "ca6": "Updated text value"
          }
        },
        "4a125d1b-0803-408e-ab8b-ccdd159b8ca8": {
          "clientAssetId": "VACUUM-9000",
          "description": "The new Vacuum 9000",
          "locationId": "8500bd50-d25d-41a4-a686-cfa32d9a7dd4",
          "barcode": "F00086728"
        }
      }'

```

Show More

### Response

```
{
  "286c1ef7-70f6-4ebd-8f87-e7f591ec6b1f": {
    "id": "286c1ef7-70f6-4ebd-8f87-e7f591ec6b1f",
    "version": "2,",
    "clientAssetId": "AH-1000",
    "categoryId": "42",
    "statusId": "5cd53aeb-6657-4fb3-a077-f700fb29e644",
    "companyId": "212c9e25-f020-45c1-b93f-5c3d8af66ecb",
    "description": "AC unit for basement",
    "locationId": "826e102a-36de-41e7-8c58-1b1696ccbba8",
    "barcode": "DR025SGPT",
    "customAttributes": {
      "ca1": true,
      "ca2": 128,
      "ca3": "1989-11-09",
      "ca4": "9e6de5b0-f0d3-4eea-9b9c-efb14423f03e",
      "ca5": [
        "f3a084e3-3531-40a7-9dce-3a17012443c7",
        "b5ee90c1-6e5d-41f2-83da-e54bf4331a8a"
      ],
      "ca6": "Updated text value"
    },
    "isActive": "true,",
    "createdAt": "2020-05-01T06:00:00.000Z",
    "createdBy": "LA7ZL85MU7ML",
    "updatedAt": "2020-05-01T06:00:00.000Z",
    "updatedBy": "LA7ZL85MU7ML"
  },
  "4a125d1b-0803-408e-ab8b-ccdd159b8ca8": {
    "id": "4a125d1b-0803-408e-ab8b-ccdd159b8ca8",
    "version": "2,",
    "clientAssetId": "VACUUM-9000",
    "categoryId": "12",
    "statusId": "f27c6e60-327c-4b22-b430-a77c5ece70e5",
    "companyId": "212c9e25-f020-45c1-b93f-5c3d8af66ecb",
    "description": "The new Vacuum 9000",
    "locationId": "e4f7c1d5-0517-46ff-912b-65a05ecd839a",
    "barcode": "F00086728",
    "customAttributes": {
      "ca11": "2020-10-31",
      "ca13": "6867e8ad-4a05-45da-82a1-17f89902f0b9",
      "ca14": "some text input"
    },
    "isActive": "true,",
    "createdAt": "2020-05-01T06:00:00.000Z",
    "createdBy": "LA7ZL85MU7ML",
    "updatedAt": "2020-05-01T06:00:00.000Z",
    "updatedBy": "LA7ZL85MU7ML"
  }
}

```

Show More
