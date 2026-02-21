# Application Types

Source: https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/App-types/App-types/

---

# Application Types

This guide describes three types of applications, and their corresponding grant types, that you can register with APS using the **Create App** window in the APS developer portal.

In OAuth 2.0, a *grant type* â sometimes called a *grant flow* â refers to the method by which an application can obtain an *access token*. Using this method, the application is granted limited access to resources such as a service or data, without exposing credentials.

Based on the needs of your application, some grant types are more appropriate than others. This guide describes the grant type that is best suited to the type of application you are creating.

See the respective sections for a high-level overview of the grant type and the terminology relevant to each application type.

## [Traditional Web App](#traditional-web-app)

Choose the [Traditional Web App](/en/docs/oauth/v2/developers_guide/traditionalweb) application type when you are building a server-side (or web-site) application that is capable of securely storing secrets on your web server. It uses the *Authorization Code grant type*, where your application first obtains an authorization code, and then exchanges it for an access token.

## [Desktop, Mobile, and Single Page Web App](#desktop-mobile-and-single-page-web-app)

Choose [Desktop, Mobile, Single-Page Web App](/en/docs/oauth/v2/developers_guide/native) if you are creating a native application for a desktop computer or mobile device, or an SPA (single-page application) web application, where the application will be deployed on end-user machines on which you cannot protect your application credentials. It uses the *Authorization Code grant type* with a *Proof Key for Code Exchange* (*PKCE*).

**Note**: *Desktop, Mobile, and Single-Page Web App type* is unable to use any API that can incur Tokens consumption (known as Premium APIs), such as Model Derivative, Design Automation, and Reality Capture. If you need access to any of these APIs, use a different application type.

## [Server-to-Server App](#server-to-server-app)

Choose the [Server-to-Server](/en/docs/oauth/v2/developers_guide/Machine-to-machine) application type when you are creating a server-side application with no end user. It uses the *Client Credential grant type*, where your application stores its client ID and client secret safely, and then passes those details to APS in exchange for a two-legged access token.
