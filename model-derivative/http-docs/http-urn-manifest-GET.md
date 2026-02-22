# modelderivative/v2/designdata/{urn}/manifest

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/reference/http/urn-manifest-GET/

---

Fetch Manifest

GET

# modelderivative/v2/designdata/{urn}/manifest

Retrieves the manifest of the specified source design.

The manifest is a JSON file containing information about all the derivatives translated from the specified source design, including the URNs of the derivatives, the translation status of each derivative, and other details.

The first time you translate a source design, the Model Derivative service creates a manifest for that design. Thereafter, every time you translate that source design, even to a different format, the Model Derivative service updates the same manifest rather than creating a new one. The manifest acts as a central registry for all the derivatives of your source design created through the Model Derivative service.

When the Model Derivative service starts a translation job (as a result of a request you make using [Create Translation Job](/en/docs/model-derivative/v2/reference/http/jobs/job-POST/)), it updates the manifest at regular intervals. You can use the manifest to check the status and progress of each derivative being generated. When multiple derivatives have been requested, each may complete at a different time. Each derivative has its own `status` attribute. The manifest also contains an overall `status` attribute. The overall `status` becomes `complete` when the `status` of all individual derivatives become complete.

Once the translation status of a derivative is `complete`, you can download the derivative.

**Note:** You cannot download 3D SVF2 derivatives.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/modelderivative/v2/designdata/{urn}/manifest |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` `viewable:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a two-legged access token obtained via a [Client Credentials Grant flow](/en/docs/oauth/v2/tutorials/get-2-legged-token/), or a three-legged access token obtained via an [Authorization Code flow](/en/docs/oauth/v2/tutorials/get-3-legged-token/) or a [Secure Service Account flow](/en/docs/ssa/v1/tutorials/getting-started-with-ssa/task3-generate-3-legged-access-token/). The Secure Service Account flow generates tokens without user interaction but maintains user context for headless server-to-server operations. |
| --- | --- |
| Accept-Encoding   string | A comma separated list of the algorithms you want the response to be encoded in, specified in the order of preference. <br>If you specify `gzip` or `*`, content is compressed and returned in gzip format. |
| region   string | Specifies the data center where the manifest and derivatives of the specified source design are stored. Possible values are: <br>`US` - (Default) Data center for the US region.`EMEA` - Data center for the European Union, Middle East, and Africa.`AUS` - Data center for the Australia region.`CAN` - Data center for the Canada region.`DEU` - Data center for the Germany region.`IND` - Data center for the India region.`JPN` - Data center for the Japan region.`GBR` - Data center for the United Kingdom region. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| urn   string | The URL-safe Base64 encoded URN of the source design. This value is used as the `urn` URI parameter in operations to access data for this source design. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The manifest was successfully retrieved. |
| --- | --- |
| 400   Bad Request | The server was unable to process the request. The syntax of the request is malformed or the request is missing a required header. Do not repeat the request without fixing the issue. The response body may indicate what is wrong with the request. |
| 401   Unauthorized | The supplied authorization header was not valid or the supplied token scope was not acceptable. Verify authentication and try again. |
| 403   Forbidden | The request was successfully validated but lacking the required permissions. Verify your credentials and permissions before you send this request again. |
| 404   Not Found | The requested resource was not found. Review the request and try again. |
| 500   Internal Server Error | An unexpected error occurred on the server, preventing it from completing your request. Please try again later. If the issue persists, contact the support team for assistance. |

### Response

## [Header (200)](#header-200)

| x-ads-app-identifier   string | The service identifier. Comprises of the service name, version, and environment. |
| --- | --- |
| x-ads-startup-time   string | The service startup time, in the following date format: `EEE MMM dd HH:mm:ss Z yyyy`. |
| x-ads-duration   string | The amount of time spent servicing the request, in milliseconds. |
| x-ads-troubleshooting   string | Provides information about server failures, if any. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| urn   string | The URL-safe Base64 encoded URN of the source design. |
| --- | --- |
| derivatives   array: object | An array of objects, where each object represents a derivative of the source design. |
| name   string | The name of the source design. |
| hasThumbnail   string | `true` - The derivative has a thumbnail.`false` - The derivative does not have a thumbnail. |
| progress   string | Indicates the progress of the process generating this derivative, as a percentage. Once complete, the value changes to `complete`. |
| outputType   string | The file type/format of the derivative. Possible values are: `dwg`, `fbx`, `ifc`, `iges`, `obj` , `step`, `stl`, `svf`, `svf2`, `thumbnail`. |
| properties   object | A JSON object containing metadata extracted from the source design. This metadata provides valuable information about the model, such as its author, client name, project status, and other relevant details. <br>**Note:** This metadata is currently returned for the following source design types:<br>RVT - Revit modelsNWD - Navisworks modelsDWG - AutoCAD models |
| status   string | Status of the task generating this derivative. Possible values are: `pending`, `inprogress`, `success`, `failed`, `timeout`. |
| messages   array: object | An array of objects where each object represents a message logged to the manifest during translation. For example, error messages and warning messages. |
| type   string | Indicates the type of the message. For example, warning indicates a warning message and error indicates an error message. |
| code   string | The ID of the message. For example, the error code reported by an error message. |
| message   object | A human-readable explanation of the event being reported. Can be a string or an array of string. |
| children   array: object | An array of objects, where each object represents a resource generated for the derivative. For example, a Model View (Viewable) of the source design. |
| guid   string | An ID that uniquely identifies the resource. |
| type   string | Type of resource this JSON object represents. |
| urn   string | The URN that you can use to access the resource. |
| role   string | File type of the resource. |
| mime   string | MIME type of the content of the resource. |
| viewableID   string | An ID assigned to a resource that can be displayed in a viewer. |
| name   string | The name of the resource. |
| status   string | Status of the task generating this resource; Possible values are: `pending`, `inprogress`, `success`, `failed`, `timeout` |
| hasThumbnail   string | `true` - There is a thumbnail for the resource.`false` - There is no thumbnail for the resource. |
| progress   string | Indicates the progress of the process generating this resource, as a percentage. Once complete, the value changes to `complete`. |
| phaseNames   object | The name of the phase the resource file was generated from. This attribute is present only on Model Views (Viewables) generated from a Revit source design. This attribute can be a string (for Revit non-sheet 2D or 3D views) or an array of strings (for Revit sheet views). |
| phaseIds   object | The unique ID of the phase the resource file was generated from. This attribute is present only on Model Views (Viewables) generated from a Revit source design. This attribute can be a string (for Revit non-sheet 2D or 3D views) or an array of strings (for Revit sheet views). |
| camera   array: number | The default viewpoint of a viewable 3D resource. |
| resolution   array: integer | An array of two integers where the first number represents the width of a thumbnail in pixels, and the second the height. Available only for thumbnail resources. |
| messages   array: object |  |
| type   string | Indicates the type of the message. For example, warning indicates a warning message and error indicates an error message. |
| code   string | The ID of the message. For example, the error code reported by an error message. |
| message   object | A human-readable explanation of the event being reported. Can be a string or an array of string. |
| children   array: object | An optional array of objects, where each object (of type `children`) represents another resource generated for this resource. |
| hasThumbnail   string | `true` - There is a thumbnail for the source design.`false` - There is no thumbnail for the source design. |
| progress   string | Indicates the overall progress of all translation jobs, as a percentage. Once all requested derivatives are generated, the value changes to `complete`. |
| type   string | The type of data that is returned. Always `manifest`. |
| region   string | Specifies the data center where the manifest, derivatives, and references are stored. Possible values are: <br>`US` - Data center for the US region.`EMEA` - Data center for European Union, Middle East, and Africa.`AUS` - Data center for the Australia region.`CAN` - Data center for the Canada region.`DEU` - Data center for the Germany region.`IND` - Data center for the India region.`JPN` - Data center for the Japan region.`GBR` - Data center for the United Kingdom region. |
| version   string | Indicates the version of the schema that the manifest is based on. |
| status   string | Overall status of all translation jobs for the source design. Possible values are: `pending`, `success`, `inprogress`, `failed`, `timeout`. |

Hint:

The following examples return raw HTTP headers and JSON objects. For a more developer-friendly experience, consider using our [TypeScript SDK](/en/docs/model-derivative/v2/reference/typescript-sdk/) or [.NET SDK](/en/docs/model-derivative/v2/reference/dot-net-sdk). Both provide strongly typed data with IntelliSense support, offering code completion, error checking, and tooltips that reduce the need to reference JSON schemas.

 

## [Example 1](#example-1)

This example shows what happens when you request a manifest before translation has begun.

### Request

cURL

```
curl --location 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest' \
--header 'Authorization: Bearer eyJh...' \
--header 'Content-Type: application/json'

```

JavaScript (Fetch)

```
// Create a new Headers object and set the required headers
const myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer eyJh..."); // Replace with your access token
myHeaders.append("Content-Type", "application/json");

// Set up the request options for the fetch call
const requestOptions = {
  method: "GET",
  headers: myHeaders,
  redirect: "follow"
};

// Make the GET request to the Model Derivative API for the manifest
fetch("https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest", requestOptions)
  .then((response) => response.text()) // Parse the response as text
  .then((result) => console.log(result)) // Log the result to the console
  .catch((error) => console.error(error)); // Log any errors

```

Show More

C# (HttpClient)

```
// Create a new HttpClient instance
var client = new HttpClient();

// Create a new HttpRequestMessage for the GET request
var request = new HttpRequestMessage(HttpMethod.Get, "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest");

// Add the Authorization header with your access token
request.Headers.Add("Authorization", "Bearer eyJh...");

// Create an empty StringContent and set the Content-Type header
var content = new StringContent(string.Empty);
content.Headers.ContentType = new MediaTypeHeaderValue("application/json");
request.Content = content;

// Send the request asynchronously and get the response
var response = await client.SendAsync(request);

// Throw an exception if the response indicates an error
response.EnsureSuccessStatusCode();

// Read and print the response content as a string
Console.WriteLine(await response.Content.ReadAsStringAsync());

```

Show More

Python (Requests)

```
import requests
import json

# Set the API endpoint URL for the manifest request
url = "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest"

# No payload is needed for a GET request
payload = {}

# Set the required headers, including your access token
headers = {
    'Authorization': 'Bearer eyJh...',  # Replace with your access token
    'Content-Type': 'application/json'
}

# Make the GET request to the Model Derivative API
response = requests.request("GET", url, headers=headers, data=payload)

# Print the response text (the manifest)
print(response.text)

```

Show More

### Response

```
{
  "type": "manifest",
  "hasThumbnail": "false",
  "status": "pending",
  "progress": "0% complete",
  "region": "US",
  "urn": "dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA",
  "derivatives": [
  ]
}

```

Show More

## [Example 2](#example-2)

This example shows what happens when you request a manifest when translation has successfully completed.

### Request

cURL

```
curl --location 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest' \
--header 'Authorization: Bearer eyJh...' \
--header 'Content-Type: application/json'

```

JavaScript (Fetch)

```
// Create a new Headers object and set the required headers
const myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer eyJh..."); // Replace with your access token
myHeaders.append("Content-Type", "application/json");

// Set up the request options for the fetch call
const requestOptions = {
  method: "GET",
  headers: myHeaders,
  redirect: "follow"
};

// Make the GET request to the Model Derivative API for the manifest
fetch("https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest", requestOptions)
  .then((response) => response.text()) // Parse the response as text
  .then((result) => console.log(result)) // Log the result to the console
  .catch((error) => console.error(error)); // Log any errors

```

Show More

C# (HttpClient)

```
// Create a new HttpClient instance
var client = new HttpClient();

// Create a new HttpRequestMessage for the GET request
var request = new HttpRequestMessage(HttpMethod.Get, "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest");

// Add the Authorization header with your access token
request.Headers.Add("Authorization", "Bearer eyJh...");

// Create an empty StringContent and set the Content-Type header
var content = new StringContent(string.Empty);
content.Headers.ContentType = new MediaTypeHeaderValue("application/json");
request.Content = content;

// Send the request asynchronously and get the response
var response = await client.SendAsync(request);

// Throw an exception if the response indicates an error
response.EnsureSuccessStatusCode();

// Read and print the response content as a string
Console.WriteLine(await response.Content.ReadAsStringAsync());

```

Show More

Python (Requests)

```
import requests
import json

# Set the API endpoint URL for the manifest request
url = "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest"

# No payload is needed for a GET request
payload = {}

# Set the required headers, including your access token
headers = {
    'Authorization': 'Bearer eyJh...',  # Replace with your access token
    'Content-Type': 'application/json'
}

# Make the GET request to the Model Derivative API
response = requests.request("GET", url, headers=headers, data=payload)

# Print the response text (the manifest)
print(response.text)

```

Show More

### Response

```
{
  "type": "manifest",
  "hasThumbnail": "true",
  "status": "inprogress",
  "progress": "99% complete",
  "region": "US",
  "urn": "dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA",
  "derivatives": [
    {
      "name": "A5.iam",
      "hasThumbnail": "true",
      "status": "success",
      "progress": "99% complete",
      "outputType": "svf",
      "children": [
        {
          "guid": "d998268f-eeb4-da87-0db4-c5dbbc4926d0",
          "type": "geometry",
          "role": "3d",
          "name": "Scene",
          "status": "success",
          "progress": "99% complete",
          "hasThumbnail": "true",
          "children": [
            {
              "guid": "4f981e94-8241-4eaf-b08b-cd337c6b8b1f",
              "type": "resource",
              "progress": "99% complete",
              "role": "graphics",
              "mime": "application/autodesk-svf"
            },
            {
              "guid": "d718eb7e-fa8a-42f9-8b32-e323c0fbea0c",
              "type": "resource",
              "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/output/1/A5.svf.png01_thumb_400x400.png",
              "resolution": [
                400.0,
                400.0
              ],
              "mime": "image/png",
              "role": "thumbnail"
            },
            {
              "guid": "34dc340b-835f-47f7-9da5-b8219aefe741",
              "type": "resource",
              "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/output/1/A5.svf.png01_thumb_200x200.png",
              "resolution": [
                200.0,
                200.0
              ],
              "mime": "image/png",
              "role": "thumbnail"
            },
            {
              "guid": "299c6ba6-650e-423e-bbd6-3aaff44ee104",
              "type": "resource",
              "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/output/1/A5.svf.png01_thumb_100x100.png",
              "resolution": [
                100.0,
                100.0
              ],
              "mime": "image/png",
              "role": "thumbnail"
            }
          ]
        }
      ]
    }
  ]
}

```

Show More

## [Example 3](#example-3)

This example shows what happens when you request a manifest when a translation has failed.

### Request

cURL

```
curl --location 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest' \
--header 'Authorization: Bearer eyJh...' \
--header 'Content-Type: application/json'

```

JavaScript (Fetch)

```
// Create a new Headers object and set the required headers
const myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer eyJh..."); // Replace with your access token
myHeaders.append("Content-Type", "application/json");

// Set up the request options for the fetch call
const requestOptions = {
  method: "GET",
  headers: myHeaders,
  redirect: "follow"
};

// Make the GET request to the Model Derivative API for the manifest
fetch("https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest", requestOptions)
  .then((response) => response.text()) // Parse the response as text
  .then((result) => console.log(result)) // Log the result to the console
  .catch((error) => console.error(error)); // Log any errors

```

Show More

C# (HttpClient)

```
// Create a new HttpClient instance
var client = new HttpClient();

// Create a new HttpRequestMessage for the GET request
var request = new HttpRequestMessage(HttpMethod.Get, "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest");

// Add the Authorization header with your access token
request.Headers.Add("Authorization", "Bearer eyJh...");

// Create an empty StringContent and set the Content-Type header
var content = new StringContent(string.Empty);
content.Headers.ContentType = new MediaTypeHeaderValue("application/json");
request.Content = content;

// Send the request asynchronously and get the response
var response = await client.SendAsync(request);

// Throw an exception if the response indicates an error
response.EnsureSuccessStatusCode();

// Read and print the response content as a string
Console.WriteLine(await response.Content.ReadAsStringAsync());

```

Show More

Python (Requests)

```
import requests
import json

# Set the API endpoint URL for the manifest request
url = "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest"

# No payload is needed for a GET request
payload = {}

# Set the required headers, including your access token
headers = {
    'Authorization': 'Bearer eyJh...',  # Replace with your access token
    'Content-Type': 'application/json'
}

# Make the GET request to the Model Derivative API
response = requests.request("GET", url, headers=headers, data=payload)

# Print the response text (the manifest)
print(response.text)

```

Show More

### Response

```
{
  "type": "manifest",
  "hasThumbnail": "false",
  "status": "failed",
  "progress": "complete",
  "region": "US",
  "urn": "dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA",
  "derivatives": [
    {
      "name": "A5.iam",
      "hasThumbnail": "false",
      "status": "failed",
      "progress": "complete",
      "messages": [
        {
          "type": "warning",
          "message": "The drawing's thumbnails were not properly created.",
          "code": "TranslationWorker-ThumbnailGenerationFailed"
        }
      ],
      "outputType": "svf",
      "children": [
        {
          "guid": "d998268f-eeb4-da87-0db4-c5dbbc4926d0",
          "type": "geometry",
          "role": "3d",
          "name": "Scene",
          "status": "success",
          "messages": [
            {
              "type": "warning",
              "code": "ATF-1023",
              "message": [
                "The file: {0} does not exist.",
                "C:\\Users\\ADSK\\Documents\\A5\\Top.ipt"
              ]
            },
            {
              "type": "warning",
              "code": "ATF-1023",
              "message": [
                "The file: {0} does not exist.",
                "C:\\Users\\ADSK\\Documents\\A5\\Bottom.ipt"
              ]
            },
            {
              "type": "error",
              "code": "ATF-1026",
              "message": [
                "The file: {0} is empty.",
                "C:/worker/viewing-inventor-lmv/tmp/job-1/5/output/1/A5.svf"
              ]
            }
          ],
          "progress": "complete",
          "hasThumbnail": "false",
          "children": [
            {
              "guid": "4f981e94-8241-4eaf-b08b-cd337c6b8b1f",
              "type": "resource",
              "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/output/1/A5.svf",
              "role": "graphics",
              "mime": "application/autodesk-svf"
            }
          ]
        }
      ]
    }
  ]
}

```

Show More

## [Example 4](#example-4)

This example demonstrates the successful response to a request for a manifest generated for a Revit model translated to the SVF format.

### Request

cURL

```
curl --location 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMS9MaW5rJTIwQXJjXzIwMTgucnZ0/manifest' \
--header 'Authorization: Bearer eyJh...' \
--header 'Content-Type: application/json'

```

JavaScript (Fetch)

```
// Create a new Headers object and set the required headers
const myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer eyJh..."); // Replace with your access token
myHeaders.append("Content-Type", "application/json");

// Set up the request options for the fetch call
const requestOptions = {
  method: "GET",
  headers: myHeaders,
  redirect: "follow"
};

// Make the GET request to the Model Derivative API for the manifest
fetch("https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMS9MaW5rJTIwQXJjXzIwMTgucnZ0/manifest", requestOptions)
  .then((response) => response.text()) // Parse the response as text
  .then((result) => console.log(result)) // Log the result to the console
  .catch((error) => console.error(error)); // Log any errors

```

Show More

C# (HttpClient)

```
// Create a new HttpClient instance
var client = new HttpClient();

// Create a new HttpRequestMessage for the GET request
var request = new HttpRequestMessage(HttpMethod.Get, "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMS9MaW5rJTIwQXJjXzIwMTgucnZ0/manifest");

// Add the Authorization header with your access token
request.Headers.Add("Authorization", "Bearer eyJh...");

// Create an empty StringContent and set the Content-Type header
var content = new StringContent(string.Empty);
content.Headers.ContentType = new MediaTypeHeaderValue("application/json");
request.Content = content;

// Send the request asynchronously and get the response
var response = await client.SendAsync(request);

// Throw an exception if the response indicates an error
response.EnsureSuccessStatusCode();

// Read and print the response content as a string
Console.WriteLine(await response.Content.ReadAsStringAsync());

```

Show More

Python (Requests)

```
import requests
import json

# Set the API endpoint URL for the manifest request
url = "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMS9MaW5rJTIwQXJjXzIwMTgucnZ0/manifest"

# No payload is needed for a GET request
payload = {}

# Set the required headers, including your access token
headers = {
    'Authorization': 'Bearer eyJh...',  # Replace with your access token
    'Content-Type': 'application/json'
}

# Make the GET request to the Model Derivative API
response = requests.request("GET", url, headers=headers, data=payload)

# Print the response text (the manifest)
print(response.text)

```

Show More

### Response

```
{
    "urn": "dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMS9MaW5rJTIwQXJjXzIwMTgucnZ0",
    "derivatives": [
        {
            "hasThumbnail": "true",
            "children": [
                {
                    "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMS9MaW5rJTIwQXJjXzIwMTgucnZ0/output/Resource/model.sdb",
                    "role": "Autodesk.CloudPlatform.PropertyDatabase",
                    "mime": "application/autodesk-db",
                    "guid": "6fac95cb-af5d-3e4f-b943-8a7f55847ff1",
                    "type": "resource",
                    "status": "success"
                },
                {
                    "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMS9MaW5rJTIwQXJjXzIwMTgucnZ0/output/Resource/AECModelData.json",
                    "role": "Autodesk.AEC.ModelData",
                    "mime": "application/json",
                    "guid": "a4aac952-a3f4-031c-4113-b2d9ac2d0de6",
                    "type": "resource",
                    "status": "success"
                },
                {
                    "guid": "02efa4e8-11ec-5b90-1c0b-4775bad24b58",
                    "type": "geometry",
                    "role": "3d",
                    "name": "3D",
                    "viewableID": "92b5dec7-790a-45b0-a5e8-cd9f76058c3a-0004bdc0",
                    "phaseNames": "New Construction",
                    "status": "success",
                    "hasThumbnail": "true",
                    "progress": "complete",
                    "children": [
                        {
                            "guid": "92b5dec7-790a-45b0-a5e8-cd9f76058c3a-0004bdc0",
                            "type": "view",
                            "role": "3d",
                            "name": "3D",
                            "status": "success",
                            "progress": "complete",
                            "camera": [
                                63.460731506347656,
                                -69.05099487304688,
                                85.06072235107422,
                                -12.099991798400879,
                                6.50972843170166,
                                9.5,
                                -0.40824830532073975,
                                0.40824830532073975,
                                0.8164966106414795,
                                1.3879648447036743,
                                0,
                                1,
                                1
                            ]
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMS9MaW5rJTIwQXJjXzIwMTgucnZ0/output/Resource/3D View/3D/3D.svf",
                            "role": "graphics",
                            "mime": "application/autodesk-svf",
                            "guid": "1821b502-b91e-f9f2-56e9-2d7cb4b0f4a3",
                            "type": "resource"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMS9MaW5rJTIwQXJjXzIwMTgucnZ0/output/Resource/3D View/3D/3D1.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "c70aa596-d404-714f-6795-9276087c3800",
                            "type": "resource",
                            "resolution": [
                                100,
                                100
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMS9MaW5rJTIwQXJjXzIwMTgucnZ0/output/Resource/3D View/3D/3D2.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "6ef65d1a-4a59-111d-f1ec-4e543bd2712b",
                            "type": "resource",
                            "resolution": [
                                200,
                                200
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMS9MaW5rJTIwQXJjXzIwMTgucnZ0/output/Resource/3D View/3D/3D4.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "2c06739e-5164-4f6d-450e-c8833fd2a2ba",
                            "type": "resource",
                            "resolution": [
                                400,
                                400
                            ],
                            "status": "success"
                        }
                    ]
                }
            ],
            "name": "Link Arc_2018.rvt",
            "progress": "complete",
            "outputType": "svf",
            "status": "success"
        },
        {
            "children": [
                {
                    "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMS9MaW5rJTIwQXJjXzIwMTgucnZ0/output/preview1.png",
                    "role": "thumbnail",
                    "mime": "image/png",
                    "guid": "db899ab5-939f-e250-d79d-2d1637ce4565",
                    "type": "resource",
                    "resolution": [
                        100,
                        100
                    ],
                    "status": "success"
                },
                {
                    "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMS9MaW5rJTIwQXJjXzIwMTgucnZ0/output/preview2.png",
                    "role": "thumbnail",
                    "mime": "image/png",
                    "guid": "3f6c118d-f551-7bf0-03c9-8548d26c9772",
                    "type": "resource",
                    "resolution": [
                        200,
                        200
                    ],
                    "status": "success"
                },
                {
                    "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMS9MaW5rJTIwQXJjXzIwMTgucnZ0/output/preview4.png",
                    "role": "thumbnail",
                    "mime": "image/png",
                    "guid": "4e751806-0920-ce32-e9fd-47c3cec21536",
                    "type": "resource",
                    "resolution": [
                        400,
                        400
                    ],
                    "status": "success"
                }
            ],
            "progress": "complete",
            "outputType": "thumbnail",
            "status": "success"
        }
    ],
    "hasThumbnail": "true",
    "progress": "complete",
    "type": "manifest",
    "region": "US",
    "version": "1.0",
    "status": "success"
}

```

Show More

## [Example 5](#example-5)

This example demonstrates the successful response to a request for a manifest generated for a Revit model translated to the SVF2 format.

### Request

cURL

```
curl --location 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMi9MaW5rJTIwQXJjXzIwMTgucnZ0/manifest' \
--header 'Authorization: Bearer eyJh...' \
--header 'Content-Type: application/json'

```

JavaScript (Fetch)

```
// Create a new Headers object and set the required headers
const myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer eyJh..."); // Replace with your access token
myHeaders.append("Content-Type", "application/json");

// Set up the request options for the fetch call
const requestOptions = {
  method: "GET",
  headers: myHeaders,
  redirect: "follow"
};

// Make the GET request to the Model Derivative API for the manifest
fetch("https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMi9MaW5rJTIwQXJjXzIwMTgucnZ0/manifest", requestOptions)
  .then((response) => response.text()) // Parse the response as text
  .then((result) => console.log(result)) // Log the result to the console
  .catch((error) => console.error(error)); // Log any errors

```

Show More

C# (HttpClient)

```
// Create a new HttpClient instance
var client = new HttpClient();

// Create a new HttpRequestMessage for the GET request
var request = new HttpRequestMessage(HttpMethod.Get, "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMi9MaW5rJTIwQXJjXzIwMTgucnZ0/manifest");

// Add the Authorization header with your access token
request.Headers.Add("Authorization", "Bearer eyJh...");

// Create an empty StringContent and set the Content-Type header
var content = new StringContent(string.Empty);
content.Headers.ContentType = new MediaTypeHeaderValue("application/json");
request.Content = content;

// Send the request asynchronously and get the response
var response = await client.SendAsync(request);

// Throw an exception if the response indicates an error
response.EnsureSuccessStatusCode();

// Read and print the response content as a string
Console.WriteLine(await response.Content.ReadAsStringAsync());

```

Show More

Python (Requests)

```
import requests
import json

# Set the API endpoint URL for the manifest request
url = "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMi9MaW5rJTIwQXJjXzIwMTgucnZ0/manifest"

# No payload is needed for a GET request
payload = {}

# Set the required headers, including your access token
headers = {
    'Authorization': 'Bearer eyJh...',  # Replace with your access token
    'Content-Type': 'application/json'
}

# Make the GET request to the Model Derivative API
response = requests.request("GET", url, headers=headers, data=payload)

# Print the response text (the manifest)
print(response.text)

```

Show More

### Response

```
{
    "urn": "dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMi9MaW5rJTIwQXJjXzIwMTgucnZ0",
    "derivatives": [
        {
            "hasThumbnail": "true",
            "children": [
                {
                    "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMi9MaW5rJTIwQXJjXzIwMTgucnZ0/output/Resource/model.sdb",
                    "role": "Autodesk.CloudPlatform.PropertyDatabase",
                    "mime": "application/autodesk-db",
                    "guid": "6fac95cb-af5d-3e4f-b943-8a7f55847ff1",
                    "type": "resource",
                    "status": "success"
                },
                {
                    "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMi9MaW5rJTIwQXJjXzIwMTgucnZ0/output/Resource/AECModelData.json",
                    "role": "Autodesk.AEC.ModelData",
                    "mime": "application/json",
                    "guid": "a4aac952-a3f4-031c-4113-b2d9ac2d0de6",
                    "type": "resource",
                    "status": "success"
                },
                {
                    "phaseNames": "New Construction",
                    "role": "3d",
                    "hasThumbnail": "true",
                    "children": [
                        {
                            "guid": "92b5dec7-790a-45b0-a5e8-cd9f76058c3a-0004bdc0",
                            "type": "view",
                            "role": "3d",
                            "name": "3D",
                            "status": "success",
                            "progress": "complete",
                            "camera": [
                                63.460731506347656,
                                -69.05099487304688,
                                85.06072235107422,
                                -12.099991798400879,
                                6.50972843170166,
                                9.5,
                                -0.40824830532073975,
                                0.40824830532073975,
                                0.8164966106414795,
                                1.3879648447036743,
                                0,
                                1,
                                1
                            ]
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMi9MaW5rJTIwQXJjXzIwMTgucnZ0/output/Resource/3D View/3D/3D1.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "c70aa596-d404-714f-6795-9276087c3800",
                            "type": "resource",
                            "resolution": [
                                100,
                                100
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMi9MaW5rJTIwQXJjXzIwMTgucnZ0/output/Resource/3D View/3D/3D2.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "6ef65d1a-4a59-111d-f1ec-4e543bd2712b",
                            "type": "resource",
                            "resolution": [
                                200,
                                200
                            ],
                            "status": "success"
                        },
                        {
                            "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMi9MaW5rJTIwQXJjXzIwMTgucnZ0/output/Resource/3D View/3D/3D4.png",
                            "role": "thumbnail",
                            "mime": "image/png",
                            "guid": "2c06739e-5164-4f6d-450e-c8833fd2a2ba",
                            "type": "resource",
                            "resolution": [
                                400,
                                400
                            ],
                            "status": "success"
                        },
                        {
                            "role": "graphics",
                            "mime": "application/autodesk-svf2",
                            "guid": "1821b502-b91e-f9f2-56e9-2d7cb4b0f4a3",
                            "type": "resource"
                        }
                    ],
                    "name": "3D",
                    "guid": "02efa4e8-11ec-5b90-1c0b-4775bad24b58",
                    "progress": "complete",
                    "type": "geometry",
                    "viewableID": "92b5dec7-790a-45b0-a5e8-cd9f76058c3a-0004bdc0",
                    "status": "success"
                }
            ],
            "name": "Link Arc_2018.rvt",
            "progress": "complete",
            "outputType": "svf2",
            "status": "success"
        },
        {
            "children": [
                {
                    "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMi9MaW5rJTIwQXJjXzIwMTgucnZ0/output/preview1.png",
                    "role": "thumbnail",
                    "mime": "image/png",
                    "guid": "db899ab5-939f-e250-d79d-2d1637ce4565",
                    "type": "resource",
                    "resolution": [
                        100,
                        100
                    ],
                    "status": "success"
                },
                {
                    "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMi9MaW5rJTIwQXJjXzIwMTgucnZ0/output/preview2.png",
                    "role": "thumbnail",
                    "mime": "image/png",
                    "guid": "3f6c118d-f551-7bf0-03c9-8548d26c9772",
                    "type": "resource",
                    "resolution": [
                        200,
                        200
                    ],
                    "status": "success"
                },
                {
                    "urn": "urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6c3ZmX3NhbXBsZV8wMi9MaW5rJTIwQXJjXzIwMTgucnZ0/output/preview4.png",
                    "role": "thumbnail",
                    "mime": "image/png",
                    "guid": "4e751806-0920-ce32-e9fd-47c3cec21536",
                    "type": "resource",
                    "resolution": [
                        400,
                        400
                    ],
                    "status": "success"
                }
            ],
            "progress": "complete",
            "outputType": "thumbnail",
            "status": "success"
        }
    ],
    "hasThumbnail": "true",
    "progress": "complete",
    "type": "manifest",
    "region": "US",
    "version": "1.0",
    "status": "success"
}

```

Show More
