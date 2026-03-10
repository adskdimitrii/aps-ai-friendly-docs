# Task 4 – Upload an AppBundle to the Automation Service

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/revit/step4-publish-appbundle/

---

# Task 4 – Upload an AppBundle to the Automation Service

An AppBundle is a package of binaries and supporting files that make a Revit add-in.

By the end of this task you will be able to:

- Put together an AppBundle.
- Upload an AppBundle to the Automation Service.
- Create an alias for the AppBundle.
- Create a new version of the AppBundle.
- Point the alias to the new version of the AppBundle.

You will use the following operations to handle AppBundles in this task:

| HTTP Request | Description |
| --- | --- |
| [POST /appbundles](../http-docs/http-appbundles-POST.md) | Registers a new AppBundle. |
| [POST /appbundles/{id}/aliases](../http-docs/http-appbundles-id-aliases-POST.md) | Creates a new alias for the AppBundle. |
| [POST /appbundles/{id}/versions](../http-docs/http-appbundles-id-versions-POST.md) | Creates a new version of the AppBundle. |
| [PATCH /appbundles/{id}/aliases/{aliasId}](../http-docs/http-appbundles-id-aliases-aliasId-DELETE.md) | Modify alias details. |

## [Step 1 - Understand the structure of an AppBundle](#step-1-understand-the-structure-of-an-appbundle)

A Revit AppBundle file is a zip file that contains specific contents stored according to a specific structure.

Download the example AppBundle for this exercise, DeleteWallsApp.zip, [from this repository](https://github.com/autodesk-platform-services/aps-tutorial-postman/tree/master/DA4Revit/walkthrough_data).

The following code block shows the structure of the AppBundle DeleteWallsApp.zip.

```
DeleteWallsApp.zip
|-- DeleteWalls.bundle
|   |-- PackageContents.xml
|   |-- Contents
|   |   |-- DeleteWalls.dll
|   |   |-- DeleteWalls.addin

```

The top-level folder is named `*.bundle`. This folder contains a file named `PackageContents.xml`. This file contains the details of the AppBundle, the relative path to its add-in file, and its runtime requirements, as shown in the following code block.

```
<?xml version="1.0" encoding="utf-8" ?>
<ApplicationPackage>
  <Components Description="Delete Walls">
    <RuntimeRequirements OS="Win64"
                          Platform="Revit"
                          SeriesMin="R2024"
                          SeriesMax="R2024" />
    <ComponentEntry AppName="DeleteWalls"
                    Version="1.0.0"
                    ModuleName="./Contents/DeleteWalls.addin"
                    AppDescription="Deletes walls"
                    LoadOnCommandInvocation="False"
                    LoadOnRevitStartup="True" />
  </Components>
</ApplicationPackage>

```

Show More

`SeriesMin` and `SeriesMax` both refer to Revit 2024 as `R2024`. The Automation Service currently supports AppBundles that run on Revit versions `R2018` through `R2024`. For more information on `PackageContents.xml`, see [PackageContents.xml Format Reference](https://help.autodesk.com/view/ACD/2024/ENU/?guid=GUID-BC76355D-682B-46ED-B9B7-66C95EEF2BD0)

The `*.bundle\Contents` folder contains the add-in file, the application DLL, and its dependencies. The following code block shows the content of *DeleteWalls.addin*.

```
<?xml version="1.0" encoding="utf-8"?>
<RevitAddIns>
  <AddIn Type="DBApplication">
    <Name>DeleteWalls</Name>
    <Assembly>.\DeleteWalls.dll</Assembly>
    <AddInId>d7fe1983-8f10-4983-98e2-c3cc332fc978</AddInId>
    <FullClassName>DeleteWalls.DeleteWallsApp</FullClassName>
    <Description>"Walls Deleter"</Description>
    <VendorId>Autodesk</VendorId>
    <VendorDescription>
    </VendorDescription>
  </AddIn>
</RevitAddIns>

```

Show More

**Notes:**

- `Type` must be `DBApplication`. The Automation Service doesn’t support applications that need Revit’s UI functionality. `Assembly` must be a relative path to the DLL.
    You can find examples of the *bundle* folder and *PackageContent.xml* file in the presentation on Autodesk Exchange Revit Apps in [this presentation](https://github.com/ADN-DevTech/typepad-migration-dump/raw/refs/heads/main/AEC/Blog/_data/_assets/3_20Autodesk_20Exchange_20Publish_20Revit_20Apps_20-_20Preparing_20Apps_20for_20the_20Store_Guidelines.pptx?download=).

    You can use PackageContents.xml from any existing Autodesk Exchange Revit app with the Automation API. However, the Automation Service reads only the `RuntimeRequirements` and `ComponentEntry` blocks, which are circled in the image shown below.



The source code and dependent library associated with this AppBundle are:

- [DeleteWalls sample](https://github.com/autodesk-platform-services/aps-tutorial-postman/tree/master/DA4Revit/walkthrough_data)
- [DesignAutomationBridge](https://www.nuget.org/packages/Autodesk.Forge.DesignAutomation.Revit)

## [Step 2 - Register the AppBundle](#step-2-register-the-appbundle)

Before you upload the AppBundle to the Automation Service, you must register the AppBundle.

- Register an AppBundle named `DeleteWallsApp` as per the following example. It uses Revit 2018 as the target engine:

### Request

```
curl -X POST \
  'https://developer.api.autodesk.com/da/us-east/v3/appbundles' \
  -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": "DeleteWallsApp",
  "engine": "Autodesk.Revit+2024",
  "description": "Delete Walls AppBundle based on Revit 2024"
}'

```

Show More

| Attribute | Description |
| --- | --- |
| `id` | The name given to the AppBundle. |
| `engine` | The engine used by the AppBundle. |

### Response

```
{
    "uploadParameters": {
        "endpointURL": "https://dasprod-store.s3.amazonaws.com",
        "formData": {
            "key": "apps/Revit/DeleteWallsApp/1",
            "content-type": "application/octet-stream",
            "policy": "eyJleHBpcmF0aW9uIjoiMjAxOC... (truncated)",
            "success_action_status": "200",
            "success_action_redirect": "",
            "x-amz-signature": "6c68268e23ecb8452... (truncated)",
            "x-amz-credential": "ASIAQ2W... (truncated)",
            "x-amz-algorithm": "AWS4-HMAC-SHA256",
            "x-amz-date": "20180810... (truncated)",
            "x-amz-server-side-encryption": "AES256",
            "x-amz-security-token": "FQoGZXIvYXdzEPj//////////wEaDHavu... (truncated)"
        }
    },
    "engine": "Autodesk.Revit+2018",
    "description": "Delete Walls AppBundle based on Revit 2018",
    "version": 1,
    "id": "YOUR_NICKNAME.DeleteWallsApp"
}

```

Show More

| Attribute | Description |
| --- | --- |
| `endpointURL` | **This is the URL you must upload your AppBundle zip file to.** |
| `version` | The version number for the AppBundle created by the POST request. For new AppBundles, the returned version is always `1`. |
| `formData` | The form data that needs to accompany your AppBundle upload. The `formData` expires in `3600` seconds. |

## [Step 3 - Upload the AppBundle](#step-3-upload-the-appbundle)

Upload the AppBundle to the signed URL returned by `endpointURL` in the previous step.

```
curl -X POST \
  'https://dasprod-store.s3.amazonaws.com' \
  -H 'Cache-Control: no-cache' \
  -F 'key=apps/Revit/DeleteWallsApp/1' \
  -F 'content-type=application/octet-stream' \
  -F 'policy=eyJleHBpcmF0aW9uIjoiMjAxOC... (truncated)' \
  -F 'success_action_status="200"' \
  -F 'success_action_redirect=' \
  -F 'x-amz-signature=6c68268e23ecb8452... (truncated)' \
  -F 'x-amz-credential=ASIAQ2W... (truncated)' \
  -F 'x-amz-algorithm=AWS4-HMAC-SHA256' \
  -F 'x-amz-date=20180810... (truncated)' \
  -F 'x-amz-server-side-encryption=AES256' \
  -F 'x-amz-security-token=FQoGZXIvYXdzEPj//////////wEaDHavu... (truncated)' \
  -F 'file=@path/to/your/app/zip'

```

Show More

**Note:** Ensure that all the form-data from the [create AppBundle](#create-a-new-appbundle) response is included in your request.

## [Step 4 - Create an alias for the AppBundle](#step-4-create-an-alias-for-the-appbundle)

When you registered the AppBundle in step 2, it was registered as version 1 of the AppBundle. In this step, you create an alias named `test` to reference that version.

```
curl -X POST \
  'https://developer.api.autodesk.com/da/us-east/v3/appbundles/DeleteWallsApp/aliases' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  -d '{
      "version": 1,
      "id": "test"
    }'

```

Show More

## [Step 5 - Update an existing AppBundle](#step-5-update-an-existing-appbundle)

To update an existing AppBundle, you must register a new version for the AppBundle and then upload the updated AppBundle for that version. If you try to overwrite an existing AppBundle, the Automation Service returns a `409 Conflict` error.

To register a new version of the AppBundle DeleteWallsApp:

### Request

```
curl -X POST \
  'https://developer.api.autodesk.com/da/us-east/v3/appbundles/DeleteWallsApp/versions'\
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  -d '{
      "id": null,
      "engine": "Autodesk.Revit+2024",
      "description": "Delete Walls AppBundle based on Revit 2024"
    }'

```

Show More

**Note:** You can omit `id` from the request body. If you include `id` in the request body, set it to `null`. If you don’t set it to `null`, the Automation Service returns an error.

### Response

```
{
    "uploadParameters": {
        "endpointURL": "https://dasprod-store.s3.amazonaws.com",
        "formData": {
            "key": "apps/Revit/DeleteWallsApp/2",
            "content-type": "application/octet-stream",
            "policy": "eyJleHBpcmF0aW9uIjoiMjAxOC... (truncated)",
            "success_action_status": "200",
            "success_action_redirect": "",
            "x-amz-signature": "6c68268e23ecb8452... (truncated)",
            "x-amz-credential": "ASIAQ2W... (truncated)",
            "x-amz-algorithm": "AWS4-HMAC-SHA256",
            "x-amz-date": "20180810... (truncated)",
            "x-amz-server-side-encryption": "AES256",
            "x-amz-security-token": "FQoGZXIvYXdzEPj//////////wEaDHavu... (truncated)"
        }
    },
    "engine": "Autodesk.Revit+2018",
    "description": "Delete Walls AppBundle based on Revit 2018",
    "version": 2,
    "id": "YOUR_NICKNAME.DeleteWallsApp"
}

```

Show More

The response to the AppBundle version post includes:

| Attribute | Description |
| --- | --- |
| `endpointURL` | **This is the signed URL to which you must upload the updated AppBundle.** |
| `version` | The new version number for the AppBundle created by the above POST request. |

## [Step 6 - Upload the updated AppBundle](#step-6-upload-the-updated-appbundle)

Follow the procedure outlined in Step 3 to upload the AppBundle to the signed URL returned by `endpointURL`.

## [Step 7 - Assign an existing alias to the updated AppBundle](#step-7-assign-an-existing-alias-to-the-updated-appbundle)

Currently, the alias *test* points to version 1 of the AppBundle.

| id | alias | version |
| --- | --- | --- |
| DeleteWallsApp | test | 1 |
| DeleteWallsApp |  | 2 |

You can reassign the alias *test* to version 2 of the AppBundle DeleteWallsApp.

| id | alias | version |
| --- | --- | --- |
| DeleteWallsApp |  | 1 |
| DeleteWallsApp | test | 2 |

To reassign the alias, you can either:

- Delete the existing alias and recreate it to point to the desired version.
- Send a PATCH request.

To send a PATCH request:

### Request

```
curl -X PATCH \
'https://developer.api.autodesk.com/da/us-east/v3/appbundles/DeleteWallsApp/aliases/test ''\
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
-d '{
            "version": 2
          }'

```

**Notes:**

- `version` - Refers to the version number the alias must point to.
- You can use this technique to make sure that an alias always points to the latest version of an AppBundle.

## [Additional notes](#additional-notes)

- Each AppBundle POST request specifies an `engine` on which the application runs. The following table shows the keywords to specify for the available Revit engines.
- The `engine` must match the `SeriesMin` and `SeriesMax` settings specified in the AppBundle’s PackageContent.xml.
- The active engine version aliases are:

| Engine | Description | JSON in AppBundle post | DesignAutomationBridge DLL |
| --- | --- | --- | --- |
| `Autodesk.Revit+2021` | Revit 2021.1.7 | “engine”: “Autodesk.Revit+2021” | [DesignAutomationBridge.dll](https://www.nuget.org/packages/Autodesk.Forge.DesignAutomation.Revit/2021.0.2) for 2021. |
| `Autodesk.Revit+2022` | Revit 2022.1.3 | “engine”: “Autodesk.Revit+2022” | [DesignAutomationBridge.dll](https://www.nuget.org/packages/Autodesk.Forge.DesignAutomation.Revit/2022.0.1) for 2022. |
| `Autodesk.Revit+2023` | Revit 2023.1.1 | “engine”: “Autodesk.Revit+2023” | [DesignAutomationBridge.dll](https://www.nuget.org/packages/Autodesk.Forge.DesignAutomation.Revit/2023.0.2) for 2023. |
| `Autodesk.Revit+2024` | Revit 2024.0.0 | “engine”: “Autodesk.Revit+2024” | [DesignAutomationBridge.dll](https://www.nuget.org/packages/Autodesk.Forge.DesignAutomation.Revit/2024.0.2) for 2024. |
| `Autodesk.Revit+2025` | Revit 2025.3.0 | “engine”: “Autodesk.Revit+2025” | [DesignAutomationBridge.dll](https://www.nuget.org/packages/Autodesk.Forge.DesignAutomation.Revit/2025.0.1) for 2025. |
| `Autodesk.Revit+2026` | Revit 2026.3.0 | “engine”: “Autodesk.Revit+2026” | [DesignAutomationBridge.dll](https://www.nuget.org/packages/Autodesk.Forge.DesignAutomation.Revit/2026.0.0) for 2026. |

**Notes:**

- For the most current list of `engines` use the operation listed [here](https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/#engines).
- If there is an error, refer the section on [troubleshooting](https://aps.autodesk.com/en/docs/design-automation/v3/developers_guide/troubleshooting/).
