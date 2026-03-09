# Extract the Inventory for a Takeoff Project

Source: https://aps.autodesk.com/en/docs/acc/tutorials/takeoff/takeoff-extract-inventory/

---

# Extract the Inventory for a Takeoff Project

This tutorial demonstrates how to extract the inventory items for a takeoff project. This will include:

- Retrieving all the packages
- Retrieving all the takeoff types
- Retrieving all the takeoff items

To learn more about the inventory tool, see the [ACC Takeoff Inventory](https://help.autodesk.com/view/TAKEOFF/ENU/?guid=Inventory) help documentation.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps), and select Autodesk Construction Cloud API.
- Provision your app to acquire access to your ACC account.
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with the `data:read` scope.
- Verify that you have access to the relevant ACC project.

## [Step 1: Retrieve the Packages](#step-1-retrieve-the-packages)

Use the project ID (`7388a640-3bff-4328-9dc2-aafe62359958`) to retrieve the packages, by calling [GET packages](../http-docs/http-takeoff-projects-project_id-packages-GET.md).

To find the project ID, see the [Retrieve ACC Account and project ID](getting-started-retrieve-account-and-project-id.md) tutorial.

### Request

```
curl -X GET \
  "https://developer.api.autodesk.com/construction/takeoff/v1/projects/7388a640-3bff-4328-9dc2-aafe62359958/packages" \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json"

```

### Response

```
{
  "pagination": {
    "offset": 0,
    "limit": 200
  },
  "results": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "Concrete",
      "createdAt": "2019-08-24T14:15:22Z",
      "updatedAt": "2020-11-11T12:32:45Z",
      "updatedByName": "Jane Johnson"
    }
  ]
}

```

Show More

The response payload includes the package IDs (`results[i].id`).

## [Step 2: Retrieve all Takeoff Types and Items](#step-2-retrieve-all-takeoff-types-and-items)

### Part A: Get all the Takeoff Types

Use the project ID (`7388a640-3bff-4328-9dc2-aafe62359958`) and package ID (`6e330582-ad88-4299-85e6-b749e8dec40d`) from the previous step to retrieve the takeoff types, by calling [GET takeoff-types](../http-docs/http-takeoff-projects-project_id-packages-package_id-takeoff-types-GET.md).

### Request

```
curl -X GET \
  "https://developer.api.autodesk.com/construction/takeoff/v1/projects/7388a640-3bff-4328-9dc2-aafe62359958/packages/6e330582-ad88-4299-85e6-b749e8dec40d/takeoff-types" \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json"

```

### Response

```
{
  "pagination": {
    "offset": 0,
    "limit": 1000
  },
  "results": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "Foundation Slab",
      "description": "Slab in the garage",
      "color": "#11ff11",
      "borderColor": "#11ff11",
      "shapeType": "SQUARE",
      "countMarkerSize": 1.5,
      "tool": "DISTANCE",
      "propertyDefinitions": [
        {
          "name": "Height",
          "unitOfMeasure": "LF",
          "value": 2.5,
          "valueLocation": "INSTANCE_WITH_TAKEOFF_TYPE_DEFAULT"
        },
        {
          "name": "Width",
          "unitOfMeasure": "LF",
          "value": 1,
          "valueLocation": "INSTANCE_WITH_TAKEOFF_TYPE_DEFAULT"
        }
      ],
      "modelMappings": [
        {
          "name": "Area",
          "mappingExpression": "Sill_Height*Width"
        }
      ],
      "primaryQuantityDefinition": {
        "classificationCodeOne": "037000",
        "classificationCodeTwo": "044000",
        "outputName": "Exterior Wall",
        "expression": "Distance*Width*Height*1.1",
        "unitOfMeasure": "CY"
      },
      "secondaryQuantityDefinitions": [
        {
          "classificationCodeOne": "CustomAreaCode1",
          "classificationCodeTwo": "CustomAreaCode2",
          "outputName": "Custom Flooring",
          "expression": "Distance*Width",
          "unitOfMeasure": "SF"
        }
      ],
      "createdAt": "2019-08-24T14:15:22Z",
      "updatedAt": "2020-11-11T12:32:45Z",
      "updatedByName": "Jane Johnson"
    }
  ]
}

```

Show More

### Part B: Get all the Takeoff Items

Use the project ID (`7388a640-3bff-4328-9dc2-aafe62359958`) and package ID (`6e330582-ad88-4299-85e6-b749e8dec40d`) from the previous step to retrieve the takeoff items, by calling [GET takeoff-items](../http-docs/http-takeoff-projects-project_id-packages-package_id-takeoff-items-GET.md).

### Request

```
curl -X GET \
  "https://developer.api.autodesk.com/construction/takeoff/v1/projects/7388a640-3bff-4328-9dc2-aafe62359958/packages/6e330582-ad88-4299-85e6-b749e8dec40d/takeoff-items" \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json"

```

### Response

```
{
  "pagination": {
    "offset": 0,
    "limit": 1000
  },
  "results": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "takeoffTypeId": "b9380176-9ac2-454d-acdd-fdfd988b9702",
      "type": "COUNT",
      "objectName": "36\" x 48\"",
      "geometry": "<path fill=\"none\" stroke=\"red\" d=\"M 10,10 h 10 m 0,10 h 10 m 0,10 h 10\">",
      "objectId": 1,
      "propertyValues": [
        {
          "name": "Perimeter",
          "unitOfMeasure": "LF",
          "source": "MEASUREMENT",
          "value": 3
        }
      ],
      "primaryQuantity": {
        "outputName": "Bedroom Wall",
        "classificationCodeOne": "085113",
        "classificationCodeTwo": "011223",
        "quantity": 15,
        "unitOfMeasure": "EA"
      },
      "secondaryQuantities": [
        {
          "outputName": "Wall Paint",
          "classificationCodeOne": "098732",
          "classificationCodeTwo": "011665",
          "quantity": 45,
          "unitOfMeasure": "LF"
        }
      ],
      "contentView": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "version": "urn:adsk.wipstg:fs.file:vf.oeSywgLpSkONo9O6CUZvkQ?version=3"
      },
      "locationId": "ff7f6eb4-6276-4993-bfeb-34cbbbba3a17",
      "createdAt": "2019-08-24T14:15:22Z",
      "updatedAt": "2020-11-11T12:32:45Z",
      "updatedByName": "Jane Johnson"
    }
  ]
}

```

Show More

## [Retrieve Additional Information (optional)](#retrieve-additional-information-optional)

Below are some examples of how to obtain additional information, relating to a takeoff project, that would allow you to construct an inventory tool, similar to what appears in the UI. For more details, see the [Takeoff Inventory](https://help.autodesk.com/view/TAKEOFF/ENU/?guid=Inventory) help documentation.

## [Get the Classification Systems](#get-the-classification-systems)

Use the project ID (`7388a640-3bff-4328-9dc2-aafe62359958`) to retrieve the classification systems, by calling [GET classification-systems](../http-docs/http-takeoff-projects-project_id-classification-systems-GET.md).

For more details about classification systems, see the [Configure Takeoff Settings](https://help.autodesk.com/view/TAKEOFF/ENU/?guid=Configure_Takeoff_Settings) help documentation.

### Request

```
curl -X GET \
  "https://developer.api.autodesk.com/construction/takeoff/v1/projects/7388a640-3bff-4328-9dc2-aafe62359958/classification-systems" \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json"

```

### Response

```
{
  "pagination": {
    "offset": 0,
    "limit": 200
  },
  "results": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "Smith Construction Classification",
      "type": "CLASSIFICATION_SYSTEM_1"
    }
  ]
}

```

Show More

The response payload includes the classification system IDs (`results[i].id`).

## [Get the Classifications for a Classification System](#get-the-classifications-for-a-classification-system)

Use the project ID (`7388a640-3bff-4328-9dc2-aafe62359958`) and classification system ID (`1a07c80a-3892-40b1-8a2f-3d0b05786d70`) from the previous step to retrieve the classifications, by calling [GET classifications](../http-docs/http-takeoff-projects-project_id-classification-systems-system_id-classifications-GET.md).

### Request

```
curl -X GET \
  "https://developer.api.autodesk.com/construction/takeoff/v1/projects/7388a640-3bff-4328-9dc2-aafe62359958/classification-systems/1a07c80a-3892-40b1-8a2f-3d0b05786d70/classifications" \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json"

```

### Response

```
{
  "pagination": {
    "offset": 0,
    "limit": 10000
  },
  "results": [
    {
      "code": "A1010",
      "parentCode": null,
      "description": "Concrete",
      "measurementType": "AREA"
    },
    {
      "code": "A1010.10",
      "parentCode": "A1010",
      "description": "Sprayed concrete",
      "measurementType": "AREA"
    },
    {
      "code": "A1010.20",
      "parentCode": "A1010",
      "description": "Foamed concrete",
      "measurementType": "AREA"
    }
  ]
}

```

Show More

## [Get Sheet or Model Information](#get-sheet-or-model-information)

Use the project ID (`7388a640-3bff-4328-9dc2-aafe62359958`) to retrieve the content views, by calling [GET content-views](../http-docs/http-takeoff-projects-project_id-content-views-GET.md).

A content view is either a 3D BIM model view, or a 2D PDF sheet that a user could use to create takeoffs.

### Request

```
curl -X GET \
  "https://developer.api.autodesk.com/construction/takeoff/v1/projects/7388a640-3bff-4328-9dc2-aafe62359958/content-views" \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json"

```

### Response

```
{
  "pagination": {
    "offset": 0,
    "limit": 200
  },
  "results": [
    [
      {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "type": "FILE_MODEL",
        "view": {
          "lineageUrn": "urn:adsk.wipqa:dm.lineage:TCBw0V-GQX2aAWWSSrhQmQ",
          "viewName": "3D"
        }
      },
      {
        "id": "95451383-ee38-44da-b06c-2d5266e726d2",
        "type": "SHEET",
        "view": {
          "sheetName": "A09.05",
          "calibration": {
            "scaleFactor": 0.987,
            "units": "FT_AND_FRACTIONAL_IN"
          }
        }
      }
    ]
  ]
}

```

Show More

For sheet names, the name is under `results[i].view.sheetName` where `results[i].type` is `SHEET`.

For model names, use `results[i].view.lineageUrn` where `results[i].type` is `FILE-MODEL`, and continue to the next step.

## [Get the Model Name](#get-the-model-name)

Use the project ID (`7388a640-3bff-4328-9dc2-aafe62359958`) and `lineageUrn` (`urn:adsk.wipprod:dm.lineage:TwJx1922Sq2MsljlLsTYFQ`) to retrieve the model name, by calling [GET project items](../../data/http-docs/http-projects-project_id-items-item_id-tip-GET.md).

### Request

```
curl -X GET \
  "https://developer.api.autodesk.com/data/v1/projects/b.7388a640-3bff-4328-9dc2-aafe62359958/items/urn:adsk.wipprod:dm.lineage:TwJx1922Sq2MsljlLsTYFQ/tip" \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/json"

```

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": {
      "href": "https://developer.api.autodesk.com/data/v1/projects/b.7388a640-3bff-4328-9dc2-aafe62359958/items/urn:adsk.wipprod:dm.lineage:TwJx1922Sq2MsljlLsTYFQ/tip"
    }
  },
  "data": {
    "type": "versions",
    "id": "urn:adsk.wipprod:fs.file:vf.TwJx1922Sq2MsljlLsTYFQ?version=1",
    "attributes": {
      "name": "Revit2018_rac_advanced_sample_project.rvt",
      "displayName": "",
      "createTime": "2021-03-26T13:28:02.0000000Z",
      "createUserId": "",
      "createUserName": "",
      "lastModifiedTime": "2021-03-26T13:29:32.0000000Z",
      "lastModifiedUserId": "",
      "lastModifiedUserName": "",
      "versionNumber": 1,
      "storageSize": 15532032,
      "fileType": "rvt",
      "extension": {
        "type": "versions:autodesk.bim360:File",
        "version": "1.0",
        "schema": {
          "href": "https://developer.api.autodesk.com/schema/v1/versions/versions:autodesk.bim360:File-1.0"
        },
        "data": {
          "processState": "PROCESSING_COMPLETE",
          "extractionState": "SUCCESS",
          "splittingState": "NOT_SPLIT",
          "reviewState": "NOT_IN_REVIEW",
          "revisionDisplayLabel": "1",
          "sourceFileName": "Revit2018_rac_advanced_sample_project.rvt"
        }
      }
    },
    "links": {
      "self": {
        "href": "https://developer.api.autodesk.com/data/v1/projects/b.7388a640-3bff-4328-9dc2-aafe62359958/versions/urn:adsk.wipprod:fs.file:vf.TwJx1922Sq2MsljlLsTYFQ%3Fversion=1"
      },
      "webView": {
        "href": "https://acc.autodesk.com/docs/files/projects/7388a640-3bff-4328-9dc2-aafe62359958?folderUrn=urn%3Aadsk.wipprod%3Afs.folder%3Aco.wmO35siCRE-xcXnxHiIXMA&entityId=urn%3Aadsk.wipprod%3Afs.file%3Avf.TwJx1922Sq2MsljlLsTYFQ%3Fversion%3D1"
      }
    },
    "relationships": {
      "item": {
        "data": {
          "type": "items",
          "id": "urn:adsk.wipprod:dm.lineage:TwJx1922Sq2MsljlLsTYFQ"
        },
        "links": {
          "related": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/b.7388a640-3bff-4328-9dc2-aafe62359958/versions/urn:adsk.wipprod:fs.file:vf.TwJx1922Sq2MsljlLsTYFQ%3Fversion=1/item"
          }
        }
      },
      "links": {
        "links": {
          "self": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/b.7388a640-3bff-4328-9dc2-aafe62359958/versions/urn:adsk.wipprod:fs.file:vf.TwJx1922Sq2MsljlLsTYFQ%3Fversion=1/relationships/links"
          }
        }
      },
      "refs": {
        "links": {
          "self": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/b.7388a640-3bff-4328-9dc2-aafe62359958/versions/urn:adsk.wipprod:fs.file:vf.TwJx1922Sq2MsljlLsTYFQ%3Fversion=1/relationships/refs"
          },
          "related": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/b.7388a640-3bff-4328-9dc2-aafe62359958/versions/urn:adsk.wipprod:fs.file:vf.TwJx1922Sq2MsljlLsTYFQ%3Fversion=1/refs"
          }
        }
      },
      "downloadFormats": {
        "links": {
          "related": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/b.7388a640-3bff-4328-9dc2-aafe62359958/versions/urn:adsk.wipprod:fs.file:vf.TwJx1922Sq2MsljlLsTYFQ%3Fversion=1/downloadFormats"
          }
        }
      },
      "derivatives": {
        "data": {
          "type": "derivatives",
          "id": "dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLlR3SngxOTIyU3EyTXNsamxMc1RZRlE_dmVyc2lvbj0x"
        },
        "meta": {
          "link": {
            "href": "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLlR3SngxOTIyU3EyTXNsamxMc1RZRlE_dmVyc2lvbj0x/manifest?scopes=b360project.7388a640-3bff-4328-9dc2-aafe62359958,O2tenant.10270419"
          }
        }
      },
      "thumbnails": {
        "data": {
          "type": "thumbnails",
          "id": "dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLlR3SngxOTIyU3EyTXNsamxMc1RZRlE_dmVyc2lvbj0x"
        },
        "meta": {
          "link": {
            "href": "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLlR3SngxOTIyU3EyTXNsamxMc1RZRlE_dmVyc2lvbj0x/thumbnail?scopes=b360project.7388a640-3bff-4328-9dc2-aafe62359958,O2tenant.10270419"
          }
        }
      },
      "storage": {
        "data": {
          "type": "objects",
          "id": "urn:adsk.objects:os.object:wip.dm.prod/7e7dd77f-a436-41d7-8c8d-05bdf1470f08.rvt"
        },
        "meta": {
          "link": {
            "href": "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/7e7dd77f-a436-41d7-8c8d-05bdf1470f08.rvt?scopes=b360project.7388a640-3bff-4328-9dc2-aafe62359958,O2tenant.10270419"
          }
        }
      }
    }
  }
}

```

Show More

The model name is under `data.attributes.name`.
