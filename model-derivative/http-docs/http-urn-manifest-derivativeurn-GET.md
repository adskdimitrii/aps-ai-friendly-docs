# modelderivative/v2/designdata/{urn}/manifest/{derivativeUrn}

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/reference/http/urn-manifest-derivativeurn-GET/

---

Download Derivative (Deprecated)

GET

# modelderivative/v2/designdata/{urn}/manifest/{derivativeUrn}

Deprecated

**Note:** This operation is deprecated. Beyond December 2022 we will only provide minimal support for this operation. So, please do not use this operation to download derivatives. Instead, use [Fetch Derivative Download URL](https://aps.autodesk.com/en/docs/model-derivative/v2/reference/http/urn-manifest-derivativeurn-signedcookies-GET/) to obtain a download URL and a set of signed cookies to securely download derivatives.

Downloads the derivative specified by the `derivativeUrn` URI parameter, which was generated from the source model specified by the `urn` URI parameter.

Note that the Model Derivative API uses 2 types of URNs. The **design URN** is generated when you upload the source design file to APS, and is used when calling most of the Model Derivative operations. A **derivative URN** is generated for each translated output file format, which is the URN you specify as the `derivativeUrn` URI parameter for this operation. To obtain the derivative URN, inspect the manifest of the translation job. Use [Fetch Manifest](http-urn-manifest-GET.md) to obtain the manifest of the translation job. See the [Translate a Source File](../how-to-docs/translate-to-obj-task3-translate-source-file.md) for a demonstration on how to obtain the **deriviative URN** and how to download a derivative.

**Note:** 3D SVF2 derivatives cannot be downloaded.

**Tip:** Before calling this endpoint, call [Check Derivative Details](http-urn-manifest-derivativeurn-HEAD.md) to determine the total content length. If the derivative is large, use the `Range` header to download the derivative in chunks.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/modelderivative/v2/designdata/{urn}/manifest/{derivativeUrn} |
| --- | --- |
| Authentication Context | User context optional |
| Required OAuth Scopes | `data:read` `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a two-legged access token obtained via a [Client Credentials Grant flow](../../oauth/how-to-docs/get-2-legged-token.md), or a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). <br>The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context. |
| --- | --- |
| Range   string | Specifies the byte range to download. Use this header to download a derivative in chunks, by requesting only a specific portion of the derivative. If not specified, the entire derivative is returned. <br>The format for specifying a range is `Range:bytes=start-end`, where:<br>`start` is the starting byte offset (inclusive).`end` is the ending byte offset (inclusive). If omitted, returns all bytes from the `start` offset to the end of the derivative.<br>For example:<br>`Range:bytes=0-63` - Returns the first 64 bytes`Range:bytes=64-127` - Returns the second set of 64 bytes`Range:bytes=1022` - Returns all the bytes from offset 1022 to the end<br>**Note:** You can specify only one range per request. |
| region   string | Specifies the data center where the manifest and derivatives of the specified source design are stored. Possible values are: <br>`US` - (Default) Data center for the US region.`EMEA` - Data center for the European Union, Middle East, and Africa.`AUS` - Data center for the Australia region.`CAN` - Data center for the Canada region.`DEU` - Data center for the Germany region.`IND` - Data center for the India region.`JPN` - Data center for the Japan region.`GBR` - Data center for the United Kingdom region. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| urn   string | The URL-safe Base64 encoded URN of the source design. This value is used as the `urn` URI parameter in operations to access data for this source design. |
| --- | --- |
| derivativeUrn   string | The URL-encoded URN of the derivative. Check the manifest of the source design to get the URNs of the derivatives available for download. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The requested bytes were successfully retrieved. |
| --- | --- |
| 400   Bad Request | The server was unable to process the request. The syntax of the request is malformed or the request is missing a required header. Do not repeat the request without fixing the issue. The response body may indicate what is wrong with the request. |
| 401   Unauthorized | The supplied authorization header was not valid or the supplied token scope was not acceptable. Verify authentication and try again. |
| 403   Forbidden | The request was successfully validated but lacking the required permissions. Verify your credentials and permissions before you send this request again. |
| 404   Not Found | The requested resource was not found. Review the request and try again. |
| 413 | The request could not be completed because the requested resource exceeded the maximum allowed size of 256 MB. Please use a range request to retrieve the resource in smaller chunks, or contact the support team for assistance with large files. |
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

Hint:

The following examples return raw HTTP headers and JSON objects. For a more developer-friendly experience, consider using our [TypeScript SDK](https://aps.autodesk.com/en/docs/model-derivative/v2/reference/typescript-sdk/) or [.NET SDK](https://aps.autodesk.com/en/docs/model-derivative/v2/reference/dot-net-sdk/). Both provide strongly typed data with IntelliSense support, offering code completion, error checking, and tooltips that reduce the need to reference JSON schemas.

 

## [Example 1](#example-1)

This example demonstrates the successful retrieval of a complete derivative (200).

### Request

cURL

```
curl \
  --location 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest/urn%3Aadsk.viewing%3Afs.file%3AdXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA%2Foutput%2F1%2FA5.svf' \
  --header 'Authorization: Bearer eyJh...'

```

JavaScript (Fetch)

```
// Define the URL for the GET request
const url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest/urn%3Aadsk.viewing%3Afs.file%3AdXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA%2Foutput%2F1%2FA5.svf';

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
var request = new HttpRequestMessage(HttpMethod.Get, "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest/urn%3Aadsk.viewing%3Afs.file%3AdXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA%2Foutput%2F1%2FA5.svf");

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
url = "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest/urn%3Aadsk.viewing%3Afs.file%3AdXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA%2Foutput%2F1%2FA5.svf"

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
Status Code: 200 OK
Content-Type=application/octet-stream
Content-Length:1658
Etag: urn%3Aadsk.viewing%3Afs.file%3AdXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA%2Foutput%2F1%2FA5.svf
x-ads-app-identifier:platform-viewing-2016.05.03.1102.2f6bfbf-production
x-ads-startup-time:Wed May 11 14:03:54 CST 2016
x-ads-duration:280 ms

with chunked content body

```

Show More

## [Example 2](#example-2)

This example demonstrates the successful retrieval of a partial derivative (206).

### Request

cURL

```
curl \
  --location 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest/urn%3Aadsk.viewing%3Afs.file%3AdXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA%2Foutput%2F1%2FA5.svf' \
  --header 'Authorization: Bearer eyJh...' \
  --header 'Range: bytes=0-100'

```

JavaScript (Fetch)

```
// Define the URL for the GET request
const url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest/urn%3Aadsk.viewing%3Afs.file%3AdXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA%2Foutput%2F1%2FA5.svf';

// Define the request options, including the HTTP method and headers
const options = {
    method: 'GET',
    headers: {
        'Authorization': 'Bearer eyJh...',
        'Range': 'bytes=0-100'
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
var request = new HttpRequestMessage(HttpMethod.Get, "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest/urn%3Aadsk.viewing%3Afs.file%3AdXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA%2Foutput%2F1%2FA5.svf");

request.Headers.Add("Authorization", "Bearer eyJh...");
request.Headers.Add("Range", "bytes=0-100");

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
url = "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest/urn%3Aadsk.viewing%3Afs.file%3AdXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA%2Foutput%2F1%2FA5.svf"

# Define the headers
headers = {
    'Authorization': 'Bearer eyJh...',
    'Range': 'bytes=0-100',
}

# Make the GET request using the requests library
response = requests.get(url, headers=headers)

# Print the response content to the console
print(response.text)

```

Show More

### Response

```
Status Code: 206 Partial Content
Content-Range=bytes 0-100/1658
Content-Type=application/octet-stream
Content-Length:1658
Etag: urn%3Aadsk.viewing%3Afs.file%3AdXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA%2Foutput%2F1%2FA5.svf
x-ads-app-identifier:platform-viewing-2016.05.03.1102.2f6bfbf-production
x-ads-startup-time:Wed May 11 14:03:54 CST 2016
x-ads-duration:280 ms

with chunked partial content body

```

Show More
