# Retrieve ACC Assets Data

Source: https://aps.autodesk.com/en/docs/acc/tutorials/assets/retrieve-assets-data/

---

# Retrieve ACC Assets Data

This tutorial demonstrates how to fetch your complete set of Autodesk Construction Cloud Asset data and project settings. This can be for the entirety of your Asset data, or filtered to a subset of Asset data.

This set will include the assets themselves, as well as all of the surrounding Asset project settings:

- categories
- status sets / Asset statuses
- Asset custom attributes
- Assignments of status sets and Asset custom attributes to categories

Usage of pagination and batch-fetch endpoints are subject to rate limiting. For more details on Assets API rate limits, see the [Assets Rate Limits](https://aps.autodesk.com/en/docs/acc/v1/overview/rate-limits/assets-rate-limits/).

## [Pagination](#pagination)

Most of the endpoints detailed below are paginated. Assets API uses cursor-based pagination, in which an opaque `cursorState` token is used to track the state of the pagination. Each paginated response will contain a `results` section, in which the relevant entities themselves will be returned, and a `pagination` section which will return the information needed to continue the pagination to fetch the full set of result entities. Pagination fields are described as follows -

| Field | Description |
| --- | --- |
| `limit` | The maximum number of entities that MAY be returned for the pagination request in the `results` section. The `results` MAY contain less than the `limit` due to filtering or for other reasons. Can be passed into any pagination request to limit the number of `results` returned. |
| `offset` | The offset of the first entity returned in the `results` section. The `offset` is returned for reference, but cannot be passed in explicitly for pagination requests (the offset is computed automatically from the `cursorState`). |
| `cursorState` | An opaque token to identify the subsequent pagination `results`. Can be passed in to the subsequent request to continue pagination. If `cursorState` is missing from the response, you have reached the end of the pagination and all results have been returned. To restart pagination, simply omit the `cursorState` from the pagination request. |
| `nextUrl` | The URL for the next paginated request. Contains the `cursorState` and any additional filters that have been applied. The `cursorState` is returned independently as well to give the client more flexibility in how they wish to paginate through entities. If `nextUrl` is missing from the response, you have reached the end of the pagination and all results have been returned. |
| `totalResults` | Not returned for all pagination endpoints, but if present will provide the total number of entities that can be returned through the pagination. |

For more details about Autodesk Construction Cloud Assets API, see the [Assets Field Guide](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/assets/).

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps), and select the Data Management and Autodesk Construction Cloud APIs.
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:read` scope.
- Verify that you have access to the relevant Autodesk Construction Cloud account, project, and folder.
- Retrieve the relevant [ACC account and project ID](getting-started-retrieve-account-and-project-id.md). In this tutorial we will use the example project ID `f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`, but you should replace that with the project ID you have retrieved for your project.

## [Step 1: Fetch Assets](#step-1-fetch-assets)

To get the assets themselves, use the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`) to call [GET assets/v2/projects/:projectId/assets](../http-docs/http-assets-assets-v2-GET.md).

You will want to ensure you set the query parameter `includeCustomAttributes=true` if you wish to include Asset custom attribute data in your fetch. If you want to include deleted assets, you can set the query parameter `includeDeleted=true` as well.

If you want to fetch a more targeted set of assets, you can provide additional filters in your request. This could include filtering by category, status, a specific location or a location hierarchy, custom attribute value(s), or any combination thereof. A complete list of the filters available, and how they are used, can be found in the [query parameter documentation](../http-docs/http-assets-assets-v2-GET.md#query-string-parameters) for the asset pagination endpoint. Filters provided in the initial pagination request will automatically be added to the `nextUrl` field to continue the filtered pagination.

If you want to include only assets that have changed since previously retrieving assets, you can use the query parameter filter `filter[updatedAt]={previousFetchTime}..`.

### Request

```
curl 'https://developer.api.autodesk.com/construction/assets/v2/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/assets?includeCustomAttributes=true' \
     -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT'

```

### Response

```
{
  "results": [
    {
      "id": "a36ff5f6-8d51-43b1-a3da-ed748a63eb5b",
      "version": 1,
      "createdAt": "2021-01-05T20:37:28.731Z",
      "createdBy": "KKD4J2WE984T",
      "updatedAt": "2021-01-05T20:37:28.731Z",
      "updatedBy": "KKD4J2WE984T",
      "isActive": true,
      "categoryId": "12",
      "locationId": "2b2656fa-d5ff-4a1f-b022-c3e803cadbd3",
      "companyId": "9fd5d33e-6a51-4edc-a647-ed737162f65d",
      "clientAssetId": "MVS-3D2",
      "statusId": "f92f1b17-d0ff-427d-ba6d-7326eaf497b0",
      "customAttributes": {
        "ca1": "110"
      }
    },
    {
      "id": "c319622f-3f05-4bb4-b717-afe02b4cd3c3",
      "version": 2,
      "createdAt": "2021-01-05T20:37:28.732Z",
      "createdBy": "KKD4J2WE984T",
      "updatedAt": "2021-01-05T20:37:28.732Z",
      "updatedBy": "KKD4J2WE984T",
      "isActive": true,
      "categoryId": "13",
      "locationId": "de780160-6aaf-4e99-b1c1-fc9f5cedbfa7",
      "companyId": "9fd5d33e-6a51-4edc-a647-ed737162f65d",
      "clientAssetId": "MVS-3D3",
      "statusId": "fbcedb87-decb-4a17-826f-948e8d2585a5",
      "customAttributes": {
        "ca1": "110",
        "ca2": true,
        "ca6": "1942-11-27"
      }
    },
    {
      "id": "d1625a1c-5bab-464f-816c-a6b79d5da4af",
      "version": 3,
      "createdAt": "2021-01-05T20:37:28.733Z",
      "createdBy": "KKD4J2WE984T",
      "updatedAt": "2021-01-05T20:37:28.733Z",
      "updatedBy": "KKD4J2WE984T",
      "isActive": true,
      "categoryId": "13",
      "locationId": "8704717d-20f3-4586-b741-86891d727479",
      "companyId": "9fd5d33e-6a51-4edc-a647-ed737162f65d",
      "clientAssetId": "MVS-3E1",
      "statusId": "fbcedb87-decb-4a17-826f-948e8d2585a5",
      "customAttributes": {
        "ca1": "220",
        "ca2": false,
        "ca6": "1970-09-18"
      }
    }
  ],
  "pagination": {
    "limit": 3,
    "offset": 0,
    "cursorState": "eyJsaW1pdCI6MjUsIm9mZnNldCI6MjV9",
    "nextUrl": "https://developer.api.autodesk.com/construction/assets/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/assets?cursorState=eyJsaW1pdCI6MjUsIm9mZnNldCI6MjV9"
  }
}

```

Show More

## [Step 2: Fetch Categories](#step-2-fetch-categories)

To get the categories, use the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`) to call [GET assets/v1/projects/:projectId/categories](../http-docs/http-assets-categories-GET.md).

If you want to include only active categories, you can set the query parameter `filter[isActive]=true`. Note that filtering to only active or inactive categories can result in the returned tree not being fully intact.

If you want to include only categories that have changed since previously retrieving categories, you can use the query parameter filter `filter[updatedAt]={previousFetchTime}..`.

### Request

```
curl 'https://developer.api.autodesk.com/construction/assets/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/categories' \
     -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT'

```

### Response

```
{
  "results": [
    {
      "id": "10",
      "name": "ROOT",
      "description": "Auto-generated ROOT category for Assets Category Hierarchy",
      "createdAt": "2021-01-05T19:55:59.603Z",
      "createdBy": "assets-service",
      "updatedAt": "2021-01-05T19:55:59.603Z",
      "updatedBy": "assets-service",
      "subcategoryIds": [ "12" ],
      "isActive": true,
      "isRoot": true,
      "isLeaf": false
    },
    {
      "id": "12",
      "name": "Electrical",
      "parentId": "10",
      "createdAt": "2021-01-05T20:37:27.381Z",
      "createdBy": "KKD4J2WE984T",
      "updatedAt": "2021-01-05T20:37:27.381Z",
      "updatedBy": "KKD4J2WE984T",
      "subcategoryIds": [ "13" ],
      "isActive": true,
      "isRoot": false,
      "isLeaf": false
    },
    {
      "id": "13",
      "name": "Light Fixtures",
      "parentId": "12",
      "createdAt": "2021-01-05T20:37:27.648Z",
      "createdBy": "KKD4J2WE984T",
      "updatedAt": "2021-01-05T20:37:27.648Z",
      "updatedBy": "KKD4J2WE984T",
      "subcategoryIds": [ ],
      "isActive": true,
      "isRoot": false,
      "isLeaf": false
    },
  ],
  "pagination": {
    "totalResults": 3
  }
}

```

Show More

## [Step 3: Fetch Status Sets And Asset Statuses](#step-3-fetch-status-sets-and-asset-statuses)

To get the status sets, use the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`) to call [GET assets/v1/projects/:projectId/status-step-sets](../http-docs/http-assets-status-step-sets-GET.md).

If you want to include deactivated status sets and Asset statuses, you can set the query parameter `includeDeleted=true`.

Note: If you just want to fetch the Asset statuses directly, you can call [GET assets/v1/projects/:projectId/asset-statuses](../http-docs/http-assets-asset-statuses-GET.md), but all statuses will be returned nested by fetching the full set of status sets as well.

If you want to include only status sets that have changed since previously retrieving status sets, you can use the query parameter filter `filter[updatedAt]={previousFetchTime}..`. Note that this will only reflect updates to the status sets themselves, not any of the contained statuses. To fetch Asset statuses that have been changed since a given time, you can call [GET assets/v1/projects/:projectId/asset-statuses](../http-docs/http-assets-asset-statuses-GET.md) with `filter[updatedAt]={previousFetchTime}..`.

### Request

```
curl 'https://developer.api.autodesk.com/construction/assets/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/status-step-sets' \
     -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT'

```

### Response

```
{
  "results": [
    {
      "id": "391e0d38-7ad2-41be-a87c-ca590f1fee91",
      "version": 2925,
      "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
      "name": "Default",
      "isDefault": true,
      "values": [
        {
          "id": "f92f1b17-d0ff-427d-ba6d-7326eaf497b0",
          "version": 11695,
          "description": "Specified",
          "bucket": "specified",
          "label": "Specified",
          "color": "blue",
          "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
          "statusStepSetId": "391e0d38-7ad2-41be-a87c-ca590f1fee91",
          "createdBy": "KKD4J2WE984T",
          "createdAt": "2020-02-26T18:58:40.163Z",
          "updatedBy": "KKD4J2WE984T",
          "updatedAt": "2020-02-26T18:58:40.163Z",
          "isActive": true
        },
        {
          "id": "ebac8429-1fa7-4d37-81c3-e3352f6a24ec",
          "version": 11693,
          "description": "Ordered",
          "bucket": "ordered",
          "label": "Ordered",
          "color": "yellow",
          "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
          "statusStepSetId": "391e0d38-7ad2-41be-a87c-ca590f1fee91",
          "createdBy": "KKD4J2WE984T",
          "createdAt": "2020-02-26T18:58:40.176Z",
          "updatedBy": "KKD4J2WE984T",
          "updatedAt": "2020-02-26T18:58:40.176Z",
          "isActive": true
        }
      ],
      "createdAt": "2020-02-26T18:58:40.130Z",
      "createdBy": "KKD4J2WE984T",
      "updatedAt": "2020-02-26T18:58:40.130Z",
      "updatedBy": "KKD4J2WE984T",
      "isActive": true
    },
    {
      "id": "f0fc7dc2-a325-4b1b-982b-584278f9a873",
      "version": 2926,
      "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
      "name": "Light Fixtures Statuses",
      "isDefault": false,
      "values": [
        {
          "id": "fbcedb87-decb-4a17-826f-948e8d2585a5",
          "version": 11694,
          "description": "Delivered",
          "bucket": "delivered",
          "label": "Delivered",
          "color": "red",
          "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
          "statusStepSetId": "f0fc7dc2-a325-4b1b-982b-584278f9a873",
          "createdBy": "KKD4J2WE984T",
          "createdAt": "2020-02-26T18:58:40.189Z",
          "updatedBy": "KKD4J2WE984T",
          "updatedAt": "2020-02-26T18:58:40.189Z",
          "isActive": true
        }
      ],
      "createdAt": "2020-02-26T18:58:40.130Z",
      "createdBy": "KKD4J2WE984T",
      "updatedAt": "2020-02-26T18:58:40.130Z",
      "updatedBy": "KKD4J2WE984T",
      "isActive": true
    }
  ],
  "pagination": {
    "limit": 3,
    "offset": 0
  }
}

```

Show More

## [Step 4: Fetch Status Set to Category Assignments](#step-4-fetch-status-set-to-category-assignments)

To get the status set to category assignments, use the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`) and category IDs obtained in Step 3 to call [POST assets/v1/projects/:projectId/category-status-step-sets/status-step-sets:batch-get](en/docs/acc/v1/reference/http/assets-category-status-step-sets-status-step-sets-batch-get-POST/).

By default this will only return the status sets explicitly assigned to the given categories. If you wish to return each categoryâs effective status set assignment (taking inheritance into account), you can set the query parameter `includeInherited=true`.

### Request

```
curl 'https://developer.api.autodesk.com/construction/assets/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/category-status-step-sets/status-step-sets:batch-get?includeInherited=true' \
     -X 'POST' \
     -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
     -H 'Content-Type: application/json' \
     -d '{
           "ids": [
             "10",
             "12",
             "13",
           ]
         }'

```

Show More

### Response

```
{
  "results": [
    {
      "categoryId": "10",
      "statusStepSetId": "391e0d38-7ad2-41be-a87c-ca590f1fee91"
    },
    {
      "categoryId": "12",
      "statusStepSetId": "391e0d38-7ad2-41be-a87c-ca590f1fee91"
    },
    {
      "categoryId": "13",
      "statusStepSetId": "f0fc7dc2-a325-4b1b-982b-584278f9a873"
    }
  ]
}

```

Show More

## [Step 5: Fetch Asset Custom Attributes](#step-5-fetch-asset-custom-attributes)

To get the Asset custom attributes, use the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`) to call [GET assets/v1/projects/:projectId/custom-attributes](../http-docs/http-assets-custom-attributes-GET.md).

If you want to include deactivated custom attributes, you can set the query parameter `includeDeleted=true`.

If you want to include only custom attributes that have changed since previously retrieving custom attributes, you can use the query parameter filter `filter[updatedAt]={previousFetchTime}..`.

### Request

```
curl 'https://developer.api.autodesk.com/construction/assets/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/custom-attributes' \
     -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT'

```

### Response

```
{
  "results": [
    {
      "id": "5903f625-9cb3-4c78-be51-468ec9073d2a",
      "version": 7485,
      "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
      "dataType": "numeric",
      "displayName": "Voltage",
      "name": "ca1",
      "description": "Voltage of the Electrical asset",
      "requiredOnIngress": true,
      "createdBy": "KKD4J2WE984T",
      "createdAt": "2020-03-22T23:09:03.730Z",
      "updatedBy": "KKD4J2WE984T",
      "updatedAt": "2020-12-18T22:16:44.083Z",
      "isActive": true
    },
    {
      "id": "e37911e0-1cc3-4f18-aa91-1ff1907e29d0",
      "version": 7486,
      "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
      "dataType": "boolean",
      "displayName": "Grounded",
      "name": "ca2",
      "description": "Is the Electrical asset grounded?",
      "requiredOnIngress": true,
      "createdBy": "KKD4J2WE984T",
      "createdAt": "2020-03-22T23:11:08.689Z",
      "updatedBy": "KKD4J2WE984T",
      "updatedAt": "2020-12-18T22:16:46.565Z",
      "isActive": true
    },
    {
      "id": "da5989c5-cdf5-40a3-8447-3168335637b5",
      "version": 5985,
      "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
      "dataType": "date",
      "displayName": "Install date",
      "name": "ca6",
      "requiredOnIngress": false,
      "createdBy": "KKD4J2WE984T",
      "createdAt": "2020-10-22T20:45:01.425Z",
      "updatedBy": "KKD4J2WE984T",
      "updatedAt": "2020-10-22T20:45:01.425Z",
      "isActive": true
    },
  ],
  "pagination": {
    "limit": 3,
    "offset": 0
  }
}

```

Show More

## [Step 6: Fetch Category to Asset Custom Attribute Assignments](#step-6-fetch-category-to-asset-custom-attribute-assignments)

To get the Asset custom attributes assigned to a category, use the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`) and category IDs obtained in Step 3 to call [GET assets/v1/projects/:projectId/categories/:categoryId/custom-attributes](en/docs/acc/v1/reference/http/assets-categories-category-id-custom-attributes-GET/).

A batch endpoint doe not yet exist for this call, so at this time a call must be made for each category ID individually to get the full set of assignments.

By default this will only return the custom attributes explicitly assigned to the given category. If you wish to return the full set of custom attributes assigned to the given category, you can set the query parameter `includeInherited=true`. When `includeInherited=true` is set, an additional field will be included in the response for each returned custom attribute `inheritedFromCategoryId` which will indicate from which explicit category assignment the custom attribute is inherited from.

### Request

```
curl 'https://developer.api.autodesk.com/construction/assets/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/categories/13/custom-attributes?includeInherited=true' \
     -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT'

```

### Response

```
{
  "results": [
    {
      "id": "5903f625-9cb3-4c78-be51-468ec9073d2a",
      "version": 7485,
      "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
      "dataType": "numeric",
      "displayName": "Voltage",
      "name": "ca1",
      "description": "Voltage of the Electrical asset",
      "requiredOnIngress": true,
      "createdBy": "KKD4J2WE984T",
      "createdAt": "2020-03-22T23:09:03.730Z",
      "updatedBy": "KKD4J2WE984T",
      "updatedAt": "2020-12-18T22:16:44.083Z",
      "isActive": true,
      "inheritedFromCategoryId": "10"
    },
    {
      "id": "e37911e0-1cc3-4f18-aa91-1ff1907e29d0",
      "version": 7486,
      "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
      "dataType": "boolean",
      "displayName": "Grounded",
      "name": "ca2",
      "description": "Is the Electrical asset grounded?",
      "requiredOnIngress": true,
      "createdBy": "KKD4J2WE984T",
      "createdAt": "2020-03-22T23:11:08.689Z",
      "updatedBy": "KKD4J2WE984T",
      "updatedAt": "2020-12-18T22:16:46.565Z",
      "isActive": true,
      "inheritedFromCategoryId": "13"
    },
    {
      "id": "da5989c5-cdf5-40a3-8447-3168335637b5",
      "version": 5985,
      "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
      "dataType": "date",
      "displayName": "Install date",
      "name": "ca6",
      "requiredOnIngress": false,
      "createdBy": "KKD4J2WE984T",
      "createdAt": "2020-10-22T20:45:01.425Z",
      "updatedBy": "KKD4J2WE984T",
      "updatedAt": "2020-10-22T20:45:01.425Z",
      "isActive": true,
      "inheritedFromCategoryId": "13"
    },
  ],
  "pagination": {
    "limit": 3,
    "offset": 0,
    "totalResults": 3
  }
}

```

Show More

## [Step 7: Fetch Locations](#step-7-fetch-locations)

The Locations API can be used to fetch location data for the `locationId` field on an asset via the [GET Nodes](../http-docs/http-locations-nodes-GET.md) endpoint.

In this example the Project ID is `f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/locations/v2/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/trees/default/nodes?filter[id]=2b2656fa-d5ff-4a1f-b022-c3e803cadbd3,de780160-6aaf-4e99-b1c1-fc9f5cedbfa7'
  -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT'

```

### Response

```
{
    "results": [
      {
        "id": "2b2656fa-d5ff-4a1f-b022-c3e803cadbd3,
        "parentId": null,
        "type": "Root",
        "name": "Project",
        "description": "Project description",
        "order": 0,
        "documentCount": 0,
        "areaDefined": false
      },
      {
        "id": "de780160-6aaf-4e99-b1c1-fc9f5cedbfa7,
        "parentId": "2b2656fa-d5ff-4a1f-b022-c3e803cadbd3",
        "type": "Area",
        "name": "Area 1",
        "description": "An Area 1 node",
        "order": 0,
        "documentCount": 2,
        "areaDefined": true
      }
    ],
    "pagination": {
      "limit": 2,
      "offset": 0,
      "totalResults": 2,
      "nextUrl": "/locations/v2/projects/4a327b27-897c-4e5a-8e48-6e01c21377f3/trees/default/nodes?limit=2&offset=2"
    }
  }

```

Show More

## [Step 8: Fetch Asset Relationships](#step-8-fetch-asset-relationships)

Assets can be associated with other entities such as Issues, Forms, Photos, etc. You can use the Relationship API to search for all relationships associated with your project, or for a given Asset directly.

For the Relationship API, your Container ID will simply be your Project ID.

See the [Relationship v2 APIs documentation](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/#bim-360-relationships-api).

You can search for all relationships in your project which include an âassetâ type using the following query parameters:

| Query Parameter | Value(s) |
| --- | --- |
| `domain` | The Assets Relationship domain: `autodesk-bim360-asset` (NOTE: the domain is the same for Autodesk Construction Cloud assets or BIM360 assets) |
| `type` | The Assets Relationship types (see below for available options) |
| `id` | OPTIONAL - ID of the Asset to search relationships for |
| `withDomain` | OPTIONAL - The related entity domain (see below for available options) |
| `withType` | OPTIONAL - The related entity type (see below for available options) |
| `withId` | OPTIONAL - The related entity ID. e.g. checklist ID, issue ID, checklist template ID |

### Supported Related Domains and Types

Note that this list of Parameters is not exhaustive. More information on the Relationship API will be provided as it becomes available.

Also note that different Domains and Types are available for Autodesk Construction Cloud asset relationships than for BIM30 asset relationships, and that this is not necessarily determined by the domain itself. For example, and `issue` in the `autodesk-bim360-issue` domain can be related to an Autodesk Construction Cloud asset, as seen in the table below.

| Type | Related Domain | Related Type |
| --- | --- | --- |
| `asset` | `autodesk-bim360-issue` | `issue` |
| `asset` | `autodesk-bim360-documentmanagement` | `documentlineage` |
| `asset` | `autodesk-construction-photo` | `photo` |
| `asset` | `autodesk-construction-form` | `form` |
| `asset` | `autodesk-construction-sheet` | `sheetlineage` |
| `asset` | `autodesk-construction-submittals` | `submittalitem` |
| `category` | `autodesk-construction-form` | `formtemplate` |

#### Example

In this example the Project ID and Relationship container ID is `f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`. We would like to query the Relationship API for all relationships with assets within this project.

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/relationships:search?domain=autodesk-bim360-asset&type=asset' \
  -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT'

```

### Response

```
{
  "page": {
    "continuationToken": "10",
    "syncToken": "eyAibGFzdENoZWNrZWQiOiIyMDE5LTEwLTE4VDEyOjEwOjA3Ljc5NloiIH0="
  },
  "relationships": [
    {
      "id": "e005c68b-53af-41d0-9e56-9be86cd9c5a9",
      "createdOn": "2020-07-28T19:52:44.262208+00:00",
      "isReadOnly": true,
      "isService": true,
      "isDeleted": false,
      "entities": [
        {
          "createdOn": "2020-07-28T19:52:44.198281+00:00",
          "domain": "autodesk-bim360-asset",
          "type": "asset",
          "id": "71fa0b41-cd23-4439-8def-4348a2a45d4b"
        },
        {
          "createdOn": "2020-07-28T19:52:44.198281+00:00",
          "domain": "autodesk-bim360-issue",
          "type": "issue",
          "id": "84929da1-f71c-4a4d-9535-32c23db9a378"
        }
      ]
    }
  ]
}

```

Show More

For more information on querying the Relationship API, see the [Relationship Querying Tutorial](relationships-relationships-tutorial.md).

Once you have the entities and their relationships to the given assets you can use the relevant APIs to fetch the data for the given entities. This may require setting up access to other APIs, depending on what type of entities are linked to your Assets. See [Retrieve Issues](issues-retrieve-issues.md) and [Get Forms Endpoint](../http-docs/http-forms-forms-GET.md) for examples of retrieving related entities.
