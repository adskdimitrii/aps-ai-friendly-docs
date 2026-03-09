# modelderivative/v2/designdata/{urn}/manifest/{derivativeUrn}/signedcookies

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/reference/http/urn-manifest-derivativeUrn-signedcookies-GET/

---

Fetch Derivative Download URL

GET

# modelderivative/v2/designdata/{urn}/manifest/{derivativeUrn}/signedcookies

Retrieves a download URL and a set of signed cookies that let you securely download the derivative specified by the `derivativeUrn` URI parameter. The signed cookies have a lifetime of 6 hours. You can use range headers with the returned download URL to download the derivative in chunks, in parallel.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/modelderivative/v2/designdata/{urn}/manifest/{derivativeUrn}/signedcookies |
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

| derivativeUrn   string | The URL-encoded URN of the derivative. Use the [Fetch Manifest operation](https://aps.autodesk.com/en/docs/model-derivative/v2/reference/http/manifest/urn-manifest-GET/) to obtain the URNs of derivatives for the specified source design. |
| --- | --- |
| urn   string | The URL-safe Base64 encoded URN of the source design. This value is used as the `urn` URI parameter in operations to access data for this source design. |

### Request

## [Query String Parameters](#query-string-parameters)

| minutes-expiration   int | Specifies how many minutes the signed cookies should remain valid. Default value is 360 minutes. The value you specify must be lower than the default value for this parameter. If you specify a value greater than the default value, the Model Derivative service will return an error with an HTTP status code of `400`. |
| --- | --- |
| response-content-disposition   string | The value that must be specified as the `response-content-disposition` query string parameter with the download URL. Must begin with `attachment`. This value defaults to the default value corresponding to the derivative/file. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The download URL of the specified derivative was successfully retrieved. |
| --- | --- |
| 400   Bad Request | The server was unable to process the request. The syntax of the request is malformed or the request is missing a required header. Do not repeat the request without fixing the issue. The response body may indicate what is wrong with the request. |
| 401   Unauthorized | The supplied authorization header was not valid or the supplied token scope was not acceptable. Verify authentication and try again. |
| 403   Forbidden | The request was successfully validated but lacking the required permissions. Verify your credentials and permissions before you send this request again. |
| 404   Not Found | The requested resource was not found. Review the request and try again. |
| 500   Internal Server Error | An unexpected error occurred on the server, preventing it from completing your request. Please try again later. If the issue persists, contact the support team for assistance. |

### Response

## [Header (200)](#header-200)

| Content-Type   string | The MIME type of the response content. Always `application/octet-stream` for binary derivative data. |
| --- | --- |
| Content-Length   string | Denotes the size of the derivative, in bytes. |
| x-ads-app-identifier   string | The service identifier. Comprises of the service name, version, and environment. |
| x-ads-startup-time   string | The service startup time, in the following date format: `EEE MMM dd HH:mm:ss Z yyyy`. |
| x-ads-duration   string | The amount of time spent servicing the request, in milliseconds. |
| Set-Cookie   string | Signed cookie to use with download URL. There will be three headers in the response named Set-Cookie |

### Response

## [Body Structure (200)](#body-structure-200)

| etag   string | The calculated ETag hash of the derivative/file, if available. |
| --- | --- |
| size   number | The size of the derivative/file, in bytes. |
| url   string | The download URL. |
| content-type   string | The content type of the derivative/file. |
| expiration   number | The 13-digit epoch time stamp indicating the time the signed cookies expire. |

Hint:

The following examples return raw HTTP headers and JSON objects. For a more developer-friendly experience, consider using our [TypeScript SDK](https://aps.autodesk.com/en/docs/model-derivative/v2/reference/typescript-sdk/) or [.NET SDK](https://aps.autodesk.com/en/docs/model-derivative/v2/reference/dot-net-sdk/). Both provide strongly typed data with IntelliSense support, offering code completion, error checking, and tooltips that reduce the need to reference JSON schemas.

 

## [Example](#example)

This example shows the successful retrieval of a download URL and signed cookies.

### Request

cURL

```
curl \
  --location 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6anAtMjIwNTIwL2JveC5pcHQ/manifest/urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6anAtMjIwNTIwL2JveC5pcHQ/output/225ba6fd-8516-460d-bb34-8bc85c09a79d/box.obj/signedcookies' \
  --header 'Authorization: Bearer eyJh...'

```

JavaScript (Fetch)

```
// Define the URL for the GET request
const url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6anAtMjIwNTIwL2JveC5pcHQ/manifest/urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6anAtMjIwNTIwL2JveC5pcHQ/output/225ba6fd-8516-460d-bb34-8bc85c09a79d/box.obj/signedcookies';

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
var request = new HttpRequestMessage(HttpMethod.Get, "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6anAtMjIwNTIwL2JveC5pcHQ/manifest/urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6anAtMjIwNTIwL2JveC5pcHQ/output/225ba6fd-8516-460d-bb34-8bc85c09a79d/box.obj/signedcookies");

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
url = "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6anAtMjIwNTIwL2JveC5pcHQ/manifest/urn:adsk.viewing:fs.file:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6anAtMjIwNTIwL2JveC5pcHQ/output/225ba6fd-8516-460d-bb34-8bc85c09a79d/box.obj/signedcookies"

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
Content-Encoding: gzip
Content-Type: application/json; charset=utf-8
Date: Thu, 26 May 2022 05:44:08 GMT
Set-Cookie: CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLmRlcml2YXRpdmUuYXV0b2Rlc2suY29tL2RYSnVPbUZrYzJzdWIySnFaV04wY3pwdmN5NXZZbXBsWTNRNmFuQXRNakl3TlRJd0wySnZlQzVwY0hRL291dHB1dC8yMjViYTZmZC04NTE2LTQ2MGQtYmIzNC04YmM4NWMwOWE3OWQvYm94Lm9iaiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY1MzU2NTQ0OH19fV19; Path=/; Domain=cdn.derivative.autodesk.com; HTTPOnly
Set-Cookie: CloudFront-Key-Pair-Id=APKAIJ4JBLIOQMJEURDQ; Path=/; Domain=cdn.derivative.autodesk.com; HTTPOnly
Set-Cookie: CloudFront-Signature=FP-wcYYIt07Qe4c2rEjvZtLNy3lCIkxrjmgWHrsWQB6KN8y-PV1~p0be85FmL2m-Y7vvg536xHBH7zfteyP-jOn6nlXamCwVWqjNj4fmCaz9pLkBCrA8kVz9rrRtKOafQCFacjEXstT4wwcjKYz0J7sKK7qyhyzUuxRhkby1OsLXp8q2be4t6zYNJ205exsA7cxjnGMl9XRhoGF13H7RA8bRdBoCZ6L~cJIJYyb~A1lvbaCG~c4FWnv1p27M22CMGm8HORX5uSN-Qcxs5MeyDVM-Zk6ku~pr4ZxMRo1Oy6dSpNax6rfeK0-BKnPJZSVaxZ2gu5EDzotDMFGd-gHaQg__; Path=/; Domain=cdn.derivative.autodesk.com; HTTPOnly
Strict-Transport-Security: max-age=31536000; includeSubDomains
Vary: Accept-Encoding
x-ads-app-identifier: platform-viewing-2022.05.01.75.c20538dec-production
x-ads-duration: 89 ms
x-ads-region: US
x-ads-startup-time: Tue May 24 06:19:02 UTC 2022
Content-Length: 255
Connection: keep-alive

{
  "etag":"be2a39d08bee2113ca39e64f5d7b9065",
  "size":4559,
  "url":"https://cdn.derivative.autodesk.com/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6anAtMjIwNTIwL2JveC5pcHQ/output/225ba6fd-8516-460d-bb34-8bc85c09a79d/box.obj",
  "content-type":"application/x-tgif",
  "expiration":1653565448973
}

```

Show More
