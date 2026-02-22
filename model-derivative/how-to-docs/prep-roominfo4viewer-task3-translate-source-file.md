# Task 3 â Translate to SVF2

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/prep-roominfo4viewer/task3-translate-source-file/

---

# Task 3 â Translate to SVF2

SVF2 is a newer format designed specifically for larger models with geometry repetition. When larger and complex models are translated to SVF2, they load much faster in the viewer. For details see [Displaying Models in a Browser](/en/docs/model-derivative/v2/developers_guide/basics/preperation/) in the Developerâs Guide.

## [Step 1 - Start a translation job](#step-1-start-a-translation-job)

When you start a translation job, you specify the Base64-encoded URN of the source file. You also specify the translated file format you require, which is SVF2 in this case. You can optionally specify the region the translation must be stored. Also, take note of the following:

- The header parameter `x-ads-force` is set to `true`. Setting this header parameter removes the derivatives produced by previous translation jobs for this source file, which is mandatory for generating master views.

- The body parameter `advanced` > `generateMasterViews` is set to true. Setting this parameter generates an extra Viewable for each phase. They contain all elements (including âroomâ elements) present in the host model for that phase. If this parameter is not specified, master views are not translated, because they are not part of the 3D view.

    **Note:** By specifying this option, translation time increases.

### Request

```
curl  -X POST \
      'https://developer.api.autodesk.com/modelderivative/v2/designdata/job' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
      -H 'x-ads-force: true' \
      -d '{
          "input": {
              "urn": "<BASE64_ENCODED_URN_OF_SOURCE_FILE>",
          },
          "output": {
              "formats": [
                  {
                      "type": "svf2",
                      "views": [
                          "2d",
                          "3d"
                      ],
                     "advanced": {
                       "generateMasterViews": true
                     }
                  }
              ]
          }
      }'

```

Show More

### Response

```
{
  "result": "success",
  "urn": "<URL_SAFE_URN_OF_SOURCE_FILE>",
  "acceptedJobs": {
      "output": {
          "destination": {
              "region": "us"
          },
          "formats": [
              {
                  "type": "svf2",
                  "views": [
                      "2d",
                      "3d"
                  ],
                  "advanced": {
                      "generateMasterViews": true
                  }
              }
          ]
      }
  }
}

```

Show More

Note down the value of `urn`. This is the URL safe Base64-encoded URN of the source file. It is this URN you use to check the status of the translation job.

## [Step 2 - Check the Status of the translation job](#step-2-check-the-status-of-the-translation-job)

To check the status of the translation job, you must look at the manifest produced by the translation job. The `status` attribute in the manifest reports the status of the translation job. The status can be:

- `pending`: The job has been received and is pending for processing.
- `inprogress`: The job has started processing, and is running.
- `success`: The job has finished successfully.
- `failed`: The translation has failed.
- `timeout`: The translation has timed out and no output is generated.

### Request

```
curl  -X GET \
      'https://developer.api.autodesk.com/modelderivative/v2/designdata/<URL_SAFE_URN_OF_SOURCE_FILE>/manifest' \
      -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

```

The Revit file ârme_advanced_sample_project.rvtâ contains a phase named `` `New Construction ``. In the response, the manifest will shows the phase as a Viewable named `New Construction` (highlighted on lines 101-178). This Viewable would not be there in the manifest if you had not specified the `generateMaterViews` option. Viewables generated from master views typically have the same name as the phase they are generated from. If a Viewable with that name already exists, the server adds a suffix to the default name.

### Response

```
{
    "urn": "<URL_SAFE_URN_OF_SOURCE_FILE>",
    "derivatives": [
        {
            "hasThumbnail": "true",
            "children": [
                {
                    "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/model.sdb",
                    "role": "Autodesk.CloudPlatform.PropertyDatabase",
                    "mime": "application/autodesk-db",
                    "guid": "6fac95cb-af5d-3e4f-b943-8a7f55847ff1",
                    "type": "resource",
                    "status": "success"
                },
                {
                    "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/AECModelData.json",
                    "role": "Autodesk.AEC.ModelData",
                    "mime": "application/json",
                    "guid": "a4aac952-a3f4-031c-4113-b2d9ac2d0de6",
                    "type": "resource",
                    "status": "success"
                },
                {
                    "phaseNames": "New Construction",
                    "role": "3d",
                    "hasThumbnail": "true",
                    "children": [
                        {
                            "guid": "92b5dec7-790a-45b0-a5e8-cd9f76058c3a-000f9130",
                            "type": "view",
                            "role": "3d",
                            "name": "3D",
                            "status": "success",
                            "progress": "complete",
                            "camera": [
                                271.4864501953125,
                                -152.76095581054688,
                                229.5323486328125,
                                59.09648132324219,
                                59.629005432128906,
                                17.14238739013672,
                                -0.40824830532073975,
                                0.40824830532073975,
                                0.8164966106414795,
                                1.349758267402649,
                                0,
                                1,
                                1
                            ]
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/3D View/3D/3D1.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "c70aa596-d404-714f-6795-9276087c3800",
                            "type": "resource",
                            "resolution": [
                                100,
                                100
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/3D View/3D/3D2.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "6ef65d1a-4a59-111d-f1ec-4e543bd2712b",
                            "type": "resource",
                            "resolution": [
                                200,
                                200
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/3D View/3D/3D4.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "2c06739e-5164-4f6d-450e-c8833fd2a2ba",
                            "type": "resource",
                            "resolution": [
                                400,
                                400
                            ],
                            "status": "success"
                        },
                        {
                            "role": "graphics",
                            "mime": "application/autodesk-svf2",
                            "guid": "4a12d1bd-ae77-bfa8-406a-5fbbad0f377c",
                            "type": "resource"
                        }
                    ],
                    "name": "3D",
                    "guid": "a0899700-5b18-9636-c2c8-c0c1adb78391",
                    "progress": "complete",
                    "type": "geometry",
                    "viewableID": "92b5dec7-790a-45b0-a5e8-cd9f76058c3a-000f9130",
                    "status": "success"
                },
                {
                    "phaseNames": "New Construction",
                    "role": "3d",
                    "hasThumbnail": "true",
                    "children": [
                        {
                            "guid": "c884ae1b-61e7-4f9d-0001-719e20b22d0b-000f9147",
                            "type": "view",
                            "role": "3d",
                            "name": "New Construction",
                            "status": "success",
                            "progress": "complete",
                            "camera": [
                                261.3863830566406,
                                -159.7818603515625,
                                223.129150390625,
                                55.39960479736328,
                                46.20491027832031,
                                17.14238739013672,
                                -0.40824830532073975,
                                0.40824830532073975,
                                0.8164966106414795,
                                1.3234660625457764,
                                0,
                                1,
                                1
                            ]
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/3D View/08f99ae5-b8be-4f8d-881b-128675723c10/New Construction/New Construction1.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "a3c19573-8948-7ae0-fb5c-75cab1d0e87a",
                            "type": "resource",
                            "resolution": [
                                100,
                                100
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/3D View/08f99ae5-b8be-4f8d-881b-128675723c10/New Construction/New Construction2.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "86d53dd2-82c8-1948-5997-00ebf6078ed7",
                            "type": "resource",
                            "resolution": [
                                200,
                                200
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/3D View/08f99ae5-b8be-4f8d-881b-128675723c10/New Construction/New Construction4.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "7e36c074-8997-d941-4dc3-6a72fcdf3b9b",
                            "type": "resource",
                            "resolution": [
                                400,
                                400
                            ],
                            "status": "success"
                        },
                        {
                            "role": "graphics",
                            "mime": "application/autodesk-svf2",
                            "guid": "b3a8a97b-d4c6-8000-9a35-9af7920042d6",
                            "type": "resource"
                        }
                    ],
                    "name": "New Construction",
                    "guid": "457a8958-790b-6dae-1127-0a57ee517344",
                    "progress": "complete",
                    "type": "geometry",
                    "viewableID": "c884ae1b-61e7-4f9d-0001-719e20b22d0b-000f9147",
                    "status": "success"
                },
                {
                    "guid": "f2e74d59-4f85-42bf-a9d8-0f0d6bbc4271-000842af",
                    "type": "geometry",
                    "role": "2d",
                    "name": "E601 - Panel Schedules",
                    "viewableID": "f2e74d59-4f85-42bf-a9d8-0f0d6bbc4271-000842af",
                    "status": "success",
                    "progress": "complete",
                    "properties": {
                        "Print Setting": {
                            "Layout": "Landscape",
                            "Paper size": "ISO A4, 210 x 297 mm"
                        }
                    },
                    "hasThumbnail": "true",
                    "children": [
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/E601 - Panel Schedules 541359/dwfx/E601 - Panel Schedules1.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "2b80b173-5aeb-4443-7f95-8b67188ea9eb",
                            "type": "resource",
                            "resolution": [
                                100,
                                100
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/E601 - Panel Schedules 541359/dwfx/E601 - Panel Schedules2.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "9b744c77-f34c-53ab-1e67-09ed095c75fd",
                            "type": "resource",
                            "resolution": [
                                200,
                                200
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/E601 - Panel Schedules 541359/dwfx/E601 - Panel Schedules4.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "76c92dac-074f-1a78-2992-391ce317b1f2",
                            "type": "resource",
                            "resolution": [
                                400,
                                400
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/9d884689-7a61-ec15-c701-cb65f1702ea1_f2d/primaryGraphics.f2d",
                            "role": "graphics",
                            "mime": "application/autodesk-f2d",
                            "guid": "eab02849-b3cf-456d-5964-6b20198d2c59",
                            "type": "resource",
                            "status": "success"
                        },
                        {
                            "guid": "ba651921-141f-4978-8866-18148547a97a",
                            "type": "view",
                            "role": "2d",
                            "name": "Sheet: E601 - Panel Schedules",
                            "viewbox": [
                                0,
                                -0.003848,
                                1187.999999,
                                840.003849
                            ]
                        }
                    ]
                },
                {
                    "guid": "7a2419bd-e042-4b38-8b95-781bc33e7dd8-000842cd",
                    "type": "geometry",
                    "role": "2d",
                    "name": "E301 - North Level 1 - Lighting Plan",
                    "viewableID": "7a2419bd-e042-4b38-8b95-781bc33e7dd8-000842cd",
                    "phaseNames": "New Construction",
                    "status": "success",
                    "progress": "complete",
                    "properties": {
                        "Print Setting": {
                            "Layout": "Landscape",
                            "Paper size": "ISO A4, 210 x 297 mm"
                        }
                    },
                    "hasThumbnail": "true",
                    "children": [
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/E301 - North Level 1 - Lighting Plan 541389/dwfx/E301 - North Level 1 - Lighting Plan1.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "985caf33-b88e-cf8a-e86e-dcfe4906c665",
                            "type": "resource",
                            "resolution": [
                                100,
                                100
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/E301 - North Level 1 - Lighting Plan 541389/dwfx/E301 - North Level 1 - Lighting Plan2.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "a665b085-7eec-f9e5-75f8-02280cb43377",
                            "type": "resource",
                            "resolution": [
                                200,
                                200
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/E301 - North Level 1 - Lighting Plan 541389/dwfx/E301 - North Level 1 - Lighting Plan4.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "cf168620-3a4b-96f8-7423-e9c6479ad21b",
                            "type": "resource",
                            "resolution": [
                                400,
                                400
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/6a5b6c9d-fa68-f1fd-b132-f02ee08ae842_f2d/primaryGraphics.f2d",
                            "role": "graphics",
                            "mime": "application/autodesk-f2d",
                            "guid": "2c7bf6f6-e220-b96f-4f8f-1341104e901e",
                            "type": "resource",
                            "status": "success"
                        },
                        {
                            "guid": "94353a0c-7aad-465d-8ff6-990546aad6c1",
                            "type": "view",
                            "role": "2d",
                            "name": "Sheet: E301 - North Level 1 - Lighting Plan",
                            "viewbox": [
                                0,
                                -0.003848,
                                1187.999999,
                                840.003849
                            ]
                        }
                    ]
                },
                {
                    "guid": "7a2419bd-e042-4b38-8b95-781bc33e7dd8-000854ac",
                    "type": "geometry",
                    "role": "2d",
                    "name": "M601 - Duct Sections",
                    "viewableID": "7a2419bd-e042-4b38-8b95-781bc33e7dd8-000854ac",
                    "phaseNames": "New Construction",
                    "status": "success",
                    "progress": "complete",
                    "properties": {
                        "Print Setting": {
                            "Layout": "Landscape",
                            "Paper size": "ISO A4, 210 x 297 mm"
                        }
                    },
                    "hasThumbnail": "true",
                    "children": [
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/M601 - Duct Sections 545964/dwfx/M601 - Duct Sections1.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "03ac6cf4-15df-1c94-78f4-dca7bf7f9738",
                            "type": "resource",
                            "resolution": [
                                100,
                                100
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/M601 - Duct Sections 545964/dwfx/M601 - Duct Sections2.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "93c4c6e1-dff6-2169-6e2e-a5f767f33d12",
                            "type": "resource",
                            "resolution": [
                                200,
                                200
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/M601 - Duct Sections 545964/dwfx/M601 - Duct Sections4.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "64860052-be20-b162-8852-7438c02114e2",
                            "type": "resource",
                            "resolution": [
                                400,
                                400
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/cdab39dc-dbad-4950-0c54-eeb7f8927f57_f2d/primaryGraphics.f2d",
                            "role": "graphics",
                            "mime": "application/autodesk-f2d",
                            "guid": "c51a5b2d-59c3-7c49-6b92-44b96ed06336",
                            "type": "resource",
                            "status": "success"
                        },
                        {
                            "guid": "4050ea1e-df8c-44d5-9655-e2d474fc9298",
                            "type": "view",
                            "role": "2d",
                            "name": "Sheet: M601 - Duct Sections",
                            "viewbox": [
                                0,
                                -0.003848,
                                1187.999999,
                                840.003849
                            ]
                        }
                    ]
                },
                {
                    "guid": "7a2419bd-e042-4b38-8b95-781bc33e7dd8-000854c7",
                    "type": "geometry",
                    "role": "2d",
                    "name": "M701 - Mechanical Schedules",
                    "viewableID": "7a2419bd-e042-4b38-8b95-781bc33e7dd8-000854c7",
                    "status": "success",
                    "progress": "complete",
                    "properties": {
                        "Print Setting": {
                            "Layout": "Landscape",
                            "Paper size": "ISO A4, 210 x 297 mm"
                        }
                    },
                    "hasThumbnail": "true",
                    "children": [
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/M701 - Mechanical Schedules 545991/dwfx/M701 - Mechanical Schedules1.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "1396ebd3-be1c-6ada-d233-794ddc71a3d0",
                            "type": "resource",
                            "resolution": [
                                100,
                                100
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/M701 - Mechanical Schedules 545991/dwfx/M701 - Mechanical Schedules2.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "dbfce7ce-800a-1ee1-f18b-f04b020fb887",
                            "type": "resource",
                            "resolution": [
                                200,
                                200
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/M701 - Mechanical Schedules 545991/dwfx/M701 - Mechanical Schedules4.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "70d954bd-dd19-5153-d7eb-cbb56154e855",
                            "type": "resource",
                            "resolution": [
                                400,
                                400
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/0297f9a2-7e21-f147-8507-e35f526459fd_f2d/primaryGraphics.f2d",
                            "role": "graphics",
                            "mime": "application/autodesk-f2d",
                            "guid": "8d2fbd31-d9f0-9de3-3c26-114e906d066e",
                            "type": "resource",
                            "status": "success"
                        },
                        {
                            "guid": "7ba739f8-c310-4c6a-b256-7625db4559a1",
                            "type": "view",
                            "role": "2d",
                            "name": "Sheet: M701 - Mechanical Schedules",
                            "viewbox": [
                                0,
                                -0.003848,
                                1187.999999,
                                840.003849
                            ]
                        }
                    ]
                },
                {
                    "guid": "1513bf56-b281-46fc-917c-711a0e9748e6-0008e95a",
                    "type": "geometry",
                    "role": "2d",
                    "name": "E201 - Unnamed",
                    "viewableID": "1513bf56-b281-46fc-917c-711a0e9748e6-0008e95a",
                    "phaseNames": "New Construction",
                    "status": "success",
                    "progress": "complete",
                    "properties": {
                        "Print Setting": {
                            "Layout": "Landscape",
                            "Paper size": "ISO A4, 210 x 297 mm"
                        }
                    },
                    "hasThumbnail": "true",
                    "children": [
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/E201 - Unnamed 584026/dwfx/E201 - Unnamed1.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "70f36c34-69d3-6e3b-5e5d-ff68a73b1bca",
                            "type": "resource",
                            "resolution": [
                                100,
                                100
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/E201 - Unnamed 584026/dwfx/E201 - Unnamed2.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "2b4c066e-358c-c01e-3fd9-74027d2d505e",
                            "type": "resource",
                            "resolution": [
                                200,
                                200
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/E201 - Unnamed 584026/dwfx/E201 - Unnamed4.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "12ad23e0-527e-0edf-f8a0-f76262e9f987",
                            "type": "resource",
                            "resolution": [
                                400,
                                400
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/04fec3ac-7ed9-f5d0-7bf1-650aace683cf_f2d/primaryGraphics.f2d",
                            "role": "graphics",
                            "mime": "application/autodesk-f2d",
                            "guid": "ec1cbd2e-7281-5622-79b8-af582bffb8a3",
                            "type": "resource",
                            "status": "success"
                        },
                        {
                            "guid": "846f95d5-a2e5-4a77-8b1c-df33bfcceb5a",
                            "type": "view",
                            "role": "2d",
                            "name": "Sheet: E201 - Unnamed",
                            "viewbox": [
                                0,
                                -0.003848,
                                1187.999999,
                                840.003849
                            ]
                        }
                    ]
                },
                {
                    "guid": "30a3bbb8-9fd7-4526-8fb5-b921e7dd1c83-00096d16",
                    "type": "geometry",
                    "role": "2d",
                    "name": "M100 - MECHANICAL LEGEND",
                    "viewableID": "30a3bbb8-9fd7-4526-8fb5-b921e7dd1c83-00096d16",
                    "status": "success",
                    "progress": "complete",
                    "properties": {
                        "Print Setting": {
                            "Layout": "Landscape",
                            "Paper size": "ISO A4, 210 x 297 mm"
                        }
                    },
                    "hasThumbnail": "true",
                    "children": [
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/M100 - MECHANICAL LEGEND 617750/dwfx/M100 - MECHANICAL LEGEND1.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "1ef58164-e462-12d3-76b7-0b0550b04685",
                            "type": "resource",
                            "resolution": [
                                100,
                                100
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/M100 - MECHANICAL LEGEND 617750/dwfx/M100 - MECHANICAL LEGEND2.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "0d01338b-3ab5-aaf2-4164-ba88a8529342",
                            "type": "resource",
                            "resolution": [
                                200,
                                200
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/M100 - MECHANICAL LEGEND 617750/dwfx/M100 - MECHANICAL LEGEND4.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "eeea1f63-1129-3ccf-1845-174a089a333b",
                            "type": "resource",
                            "resolution": [
                                400,
                                400
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/63ebfacb-dc24-b291-b484-a43ddd580eb2_f2d/primaryGraphics.f2d",
                            "role": "graphics",
                            "mime": "application/autodesk-f2d",
                            "guid": "81211152-eebf-e5b6-25f8-db473d70d57e",
                            "type": "resource",
                            "status": "success"
                        },
                        {
                            "guid": "f16a79a9-00a5-4e38-a3ac-a3fcd8c85ef3",
                            "type": "view",
                            "role": "2d",
                            "name": "Sheet: M100 - MECHANICAL LEGEND",
                            "viewbox": [
                                0,
                                -0.003848,
                                1187.999999,
                                840.003849
                            ]
                        }
                    ]
                },
                {
                    "guid": "4aded12f-bb3e-43d3-a764-654a0a8454e4-000987a6",
                    "type": "geometry",
                    "role": "2d",
                    "name": "E101 - Electrical Power Riser Diagram",
                    "viewableID": "4aded12f-bb3e-43d3-a764-654a0a8454e4-000987a6",
                    "phaseNames": "New Construction",
                    "status": "success",
                    "progress": "complete",
                    "properties": {
                        "Print Setting": {
                            "Layout": "Landscape",
                            "Paper size": "ISO A4, 210 x 297 mm"
                        }
                    },
                    "hasThumbnail": "true",
                    "children": [
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/E101 - Electrical Power Riser Diagram 624550/dwfx/E101 - Electrical Power Riser Diagram1.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "507d195d-e256-8de0-3e83-f5be5243f559",
                            "type": "resource",
                            "resolution": [
                                100,
                                100
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/E101 - Electrical Power Riser Diagram 624550/dwfx/E101 - Electrical Power Riser Diagram2.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "e88c283b-556c-aa1a-d7b1-319e4e9b56ab",
                            "type": "resource",
                            "resolution": [
                                200,
                                200
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/Resource/Sheet/E101 - Electrical Power Riser Diagram 624550/dwfx/E101 - Electrical Power Riser Diagram4.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "b0de6dfe-96cb-83ea-66f6-3826f6f690fa",
                            "type": "resource",
                            "resolution": [
                                400,
                                400
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/7dc1b479-4b5d-2f81-ad16-de65f26ad223_f2d/primaryGraphics.f2d",
                            "role": "graphics",
                            "mime": "application/autodesk-f2d",
                            "guid": "16553508-76ce-ce3d-fc20-db62a6415c27",
                            "type": "resource",
                            "status": "success"
                        },
                        {
                            "guid": "927690bb-93c2-4898-b36b-334d89a9efcb",
                            "type": "view",
                            "role": "2d",
                            "name": "Sheet: E101 - Electrical Power Riser Diagram",
                            "viewbox": [
                                0,
                                -0.003848,
                                1187.999999,
                                840.003849
                            ]
                        }
                    ]
                }
            ],
            "name": "rme_advanced_sample_project.rvt",
            "progress": "complete",
            "outputType": "svf2",
            "status": "success"
        },
        {
            "children": [
                {
                    "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/preview1.png",
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
                    "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/preview2.png",
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
                    "urn": "urn:adsk.viewing:fs.file:<URL_SAFE_URN_OF_SOURCE_FILE>/output/preview4.png",
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

Note down the value of the `urn` parameter on lighted, which is highlighted above. This value is the URL safe Base64-encoded of the source file. In the next task, you insert this value in the JavaScript code handling the viewer.
