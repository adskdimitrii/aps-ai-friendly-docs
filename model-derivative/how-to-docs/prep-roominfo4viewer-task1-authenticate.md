# Task 1 â Obtain an Access Token

Source: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/prep-roominfo4viewer/task1-authenticate/

---

# Task 1 â Obtain an Access Token

This task produces a two-legged token with a scope sufficient to authenticate the remaining tasks in this walkthrough.

By the end of this task, you will know how to obtain a two-legged access token when the Client ID and Client Secret is known.

You use the following operation for this task:

| Operation | HTTP Request |
| --- | --- |
| [Get an Access Token](/en/docs/oauth/v2/reference/http/gettoken-POST/) | POST /token |

## [Step 1 - Register an App](#step-1-register-an-app)

Follow the instructions in the walkthrough [Create an app](/en/docs/oauth/v2/tutorials/create-app) to register an app for this walkthrough. Note down the Client ID and Client Secret you recieve for the app. When specifying details of the app, make sure that the âModel Derivative APIâ and âData Management APIâ are selected.

## [Step 2: Encode your Client ID and Client Secret](#step-2-encode-your-client-id-and-client-secret)

Before you request an access token, you must encode your Client ID and Client Secret to ensure the integrity of the data you send. To do this, first, concatenate your Client ID with your Client Secret using the colon character as a separator. After that, convert the concatenated string to a Base64 encoded string.

1. Concatenate your Client ID and Client Secret with a colon character (:) in between, as shown below.
  
  

```
<CLIENT_ID>:<CLIENT_SECRET>

```

2. Use the appropriate function or method in your preferred programming language to encode the combined string to the Base64 format. Examples:
    | Programming Language | Method/Function |
    | --- | --- |
    | JavaScript | `btoa()` function |
    | Python | `b64encode()` function from the `base64` module |
    | C# | `Convert.ToBase64String()` method |
  JavaScript

  
  
  

```
const clientId =  "<CLIENT_ID>";
const clientSecret =  "<CLIENT_SECRET>";
const clientAuthKeys =  btoa(clientId +":"+clientSecret);

```
Python

  
  
  

```
import base64

clientId = "<CLIENT_ID>"
clientSecret = "<CLIENT_SECRET>"
clientAuthKeys = base64.b64encode((clientId + ":" + clientSecret).encode("ascii")).decode("ascii")

```
C#

  
  
  

```
using System;
using System.Text;

string clientId = "<CLIENT_ID>";
string clientSecret = "<CLIENT_SECRET>";
string combinedKeys = clientId + ":" + clientSecret;
byte[] bytesToEncode = Encoding.UTF8.GetBytes(combinedKeys);
string encodedText = Convert.ToBase64String(bytesToEncode);

```
  Show More
    **Note:** There are online tools that you can use to convert the combined string to a Base64 encoded string. However, we donât recommend that you use such tools. Exposing your Client ID and Client Secret to an online tool can pose a security threat.

    You should receive a string that looks like `RjZEbjh5cGVtMWo4UDZzVXo4SVgzcG1Tc09BOTlHVVQ6QVNOa3c4S3F6MXQwV1hISw==`.

## [Step 3: Use encoded string to obtain an Access Token](#step-3-use-encoded-string-to-obtain-an-access-token)

Call the [POST token](/en/docs/oauth/v2/reference/http/gettoken-POST) endpoint:

The Base64 encoded Client ID + Client Secret are passed through the `Authorization` header. The `grant_type` and `scope` are specified as form fields in the request body.

```
curl -v 'https://developer.api.autodesk.com/authentication/v2/token' \
   -X 'POST' \
   -H 'Content-Type: application/x-www-form-urlencoded' \
   -H 'Accept: application/json' \
   -H 'Authorization: Basic <BASE64_ENCODED_STRING_FROM_STEP_2>' \
   -d 'grant_type=client_credentials' \
   -d 'scope=data:write data:read bucket:create bucket:delete'

```

A successful response, will look like the following:

```
HTTP/1.1 200 OK
Cache-Control: no-cache, no-store, no-store
Content-Type: application/json;charset=UTF-8
Date: Mon, 20 Feb 2017 04:46:41 GMT
Expires: Thu, 01 Jan 1970 00:00:00 GMT
max-age: Thu, 01 Jan 1970 00:00:00 GMT
Pragma: no-cache
Server: Apigee Router
Set-Cookie: PF=2xeh6LTdKKqibsTu9HlyM5;Path=/;Secure;HttpOnly
X-Frame-Options: SAMEORIGIN
Content-Length: 436
Connection: keep-alive

{
  "token_type": "Bearer",
  "expires_in": 1799,
  "access_token": "<YOUR_ACCESS_TOKEN>"
}

```

Show More

**Notes:**

- Copy the access token (indicated by `<YOUR_ACCESS_TOKEN>` in the preceding example) in the response. You use this value for all subsequent requests in this walkthrough.
- The access token expires in the number of seconds specified by the `expires_in` attribute.
- Although the scope specified in the request is `data:write data:read bucket:create bucket:delete`, Model Derivative requires only the scopes `data:write` and `data:read`. The scopes `bucket:create bucket:delete` are for HTTP requests to the Data Management API.
