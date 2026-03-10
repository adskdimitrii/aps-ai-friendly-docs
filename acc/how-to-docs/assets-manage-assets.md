# Managing ACC Assets

Source: https://aps.autodesk.com/en/docs/acc/tutorials/assets/manage-assets/

---

# Managing ACC Assets

Managing assets is the core of the functionality the Autodesk Construction Cloud Assets service provides. This tutorial demonstrates how to use the ACC Assets API to manage a ACC project’s assets. This will include:

- Creating new assets
- Updating existing assets
- Deleting assets
- Creating new relationships between assets and other entities (e.g. forms)
- Deleting relationships between assets and other entities

This tutorial assumes that the project’s Asset settings have already been set up. For more details on how to do this,
see the [Setup ACC Assets Project Settings](assets-create-assets-project-settings.md) tutorial.

## [Batch Endpoints](#batch-endpoints)

In order to reduce the number of calls needed to manage assets, many of the Assets APIs are batched. This includes creating, updating, fetching, and deleting assets, as well as fetching categories, statuses, status sets, and custom attributes.

The specific syntax varies a bit between endpoints, but in general batch endpoints will accept a set of items, assets to create or category IDs to fetch for example, and return the relevant set of entities.

When fetching entities in batch, invalid entities that are requested will simply be omitted from the response. It is the client’s responsibility to ensure the requested entities are indeed present in the response.

Batch endpoints generally support operating on up to 100 entities at a given time, unless otherwise noted in the endpoint documentation.

For more details about Autodesk Construction Cloud Assets API, see the [Assets Field Guide](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/assets/).

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps), and select the Data Management and Autodesk Construction Cloud APIs.
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:create` and `data:write` scopes.
- Verify that you have access to the relevant Autodesk Construction Cloud account, project, and folder.
- Retrieve the relevant [ACC account and project ID](getting-started-retrieve-account-and-project-id.md). In this tutorial we will use the example project ID `f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`, but you should replace that with the project ID you have retrieved for your project.

## [Step 1: Create new Assets](#step-1-create-new-assets)

To create new assets, use the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`) to call [POST assets/v2/projects/:projectId/assets:batch-create](../http-docs/http-assets-assets-batch-create-POST-v2.md).

This is a batch endpoint that can be used to create multiple assets at a time. The endpoint accepts a set of asset definitions and returns the set of created assets.

Unlike batch fetch endpoints, batch creating assets is “all-or-nothing”. If any of the asset definitions in the request are invalid, none of the assets will be created and a `400 - Error: Bad Request` will be returned with a list of the violations that need to be corrected before the request can succeed.

For more details on finding out which categories, statuses, and custom attributes are available and required, see the [Retrieve ACC Assets Data](assets-retrieve-assets-data.md) tutorial.

### Request

```
curl 'https://developer.api.autodesk.com/construction/assets/v2/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/assets:batch-create' \
     -X 'POST' \
     -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
     -H 'Content-Type: application/json' \
     -d '[
           {
             "clientAssetId": "MVS-3D2",
             "categoryId": "124",
             "statusId": "b302d910-b5e3-46ba-81d8-6b6d30406e14",
             "description": "Electrical outlet - single",
             "barcode": "F0086728",
             "customAttributes": {
               "ca1": "fd0e4a00-26df-454e-8fba-e76652aa55b4"
             }
           },
           {
             "clientAssetId": "MVS-F38",
             "categoryId": "124",
             "statusId": "e0484858-1683-42fe-9136-6575e43c8eac",
             "description": "Electrical outlet - double",
             "barcode": "F0086730",
             "customAttributes": {
               "ca1": "582eac28-f4e4-475d-b38c-fd57997c9cc6"
             }
           }
         ]'

```

Show More

### Response

```
{
  "results": [
    {
      "id": "8947f8af-3247-4bfe-82f9-976181596e24",
      "clientAssetId": "MVS-3D2",
      "categoryId": "124",
      "statusId": "b302d910-b5e3-46ba-81d8-6b6d30406e14",
      "description": "Electrical outlet - single",
      "barcode": "F0086728",
      "customAttributes": {
        "ca1": "fd0e4a00-26df-454e-8fba-e76652aa55b4"
      },
      "companyId": "07b5f07d-c54a-4236-a086-f84192fabdb3",
      "createdAt": "2020-05-01T06:00:00.000Z",
      "createdBy": "LA7ZL85MU7ML",
      "updatedAt": "2020-05-01T06:00:00.000Z",
      "updatedBy": "LA7ZL85MU7ML",
      "isActive": true,
      "version": 1
    },
    {
      "id": "a0fd5800-1616-49d8-a847-103fc44bdc6a",
      "clientAssetId": "MVS-F38",
      "categoryId": "124",
      "statusId": "e0484858-1683-42fe-9136-6575e43c8eac",
      "description": "Electrical outlet - double",
      "barcode": "F0086730",
      "customAttributes": {
        "ca1": "582eac28-f4e4-475d-b38c-fd57997c9cc6"
      },
      "companyId": "07b5f07d-c54a-4236-a086-f84192fabdb3",
      "createdAt": "2020-05-01T06:00:00.000Z",
      "createdBy": "LA7ZL85MU7ML",
      "updatedAt": "2020-05-01T06:00:00.000Z",
      "updatedBy": "LA7ZL85MU7ML",
      "isActive": true,
      "version": 1
    }
  ]
}

```

Show More

## [Step 2: Update Existing Assets](#step-2-update-existing-assets)

To update existing assets, like the assets that were created in Step 1 above, use the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`) to call [PATCH assets/v2/projects/:projectId/assets:batch-patch](../http-docs/http-assets-assets-batch-patch-PATCH-v2.md).

This is a batch endpoint that can be used to modify multiple assets at a time. The endpoint accepts a map of asset IDs to the desired asset patch updates, and returns the set of updated assets. Note that this is a patch and not a full update, so only the fields specified in the request body will be updated and the remaining fields will be left unaltered.

Unlike batch fetch endpoints, batch updating assets is “all-or-nothing”. If any of the asset patches in the request are invalid, none of the assets will be updated and a `400 - Error: Bad Request` will be returned with a list of the violations that need to be corrected before the request can succeed.

For more details on finding out which categories, statuses, and custom attributes are available and required, see the [Retrieve ACC Assets Data](assets-retrieve-assets-data.md) tutorial.

### Request

```
curl 'https://developer.api.autodesk.com/construction/assets/v2/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/assets:batch-patch' \
     -X 'PATCH' \
     -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
     -H 'Content-Type: application/json' \
     -d '{
           "8947f8af-3247-4bfe-82f9-976181596e24": {
             "clientAssetId": "MVS-3D2 v2.0",
             "description": "Modified 2.0 Electrical outlet - single",
             "statusId": "e0484858-1683-42fe-9136-6575e43c8eac"
           },
           "4a125d1b-0803-408e-ab8b-ccdd159b8ca8": {
             "clientAssetId": "MVS-F38 v2.0",
             "description": "Modified 2.0 Electrical outlet - double",
             "customAttributes": {
                "ca1": "fd0e4a00-26df-454e-8fba-e76652aa55b4"
              }
           }
         }'

```

Show More

### Response

```
{
  "8947f8af-3247-4bfe-82f9-976181596e24": {
    "id": "8947f8af-3247-4bfe-82f9-976181596e24",
    "clientAssetId": "MVS-3D2 v2.0",
    "categoryId": "124",
    "description": "Modified 2.0 Electrical outlet - single",
    "statusId": "e0484858-1683-42fe-9136-6575e43c8eac",
    "barcode": "F0086728",
    "customAttributes": {
      "ca1": "fd0e4a00-26df-454e-8fba-e76652aa55b4"
    },
    "companyId": "07b5f07d-c54a-4236-a086-f84192fabdb3",
    "createdAt": "2020-05-01T06:00:00.000Z",
    "createdBy": "LA7ZL85MU7ML",
    "updatedAt": "2020-05-02T14:00:00.000Z",
    "updatedBy": "LA7ZL85MU7ML",
    "isActive": true,
    "version": 2
  },
  "a0fd5800-1616-49d8-a847-103fc44bdc6a": {
    "id": "a0fd5800-1616-49d8-a847-103fc44bdc6a",
    "clientAssetId": "MVS-F38 v2.0",
    "categoryId": "124",
    "statusId": "e0484858-1683-42fe-9136-6575e43c8eac",
    "description": "Modified 2.0 Electrical outlet - double",
    "barcode": "F0086730",
    "customAttributes": {
      "ca1": "fd0e4a00-26df-454e-8fba-e76652aa55b4"
    },
    "companyId": "07b5f07d-c54a-4236-a086-f84192fabdb3",
    "createdAt": "2020-05-01T06:00:00.000Z",
    "createdBy": "LA7ZL85MU7ML",
    "updatedAt": "2020-05-02T14:00:00.000Z",
    "updatedBy": "LA7ZL85MU7ML",
    "isActive": true,
    "version": 2
  }
}

```

Show More

## [Step 3: Fetch Existing Assets](#step-3-fetch-existing-assets)

To fetch existing assets, like the assets that were created in Step 1 above, use the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`) to call [POST assets/v2/projects/:projectId/assets:batch-get](../http-docs/http-assets-assets-batch-get-v2-POST.md).

This is a batch endpoint that can be used to fetch multiple assets at a time. The endpoint accepts a set of asset IDs to be fetched, and returns the set of valid requested assets. Any invalid asset IDs in the request will simply be omitted from the response and the client is responsible for verifying the presence of all requested assets.

### Request

```
curl 'https://developer.api.autodesk.com/construction/assets/v2/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/assets:batch-get?includeCustomAttributes=true' \
       -X 'POST' \
       -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
       -H 'Content-Type: application/json' \
       -d '{
             "ids": [
               "8947f8af-3247-4bfe-82f9-976181596e24",
               "a0fd5800-1616-49d8-a847-103fc44bdc6a"
             ]
           }'

```

Show More

### Response

```
{
  "results": [
    {
      "id": "8947f8af-3247-4bfe-82f9-976181596e24",
      "clientAssetId": "MVS-3D2",
      "categoryId": "124",
      "statusId": "b302d910-b5e3-46ba-81d8-6b6d30406e14",
      "description": "Electrical outlet - single",
      "barcode": "F0086728",
      "customAttributes": {
        "ca1": "fd0e4a00-26df-454e-8fba-e76652aa55b4"
      },
      "companyId": "07b5f07d-c54a-4236-a086-f84192fabdb3",
      "createdAt": "2020-05-01T06:00:00.000Z",
      "createdBy": "LA7ZL85MU7ML",
      "updatedAt": "2020-05-01T06:00:00.000Z",
      "updatedBy": "LA7ZL85MU7ML",
      "isActive": true,
      "version": 1
    },
    {
      "id": "a0fd5800-1616-49d8-a847-103fc44bdc6a",
      "clientAssetId": "MVS-F38",
      "categoryId": "124",
      "statusId": "e0484858-1683-42fe-9136-6575e43c8eac",
      "description": "Electrical outlet - double",
      "barcode": "F0086730",
      "customAttributes": {
        "ca1": "582eac28-f4e4-475d-b38c-fd57997c9cc6"
      },
      "companyId": "07b5f07d-c54a-4236-a086-f84192fabdb3",
      "createdAt": "2020-05-01T06:00:00.000Z",
      "createdBy": "LA7ZL85MU7ML",
      "updatedAt": "2020-05-01T06:00:00.000Z",
      "updatedBy": "LA7ZL85MU7ML",
      "isActive": true,
      "version": 1
    }
  ]
}

```

Show More

## [Step 4: Create Asset Relationships](#step-4-create-asset-relationships)

To create asset relationships, attaching an issue to an asset for example, the preferred means is to use the Relationship API. For more information on how to create relationships please see Create Relationships tutorial</en/docs/bim360/v1/tutorials/relationships/relationships-create/>.

In order to create a relationship between an asset and another entity, you will need to obtain the ID of the entity you wish to link to the asset. This may require setting up access to other Autodesk APIs, depending on what type of entities you wish to link to your assets. See the [GET issues](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/field-issues-GET/) or [GET forms](../http-docs/http-forms-forms-GET.md) for examples of retrieving related entities. In this example we will assume we fetched the issues for the project, and wish to attach an issue with ID `a3311fc6-4571-4fca-9fb4-37120d976bd2` to the asset.

Note that within Autodesk Construction Cloud projects, assets may be linked to any of the following domains and types:

| Domain | Entity Type |
| --- | --- |
| autodesk-bim360-documentmanagement | documentlineage |
| autodesk-construction-form | form |
| autodesk-bim360-issue | issue |
| autodesk-construction-markup | markupdocument |
| autodesk-construction-markup | markupsheethistory |
| autodesk-construction-photo | photo |
| autodesk-bim360-rfi | rfi |
| autodesk-construction-sheet | sheetlineage |
| autodesk-construction-submittals | submittalitem |
| autodesk-construction-schedule | activity |
| autodesk-bim360-meetingminutes | meeting |
| autodesk-bim360-meetingminutes | meetingitem |
| autodesk-bim360-meetingminutes | meetingitemseries |
| autodesk-bim360-cost | pco |
| autodesk-bim360-cost | oco |
| autodesk-bim360-cost | rco |
| autodesk-bim360-cost | rfq |
| autodesk-bim360-cost | sco |
| autodesk-bim360-cost | contract |
| autodesk-bim360-cost | costpayment |
| autodesk-bim360-cost | budget |
| autodesk-bim360-cost | budgetpayment |
| autodesk-bim360-cost | expense |
| autodesk-bim360-cost | maincontract |

Additionally, you can use the Relationships API to search for all existing relationships associated with your project, or you can search for the relationships associated with a specific asset.
For more information on querying the Relationships API,
see the [Relationship Field Guide](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/relationships/) and the [Relationship Querying](relationships-relationships-tutorial.md) tutorial.

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/fbd6cb57-7d0e-4961-8c2c-69646514ef44/relationships' \
     -X 'PUT' \
     -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
     -H 'Content-Type: application/json' \
     -d '[
           {
             "entities": [
               {
                 "id": "a0fd5800-1616-49d8-a847-103fc44bdc6a",
                 "domain": "autodesk-bim360-asset",
                 "type": "asset"
               },
               {
                 "id": "a3311fc6-4571-4fca-9fb4-37120d976bd2",
                 "domain": "autodesk-bim360-issue",
                 "type": "issue"
               }
             ]
           }
         ]'

```

Show More

### Response

```
[
  {
    "id": "2299821e-c3e6-4ad7-92c3-ea4ddaf941bf",
    "createdOn": "2020-05-01T06:00:00.000Z",
    "isReadOnly": false,
    "isService": false,
    "isDeleted": false,
    "entities": [
      {
        "id": "a0fd5800-1616-49d8-a847-103fc44bdc6a",
        "domain": "autodesk-bim360-asset",
        "type": "asset",
        "createdOn": "2020-05-01T06:00:00.000Z"
      },
      {
        "id": "a3311fc6-4571-4fca-9fb4-37120d976bd2",
        "domain": "autodesk-bim360-issue",
        "type": "issue",
        "createdOn": "2020-05-01T06:00:00.000Z"
      }
    ]
  }
]

```

Show More

## [Step 5: Delete Asset Relationships](#step-5-delete-asset-relationships)

To delete the relationship between an asset and a given entity, first you must determine the relationship IDs you want to delete.

You can use the Relationships API to search for all existing relationships associated with your project, or you can search for the relationships associated with a specific asset.
For more information on querying the Relationships API,
see the [Relationships Field Guide](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/relationships/) and the [Relationships Querying](relationships-relationships-tutorial.md) tutorial.

In this example, we will use the ID of the relationship we created in step 5 above (`2299821e-c3e6-4ad7-92c3-ea4ddaf941bf`).

Use the relationship IDs you want to delete and the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`)
to call [POST relationship/v2/containers/:containerId/relationships:delete](../http-docs/http-relationship-service-v2-delete-relationships-POST.md).

### Request

```
curl 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/relationships:delete' \
       -X 'POST' \
       -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
       -H 'Content-Type: application/json' \
       -d '[ "2299821e-c3e6-4ad7-92c3-ea4ddaf941bf" ]'

```

### Response

```
{
  "deleted": [
    "2299821e-c3e6-4ad7-92c3-ea4ddaf941bf"
  ]
}

```

## [Step 6: Delete Assets](#step-6-delete-assets)

To delete assets, like the assets that were created in Step 1 above, use the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`) to call [POST assets/v2/projects/:projectId/assets:batch-delete](../http-docs/http-assets-assets-batch-delete-v2-POST.md).

This is a batch endpoint that can be used to delete multiple assets at a time. The endpoint accepts a set of asset IDs to be deleted, and simply returns a `204 - No Content` response if successful.

Note that when assets are deleted, they are always *soft* deleted. This means that the deleted assets are not fully removed from the assets service, but will not be returned when fetching assets unless you include the query parameter `includeDeleted=true`. Soft-deleted assets can be identified as having `isActive=false`.

Unlike batch fetch endpoints, batch deleting assets is “all-or-nothing”. If any of the asset IDs in the request are invalid, none of the assets will be deleted and a `400 - Error: Bad Request` will be returned with a list of the violations that need to be corrected before the request can succeed.

### Request

```
curl 'https://developer.api.autodesk.com/construction/assets/v2/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/assets:batch-delete' \
       -X 'POST' \
       -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
       -H 'Content-Type: application/json' \
       -d '{
             "ids": [
               "8947f8af-3247-4bfe-82f9-976181596e24",
               "a0fd5800-1616-49d8-a847-103fc44bdc6a"
             ]
           }'

```

Show More

### Response

```
204 No Content

```
