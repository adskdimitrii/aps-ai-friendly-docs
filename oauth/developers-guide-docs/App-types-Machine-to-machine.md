# Server-to-Server App

Source: https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/App-types/Machine-to-machine/

---

# Server-to-Server App

Choose the **Server-to-Server** application type when you are creating a server-side application with no end user. It uses the *Client Credentials grant type*, where your application stores its client ID and client secret safely, and then passes those details to APS in exchange for a two-legged access token.

## [Client Credentials Grant Type](#client-credentials-grant-type)

At a high-level, the *Client Credentials grant type* has only two steps:

1. Your application passes its client credentials to the APS Authorization Server.
2. If the credentials are accurate, the Authorization Server responds with an access token.

We use the Client Credentials type in this case as it is intended for server-side (confidential) client applications with no end user, which normally describes server-to-server communication. See [Client Credentials grant type](../http-docs/http-gettoken-POST.md) for more details, and an example.

[![../../../_images/server-to-server.svg](../../../_images/server-to-server.svg)](../../../_images/server-to-server.svg)

There are a number of concepts that you need to be familiar with relevant to this application type and grant type:

| Term | Meaning |
| --- | --- |
| app | The âappâ, or âapplicationâ, is the code that youâre writing that calls APS APIs. It can be a web application, a headless server process, a mobile app, or even embedded firmware. Within the APS developer portal, your application is registered in the My Apps section.       Sometimes âappâ refers to your code; other times, it refers to the entity registered in the Dev Portal. It will be clear from context which is meant.      When you register your application in the APS developer portal, you select the APIs that you want to bind it to. This ensures that even if you lose control of your authentication credentials, calls cannot be made on your behalf to APIs the application was not designed for.          A registered application has assigned to it credentials called a âclient IDâ and âclient secret.â These are analogous to a username and password, except that you do not select them; APS assigns them to your application. Your application uses these to obtain access tokens. |
| client ID | The âclient IDâ is essentially your applicationâs username and can be found in the My Apps section of the Autodesk DevPortal. It is a 32-character alphanumeric string (e.g., 5zw90va0UuwMKTnPS5sLsdgZjDkVYXN7). Your application passes it as the value for the *client_id* query parameter, and APS returns it in the *client_id* attribute in the returned JSON payload.       Other platforms, sometimes call this a âconsumer keyâ or âAPI key.â |
| client secret | The âclient secretâ is essentially your applicationâs password and can be found next to the client ID in the My Apps section of the Autodesk DevPortal. It is a 16-character alphanumeric string (e.g., 7I6uN1rjneirxiMW), and your application passes it as the value for the *client_secret* query parameter.       Other platforms sometimes call this a âconsumer secretâ or âAPI secret.â |
| two-legged authentication | This is often considered the default type of authentication, and it is the simplest. When your application needs to call the API without having to access resources that require an end userâs permission (for example, translating a design file from one format to another), the communication is directly between your application and APS.       This kind of authentication is called âtwo-leggedâ because your application and APS are the two âlegs.â |
| three-legged authentication | Three-legged authentication is not supported with the Server-to-Server application type as communication does not involve the third leg (the end user). |
| access token | APS returns an access token (sometimes just âtokenâ or âbearer tokenâ) at the end of a successful authentication. APS uses JSON Web Tokens (JWT), which are alphanumeric strings of variable length (including periods to separate their different parts), that the application uses in subsequent API calls to the platform. The platform keeps track of what resources the token is entitled to access, and either allows or denies access at call time.       Tokens have a limited lifespan and expire after a specified number of seconds. |
