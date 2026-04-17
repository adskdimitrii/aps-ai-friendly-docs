# Get Axis and Origin Information for Elements

Source: https://aps.autodesk.com/en/docs/aecdatamodel/tutorials/geometry/get-axis-origin-elements/

---

# Get Axis and Origin Information for Elements

This guide shows how to extract precise geometric data from structural beam elements for fabrication workflows. Beam axis and origin data is essential for CNC programming, shop drawings, and automated fabrication processes because fabrication requires exact positioning and orientation data. The axis defines the beam’s centerline for cutting and drilling operations, while the origin provides the reference point for placement.

By the end of this guide, you will be able to:

- Locate element groups containing structural geometry data using folder-based queries.
- Filter elements by category to target only structural framing (beam) elements.
- Extract axis and origin component data from beam elements for fabrication workflows.
- Understand the geometric data structure and how to calculate beam dimensions from response data.

You will use the following queries in this guide:

## [Task 1: Find the element group](#task-1-find-the-element-group)

Enter the following query to discover element group with geometry data in desired folder

**elementGroupsByFolder Query**

```
query elementGroupsByFolder($projectId: ID!, $folderId: ID!, $pagination: PaginationInput) {
        elementGroupsByFolder(projectId: $projectId, folderId: $folderId, filter: $filter, pagination: $pagination) {
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
  "projectId": "urn:adsk.workspace:beta.project:b00c749f-e6a9-4153-b1c9-00f73db65d93",
  "folderId": "urn:adsk.wipstg:fs.folder:co.vf8mHX_QQXWG7Bv1J_-wJA",
  "pagination": { "limit": 20 }
}

```

**Sample Response**

```
{
    "data": {
        "elementGroupsByFolder": {
            "pagination": {
                "pageSize": 21,
                "cursor": null
            },
            "results": [
                {
                    "id": "YWVjZH5sWTh2Z3AwRmRtQVQ0SUdkQjBXdVNMX0wyQ35kNjRiYTQ4Zi00MzNhLTVkZWYtOWZmNS00YThmODkwYjhhZWE",
                    "name": "Snowdon Towers Sample Structural_2026.rvt"
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

For this tutorial, we’ll use the “Snowdon Towers Sample Structural_2026.rvt” element group:

`YWVjZH5sWTh2Z3AwRmRtQVQ0SUdkQjBXdVNMX0wyQ35kNjRiYTQ4Zi00MzNhLTVkZWYtOWZmNS00YThmODkwYjhhZWE`

## [Task 2: Query beam elements for axis and origin data](#task-2-query-beam-elements-for-axis-and-origin-data)

Extracting geometric component data specifically from structural framing elements (beams). The filter property.name.category==’Structural Framing’ and ‘property.name.Element Context’==Instance targets only beam elements, and the components filter {types: [ORIGIN, AXIS]} returns the precise geometric data needed for fabrication.

```
query elementsByElementGroup($elementGroupId: ID!, $pagination: PaginationInput) {
        elementsByElementGroup(elementGroupId: $elementGroupId, filter: {query: "property.name.category=='Structural Framing' and 'property.name.Element Context'==Instance"}, pagination: $pagination) {
            pagination {
                pageSize
                cursor
            }
            results {
                id
                name
                components (filter: {types: [ORIGIN, AXIS]}){
                    results {
                        componentType
                        ... on AxisRepresentationComponent {
                            curve {
                                type
                                ... on Line {
                                    position  {
                                        x
                                        y
                                        z
                                    }
                                    range{
                                        low
                                        high
                                        type
                                    }
                                }
                            }
                        }
                        ... on OriginComponent {
                            origin {
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
    "elementGroupId": "YWVjZH5sWTh2Z3AwRmRtQVQ0SUdkQjBXdVNMX0wyQ35kNjRiYTQ4Zi00MzNhLTVkZWYtOWZmNS00YThmODkwYjhhZWE"
}

```

**Sample Response**

```
{
    "data": {
        "elementsByElementGroup": {
            "pagination": {
                "pageSize": 50,
                "cursor": "Y3Vyc241MH41MA"
            },
            "results": [
                {
                    "id": "YWVjZX5sWTh2Z3AwRmRtQVQ0SUdkQjBXdVNMX0wyQ34wMDJkMDNhYi0wYTcyLTVhOWYtOTMwZi01ZGEzYTYzMGFmZmQ",
                    "name": "16K2",
                    "components": {
                        "results": [
                            {
                                "componentType": "ORIGIN",
                                "origin": {
                                    "x": -3.7507333333332604,
                                    "y": 1.6763999999997956,
                                    "z": 17.780000000000005
                                }
                            },
                            {
                                "componentType": "AXIS",
                                "curve": {
                                    "type": "LINE",
                                    "position": {
                                        "x": -3.7507333333332604,
                                        "y": 1.6763999999997956,
                                        "z": 17.780000000000005
                                    },
                                    "range": {
                                        "low": 0.0,
                                        "high": 4.178300000000179,
                                        "type": 1
                                    }
                                }
                            }
                        ]
                    }
                },
                ...
                ...
                ...
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

The response provides key data points for fabrication: the Origin is the 3D reference point for beam placement, the Axis Position shows starting coordinates of the beam centerline, and the Range provides the length span (high - low = beam length). This data feeds directly into CNC programming for automated cutting, drilling, and positioning operations.

Tip

Beam length = `range.high - range.low` (4.18 units in this example)
