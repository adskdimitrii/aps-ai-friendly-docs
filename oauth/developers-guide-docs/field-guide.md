# Field Guide

Source: https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/field-guide/

---

# Field Guide

## [Client](#client)

The âClientâ is the application requesting access to a protected resource on behalf of the Resource Owner (User). There are 2 types of Clients namely Confidential Clients and Public Clients.

### Confidential Clients

Confidential clients are those who have the capability to keep the client_secret confidential. Mostly, these clients are only apps that run on a server under the developerâs control, with no access to the source code by the user.

A web application with a secure backend that uses the Authorization Code Flow is considered a Confidential application.

### Public Clients

Public Clients are those who cannot hold credentials securely. Hence, public applications can only use grant types that do not require the use of their client secret.

A native application that uses the Authorization Code Flow with PKCE to be deployed on end-user machines is considered a Public application.

## [Grant](#grant)

A grant is a protocol of acquiring an access token. Respective grant types are listed below under each Client. Refer to the [GET authorize](../http-docs/http-authorize-GET.md) endpoint reference for more information.

### Grant Types

Confidential applications can use grant types that require them to authenticate by specifying their client ID and client secret when calling the [Token endpoint](../http-docs/http-gettoken-POST.md).

Public applications can only use grant types that do not require the use of their client secret.

## [Client ID](#client-id)

The âclient IDâ is essentially your appâs username and can be found in the [My Apps](/myapps) section.

On other platforms, this is sometimes called âconsumer keyâ or âAPI keyâ.

It is an alphanumeric string (e.g., `5zw90va0UuwMKTnPS5sLsdgZjDkVYXN7`), and it is passed as the value for the `client_id` query parameter and JSON attribute.

## [Client Secret](#client-secret)

The âclient secretâ is essentially your appâs password and can be found next to the client ID in the [My Apps](/myapps) section.

On other platforms, this is sometimes called âconsumer secretâ or âAPI secretâ.

It is an alphanumeric string (e.g., `7I6uN1rjneirxiMW`), and it is passed as the value for the `client_secret` query parameter.

If you lose control of your credentials, you can regenerate your client secret.

## [Authorization Code](#authorization-code)

In a three-legged authorization code grant type flow, an authorization code is passed through a `code` query parameter when the user is redirected back to the app via the callback URL. Anything returned this way is accessible to the end user and, in principle, any intermediate system (including spyware in a browser extension).

For this reason, returning an access token directly poses a security risk. But an authorization code on its own cannot be used to get an access token; the app has to supplement it with its client ID and secret in the [POST token](../http-docs/http-gettoken-POST.md) endpoint. Because the end user (and any part of the app that runs in the web browser) does not have the client ID and secret, the access token is not exposed.

The authorization code is a 40-character string (e.g., `wroM1vFA4E-Aj241-quh_LVjm7UldawnNgYEHQ8I`).

## [Access Token](#access-token)

An access token (sometimes just âtokenâ or âbearer tokenâ) is returned at the end of a successful authentication flow.

The token is used in subsequent API calls to APS. The platform keeps track of what resources the token is entitled to access and either allows or denies access at call time.

APS uses JSON Web Tokens (JWT), which are alphanumeric strings of variable length (including periods to spearate their different parts), and they are passed as the value for the `access_token` JSON attribute and `token` query parameter.

Tokens have a limited lifespan and expire after the number of seconds specified in the `expires_in` JSON attribute that is returned alongside the `access_token` attribute when it is first acquired.

The expiry duration for access token is 60 minutes.

## [Refresh Token](#refresh-token)

In a three-legged context, it would be very disruptive to require that an end user of your app be required to go through the authentication flow every time the access token expired. When your app obtains a three-legged token, it is also provided a refresh token.

It is a 42-character alphanumeric strings (e.g., `SDrclmgQSGyF79wjLqxQeEIjqELf0wE8aMym02PjRy`), and it is passed as the value for the `refresh_token` query parameter and JSON attribute.

In a three-legged context, the [POST token](../http-docs/http-gettoken-POST.md) endpoint returns a JSON object that includes a refresh token. For example:

```
{
  "token_type": "Bearer",
  "expires_in": 1800,
  "refresh_token": "f2NWXxfnJOJMA1cW4k2zjFwmphf8vZjEUx3kmplFfn",
  "access_token": "9WlQeEpOdVrAO9SOH8ab4m00Ngrd"
}

```

The expiry duration for refresh token is 15 days.
