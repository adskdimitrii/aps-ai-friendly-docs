# Task 4 â Extract Metadata

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/xtract-metadata/task4-extract_metadata/

---

# Task 4 â Extract Metadata

In order to extract metadata, you must wait until the translation job is done. There are two ways by which you can do this:

1. Periodically download the manifest and check if its `status` is `complete`.
2. Set up a webhook to notify you when the job is done.

## [Expected task outcome](#expected-task-outcome)

By the end of this task you will be able to:

- Get a list of Viewables contained within a model.
- Use the metadata GUID of the Viewable to retrieve the properties of objects in the Viewable.

You will use the following operations in this task:

| Operation | HTTP Request |
| --- | --- |
| [Fetch Manifest](../http-docs/http-urn-manifest-GET.md) | GET /{urn}/manifest |
| [List Model Views](../http-docs/http-urn-metadata-GET.md) | GET /{urn}/metadata |
| [Fetch Object Tree](../http-docs/http-urn-metadata-guid-GET.md) | GET /{urn}/metadata/{modelGuid} |
| [Fetch All Properties](../http-docs/http-urn-metadata-guid-properties-GET.md) | GET /{urn}/metadata/{modelGuid}/properties |
| [Fetch Specific Properties](../http-docs/http-urn-metadata-guid-properties-query-POST.md) | POST /{urn}/metadata/{modelGuid}/properties:query |

## [Step 1 - Check the status of the translation job](#step-1-check-the-status-of-the-translation-job)

### Request

```
curl  -X GET \
      'https://developer.api.autodesk.com/modelderivative/v2/designdata/<URL_SAFE_URN_OF_SOURCE_FILE>/manifest' \
      -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

```

When the translation job completes successfully, you will see a response similar to:

### Response

```
{
  "urn": "dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxfZGVyaXZhdGl2ZV9wcm9wX2VuaGFuY2VtZW50X3Rlc3RpbmcvcmFjX2Jhc2ljX3NhbXBsZV9wcm9qZWN0LnJ2dA",
  "derivatives": [
    {
      "hasThumbnail": "true",
      "children": [
        {
          "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxfZGVyaXZhdGl2ZV9wcm9wX2VuaGFuY2VtZW50X3Rlc3RpbmcvcmFjX2Jhc2ljX3NhbXBsZV9wcm9qZWN0LnJ2dA/output/Resource/model.sdb",
          "role": "Autodesk.CloudPlatform.PropertyDatabase",
          "mime": "application/autodesk-db",
          "guid": "6fac95cb-af5d-3e4f-b943-8a7f55847ff1",
          "type": "resource",
          "status": "success"
        },
        {
          "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxfZGVyaXZhdGl2ZV9wcm9wX2VuaGFuY2VtZW50X3Rlc3RpbmcvcmFjX2Jhc2ljX3NhbXBsZV9wcm9qZWN0LnJ2dA/output/Resource/AECModelData.json",
          "role": "Autodesk.AEC.ModelData",
          "mime": "application/json",
          "guid": "a4aac952-a3f4-031c-4113-b2d9ac2d0de6",
          "type": "resource",
          "status": "success"
        },
        {

          "...truncated for clarity": ""

        }
      ],
      "name": "rac_basic_sample_project.rvt",
      "progress": "complete",
      "outputType": "svf2",
      "properties": {
        "Document Information": {
          "RVTVersion": "2020",
          "Project Name": "Sample House",
          "Project Number": "001-00",
          "Author": "Samuel Macalister",
          "Project Address": "Enter address here",
          "Project Issue Date": "Issue Date",
          "Project Status": "Project Status",
          "Building Name": "Samuel Macalister sample house design",
          "Client Name": "Autodesk",
          "Organization Name": "Autodesk",
          "Organization Description": ""
        }
      },
      "status": "success"
    },
    {
      "children": [
        {
          "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxfZGVyaXZhdGl2ZV9wcm9wX2VuaGFuY2VtZW50X3Rlc3RpbmcvcmFjX2Jhc2ljX3NhbXBsZV9wcm9qZWN0LnJ2dA/output/preview1.png",
          "role": "thumbnail",
          "mime": "image/png",
          "guid": "db899ab5-939f-e250-d79d-2d1637ce4565",
          "type": "resource",
          "resolution": [
            100,
            100
          ],
          "status": "success"
        },
        {
          "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxfZGVyaXZhdGl2ZV9wcm9wX2VuaGFuY2VtZW50X3Rlc3RpbmcvcmFjX2Jhc2ljX3NhbXBsZV9wcm9qZWN0LnJ2dA/output/preview2.png",
          "role": "thumbnail",
          "mime": "image/png",
          "guid": "3f6c118d-f551-7bf0-03c9-8548d26c9772",
          "type": "resource",
          "resolution": [
            200,
            200
          ],
          "status": "success"
        },
        {
          "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxfZGVyaXZhdGl2ZV9wcm9wX2VuaGFuY2VtZW50X3Rlc3RpbmcvcmFjX2Jhc2ljX3NhbXBsZV9wcm9qZWN0LnJ2dA/output/preview4.png",
          "role": "thumbnail",
          "mime": "image/png",
          "guid": "4e751806-0920-ce32-e9fd-47c3cec21536",
          "type": "resource",
          "resolution": [
            400,
            400
          ],
          "status": "success"
        }
      ],
      "progress": "complete",
      "outputType": "thumbnail",
      "status": "success"
    }
  ],
  "hasThumbnail": "true",
  "progress": "complete",
  "type": "manifest",
  "region": "US",
  "version": "1.0",
  "status": "success"
}

```

Show More

## [Step 2 - Retrieve a list of Viewables](#step-2-retrieve-a-list-of-viewables)

Once the source file has been translated to SVF2, you can retrieve a list of model view (metadata) IDs contained within the source file.

Note: Although the Revit file used in this walkthrough contains multiple model views, Fusion 360 and Inventor models contain only a single model view.

### Request

```
curl  -X GET \
      'https://developer.api.autodesk.com/modelderivative/v2/designdata/<URL_SAFE_URN_OF_SOURCE_FILE>/metadata' \
      -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

```

### Response

```
{
    "data": {
        "type": "metadata",
        "metadata": [
            {
                "name": "{3D}",
                "role": "3d",
                "guid": "6bfb4886-f2ee-9ccb-8db0-c5c170220c40"
            },
            {
                "name": "A102 - Plans",
                "role": "2d",
                "guid": "abdacd31-f94c-e84f-9a58-4663e281d894"
            },
            {
                "name": "A104 - Elev./Sec./Det.",
                "role": "2d",
                "guid": "8be5a450-c03d-fcb2-6125-08d5baf4b9d9"
            },
            {
                "name": "A103 - Elevations/Sections",
                "role": "2d",
                "guid": "10f26e65-bbca-7a68-125e-749e559c1e3b"
            },
            {
                "name": "A105 - Elev./ Stair Sections",
                "role": "2d",
                "guid": "db90b95d-0265-5fe4-376a-4dd3386c3d7d"
            },
            {
                "name": "A101 - Site Plan",
                "role": "2d",
                "guid": "1fd6b2ec-267d-8ba3-6b00-abe1adf80994"
            },
            {
                "name": "A001 - Title Sheet",
                "role": "2d",
                "guid": "97e8b569-a295-8750-f788-2d5067608b9c"
            }
        ]
    }
}

```

Show More

Note down the value of `guid` of the first model view (Viewable), which is named `{3D}`. In the next few steps we will use this value as `<GUID_OF_VIEWABLE>`.

## [Step 3 - Get object hierarchy](#step-3-get-object-hierarchy)

Once you know the GUID of a Viewable, you can get the object tree of that Viewable.

- Replace `<GUID_OF_VIEWABLE>` with the `guid` returned for the Viewable named `{3D}`.

### Request

```
curl  -X GET \
      'https://developer.api.autodesk.com/modelderivative/v2/designdata/<URL_SAFE_URN_OF_SOURCE_FILE>/metadata/<GUID_OF_VIEWABLE>' \
      -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

```

Once you submit the request, the Model Derivative service starts extracting the object properties. If extracting properties takes time, the Model Derivative service will send you the following response. It implies that the request was accepted, but processing is still in progress. If you receive such a result, submit the request again.

### Response 1

```
{
  "result": "success"
}

```

### Response 2

```
{
  "data": {
    "type": "objects",
    "objects": [
      {
        "objectid": 1,
        "objects": [
          {
            "objectid": 161,
            "objects": [
              {
                "objectid": 5409,
                "objects": [
                  {
                    "objectid": 5414,
                    "objects": [
                      {
                        "objectid": 435,
                        "name": "RPC Male"
                      }
                    ],
                    "name": "Alex"
                  }
                ],
                "name": "RPC Male"
              },
              {
                "objectid": 5408,
                "objects": [
                  {
                    "objectid": 5412,
                    "objects": [
                      {
                        "objectid": 566,
                        "name": "RPC Female"
                      },
                      {
                        "objectid": 565,
                        "name": "RPC Female"
                      },
                      {
                        "objectid": 617,
                        "name": "RPC Female"
                      }
                    ],
                    "name": "YinYin"
                  }
                ],
                "name": "RPC Female"
              },
              {
                "objectid": 5407,
                "objects": [
                  {
                    "objectid": 5410,
                    "objects": [
                      {
                        "objectid": 303,
                        "name": "M_RPC Beetle"
                      }
                    ],
                    "name": "M_RPC Beetle"
                  }
                ],
                "name": "M_RPC Beetle"
              }
            ],
            "name": "Entourage"
          },
          {

            "... truncated for clarity": ""

          }
        ],
        "name": "Model"
      }
    ]
  }
}

```

Show More

## [Step 4 - Get object hierarchy (filtered)](#step-4-get-object-hierarchy-filtered)

Because the object tree can be very long, you can filter the list that is returned. If you know the `objectid` of the root node of a sub-tree, you can get the object tree for that sub tree. Note that it will also return the sub-trees of the siblings of that root node.

- Replace `<OBJECT_ID_OF_ROOT_OF_SUB_TREE>` with `161`, an `objectid` that was returned in the previous step.

### Request

```
curl  -X GET \
      'https://developer.api.autodesk.com/modelderivative/v2/designdata/<URL_SAFE_URN_OF_SOURCE_FILE>/metadata/<GUID_OF_VIEWABLE>?<OBJECT_ID_OF_ROOT_OF_SUB_TREE>' \
      -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

```

```
{
    "data": {
        "type": "objects",
        "objects": [
            {
                "objectid": 161,
                "objects": [
                    {
                        "objectid": 5409,
                        "objects": [
                            {
                                "objectid": 5414,
                                "objects": [
                                    {
                                        "objectid": 435,
                                        "name": "RPC Male"
                                    }
                                ],
                                "name": "Alex"
                            }
                        ],
                        "name": "RPC Male"
                    },
                    {
                        "objectid": 5408,
                        "objects": [
                            {
                                "objectid": 5412,
                                "objects": [
                                    {
                                        "objectid": 566,
                                        "name": "RPC Female"
                                    },
                                    {
                                        "objectid": 565,
                                        "name": "RPC Female"
                                    },
                                    {
                                        "objectid": 617,
                                        "name": "RPC Female"
                                    }
                                ],
                                "name": "YinYin"
                            }
                        ],
                        "name": "RPC Female"
                    },
                    {
                        "objectid": 5407,
                        "objects": [
                            {
                                "objectid": 5410,
                                "objects": [
                                    {
                                        "objectid": 303,
                                        "name": "M_RPC Beetle"
                                    }
                                ],
                                "name": "M_RPC Beetle"
                            }
                        ],
                        "name": "M_RPC Beetle"
                    }
                ],
                "name": "Entourage"
            }
        ]
    }
}

```

Show More

## [Step 5 - Retrieve properties of all objects in the Viewable](#step-5-retrieve-properties-of-all-objects-in-the-viewable)

Once you know the GUID of a Viewable, you can get the properties of all objects in that Viewable.

- Replace `<GUID_OF_VIEWABLE>` with the `guid` returned for the Viewable named `{3D}`

### Request

```
curl  -X GET \
      'https://developer.api.autodesk.com/modelderivative/v2/designdata/<URL_SAFE_URN_OF_SOURCE_FILE>/metadata/<GUID_OF_VIEWABLE>/properties' \
      -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

```

Once you submit the request, the Model Derivative service starts extracting the object properties. If extracting properties takes time, the Model Derivative service will send you the following response. It implies that the request was accepted, but processing is still in progress. If you receive such a result, submit the request again.

### Response 1

```
{
  "result": "success"
}

```

### Response 2

```
{
  "data": {
      "type": "properties",
      "collection": [
          {
              "objectid": 435,
              "name": "RPC Male",
              "externalId": "5ba82f05-9759-4b6e-8b19-8f869f7ed622-000e919b",
              "properties": {
                  "Identity Data": {
                      "Type Name": "Alex",
                      "Mark": "",
                      "Comments": "",
                      "Image": "",
                      "Code Name": "",
                      "OmniClass Title": "",
                      "OmniClass Number": "",
                      "Type Mark": "",
                      "Assembly Description": "",
                      "Cost": "0.000",
                      "Assembly Code": "",
                      "Description": "",
                      "URL": "",
                      "Type Comments": "",
                      "Manufacturer": "",
                      "Model": "",
                      "Keynote": "",
                      "Type Image": "",
                      "Render Appearance": "RPC-8-X9C2-NGU9-LXF5-4",
                      "Render Appearance Properties": "{2, 15},{22, RPC-8-X9C2-NGU9-LXF5-4},{1, 0},{1, 0},{2, 40},{1, 8},{5, Color},{1, 0},{1, 0},{3, 0.8},{3, 0.8},{3, 0.8},{1, 8},{7, BBoxMin},{1, 0},{1, 0},{1, 0},{1, 0},{1, 0},{1, 8},{7, BBoxMax},{1, 0},{1, 0},{1, 0},{1, 0},{1, 0},{2, 11},{9, RPCTypeId},{1, 0},{1, 0},{22, RPC-8-X9C2-NGU9-LXF5-4},{1, 6},{14, RPCPlantHeight},{1, 0},{1, 0},{7, 5.83333},{2, 11},{7, keyword},{1, 0},{1, 0},{18, :Geometry:RPC:Alex},{2, 11},{8, category},{1, 0},{1, 0},{16, :People [Casual]},{2, 11},{12, LocalizedUID},{1, 0},{1, 0},{4, Alex},{2, 14},{6, Height},{1, 0},{1, 0},{7, 5.83333},{1, 2},{16, Cast Reflections},{1, 0},{1, 0},{1, 0},{1, 2},{6, Jitter},{1, 0},{1, 0},{1, 1},{1, 2},{9, Billboard},{1, 0},{1, 0},{1, 0},{1, 2},{12, Cast Shadows},{1, 0},{1, 0},{1, 1},{1, 2},{20, Apply Filter Effects},{1, 0},{1, 0},{1, 0},{2, 11},{28, Apply Filter Effects-Text-FC},{1, 0},{1, 0},{4, None},{2, 11},{11, RPCFilePath},{1, 0},{1, 0},{84, C:\\RevitRender\\Version2015940\\2017\\assetlibrary_base.fbm\\RPCs\\ArchVision_C1_Alex.rpc},{2, 11},{20, AdvancedUIDefinition},{1, 0},{1, 0},{0, },{2, 11},{10, AssetLibID},{1, 0},{1, 0},{36, 4D3F6E72-3F99-4203-98E9-AF80B3C7A7A4},{2, 11},{10, BaseSchema},{1, 0},{1, 0},{9, RPCSchema},{2, 11},{12, ExchangeGUID},{1, 0},{1, 0},{0, },{1, 2},{6, Hidden},{1, 0},{1, 0},{1, 0},{1, 4},{11, RPCCategory},{1, 0},{1, 0},{1, 0},{2, 11},{8, RPCImage},{1, 0},{1, 0},{0, },{1, 4},{13, SchemaVersion},{1, 0},{1, 0},{1, 5},{2, 11},{12, UIDefinition},{1, 0},{1, 0},{0, },{2, 11},{6, UIName},{1, 0},{1, 0},{22, RPC-8-X9C2-NGU9-LXF5-4},{2, 11},{11, VersionGUID},{1, 0},{1, 0},{9, RPCSchema},{2, 11},{9, assettype},{1, 0},{1, 0},{11, RPCGeometry},{2, 11},{11, description},{1, 0},{1, 0},{0, },{2, 11},{9, localname},{1, 0},{1, 0},{3, RPC},{2, 11},{9, localtype},{1, 0},{1, 0},{3, RPC},{1, 4},{8, revision},{1, 0},{1, 0},{1, 1},{2, 11},{9, thumbnail},{1, 0},{1, 0},{0, },{1, 4},{7, version},{1, 0},{1, 0},{1, 1},{1, 2},{20, RPC_Cast Reflections},{1, 0},{1, 0},{1, 1},{1, 2},{10, RPC_Jitter},{1, 0},{1, 0},{1, 1},{1, 2},{13, RPC_Billboard},{1, 0},{1, 0},{1, 0},{1, 2},{16, RPC_Cast Shadows},{1, 0},{1, 0},{1, 1},{1, 2},{24, RPC_Apply Filter Effects},{1, 0},{1, 0},{1, 0},{2, 11},{32, RPC_Apply Filter Effects-Text-FC},{1, 0},{1, 0},{4, None},{21, assetlibrary_base.fbx},{1, 5},"
                  },
                  "Phasing": {
                      "Phase Demolished": "None",
                      "Phase Created": "Working Drawings"
                  },
                  "Constraints": {
                      "Moves With Nearby Elements": "No",
                      "Offset from Host": "-150.000 mm",
                      "Host": "Level : Ceiling",
                      "Level": "Ceiling"
                  },
                  "Dimensions": {
                      "Height": "0.000 mm"
                  }
              }
          },
          {

              "...truncated for clarity":""

          },
          {
              "objectid": 4268,
              "name": "Floor",
              "externalId": "Floor:Floors",
              "properties": {}
          },
          {
              "objectid": 91,
              "name": "Floors",
              "externalId": "Floors:",
              "properties": {}
          },
          {
              "objectid": 1,
              "name": "Model",
              "externalId": "doc",
              "properties": {
                  "Route Analysis": {
                      "Route Analysis Settings": ""
                  },
                  "Energy Analysis": {
                      "Energy Settings": ""
                  },
                  "Other": {
                      "Project Number": "001-00",
                      "Project Name": "Sample House",
                      "Project Address": "Enter address here",
                      "Client Name": "Autodesk",
                      "Project Status": "Project Status",
                      "Project Issue Date": "Issue Date"
                  },
                  "Identity Data": {
                      "Author": "Samuel Macalister",
                      "Building Name": "Samuel Macalister sample house design",
                      "Organization Description": "",
                      "Organization Name": "Autodesk"
                  }
              }
          }
      ]
  }
}

```

Show More

## [Step 6 - Retrieve specific properties of specific objects in a Viewable](#step-6-retrieve-specific-properties-of-specific-objects-in-a-viewable)

The number of objects and their properties can be very large. The request in Step 5 would have resulted in more than 30,000 lines, had the response not been truncated. Such responses can take time and consume much bandwidth. Alternatively, you can query the objects you are interested in and request only the properties you need. The following request retrieves all objects whose names begin with `M_Pile-Steel`, and retrieves all properties that are categorized as `Dimensions`. The results are paginated, and the response shows page 2 of a page that can contain no more than 5 objects.

### Request

```
curl  -X POST \
      'https://developer.api.autodesk.com/modelderivative/v2/designdata/<URL_SAFE_URN_OF_SOURCE_FILE>/metadata/<GUID_OF_VIEWABLE>/properties:query' \
      -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
      -H 'Content-Type: application/json' \
      -d '{
              "query": {
                  "$prefix": [
                      "name",
                      "M_Pile-Steel"
                  ]
              },
              "fields": [
                  "objectid",
                  "name",
                  "externalId",
                  "properties.Dimensions"
              ],
              "pagination": {
                  "offset": 5,
                  "limit": 5
              },
              "payload": "text"
          }'

```

Show More

### Response

```
{
    "pagination": {
        "limit": 5,
        "offset": 5,
        "totalResults": 11
    },
    "data": {
        "type": "properties",
        "collection": [
            {
                "objectid": 577,
                "name": "M_Pile-Steel Pipe",
                "externalId": "656284ae-d84a-4c5c-ae16-d638fa151c7e-0007d1bf",
                "properties": {
                    "Dimensions": {
                        "Elevation at Bottom": "-7102.000 mm",
                        "Elevation at Top": "-950.000 mm",
                        "Depth": "6000.000 mm",
                        "Diameter": "300.000 mm",
                        "Minimum Embedment": "152.000 mm",
                        "Radius": "150.000 mm"
                    }
                }
            },
            {
                "objectid": 579,
                "name": "M_Pile-Steel Pipe",
                "externalId": "656284ae-d84a-4c5c-ae16-d638fa151c7e-0007d1c3",
                "properties": {
                    "Dimensions": {
                        "Elevation at Bottom": "-7102.000 mm",
                        "Elevation at Top": "-950.000 mm",
                        "Depth": "6000.000 mm",
                        "Diameter": "300.000 mm",
                        "Minimum Embedment": "152.000 mm",
                        "Radius": "150.000 mm"
                    }
                }
            },
            {
                "objectid": 581,
                "name": "M_Pile-Steel Pipe",
                "externalId": "656284ae-d84a-4c5c-ae16-d638fa151c7e-0007d1d7",
                "properties": {
                    "Dimensions": {
                        "Elevation at Bottom": "-7102.000 mm",
                        "Elevation at Top": "-950.000 mm",
                        "Depth": "6000.000 mm",
                        "Diameter": "300.000 mm",
                        "Minimum Embedment": "152.000 mm",
                        "Radius": "150.000 mm"
                    }
                }
            },
            {
                "objectid": 583,
                "name": "M_Pile-Steel Pipe",
                "externalId": "656284ae-d84a-4c5c-ae16-d638fa151c7e-0007d1db",
                "properties": {
                    "Dimensions": {
                        "Elevation at Bottom": "-7102.000 mm",
                        "Elevation at Top": "-950.000 mm",
                        "Depth": "6000.000 mm",
                        "Diameter": "300.000 mm",
                        "Minimum Embedment": "152.000 mm",
                        "Radius": "150.000 mm"
                    }
                }
            },
            {
                "objectid": 585,
                "name": "M_Pile-Steel Pipe",
                "externalId": "656284ae-d84a-4c5c-ae16-d638fa151c7e-0007d20c",
                "properties": {
                    "Dimensions": {
                        "Elevation at Bottom": "-7102.000 mm",
                        "Elevation at Top": "-950.000 mm",
                        "Depth": "6000.000 mm",
                        "Diameter": "300.000 mm",
                        "Minimum Embedment": "152.000 mm",
                        "Radius": "150.000 mm"
                    }
                }
            }
        ]
    }
}

```

Show More
