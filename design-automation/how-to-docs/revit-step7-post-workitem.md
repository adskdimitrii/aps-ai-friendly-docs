# Task 7 – Submit a WorkItem

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/revit/step7-post-workitem/

---

# Task 7 – Submit a WorkItem

When you post a WorkItem to the Automation Service, you are instructing the service to execute an Activity.

The relationship between an Activity and a WorkItem can be thought of as a “function definition” and “function call”, respectively.
Named parameters of the Activity have corresponding named arguments of the WorkItem.
Like in function calls, optional parameters of the Activity can be skipped and left unspecified while posting a WorkItem.

By the end of this task, you will be able to:
> - Create a WorkItem to execute an Activity.
> - Check if execution succeeded or failed.
> - Get the URL to the execution log file.

You will use the following operations to work with WorkItems in this task:

| HTTP Request | Description |
| --- | --- |
| [POST /workitems](../http-docs/http-workitems-POST.md) | Creates a new WorkItem and queues it for processing. |
| [GET /workitems/{id}](../http-docs/http-workitems-id-GET.md) | Gets the status of a specific WorkItem. |

## [Step 1 - Create a WorkItem](#step-1-create-a-workitem)

To create a work item to execute the Activity DeleteWallsActivity:

### Request
> ```
> curl -X POST \
> 'https://developer.api.autodesk.com/da/us-east/v3/workitems' \
> -H 'Content-Type: application/json' \
> -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
> -d '{
> "activityId": "<YOUR_APP_NICKNAME>.DeleteWallsActivity+test",
> "arguments": {
> "rvtFile": {
> "url": "urn:adsk.objects:os.object:<YOUR_BUCKET_KEY>/<OBJECT_KEY_4_INPUT_FILE>",
> "verb": "get",
> "headers": {
> "Authorization": "Bearer <YOUR_ACCESS_TOKEN>"
> }
> },
> "result": {
> "url": "urn:adsk.objects:os.object:<YOUR_BUCKET_KEY>/<RESULT_FILE_OBJECT_KEY>",
> "verb": "put",
> "headers": {
> "Authorization": "Bearer <YOUR_ACCESS_TOKEN>"
> }
> }
> }
> }'
>
> ```
>
>
> Show More
>
> **Note**
>
> | Attribute | Description |
> | --- | --- |
> | `activityId` | The target Activity defined by “owner.activity+alias”(`<YOUR_NICKNAME>.DeleteWallsActivity+test`) this WorkItem will execute. |
> | `arguments` | The argument list that is required by the Activity (`DeleteWallsActivity`):       - `rvtFile` - The URN of the input file that the Automation Service must “get” from OSS.   - `result` - The URN of the output file that the Automation Service must “put” (upload) to OSS. |

### Response

```
{
    "status": "pending",
    "stats": {
        "timeQueued": "2018-04-16T21:45:08.1357163Z"
    },
    "id": "<YOUR_WORKITEM_ID>"
}

```

## [Step 2 - Check status of a WorkItem](#step-2-check-status-of-a-workitem)

WorkItems are queued before they are processed.
A WorkItem’s processing time will vary depending on the size and complexity of the input files, the type of processing done by the AppBundle, and the size of the output files.

In this walkthrough, you will be checking the WorkItem status to see if it has completed.
However, the best practice is to use the `onComplete` argument when submitting a WorkItem.
This onComplete argument enables you to specify a callback URL, which will be called once the WorkItem is completed.
For more information on the `onComplete` argument see “Output arguments: onComplete callback” under the Additional notes section below.

You can check the status of a WorkItem by calling `[GET] /workitems/{id}`:

### Request

```
curl -X GET \
  'https://developer.api.autodesk.com/da/us-east/v3/workitems/YOUR_WORKITEM_ID' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>'

```

### Response

```
{
    "status": "success",
    "reportUrl":  "https://dasprod-store.s3.amazonaws.com/workItem/<YOUR_APP_NICKNAME>/<YOUR_WORKITEM_ID>/report.txt?...(truncated)",
    "stats": {
        "timeQueued": "2018-04-13T03:15:15.9772282Z",
        "timeDownloadStarted": "2018-04-13T03:15:17.2960823Z",
        "timeInstructionsStarted": "2018-04-13T03:15:20.2803318Z",
        "timeInstructionsEnded": "2018-04-13T03:15:41.6075799Z",
        "timeUploadEnded": "2018-04-13T03:15:42.0450494Z"
    },
    "id": "<YOUR_WORKITEM_ID>"
}

```

Show More

| Attribute | Description |
| --- | --- |
| `status` | Indicates if execution is pending, successful, failed or cancelled. |
| `reportUrl` | The URL to get the report log for this WorkItem’s execution. |

## [Additional notes](#additional-notes)

If an input argument of an Activity requires JSON values, the JSON values can be embedded in the WorkItem itself.

For example, the Activity `CountItActivity` requires a parameter named `countItParams`. The Activity expects the argument value to be a JSON file. The WorkItem is able to embed the JSON values in the WorkItem itself as shown below.
By prefixing those values with `data:application/json`, you instruct the Automation Service to handle them as a JSON stream and save them as a JSON file:

### Request

```
curl -X POST \
  'https://developer.api.autodesk.com/da/us-east/v3/workitems' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -d '{
          "activityId": "<YOUR_NICKNAME>.CountItActivity+test",
          "arguments": {
            "rvtFile": {
              "url": "https://s3.amazonaws.com/revitio-dev/test-data/CountIt.rvt"
            },
            "countItParams": {
              "url": "data:application/json,{'walls': false, 'floors': true, 'doors': true, 'windows': true}"
            },
            "result": {
              "verb": "put",
              "url": "<SIGNED_URL_TO_RESULT>"
            }
          }
      }'

```

Show More

#### Input arguments: eTransmit files

The Automation Service is capable of processing outputs from eTransmit for Revit, so long as you first create a zip file from those outputs:

### Request

```
curl POST \
  https://developer.api.autodesk.com/da/us-east/v3/workitems \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -d '{
        "activityId" : "<YOUR_NICKNAME>.CountItActivity+test",
        "arguments": {
          "rvtFile": {
            "url": "https://s3.amazonaws.com/revitio-dev/test-data/TopHost.zip"
            "pathInZip": "CountIt.rvt"
          },
          "countItParams": {
            "url": "data:application/json,{'walls': true, 'floors': true, 'doors': true, 'windows': true}"
          },
          "result": {
            "verb": "put",
            "url": "<SIGNED_URL_TO_RESULT>"
          }
        }
    }'

```

Show More

A sample eTransmit file `TopHost.zip` is available at [TopHost.zip](https://revitio.s3.amazonaws.com/documentation/TopHost.zip).

The name of the “Root Model” is read from the manifest file. The root model is then found in the zip.

#### Host RVT file with linked models

### Request

```
curl POST \
  'https://developer.api.autodesk.com/da/us-east/v3/workitems' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -d '{
        "activityId": "YOUR_NICKNAME.CountItActivity+test",
        "arguments": {
          "rvtFile": {
            "url": "https://s3.amazonaws.com/revitio-dev/test-data/TopHost.rvt",
            "references": [
              {
                "url": "https://s3.amazonaws.com/revitio-dev/test-data/LinkA.rvt",
                "references": [
                  {
                    "url": "https://s3.amazonaws.com/revitio-dev/test-data/LinkA1.rvt"
                  },
                  {
                    "url": "https://s3.amazonaws.com/revitio-dev/test-data/LinkA2.rvt"
                  }
                ]
              },
              {
                "url": "https://s3.amazonaws.com/revitio-dev/test-data/LinkB.rvt"
              }
            ]
          },
          "countItParams": {
            "url": "data:application/json,{'walls': true, 'floors': true, 'doors': true, 'windows': true}"
          },
          "result": {
            "verb": "put",
            "url": "https://myWebsite/signed/url/to/result"
          }
        }
    }'

```

Show More

The root model in this example is `TopHost.rvt` and it contains `LinkA.rvt` and `LinkB.rvt`. The file `LinkA.rvt` in turn contains `LinkA1.rvt` and `LinkA2.rvt`. Each file is uploaded to a cloud location and the path is provided for each individually:

```
TopHost.rvt
|-- LinkA.rvt
|   |-- LinkA1.rvt
|   |-- LinkA2.rvt
|
|-- LinkB.rvt

```

#### RvtLinks in sub-folders

The WorkItem’s `localName` variable can be used to create a folder structure inside the working directory. For example, a Revit file **Host.rvt** containing a relative link **SubFolder/Link.rvt** can be defined in this way for `rvtFile` in the WorkItem:

```
{
  "url": "https://s3.amazonaws.com/revitio-dev/test-data/TestForSubFolders/Host.rvt",
  "references": [
    {
      "url": "https://s3.amazonaws.com/revitio-dev/test-data/TestForSubFolders/Link.rvt",
      "localName": "SubFolder/Link.rvt"
    }
  ]
}

```

Show More

This will create the directory/file structure in the current working directory (CWD):

```
{CWD}/Host.rvt
{CWD}/SubFolder/Link.rvt

```

Because you are not allowed to create a folder structure outside of your current working directory, if the host file has linked files with relative paths like **../ParallelFolder/Link.rvt**, you can move the entire structure down one level by creating a top level folder of your own. The same `localName` variable can be used for the top host link you use for linked files. Here is an example json:

```
{
 "url": "https://path/to/Host.rvt",
 "localName": "TopFolder/Host.rvt",
 "references": [
   {
     "url": "https://path/to/Link.rvt",
     "localName": "ParallelFolder/Link.rvt"
   }
 ]
}

```

Show More

This will create the directory/file structure:

```
{CWD}/TopFolder/Host.rvt
{CWD}/ParallelFolder/Link.rvt

```

#### Input arguments: Zip file

To increase download speed, the Automation API the ability to use a zip file for input arguments. To specify the path to the host Revit file, use the `"pathInZip":` option:

```
"arguments": {
  "rvtFile": {
    "url": "https://s3.amazonaws.com/revitio-dev/test-data/CountIt.zip",
    "pathInZip": "CountIt.rvt"
  },
}

```

**Notes:**

- When providing a zip file as input argument, the `"pathInZip"` option can be specified. In our example, we specified `CountIt.rvt`:

```
CountIt.zip
|-- CountIt.rvt
...

```

#### Output arguments: onComplete callback

Each WorkItem supports a special output argument named `onComplete`. When provided, the Automation Service calls the callback URL when it completes processing the WorkItem.

Here is an example of how to call `[POST] /workitems` with the `onComplete` argument added to the example in [Step 1](##step-1-post-a-workitem):

### Request

```
curl -X POST \
  'https://developer.api.autodesk.com/da/us-east/v3/workitems' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -d '{
        "activityId": "<YOUR_NICKNAME>.DeleteWallsActivity+test",
        "arguments": {
          "rvtFile": {
            "url": "https://s3.amazonaws.com/revitio-dev/test-data/DeleteWalls.rvt"
          },
          "result": {
            "verb": "put",
            "url": "<SIGNED_URL_TO_RESULT>"
          },
          "onComplete": {
            "verb": "post",
            "url": "https://myWebsite/callback"
          }
        }
      }'

```

Show More

This argument is optional for the `[POST] /workitems` call.

Once the WorkItem is processed, the specified URL is called with a payload identical to the response received on `[GET] /workitems/{id}` call.

The implementation of the callback URL is similar to how you implement a callback URL for the [Webhooks API](https://aps.autodesk.com/en/docs/webhooks/v1/overview/). Refer to the Webhooks API documentation for information on specifying the callback URL. Additional documentation for [configuring local server](../../webhooks/how-to-docs/configuring-your-server.md) is also available.

**Notes:**

- Revit 2018 supports `Open IFC` and `Export IFC` functionality.
- Revit 2019 and higher support `Open IFC` , `Export IFC` and `Link IFC` functionality.
