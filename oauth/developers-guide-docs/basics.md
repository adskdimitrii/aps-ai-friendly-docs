# API Basics

Source: https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/basics/

---

# API Basics

While the details may get more complex, the basic flow for using OAuth on the platform is as follows:

- Your app makes an HTTP call to an OAuth REST endpoint and provides its credentials.

- A token is returned to your app.

- In making subsequent HTTP calls to various APIs on the platform, your app includes the token in a request header.

There are a number of concepts that you need to be familiar with:

Term Meaning app The âappâ is the code that youâre writing that calls APS APIs. It can be a web application, a headless server process, a mobile app, or even embedded firmware. Within the APS developer portal, your app is registered in the My Apps section. Sometimes âappâ refers to your code; other times, it refers to the entity registered in the Dev Portal. It will be clear from context which is meant. When you register your app in the APS developer portal, you select the APIs that you want to bind it to. This ensures that even if you lose control of your authentication credentials, calls cannot be made on your behalf to APIs the app was not designed for. A registered app has assigned to it credentials called a âclient IDâ and âclient secretâ, which are analogous to a username and password, except that you do not select them. These are used to obtain access tokens. client ID The âclient IDâ is essentially your appâs username and can be found in the My Apps section. It is an alphanumeric string (e.g., 5zw90va0UuwMKTnPS5sLsdgZjDkVYXN7), and it is passed as the value for the client_id query parameter and JSON attribute. On other platforms, this is sometimes called âconsumer keyâ or âAPI keyâ. client secret The âclient secretâ is essentially your appâs password and can be found next to the client ID in the My Apps section. It is an alphanumeric string (e.g., 7I6uN1rjneirxiMW), and it is passed as the value for the client_secret query parameter. On other platforms, this is sometimes called âconsumer secretâ or âAPI secretâ. two-legged authentication This is often considered the default type of authentication, and it is the simplest. When your app needs to call the API without having to access resources that require an end userâs permission (for example, translating a design file from one format to another), the communication is directly between your app and APS. The end user, if there is one, does not need to be aware of the authentication or provide authorization for the app to access any resources. This kind of flow is called âtwo-leggedâ because your app and APS are the two âlegsâ. See the section below about common authentication flows. three-legged authentication When an app needs to access resources belonging to an end user, that user must explicitly provide authorization. The typical mechanism, in the case of a web app, is for the app to redirect the user to an Autodesk login page with information about which of the userâs resources it wishes to access. The user then provides explicit consent, letting APS know that the referring app is to be granted the requested access. The user is then redirected back to the app, which can then access the required resources. This kind of flow is called âthree-leggedâ because your app, APS, and the end user make up the three âlegsâ of the flow. Three-legged authentication can be done by using authorization code. When the authorization code grant is used, an Authorization Code is issued to the user to exchange it to obtain Access Token and Refresh Token. See the section below about common authentication flows. callback URL In certain contexts, your app needs to hand over part of the authentication flow to APS. For example, in three-legged authentication for a web app, an end user of your app is redirected to an Autodesk login flow, so that the user can tell the platform that your app is authorized to act on the userâs behalf. The callback URL is what is passed to the Autodesk login flow to tell it how to redirect the user back to your app. Callback URLs are specified in two places. You first specify a callback URL for your app in the My Apps section. Then, when you redirect your user to the Autodesk login flow, you also specify the callback URL in the redirect_uri parameter. This allows you to use different callback URLs in different parts of your app. All callback URLs are validated against what is specified in your appâs registration, and any run-time callback URL must match the pattern of the registered one. See the GET authorize documentation for more details on the relationship between the callback URL field and the redirect_uri parameter. Note that if your app does not require three-legged authentication, you can put any valid value in the callback URL field when you register your app, as no redirect_uri will ever be validated against it. authorization code In a three-legged authorization code grant type flow, an authorization code is passed through a code query parameter when the user is redirected back to the app via the callback URL. Along with its client ID and secret, an app calls the POST token endpoint to exchange the authorization code for an access token. The authorization code is a 40-character string (e.g., wroM1vFA4E-Aj241-quh_LVjm7UldawnNgYEHQ8I). access token An access token (sometimes just âtokenâ or âbearer tokenâ) is returned at the end of a successful authentication flow. APS uses JSON Web Tokens (JWT), which are alphanumeric strings of variable length (including periods to separate their different parts), used in subsequent API calls to the platform. The platform keeps track of what resources the token is entitled to access and either allows or denies access at call time. Tokens have a limited lifespan and expire after a specified number of seconds. scopes A scope is a permission that is set on a token, a context in which that token may act. For example, a token with the data:read scope is permitted to read data within the APS ecosystem and can be used on those endpoints that require that scope. Tokens without that scope would be denied access to such endpoints. (Individual endpoint reference pages list the required scopes.) Scopes serve two principal functions: In a three-legged context, they act as a mechanism for requesting and securing permission to act on an end userâs behalf in specified ways. In both two- and three-legged contexts, they ensure that if you lose control of your token, it cannot be misused to access resources for which it was not intended. For more information, see the Scopes page. authentication context With the exception of OAuth endpoints and those that do not require authentication, all endpoints have one of the following authentication contexts: app only: The endpoint accepts either a two-legged or three-legged token, but it will only act on behalf of the app itself, ignoring any permissions associated with the end user. user context required: The endpoint requires a three-legged token and acts on behalf of the authenticating end user. user context optional: If provided a two-legged token, the endpoint will act on behalf of the app, accessing only those resources for which the app itself has permission. If provided a three-legged token, the endpoint will act on behalf of the end user, accessing only those resources for which the user has permission.

## Common Authentication and Authorization Flows

Make sure you familiarize yourself with the terminology in the table above before reading this section.

### Two-Legged Authentication

In formal OAuth terminology, to accomplish two-legged authentication on APS requires that you use the âClient Credentialsâ grant type.

This means that your app directly communicates with APS for authentication and accessing resources. If itâs a web app, the end user is not directly aware of any of these server-to-server communications, as none of it is passed through the web browser.

A typical workflow is as follows:

- Your app (the âclientâ in OAuth terminology) send its client credentials to your APS Authorization Server.

- Assuming successful validation of the credentials, an access token is returned.

- Your app can make calls to any âapp onlyâ or âuser context optionalâ endpoint for which the token has the required scopes by including the Authorization: Bearer <token> request header (where <token> is your access token).

- When the token expires, your app will need to retrieve a new token by going through all these steps again.

### Three-Legged Authentication and Authorization using Authorization Code grant

In formal OAuth terminology, to accomplish three-legged authentication and authorization on APS, the authorization code grant type can be adopted.

To use a web app as an example, this means that your app redirects the end user to an Autodesk login and authorization flow, and an authorization code is returned to your app (via a query parameter in the callback). Your app then exchanges that authorization code for a token by communicating with the Authentication server directly.

While other grant types are possible (that enable other flows), they are less secure and thus highly discouraged and not documented here.

A typical workflow is as follows:

- Your app (the âclientâ in OAuth terminology) triggers the browser (the âuser agentâ in OAuth terminology) to redirect the end user to the GET authorize endpoint in the browser itself . (Remember that typical web browsing is technically hitting HTTP REST endpoints!) Using query parameters, your app identifies itself, requests scopes, and indicates the callback URL to redirect the browser to after authorization has completed.

- If the user is not already logged in to the Autodesk account via the authentication service, the user is prompted to log in or create an Autodesk account.

- The user is presented with an in-browser consent page and must explicitly accept the scopes that your app is requesting.

- The userâs browser is then redirected to the callback URL, along with a code query parameter that contains the authorization code.

- The browserâs loading the callback URL is what passes the authorization code back to your app.

- Your app then uses that authorization code, its client ID, and its client secret to call the POST token endpoint.

- Assuming successful validation of the credentials, an access token and a refresh token are returned.

- Your app can make calls to any âuser context requiredâ or âuser context optionalâ endpoint for which the token has the required scopes by including the Authorization: Bearer <token> request header (where <token> is your 28-character access token).

- When the token expires, your app can use the refresh token to acquire a new access token. (This avoids having to go through steps 1-6 every time the access token expires.)
