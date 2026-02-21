# Task 3 â Publish an Activity

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/3dsmax/task3-create-activity/

---

# Task 3 â Publish an Activity

An Activity describes an action that can be executed on the Automation Service.
In this walkthrough, you will create an Activity that takes the following inputs:

- A zip file containing a 3ds Max scene.
- A string that indicates the name of the 3ds Max file inside the zip file.
- A MAXScript file to be executed.

By the end of this task, you will know how to create the first version of an Activity and associate it to an Alias.

You will use the following operations to handle Activities for this task:

| HTTP Request | Description |
| --- | --- |
| [POST /activities](/en/docs/design-automation/v3/reference/http/activities-POST) | Creates a new Activity. |
| [POST /activities/{id}/aliases](/en/docs/design-automation/v3/reference/http/activities-id-aliases-POST) | Creates a new alias for this Activity. |

## [Step 1 - Create a new Activity](#step-1-create-a-new-activity)

To create a new Activity named `ExecuteMaxscript`, post this request:

### Request

```
curl -X POST \
    'https://developer.api.autodesk.com/da/us-east/v3/activities' \
    -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
    -H 'Content-Type: application/json' \
    -d '{
        "id": "ExecuteMaxscript",
        "commandLine": "\"$(engine.path)/3dsmaxbatch.exe\" -sceneFile \"$(args[InputMaxScene].path)\" \"$(args[MaxscriptToExecute].path)\"",
        "description": "Execute a MAXScript on a max file provided in a zip",
        "appbundles": [
            ],
        "engine" : "Autodesk.3dsMax+2023",
        "parameters": {
            "InputMaxScene": {
                "zip": false,
                "ondemand": false,
                "verb": "get",
                "description": "Input for providing the 3ds Max scene to be loaded before executing the script",
                "required": true,
                "localName": "workingFolder"
            },
            "MaxscriptToExecute": {
                "zip": false,
                "verb": "get",
                "description": "The MAXScript to run using 3dsmaxbatch.exe",
                "ondemand": false,
                "required": true,
                "localName": "maxscriptToExecute.ms"
            },
            "OutputZip": {
                "zip": true,
                "ondemand": false,
                "verb": "put",
                "description": "Gather everything in the working folder inside a zip for output",
                "required": true,
                "localName": "workingFolder"
            }
        }
    }'

```

Show More

| Attribute | Description |
| --- | --- |
| `id` | The name given to your new Activity. |
| `commandLine` | The command run by this Activity.   The variables used in the command line are replaced with actual values before executing the Activity.   This mechanism lets you replace the file path(s) you used in the command line while testing locally   with file paths that makes sense in the Automation Service environment.       The variables used in the command line are:       - `$(engine.path)` - Will be replaced by the path to the folder containing the engine.      The engine is specified under the `engine` attribute in the JSON payload as `"engine": "Autodesk.3dsMax+2021`.   **Do not edit or alter this âcommandLineâ in the request body of Activity posts.**       - `$(args[InputMaxScene].path)` - Will be replaced by the path to a file specified by the parameter named `InputMaxScene`.       - `$(args[MaxscriptToExecute].path)` - Will be replaced by the path to a file specified by the parameter named `MaxscriptToExecute`.       For more information see [Command lines](/en/docs/design-automation/v3/developers_guide/field-guide#command-lines) |
| `engine` | The engine on which the Activity must run. |

### Response

```
{
    "commandLine": [
        "\"$(engine.path)/3dsmaxbatch.exe\" -sceneFile \"$(args[InputMaxScene].path)\" \"$(args[MaxscriptToExecute].path)\""
    ],
    "parameters": {
        "InputMaxScene": {
            "zip": false,
            "ondemand": false,
            "verb": "get",
            "description": "Input for providing the 3ds Max scene to be loaded before executing the script",
            "required": true,
            "localName": "workingFolder"
        },
        "MaxscriptToExecute": {
            "verb": "get",
            "description": "The MAXScript to run using 3dsmaxbatch.exe",
            "required": true,
            "localName": "maxscriptToExecute.ms"
        },
        "OutputZip": {
            "zip": true,
            "verb": "put",
            "description": "Gather everything in the working folder inside a zip for output",
            "required": true,
            "localName": "workingFolder"
        }
    },
    "id": "<YOUR_NICKNAME>.ExecuteMaxscript",
    "engine": "Autodesk.3dsMax+2023",
    "appbundles": [],
    "description": "Execute a MAXScript on a max file provided in a zip",
    "version": 1
}

```

Show More

## [Step 2 - Create an Alias to the Activity](#step-2-create-an-alias-to-the-activity)

In the previous step, you created version 1 of the Activity `ExecuteMaxscript`.
In this step, you create an Alias named tutorial to point to this version of the Activity. An Alias always points to a specific version of an Activity.

To create an Alias:

### Request

```
curl -X POST \
    'https://developer.api.autodesk.com/da/us-east/v3/activities/ExecuteMaxscript/aliases' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
    -d '{
            "id": "tutorial",
            "version": 1
        }'

```

Show More

**Notes:**

- Pay special attention to the URI `https://developer.api.autodesk.com/da/us-east/v3/activites/{id}/aliases`. The URI contains the unqualified id of the Activity we created in the previous step to identify the Activity we created.
- For more information on qualified ids and unqualified ids, refer [Aliases and Ids](/en/docs/design-automation/v3/developers_guide/aliases-and-ids)

### Response

```
{
    "version": 1,
    "id": "tutorial"
}

```
