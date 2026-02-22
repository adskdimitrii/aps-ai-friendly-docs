# modelderivative/v2/designdata/{urn}/manifest

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/reference/http/urn-manifest-DELETE/

---

Delete Manifest

DELETE

# modelderivative/v2/designdata/{urn}/manifest

Deletes the manifest of the specified source design. It also deletes all derivatives (translated output files) generated from the source design. However, it does not delete the source design.

**Note:** This operation is idempotent. If you call it multiple times, even when no manifest exists, it will still return a successful response (200).

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/modelderivative/v2/designdata/{urn}/manifest |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:write` `data:read` |
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

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The manifest was successfully deleted. |
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

### Response

## [Body Structure (200)](#body-structure-200)

| result   string | A message describing outcome of the operation. Always `success` for status `200`. |
| --- | --- |

Hint:

The following examples return raw HTTP headers and JSON objects. For a more developer-friendly experience, consider using our [TypeScript SDK](/en/docs/model-derivative/v2/reference/typescript-sdk/) or [.NET SDK](/en/docs/model-derivative/v2/reference/dot-net-sdk). Both provide strongly typed data with IntelliSense support, offering code completion, error checking, and tooltips that reduce the need to reference JSON schemas.

 

## [Example](#example)

This example demonstrates the successful deletion of a manifest and its derivatives (200).

### Request

cURL

```
curl --location --request DELETE 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest' \
  --header 'Authorization: Bearer eyJh...'

```

JavaScript (Fetch)

```
// Define the URL for the DELETE request
const url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest';

// Define the request options, including the HTTP method and headers
const options = {
    method: 'DELETE',
    headers: {
        'Authorization': 'Bearer eyJh...'
    }
};

// Make the DELETE request using the Fetch API
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

// Create a new HTTP DELETE request to the specified URL
var request = new HttpRequestMessage(HttpMethod.Delete, "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest");

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

# Define the URL for the DELETE request
url = "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWxkZXJpdmF0aXZlL0E1LnppcA/manifest"

# Define the headers
headers = {
    'Authorization': 'Bearer eyJh...',
}

# Make the DELETE request using the requests library
response = requests.delete(url, headers=headers)

# Print the response content to the console
print(response.text)

```

Show More

### Response

```
Status Code: 200 OK
Content-Type:application/json;charset=utf-8
x-ads-app-identifier:platform-viewing-2016.05.03.1102.2f6bfbf-production
x-ads-startup-time:Wed May 11 14:03:54 CST 2016
x-ads-duration:280 ms

{
  "result":"success"
}

```

Show More
