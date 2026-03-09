# Task 4 â Publish an Activity

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/inventor/task4-publish-activity/

---

# Task 4 â Publish an Activity

An Activity is an action that can be executed on the Automation Service. You create and post Activities to run specific AppBundles.

By the end of this task, you will know:
> - What an Activity is.
> - How to create an Activity.
> - How to create new versions of an Activity.
> - How to reference a specific version of an Activity by an alias.

You will use the following operations to handle Activities for this task:

| HTTP Request | Description |
| --- | --- |
| [POST /activities](../http-docs/http-activities-POST.md) | Creates a new Activity. |
| [POST /activities/{id}/aliases](../http-docs/http-activities-id-aliases-POST.md) | Creates a new alias for this Activity. |
| [POST /activities/{id}/versions](../http-docs/http-activities-id-versions-GET.md) | Creates a new version of the Activity. |
| [PATCH /activities/{id}/aliases/{aliasId}](../http-docs/http-activities-id-aliases-aliasId-PATCH.md) | Modifies alias details. |

## [Step 1 - Create a new Activity](#step-1-create-a-new-activity)

To create a new Activity named ChangeParamActivity, post this request:

### Request

```
curl -X POST \
  'https://developer.api.autodesk.com/da/us-east/v3/activities' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  -d '{
        "id": "ChangeParamActivity",
        "commandLine": [
            "$(engine.path)\\InventorCoreConsole.exe /i \"$(args[InventorDoc].path)\" /al \"$(appbundles[ChangeParamApp].path)\" \"$(args[InventorParams].path)\""
        ],
        "parameters": {
          "InventorDoc": {
            "zip": false,
            "ondemand": false,
            "verb": "get",
            "description": "Input Inventor part file",
            "localName": "Input.ipt"
          },
           "InventorParams": {
            "zip": false,
            "ondemand": false,
            "verb": "get",
            "description" : "JSON object containing new width and height parameters",
            "localName": "params.json"
          },
          "OutputIpt": {
            "zip": false,
            "ondemand": false,
            "optional": true,
            "localName": "ResultSmall.ipt",
            "verb": "post"
          },
          "OutputIam": {
            "zip": false,
            "ondemand": false,
            "optional": true,
            "localName": "ResultSmall.zip",
            "verb": "post"
          },
          "OutputBmp": {
            "zip": false,
            "ondemand": false,
            "optional": true,
            "localName": "ResultSmall.bmp",
            "verb": "post"
          }
        },
        "engine": "Autodesk.Inventor+24",
        "appbundles": [
            "YOUR_APP_NICKNAME.ChangeParamApp+my_working_version"
        ],
        "settings": {},
        "description": "Resizes an Inventor part or assembly to the height and width parameters contained in the JSON object specified by the InventorParams parameter. Also produces a BMP file of the result."
    }'

```

Show More

| Attribute | Description |
| --- | --- |
| `id` | The name given to your new Activity. |
| `commandLine` | The command run by this Activity.       - `$(engine.path)\\InventorCoreConsole.exe` - The full path to the Inventor engine.      The version of Inventor to be used is defined in the request body as âengineâ: âAutodesk.Inventor+24 (Inventor 2020).   More information about engines can be found in the Additional notes section of the [previous step](inventor-task3-upload-appbundle.md#additional-notes) .       - `$(args[InventorDoc].path)` - The full path to the folder that the file identified by the parameter InventorDoc is downloaded to.       - `$(appbundles[ChangeParamApp].path)` - The full path to where the AppBundle specified under `appbundles` is unzipped to.       - `$(args[InventorParams].path)` - The full path to where the JSON file carrying the height and width parameters is saved to. |
| `parameters` | Defines the inputs and outputs that need to be provided when the Activity is executed.   Input parameters are identified by the attribute âverbâ:âgetâ. Output parameters are identified by the attribute `âverbâ:âputâ. |
| `engine` | The engine on which your Activity runs. The available engine versions are described in the Additional notes section in [Task 3](inventor-task3-upload-appbundle.md#additional-notes) |
| `appbundles` | The fully qualified id of the AppBundle referred to in `commandLine`. |

### Response

```
{
  "commandLine": [
      "$(engine.path)\\InventorCoreConsole.exe /i \"$(args[InventorDoc].path)\" /al \"$(appbundles[ChangeParamApp].path)\" \"$(args[InventorParams].path)\""
  ],
  "parameters": {
      "InventorDoc": {
          "verb": "get",
          "description": "Input Inventor part file",
          "localName": "Input.ipt"
      },
      "InventorParams": {
          "verb": "get",
          "description": "JSON object containing new width and height parameters",
          "localName": "params.json"
      },
      "OutputIpt": {
          "verb": "post",
          "localName": "ResultSmall.ipt"
      },
      "OutputIam": {
          "zip": false,
          "verb": "post",
          "localName": "ResultSmall.zip"
      },
      "OutputBmp": {
          "verb": "post",
          "localName": "ResultSmall.bmp"
      }
  },
  "id": "<YOUR_APP_NICKNAME>.ChangeParamActivity",
  "engine": "Autodesk.Inventor+24",
  "appbundles": [
      "<YOUR_APP_NICKNAME>.ChangeParamApp+my_working_version"
  ],
  "settings": {},
  "description": "Resizes an Inventor part or assembly to the height and width parameters contained in the JSON object specified by the InventorParams parameter. Also produces a BMP file of the result.",
  "version": 1
}

```

Show More

The response includes:

| Attribute | Description |
| --- | --- |
| `version` | The version number for the Activity created by the post request. A post request that creates a new Activity will get version number `1`. |

## [Step 2 - Create an alias to the Activity](#step-2-create-an-alias-to-the-activity)

The Automation API does not let you reference an Activity by its `id`. You must always reference an Activity by an alias. Note that an alias points to a specific version of an Activity and not the Activity itself.

To create an alias named `current_version`, which refers to version `1` of the `ChangeParamActivity`:

### Request

```
curl -X POST \
  'https://developer.api.autodesk.com/da/us-east/v3/activities/ChangeParamActivity/aliases' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -d '{
        "version": 1,
        "id": "my_current_version""
      }'

```

Show More

### Response

```
{
    "version": 1,
    "id": "my_current_version"
}

```

## [Step 3 - Update an existing Activity](#step-3-update-an-existing-activity)

**NOTE: This step is optional**

The Automation API does not let you overwrite an Activity once you have created it. If you want to modify/update an existing Activity,
you must update it as a new version.
If you try to overwrite an existing Activity, the Automation Service returns a `` `409 Conflict `` error.

To create a new version of an Activity:

### Request

```
curl -X POST \
  'https://developer.api.autodesk.com/da/us-east/v3/activities/ChangeParamActivity/versions' \
  -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": null,
    "commandLine": [
        "$(engine.path)\\InventorCoreConsole.exe /i \"$(args[InventorDoc].path)\" /al $\"(appbundles[ChangeParamApp].path)\" \"$(args[InventorParams].path)\""
    ],
    "parameters": {
      "InventorDoc": {
        "zip": false,
        "ondemand": false,
        "verb": "get",
        "description": "Input Inventor part file",
        "localName": "Input.ipt"
      },
       "InventorParams": {
            "zip": false,
            "ondemand": false,
            "verb": "get",
            "description" : "JSON object containing new width and height parameters",
        "localName": "params.json"
      },
      "OutputIpt": {
        "zip": false,
        "ondemand": false,
        "optional": true,
        "localName": "ResultSmall.ipt",
        "verb": "post"
      },
      "OutputIam": {
        "zip": true,
        "ondemand": false,
        "optional": true,
        "localName": "ResultSmall.zip",
        "verb": "post"
      },
      "OutputBmp": {
        "zip": false,
        "ondemand": false,
        "optional": true,
        "localName": "ResultSmall.bmp",
        "verb": "post"
      }
    },
    "engine": "Autodesk.Inventor+2024",
    "appbundles": [
        "<YOUR_APP_NICKNAME>.ChangeParamApp+my_working_version"
    ],
    "settings": {},
    "description": "Resizes an Inventor part or assembly to the height and width parameters contained in the JSON object specified by the InventorParams parameter. Also produces a BMP file of the result."
}'

```

Show More

**Note:** You can omit `id` from the request body. If you include `id` in the request body, set it to `null`. If you donât set it to `null`, the Automation Service throws an error.

### Response

```
{
    "commandLine": [
        "$(engine.path)\\InventorCoreConsole.exe /i \"$(args[InventorDoc].path)\" /al \"$(appbundles[ChangeParamApp].path)\" \"$(args[InventorParams].path)\""
    ],
    "parameters": {
        "InventorDoc": {
            "verb": "get",
            "description": "Input Inventor part file",
            "localName": "Input.ipt"
        },
        "InventorParams": {
            "verb": "get",
            "description": "JSON object containing new width and height parameters",
            "localName": "params.json"
        },
        "OutputIpt": {
            "verb": "post",
            "localName": "ResultSmall.ipt"
        },
        "OutputIam": {
            "zip": true,
            "verb": "post",
            "localName": "ResultSmall.zip"
        },
        "OutputBmp": {
            "verb": "post",
            "localName": "ResultSmall.bmp"
        }
    },
    "id": "YOUR_APP_NICKNAME.ChangeParamActivity",
    "engine": "Autodesk.Inventor+24",
    "appbundles": [
        "YOUR_APP_NICKNAME.ChangeParamApp+my_working_version"
    ],
    "settings": {},
    "description": "Resizes an Inventor part or assembly to the height and width parameters contained in the JSON object specified by the InventorParams parameter. Also produces a BMP file of the result.",
    "version": 2
}

```

Show More

## [Step 4 - Assign an existing alias to the updated Activity](#step-4-assign-an-existing-alias-to-the-updated-activity)

**NOTE: Perform this step only if you carried out Step 3**

Currently, the alias *current_version* points to version 1 of the Activity.

| id | alias | version |
| --- | --- | --- |
| ChangeParamActivity | current_version | 1 |
| ChangeParamActivity |  | 2 |

You can reassign the alias *current_version* to point to version 2 of the Activity.

| id | alias | version |
| --- | --- | --- |
| ChangeParamActivity |  | 1 |
| ChangeParamActivity | current_version | 2 |

To update the alias, you can either:

- Delete the existing alias and recreate it with the version you want to label.
- Send a PATCH request.

To send a PATCH request:

### Request

```
  curl -X PATCH \
  'https://developer.api.autodesk.com/da/us-east/v3/activities/ChangeParamActivity/aliases/my_current_version' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  -d '{
  "version": 2
}'

```

**Notes:**

- `version` - Refers to the version number the alias labels.
