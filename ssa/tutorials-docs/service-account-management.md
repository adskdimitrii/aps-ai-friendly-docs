# Manage Secure Service Accounts

Source: https://aps.autodesk.com/en/docs/ssa/tutorials/service-account-management/

---

# Manage Secure Service Accounts

This walkthrough assumes that you have:

- Already created Secure Service Accounts (SSAs)
- A valid client ID and client secret

You will learn how to:

- Retrieve all SSAs
- Delete a specific SSA

This walkthrough uses the following operation:

| Operation | HTTP Request |
| --- | --- |
| [Get an Access Token](../../oauth/http-docs/http-gettoken-POST.md) | POST /token |
| [Get All Service Accounts](../http-docs/http-ssa-get-service-accounts-GET.md) | GET /service-accounts |
| [Delete a specific Service Account](../http-docs/http-ssa-delete-service-account-DELETE.md) | DELETE /service-accounts/{serviceAccountId} |

## [Step 1: Encode your Client ID and Client Secret](#step-1-encode-your-client-id-and-client-secret)

Before you request an access token, you must encode your Client ID and Client Secret to ensure data integrity. First, concatenate your Client ID with your Client Secret using a colon as a separator. Then convert the concatenated string to Base64 format.

1. Concatenate your Client ID and Client Secret with a colon character (:) in between, as shown below.
  
  

```
<CLIENT_ID>:<CLIENT_SECRET>

```

2. Use the appropriate function or method in your preferred programming language to convert the combined string to Base64 format. Examples:
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
    **Note:** Online tools exist to convert strings to Base64 encoding. However, we don’t recommend using such tools. Exposing your Client ID and Client Secret to an online tool poses a security threat.

    You should receive a string that looks like `RjZEbjh5cGVtMWo4UDZzVXo4SVgzcG1Tc09BOTlHVVQ6QVNOa3c4S3F6MXQwV1hISw==`.

## [Step 2: Use the encoded string to obtain an Access Token](#step-2-use-the-encoded-string-to-obtain-an-access-token)

Call the [POST token](../../oauth/http-docs/http-gettoken-POST.md) operation:

The Base64 encoded string is passed through the `Authorization` header. The `grant_type` and `scope` are specified as form fields in the request body.

```
curl -v 'https://developer.api.autodesk.com/authentication/v2/token' \
   -X 'POST' \
   -H 'Content-Type: application/x-www-form-urlencoded' \
   -H 'Accept: application/json' \
   -H 'Authorization: Basic <BASE64_ENCODED_STRING_FROM_STEP_1>' \
   -d 'grant_type=client_credentials' \
   -d 'scope=application:service_account:read application:service_account:write application:service_account_key:write'

```

A successful response will look like the following:

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

## [Step 3: Retrieve all SSAs](#step-3-retrieve-all-ssas)

### Request

```
curl -v 'https://developer.api.autodesk.com/authentication/v2/service-accounts' \
  -X 'GET' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN_FROM_STEP_2>'

```

### Response

```
HTTP/1.1 200 OK

{
  "serviceAccounts": [
    {
      "serviceAccountId": "TQUXKFEXUHLS",
      "email": "testserviceaccount1@BQ9teWlrzwgWetA5Eeog4bWAB5cZp2Zg.adskserviceaccount.autodesk.com",
      "createdBy": "BQ9teWlrzwgWetA5Eeog4bWAB5cZp2Zg",
      "status": "ENABLED",
      "createdAt": "2024-01-25 03:08:04.156576834 +0000 UTC",
      "accessedAt": "2024-01-25 03:08:04.156576834 +0000 UTC",
      "expiresAt": "2025-01-25 03:08:04.156576834 +0000 UTC"
    },
    {
      "serviceAccountId": "TQUXKFEXUHLL",
      "email": "testserviceaccount1@nWPwCnuV5M57GA32NZaB6FKMF7MqQ8Dg.adskserviceaccount.autodesk.com",
      "createdBy": "BQ9teWlrzwgWetA5Eeog4bWAB5cZp2Zg",
      "status": "DISABLED",
      "createdAt": "2024-01-25 03:08:04.156576834 +0000 UTC",
      "accessedAt": "2024-01-25 03:08:04.156576834 +0000 UTC",
      "expiresAt": "2025-01-25 03:08:04.156576834 +0000 UTC"
    }
  ]
}

```

Show More

## [Step 4: Delete a specific SSA](#step-4-delete-a-specific-ssa)

### Request

```
curl -v 'https://developer.api.autodesk.com/authentication/v2/service-accounts/{{serviceAccountId}}' \
  -X 'DELETE' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN_FROM_STEP_2>'

```

### Response

```
HTTP/1.1 204 No Content

```
