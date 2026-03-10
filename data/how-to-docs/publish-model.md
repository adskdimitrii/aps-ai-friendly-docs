# Publish a Cloud Workshared Revit Model to Next Gen BIM 360 Docs

Source: https://aps.autodesk.com/en/docs/data/v2/tutorials/publish-model/

---

# Publish a Cloud Workshared Revit Model to Next Gen BIM 360 Docs

This walkthrough demonstrates how to publish the latest synchronized Cloud Workshared Revit models to Next Gen BIM 360 Docs. Each time you publish a latest model to Next Gen BIM 360 Docs, you create a new version of the model. To publish the latest model, you need to first:

- [Initiate collaboration through Revit](https://knowledge.autodesk.com/support/collaboration-for-revit), and select BIM 360 Docs. This creates the first version in BIM 360 Docs.
- Modify the model locally, and [synchronize the changes with the central model](https://knowledge.autodesk.com/support/collaboration-for-revit/learn-explore/caas/video/youtube/watch-v-RMlxaygDaU8.html).

The steps of the walkthrough include finding the ID of the model that you want to update in BIM 360 Docs, publishing the model to BIM 360 Docs, and verifying that the model has finished publishing.

## [Before You Begin](#before-you-begin)

- Acquire a subscription to [BIM 360 Design](https://info.bim360.autodesk.com/bim-360-design). Note that anyone subscribed to Revit Collaboration Suite is automatically granted access to BIM 360 Design.
- [Register an app](https://aps.autodesk.com/myapps), and select the Data Management, BIM 360, and Webhooks APIs.
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:create` `data:read` and `data:write` scopes.
- Verify that you have access to the relevant BIM 360 Docs folder.

## [Step 1: Find the Hub ID for the BIM 360 Account](#step-1-find-the-hub-id-for-the-bim-360-account)

The first few steps of the walkthrough demonstrate how to iterate through several Data Management endpoints to find the ID of the cloud workshared Revit model you want to update.

Call [GET hubs](../http-docs/http-hubs-GET.md) to find the hub ID for the BIM 360 account that contains the model you want to update .

In this example, assume that the model you want to update is in a hub called `DemoAccount`.

Note that the response payloads have been simplified.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/project/v1/hubs?filter[attributes.name]=DemoAccount"

```

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": {
      "href": "https://developer.api.autodesk.com/project/v1/hubs?filter[attributes.name]=DemoAccount"
    }
  },
  "data": [
    {
      "type": "hubs",
      "id": "b.ddde928d-b610-4b18-b43d-2915ad438a84",
      "attributes": {
        "name": "DemoAccount",
        "extension": {
          "type": "hubs:autodesk.bim360:Account",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/hubs:autodesk.bim360:Account-1.0"
          },
          "data": {}
        }
      }
    }
  ]
}

```

Show More

Find the hub (`data.attributes.name`), and note the hub ID - `b.ddde928d-b610-4b18-b43d-2915ad438a84`.

## [Step 2: Find the project ID](#step-2-find-the-project-id)

Use the hub ID (`b.ddde928d-b610-4b18-b43d-2915ad438a84`) to call [GET hubs/:hub_id/projects](../http-docs/http-hubs-hub_id-projects-GET.md) to get the ID of the project that contains the model you want to update.

In this example, assume that the model you want to update is in a project called `DemoProject`.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/project/v1/hubs/b.ddde928d-b610-4b18-b43d-2915ad438a84/projects?filter[attributes.name]=DemoProject"

```

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": {
      "href": "https://developer.api.autodesk.com/project/v1/hubs/b.ddde928d-b610-4b18-b43d-2915ad438a84/projects?filter[attributes.name]=DemoProject"
    }
  },
  "data": [
    {
      "type": "projects",
      "id": "b.c8112490-4e08-435c-994b-64fe60fea507",
      "attributes": {
        "name": "DemoProject",
        "extension": {
          "type": "projects:autodesk.bim360:Project",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/projects:autodesk.bim360:Project-1.0"
          },
          "data": {}
        }
      }
    }
  ]
}

```

Show More

Find the project (`data.attributes.name`), and note the project ID (`data.id`) - `b.c8112490-4e08-435c-994b-64fe60fea507`.

## [Step 3: Find the Project Files Folder ID](#step-3-find-the-project-files-folder-id)

Use the hub ID (`b.ddde928d-b610-4b18-b43d-2915ad438a84`) and the project ID (`b.c8112490-4e08-435c-994b-64fe60fea507`) to call [GET hubs/:hub_id/projects/:project_id/topFolders](../http-docs/http-hubs-hub_id-projects-project_id-topFolders-GET.md) to get the Project Files folder ID.

Note that you can only publish the latest synchronized cloud workshared Revit models to the BIM 360 Project Files folder or to a folder nested under the Project Files folder.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT"
            "https://developer.api.autodesk.com/project/v1/hubs/b.ddde928d-b610-4b18-b43d-2915ad438a84/projects/b.c8112490-4e08-435c-994b-64fe60fea507/topFolders"

```

### Response

```
{
  "jsonapi": {
      "version": "1.0"
   },
  },
  "data": [
      {
          "type": "folders",
          "id": "urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA",
          "attributes": {
              "name": "Project Files",
              "displayName": "Project Files",
              "createTime": "2017-06-13T05:16:18.0000000Z",
              "createUserId": "38SCJGX4R4PV",
              "createUserName": "John Doe",
              "lastModifiedTime": "2018-02-22T17:51:11.0000000Z",
              "lastModifiedUserId": "38SCJGX4R4PV",
              "lastModifiedUserName": "John Doe",
              "lastModifiedTimeRollup": "2018-02-22T17:58:36.0000000Z",
              "objectCount": 4,
              "hidden": false,
              "extension": {
                  "type": "folders:autodesk.bim360:Folder",
                  "version": "1.0",
                  "schema": {
                      "href": "https://developer.api.autodesk.com/schema/v1/versions/folders:autodesk.bim360:Folder-1.0"
                  },
             }
         }
}

```

Show More

Find the Project Files folder (`data.attributes.name`), and note the folder ID (`data.id`) - `urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA`

In this example, assume that the model you want to update is in the Project Files folder.

Note that if you want to publish the document to a folder nested under the Project Files folder, you need to call [GET projects/:project_id/folders/:folder_id/contents](../http-docs/http-projects-project_id-folders-folder_id-contents-GET.md) repeatedly through the hierarchy of folders until you find the Folder ID of the folder that contains the model you want to update. For the first iteration, use the Project Files ID (`urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA`).

## [Step 4: Find the Item ID of the Cloud Workshared Model](#step-4-find-the-item-id-of-the-cloud-workshared-model)

Use the project ID (`b.c8112490-4e08-435c-994b-64fe60fea507`) and the folder ID (`urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA`) to call [GET projects/:project_id/folders/:folder_id/contents](../http-docs/http-projects-project_id-folders-folder_id-contents-GET.md) to get the ID of the model (item) you want to update.

Use the `items:autodesk.bim360:C4RModel` filter to filter out non-cloud workshared Revit files.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/data/v1/projects/b.c8112490-4e08-435c-994b-64fe60fea507/folders/urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA/contents?filter[attributes.extension.type]=items%3Aautodesk.bim360%3AC4RModel"

```

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": {
      "href": "https://developer.api.autodesk.com/data/v1/projects/b.c8112490-4e08-435c-994b-64fe60fea507/folders/urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA/contents?filter[attributes.extension.type]=items:autodesk.bim360:C4RModel"
    }
  },
  "data": [
    {
      "type": "items",
      "id": "urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q",
      "attributes": {
        "displayName": "DemoModel",
        "createTime": "2018-02-22T17:51:11.0000000Z",
        "createUserId": "38SCJGX4R4PV",
        "createUserName": "John Doe",
        "lastModifiedTime": "2018-02-22T17:58:36.0000000Z",
        "lastModifiedUserId": "38SCJGX4R4PV",
        "lastModifiedUserName": "John Doe",
        "hidden": false,
        "reserved": false,
        "extension": {
          "type": "items:autodesk.bim360:C4RModel",
          "version": "1.0.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/items:autodesk.bim360:C4RModel-1.0.0"
          },
          "data": {}
        }
      }
    }
  ],
  "included": [
    {
      "type": "versions",
      "id": "urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q?version=3",
      "attributes": {
        "name": "DemoModel.rvt",
        "displayName": "DemoModel",
        "createTime": "2018-02-22T17:57:43.0000000Z",
        "createUserId": "38SCJGX4R4PV",
        "createUserName": "John Doe",
        "lastModifiedTime": "2018-02-22T17:58:37.0000000Z",
        "lastModifiedUserId": "38SCJGX4R4PV",
        "lastModifiedUserName": "John Doe",
        "versionNumber": 3,
        "mimeType": "application/vnd.autodesk.r360",
        "fileType": "rvt",
        "extension": {
          "type": "versions:autodesk.bim360:C4RModel",
          "version": "1.1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/versions:autodesk.bim360:C4RModel-1.1.0"
          },
        }
      }
    }
  ]
}

```

Show More

In this example, assume that the model you want to update is called `DemoModel`.

Find the model (`data[i].attributes.displayName`), and note the item ID (`data.id`) - `urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q`.

## [Step 5: (Optional) Verify Whether a Model Needs to Be Published](#step-5-optional-verify-whether-a-model-needs-to-be-published)

Use the project ID (`b.c8112490-4e08-435c-994b-64fe60fea507`) and item ID of the model (`urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q`) to call the [GetPublishModelJob](../http-docs/http-GetPublishModelJob.md) command to verify whether a model needs to be published.

Every time you [synchronize the current model](https://knowledge.autodesk.com/support/collaboration-for-revit/learn-explore/caas/video/youtube/watch-v-RMlxaygDaU8.html) with the central model, it sets the `data` attribute of the [GetPublishModelJob](../http-docs/http-GetPublishModelJob.md) command to `null`. When you publish the latest version to BIM 360 Docs (using the [PublishModel](../http-docs/http-PublishModel.md) command or the [PublishWithoutLinks](../http-docs/http-PublishWithoutLinks.md) command), it sets the status to `processing` or `complete`.

You can use this command to find out whether the model in BIM 360 Docs is the latest version, or whether it needs to be published.

### Request

```
  curl -X POST -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/data/v1/projects/b.c8112490-4e08-435c-994b-64fe60fea507/commands" -H 'content-type: application/vnd.api+json' -d '
{
  "jsonapi": {
  "version": "1.0"
  },
  "data": {
  "type": "commands",
  "attributes": {
    "extension": {
      "type": "commands:autodesk.bim360:C4RModelGetPublishJob",
      "version": "1.0.0"
    }
  },
  "relationships": {
    "resources": {
      "data": [ { "type": "items", "id": "urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q" } ]
    }
  }
  }
}'

```

Show More

### Response

If you have updated the central model, the `data` attribute is set to `null` until you publish it.

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "data": null
}

```

If you have published the latest version, the `status` attribute is set to `processing` or `complete`.

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "data": {
    "type": "commands",
    "id": "971ee7a6-5737-483a-bc64-31a88aae09b3_3_636549189940000000",
    "attributes": {
      "status": "complete",
      "extension": {
        "type": "commands:autodesk.bim360:C4RModelGetPublishJob",
        "version": "1.0.0"
      }
    }
  }
}

```

Show More

## [Step 6: Publish the Latest Version of the Model to BIM 360 Docs](#step-6-publish-the-latest-version-of-the-model-to-bim-360-docs)

Use the project ID (`b.c8112490-4e08-435c-994b-64fe60fea507`) and item ID (`urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q`) to call the [PublishModel](../http-docs/http-PublishModel.md) command to publish the latest version of the model to BIM 360 Docs or the [PublishWithoutLinks](../http-docs/http-PublishWithoutLinks.md) command to publish the latest version of the model without the links it contains to BIM 360 Docs.

Note that you do not need to create an empty storage object when publishing a model using the PublishModel command or PublishModelWithoutLinks command.

### Request PublishModel command

```
  curl -X POST -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/data/v1/projects/b.c8112490-4e08-435c-994b-64fe60fea507/commands" -H 'content-type: application/vnd.api+json' -d '
{
  "jsonapi": {
  "version": "1.0"
  },
  "data": {
  "type": "commands",
  "attributes": {
    "extension": {
      "type": "commands:autodesk.bim360:C4RModelPublish",
      "version": "1.0.0"
      }
    },
  "relationships": {
    "resources": {
      "data": [ { "type": "items", "id": "urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q" } ]
    }
  }
  }
}'

```

Show More

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "data": {
    "type": "commands",
    "id": "971ee7a6-5737-483a-bc64-31a88aae09b3_3_636549189940000000",
    "attributes": {
      "status": "committed",
      "extension": {
        "type": "commands:autodesk.bim360:C4RModelPublish",
        "version": "1.0.0"
      }
    }
  }
}

```

Show More

### Request PublishWithoutLinks command

```
  curl -X POST -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/data/v1/projects/b.c8112490-4e08-435c-994b-64fe60fea507/commands" -H 'content-type: application/vnd.api+json' -d '
{
  "jsonapi": {
  "version": "1.0"
  },
  "data": {
  "type": "commands",
  "attributes": {
    "extension": {
      "type": "commands:autodesk.bim360:C4RPublishWithoutLinks",
      "version": "1.0.0"
      }
    },
  "relationships": {
    "resources": {
      "data": [ { "type": "items", "id": "urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q" } ]
    }
  }
  }
}'

```

Show More

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "data": {
    "type": "commands",
    "id": "971ee7a6-5737-483a-bc64-31a88aae09b3_3_636549189940000000",
    "attributes": {
      "status": "committed",
      "extension": {
        "type": "commands:autodesk.bim360:C4RPublishWithoutLinks",
        "version": "1.0.0"
      }
    }
  }
}

```

Show More

## [Step 7: Verify the Model Has Finished Publishing](#step-7-verify-the-model-has-finished-publishing)

The [PublishModel](../http-docs/http-PublishModel.md) and [PublishWithoutLinks](../http-docs/http-PublishWithoutLinks.md) commands are asynchronous and initiate a job that runs in the background, rather than halting execution of your program. When the model has finished publishing to BIM 360 Docs, a new version of the model is created. There are two ways that you can track the job’s progress:

### a) Manually Poll for the Status

Use the project ID (`b.c8112490-4e08-435c-994b-64fe60fea507`) and item ID (`urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q`) to iteratively call [GET projects/:project_id/items/:item_id](../http-docs/http-projects-project_id-items-item_id-GET.md), which returns the extraction status of the latest (tip) version of the model.

When `included[i].data.extractState` is set to `SUCCESS`, the model has finished publishing.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/data/v1/projects/b.c8112490-4e08-435c-994b-64fe60fea507/items/urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q"

```

### Request

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": {
      "href": "https://developer.api.autodesk.com/data/v1/projects/b.c8112490-4e08-435c-994b-64fe60fea507/items/urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q"
    }
  },
  "data": {
    "type": "items",
    "id": "urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q",
    "attributes": {
      "displayName": "DemoModel",
      "createTime": "2018-02-22T17:51:11.0000000Z",
      "createUserId": "38SCJGX4R4PV",
      "createUserName": "John Doe",
      "lastModifiedTime": "2018-02-23T14:19:58.0000000Z",
      "lastModifiedUserId": "38SCJGX4R4PV",
      "lastModifiedUserName": "John Doe",
      "hidden": false,
      "reserved": false,
      "extension": {
        "type": "items:autodesk.bim360:C4RModel",
        "version": "1.0.0",
        "schema": {
          "href": "https://developer.api.autodesk.com/schema/v1/versions/items:autodesk.bim360:C4RModel-1.0.0"
        },
        "data": {}
      }
    }
  },
  "included": [
    {
      "type": "versions",
      "id": "urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q?version=4",
      "attributes": {
        "name": "DemoModel.rvt",
        "displayName": "DemoModel",
        "createTime": "2018-02-23T14:19:04.0000000Z",
        "createUserId": "38SCJGX4R4PV",
        "createUserName": "John Doe",
        "lastModifiedTime": "2018-02-23T14:19:59.0000000Z",
        "lastModifiedUserId": "38SCJGX4R4PV",
        "lastModifiedUserName": "John Doe",
        "versionNumber": 4,
        "mimeType": "application/vnd.autodesk.r360",
        "fileType": "rvt",
        "extension": {
          "type": "versions:autodesk.bim360:C4RModel",
          "version": "1.1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/versions:autodesk.bim360:C4RModel-1.1.0"
          },
          "data": {
            "modelVersion": 4,
            "projectGuid": "cb5b9d79-a68a-4d35-adf6-dc824248f698",
            "originalItemUrn": "urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q",
            "isCompositeDesign": false,
            "modelType": "multiuser",
            "latestEpisodeGuid": "bb57cf74-0e5c-459c-9271-5b421f9fc886",
            "mimeType": "application/vnd.autodesk.r360",
            "modelGuid": "971ee7a6-5737-483a-bc64-31a88aae09b3",
            "compositeParentFile": "",
            "processState": "PROCESSING_COMPLETE",
            "extractionState": "SUCCESS",
            "splittingState": "NOT_SPLIT",
            "reviewState": "NOT_IN_REVIEW",
            "revisionDisplayLabel": "4"
          }
        }
      }
    }
  ]
}

```

Show More

### b) Set up Automatic Notifications

You can also track the job’s progress by setting up [webhooks](https://aps.autodesk.com/en/docs/webhooks/v1/overview/) to send automatic notifications whenever the folder that you published the model to is updated.

[Register the webhook](../../webhooks/how-to-docs/create-a-hook-data-management.md) (`scope.folder`) to the Project Files folder (`urn:adsk.wipprod:fs.folder:co.BJU3PTc4Sd2CmXM492XUiA`), and set up notifications to be triggered when a file is modified (`dm.version.modified`) in the folder.

Every time a file in the folder is modified, you receive details about the event.

```
{
  "version": "1.0",
  "resourceUrn": "urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q%3Fversion=4",
  "hook": {
  "system": "data",
  "event": "dm.version.modified",
  "hookId": "1fcd3e30-9f3f-11e7-951f-0fd5337ed5ce",
  "tenant": "urn:adsk.wipprod:fs.folder:co.s424tpjyS_yYBs5ozch94g",
  "callbackUrl": "http://bf067e05.ngrok.io/callback",
  "createdBy": "************",
  "createdDate": "2017-09-22T02:38:32.341+0000",
  "creatorType": "Application",
  "hookAttribute": {
    "myfoo": 34,
    "projectId": "someURN",
    "myobject": {
    "nested": true
    }
  },
  "scope": {
    "folder": "urn:adsk.wipprod:fs.folder:co.s424tpjyS_yYBs5ozch94g"
  },
  "urn": "urn:adsk.webhooks:events.hook:1fcd3e30-9f3f-11e7-951f-0fd5337ed5ce",
  "status": "active",
  "__self__": "/systems/data/events/dm.version.modified/hooks/1fcd3e30-9f3f-11e7-951f-0fd5337ed5ce"
  },
  "payload": {
  "ext": "txt",
  "modifiedTime": "2017-09-06T03:04:48+0000",
  "lineageUrn": "urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q",
  "sizeInBytes": 36,
  "hidden": false,
  "indexable": true,
  "project": "4f8b8b74-3853-473d-85c4-4e8a8bff885b",
  "source": "urn:adsk.wipprod:fs.file:vf.hPW2BlBbQG2L5HjCOh7Z8Q?version=1",
  "modification_flags": "{\"newVersion\":false,\"accessDefOrScopeChange\":false,\"metadataOnly\":true}",
  "version": "1",
  "contentURL": "urn:adsk.objects:os.object:wip.dm.qa/3bbfde79-aae5-47e5-a7d0-364d5471ab74.txt",
  "user_info": {
    "id": "*************"
  },
  "name": "0854da0c-4131-4080-bb5e-a7d764e7a24b.txt",
  "modifiedBy": "*************",
  "state": "CONTENT_AVAILABLE",
  "parentFolderUrn": "urn:adsk.wipprod:fs.folder:co.chOa5mlkR6mjN-PEx8-r8Q",

```

Show More

Note the item ID, i.e., `lineageURN` - `urn:adsk.wipprod:dm.lineage:hPW2BlBbQG2L5HjCOh7Z8Q`. If it is a cloud workshared Revit model that you published, use it to call [GET projects/:project_id/items/:item_id](../http-docs/http-projects-project_id-items-item_id-GET.md), which returns the extraction status of the latest (tip) version of the model.

When `included[i].data.extractState` is set to `SUCCESS`, the model has finished publishing.
