# service-accounts/{serviceAccountId}/keys

Source: https://aps.autodesk.com/en/docs/ssa/reference/http/ssa-create-service-account-key-POST/

---

Create Keys

POST

# service-accounts/{serviceAccountId}/keys

Creates a service account key.

A service account key is a public-private key pair, generated using RSA with a key length of 2048 bits by the Identity Authorization Service (AuthZ).

The private key is returned once during its creation. AuthZ only stores the public key.

A service account can have up to 3 keys at any given time.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/authentication/v2/service-accounts/{serviceAccountId}/keys |
| --- | --- |
| Authentication Context | app only |
| Required OAuth Scopes | `application:service_account_key:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [OAuth](../../oauth/http-docs/http-gettoken-POST.md) |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| serviceAccountId   string | The Autodesk ID of the service account |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | A key was successfully created for the specified service account. |
| --- | --- |
| 400   Bad Request | The request was invalid. The service account may not be in an enabled state. Verify the service account status and retry the request. |
| 401   Unauthorized | The access token is invalid. It may have either expired or may not be a two-legged access token. Please verify the token and retry the request. |
| 403   Forbidden | The service account may have reached its maximum key limit. Delete unused keys to create additional capacity and try again. |
| 404   Not Found | The service account is not found. Please verify the account details and retry the request. |
| 500   Internal Server Error | An unknown server-side error occurred. Please try again later. If the problem persists, please contact support. |

### Response

## [Body Structure (201)](#body-structure-201)

| kid   string | The ID of the private key. |
| --- | --- |
| privateKey   string | The private key value, in PEM format. |

## [Example](#example)

This example illustrates the successful creation of a key for a service account.

### Request

```
curl \
 --location \
 --request POST 'https://developer.api.autodesk.com/authentication/v2/service-accounts/DKS2BNRDMTFV4RMB/keys' \
 --header 'Authorization: Bearer eyJh....' \

```

### Response

```
{
  "kid": "c546e44b-4b98-48cc-a4fa-7a3af5289af5",
  "privateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIIEow.... ....gvjNX\n-----END RSA PRIVATE KEY-----\n"
}

```
