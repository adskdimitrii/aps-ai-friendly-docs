# service-accounts/{serviceAccountId}/keys/{keyId}

Source: https://aps.autodesk.com/en/docs/ssa/reference/http/ssa-enable-disable-key-PATCH/

---

Enable or Disable Key

PATCH

# service-accounts/{serviceAccountId}/keys/{keyId}

Enables or disables a service account key.

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/authentication/v2/service-accounts/{serviceAccountId}/keys/{keyId} |
| --- | --- |
| Authentication Context | app only |
| Required OAuth Scopes | `application:service_account_key:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [OAuth](../../oauth/http-docs/http-gettoken-POST.md) |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| serviceAccountId   string | The Autodesk ID of the service account |
| --- | --- |
| keyId   string | The ID of the private key |

### Request

## [Body Structure](#body-structure)

| status*   enum:string | The status of the service account key Possible values: `ENABLED`, `DISABLED` |
| --- | --- |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 204   No Content | The service account was successfully updated. |
| --- | --- |
| 400   Bad Request | The request was invalid. The service account may not be in an enabled state. Verify the service account status and retry the request. |
| 401   Unauthorized | The access token is invalid. It may have either expired or may not be a two-legged access token. Please verify the token and retry the request. |
| 403   Forbidden | The request was successfully validated but lacked the required permissions. Verify your credentials and permissions before you send this request again. |
| 404   Not Found | The service account or key is not found. Please verify the account and key details and retry the request. |
| 500   Internal Server Error | An unknown server-side error occurred. Please try again later. If the problem persists, please contact support. |

### Response

## [Body Structure (204)](#body-structure-204)

Response for 204 has no body.

## [Example](#example)

This example illustrates the successful enabling of a disabled key. This request has no response body. It only has a response header.

### Request

```
curl \
   --location \
   --request PATCH 'https://developer.api.autodesk.com/authentication/v2/service-accounts/DKS2BNRDMTFV4RMB/keys/2ba69206-295d-43c7-9a89-66aad5c5e918' \
   --header 'Authorization: Bearer eyJh....' \
   --header 'Accept: application/json' \
   --header 'Content-Type: application/json' \
   --data '{
     "status": "ENABLED"
 }'

```

Show More

### Response (200)

```
HTTP/1.1 204 No Content

Date: Wed, 26 Mar 2025 08:56:28 GMT
Content-Type: application/json; charset=utf-8
Connection: keep-alive
strict-transport-security: max-age=31536000; includeSubDomains; preload
x-content-type-options: nosniff
x-request-id: 2a93e933-4d12-4ae7-a683-448ccc2aad4c
x-frame-options: SAMEORIGIN
ratelimit-remaining: 9
ratelimit-value: 10

```

Show More
