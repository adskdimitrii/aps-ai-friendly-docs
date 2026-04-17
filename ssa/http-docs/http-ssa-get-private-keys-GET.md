# service-accounts/{serviceAccountId}/keys

Source: https://aps.autodesk.com/en/docs/ssa/reference/http/ssa-get-private-keys-GET/

---

Get All Keys

GET

# service-accounts/{serviceAccountId}/keys

Lists all keys associated with the service account. This operation will only return key metadata, not the private or public key.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/authentication/v2/service-accounts/{serviceAccountId}/keys |
| --- | --- |
| Authentication Context | app only |
| Required OAuth Scopes | `application:service_account_key:read` |
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

| 200   OK | The keys were successfully retrieved. |
| --- | --- |
| 400   Bad Request | The request was invalid. The service account may not be in an enabled state. Verify the service account status and retry the request. |
| 401   Unauthorized | The access token is invalid. It may have either expired or may not be a two-legged access token. Please verify the token and retry the request. |
| 403   Forbidden | The request was successfully validated but lacked the required permissions. Verify your credentials and permissions before you send this request again. |
| 404   Not Found | The service account is not found. Please verify the account details and retry the request. |
| 500   Internal Server Error | An unknown server-side error occurred. Please try again later. If the problem persists, please contact support. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| keys   array: object | Contains the details of a list of keys |
| --- | --- |
| kid   string | The ID of the private key |
| status   enum:string | The status of the key Possible values: `ENABLED`, `DISABLED` |
| createdAt   datetime: ISO 8601 | The creation time of the key, in UTC format |
| accessedAt   datetime: ISO 8601 | This is the most recent time an access token was generated for this service account key, in UTC format |

## [Example](#example)

This example illustrates the successful retrieval of all keys for a service account.

### Request

```
curl \
 --location \
 'https://developer.api.autodesk.com/authentication/v2/service-accounts/DKS2BNRDMTFV4RMB/keys' \
 --header 'Authorization: Bearer eyJh....' \

```

### Response

```
{
  "keys": [
    {
      "kid": "2ba69206-295d-43c7-9a89-66aad5c5e918",
      "status": "DISABLED",
      "createdAt": "2025-03-26 08:38:27 +0000 UTC",
      "accessedAt": "2025-03-26 08:38:27 +0000 UTC"
    },
    {
      "kid": "c546e44b-4b98-48cc-a4fa-7a3af5289af5",
      "status": "ENABLED",
      "createdAt": "2025-03-26 08:29:03 +0000 UTC",
      "accessedAt": "2025-03-26 08:29:03 +0000 UTC"
    }
  ]
}

```

Show More
