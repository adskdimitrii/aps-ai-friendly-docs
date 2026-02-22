# modelderivative/v2/designdata/{urn}/thumbnail

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/reference/http/urn-thumbnail-GET/

---

Fetch Thumbnail

GET

# modelderivative/v2/designdata/{urn}/thumbnail

Retrieves a thumbnail of the specified source design.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/modelderivative/v2/designdata/{urn}/thumbnail |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

- Authorization*string Must be `Bearer <token>`, where `<token>` is a two-legged access token obtained via a [Client Credentials Grant flow](/en/docs/oauth/v2/tutorials/get-2-legged-token/), or a three-legged access token obtained via an [Authorization Code flow](/en/docs/oauth/v2/tutorials/get-3-legged-token/) or a [Secure Service Account flow](/en/docs/ssa/v1/tutorials/getting-started-with-ssa/task3-generate-3-legged-access-token/). The Secure Service Account flow generates tokens without user interaction but maintains user context for headless server-to-server operations.
- regionstring Specifies the data center where the manifest and derivatives of the specified source design are stored. Possible values are:

- `US` - (Default) Data center for the US region.
- `EMEA` - Data center for the European Union, Middle East, and Africa.
- `AUS` - Data center for the Australia region.
- `CAN` - Data center for the Canada region.
- `DEU` - Data center for the Germany region.
- `IND` - Data center for the India region.
- `JPN` - Data center for the Japan region.
- `GBR` - Data center for the United Kingdom region.

* Required

### Request

## [URI Parameters](#uri-parameters)

| urn   string | The URL-safe Base64 encoded URN of the source design. This value is used as the `urn` URI parameter in operations to access data for this source design. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| width   int | Width of thumbnail in pixels. Possible values: <br>`100` - 100 pixels wide.`200` - 200 pixels wide.`400` - 400 pixels wide.<br>If `width` is omitted, but `height` is specified, `width` defaults to `height`. If both `width` and `height` are omitted, the server will return a thumbnail closest to `200`, if such a thumbnail is available. |
| --- | --- |
| height   int | Height of thumbnails in pixels. Possible values: <br>`100` - 100 pixels high.`200` - 200 pixels high.`400` - 400 pixels high.<br>If `height` is omitted, but `width` is specified, `height` defaults to `width`. If both `width` and `height` are omitted, the server will return a thumbnail closest to `200`, if such a thumbnail is available. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The requested thumbnail was successfully retrieved. |
| --- | --- |
| 400   Bad Request | The server was unable to process the request. The syntax of the request is malformed or the request is missing a required header. Do not repeat the request without fixing the issue. The response body may indicate what is wrong with the request. |
| 401   Unauthorized | The supplied authorization header was not valid or the supplied token scope was not acceptable. Verify authentication and try again. |
| 403   Forbidden | The request was successfully validated but lacking the required permissions. Verify your credentials and permissions before you send this request again. |
| 404   Not Found | The requested resource was not found. Review the request and try again. |
| 500   Internal Server Error | An unexpected error occurred on the server, preventing it from completing your request. Please try again later. If the issue persists, contact the support team for assistance. |

### Response

## [Header (200)](#header-200)

| x-ads-name   string | File name of the thumbnail. |
| --- | --- |
| x-ads-size   string | Thumbnail size. Possible values are: `[100,100]`, `[200,200]`, `[400,400]` |
| x-ads-role   string | The source of the thumbnail. Possible values: <br>`rendered` - Generated pursuant to this operation call.`extracted` - Obtained from the original design file. |
| x-ads-job-status   string | The execution status of the translation job. Possible values: <br>`inprogress` - Translation job is in progress.`success` - Translation job completed successfully.`failed` - Translation job failed.`timedout` - Translation job timed out. |
| x-ads-app-identifier   string | The service identifier. Comprises of the service name, version, and environment. |
| x-ads-startup-time   string | The service startup time, in the following date format: `EEE MMM dd HH:mm:ss Z yyyy`. |
| x-ads-duration   string | The amount of time spent servicing the request, in milliseconds. |
| x-ads-troubleshooting   string | Provides information about server failures, if any. |

The body response is a binary stream of the thumbnail.

Hint:

The following examples return raw HTTP headers and JSON objects. For a more developer-friendly experience, consider using our [TypeScript SDK](/en/docs/model-derivative/v2/reference/typescript-sdk/) or [.NET SDK](/en/docs/model-derivative/v2/reference/dot-net-sdk). Both provide strongly typed data with IntelliSense support, offering code completion, error checking, and tooltips that reduce the need to reference JSON schemas.

 

## [Example 1](#example-1)

This example demonstrates the successful retrieval of a thumbnail (200).

### Request

cURL

```
curl \
  --location 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/thumbnail' \
  --header 'Authorization: Bearer eyJh...'

```

JavaScript (Fetch)

```
// Define the URL for the GET request
const url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/thumbnail';

// Define the request options, including the HTTP method and headers
const options = {
    method: 'GET',
    headers: {
        'Authorization': 'Bearer eyJh...'
    }
};

// Make the GET request using the Fetch API
fetch(url, options)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));

```

Show More

C# (HttpClient)

```
// Create a new instance of HttpClient to send HTTP requests
var client = new HttpClient();

// Create a new HTTP GET request to the specified URL
var request = new HttpRequestMessage(HttpMethod.Get, "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/thumbnail");

request.Headers.Add("Authorization", "Bearer eyJh...");

// Send the HTTP request asynchronously and get the response
var response = await client.SendAsync(request);

// Ensure the response indicates success (status code 200-299)
response.EnsureSuccessStatusCode();

// Read the response content as a string and print it to the console
Console.WriteLine(await response.Content.ReadAsStringAsync());

```

Show More

Python (Requests)

```
# Import the requests library to handle HTTP requests
import requests

# Define the URL for the GET request
url = "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/thumbnail"

# Define the headers
headers = {
    'Authorization': 'Bearer eyJh...',
}

# Make the GET request using the requests library
response = requests.get(url, headers=headers)

# Print the response content to the console
print(response.text)

```

Show More

### Response

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
Cache-Control: public, max-age=86400
Content-Type: image/png
x-ads-app-identifier: platform-viewing-2016.05.03.1102.2f6bfbf-production
x-ads-duration: 142 ms
x-ads-name: 0.svf.png01_thumb_100x100.png
x-ads-job-status: success
x-ads-role: rendered
x-ads-size: [100, 100]
x-ads-startup-time: Thu May 19 10:38:55 UTC 2016
transfer-encoding: chunked
Connection: keep-alive

```

Show More

## [Example 2](#example-2)

This example demonstrates the successful retrieval of a thumbnail with specified dimensions (200).

### Request

cURL

```
curl \
  --location 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/thumbnail?width=400&height=400' \
  --header 'Authorization: Bearer eyJh...'

```

JavaScript (Fetch)

```
// Define the URL for the GET request
const url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/thumbnail?width=400&height=400';

// Define the request options, including the HTTP method and headers
const options = {
    method: 'GET',
    headers: {
        'Authorization': 'Bearer eyJh...'
    }
};

// Make the GET request using the Fetch API
fetch(url, options)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));

```

Show More

C# (HttpClient)

```
// Create a new instance of HttpClient to send HTTP requests
var client = new HttpClient();

// Create a new HTTP GET request to the specified URL
var request = new HttpRequestMessage(HttpMethod.Get, "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/thumbnail?width=400&height=400");

request.Headers.Add("Authorization", "Bearer eyJh...");

// Send the HTTP request asynchronously and get the response
var response = await client.SendAsync(request);

// Ensure the response indicates success (status code 200-299)
response.EnsureSuccessStatusCode();

// Read the response content as a string and print it to the console
Console.WriteLine(await response.Content.ReadAsStringAsync());

```

Show More

Python (Requests)

```
# Import the requests library to handle HTTP requests
import requests

# Define the URL for the GET request
url = "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/thumbnail?width=400&height=400"

# Define the headers
headers = {
    'Authorization': 'Bearer eyJh...',
}

# Make the GET request using the requests library
response = requests.get(url, headers=headers)

# Print the response content to the console
print(response.text)

```

Show More

### Response

```
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
Cache-Control: public, max-age=86400
Content-Type: image/png
x-ads-app-identifier: platform-viewing-2016.05.03.1102.2f6bfbf-production
x-ads-duration: 142 ms
x-ads-name: 0.svf.png01_thumb_400x400.png
x-ads-job-status: success
x-ads-role: rendered
x-ads-size: [400, 400]
x-ads-startup-time: Thu May 19 10:40:25 UTC 2016
transfer-encoding: chunked
Connection: keep-alive

```

Show More
