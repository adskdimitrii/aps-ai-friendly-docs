# Relationship Querying

Source: https://aps.autodesk.com/en/docs/acc/tutorials/relationships/relationships-tutorial/

---

# Relationship Querying

The Relationship Service is used in BIM 360 to link entities across domains. The following document assumes the reader is familiar with the concept of domain entity linking. If you have not already done so refer to [Relationship Service Field Guide](/en/docs/bim360/v1/overview/field-guide/relationships) which explains the concepts underpinning the relationship service.

## [Relationship Domain and Entity Types](#relationship-domain-and-entity-types)

It is important to note that the entity types returned from the relationship service may not yet be accessible via a public BIM 360 APIs. These identifiers can still be used to construct URL-based deep links back to the appropriate BIM 360 application module user experience. This is a useful feature for developers building bespoke 3LO web user experiences against the BIM 360 API.

### Example Deep-Link Page URLs

Open the Assets module and display a specific Asset :-

```
https://assets.b360.autodesk.com/projects/<YOUR PROJECT GUID>/assets?preview=<RELATIONSHIP SERVICE ENTITY ID>

```

Open the Project Management module and display a specific Meeting :-

```
https://meetings.b360.autodesk.com/projects/<YOUR PROJECT GUID>/meetings/<RELATIONSHIP SERVICE ENTITY ID>

```

### BIM 360 API Supported Relationship Service Entity Types

The following table lists `Domains` and `Entity Types` currently supported by the Relationship Service which are also available via a BIM 360 API.

| Domain | Entity Type | BIM 360 Module |
| --- | --- | --- |
| autodesk-bim360-asset | asset | Assets |
| autodesk-bim360-asset | category | Assets |
| autodesk-bim360-checklist | checklist | Field Management |
| autodesk-bim360-checklist | checklisttemplate | Field Management |
| autodesk-bim360-cost | budget | Cost Management |
| autodesk-bim360-cost | budgetpayment | Cost Management |
| autodesk-bim360-cost | contract | Cost Management |
| autodesk-bim360-cost | costpayment | Cost Management |
| autodesk-bim360-cost | maincontract | Cost Management |
| autodesk-bim360-cost | oco | Cost Management |
| autodesk-bim360-cost | pco | Cost Management |
| autodesk-bim360-cost | rco | Cost Management |
| autodesk-bim360-cost | rfq | Cost Management |
| autodesk-bim360-cost | sco | Cost Management |
| autodesk-bim360-documentmanagement | documentlineage | Document Management |
| autodesk-bim360-documentmanagement | documentversion | Document Management |
| autodesk-bim360-documentmanagement | filelineage | Document Management |
| autodesk-bim360-documentmanagement | fileversion | Document Management |
| autodesk-bim360-issue | collaboration | Various |
| autodesk-bim360-issue | coordination | Various |
| autodesk-bim360-issue | design | Various |
| autodesk-bim360-issue | issue | Various |
| autodesk-bim360-issue | quality | Various |
| autodesk-bim360-modelcoordination | clashgroup | Model Coordination |
| autodesk-bim360-modelcoordination | container | Model Coordination |
| autodesk-bim360-modelcoordination | documentlineage | Model Coordination |
| autodesk-bim360-modelcoordination | scope | Model Coordination |
| autodesk-bim360-rfi | rfi | Project Management |

### Additional Relationship Service Entity Types

The following table lists `Domains` and `Entity Types` currently supported by the Relationship Service which are not yet available via a BIM 360 API.

| Domain | Entity Type | BIM 360 Module |
| --- | --- | --- |
| autodesk-bim360-locations | location | Various |
| autodesk-bim360-markup | markup | Various |
| autodesk-bim360-meetingminutes | meeting | Project Management |
| autodesk-bim360-meetingminutes | meetingitem | Project Management |

## [Get Relationships by ID](#get-relationships-by-id)

The [get relationship by unique ID endpoint](/en/docs/bim360/v1/reference/http/relationships-get-relationship-by-id-GET) is used to retrieve a relationship given its GUID unique ID. This endpoint is only typically useful if you have previously cached the IDs of relationships from a search query (see below).

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/04074497-ed5d-4ea3-861d-1f146418f5bb/relationships/b544a7eb-3c64-4a56-a7ff-392d0441015f'
     -H 'Authorization: Bearer <token>'

```

### Example Response

```
{
    "id": "b544a7eb-3c64-4a56-a7ff-392d0441015f",
    "createdOn": "2015-10-21T16:32:22Z",
    "isReadOnly": true,
    "isService": false,
    "isDeleted": false,
    "entities": [
        {
            "createdOn": "2015-10-21T16:32:22Z",
            "domain": "autodesk-bim360-asset",
            "type": "asset",
            "id": "b1d1e7d4-f0ed-11e9-81b4-2a2ae2dbcce4"
        },
        {
            "createdOn": "2015-10-21T16:32:22Z",
            "domain": "autodesk-bim360-issue",
            "type": "issue",
            "id": "92d6bb28-9c5c-424a-8b29-6d847542fa7f"
        }
    ]
}

```

Show More

In the case of this example the relationship ID `b544a7eb-3c64-4a56-a7ff-392d0441015f` corresponds to an association between an Asset and an Issue.

## [Get Relationship Batch](#get-relationship-batch)

The [relationship batch endpoint](/en/docs/bim360/v1/reference/http/relationships-get-relationships-batch-POST) can be used to retrieve a set of relationships using their unique GUID IDs. This endpoint is only typically useful if you have previously cached the IDs of relationships from a search query (see below).

### Example Request

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/04074497-ed5d-4ea3-861d-1f146418f5bb/relationships:batch' \
     -X POST \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: application/json' \
     -d '[
           "d98c1dd4-008f-04b2-e980-0998ecf8427e",
           "b544a7eb-3c64-4a56-a7ff-392d0441015f"
         ]'

```

Show More

### Example Response

```
[
    {
        "id": "d98c1dd4-008f-04b2-e980-0998ecf8427e",
        "createdOn": "2015-10-21T16:32:22Z",
        "isReadOnly": true,
        "isService": false,
        "isDeleted": false,
        "entities": [
            {
                "createdOn": "2015-10-21T16:32:22Z",
                "domain": "autodesk-bim360-asset ",
                "type": "asset",
                "id": "b43e4bb3-0223-430d-bc2c-2adfdf3c629f"
            },
            {
                "createdOn": "2015-10-21T16:32:22Z",
                "domain": "autodesk-bim360-issue",
                "type": "issue",
                "id": "b625c02e-52c8-4a64-9874-8a5195f1de6c"
            }
        ]
    },
    {
        "id": "b544a7eb-3c64-4a56-a7ff-392d0441015f",
        "createdOn": "2015-10-21T16:32:22Z",
        "isReadOnly": true,
        "isService": false,
        "isDeleted": false,
        "entities": [
            {
                "createdOn": "2015-10-21T16:32:22Z",
                "domain": "autodesk-bim360-asset",
                "type": "asset",
                "id": "b1d1e7d4-f0ed-11e9-81b4-2a2ae2dbcce4"
            },
            {
                "createdOn": "2015-10-21T16:32:22Z",
                "domain": "autodesk-bim360-issue",
                "type": "issue",
                "id": "92d6bb28-9c5c-424a-8b29-6d847542fa7f"
            }
        ]
    }
]

```

Show More

## [Relationship Search vs. Intersect](#relationship-search-vs-intersect)

Whilst superficially similar, the relationship search and intersect endpoints have been designed to serve two very different use cases. When choosing between search and intersect it is important to remember the relationship domain entity model is hierarchical whilst considering what you are trying to achieve. To recap, a domain can have many entity types and for any given domain entity type there can be one or more instances of this type in the domain, represented by the ID of the instance.

![../../../_images/domain-relationships.png](../../../_images/domain-relationships.png)

Both the search and intersect endpoints contain an implicit assumption that users understand the existence of this hierarchy. If searching for relationships to a specific entity the assumption holds that the user will supply not only the entityâs ID but also itâs entity type and domain. Likewise when searching for relationships to specific entity types (omitting an ID) the assumption holds that the user will supply not only the entity type but also the domain. The domain is at the top of the hierarchy so no supplementary qualification is required when searching for relationships to domains.

The search endpoint is a `GET` method requiring users to supply search criteria which will be used to match either end of the relationships stored for the project. For example, it can be used to search for all the relationships between (with) the issues domain and asset entity types in the assets domain. By further qualifying the search we can retrieve relationships between coordination issues types in the issues domain and asset entity types in the assets domain. Finally we can specify a specific entity instance and intersect it with either a domain, entity type and domain or another fully qualified entity.

By contrast the intersect endpoint makes more specific starting assumptions about the nature of the search you are performing. Unlike the search endpoint the intersect endpoint requires users to `POST` a set of fully qualified domain entities (domain, entity type and id) along with a domain, domain and entity type or a second set of fully qualified domain entities. The intersect endpoint literally intersects these two sets with the relationships in the system. This endpoint has been specifically designed to support paged workflows where the requirement is to efficiently find entities related to a starting fixed set of known entities. For example suppose you have queried the BIM 360 issues service and are paging through the resulting issues returned by the service. You can use the intersect endpoint to pass in batches of issues and query the things (entities) these issues are related to. You may restrict this query to intersect specific domains, domain and entity types or a second set of specific entities. For example to determine if the issues returned from the issues service were associated with assets you would restrict the intersection to the asset entity type in the assets domain.

## [Search Relationships](#search-relationships)

The [relationship search endpoint](/en/docs/bim360/v1/reference/http/relationships-search-relationships-GET) can be used to retrieve relationships using the domain, entity type and id hierarchy [implicit in the relationship serviceâs data model](/en/docs/bim360/v1/overview/field-guide/relationships). The search endpoint uses the `domain`, `type`, `id`, `withDomain`, `withType` and `withId` query parameters to control the search endpointâs behaviour. `Deleted` relationships will only be returned if the `includeDeleted` query parameter is set to true. Remember the importance of supplying fully qualified search qualifiers `domain+entityType+id`, `domain+entityType` or `domain` on either side of the search.

### Example Request

In this request we are searching for relationships which exists between the issue entity type in the issues domain and the asset entity type in the assets domain which were created between a specific date range, we have also optionally chosen to include deleted relationships in this search.

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/04074497-ed5d-4ea3-861d-1f146418f5bb/relationships:search?domain=autodesk-bim360-issue&type=issue&createdAfter=2015-10-21T16%3a32%3a21Z&createdBefore=2015-10-21T16%3a30%3a45Z&withDomain=autodesk-bim360-asset&withType=asset&includeDeleted=True&pageLimit=20' \
     -H 'Authorization: Bearer <token>'

```

### Example Response

```
{
    "page": {
        "continuationToken": "10",
        "syncToken": "eyAibGFzdENoZWNrZWQiOiIyMDE5LTEwLTE4VDEyOjEwOjA3Ljc5NloiIH0="
    },
    "relationships": [
        {
            "id": "d98c1dd4-008f-04b2-e980-0998ecf8427e",
            "createdOn": "2015-10-21T16:32:22Z",
            "isReadOnly": true,
            "isService": false,
            "isDeleted": false,
            "entities": [
                {
                    "createdOn": "2015-10-21T16:32:22Z",
                    "domain": "autodesk-bim360-asset ",
                    "type": "asset",
                    "id": "b43e4bb3-0223-430d-bc2c-2adfdf3c629f"
                },
                {
                    "createdOn": "2015-10-21T16:32:22Z",
                    "domain": "autodesk-bim360-issue",
                    "type": "issue",
                    "id": "b625c02e-52c8-4a64-9874-8a5195f1de6c"
                }
            ]
        },
        {
            "id": "b544a7eb-3c64-4a56-a7ff-392d0441015f",
            "createdOn": "2015-10-21T16:32:22Z",
            "isReadOnly": true,
            "isService": false,
            "isDeleted": false,
            "entities": [
                {
                    "createdOn": "2015-10-21T16:32:22Z",
                    "domain": "autodesk-bim360-asset",
                    "type": "asset",
                    "id": "b1d1e7d4-f0ed-11e9-81b4-2a2ae2dbcce4"
                },
                {
                    "createdOn": "2015-10-21T16:32:22Z",
                    "domain": "autodesk-bim360-issue",
                    "type": "issue",
                    "id": "92d6bb28-9c5c-424a-8b29-6d847542fa7f"
                }
            ]
        }
    ]
}

```

Show More

## [Intersect Relationships](#intersect-relationships)

The [relationship intersection endpoint](/en/docs/bim360/v1/reference/http/relationships-intersect-relationships-POST) is similar to the [relationship search endpoint](/en/docs/bim360/v1/reference/http/relationships-search-relationships-GET) in that it allows callers to control the domains and entity types which are being queried. The intersection endpoint however takes things one step further in that it requires users to pass a set of entities and then intersect these entities with other domains and entity types. Callers `POST` two collections of domain entities , `entities` which must be fully specified (Domain, Entity and Entity ID) and a second collection `withEntities` which can be fully or partially specified. In the following example four BIM 360 assets are passed in the `entities` collection and the `withEntities` collection is used to request relationships which contain these assets and links to any issues or photos associated with these assets.

### Example Request

In this example we have a set of asset entities from the assets domain and we are intersecting this set of entities with the issues domain to find issues which are related to the assets passed in the `entities` collection.

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/04074497-ed5d-4ea3-861d-1f146418f5bb/relationships:intersect' \
     -X POST \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "entities": [
             {
               "domain": "autodesk-bim360-asset",
               "type": "asset",
               "id": "b1d1e7d4-f0ed-11e9-81b4-2a2ae2dbcce4"
             },
             {
               "domain": "autodesk-bim360-asset",
               "type": "asset",
               "id": "8d7b691a-6631-4ea0-af7b-df9e2e3922c5"
             },
             {
               "domain": "autodesk-bim360-asset",
               "type": "asset",
               "id": "fb86ee43-e920-476f-908e-33da70c66551"
             },
             {
               "domain": "autodesk-bim360-asset",
               "type": "asset",
               "id": "a2303c73-5460-42f8-9ec8-089d2aecc6b3"
             }
           ],
           "withEntities": [
             {
               "domain": "autodesk-bim360-issue",
               "type": "issue"
             }
           ]
         }'

```

Show More

### Example Response

```
{
    "page": {
        "continuationToken": null,
        "syncToken": "eyAibGFzdENoZWNrZWQiOiIyMDE5LTEwLTE4VDEyOjEwOjA3Ljc5NloiIH0="
    },
    "relationships": [
        {
            "id": "d98c1dd4-008f-04b2-e980-0998ecf8427e",
            "createdOn": "2015-10-21T16:32:22Z",
            "isReadOnly": true,
            "isService": false,
            "isDeleted": false,
            "entities": [
                {
                    "createdOn": "2015-10-21T16:32:22Z",
                    "domain": "autodesk-bim360-asset ",
                    "type": "asset",
                    "id": "b1d1e7d4-f0ed-11e9-81b4-2a2ae2dbcce4"
                },
                {
                    "createdOn": "2015-10-21T16:32:22Z",
                    "domain": "autodesk-bim360-issue",
                    "type": "issue",
                    "id": "b625c02e-52c8-4a64-9874-8a5195f1de6c"
                }
            ]
        },
        {
            "id": "b544a7eb-3c64-4a56-a7ff-392d0441015f",
            "createdOn": "2015-10-21T16:32:22Z",
            "isReadOnly": true,
            "isService": false,
            "isDeleted": false,
            "entities": [
                {
                    "createdOn": "2015-10-21T16:32:22Z",
                    "domain": "autodesk-bim360-asset",
                    "type": "asset",
                    "id": "a2303c73-5460-42f8-9ec8-089d2aecc6b3"
                },
                {
                    "createdOn": "2015-10-21T16:32:22Z",
                    "domain": "autodesk-bim360-issue",
                    "type": "issue",
                    "id": "92d6bb28-9c5c-424a-8b29-6d847542fa7f"
                }
            ]
        }
    ]
}

```

Show More

In the response above only two assets in the request are returned. This indicates that only these two assets have a connection to an Issue or Photo, the other two assets did not have any relationships to Issues or Photos.

## [Relationship Sync](#relationship-sync)

The relationship service supports full data synchronisation via the [relationship sync endpoint](/en/docs/bim360/v1/reference/http/relationships-relationships-sync-POST). This endpoint allows callers to replicate ALL of the relationships stored in the relationship service to an external repository. After relationships have been initially replicated subsequent calls to the the sync endpoint can be used to discover changes which have occurred between the time the initial synchronisation ended and ânowâ.

### Bootstrapping Sync with no syncToken

Calling the [relationship sync endpoint](/en/docs/bim360/v1/reference/http/relationships-relationships-sync-POST) with no initial `syncToken` will result in a full download of all the relationships currently in the system.

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/04074497-ed5d-4ea3-861d-1f146418f5bb/relationships:sync' \
     -X POST \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: application/json' \
     -d '{
        "syncToken": null,
        "filters": null
     }'

```

Show More

### Calling Sync with a syncToken

Calling the [relationship sync endpoint](/en/docs/bim360/v1/reference/http/relationships-relationships-sync-POST) with a `syncToken` will result in a full download of all the relationships which have changed (been added to the service or deleted) since the initial call which yielded the `syncToken` passed in the request. The [relationship search endpoint](/en/docs/bim360/v1/reference/http/relationships-search-relationships-GET) and the [relationship intersection endpoint](/en/docs/bim360/v1/reference/http/relationships-intersect-relationships-POST) both return syncTokens in the page header in their responses. These syncTokens can be passed to the [relationship sync endpoint](/en/docs/bim360/v1/reference/http/relationships-relationships-sync-POST) to limit the scope of the synchronisation. For example if a syncToken from a filtered search is used then the relationships downloaded will be restricted by the same search criteria used in the search request.

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/04074497-ed5d-4ea3-861d-1f146418f5bb/relationships:sync' \
     -X POST \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: application/json' \
     -d '{
        "syncToken": "eyAibGFzdENoZWNrZWQiOiIyMDE5LTEwLTE4VDEyOjEwOjA3Ljc5NloiIH0=",
        "filters": null
     }'

```

Show More

### Sync Token Response

```
{
    "current": {
        "data": [
            {
                "id": "d98c1dd4-008f-04b2-e980-0998ecf8427e",
                "createdOn": "2015-10-21T16:32:22Z",
                "isReadOnly": true,
                "isService": false,
                "isDeleted": false,
                "entities": [
                    {
                        "createdOn": "2015-10-21T16:32:22Z",
                        "domain": "autodesk-bim360-asset ",
                        "type": "asset",
                        "id": "b1d1e7d4-f0ed-11e9-81b4-2a2ae2dbcce4"
                    },
                    {
                        "createdOn": "2015-10-21T16:32:22Z",
                        "domain": "autodesk-bim360-issue",
                        "type": "issue",
                        "id": "b625c02e-52c8-4a64-9874-8a5195f1de6c"
                    }
                ]
            }
        ]
    },
    "deleted": {
        "data": [
            {
                "id": "74b70bb8-8802-a1fd-f201-890375a60c8f",
                "createdOn": "2015-10-21T16:32:22Z",
                "isReadOnly": true,
                "isService": false,
                "isDeleted": true,
                "entities": [
                    {
                        "createdOn": "2015-10-21T16:32:22Z",
                        "domain": "autodesk-bim360-asset",
                        "type": "asset",
                        "id": "a2303c73-5460-42f8-9ec8-089d2aecc6b3"
                    },
                    {
                        "createdOn": "2015-10-21T16:32:22Z",
                        "domain": "autodesk-bim360-issue",
                        "type": "issue",
                        "id": "92d6bb28-9c5c-424a-8b29-6d847542fa7f"
                    }
                ]
            }
        ]
    },
    "moreData": true,
    "overwrite": false,
    "nextSyncToken": "eyAibGFzdENoZWNrZWQiOiIyMDE5LTEwLTE4VDEyOjEwOjA3Ljc5NloiIH0="
}

```

Show More

### Relationship Sync Status

The [relationship service sync status endpoint](/en/docs/bim360/v1/reference/http/relationships-relationships-sync-status-POST) can be used to check if there is new data or changes available for a given syncToken. This endpoint accepts multiple syncTokens and returns a response for each syncToken passed. If `moreData` is set to `true` then a call to the [relationship sync endpoint](/en/docs/bim360/v1/reference/http/relationships-relationships-sync-POST) with the syncToken passed in the status check will yield updated relationships. The `overwrite` flag instructs callers âre-setâ their copy of the relationship data if it is set to `true`.

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/04074497-ed5d-4ea3-861d-1f146418f5bb/relationships:syncStatus' \
     -X POST \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: application/json' \
     -d '[
           {
             "syncToken": "eyAibGFzdENoZWNrZWQiOiIyMDE5LTEwLTE4VDEyOjEwOjA3Ljc5NloiIH0="
           }
         ]'

```

Show More

### Sync Status Response - More Data

```
{
    "results": [
        {
            "moreData": true,
            "overwrite": false,
            "syncToken": "eyAibGFzdENoZWNrZWQiOiIyMDE5LTEwLTE4VDEyOjEwOjA3Ljc5NloiIH0="
        }
    ]
}

```

Show More

### Sync Status Response - No New Data

```
{
    "results": [
        {
            "moreData": false,
            "overwrite": false,
            "syncToken": "eyAibGFzdENoZWNrZWQiOiIyMDE5LTEwLTE4VDEyOjEwOjA3Ljc5NloiIH0="
        }
    ]
}

```

Show More
