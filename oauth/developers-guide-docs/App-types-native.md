# Desktop, Mobile, and Single-Page App

Source: https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/App-types/native/

---

# Desktop, Mobile, and Single-Page App

Choose **Desktop, Mobile, Single-Page App** if you are creating a native application for a desktop computer or mobile device, or a single-page application (SPA), where the application will be deployed on end-user machines on which you cannot protect your application credentials. (An SPA is a special kind of web application that runs entirely in the end userâs browser without any page reloading, or transfer to other web pages.)

This application type uses the *Authorization Code grant type* with a *Proof Key for Code Exchange* (*PKCE*). If you are using login via *Implicit grant type*, it is highly recommended that you switch to the more secure PKCE-based login.

The Authorization Code grant type with PKCE is the same as the standard Authorization Code grant type with an extra step at the beginning and an extra verification at the end.

## [Authorization Code Grant Type with PKCE](#authorization-code-grant-type-with-pkce)

At a high level, the authorization flow has the following steps:

1. Your application generates a code verifier followed by a code challenge.
2. Your application directs the browser to the APS login page, along with the generated code challenge, and the user authenticates.
3. APS redirects back to your native application or SPA, with an authorization code.
4. Your application sends this code, along with the code verifier, to APS. APS returns an access token, refresh token, and optionally an ID token.
5. Your application can now use these tokens to call the resource server (for example, an API) on behalf of the user.

Refer to [Example 2](../http-docs/http-authorize-GET.md#example-2) of this reference to see the complete flow using the Authorization Code grant type with PKCE.
> [](../../../_images/desktop-mobile-spa.png)

There are a number of concepts that you need to be familiar with relevant to this application type and grant type:

| Term | Meaning |
| --- | --- |
| app | The âappâ, or âapplicationâ, is the code that youâre writing that calls APS APIs. It can be a web application, a headless server process, a mobile app, or even embedded firmware. Within the APS developer portal, your application is registered in the My Apps section.       Sometimes âappâ refers to your code; other times, it refers to the entity registered in the Dev Portal. It will be clear from context which is meant.      When you register your application in the APS developer portal, you select the APIs that you want to bind it to. This ensures that even if you lose control of your authentication credentials, calls cannot be made on your behalf to APIs the application was not designed for.          A registered application has assigned to it credentials called a âclient IDâ and âclient secret.â These are analogous to a username and password, except that you do not select them; APS assigns them to your application. Your application uses these to obtain access tokens. |
| client ID | The âclient IDâ is essentially your applicationâs username and can be found in the My Apps section of the Autodesk DevPortal. It is a 32-character alphanumeric string (e.g., 5zw90va0UuwMKTnPS5sLsdgZjDkVYXN7). Your application passes it as the value for the *client_id* query parameter, and APS returns it in the *client_id* attribute in the returned JSON payload.       Other platforms, sometimes call this a âconsumer keyâ or âAPI key.â |
| client secret | The âclient secretâ is not supported by this application type as it assumes that your application cannot protect application credentials residing on the userâs computer or device.       Other platforms sometimes call this a âconsumer secretâ or âAPI secret.â |
| two-legged authentication | Two-legged tokens are not supported by this application type. |
| three-legged authentication | When an application needs to access resources belonging to an end user, that user must explicitly provide authorization. The typical mechanism, in the case of a web application, is for the application to redirect the user to an Autodesk login page with information about which of the userâs resources it wishes to access. The user then provides explicit consent, authorizing APS to grant the referring application the requested access. APS then redirects the user back to the application, using a callback URL that you provide, and your application can then access the required resources.       This kind of authentication is called âthree-leggedâ because your application, APS, and the end user make up the three âlegsâ of the authentication. When you use the Authorization Code grant type, APS issues an authorization code to your application to exchange it to obtain access tokens and refresh tokens. |
| callback URL | In certain contexts, your application needs to hand over part of the authentication to APS. For example, in three-legged authentication for a web application, your application redirects the end user to an Autodesk login page, so that the user can tell APS that your application is authorized to act on the userâs behalf. The callback URL is what is passed to the Autodesk login page to tell it how to redirect the user back to your application.       Callback URLs are specified in two places. You first register one or more callback URLs for your application in the My Apps section of the Autodesk DevPortal. Then, when you redirect your user to the Autodesk login page, you also specify the callback URL in the *redirect_uri* parameter. This allows you to use different callback URLs in different parts of your application. APS validates any run-time callback URLs against registered with your application.             See the GET authorize documentation for more details on the relationship between the callback URL field and the *redirect_uri* parameter.             Note that if your application does not require three-legged authentication, you can put any valid value in the callback URL field when you register your application, as no *redirect_uri* will ever be validated against it.      Multiple callback URLs can be supported by the Traditional Web App application type. |
| authorization code | In a three-legged authorization code grant type, APS passes an authorization code as a query parameter it appends to the callback URL at the time it redirects the end user back to the application.       Along with its client ID and secret, an application calls the POST token endpoint to exchange the authorization code for an access token.      The authorization code is a 40-character string (e.g., wroM1vFA4E-Aj241-quh_LVjm7UldawnNgYEHQ8I). |
| access token | APS returns an access token (sometimes just âtokenâ or âbearer tokenâ) at the end of a successful authentication. APS uses JSON Web Tokens (JWT), which are alphanumeric strings of variable length (including periods to separate their different parts), that the application uses in subsequent API calls to the platform. The platform keeps track of what resources the token is entitled to access, and either allows or denies access at call time.       Tokens have a limited lifespan and expire after a specified number of seconds. |
