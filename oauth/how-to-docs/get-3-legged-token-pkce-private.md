# Get a 3-Legged Token with Authorization Code Grant (PKCE) for Private Clients

Source: https://aps.autodesk.com/en/docs/oauth/v2/tutorials/get-3-legged-token-pkce/get-3-legged-token-pkce-private/

---

# Get a 3-Legged Token with Authorization Code Grant (PKCE) for Private Clients

If you need an end user to authorize your app to act on the userâs behalf, please refer this walkthrough.

The authorization code grant type with PKCE is used to obtain both access tokens and refresh tokens and PKCE is strongly recommended for private clients as well but is not an optimization.

This flow is very similar to the authorization code flow. However, in this case you have to pass a code_challenge along with the authorization request.

- Guide for generating code_challenge : Code-Challenge Documentation Link

Note that this walkthrough does not show you how to write server-side code. Instead, it uses cURL commands to illustrate the calls you need to instrument in your code.

This walkthrough presupposes that the app is a web app and that it needs to read the userâs data.

## Before You Begin

Before you begin, follow the Create an App walkthrough. Refer to the section, Step 2: Register an App and select Traditional Web App to create your app on the APS developer Platform. Specify your appâs callback URL and note your client ID and secret.

Refer to the following image to familiarize yourself with the PKCE overall flow:

- Private client PKCE flow

## Step 1: Direct the User to the Authorization Web Flow with PKCE

At some point in the UI of your web app, you will find that you need to get the end userâs consent to access APS resources on the userâs behalf. Depending on your app, you may do this when the user first starts using the app, or you may wait until your app actually needs to access the resource. Whatever the case, you will redirect the user to the GET authorize endpoint in their browser. For example, you might provide a link that looks like the following:

```
< a href = "https://developer.api.autodesk.com/authentication/v2/authorize?response_type=code&client_id=GCi5oTYLE36CTUlcL7wWbhq9mC5DzG9w&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2Foauth%2Fcallback%2F&nonce=1232132&scope=data:read&prompt=login&state=12321321&code_challenge=fePr9SDGJIToHximLHTRokkzkfzZksznrDIx9bexsto&code_challenge_method=S256" > Click here to grant access to your data! </ a >
```

That href attribute is a bit difficult to read. Letâs break it down:

- https://developer.api.autodesk.com/authentication/v2/authorize This is the endpoint URI and should be used verbatim.

This is the endpoint URI and should be used verbatim.

- response_type=code This is what tells the OAuth server that youâre using the âAuthentication Codeâ grant type and should be used verbatim.

This is what tells the OAuth server that youâre using the âAuthentication Codeâ grant type and should be used verbatim.

- client_id=GCi5oTYLE36CTUlcL7wWbhq9mC5DzG9w Replace the value here with your appâs client ID.

Replace the value here with your appâs client ID.

- redirect_uri=http%3A%2F%2Flocalhost%3A8080%2Foauth%2Fcallback%2F This is the URL-encoded callback URL you want the user redirected to after they grant consent. In this example, the URL is http://localhost:8080/oauth/callback/ . Replace the value here with the appropriate URL for your web app. Note that it must match the pattern specified for the callback URL in your appâs registration in the APS developer portal.

This is the URL-encoded callback URL you want the user redirected to after they grant consent. In this example, the URL is http://localhost:8080/oauth/callback/ . Replace the value here with the appropriate URL for your web app. Note that it must match the pattern specified for the callback URL in your appâs registration in the APS developer portal.

- scope=data:read This requests the data:read scope. You can leave this value as it is for the purpose of this example, but in your own app, you should request one or more scopes you actually need. If you need to include multiple scopes, you can include them all as space-delimited items. For example: scope=data:create%20data:read%20data:write includes data:read , data:write , and data:create scopes.

This requests the data:read scope. You can leave this value as it is for the purpose of this example, but in your own app, you should request one or more scopes you actually need. If you need to include multiple scopes, you can include them all as space-delimited items. For example: scope=data:create%20data:read%20data:write includes data:read , data:write , and data:create scopes.

- nonce=12321321 The nonce is a mandatory field and is a string value used to associate a client session with an ID token and to mitigate replay attacks. Mandatory when scope is openid.

The nonce is a mandatory field and is a string value used to associate a client session with an ID token and to mitigate replay attacks. Mandatory when scope is openid.

- prompt=login It helps to clear the current session in order to focus on the request and allows the user to login.

It helps to clear the current session in order to focus on the request and allows the user to login.

- state=12321321 The state is an optional parameter but if set, then it is returned in the response. This is an opaque value used by the client to maintain state between the request and callback URL.

The state is an optional parameter but if set, then it is returned in the response. This is an opaque value used by the client to maintain state between the request and callback URL.

- code_challenge It is the code challenge used for PKCE.

It is the code challenge used for PKCE.

- code_challenge_method It is the method used to generate the challenge, which is always S256.

It is the method used to generate the challenge, which is always S256.

Clicking on this link will take the end user to the Autodesk Sign In page:

After entering their Autodesk ID credentials and logging in, the user will be redirected to the OAuth consent page:

When consent has been granted, the user will be redirected back to your callback URL ( redirect_uri ) with an additional code query parameter that contains the authorization code with PKCE (e.g., wroM1vFA4E-Aj241-quh_LVjm7UldawnNgYEHQ8I ).

## Step 2: Implement Code that Extracts the Authorization Code with PKCE

In this example, the user was redirected to http://localhost:8080/oauth/callback/?code=wroM1vFA4E-Aj241-quh_LVjm7UldawnNgYEHQ8I .

Your code that serves up the /oauth/callback/ URL in your web app should extract this code query parameter value and store it in a temporary variable.

## Step 3: Exchange the Authorization Code with PKCE for an Access Token

Immediately after extracting the code query parameter value, you should exchange the authorization code for an access token using the POST token endpoint:

Replace the client_id , client_secret , code , and redirect_uri values in the example below with those specific to your app and from the above steps.

```
curl -v 'https://developer.api.autodesk.com/authentication/v2/token' -X 'POST' -H 'Content-Type: application/x-www-form-urlencoded'' -H ' accept: application/json ' \' -d 'grant_type=authorization_code' -d 'client_id=GCi5oTYLE36CTUlcL7wWbhq9mC5DzG9w' -d 'client_secret=ASNkw8Kqz1t0WXHK' \ -d 'code_verifier=ZGI6X4QR3FFXh3Bs9zNMgazTYDHEb_GqTt_fue4tFKYjRNR9N32bCqr~Hsxl673Ssf0RqyxC0avKNo_AKlE_7tj6cm4i5XbmjuGrCsu7X9rE~MqmoBLrLjvmvQscCfi2' -d 'code=wroM1vFA4E-Aj241-quh_LVjm7UldawnNgYEHQ8I' -d 'redirect_uri=http://localhost:8080/oauth/callback/'
```

For this flow, you wouldnât be running cURL commands in your terminal anyway, but you can use this example to instrument the correct call in your server-side code.

A successful response, in relevant part, will look like this (the example is formatted for ease of reading):

```
{ "access_token" : "eyJhbGciOiJSUzI1NiIsImtpZCI6IlU3c0dGRldUTzlBekNhSzBqZURRM2dQZXBURVdWN2VhIn0.eyJzY29wZSI6WyJkYXRhOnJlYWQiXSwiY2xpZW50X2lkIjoiR0NpNW9UWUxFMzZDVFVsY0w3d1diaHE5bUM1RHpHOXciLCJpc3MiOiJodHRwczovL2RldmVsb3Blci5hcGkuYXV0b2Rlc2suY29tIiwiYXVkIjoiaHR0cHM6Ly9hdXRvZGVzay5jb20iLCJqdGkiOiJXWUhWa3Mwc0hBdmYzZWphWHFCdUl4UWNKa29RMnpEMW9aSHkydG1sVHVMdTliN0R1M3pvU1padnpXRGxZM0lsIiwidXNlcmlkIjoiM1hWU0w3MkpMMlU1IiwiZXhwIjoxNjY5ODgzMjcyfQ.Z7M2ZeuCc9oCuPn1CBr7axkOfONWtrZIROq0rROmpZ_Or5S34YL1BvcrVqfQj8VnmXgw5WbJcUEmDrRnH3Qo9nxK5OxKaunOL00qTQZZQ8KrmOkCx9ZVeKZhrss21f4asQWI7kgG09xLRvlt1jNcFvSrbXSCDm8suALhBv5PF_8S2cTbH-lNz0vZVn2uHzsokAGFDGnxZkaEZagqJUHIOdQiSJF_dP3s4j5OFCq60LP_hwBV5LXkZ4eq2rSpqwtvpldJxzXE3T9KdXeHEz__GSnuItS7_EkCu0Gmk5tf6JWyZImV68-uu4c8rB1rXV2XaiLS69zRWfyD9bpX6OZw1w" , "token_type" : "Bearer" , "expires_in" : 3599 , "refresh_token" : "Zxn4ucyciQSfCN7dC7e4MWCaIZRLtYsB6vhcmg5LMH" }
```

Use the appropriate methods in your server-side code to extract the relevant information returned by the endpoint. You will then be able to use the access token to make calls to other API endpoints on behalf of the end user that require the data:read scope and have a âuser context requiredâ or âuser context optionalâ authentication context.
