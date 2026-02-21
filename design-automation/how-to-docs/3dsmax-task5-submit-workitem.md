# Task 5 - Submit a WorkItem

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/3dsmax/task5-submit-workitem/

---

# Task 5 - Submit a WorkItem

Submitting a WorkItem is the way to request the Automation Service to execute an Activity.
This is where you will specify the different input and output values required by the Activity.
You defined these inputs when you created the Activity during [Task 3](/en/docs/design-automation/v3/tutorials/3dsmax/task3-create-activity/). You obtained the signed URLs to the input and output locations in [Task 4](/en/docs/design-automation/v3/tutorials/3dsmax/task4-manage-cloud-storage).

By the end of this task, you will be able to create a WorkItem to execute an Activity.

You will use the following operations to work with WorkItems in this task:

| HTTP Request | Description |
| --- | --- |
| [POST /workitems](/en/docs/design-automation/v3/reference/http/workitems-POST) | Creates a new WorkItem and queues it for processing. |

## [Step 1 - Create a WorkItem](#step-1-create-a-workitem)

### Request

```
curl -X POST \
    'https://developer.api.autodesk.com/da/us-east/v3/workitems' \
    -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
    -H 'Content-Type: application/json' \
    -d '{
            "activityId":"<YOUR_NICKNAME>.ExecuteMaxscript+tutorial",
            "arguments":{
                "InputMaxScene":{
                    "url":"urn:adsk.objects:os.object:<YOUR_BUCKET_KEY>/<OBJECT_KEY_4_INPUT_ZIP_FILE>",
                    "pathInZip":"<RELATIVE_PATH_TO_MAX_SCENE_INSIDE_ZIP_FILE>",
                    "verb":"get",
                    "headers":{
                        "Authorization":"Bearer <YOUR_ACCESS_TOKEN>"
                    }
                },
                "MaxscriptToExecute":{
                    "url":"urn:adsk.objects:os.object:<YOUR_BUCKET_KEY>/<OBJECT_KEY_4_MAXSCRIPT_FILE>",
                    "verb":"get",
                    "headers":{
                        "Authorization":"Bearer <YOUR_ACCESS_TOKEN>"
                    }
                },
                "OutputZip":{
                    "url":"urn:adsk.objects:os.object:<YOUR_BUCKET_KEY>/<OBJECT_KEY_4_OUTPUT_FILE>",
                    "verb":"put",
                    "headers":{
                        "Authorization":"Bearer <YOUR_ACCESS_TOKEN>"
                    }
                }
            }
        }'

```

Show More

**Notes:**

- `activityId` is the fully qualified id to identify the Activity you created in [Task 3](/en/docs/design-automation/v3/tutorials/3dsmax/task3-create-activity). This id is created with 3 pieces as described [here](/en/docs/design-automation/v3/developers_guide/aliases-and-ids/).
- Replace the `pathInZip` values inside the `InputMaxScene` argument with the path to the 3ds Max scene file inside your zip file. If the 3ds Max file is at the root of your zip, simply specify the 3ds Max file name.
- If you do not wish to use a zip file to hold the 3ds Max scene, but prefer to use the 3ds Max scene itself, provide the URN of the scene file directly and remove the `pathInZip` attribute inside the `InputMaxScene` argument.

### Response

```
{
    "status": "pending",
    "stats": {
        "timeQueued": "2023-10-05T03:54:15.0618534Z"
    },
    "id": "<YOUR_WORKITEM_ID>"
}

```

**Notes:**

- Jot down the `id` in the response. This is the id that identifies your WorkItem. You will use this id in [Task 6](/en/docs/design-automation/v3/tutorials/3dsmax/task6-download-results).
