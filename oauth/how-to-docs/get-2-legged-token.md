# Get a 2-Legged Token

Source: https://aps.autodesk.com/en/docs/oauth/v2/tutorials/get-2-legged-token/

---

# Get a 2-Legged Token

Learn how to use the simplest authentication mechanism on APS with this example that acquires a token with the `data:read` scope.

## [Before You Begin](#before-you-begin)

[Create an app](/en/docs/oauth/v2/tutorials/create-app). Note your Client ID and Client Secret.

## [Step 1: Convert Client ID and Secret to Base64 encoded string](#step-1-convert-client-id-and-secret-to-base64-encoded-string)

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
    **Note:** There are online tools that you can use to convert the combined string to a Base64 encoded string. However, we donât recommend that you use such tools. Exposing your Client ID and Client Secret to an online tool can pose a security threat.

    You should receive a string that looks like `RjZEbjh5cGVtMWo4UDZzVXo4SVgzcG1Tc09BOTlHVVQ6QVNOa3c4S3F6MXQwV1hISw==`.

## [Step 2: Use encoded string to obtain an Access Token](#step-2-use-encoded-string-to-obtain-an-access-token)

Call the [POST token](/en/docs/oauth/v2/reference/http/gettoken-POST) endpoint:

The Base64 encoded Client ID + Client Secret are passed through the `Authorization` header. The `grant_type` and `scope` are specified as form fields in the request body.

```
curl -v 'https://developer.api.autodesk.com/authentication/v2/token' \
   -X 'POST' \
   -H 'Content-Type: application/x-www-form-urlencoded' \
   -H 'Accept: application/json' \
   -H 'Authorization: Basic <BASE64_ENCODED_STRING_FROM_STEP_1>' \
   -d 'grant_type=client_credentials' \
   -d 'scope=data:read'

```

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
  "access_token": "eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5X2RldiJ9.eyJjbGllbnRfaWQiOiJjWTFqcm1rQXhPSVptbnNsOVhYN0puVURtVEVETGNGeCIsImV4cCI6MTQ4NzU2NzgwMSwic2NvcGUiOlsiZGF0YTpyZWFkIl0sImF1ZCI6Imh0dHBzOi8vYXV0b2Rlc2suY29tL2F1ZC9qd3RleHAzMCIsImp0aSI6InJZcEZZTURyemtMOWZ1ZFdKSVVlVkxucGNWT29BTDg0dFpKbXlmZ29ORW1MakF0YVVtWktRWU1lYUR2UGlnNGsifQ.uzNexXCeu4efGPKGGhHdKxoJDXHAzLb28B2nSjrq_ys"
}

```

Show More

You can now use the access token to make calls to other API endpoints that require the `data:read` scope and have an âapp onlyâ or âuser context optionalâ authentication context until the token expires.
