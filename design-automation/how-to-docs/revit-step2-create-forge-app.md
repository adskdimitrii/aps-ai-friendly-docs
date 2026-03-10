# Task 2 – Obtain an Access Token

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/revit/step2-create-forge-app/

---

# Task 2 – Obtain an Access Token

This task produces a two-legged OAuth token with a scope sufficient to authenticate the remaining tasks in this walkthrough.

By the end of this task, you will know how to obtain a two-legged access token when the Client ID and Client Secret is known.

You use the following operations in this task:

| HTTP Request | Operation |
| --- | --- |
| POST /authenticate | [Get a two-legged access token](../../oauth/http-docs/http-gettoken-POST.md) |

## [Step 1 - Register an App](#step-1-register-an-app)

Follow the instructions on [Create an App](../../oauth/how-to-docs/create-app.md) to register the App you will create for this walkthrough.

## [Step 2 - Convert Client ID and Secret to Base64 encoded string](#step-2-convert-client-id-and-secret-to-base64-encoded-string)

You must combine your Client ID with the Client Secret and convert it to a Base64 encoded string before you can request a two-legged OAuth access token.

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
    **Note:** There are online tools that you can use to convert the combined string to a Base64 encoded string. However, we don’t recommend that you use such tools. Exposing your Client ID and Client Secret to an online tool can be a security threat.

    You should receive a string that looks like `RjZEbjh5cGVtMWo4UDZzVXo4SVgzcG1Tc09BOTlHVVQ6QVNOa3c4S3F6MXQwV1hISw==`.

## [Step 3 - Use encoded string to obtain an Access Token](#step-3-use-encoded-string-to-obtain-an-access-token)

Call the [POST token](../../oauth/http-docs/http-gettoken-POST.md) endpoint:

The Base64 encoded Client ID + Client Secret are passed through the `Authorization` header. The `grant_type` and `scope` are specified as form fields in the request body.

```
curl -v 'https://developer.api.autodesk.com/authentication/v2/token' \
   -X 'POST' \
   -H 'Content-Type: application/x-www-form-urlencoded' \
   -H 'Accept: application/json' \
   -H 'Authorization: Basic <BASE64_ENCODED_STRING_FROM_STEP_1>' \
   -d 'grant_type=client_credentials' \
   -d 'scope=code:all bucket:create bucket:read data:create data:write data:read'

```

**Note:** The `bucket:read` scope is not required for the walkthrough. However, you will need `bucket:read` if you plan to list the files in a bucket.

A successful response, in relevant part, will look like this (though again, the example is formatted for ease of reading):

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

- Note down the access token (indicated by `<YOUR_ACCESS_TOKEN>` in the preceding example) in the response. You use this value for all subsequent requests in this walkthrough. The token remains valid for an hour. In the Postman Collection for this walkthrough, the access token is saved to the variable `TBD`.
- The access token expires in the number of seconds specified by the `expires_in` attribute.
