# Get a 3-Legged Token with Authorization Code Grant

Source: https://aps.autodesk.com/en/docs/oauth/v2/tutorials/get-3-legged-token/

---

# Get a 3-Legged Token with Authorization Code Grant

If you need an end user to authorize your app to act on the userâs behalf, please refer this walkthrough.

The authorization code grant type is used to obtain both access tokens and refresh tokens and is optimized for confidential clients.

Note that this walkthrough does not show you how to write server-side code. Instead, it uses cURL commands to illustrate the calls you need to instrument in your code.

This walkthrough presupposes that the app is a web app and that it needs to read the userâs data.

## Before You Begin

Before you begin, follow the Create an App walkthrough to create your app on the APS Platform. Specify your appâs callback URL and note your client ID and secret.

Familiarize yourself with the overall flow:

## Step 1: Direct the User to the Authorization Web Flow

At some point in the UI of your web app, you will find that you need to get the end userâs consent to access APS resources on the userâs behalf. Depending on your app, you may do this when the user first starts using the app, or you may wait until your app actually needs to access the resource. Whatever the case, you will redirect the user to the GET authorize endpoint in their browser. For example, you might provide a link that looks like the following:

```
https://developer.api.autodesk.com/authentication/v2/authorize?response_type=code&client_id=F6Dn8ypem1j8P6sUz8IX3pmSsOA99GUT&redirect_uri=http://localhost:8080/oauth/callback/&scope=data:read
```

The following is the break down of the above attribute:

- https://developer.api.autodesk.com/authentication/v2/authorize This is the endpoint URI and should be used verbatim.

This is the endpoint URI and should be used verbatim.

- response_type=code This is what tells the OAuth server that youâre using the âAuthentication Codeâ grant type and should be used verbatim.

This is what tells the OAuth server that youâre using the âAuthentication Codeâ grant type and should be used verbatim.

- client_id=F6Dn8ypem1j8P6sUz8IX3pmSsOA99GUT Replace the value here with your appâs client ID.

Replace the value here with your appâs client ID.

- redirect_uri=http%3A%2F%2Flocalhost%3A8080%2Foauth%2Fcallback%2F This is the URL-encoded callback URL you want the user redirected to after they grant consent. In this example, that URL is http://localhost:8080/oauth/callback/ . Replace the value here with the appropriate URL for your web app. Note that it must match the pattern specified for the callback URL in your appâs registration in the APS developer portal.

This is the URL-encoded callback URL you want the user redirected to after they grant consent. In this example, that URL is http://localhost:8080/oauth/callback/ . Replace the value here with the appropriate URL for your web app. Note that it must match the pattern specified for the callback URL in your appâs registration in the APS developer portal.

- scope=data:read This requests the data:read scope. You can leave this value as it is for the purpose of this example, but in your own app, you should request one or more scopes you actually need. If you need to include multiple scopes, you can include them all as space-delimited items. For example: scope=data:create%20data:read%20data:write includes data:read , data:write , and data:create scopes.

This requests the data:read scope. You can leave this value as it is for the purpose of this example, but in your own app, you should request one or more scopes you actually need. If you need to include multiple scopes, you can include them all as space-delimited items. For example: scope=data:create%20data:read%20data:write includes data:read , data:write , and data:create scopes.

Clicking on this link will take the end user to the Autodesk Sign In page:

After entering their Autodesk ID credentials and logging in, the user will be redirected to the OAuth consent page:

When consent has been granted, the user will be redirected back to your callback URL ( redirect_uri ) with an additional code query parameter that contains the authorization code (e.g., wroM1vFA4E-Aj241-quh_LVjm7UldawnNgYEHQ8I ).

## Step 2: Implement Code that Extracts the Authorization Code

In this example, the user was redirected to http://localhost:8080/oauth/callback/?code=DgK8pixFrHk8N_7tym_EVhDcHnaTV9SR6yoWmOyb&state= .

Your code that serves up the /oauth/callback/ URL in your web app should extract this code query parameter value and store it in a temporary variable.

## Step 3: Exchange the Authorization Code for an Access Token

Immediately after extracting the code query parameter value, you should exchange the authorization code for an access token using the POST token endpoint:

To generate Basic Header for your <client_id> and <client_secret>, execute the following command:

```
echo -n '<client_id>:<client_secret>' | base64
```

Replace the Authorization , code , and redirect_uri values in the example below with those specific to your app and from the above steps.

```
curl -v 'https://developer.api.autodesk.com/authentication/v2/token' \ -X 'POST' \ -H 'Content-Type: application/x-www-form-urlencoded' \ -H 'Authorization: Basic RjZEbjh5cGVtMWo4UDZzVXo4SVgzcG1Tc09BOTlHVVQ6QVNOa3c4S3F6MXQwV1hISw==' \ -d 'grant_type=authorization_code' \ -d 'code=DgK8pixFrHk8N_7tym_EVhDcHnaTV9SR6yoWmOyb' \ -d 'redirect_uri=http://localhost:8080/oauth/callback/'
```

For this flow, you will not be executing cURL commands directly in your terminal. However, you can use this example to implement the correct call in your server-side code.

A successful response, in relevant part, will resemble this format (although, the example is formatted for ease of reading):

```
{ "access_token" : "eyJhbGciOiJSUzI1NiIsImtpZCI6IlU3c0dGRldUTzlBekNhSzBqZURRM2dQZXBURVdWN2VhIn0.eyJzY29wZSI6WyJkYXRhOnJlYWQiXSwiY2xpZW50X2lkIjoiRjZEbjh5cGVtMWo4UDZzVXo4SVgzcG1Tc09BOTlHVVQiLCJpc3MiOiJodHRwczovL2RldmVsb3Blci5hcGkuYXV0b2Rlc2suY29tIiwiYXVkIjoiaHR0cHM6Ly9hdXRvZGVzay5jb20iLCJqdGkiOiJUaDZMbWVLdzN2c0ZxSTNPR0hrUmhxUG9rTXJnR1RPanhjUW1hQXlRS2RnU1VTbzV5cEY5dTZqekM4UmwwVnNBIiwidXNlcmlkIjoiM1hWU0w3MkpMMlU1IiwiZXhwIjoxNjY5ODY5MDQ1fQ.diknPiZfHDSmgl3iPuQgXMZQhCRBVQGyvj3e0GCRQtSUjE5pVnm6a7PnGJwcrvnsaV7wrNOGi_dPDcQW_pYyrQV925kKtV4GYLLrrf639s0wpdlj7nHJGPgy_oRu4pFTSBtj5qW6i3hIaujtVtzLc9DtvKAWYPRSq-_j9niibM1TrLc_6mrIse-jtQP6qkmWj7IzZPxgX947_4rYW06-Vzb4Yyu1VlmGs7A1koUPMIp2N4RUTGzUyM1z9xszqQHZBkznKRVZVJOkzO6kHyAFWr3ksYgRNdGU2zY_x_OTe3MW4uBfLgQTw-Eo5xsc7a87xvX7vSDfl14ctwwE8lMnBw" , "token_type" : "Bearer" , "expires_in" : 3599 , "refresh_token" : "l8rZq7ckWJ2KocuJg0hqu3oSd8AzG4jsypcXzl4ZUo" }
```

Use the appropriate methods in your server-side code to extract the relevant information returned by the endpoint. You will then be able to use the access token to make calls to other API endpoints on behalf of the end user that require the data:read scope and have a âuser context requiredâ or âuser context optionalâ authentication context.
