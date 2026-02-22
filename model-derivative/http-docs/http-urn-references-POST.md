# modelderivative/v2/designdata/{urn}/references

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/reference/http/urn-references-POST/

---

Specify References

POST

# modelderivative/v2/designdata/{urn}/references

Specifies the location of the files referenced by the specified source design.

When you call [Create Translation Job](/en/docs/model-derivative/v2/reference/http/job-POST), set `checkReferences` to `true`. The Model Derivative service will then use the details you specify in this operation to locate and download the referenced files.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/modelderivative/v2/designdata/{urn}/references |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` `data:write` `data:create` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a two-legged access token obtained via a [Client Credentials Grant flow](/en/docs/oauth/v2/tutorials/get-2-legged-token/), or a three-legged access token obtained via an [Authorization Code flow](/en/docs/oauth/v2/tutorials/get-3-legged-token/) or a [Secure Service Account flow](/en/docs/ssa/v1/tutorials/getting-started-with-ssa/task3-generate-3-legged-access-token/). The Secure Service Account flow generates tokens without user interaction but maintains user context for headless server-to-server operations. |
| --- | --- |
| region   string | Specifies the data center where the manifest and derivatives of the specified source design are stored. Possible values are: <br>`US` - (Default) Data center for the US region.`EMEA` - Data center for the European Union, Middle East, and Africa.`AUS` - Data center for the Australia region.`CAN` - Data center for the Canada region.`DEU` - Data center for the Germany region.`IND` - Data center for the India region.`JPN` - Data center for the Japan region.`GBR` - Data center for the United Kingdom region. |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| urn   string | The Base64 (URL Safe) encoded design URN. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

Expand all

| urn*   string | The URL safe Base64 encoded URN of the source design. Mandatory if the Base64 encoded urn in the request URL is a logical URN. |
| --- | --- |
| region   enum:string | Specifies where the referenced files are stored. Possible values: <br>`US` - Data center for the US region.`EMEA` - Data center for the European Union, Middle East, and Africa.`AUS` - Data center for the Australia region.`CAN` - Data center for the Canada region.`DEU` - Data center for the Germany region.`IND` - Data center for the India region.`JPN` - Data center for the Japan region.`GBR` - Data center for the United Kingdom region. |
| filename*   string | The file name of the top level component. By default, it is set to `""` and the file will be download with its `urn`. |
| references*   array: object | An array of objects, where each object represents a referenced file. |
| urn*   string | The URN of the referenced file. |
| relativePath*   string | The path to the referenced file, relative to the top level component. By default, it is set to `""`, which means that the referenced file and top level component are in the same folder. |
| filename*   string | The file name of the referenced file. By default, it is set to `""` and the referenced file will be downloaded by its `urn` and placed relative to the top-level component using `relativePath`. |
| metadata   object | An object to hold custom metadata. |
| *   object |  |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The locations of referenced files were successfully recorded. |
| --- | --- |
| 400   Bad Request | The server was unable to process the request. The syntax of the request is malformed or the request is missing a required header. Do not repeat the request without fixing the issue. The response body may indicate what is wrong with the request. |
| 401   Unauthorized | The supplied authorization header was not valid or the supplied token scope was not acceptable. Verify authentication and try again. |
| 403   Forbidden | The request was successfully validated but lacking the required permissions. Verify your credentials and permissions before you send this request again. |
| 404   Not Found | The requested resource was not found. Review the request and try again. |
| 406   Not Acceptable | The request contains unacceptable references. For example, one or more referenced files may be stored in a different region than the source design. Please verify that all referenced resources are in the same region and adjust your request accordingly. |
| 500   Internal Server Error | An unexpected error occurred on the server, preventing it from completing your request. Please try again later. If the issue persists, contact the support team for assistance. |

### Response

## [Header (200)](#header-200)

| x-ads-app-identifier   string | The service identifier. Comprises of the service name, version, and environment. |
| --- | --- |
| x-ads-duration   string | The amount of time spent servicing the request, in milliseconds. |
| x-ads-startup-time   string | The service startup time, in the following date format: `EEE MMM dd HH:mm:ss Z yyyy`. |

### Response

## [Body Structure (200)](#body-structure-200)

| result   string | The result of the operation. Always `success` for status `200`. |
| --- | --- |
| urn   string | The URN of the top level component. |

Hint:

The following examples return raw HTTP headers and JSON objects. For a more developer-friendly experience, consider using our [TypeScript SDK](/en/docs/model-derivative/v2/reference/typescript-sdk/) or [.NET SDK](/en/docs/model-derivative/v2/reference/dot-net-sdk). Both provide strongly typed data with IntelliSense support, offering code completion, error checking, and tooltips that reduce the need to reference JSON schemas.

 

## [Example 1](#example-1)

This example shows how to create references for a source file. The source design and referenced files must be stored in the same region.

### Request

cURL

```
curl --location 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6anAtYnVja2V0LTI1MDUwMi9zY2lzc29ycy5pYW0=/references' \
--header 'Authorization: Bearer eyJh...' \
--header 'Content-Type: application/json' \
--data '{
        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/scissors.iam",
        "filename": "scissors.iam",
        "references": [
                {
                        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/blade_main.ipt",
                        "relativePath": "Components/blade_main.ipt",
                        "filename": "blade_main.ipt"
                },
                {
                        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/blade_top.ipt",
                        "relativePath": "Components/blade_top.ipt",
                        "filename": "blade_top.ipt"
                },
                {
                        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/scissor_spring.ipt",
                        "relativePath": "Components/scissor_spring.ipt",
                        "filename": "scissor_spring.ipt"
                }
        ]
}'

```

Show More

JavaScript (Fetch)

```
// Create headers for the request
const myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer eyJh...");
myHeaders.append("Content-Type", "application/json");

// Prepare the payload with the source file and its references
const raw = JSON.stringify({
        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/scissors.iam",
        "filename": "scissors.iam",
        "references": [
                {
                        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/blade_main.ipt",
                        "relativePath": "Components/blade_main.ipt",
                        "filename": "blade_main.ipt"
                },
                {
                        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/blade_top.ipt",
                        "relativePath": "Components/blade_top.ipt",
                        "filename": "blade_top.ipt"
                },
                {
                        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/scissor_spring.ipt",
                        "relativePath": "Components/scissor_spring.ipt",
                        "filename": "scissor_spring.ipt"
                }
        ]
});

// Set up the request options for fetch
const requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: raw,
        redirect: "follow"
};

// Send the POST request to the API endpoint
fetch("https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6anAtYnVja2V0LTI1MDUwMi9zY2lzc29ycy5pYW0=/references", requestOptions)
        .then((response) => response.text()) // Parse the response as text
        .then((result) => console.log(result)) // Log the result to the console
        .catch((error) => console.error(error)); // Log any errors

```

Show More

C# (HttpClient)

```
// Create a new HttpClient instance
var client = new HttpClient();
// Set the Authorization header with the Bearer token
client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", "eyJh...");
// Set the Accept header to application/json
client.DefaultRequestHeaders.Accept.Add(new System.Net.Http.Headers.MediaTypeWithQualityHeaderValue("application/json"));

// Prepare the payload with the source file and its references
var payload = new
{
        urn = "urn:adsk.objects:os.object:jp-bucket-250502/scissors.iam",
        filename = "scissors.iam",
        references = new[]
        {
                new {
                        urn = "urn:adsk.objects:os.object:jp-bucket-250502/blade_main.ipt",
                        relativePath = "Components/blade_main.ipt",
                        filename = "blade_main.ipt"
                },
                new {
                        urn = "urn:adsk.objects:os.object:jp-bucket-250502/blade_top.ipt",
                        relativePath = "Components/blade_top.ipt",
                        filename = "blade_top.ipt"
                },
                new {
                        urn = "urn:adsk.objects:os.object:jp-bucket-250502/scissor_spring.ipt",
                        relativePath = "Components/scissor_spring.ipt",
                        filename = "scissor_spring.ipt"
                }
        }
};

// Serialize the payload to JSON and create the StringContent
var content = new StringContent(
        Newtonsoft.Json.JsonConvert.SerializeObject(payload),
        System.Text.Encoding.UTF8,
        "application/json"
);

// Send the POST request to the API endpoint
var response = await client.PostAsync(
        "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6anAtYnVja2V0LTI1MDUwMi9zY2lzc29ycy5pYW0=/references",
        content
);

// Read and print the response from the API
var result = await response.Content.ReadAsStringAsync();
Console.WriteLine(result);

```

Show More

Python (Requests)

```
# Import required libraries
import requests
import json

# Set the API endpoint URL
url = "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6anAtYnVja2V0LTI1MDUwMi9zY2lzc29ycy5pYW0=/references"

# Prepare the payload with the source file and its references
payload = json.dumps({
        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/scissors.iam",
        "filename": "scissors.iam",
        "references": [
                {
                        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/blade_main.ipt",
                        "relativePath": "Components/blade_main.ipt",
                        "filename": "blade_main.ipt"
                },
                {
                        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/blade_top.ipt",
                        "relativePath": "Components/blade_top.ipt",
                        "filename": "blade_top.ipt"
                },
                {
                        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/scissor_spring.ipt",
                        "relativePath": "Components/scissor_spring.ipt",
                        "filename": "scissor_spring.ipt"
                }
        ]
})
# Set the request headers including authorization
headers = {
        'Authorization': 'Bearer eyJh...',
        'Content-Type': 'application/json'
}

# Send the POST request to the API
response = requests.post(url, headers=headers, data=payload)

# Print the response from the API
print(response.text)

```

Show More

### Response

```
HTTP/1.1 200 OK
Server: nginx
Date: Fri, 16 May 2025 06:22:28 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 20
Connection: keep-alive
x-ads-duration: 339 ms
x-ads-startup-time: Thu Apr 24 11:14:32 UTC 2025
x-ads-app-identifier: platform-viewing-2025.02.01.1205.2f1fdcae1-staging
strict-transport-security: max-age=31536000; includeSubDomains; preload
x-frame-options: SAMEORIGIN
x-request-id: 1ed7bcb2-9746-42fb-b959-b4c35198715f

{
  "result": "success"
}

```

Show More

## [Example 2](#example-2)

This example demonstrates what happens when the source design and referenced files are stored in different regions. The system returns an HTTP 406 error for this request.

### Request

cURL

```
curl --location 'https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6anAtYnVja2V0LTI1MDUwMi9zY2lzc29ycy5pYW0=/references' \
--header 'Authorization: Bearer eyJh...' \
--header 'Content-Type: application/json' \
--data '{
        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/scissors.iam",
        "filename": "scissors.iam",
        "references": [
                {
                        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/blade_main.ipt",
                        "relativePath": "Components/blade_main.ipt",
                        "filename": "blade_main.ipt"
                },
                {
                        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/blade_top.ipt",
                        "relativePath": "Components/blade_top.ipt",
                        "filename": "blade_top.ipt"
                },
                {
                        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/scissor_spring.ipt",
                        "relativePath": "Components/scissor_spring.ipt",
                        "filename": "scissor_spring.ipt"
                }
        ]
}'

```

Show More

JavaScript (Fetch)

```
// Create headers for the request
const myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer eyJh...");
myHeaders.append("Content-Type", "application/json");

// Prepare the payload with the source file and its references
const raw = JSON.stringify({
        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/scissors.iam",
        "filename": "scissors.iam",
        "references": [
                {
                        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/blade_main.ipt",
                        "relativePath": "Components/blade_main.ipt",
                        "filename": "blade_main.ipt"
                },
                {
                        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/blade_top.ipt",
                        "relativePath": "Components/blade_top.ipt",
                        "filename": "blade_top.ipt"
                },
                {
                        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/scissor_spring.ipt",
                        "relativePath": "Components/scissor_spring.ipt",
                        "filename": "scissor_spring.ipt"
                }
        ]
});

// Set up the request options for fetch
const requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: raw,
        redirect: "follow"
};

// Send the POST request to the API endpoint
fetch("https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6anAtYnVja2V0LTI1MDUwMi9zY2lzc29ycy5pYW0=/references", requestOptions)
        .then((response) => response.text()) // Parse the response as text
        .then((result) => console.log(result)) // Log the result to the console
        .catch((error) => console.error(error)); // Log any errors

```

Show More

C# (HttpClient)

```
// Create a new HttpClient instance
var client = new HttpClient();
// Set the Authorization header with the Bearer token
client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", "eyJh...");
// Set the Accept header to application/json
client.DefaultRequestHeaders.Accept.Add(new System.Net.Http.Headers.MediaTypeWithQualityHeaderValue("application/json"));

// Prepare the payload with the source file and its references
var payload = new
{
        urn = "urn:adsk.objects:os.object:jp-bucket-250502/scissors.iam",
        filename = "scissors.iam",
        references = new[]
        {
                new {
                        urn = "urn:adsk.objects:os.object:jp-bucket-250502/blade_main.ipt",
                        relativePath = "Components/blade_main.ipt",
                        filename = "blade_main.ipt"
                },
                new {
                        urn = "urn:adsk.objects:os.object:jp-bucket-250502/blade_top.ipt",
                        relativePath = "Components/blade_top.ipt",
                        filename = "blade_top.ipt"
                },
                new {
                        urn = "urn:adsk.objects:os.object:jp-bucket-250502/scissor_spring.ipt",
                        relativePath = "Components/scissor_spring.ipt",
                        filename = "scissor_spring.ipt"
                }
        }
};

// Serialize the payload to JSON and create the StringContent
var content = new StringContent(
        Newtonsoft.Json.JsonConvert.SerializeObject(payload),
        System.Text.Encoding.UTF8,
        "application/json"
);

// Send the POST request to the API endpoint
var response = await client.PostAsync(
        "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6anAtYnVja2V0LTI1MDUwMi9zY2lzc29ycy5pYW0=/references",
        content
);

// Read and print the response from the API
var result = await response.Content.ReadAsStringAsync();
Console.WriteLine(result);

```

Show More

Python (Requests)

```
# Import required libraries
import requests
import json

# Set the API endpoint URL
url = "https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6anAtYnVja2V0LTI1MDUwMi9zY2lzc29ycy5pYW0=/references"

# Prepare the payload with the source file and its references
payload = json.dumps({
        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/scissors.iam",
        "filename": "scissors.iam",
        "references": [
                {
                        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/blade_main.ipt",
                        "relativePath": "Components/blade_main.ipt",
                        "filename": "blade_main.ipt"
                },
                {
                        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/blade_top.ipt",
                        "relativePath": "Components/blade_top.ipt",
                        "filename": "blade_top.ipt"
                },
                {
                        "urn": "urn:adsk.objects:os.object:jp-bucket-250502/scissor_spring.ipt",
                        "relativePath": "Components/scissor_spring.ipt",
                        "filename": "scissor_spring.ipt"
                }
        ]
})
# Set the request headers including authorization
headers = {
        'Authorization': 'Bearer eyJh...',
        'Content-Type': 'application/json'
}

# Send the POST request to the API
response = requests.post(url, headers=headers, data=payload)

# Print the response from the API
print(response.text)

```

Show More

### Response

```
Status Code: 406 Not Acceptable
Access-Control-Allow-Credentials:true
Access-Control-Allow-Origin:*
Connection: close
Content-Length:144
Content-Type:application/json;charset=utf-8
Date: Fri, 01 Sep 2017 06:00:42 GMT
x-ads-app-identifier:platform-viewing-2017.07.02.32.cf55416-production
x-ads-duration:34 ms
x-ads-startup-time:Wed Aug 30 03:20:17 UTC 2017

{
  "diagnostic": "Can not register the same design on different regions, you should delete old registration for register it to another region."
}

```

Show More
