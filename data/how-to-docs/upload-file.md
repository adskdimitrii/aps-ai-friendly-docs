# Upload a File

Source: https://aps.autodesk.com/en/docs/data/v2/tutorials/upload-file/

---

# Upload a File

This walkthrough explains how to upload a file as a resource item to the project.

In the examples, the responses have been condensed for simplicity.

## [Before You Begin](#before-you-begin)

Make sure that you have [registered an app](/en/docs/oauth/v2/tutorials/create-app) and successfully [acquired an OAuth token](/en/docs/oauth/v2/tutorials).

See the Authentication and Scopes section in the [API Basics](/en/docs/data/v2/overview/basics) for the appropriate token based on the data you are accessing.

In general, access to BIM 360 Team, BIM 360 Docs, Fusion Team, and A360 Personal data requires the use of a [3-legged OAuth2 token](/en/docs/oauth/v2/tutorials/get-3-legged-token).

HTTP `GET` requests to the Project and Data services require the `data:read` scope.

HTTP `POST` requests to the Data service require the `data:create` scope, but can also be called with the `data:write` scope.

To upload a file to BIM 360 Docs, see the [Upload Documents to BIM 360 Docs](/en/docs/bim360/v1/tutorials/upload-document/) walkthrough.

## [Step 1: Find the hub that has your resource](#step-1-find-the-hub-that-has-your-resource)

The Data Management service exposes a [GET hubs](/en/docs/data/v2/reference/http/hubs-GET) endpoint that provides a
list of available hubs for the logged in user. A GET request to that endpoint allow us
to find the URL for the hub we want.

### Example

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/project/v1/hubs"

```

The resource provides the following response:

```
 {
   "jsonapi":{
      "version":"1.0"
   },
  "links":{
    "self":{
      "href":"https://developer.api.autodesk.com/project/v1/hubs"
    }
  },
   "data":[
      {
         "type":"hubs",
         "id":"a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4",
         "attributes":{
            "name":"John's Hub",
            "extension":{
               "type":"hubs:autodesk.core:Hub",
               "version":"1.0",
               "schema":{
                  "href":"https://developer.api.autodesk.com/schema/v1/versions/hubs%3Aautodesk.core%3AHub-1.0"
               },
               "data":{}
            }
         },
         "links":{
            "self":{
               "href":"https://developer.api.autodesk.com/project/v1/hubs/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4"
            }
         },
         "relationships":{
            "projects":{
               "links":{
                  "related":{
                     "href":"https://developer.api.autodesk.com/project/v1/hubs/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4/projects"
                  }
               }
            }
         }
      },
      {
         "type":"hubs",
         "id":"a.YnVzaW5lc3M6d2lwMWZxYWF1dG9kZXNrMTYx",
         "attributes":{
            "name":"Bob's Hub",
            "extension":{
               "type":"hubs:autodesk.core:Hub",
               "version":"1.0",
               "schema":{
                  "href":"https://developer.api.autodesk.com/schema/v1/versions/hubs%3Aautodesk.core%3AHub-1.0"
               },
               "data":{}
            }
         },
         "links":{
            "self":{
               "href":"https://developer.api.autodesk.com/project/v1/hubs/a.YnVzaW5lc3M6d2lwMWZxYWF1dG9kZXNrMTYx"
            }
         },
         "relationships":{
            "projects":{
               "links":{
                  "related":{
                     "href":"https://developer.api.autodesk.com/project/v1/hubs/a.YnVzaW5lc3M6d2lwMWZxYWF1dG9kZXNrMTYx/projects"
                  }
               }
            }
         }
      }
   ]
}

```

Show More

## [Step 2: Find the project that has your resource](#step-2-find-the-project-that-has-your-resource)

In the above example, assume that your resource exists in âJohnâs Hubâ. Make
note of the the hub ID (`a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4`). The ID can be
used with the [GET hubs/:hub_id/projects](/en/docs/data/v2/reference/http/hubs-hub_id-projects-GET) endpoint to obtain a list of all the
projects the user has access to within the hub.

### Example

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/project/v1/hubs/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4/projects"

```

The resource provides the following response:

```
{
   "jsonapi":{ "version":"1.0" },
   "links":{
      "self":{
         "href":"https://developer.api.autodesk.com/project/v1/hubs/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4/projects"
      }
   },
   "data":[
      {
         "type":"projects",
         "id":"a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4IzIwMTYwNDE4Mzk0MzY5OA",
         "attributes":{
            "name":"John's First Project",
            "extension":{
               "type":"projects:autodesk.core:Project",
               "version":"1.0",
               "schema":{
                  "href":"https://developer.api.autodesk.com/schema/v1/versions/projects%3Aautodesk.core%3AProject-1.0"
               },
               "data":{}
            }
         },
         "links":{
            "self":{
               "href":"https://developer.api.autodesk.com/project/v1/hubs/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4IzIwMTYwNDE4Mzk0MzY5OA"
            }
         },
         "relationships":{
            "hub":{
               "data":{
                  "type":"hubs",
                  "id":"a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4"
               },
               "links":{
                  "related":{
                     "href":"https://developer.api.autodesk.com/project/v1/hubs/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4"
                  }
               }
            },
            "rootFolder":{
               "data":{
                  "type":"folders",
                  "id":"urn:adsk.wipprod:fs.folder:co.O7ZwaiGAQOueskTkQqPoxQ"
               },
               "meta":{
                  "link":{
                     "href":"https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4IzIwMTYwNDE4Mzk0MzY5OA/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.O7ZwaiGAQOueskTkQqPoxQ"
                  }
               }
            }
         }
      },
      {
         "type":"projects",
         "id":"a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM",
         "attributes":{
            "name":"John's Second Project",
            "extension":{
               "type":"projects:autodesk.core:Project",
               "version":"1.0",
               "schema":{
                  "href":"https://developer.api.autodesk.com/schema/v1/versions/projects%3Aautodesk.core%3AProject-1.0"
               },
               "data":{}
            }
         },
         "links":{
            "self":{
               "href":"https://developer.api.autodesk.com/project/v1/hubs/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM"
            }
         },
         "relationships":{
            "hub":{
               "data":{
                  "type":"hubs",
                  "id":"a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4"
               },
               "links":{
                  "related":{
                     "href":"https://developer.api.autodesk.com/project/v1/hubs/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4"
                  }
               }
            },
            "rootFolder":{
               "data":{
                  "type":"folders",
                  "id":"urn:adsk.wipprod:fs.folder:co.mgS-lb-BThaTdHnhiN_mbA"
               },
               "meta":{
                  "link":{
                     "href":"https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.mgS-lb-BThaTdHnhiN_mbA"
                  }
               }
            }
         }
      }
   ]
}

```

Show More

## [Step 3: Create a storage location](#step-3-create-a-storage-location)

In the above example, assume that your resource exists in âJohnâs Second Projectâ.
Make note of the the project and folder IDs (`a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM` and `urn:adsk.wipprod:fs.folder:co.mgS-lb-BThaTdHnhiN_mbA` respectively).

The [POST projects/:project_id/storage](/en/docs/data/v2/reference/http/projects-project_id-storage-POST) endpoint creates a storage location in the OSS where files can be uploaded to.

Note that you cannot upload documents to the root folder in BIM 360 Docs; you can only upload documents to the Project Files folder or to a folder nested under the Project Files folder. For more details, see the [Upload Documents to BIM 360 Docs](/en/docs/bim360/v1/tutorials/upload-document/) walkthrough.

### Example

```
curl -X POST -H "Content-Type: application/vnd.api+json" -H "Accept: application/vnd.api+json" -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" -d '{
      "jsonapi": { "version": "1.0" },
      "data": {
        "type": "objects",
        "attributes": {
          "name": "myfile.jpg"
        },
        "relationships": {
          "target": {
            "data": { "type": "folders", "id": "urn:adsk.wipprod:fs.folder:co.mgS-lb-BThaTdHnhiN_mbA" }
          }
        }
      }
}' "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/storage"

```

Show More

The resource provides the following response:

```
{
  "jsonapi": { "version": "1.0" },
  "data": {
    "type": "objects",
    "id": "urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg",
    "relationships": {
      "target": {
        "data": {
          "type": "folders",
          "id": "urn:adsk.wipprod:fs.folder:co.mgS-lb-BThaTdHnhiN_mbA"
        },
        "links": {
          "related": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/folders/urn%3Aadsk.wipprod%3Afs.folder%3Aco.mgS-lb-BThaTdHnhiN_mbA"
          }
        }
      }
    }
  }
}

```

Show More

## [Step 4: Generate a signed S3 url](#step-4-generate-a-signed-s3-url)

In the above example, make note of the object ID (`urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg` where `wip.dm.prod` is the bucket key and `2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg` is the object Key.)

The [GET buckets/:bucket_key/objects/:object_key/signeds3upload](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-GET) endpoint generates a signed URL of the storage upload location created in the last step.

This endpoint supports generating multiple signed URLs to allow parallel upload of chunks of the same file. Please refer to the documentation of this endpoint for more information.

### Example

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg/signeds3upload"

```

A successful response contains a signed url that can be used to upload the object.

```
{
  "uploadKey": "[UPLOAD_KEY_FROM_GET_UPLOAD_URLS_RESPONSE]",
  "uploadExpiration": "2022-02-05T00:00:00Z",
  "urlExpiration": "2022-02-03T05:23:29Z",
  "urls": [
      "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/26668812-6bb1-4f80-bab2-09776f24fd98?uploadId=[UPLOAD_ID]&partNumber=1&X-Amz-Security-Token=[AMZ_TOKEN]%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220203T052230Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=[AMZ_CREDENTIAL]%2F20220203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=[AMZ_SIGNATURE]"
  ]
}

```

Show More

## [Step 5: Upload a file to the signed url](#step-5-upload-a-file-to-the-signed-url)

The file itself can then be uploaded to the signed url as per the following example.

Note: This upload is directly to S3 and as such doesnât need an âAuthorizationâ header.

### Example

```
curl -X PUT -H --data-binary @D:\Temp\myfile.jpg "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/26668812-6bb1-4f80-bab2-09776f24fd98?uploadId=[UPLOAD_ID]&partNumber=1&X-Amz-Security-Token=[AMZ_TOKEN]%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220203T052230Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=[AMZ_CREDENTIAL]%2F20220203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=[AMZ_SIGNATURE]"

```

## [Step 6: Complete the upload](#step-6-complete-the-upload)

The upload needs to be completed by calling the [POST buckets/:bucket_key/objects/:object_key/signeds3upload](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-POST) endpoint. An object will not be accessible until this endpoint is called. This endpoint must be called within 24 hours of the upload beginning, otherwise the object will be discarded, and the upload must begin again from scratch.

**Note:** The value to be used for `uploadkey` for this request was returned in the response of step 4.

### Example

```
curl -X POST -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" -H "Content-Type: application/json" --data-raw '{"uploadKey":"[UPLOAD_KEY_FROM_GET_UPLOAD_URLS_RESPONSE]"}' "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg/signeds3upload"

```

The resource provides the following response:

```
{
  "bucketKey" : "wip.dm.prod",
  "objectId" : "urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg",
  "objectKey" : "2ac28abc-9f6e-463d-bcc4-5c194d552beb.jpg",
  "size" : 879394,
  "contentType" : "application/octet-stream",
  "location" : "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg"
}

```

Show More

## [Step 7: Create the first version of the uploaded file](#step-7-create-the-first-version-of-the-uploaded-file)

In the above examples, make note of the the object ID, project ID and folder ID which are respectively, `urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg`, `a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM`, and `urn:adsk.wipprod:fs.folder:co.mgS-lb-BThaTdHnhiN_mbA`.

The [POST projects/:project_id/items](/en/docs/data/v2/reference/http/projects-project_id-items-POST) endpoint creates the first version of the uploaded file.

### Example

```
curl -X POST -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" -H "Content-Type: application/vnd.api+json" -H "Accept: application/vnd.api+json" -d '{
    "jsonapi": { "version": "1.0" },
    "data": {
      "type": "items",
      "attributes": {
        "displayName": "myfile.jpg",
        "extension": {
          "type": "items:autodesk.core:File",
          "version": "1.0"
        }
      },
      "relationships": {
        "tip": {
          "data": {
            "type": "versions", "id": "1"
          }
        },
        "parent": {
          "data": {
            "type": "folders",
            "id": "urn:adsk.wipprod:fs.folder:co.mgS-lb-BThaTdHnhiN_mbA"
          }
        }
      }
    },
    "included": [
      {
        "type": "versions",
        "id": "1",
        "attributes": {
          "name": "myfile.jpg",
          "extension": {
            "type": "versions:autodesk.core:File",
            "version": "1.0"
          }
        },
        "relationships": {
          "storage": {
            "data": {
              "type": "objects",
              "id": "urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg"
            }
          }
        }
      }
    ]
  }' "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/items"

```

Show More

The resource provides the following response:

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": {
      "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/items"
    }
  },
  "data": {
    "type": "items",
    "id": "urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ",
    "attributes": {
      "displayName": "myfile.jpg",
      "createTime": "2016-05-30T15:32:05+00:00",
      "createUserId": "KPN8P8P65K",
      "createUserName": "John Doe",
      "lastModifiedTime": "2016-05-30T15:32:05+00:00",
      "lastModifiedUserId": "KPN8P8P65K",
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
        "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/items/urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ"
      }
    },
    "relationships": {
      "tip": {
        "data": {
          "type": "versions",
          "id": "urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ?version=1"
        },
        "links": {
          "related": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/items/urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ/tip"
          }
        }
      },
      "versions": {
        "links": {
          "related": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/items/urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ/versions"
          }
        }
      },
      "parent": {
        "data": {
          "type": "folders",
          "id": "urn:adsk.wipprod:fs.folder:co.mgS-lb-BThaTdHnhiN_mbA"
        },
        "links": {
          "related": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/items/urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ/parent"
          }
        }
      },
      "refs": {
        "links": {
          "self": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/items/urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ/relationships/refs"
          },
          "related": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/items/urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ/refs"
          }
        }
      },
      "links": {
        "links": {
          "self": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/items/urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ/relationships/links"
          }
        }
      }
    }
  },
  "included": [
    {
      "type": "versions",
      "id": "urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ?version=1",
      "attributes": {
        "name": "myfile.jpg",
        "displayName": "myfile.jpg",
        "createTime": "2016-05-30T15:32:05+00:00",
        "createUserId": "KPN8P8P65K",
        "createUserName": "John Doe",
        "lastModifiedTime": "2016-05-30T15:32:05+00:00",
        "lastModifiedUserId": "KPN8P8P65K",
        "lastModifiedUserName": "John Doe",
        "versionNumber": 1,
        "mimeType": "application/image",
        "fileType": "jpg",
        "storageSize": 879394,
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
          "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/versions/urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ%3Fversion%3D1"
        }
      },
      "relationships": {
        "item": {
          "data": {
            "type": "items",
            "id": "urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ"
          },
          "links": {
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/versions/urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ%3Fversion%3D1/item"
            }
          }
        },
        "links": {
          "links": {
            "self": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/versions/urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ%3Fversion%3D1/relationships/links"
            }
          }
        },
        "refs": {
          "links": {
            "self": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/versions/urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ%3Fversion%3D1/relationships/refs"
            },
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/versions/urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ%3Fversion%3D1/refs"
            }
          }
        },
        "downloadFormats": {
          "links": {
            "related": {
              "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/versions/urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ%3Fversion%3D1/refs"
            }
          }
        },
        "derivatives": {
          "data": {
            "type": "derivatives",
            "id": "dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuQWVZZ0R0Y1RTdXFZb3lNd2VXRmhoUT92ZXJzaW9uPTE"
          },
          "meta": {
            "link": {
              "href": "https://developer.api.autodesk.com/viewingservice/v1/dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuQWVZZ0R0Y1RTdXFZb3lNd2VXRmhoUT92ZXJzaW9uPTE"
            }
          }
        },
        "thumbnails": {
          "data": {
            "type": "thumbnails",
            "id": "dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuQWVZZ0R0Y1RTdXFZb3lNd2VXRmhoUT92ZXJzaW9uPTE"
          },
          "meta": {
            "link": {
              "href": "https://developer.api.autodesk.com/viewingservice/v1/thumbnails/dXJuOmFkc2sud2lwc3RnOmZzLmZpbGU6dmYuQWVZZ0R0Y1RTdXFZb3lNd2VXRmhoUT92ZXJzaW9uPTE"
            }
          }
        },
        "storage": {
          "data": {
            "type": "objects",
            "id": "urn:adsk.objects:os.object:wip.dm.prod/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg"
          },
          "meta": {
            "link": {
              "href": "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/2a6d61f2-49df-4d7b-9aed-439586d61df7.jpg"
            }
          }
        }
      }
    }
  ]
}

```

Show More

## [Step 8: Update the version of a file](#step-8-update-the-version-of-a-file)

An uploaded resource can have multiple versions. To create a new version of an existing resource, Step 3 and 4 in this walkthrough will needed to be repeated. Make note of the new object ID in Step 3. Get the item ID of the resource from Step 5 or call the [GET projects/:project_id/folders/:folder_id/contents](/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET) endpoint.

The [POST projects/:project_id/versions](/en/docs/data/v2/reference/http/projects-project_id-versions-POST) endpoint creates a new version of the uploaded file.

### Example

```
curl -X POST -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" -H "Content-Type: application/vnd.api+json" -H "Accept: application/vnd.api+json" -d '{
   "jsonapi": { "version": "1.0" },
   "data": {
      "type": "versions",
      "attributes": {
         "name": "myfile.jpg",
         "extension": { "type": "versions:autodesk.core:File", "version": "1.0"}
      },
      "relationships": {
         "item": { "data": { "type": "items", "id": "urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ" } },
         "storage": { "data": { "type": "objects", "id": "urn:adsk.objects:os.object:wip.dm.prod/980cff2c-f0f8-43d9-a151-4a2d916b91a2.jpg" } }
      }
   }
}' "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/versions"

```

Show More

The resource provides the following response:

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": {
      "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/versions"
    }
  },
  "data": {
    "type": "versions",
    "id": "urn:adsk.wipprod:fs.file:vf.AeYgDtcTSuqYoyMweWFhhQ?version=2",
    "attributes": {
      "name": "myfile.jpg",
      "displayName": "myfile.jpg",
      "createTime": "2016-06-03T20:10:19+00:00",
      "createUserId": "KPN8P8P65K7K",
      "createUserName": "John Doe",
      "lastModifiedTime": "2016-06-03T20:10:19+00:00",
      "lastModifiedUserId": "KPN8P8P65K7K",
      "lastModifiedUserName": "John Doe",
      "versionNumber": 2,
      "mimeType": "image/jpeg",
      "storageSize": 777835,
      "fileType": "jpg",
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
        "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.AeYgDtcTSuqYoyMweWFhhQ%3Fversion%3D2"
      }
    },
    "relationships": {
      "item": {
        "data": {
          "type": "items",
          "id": "urn:adsk.wipprod:dm.lineage:AeYgDtcTSuqYoyMweWFhhQ"
        },
        "links": {
          "related": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.AeYgDtcTSuqYoyMweWFhhQ%3Fversion%3D2/item"
          }
        }
      },
      "links": {
        "links": {
          "self": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.AeYgDtcTSuqYoyMweWFhhQ%3Fversion%3D2/relationships/links"
          }
        }
      },
      "refs": {
        "links": {
          "self": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.AeYgDtcTSuqYoyMweWFhhQ%3Fversion%3D2/relationships/refs"
          },
          "related": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.AeYgDtcTSuqYoyMweWFhhQ%3Fversion%3D2/refs"
          }
        }
      },
      "downloadFormats": {
        "links": {
          "related": {
            "href": "https://developer.api.autodesk.com/data/v1/projects/a.cGVyc29uYWw6d2lwMWZxYWUyOWNlZGY4I0QyMDE2MDQxODM5NDM2NzM/versions/urn%3Aadsk.wipprod%3Afs.file%3Avf.AeYgDtcTSuqYoyMweWFhhQ%3Fversion%3D2/downloadFormats"
          }
        }
      },
      "derivatives": {
        "data": {
          "type": "derivatives",
          "id": "dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLkFlWWdEdGNUU3VxWW95TXdlV0ZoaFEdmVyc2lvbj0y"
        },
        "meta": {
          "link": {
            "href": "https://developer.api.autodesk.com/viewingservice/v1/dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLkFlWWdEdGNUU3VxWW95TXdlV0ZoaFEdmVyc2lvbj0y"
          }
        }
      },
      "thumbnails": {
        "data": {
          "type": "thumbnails",
          "id": "dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLkFlWWdEdGNUU3VxWW95TXdlV0ZoaFEdmVyc2lvbj0y"
        },
        "meta": {
          "link": {
            "href": "https://developer.api.autodesk.com/viewingservice/v1/thumbnails/dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLkFlWWdEdGNUU3VxWW95TXdlV0ZoaFEdmVyc2lvbj0y"
          }
        }
      },
      "storage": {
        "data": {
          "type": "objects",
          "id": "urn:adsk.objects:os.object:wip.dm.prod/980cff2c-f0f8-43d9-a151-4a2d916b91a2.jpg"
        },
        "meta": {
          "link": {
            "href": "https://developer.api.autodesk.com/oss/v2/buckets/wip.dm.prod/objects/980cff2c-f0f8-43d9-a151-4a2d916b91a2.jpg"
          }
        }
      }
    }
  }
}

```

Show More
