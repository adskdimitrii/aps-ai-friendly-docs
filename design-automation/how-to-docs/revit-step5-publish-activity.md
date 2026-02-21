# Task 5 â Publish an Activity

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/revit/step5-publish-activity/

---

# Task 5 â Publish an Activity

An Activity is an action that can be executed on the Automation Service. You create and post Activities to run specific AppBundles.

By the end of this task, you will know:
> - What an Activity is.
> - How to create an Activity.
> - How to create new versions of an Activity.
> - How to reference a specific version of an Activity by an alias.

You will use the following operations to handle Activities for this task:

| HTTP Request | Description |
| --- | --- |
| [POST /activities](/en/docs/design-automation/v3/reference/http/activities-POST) | Creates a new Activity. |
| [POST /activities/{id}/aliases](/en/docs/design-automation/v3/reference/http/activities-id-aliases-POST) | Creates a new alias for this Activity. |
| [POST /activities/{id}/versions](/en/docs/design-automation/v3/reference/http/activities-id-versions-GET) | Creates a new version of the Activity. |
| [PATCH /activities/{id}/aliases/{aliasId}](/en/docs/design-automation/v3/reference/http/activities-id-aliases-aliasId-PATCH) | Modifies alias details. |

## [Step 1 - Create a new Activity](#step-1-create-a-new-activity)

To create a new Activity named DeleteWallsActivity, post this request:

### Request

```
curl -X POST \
  'https://developer.api.autodesk.com/da/us-east/v3/activities' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  -d '{
            "id": "DeleteWallsActivity",
            "commandLine": [ "$(engine.path)\\\\revitcoreconsole.exe /i \"$(args[rvtFile].path)\" /al \"$(appbundles[DeleteWallsApp].path)\"" ],
            "parameters": {
              "rvtFile": {
                "zip": false,
                "ondemand": false,
                "verb": "get",
                "description": "Input Revit model",
                "required": true,
                "localName": "$(rvtFile)"
              },
              "result": {
                "zip": false,
                "ondemand": false,
                "verb": "put",
                "description": "Results",
                "required": true,
                "localName": "result.rvt"
              }
            },
            "engine": "Autodesk.Revit+2024",
            "appbundles": [ "<YOUR_NICKNAME>.DeleteWallsApp+test" ],
            "description": "Deletes walls from Revit file."
    }'

```

Show More

| Attribute | Description |
| --- | --- |
| `id` | The name given to your new Activity. |
| `commandLine` | The command run by this Activity.       - `$(engine.path)\\\\revitcoreconsole.exe` - The full path to the folder from which the engine for Revit executes.      The engine is defined in the request body as `"engine": "Autodesk.Revit+2024"`. More information about engines can be found in the   Additional notes section in [Task 4](/en/docs/design-automation/v3/tutorials/revit/step4-publish-appbundle#additional-notes).   **Do not edit or alter this âcommandLineâ in the request body of Activity posts.**       - `$(args[rvtFile].path)` - The full path to the folder that contains the input Revit model. `rvtFile` is the parameter that      represents the Revit model to which the Activity `DeleteWallsActivity` applies the AppBundle. The AppBundle is defined in   the request body as `"appbundles": [ "<YOUR_NICKNAME>.DeleteWallsApp\ +test" ]`. |
| `parameters` | The parameters that must be passed to this Activity, when it is executed (via a WorkItem).   You will specify values for these parameters in task 6, at the time you submit a WorkItem to execute this Activity |
| `engine` | The engine on which your Activity runs. The available engine versions are described in the Additional notes section in   [Task 4](/en/docs/design-automation/v3/tutorials/revit/step4-publish-appbundle#additional-notes). |
| `appbundles` | The fully qualified id of the AppBundle that this Activity applies to the input rvt file.   It is currently defined as `[ "<YOUR_NICKNAME>.DeleteWallsApp\ +test" ]` ,   where `<YOUR_NICKNAME>` represents the Client ID of the app the AppBundle `DeleteWallsApp` was uploaded to. |

### Response

```
{
    "commandLine": [
        "$(engine.path)\\\\revitcoreconsole.exe /i \"$(args[rvtFile].path)\" /al \"$(appbundles[DeleteWallsApp].path)\""
    ],
    "parameters": {
        "rvtFile": {
            "verb": "get",
            "zip":false,
            "ondemand":false,
            "description": "Input Revit model",
            "required": true,
            "localName": "input.rvt"
        },
        "result": {
            "verb": "put",
            "description": "Results",
            "required": true,
            "localName": "result.rvt"
        }
    },
    "engine": "Autodesk.Revit+2018",
    "appbundles": [
        "<YOUR_NICKNAME>.DeleteWallsApp+test"
    ],
    "description": "Delete walls from Revit file.",
    "version": 1,
    "id": "<YOUR_NICKNAME>.DeleteWallsActivity"
}

```

Show More

The response includes:

| Attribute | Description |
| --- | --- |
| `version` | The version number for the Activity created by the post request. A post request that creates a new Activity will get version number `1`. |

## [Step 2 - Create an alias to the Activity](#step-2-create-an-alias-to-the-activity)

The Automation API does not let you reference an Activity by its `id`. You must always reference an Activity by an alias. Note that an alias points to a specific version of an Activity and not the Activity itself.

To create an alias named `test`, which refers to version `1` of the `DeleteWallsActivity`:

### Request

```
curl -X POST \
  'https://developer.api.autodesk.com/da/us-east/v3/activities/DeleteWallsActivity/aliases' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  -d '{
      "version": 1,
      "id": "test"
    }'

```

Show More

### Response

```
{
    "version": 1,
    "id": "test"
}

```

## [Step 3 - Update an existing Activity](#step-3-update-an-existing-activity)

The Automation API does not let you overwrite an Activity once you have created it. If you want to modify/update an existing Activity,
you must update it as a new version.
If you try to overwrite an existing Activity, the Automation Service returns a `409 Conflict` error.

To create a new version of an Activity:

### Request

```
curl -X POST \
 'https://developer.api.autodesk.com/da/us-east/v3/activities/DeleteWallsActivity/versions' \
 -H 'Content-Type: application/json' \
 -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
 -d '{
        "id": null,
        "commandLine": [ "$(engine.path)\\\\revitcoreconsole.exe /i \"$(args[rvtFile].path)\" /al \"$(appbundles[DeleteWallsApp].path)\"" ],
        "parameters": {
          "rvtFile": {
            "verb": "get",
            "zip":false,
            "ondemand":false,
            "description": "Input Revit model",
            "required": true,
            "localName": "input.rvt"
          },
          "result": {
            "zip": false,
            "ondemand": false,
            "verb": "put",
            "description": "Results",
            "required": true,
            "localName": "result.rvt"
          }
        },
        "engine": "Autodesk.Revit+2018",
        "appbundles": [ "<YOUR_NICKNAME>.DeleteWallsApp+test" ],
        "description": "Delete walls from Revit file Updated."
}'

```

Show More

**Note:** You can omit `id` from the request body. If you include `id` in the request body, set it to `null`. If you donât set it to `null`, the Automation Service returns an error.

### Response

```
{
    "commandLine": [
        "$(engine.path)\\\\revitcoreconsole.exe /i \"$(args[rvtFile].path)\" /al \"$(appbundles[DeleteWallsApp].path)\""
    ],
    "parameters": {
        "rvtFile": {
            "verb": "get",
            "description": "Input Revit model",
            "required": true,
            "localName": "$(rvtFile)"
        },
        "result": {
            "verb": "put",
            "description": "Results",
            "required": true,
            "localName": "result.rvt"
        }
    },
    "engine": "Autodesk.Revit+2018",
    "appbundles": [
        "<YOUR_NICKNAME>.DeleteWallsApp+test"
    ],
    "description": "Delete walls from Revit file Updated.",
    "version": 2,
    "id": "<YOUR_NICKNAME>.DeleteWallsActivity"
}

```

Show More

## [Step 4 - Assign an existing alias to the updated Activity](#step-4-assign-an-existing-alias-to-the-updated-activity)

Currently, the alias *test* points to version 1 of the Activity.

| id | alias | version |
| --- | --- | --- |
| DeleteWallsActivity | test | 1 |
| DeleteWallsActivity |  | 2 |

You can reassign the alias *test* to point to version 2 of the Activity.

| id | alias | version |
| --- | --- | --- |
| DeleteWallsActivity |  | 1 |
| DeleteWallsActivity | test | 2 |

To update the alias, you can either:

- Delete the existing alias and recreate it with the version you want to label.
- Send a PATCH request.

To send a PATCH request:

### Request

```
curl -X PATCH \
'https://developer.api.autodesk.com/da/us-east/v3/activities/DeleteWallsActivity/aliases/test' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
-d '{
        "version": 2
        }'

```

**Notes:**

- `version` - Refers to the version number the alias labels.

## [Additional notes](#additional-notes)

By default the Automation Service runs the Revit engine in English. However, you can request the Automation Service to run the Revit engine in a specific language using the `/l` specifier on `commandLine`.
The list of supported languages are listed in [this article](https://knowledge.autodesk.com/support/revit-products/troubleshooting/caas/CloudHelp/cloudhelp/2020/ENU/Revit-Installation/files/GUID-BD09C1B4-5520-475D-BE7E-773642EEBD6C-htm.html) for the full list of language codes.

The following example instructs the Automation Service to launch the Revit engine in German. This feature is useful when you want the built-in elements to be labelled in German.

```
{
    "commandLine": [
        "$(engine.path)\\\\revitcoreconsole.exe /i \"$(args[rvtFile].path)\" /al \"$(appbundles[DeleteWallsApp].path)\" /l DEU"
    ],
...
}

```
