# Task 4 – Extract Metadata

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/xtract-geometry-from-source-file/task4-extract_metadata/

---

# Task 4 – Extract Metadata

To extract geometry, you must know the object IDs of the geometries to extract. To get the object ID of geometry you must first get the metadata GUID of the Viewable it resides on.

By the end of this task you will be able to:

- Get a list of Viewables contained within a model.
- Retrieve the properties of objects that reside within the Viewable.

You will use the following operations in this task:

| Operation | HTTP Request |
| --- | --- |
| [List Model Views](../http-docs/http-urn-metadata-GET.md) | GET /{urn}/metadata |
| [Fetch All Properties](../http-docs/http-urn-metadata-guid-properties-GET.md) | GET /{urn}/metadata/{modelGuid}/properties |

## [Step 1 - Retrieve a list of Viewables](#step-1-retrieve-a-list-of-viewables)

Once the source file has been translated to SVF2, you can retrieve a list of model view (metadata) IDs contained within the source file.

Note: Although the Inventor model used in this walkthrough contains only a single model view, Revit models contain multiple model views.

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
                "name": "Scene",
                "role": "3d",
                "guid": "b5664c2a-5c6c-4c04-bf07-3474278a9df3"
            }
        ]
    }
}

```

Show More

Note down the value of `guid` of the Viewable. In the next step, you use this value to retrieve the properties of the objects in the Viewable.

## [Step 2 - Retrieve the object tree of the Viewable](#step-2-retrieve-the-object-tree-of-the-viewable)

The object tree is a hierarchical list of objects/geometries contained within the Viewable.

Note the URI parameters `<URL_SAFE_URN_OF_SOURCE_FILE>` and `<GUID_OF_VIEWABLE>`. Replace them with the URL safe URN of the source file, and the `guid` value you noted down in the previous step.

### Request

```
curl  -X GET \
      'https://developer.api.autodesk.com/modelderivative/v2/designdata/<URL_SAFE_URN_OF_SOURCE_FILE>/metadata/<GUID_OF_VIEWABLE>/properties' \
      -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

```

Once you submit the request, the Model Derivative service starts extracting the object properties. If extracting properties takes time, the Model Derivative service sends you the following response. It implies that the request was accepted, but processing is still in progress. If you receive such a result, submit the request again.

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
            "name": "Stapler",
            "objects": [
               {
                  "objectid": 2,
                  "name": "Stapler",
                  "objects": [
                     {
                        "objectid": 3,
                        "name": "Bottom:1",
                        "objects": [
                           {
                              "objectid": 4,
                              "name": "Bottom - Back:1",
                              "objects": [
                                 {
                                    "objectid": 5,
                                    "name": "Solid1"
                                 }
                              ]
                           },
                           {
                              "objectid": 6,
                              "name": "Bottom - Front:1",
                              "objects": [
                                 {
                                    "objectid": 7,
                                    "name": "Solid1"
                                 }
                              ]
                           },
                           {
                              "objectid": 8,
                              "name": "Lower Mount:1",
                              "objects": [
                                 {
                                    "objectid": 9,
                                    "name": "Solid1"
                                 }
                              ]
                           },
                           {
                              "objectid": 10,
                              "name": "Spring:1",
                              "objects": [
                                 {
                                    "objectid": 11,
                                    "name": "Solid1"
                                 }
                              ]
                           },
                           {
                              "objectid": 12,
                              "name": "Bottom - Anvil:1",
                              "objects": [
                                 {
                                    "objectid": 13,
                                    "name": "Solid1"
                                 }
                              ]
                           }
                        ]
                     },
                     {
                        "objectid": 14,
                        "name": "Upper:1",
                        "objects": [
                           {
                              "objectid": 15,
                              "name": "Upper - Back:1",
                              "objects": [
                                 {
                                    "objectid": 16,
                                    "name": "Solid1"
                                 }
                              ]
                           },
                           {
                              "objectid": 17,
                              "name": "Upper - Front:1",
                              "objects": [
                                 {
                                    "objectid": 18,
                                    "name": "Solid1"
                                 }
                              ]
                           },
                           {
                              "objectid": 19,
                              "name": "Channel - Spring Clip:1",
                              "objects": [
                                 {
                                    "objectid": 20,
                                    "name": "Solid1"
                                 }
                              ]
                           },
                           {
                              "objectid": 21,
                              "name": "Channel:1",
                              "objects": [
                                 {
                                    "objectid": 22,
                                    "name": "Channel - Base:1",
                                    "objects": [
                                       {
                                          "objectid": 23,
                                          "name": "Solid1"
                                       }
                                    ]
                                 },
                                 {
                                    "objectid": 24,
                                    "name": "Channel - Pusher:1",
                                    "objects": [
                                       {
                                          "objectid": 25,
                                          "name": "Solid1"
                                       }
                                    ]
                                 },
                                 {
                                    "objectid": 26,
                                    "name": "Channel - Cover:1",
                                    "objects": [
                                       {
                                          "objectid": 27,
                                          "name": "Solid1"
                                       }
                                    ]
                                 },
                                 {
                                    "objectid": 28,
                                    "name": "Channel - Hinge Pin:1",
                                    "objects": [
                                       {
                                          "objectid": 29,
                                          "name": "Solid1"
                                       }
                                    ]
                                 },
                                 {
                                    "objectid": 30,
                                    "name": "Staples:1",
                                    "objects": [
                                       {
                                          "objectid": 31,
                                          "name": "Solid1"
                                       }
                                    ]
                                 },
                                 {
                                    "objectid": 32,
                                    "name": "Channel - Bumper:1",
                                    "objects": [
                                       {
                                          "objectid": 33,
                                          "name": "Solid1"
                                       }
                                    ]
                                 }
                              ]
                           }
                        ]
                     }
                  ]
               }
            ]
         }
      ]
   }
}

```

Show More
