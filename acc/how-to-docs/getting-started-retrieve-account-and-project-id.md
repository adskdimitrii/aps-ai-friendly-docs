# Retrieve Forma Hub and Project ID

Source: https://aps.autodesk.com/en/docs/acc/tutorials/getting-started/retrieve-account-and-project-id/

---

# Retrieve Forma Hub and Project ID

This tutorial demonstrates how to obtain your Forma Hub and Project ID. If you already have these, you can skip this tutorial.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps), and select the Data Management and Forma APIs.
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:create` `data:read` and `data:write` scopes.
- Verify that you have access to the relevant Forma hub, project, and folder.

## [Step 1: Find the Hub ID for the Forma Hub](#step-1-find-the-hub-id-for-the-forma-hub)

Find the hub ID for the Forma hub you are interested in, by calling [GET hubs](../../data/http-docs/http-hubs-GET.md).

Note that the Forma hub ID corresponds to a Data Management hub ID. To convert an account ID into a hub ID you need to add a “**b.**" prefix. For example, an account ID of d952a4eb-ad57-4d64-b9ab-d540b3b4522e translates to a hub ID of **b.**d952a4eb-ad57-4d64-b9ab-d540b3b4522e.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/project/v1/hubs"

```

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": {
      "href": "https://developer.api.autodesk.com/project/v1/hubs"
    }
  },
  "data": [
    {
      "type": "hubs",
      "id": "b.d6cf8c84-c25e-4534-ae5c-62e08480e751",
      "attributes": {
        "name": "My First Hub",
        "extension": {
          "type": "hubs:autodesk.acc:Account",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/hubs:autodesk.acc:Account-1.0"
          },
          "data": {}
        }
      }
    }
  ]
}

```

Show More

In this example, assume that the hub that you are interested in is called `My First Hub`.

Find the hub (`data.name`), and note the hub ID - `b.d6cf8c84-c25e-4534-ae5c-62e08480e751`.

## [Step 2: Find the Project ID](#step-2-find-the-project-id)

To get a list of all the projects in the hub, use the hub ID (`b.d6cf8c84-c25e-4534-ae5c-62e08480e751`) to call [GET hubs/:hub_id/projects](../../data/http-docs/http-hubs-hub_id-projects-GET.md). Find the project ID of the project that you are interested in.

Note that the project ID in Forma corresponds to the project ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/). To convert a project ID in Forma to a project ID in the Data Management API, you need to add a “**b.**" prefix. For example, a project ID of a4be0c34a-4ab7 translates to a project ID of **b.**a4be0c34a-4ab7.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/project/v1/hubs/b.d6cf8c84-c25e-4534-ae5c-62e08480e751/projects"

```

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": {
      "href": "https://developer.api.autodesk.com/project/v1/hubs/b.d6cf8c84-c25e-4534-ae5c-62e08480e751/projects"
    }
  },
  "data": [
    {
      "type": "projects",
      "id": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
      "attributes": {
        "name": "My First Project",
        "extension": {
          "type": "projects:autodesk.core:Project",
          "version": "1.0"
        }
      }
    }
  ]
}

```

Show More

In this example, assume that `My First Project` is the project you are interested in.

Find the project (`data.attributes.name`), and note the project ID (`data.id`) - `f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`.
