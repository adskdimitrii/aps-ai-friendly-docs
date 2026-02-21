# Task 4 â Publish an Activity

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/fusion/task4-publish-activity/

---

# Task 4 â Publish an Activity

An Activity is an action that can be executed in the Automation Service. You create and post Activities to run specific AppBundles.

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

To create a new Activity named ConfigureDesignActivity, post this request:

### Request

```
curl -X POST \
  'https://developer.api.autodesk.com/da/us-east/v3/activities' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  -d '{
        "id": "ConfigureDesignActivity",
        "engine": "Autodesk.Fusion+Latest",
        "commandline": [],
        "parameters": {
            "TaskParameters": {
                "verb": "read",
                "description": "the parameters for the script",
                "required": false
            },
            "PersonalAccessToken": {
                "verb": "read",
                "description": "the personal access token to use",
                "required": true
            }
        },
        "appbundles": [
            "YOUR_NICKNAME.ConfigureDesignAppBundle+my_working_version"
        ],
        "settings": {},
        "description": ""
    }'

```

Show More

| Attribute | Description |
| --- | --- |
| `id` | The name given to your new Activity. |
| `engine` | The engine on which your Activity runs. The available engine versions are described in the Additional notes section in [Task 3](/en/docs/design-automation/v3/tutorials/fusion/task3-upload-appbundle#additional-notes) |
| `appbundles` | The fully qualified id of the AppBundle. |

### Response

```
{
  "id": "<YOUR_NICKNAME>.ConfigureDesignActivity",
  "engine": "Autodesk.Fusion+Latest",
  "appbundles": [
      "<YOUR_NICKNAME>.ConfigureDesignAppBundle+my_working_version"
  ],
  "settings": {},
  "description": "",
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

To create an alias named `current_version`, which refers to version `1` of the `ConfigureDesignActivity`:

### Request

```
curl -X POST \
  'https://developer.api.autodesk.com/da/us-east/v3/activities/ConfigureDesignActivity/aliases' \
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
  'https://developer.api.autodesk.com/da/us-east/v3/activities/ConfigureDesignActivity/versions' \
  -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": null,
    "engine": "Autodesk.Fusion+Latest",
    "appbundles": [
        "<YOUR_NICKNAME>.ConfigureDesignActivity+my_working_version"
    ],
    "settings": {},
    "description": ""
}'

```

Show More

**Note:** You can omit `id` from the request body. If you include `id` in the request body, set it to `null`. If you donât set it to `null`, the Automation Service throws an error.

### Response

```
{
    "id": "YOUR_NICKNAME.ConfigureDesignActivity",
    "engine": "Autodesk.Fusion+Latest",
    "appbundles": [
        "YOUR_NICKNAME.ConfigureDesignActivity+my_working_version"
    ],
    "settings": {},
    "description": "",
    "version": 2
}

```

Show More

## [Step 4 - Assign an existing alias to the updated Activity](#step-4-assign-an-existing-alias-to-the-updated-activity)

**NOTE: Perform this step only if you carried out Step 3**

Currently, the alias *current_version* points to version 1 of the Activity.

| id | alias | version |
| --- | --- | --- |
| ConfigureDesignActivity | current_version | 1 |
| ConfigureDesignActivity |  | 2 |

You can reassign the alias *current_version* to point to version 2 of the Activity.

| id | alias | version |
| --- | --- | --- |
| ConfigureDesignActivity |  | 1 |
| ConfigureDesignActivity | current_version | 2 |

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
