# Task 3 – Upload an AppBundle to the Automation Service

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/fusion/task3-upload-appbundle/

---

# Task 3 – Upload an AppBundle to the Automation Service

An AppBundle is a zipped folder containing the TypeScript file. The file is saved to a specific structure, and is accompanied by a file named *PackageContents.xml*, which describes the content of the folder.

A script uses the Fusion API to add new functionality to Fusion in the form of custom commands.

Information on how to create a Fusion script, [can be found here.](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-A92A4B10-3781-4925-94C6-47DA85A4F65A)

For information on creating an Automation API-ready Fusion script, see the information about the TypeScript Add-In for Fusion [here](https://aps.autodesk.com/en/docs/design-automation/v3/developers_guide/fusion/typescript/).

By the end of this task you will be able to:

- Describe what an AppBundle is.
- Explain the role of *PackageContents.xml* file
- Upload an AppBundle to the Automation Service.
- Create an alias for a version of the AppBundle.

You will use the following operations to handle AppBundles in this task:

| HTTP Request | Description |
| --- | --- |
| [POST /appbundles](../http-docs/http-appbundles-POST.md) | Registers a new AppBundle. |
| [POST /appbundles/{id}/aliases](../http-docs/http-appbundles-id-aliases-POST.md) | Creates a new alias for the AppBundle. |
| [POST /appbundles/{id}/versions](../http-docs/http-appbundles-id-versions-POST.md) | Creates a new version of the AppBundle. |
| [PATCH /appbundles/{id}/aliases/{aliasId}](../http-docs/http-appbundles-id-aliases-aliasId-DELETE.md) | Modify alias details. |

- More information on AppBundles can be found [here](https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/#appbundles).

## [Step 1 - Download or build an Fusion AppBundle](#step-1-download-or-build-an-fusion-appbundle)

- Download the AppBundle, *ConfigureDesign.zip* from [here](https://github.com/autodesk-platform-services/aps-tutorial-postman/blob/master/DA4Fusion/walkthrough_data/ConfigureDesign.zip).

## [Step 2 - Understand the Structure of the AppBundle](#step-2-understand-the-structure-of-the-appbundle)

A Fusion AppBundle is a zipped package of a TypeScript file stored according to a specific structure. The following code block shows the structure of the AppBundle *ConfigureDesign.zip*, which you downloaded in Step 1.

```
ConfigureDesign.zip
|-- ConfigureDesign
|   |-- PackageContents.xml
|   |-- Contents
|   |   |-- main.ts

```

| File | Description |
| --- | --- |
| *PackageContents.xml* | Contains a description of the add-in, including the GUIDs and relative path to the add-in. For more information on *PackageContents.xml*, see [PackageContents.xml Format Reference](https://help.autodesk.com/view/ACD/2021/ENU/?guid=GUID-BC76355D-682B-46ED-B9B7-66C95EEF2BD0) |
| *main.ts* | The TypeScript file that will be executed with the fusion api |

## [Step 3 - Register the AppBundle](#step-3-register-the-appbundle)

Before you upload the AppBundle to the Automation Service, you must register the AppBundle.

- Register an AppBundle named `ConfigureDesignAppBundle` as per the following example. It uses the latest Fusion engine as the target engine:

### Request

```
curl -X POST \
  'https://developer.api.autodesk.com/da/us-east/v3/appbundles' \
  -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
        "id": "ConfigureDesignAppBundle",
        "engine": "Autodesk.Fusion+Latest",
        "description": "My first fusion appbundle based on the latest Fusion engine"
      }'

```

Show More

| Attribute | Description |
| --- | --- |
| `id` | The name given to the AppBundle. |
| `engine` | The engine that the AppBundle must be loaded on; Fusion latest in this case. For more information on engine aliases, see the Additional Notes section at the bottom of this page. |

### Response

```
{
    "uploadParameters": {
        "endpointURL": "https://dasprod-store.s3.amazonaws.com",
        "formData": {
            "key": "apps/<YOUR_NICKNAME>/ConfigureDesignAppBundle/1",
            "content-type": "application/octet-stream",
            "policy": "eyJleHBpcmF0aW9uIjo... (truncated)",
            "success_action_status": "200",
            "success_action_redirect": "",
            "x-amz-signature": "27e07941f952... (truncated)",
            "x-amz-credential": "ASIATGVJZKM3N... (truncated)",
            "x-amz-algorithm": "AWS4-HMAC-SHA256",
            "x-amz-date": "20191128T083159Z",
            "x-amz-server-side-encryption": "AES256",
            "x-amz-security-token": "IQoJb3JpZ2luX2VjEGgaC... (truncated)"
        }
    },
    "id": "<YOUR_NICKNAME>.ConfigureDesignAppBundle",
    "engine": "Autodesk.Fusion+Latest",
    "description": "Change Parameters AppBundle based on the latest Fusion engine",
    "version": 1
}

```

Show More

| Attribute | Description |
| --- | --- |
| `endpointURL` | The URL you must upload the AppBundle zip file to. |
| `version` | The version number of the AppBundle created by the POST request. For new AppBundles, the returned version is always `1`. |
| `formData` | The form data that must accompany the AppBundle when you upload it to endpointURL. formData expires in `3600` seconds. |

## [Step 4 - Upload the AppBundle](#step-4-upload-the-appbundle)

Upload the AppBundle to the signed URL returned by `endpointURL` in the previous step.

```
curl -X POST \
  'https://dasprod-store.s3.amazonaws.com' \
  -H 'Cache-Control: no-cache' \
  -F key=apps/da4fusion_app/ConfigureDesignAppBundle/1 \
  -F content-type=application/octet-stream \
  -F policy=eyJleHBpcmF0aW9uIjoi... (truncated)  \
  -F success_action_status=200 \
  -F x-amz-signature=27e07941f952d73d57eca... (truncated)  \
  -F x-amz-credential=ASIATGVJZKM3NNGDUZMR/20191128/us-east-1/s3/aws4_request/ \
  -F x-amz-algorithm=AWS4-HMAC-SHA256 \
  -F x-amz-date=20191128T083159Z \
  -F x-amz-server-side-encryption=AES256 \
  -F 'x-amz-security-token=IQoJb3JpZ2luX2VjEGgaCXVzLWVhc3QtMSJ... (truncated) ' \
  -F success_action_redirect= \
  -F file= @path/to/your/Script/ConfigureDesign.zip

```

Show More

**Note:** Ensure that all the form-data from the [Register AppBundle](#step-3-register-the-appbundle) response is included in your request.

## [Step 5 - Create an alias for the AppBundle](#step-5-create-an-alias-for-the-appbundle)

When you registered the AppBundle in step 2, it was registered as version 1 of the AppBundle. In this step, you create an alias named `my_working_version` to reference that version. You can think of the alias as a tag that points to a version of an AppBundle.

```
curl -X POST \
  'https://developer.api.autodesk.com/da/us-east/v3/appbundles/ConfigureDesignAppBundle/aliases' \
    -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
    -H 'Content-Type: application/json' \
    -d '{
          "version": 1,
          "id": "my_working_version"
        }'

```

Show More

**Note:**

If you make changes to the AppBundle later, you must register it as a new version and then upload it. You can then update the alias to point to the newer version
of the AppBundle. Consequently, endpoints referencing the AppBundle using the alias get access to the updated version of the AppBundle.

## [Additional notes](#additional-notes)

### Notes on Engines

- Each AppBundle POST request specifies an `engine` on which the application runs. The following table shows the keywords to specify for the available Fusion engines.
- It is recommended to always choose the `Autodesk.Fusion+Latest` engine.
- In rare cases, you might want to access an older engine version. You can obtain the list of available `engines` using the operation listed [here](https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/#engines).

**Notes:**

- If there is an error, refer the section on [troubleshooting](https://aps.autodesk.com/en/docs/design-automation/v3/developers_guide/troubleshooting/).
- For information about the changes between releases, [see the Fusion What’s New blog posts](https://www.autodesk.com/products/fusion-360/blog/tag/whats-new/).
