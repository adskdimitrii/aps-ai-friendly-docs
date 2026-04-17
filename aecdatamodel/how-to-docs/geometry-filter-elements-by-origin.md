# Filter Elements by their Origin

Source: https://aps.autodesk.com/en/docs/aecdatamodel/tutorials/geometry/filter-elements-by-origin/

---

# Filter Elements by their Origin

This tutorial shows how to filter elements in an ElementGroup based on their spatial location using origin coordinates. Origin-based filtering is essential for location-aware queries, spatial analysis, zone-based element selection, and clash detection workflows. By filtering elements within a specific 3D area, you can isolate components in particular building zones or coordinate ranges.

By the end of this guide, you will be able to:

- Locate element groups containing geometry data using folder-based queries.
- Filter elements by their origin coordinates within a specified 3D area.
- Query all elements that have origin component data available.
- Understand the origin coordinate system and construct effective spatial queries.
- Apply origin filters for zone-based selection and spatial analysis workflows.

In this tutorial, you will learn how to filter elements in an ElementGroup by their Origin, by using the [OriginComponentFilter](../reference-docs/inputs-origincomponentfilterinput.md).
You will use the following queries in this guide:

| Type | Operation | Description |
| --- | --- | --- |
| Query | [elementGroupsByFolderAndSubFolders](../reference-docs/queries-elementgroupsbyfolderandsubfolders.md) | Retrieves element groups inside a folder and its subfolders, using additional filters if provided. |
| Query | [elementsByElementGroup](../reference-docs/queries-elementsbyelementgroup.md) | Retrieves elements inside a group with RSQL filtering and component data. |

## [Task 1: Find the element group](#task-1-find-the-element-group)

Enter the following query to discover element group with geometry data in desired folder

**elementGroupsByFolderAndSubFolders Query**

```
query elementGroupsByFolderAndSubFolders($projectId: ID!, $folderId: ID!, $pagination: PaginationInput) {
        elementGroupsByFolderAndSubFolders(projectId: $projectId, folderId: $folderId, filter: $filter, pagination: $pagination) {
            pagination {
                pageSize
                cursor
            }
            results {
                id
                name
            }
        }
}

```

Show More

**Variables**

```
{
  "projectId": "<YOUR_PROJECT_ID>",
  "folderId": "<YOUR_FOLDER_ID>",
  "pagination": {
   "limit": 100
    }
}

```

**Sample Response**

```
{
    "data": {
        "elementGroupsByFolderAndSubFolders": {
            "pagination": {
                "pageSize": 21,
                "cursor": null
            },
            "results": [
                {
                    "id": "<YOUR_ELEMENT_GROUP_ID>",
                    "name": "<YOUR_ELEMENT_GROUP_NAME>"
                }
            ]
        }
    },
    "extensions": {
        "pointValue": {
            "requestedQueryPointValue": 11
        }
    }
}

```

Show More

For the rest of this tutorial, pick the elementGroupId of the elementGroup you are interested in from the above query.

## [Task 2: Filter Elements from an ElementGroup by their Origin](#task-2-filter-elements-from-an-elementgroup-by-their-origin)

In this task you will learn how to filter elements from the ElementGroup you selected in Task 1, by their OriginComponents.

**elementsByElementGroup Query**

```
query elementsByElementGroup($elementGroupId: ID!, $filter: ElementFilterInput) {
    elementsByElementGroup(elementGroupId: $elementGroupId, filter: $filter) {
        pagination{
            pageSize
            cursor
        }
        results {
            id
            name
            alternativeIdentifiers{
                revitElementId
            }
            components (filter: {types: [ORIGIN]}){
                results{
                    ... on OriginComponent{
                        componentType
                        origin{
                            x
                            y
                            z
                        }
                    }
                }
            }
        }
    }
}

```

Show More

**Variables**

```
{
    "elementGroupId": "<YOUR_ELEMENT_GROUP_ID>",
    "filter": {
        "originComponentFilter": {
            "originRange": {
                "startPoints": {
                   "x": x1,
                   "y": y1,
                   "z": z1
                },
                "endPoints": {
                   "x": x2,
                   "y": y2,
                   "z": z2
                }
            }
        }
    }
}

```

Show More

Here the elementGroupId is the ID you selected in Task 1 and x1, y1, and z1 are the start coordinates of the range and x2, y2 and z2 are the end coordinates of the range you are interested in.

**Sample Response**

```
{
    "data": {
        "elementsByElementGroup": {
            "pagination": {
                "pageSize": 7,
                "cursor": null
            },
            "results": [
                {
                    "id": "YWVjZX5sWTh2Z3AwRmRtQVQ0SUdkQjBXdVNMX0wyQ34wMzk3Y2JkNC1mNzlkLTUwYTQtOTdhZi0wODc0MmZjZjk3OTg",
                    "name": "Generic - 12\"",
                    "alternativeIdentifiers": {
                        "revitElementId": "155332"
                    },
                    "components": {
                        "results": [
                            {
                                "componentType": "ORIGIN",
                                "origin": {
                                    "x": -27.241926331003356,
                                    "y": -91.80926693875303,
                                    "z": 0.0
                                }
                            }
                        ]
                    }
                },
                {
                    "id": "YWVjZX5sWTh2Z3AwRmRtQVQ0SUdkQjBXdVNMX0wyQ340Y2U2NGYyZS0xNjEzLTVjYTktOGZjOC01YzFhYWZiYTY2ODI",
                    "name": "Detail Lines",
                    "alternativeIdentifiers": {
                        "revitElementId": "154714"
                    },
                    "components": {
                        "results": [
                            {
                                "componentType": "ORIGIN",
                                "origin": {
                                    "x": -26.132923492090246,
                                    "y": -82.44124049541749,
                                    "z": 0.0
                                }
                            }
                        ]
                    }
                },
                ................
            ]
        }
    },
    "extensions": {
        "pointValue": {
            "requestedQueryPointValue": 11,
            "responseQueryPointValue": 0
        }
    }
}

```

Show More

The response will then return all elements with an OriginComponent within that range

## [Task 3: Get All Elements with an OriginComponent in an ElementGroup](#task-3-get-all-elements-with-an-origincomponent-in-an-elementgroup)

In this task you will learn how to get all elements from the ElementGroup you selected in Task 1, that have an OriginComponent.

**elementsByElementGroup Query**

```
query elementsByElementGroup($elementGroupId: ID!, $filter: ElementFilterInput) {
    elementsByElementGroup(elementGroupId: $elementGroupId, filter: $filter) {
        pagination{
            pageSize
            cursor
        }
        results {
            id
            name
            alternativeIdentifiers{
                revitElementId
            }
            components (filter: {types: [ORIGIN]}){
                results{
                    ... on OriginComponent{
                        componentType
                        origin{
                            x
                            y
                            z
                        }
                    }
                }
            }
        }
    }
}

```

Show More

**Variables**

```
{
    "elementGroupId": "<YOUR_ELEMENT_GROUP_ID>",
    "filter": {
        "originComponentFilter": {
            "exists": true
        }
    }
}

```

Show More

Here the elementGroupId is the ID you selected in Task 1.

**Sample Response**

```
{
    "data": {
        "elementsByElementGroup": {
            "pagination": {
                "pageSize": 50,
                "cursor": "Y3Vyc341MH41MA"
            },
            "results": [
                {
                    "id": "YWVjZX5sWTh2Z3AwRmRtQVQ0SUdkQjBXdVNMX0wyQ34wMDAzZjU2NC0xOWI4LTU3MTYtYmMxOS0wMWUxMGNhMjhjOWI",
                    "name": "Interior - 5\" Partition (2-hr)",
                    "alternativeIdentifiers": {
                        "revitElementId": "205055"
                    },
                    "components": {
                        "results": [
                            {
                                "componentType": "ORIGIN",
                                "origin": {
                                    "x": 10.57055031648508,
                                    "y": -148.56258366330073,
                                    "z": 0.0
                                }
                            }
                        ]
                    }
                },
                {
                    "id": "YWVjZX5sWTh2Z3AwRmRtQVQ0SUdkQjBXdVNMX0wyQ34wMDEwOGMyYi1kMTM3LTVjN2MtOGQ2NC1kNGM0Mjg1MWZiMDA",
                    "name": "Detail Lines",
                    "alternativeIdentifiers": {
                        "revitElementId": "205728"
                    },
                    "components": {
                        "results": [
                            {
                                "componentType": "ORIGIN",
                                "origin": {
                                    "x": -22.003074422013373,
                                    "y": -240.0996393745324,
                                    "z": 0.0
                                }
                            }
                        ]
                    }
                },
                ................
            ]
        }
    },
    "extensions": {
        "pointValue": {
            "requestedQueryPointValue": 11,
            "responseQueryPointValue": 0
        }
    }
}

```

Show More

The response will then return all elements with an OriginComponent.
