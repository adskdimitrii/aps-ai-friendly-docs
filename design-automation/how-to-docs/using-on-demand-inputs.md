# Use OnDemand Inputs

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/common/using-on-demand-inputs/

---

# Use OnDemand Inputs

Once you have a running custom AppBundle with an Activity and a WorkItem, you can consider more advanced processing.

This walkthrough will explain how you can optimize data downloads using so called onDemand inputs in Activities and WorkItems. This mechanism allows your AppBundle to ask for additional data to be downloaded using an http call during WorkItem processing only on an as-needed basis.

Conceptually, onDemand inputs allow your AppBundle to access additional resources based on the actual run of a given WorkItem, using a url that can be parameterized to query exactly the data you need right now. It can either access additional specific design files on your storage, or call your own serverâs http API to query for json data etc.

There are several steps you need to take in order to be able to use onDemand inputs. First, when you are creating your activity, you must specify some of the input arguments as being onDemand. Note that onDemand can only be used when the parameter verb is `get` or `head`.

## [Example](#example)

```
curl -i -X POST \
  https://developer.api.autodesk.com/da/us-east/v3/activities
  ...
  -d '{
  "id": "MyActivity",
  ...
    "parameters": {
      "InventorDoc": {
        "verb": "get"
      },
      "OptionalIpt": {
        "verb": "get",
        "onDemand": true
      },
      ...
    }
  }

```

Show More

Second, you must refer to this parameter when sending the WorkItem, as shown here:

## [Example](#id1)

```
curl -i -X POST \
  https://developer.api.autodesk.com/da/us-east/v3/workitems \
  ...
  -d '{
  "activityId": "MyActivity+prod",
  ...
  "arguments": {
    "InventorDoc": {
      "url": "https://s3-us-east-1.amazonaws.com/inventorio-prod/documentation/APIBasics/Box.ipt"
    },
    "OptionalIpt": {
      "url": "https://s3-us-east-1.amazonaws.com/inventorio-prod/documentation/APIBasics"
    }
  ...
  }
}

```

Show More

Third, your AppBundle add-in has to be able to ask for the optional onDemand input. This is done via writing specially formatted text to the log trace. The required format is best documented in the following method that handles a request for such an optional input and waits for the http call result:

## [Example](#id2)

```
private static bool GetOnDemandFile(string name, string suffix, string headers, string responseFile)
    {
        // writing a string (formatted according to ACESAPI format) to trace
        // invokes the onDemand call to get the desired optional input file
        LogTrace("!ACESAPI:acesHttpOperation({0},{1},{2},{3},{4})",
            name ?? "", suffix ?? "", headers ?? "", "", responseFile ?? "");

        // waiting for a control character indicating
        // that the download has successfully finished
        int idx = 0;
        while (true)
        {
            char ch = Convert.ToChar(Console.Read());
            // error
            if (ch == '\x3')
            {
                return false;
            }
            // success
            else if (ch == '\n')
            {
                return true;
            }

            // to many unexpected characters already read from console,
            // treating as other error / timeout
            if (idx >= 16)
            {
                return false;
            }
            idx++;
        }
    }

```

Show More

An actual call to the function can be made like

```
GetOnDemandFile("OptionalIpt", "optPart.ipt", "", $"file://optPart.ipt");

```

## [function parameters](#function-parameters)

| Name | Description |
| --- | --- |
| name | name of the onDemand input parameter as specified in the Activity |
| suffix | a query string - optional parameters that can be addded to the url defined in the WorkItem |
| headers | http call headers |
| responseFile | tells the system the filename under which the onDemand file is saved by the http call, must start with âfile://â |

The tricky pieces here are:

- the special beggining of the trace line (â!ACESAPI:acesHttpOperationâ),
- the way to identify that the http operation has finished (and how) - check the test of char read from console in the function code sample above.

The method to support onDemand calls from an add-in is part of the [Inventor Visual Studio template](https://marketplace.visualstudio.com/items?itemName=Autodesk.DesignAutomation2) .

## [Known issues:](#known-issues)

- when you use the parameter zip=âtrueâ with parameter onDemand=âtrueâ then a zip file will be downloaded, not unzipped.
