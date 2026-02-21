# OIDC Specification

Source: https://aps.autodesk.com/en/docs/oauth/v2/reference/http/openid-GET/

---

Token

GET

# OIDC Specification

Openid-configuration is a Well-known URI Discovery Mechanism for the Provider Configuration URI and is defined in OpenID Connect (OIDC). Openid-configuration is a URI defined within OpenID Connect which provides configuration information about the Identity Provider (IDP).

This endpoint retrieves the metadata as a JSON listing of OpenID/OAuth endpoints, supported scopes and claims, public keys used to sign the tokens, and other details.

For more information, see [OpenID Connect Discovery Specification](https://openid.net/specs/openid-connect-discovery-1_0.html)

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/.well-known/openid-configuration |
| --- | --- |
| Data Format | JSON |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful request; metadata returned. |
| --- | --- |
| 500   Internal Server Error | Generic internal server error. |

### Response

## [Body Structure (200)](#body-structure-200)

The response body for a successful call is a flat JSON object with the following attributes:

| issuer   string | Issuer URL |
| --- | --- |
| authorization_endpoint   string | Browser URL to redirect an end user in order to acquire the userâs consent for your app to access the specified resources. |
| token_endpoint   string | Retrieves a two-legged or three-legged access token. |
| userinfo_endpoint   string | Retrieves the user information. |
| jwks_uri   string | Retrieves the list of public keys in the JWKS format. |
| revoke_endpoint   string | Takes an access token or refresh token and revokes it. |
| introspect_endpoint   string | Examines an access token including the reference token and returns the status information of the tokens. |
| scopes_supported   array | List of supported scopes |
| response_types_supported   array | Supported response types |
| response_modes_supported   array | Supported response modes |
| grant_types_supported   array | Supported grant types |
| subject_types_supported   array | Supported subject types |
| id_token_signing_alg_values_supported   array | Signing algorithm value |

## [Example](#example)

Successful retrieval of the list of metadata (200)

### Request

```
curl -v 'https://developer.api.autodesk.com/.well-known/openid-configuration' \
     -X 'GET' \

```

### Response

```
HTTP/1.1 200 OK

{
 "issuer": https://developer.api.autodesk.com,
 "authorization_endpoint": https://developer.api.autodesk.com/authentication/v2/authorize,
 "token_endpoint": https://developer.api.autodesk.com/authentication/v2/token,
 "userinfo_endpoint": https://api.userprofile.autodesk.com/userinfo,
 "jwks_uri": https://developer.api.autodesk.com/authentication/v2/keys,
 "revoke_endpoint": https://developer.api.autodesk.com/authentication/v2/revoke,
 "introspect_endpoint": https://developer.api.autodesk.com/authentication/v2/introspect,
 "scopes_supported": [
   "user-profile:read",
   "user:read",
   "user:write",
   "viewables:read",
   "data:read",
   "data:write",
   "data:create",
   "data:search",
   "bucket:create",
   "bucket:read",
   "bucket:update",
   "bucket:delete",
   "code:all",
   "account:read",
   "account:write",
   "openid"
 ],
 "response_types_supported": [
   "code",
   "code id_token",
   "id_token"
 ],
 "response_modes_supported": [
   "fragment",
   "form_post",
   "query"
 ],
 "grant_types_supported": [
   "authorization_code",
   "client_credentials",
   "refresh_token"
 ],
 "subject_types_supported": [
   "public"
 ],
 "id_token_signing_alg_values_supported": [
   "RS256"
 ]
}

```

Show More
