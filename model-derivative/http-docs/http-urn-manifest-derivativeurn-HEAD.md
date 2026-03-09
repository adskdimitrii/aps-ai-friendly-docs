# modelderivative/v2/designdata/{urn}/manifest/{derivativeUrn}

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/reference/http/urn-manifest-derivativeurn-HEAD/

---

Check Derivative Details

HEAD

# modelderivative/v2/designdata/{urn}/manifest/{derivativeUrn}

Retrieves information about the specified derivative.

Use this operation to determine the total content length of a derivative before you download it. If the derivative is large, you can choose to download the derivative in chunks, by specifying a chunk size using the `Range` header parameter.

## [Resource Information](#resource-information)

| Method and URI | HEAD https://developer.api.autodesk.com/modelderivative/v2/designdata/{urn}/manifest/{derivativeUrn} |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

- Authorization*string Must be `Bearer <token>`, where `<token>` is a two-legged access token obtained via a [Client Credentials Grant flow](../../oauth/how-to-docs/get-2-legged-token.md), or a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account flow](https://aps.autodesk.com/en/docs/ssa/v1/tutorials/getting-started-with-ssa/task3-generate-3-legged-access-token/). The Secure Service Account flow generates tokens without user interaction but maintains user context for headless server-to-server operations.
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
| derivativeUrn   string | The URL-encoded URN of the derivative. Check the manifest of the source design to get the URNs of the derivatives available for download. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Information about the specified derivative was successfully retrieved. |
| --- | --- |
| 202   Accepted | The request was accepted but processing is not complete. Repeat the request until you receive an HTTP status of `200`. |
| 400   Bad Request | The server was unable to process the request. The syntax of the request is malformed or the request is missing a required header. Do not repeat the request without fixing the issue. The response body may indicate what is wrong with the request. |
| 401   Unauthorized | The supplied authorization header was not valid or the supplied token scope was not acceptable. Verify authentication and try again. |
| 403   Forbidden | The request was successfully validated but lacking the required permissions. Verify your credentials and permissions before you send this request again. |
| 404   Not Found | The requested resource was not found. Review the request and try again. |
| 500   Internal Server Error | An unexpected error occurred on the server, preventing it from completing your request. Please try again later. If the issue persists, contact the support team for assistance. |

### Response

## [Header (200)](#header-200)

| Content-Type   string | The MIME type of the response content. Always `application/octet-stream` for binary derivative data. |
| --- | --- |
| Content-Length   string | Denotes the size of the specified derivative, in bytes. |
| x-ads-app-identifier   string | The service identifier. Comprises of the service name, version, and environment. |
| x-ads-startup-time   string | The service startup time, in the following date format: `EEE MMM dd HH:mm:ss Z yyyy`. |
| x-ads-duration   string | The amount of time spent servicing the request, in milliseconds. |
| x-ads-troubleshooting   string | Provides information about server failures, if any. |

### Response

## [Body Structure (200)](#body-structure-200)

Response for 200 has no body.

### Response

## [Body Structure (202)](#body-structure-202)

Response for 202 has no body.

Hint:

The following examples return raw HTTP headers and JSON objects. For a more developer-friendly experience, consider using our [TypeScript SDK](https://aps.autodesk.com/en/docs/model-derivative/v2/reference/typescript-sdk/) or [.NET SDK](https://aps.autodesk.com/en/docs/model-derivative/v2/reference/dot-net-sdk/). Both provide strongly typed data with IntelliSense support, offering code completion, error checking, and tooltips that reduce the need to reference JSON schemas.

 

## [Example](#example)

This example demonstrates the successful retrieval of derivativeâs metadata (200).

### Request

cURL

```
curl --location 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest/urn%3Aadsk.viewing%3Afs.file%3AdXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA%2Foutput%2F1%2FA5.svf' \
  --header 'Authorization: Bearer eyJh...'

```

JavaScript (Fetch)

```
// Define the URL for the HEAD request
const url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest/urn%3Aadsk.viewing%3Afs.file%3AdXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA%2Foutput%2F1%2FA5.svf';

// Define the request options, including the HTTP method and headers
const options = {
    method: 'HEAD',
    headers: {
        'Authorization': 'Bearer eyJh...'
    }
};

// Make the HEAD request using the Fetch API
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

// Create a new HTTP HEAD request to the specified URL
var request = new HttpRequestMessage(HttpMethod.Head, "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest/urn%3Aadsk.viewing%3Afs.file%3AdXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA%2Foutput%2F1%2FA5.svf");

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

# Define the URL for the HEAD request
url = "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest/urn%3Aadsk.viewing%3Afs.file%3AdXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA%2Foutput%2F1%2FA5.svf"

# Define the headers
headers = {
    'Authorization': 'Bearer eyJh...',
}

# Make the HEAD request using the requests library
response = requests.head(url, headers=headers)

# Print the response content to the console
print(response.text)

```

Show More

### Response

```
Status Code: 200 OK
Content-Type=application/octet-stream
Content-Length:1658
x-ads-app-identifier:platform-viewing-2016.05.03.1102.2f6bfbf-production
x-ads-startup-time:Wed May 11 14:03:54 CST 2016
x-ads-duration:280 ms

```
