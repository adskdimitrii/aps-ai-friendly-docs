# Create an Attachment

Source: https://aps.autodesk.com/en/docs/data/v2/tutorials/create-attachment/

---

# Create an Attachment

This walkthrough explains how to attach one version of a file to another. The pre-requisite is to have two of your files uploaded to the âdataâ domain service. This can be done using A360 or the Data Management API. For details on the latter see
the [Upload a File](/en/docs/data/v2/tutorials/upload-file/) walkthrough.

## [Before You Begin](#before-you-begin)

Make sure that you have [registered an app](/en/docs/oauth/v2/tutorials/create-app) and successfully [acquired an OAuth token](/en/docs/oauth/v2/tutorials).

See the Authentication and Scopes section in the [API Basics](/en/docs/data/v2/overview/basics) for the appropriate token based on the data you are accessing.

In general, access to BIM 360 Team, BIM 360 Docs, Fusion Team, and A360 Personal data requires the use of a [3-legged OAuth2 token](/en/docs/oauth/v2/tutorials/get-3-legged-token).

HTTP `GET` requests to the Project and Data services require the `data:read` scope.

HTTP `POST` requests to the Data service require the `data:create` scope, but can also be called with the `data:write` scope.

## [Step 1: Create an attachment](#step-1-create-an-attachment)

Suppose you have an Excel spreadsheet you want to attach to a DWG file, version 2 to version 2 respectively. For this example, letâs assume the DWGâs version ID is `urn:adsk.wipprod:fs.file:vf.J_9fiaqVSa-GSc88OErcAg?version=2` and the spreadsheetâs is `urn:adsk.wipprod:fs.file:vf.ooWjwAQJR0uEoPRyfEnvew?version=2`. Also, the project these files reside in has the ID, `a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2`.

The [POST projects/:project_id/version/:version_id/relationships/refs](/en/docs/data/v2/reference/http/projects-project_id-versions-version_id-relationships-refs-POST) endpoint can create a custom relationship between the two versions which represents a file attachment. Notice the extension type comes from the Autodesk Schema Service, where the ref type is `auxiliary` and the extension type is `autodesk.core:Attachment`.

For more information about custom relationships, see the corresponding section in the [API Basics](/en/docs/data/v2/overview/basics).

### Example

```
curl -X POST -H "Authorization: Bearer 2wlSxqoUimJT3snKbaDg5HiV2Aam" -H "Accept: application/vnd.api+json" -H "Content-Type: application/vnd.api+json" -d
'{
  "jsonapi": {
    "version": "1.0"
  },
  "data": {
    "type": "versions",
    "id": "urn:adsk.wipprod:fs.file:vf.ooWjwAQJR0uEoPRyfEnvew?version=2",
    "meta": {
      "extension": {
        "type": "auxiliary:autodesk.core:Attachment",
        "version": "1.0"
      }
    }
  }
}' "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/versions/urn:adsk.wipprod:fs.file:vf.J_9fiaqVSa-GSc88OErcAg%3Fversion%3D2/relationships/refs"

```

Show More

On success, the endpoint returns a 204 (No Content).

## [Step 2: Retrieve attachments for a file](#step-2-retrieve-attachments-for-a-file)

The [GET projects/:project_id/version/:version_id/relationships/refs](/en/docs/data/v2/reference/http/projects-project_id-versions-version_id-relationships-refs-GET) endpoint can also be used to retrieve the custom relationships for a version. Notice the response includes the attachment that was created in the previous step.

### Example

```
curl -X GET -H "Authorization: Bearer 2wlSxqoUimJT3snKbaDg5HiV2Aam" "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/versions/urn:adsk.wipprod:fs.file:vf.J_9fiaqVSa-GSc88OErcAg%3Fversion%3D2/relationships/refs"

```

The resource provides the following response:

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": {
      "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/versions/urn:adsk.wipprod:fs.file:vf.J_9fiaqVSa-GSc88OErcAg?version=2/relationships/refs"
    },
    "related": {
      "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/versions/urn:adsk.wipprod:fs.file:vf.J_9fiaqVSa-GSc88OErcAg?version=2/refs"
    }
  },
  "data": [
    {
      "type": "versions",
      "id": "urn:adsk.wipprod:fs.file:vf.ooWjwAQJR0uEoPRyfEnvew?version=2",
      "meta": {
        "refType": "auxiliary",
        "fromId": "urn:adsk.wipprod:fs.file:vf.J_9fiaqVSa-GSc88OErcAg?version=2",
        "fromType": "versions",
        "toId": "urn:adsk.wipprod:fs.file:vf.ooWjwAQJR0uEoPRyfEnvew?version=2",
        "toType": "versions",
        "direction": "from",
        "extension": {
          "type": "auxiliary:autodesk.core:Attachment",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/auxiliary%3Aautodesk.core%3AAttachment-1.0"
          },
          "data": {}
        }
      }
    }
  ],
  "included": [
    {
      "type": "items",
      "id": "urn:adsk.wipprod:dm.lineage:ooWjwAQJR0uEoPRyfEnvew",
      "attributes": {
        "displayName": "proposal_cost_breakdown.xls",
        "createTime": "2016-05-17T15:15:58+00:00",
        "createUserId": "KPN8P8P65K7K",
        "createUserName": "John Doe",
        "lastModifiedTime": "2016-05-17T15:15:58+00:00",
        "lastModifiedUserId": "KPN8P8P65K7K",
        "lastModifiedUserName": "John Doe",
        "extension": {
          "type": "items:autodesk.core:File",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/items%3Aautodesk.core%3AFile-1.0"
          },
          "data": {}
        }
      },
      "links": {
        "self": {
          "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/items/urn:adsk.wipprod:dm.lineage:ooWjwAQJR0uEoPRyfEnvew"
        }
      },
      "relationships": {
        "tip": {
          "data": {
            "type": "versions",
            "id": "urn:adsk.wipprod:fs.file:vf.ooWjwAQJR0uEoPRyfEnvew?version=2"
          },
          "links": {
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/items/urn:adsk.wipprod:dm.lineage:ooWjwAQJR0uEoPRyfEnvew/tip"
            }
          }
        },
        "versions": {
          "links": {
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/items/urn:adsk.wipprod:dm.lineage:ooWjwAQJR0uEoPRyfEnvew/versions"
            }
          }
        },
        "parent": {
          "data": {
            "type": "folders",
            "id": "urn:adsk.wipprod:fs.folder:co.pulk3AL9SN2nbH5qhblgkg"
          },
          "links": {
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/items/urn:adsk.wipprod:dm.lineage:ooWjwAQJR0uEoPRyfEnvew/parent"
            }
          }
        },
        "refs": {
          "links": {
            "self": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/items/urn:adsk.wipprod:dm.lineage:ooWjwAQJR0uEoPRyfEnvew/relationships/refs"
            },
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/items/urn:adsk.wipprod:dm.lineage:ooWjwAQJR0uEoPRyfEnvew/refs"
            }
          }
        }
      }
    },
    {
      "type": "items",
      "id": "urn:adsk.wipprod:dm.lineage:J_9fiaqVSa-GSc88OErcAg",
      "attributes": {
        "displayName": "warehouse.dwg",
        "createTime": "2016-05-24T23:13:27+00:00",
        "createUserId": "KPN8P8P65K7K",
        "createUserName": "John Doe",
        "lastModifiedTime": "2016-05-24T23:13:27+00:00",
        "lastModifiedUserId": "KPN8P8P65K7K",
        "lastModifiedUserName": "John Doe",
        "extension": {
          "type": "items:autodesk.core:File",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/items%3Aautodesk.core%3AFile-1.0"
          },
          "data": {}
        }
      },
      "links": {
        "self": {
          "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/items/urn:adsk.wipprod:dm.lineage:J_9fiaqVSa-GSc88OErcAg"
        }
      },
      "relationships": {
        "tip": {
          "data": {
            "type": "versions",
            "id": "urn:adsk.wipprod:fs.file:vf.J_9fiaqVSa-GSc88OErcAg?version=2"
          },
          "links": {
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/items/urn:adsk.wipprod:dm.lineage:J_9fiaqVSa-GSc88OErcAg/tip"
            }
          }
        },
        "versions": {
          "links": {
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/items/urn:adsk.wipprod:dm.lineage:J_9fiaqVSa-GSc88OErcAg/versions"
            }
          }
        },
        "parent": {
          "data": {
            "type": "folders",
            "id": "urn:adsk.wipprod:fs.folder:co.HO8p9IwESSq49XJgw85WKQ"
          },
          "links": {
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/items/urn:adsk.wipprod:dm.lineage:J_9fiaqVSa-GSc88OErcAg/parent"
            }
          }
        },
        "refs": {
          "links": {
            "self": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/items/urn:adsk.wipprod:dm.lineage:J_9fiaqVSa-GSc88OErcAg/relationships/refs"
            },
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/items/urn:adsk.wipprod:dm.lineage:J_9fiaqVSa-GSc88OErcAg/refs"
            }
          }
        }
      }
    },
    {
      "type": "versions",
      "id": "urn:adsk.wipprod:fs.file:vf.ooWjwAQJR0uEoPRyfEnvew?version=2",
      "attributes": {
        "name": "proposal_cost_breakdown.xls",
        "displayName": "proposal_cost_breakdown.xls",
        "createTime": "2016-05-17T15:15:58+00:00",
        "createUserId": "KPN8P8P65K7K",
        "createUserName": "John Doe",
        "lastModifiedTime": "2016-05-17T15:15:58+00:00",
        "lastModifiedUserId": "KPN8P8P65K7K",
        "lastModifiedUserName": "John Doe",
        "versionNumber": 1,
        "mimeType": "application/others",
        "fileType": "others",
        "storageSize": 7969,
        "extension": {
          "type": "versions:autodesk.core:File",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/versions%3Aautodesk.core%3AFile-1.0"
          },
          "data": {}
        }
      },
      "links": {
        "self": {
          "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/versions/urn:adsk.wipprod:fs.file:vf.ooWjwAQJR0uEoPRyfEnvew%3Fversion%3D2"
        }
      },
      "relationships": {
        "item": {
          "data": {
            "type": "items",
            "id": "urn:adsk.wipprod:dm.lineage:ooWjwAQJR0uEoPRyfEnvew"
          },
          "links": {
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/versions/urn:adsk.wipprod:fs.file:vf.ooWjwAQJR0uEoPRyfEnvew%3Fversion%3D2/item"
            }
          }
        },
        "refs": {
          "links": {
            "self": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/versions/urn:adsk.wipprod:fs.file:vf.ooWjwAQJR0uEoPRyfEnvew%3Fversion%3D2/relationships/refs"
            },
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/versions/urn:adsk.wipprod:fs.file:vf.ooWjwAQJR0uEoPRyfEnvew%3Fversion%3D2/refs"
            }
          }
        },
        "derivatives": {
          "data": {
            "type": "derivatives",
            "id": "dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYub29XandBUUpSMHVFb1BSeWZFbnZldz92ZXJzaW9uPTE"
          },
          "meta": {
            "link": {
              "href": "https://developer.api.autodesk.com/viewingservice/v1/dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYub29XandBUUpSMHVFb1BSeWZFbnZldz92ZXJzaW9uPTE"
            }
          }
        },
        "thumbnails": {
          "data": {
            "type": "thumbnails",
            "id": "dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYub29XandBUUpSMHVFb1BSeWZFbnZldz92ZXJzaW9uPTE"
          },
          "meta": {
            "link": {
              "href": "https://developer.api.autodesk.com/viewingservice/v1/thumbnails/dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYub29XandBUUpSMHVFb1BSeWZFbnZldz92ZXJzaW9uPTE"
            }
          }
        },
        "storage": {
          "data": {
            "type": "objects",
            "id": "urn:adsk.objects:os.object:wip.dm.prod/5a60c0c9-5347-4750-b394-d64d4853ea5c.xls"
          },
          "meta": {
            "link": {
              "href": "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/5a60c0c9-5347-4750-b394-d64d4853ea5c.xls"
            }
          }
        }
      }
    },
    {
      "type": "versions",
      "id": "urn:adsk.wipprod:fs.file:vf.J_9fiaqVSa-GSc88OErcAg?version=2",
      "attributes": {
        "name": "warehouse.dwg",
        "displayName": "warehouse.dwg",
        "createTime": "2016-05-24T23:13:27+00:00",
        "createUserId": "KPN8P8P65K7K",
        "createUserName": "John Doe",
        "lastModifiedTime": "2016-05-24T23:13:27+00:00",
        "lastModifiedUserId": "KPN8P8P65K7K",
        "lastModifiedUserName": "John Doe",
        "versionNumber": 1,
        "mimeType": "application/vnd.autodesk.autocad.dwg",
        "fileType": "dwg",
        "storageSize": 475304,
        "extension": {
          "type": "versions:autodesk.core:File",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/versions%3Aautodesk.core%3AFile-1.0"
          },
          "data": {}
        }
      },
      "links": {
        "self": {
          "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/versions/urn:adsk.wipprod:fs.file:vf.J_9fiaqVSa-GSc88OErcAg%3Fversion%3D2"
        }
      },
      "relationships": {
        "item": {
          "data": {
            "type": "items",
            "id": "urn:adsk.wipprod:dm.lineage:J_9fiaqVSa-GSc88OErcAg"
          },
          "links": {
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/versions/urn:adsk.wipprod:fs.file:vf.J_9fiaqVSa-GSc88OErcAg%3Fversion%3D2/item"
            }
          }
        },
        "refs": {
          "links": {
            "self": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/versions/urn:adsk.wipprod:fs.file:vf.J_9fiaqVSa-GSc88OErcAg%3Fversion%3D2/relationships/refs"
            },
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.YnVzaW5lc3M6YXV0b2Rlc2sxODcjMjAxNjA1MTcxMjgwOTc2/versions/urn:adsk.wipprod:fs.file:vf.J_9fiaqVSa-GSc88OErcAg%3Fversion%3D2/refs"
            }
          }
        },
        "derivatives": {
          "data": {
            "type": "derivatives",
            "id": "dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuSl85ZmlhcVZTYS1HU2M4OE9FcmNBZz92ZXJzaW9uPTE"
          },
          "meta": {
            "link": {
              "href": "https://developer.api.autodesk.com/viewingservice/v1/dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuSl85ZmlhcVZTYS1HU2M4OE9FcmNBZz92ZXJzaW9uPTE"
            }
          }
        },
        "thumbnails": {
          "data": {
            "type": "thumbnails",
            "id": "dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuSl85ZmlhcVZTYS1HU2M4OE9FcmNBZz92ZXJzaW9uPTE"
          },
          "meta": {
            "link": {
              "href": "https://developer.api.autodesk.com/viewingservice/v1/thumbnails/dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuSl85ZmlhcVZTYS1HU2M4OE9FcmNBZz92ZXJzaW9uPTE"
            }
          }
        },
        "storage": {
          "data": {
            "type": "objects",
            "id": "urn:adsk.objects:os.object:wip.dm.prod/9c169b42-5893-442b-80f5-34b25680ef34.dwg"
          },
          "meta": {
            "link": {
              "href": "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/9c169b42-5893-442b-80f5-34b25680ef34.dwg"
            }
          }
        }
      }
    }
  ]
}

```

Show More
