# Create Relationships

Source: https://aps.autodesk.com/en/docs/acc/tutorials/relationships/relationships-create/

---

# Create Relationships

This tutorial demonstrates how to create a relationship between two entities (for example, an asset and a document). The steps include verifying compatibility of entity types in the Relationships service, finding information about the entities you want to create a relationship for, and creating the relationship between the entities. For information about the Relationships API, see the [Field Guide](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/relationships/).

Note that in order to create a relationship between two entities, the entities must already exist, and the caller must have permission to
access both entities in the proposed relationship.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps), and select the Data Management and BIM 360 APIs.
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:create` `data:read` and `data:write` scopes.
- Verify that you have access to the relevant account, project, folder and contents.
- Find the relationships container ID for the relevant project.

Note that this tutorial assumes you are familiar with the BIM 360 Assets and Document Management APIs.

## [Step 1: Verify Entity Compatibility](#step-1-verify-entity-compatibility)

You first need to check whether the entities you want to associate with each other are compatible.

To verify compatibility, call [GET utility/relationships:writable](../http-docs/http-relationship-service-v2-get-writable-relationship-domains-GET.md), and find the object containing the relationship domain and entity type you want to create a relationship against.
For example, check whether you can create a relationship between an asset and a document. The asset `domain` is `autodesk-bim360-asset`, and the `entity type` is `asset`. In this example, the `allow` attribute contains an array of entity types that assets can have a relationship with. For a list of domains and their entity types, see the [Relationship Querying tutorial](relationships-relationships-tutorial.md).

Note that some domains have a `bim360` prefix, and others have a `construction` prefix.

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
         },
         {
           "domain": "autodesk-construction-photo",
           "entityTypes": [
             "photo"
           ]
         },
         {
           "domain": "autodesk-construction-form",
           "entityTypes": [
             "form"
           ]
         }
       ]
     },
     {
       "entityType": "category",
       "allow": [
         {
           "domain": "autodesk-construction-form",
           "entityTypes": [
             "formtemplate"
           ]
         }
       ]
     }
   ]
 }
 (...)
 {
       "domain": "autodesk-construction-photo",
       "entityTypes": [
           {
               "entityType": "photo",
               "allow": [
                   {
                       "domain": "autodesk-bim360-asset",
                       "entityTypes": [
                           "asset"
                       ]
                   },
                   {
                       "domain": "autodesk-construction-form",
                       "entityTypes": [
                           "form",
                           "formfield"
                       ]
                   }
               ]
           }
       ]
 }
]

```

Show More

## [Step 2: Find Information About Entities](#step-2-find-information-about-entities)

You need to find information about the entities you want to create a relationship for. For example, to create a relationship between an asset and a document, you need to call [GET assets](../http-docs/http-assets-assets-v2-GET.md) to find the ID of the asset, and [GET folders/:folder_id/contents](../../data/http-docs/http-projects-project_id-folders-folder_id-contents-GET.md) to find the ID of the document.

## [Step 3: Create a Relationship](#step-3-create-a-relationship)

To create relationships between compatible entities, use the information you found in the previous steps and the container ID to call [PUT containers/:containerId/relationships](../http-docs/http-relationship-service-v2-add-relationships-PUT.md).
Note that one entity may be related to a batch of up to 20 entities within a single API call.

In this example, we are creating a relationship between an asset and a document.

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/fbd6cb57-7d0e-4961-8c2c-69646514ef44/relationships' \
    -X PUT \
    -H 'Authorization: Bearer <token>' \
    -H 'Content-Type: application/json' \
    -d '[
            {
                "entities": [
                    {
                        "domain": "autodesk-bim360-asset",
                        "type": "asset",
                        "id": "2b95ba7a-3df5-4e99-a693-9c7cc15ee8c0"
                    },
                    {
                        "domain": "autodesk-bim360-documentmanagement",
                        "type": "documentlineage",
                        "id": "urn:adsk.wipprod:dm.lineage:hC6k4hndRWaeIVhIjvHu8w"
                    }
                ]
            }
        ]'

```

Show More

### Example Response

```
[
 {
     "id": "b544a7eb-3c64-4a56-a7ff-392d0441015f",
     "createdOn": "2021-10-21T16:32:22Z",
     "isReadOnly": false,
     "isService": false,
     "isDeleted": false,
     "entities": [
         {
             "domain": "autodesk-bim360-asset",
             "type": "asset",
             "id": "2b95ba7a-3df5-4e99-a693-9c7cc15ee8c0"
         },
         {
             "domain": "autodesk-bim360-documentmanagement",
             "type": "documentlineage",
             "id": "urn:adsk.wipprod:dm.lineage:hC6k4hndRWaeIVhIjvHu8w"
         }
     ]
 }
]

```

Show More

Note that you can create relationships by supplying your own relationship IDs (UUID). For example, you can choose to use `b544a7eb-3c64-4a56-a7ff-392d0441015f` as the ID. If the ID is already in use, the server will reject the request with an HTTP `409 Conflict` error.

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/fbd6cb57-7d0e-4961-8c2c-69646514ef44/relationships' \
    -X PUT \
    -H 'Authorization: Bearer <token>' \
    -H 'Content-Type: application/json' \
    -d '[
            {
                "id": "b544a7eb-3c64-4a56-a7ff-392d0441015f",
                "entities": [
                    {
                       "domain": "autodesk-bim360-asset",
                        "type": "asset",
                        "id": "2b95ba7a-3df5-4e99-a693-9c7cc15ee8c0"
                    },
                    {
                        "domain": "autodesk-bim360-documentmanagement",
                        "type": "documentlineage",
                        "id": "urn:adsk.wipprod:dm.lineage:hC6k4hndRWaeIVhIjvHu8w"
                    }
                ]
            }
        ]'

```

Show More

### Example Conflict Response

```
{
    "conflict": [
        {
            "id": "b544a7eb-3c64-4a56-a7ff-392d0441015f",
            "actual": {
                "id": "74b70bb8-8802-a1fd-f201-890375a60c8f",
                "createdOn": "2021-10-21T16:32:22Z",
                "isReadOnly": false,
                "isService": false,
                "isDeleted": false,
                "entities": [
                    {
                       "domain": "autodesk-bim360-asset",
                        "type": "asset",
                        "id": "2b95ba7a-3df5-4e99-a693-9c7cc15ee8c0"
                    },
                    {
                        "domain": "autodesk-bim360-documentmanagement",
                        "type": "documentlineage",
                        "id": "urn:adsk.wipprod:dm.lineage:hC6k4hndRWaeIVhIjvHu8w"
                    }
                ]
            }
        }
    ]
}

```

Show More
