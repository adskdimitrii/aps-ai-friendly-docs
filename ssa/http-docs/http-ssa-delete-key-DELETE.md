# service-accounts/{serviceAccountId}/keys/{keyId}

Source: https://aps.autodesk.com/en/docs/ssa/reference/http/ssa-delete-key-DELETE/

---

Delete Key

DELETE

# service-accounts/{serviceAccountId}/keys/{keyId}

Deletes an existing key.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/authentication/v2/service-accounts/{serviceAccountId}/keys/{keyId} |
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
| keyId   string | The ID of the private key |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 204   No Content | An unknown server-side error occurred. Please try again later. If the problem persists, please contact support. |
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

This example illustrates the successful deletion of a key. This request has no response body. It only has a response header.

### Request

```
curl \
 --location \
 --request DELETE 'https://developer.api.autodesk.com/authentication/v2/service-accounts/DKS2BNRDMTFV4RMB/keys/2ba69206-295d-43c7-9a89-66aad5c5e918' \
 --header 'Authorization: Bearer eyJh....' \
 --header 'Accept: application/json' \

```

### Response

```
HTTP/1.1 204 No Content

Date: Wed, 26 Mar 2025 09:10:27 GMT
Content-Type: application/json; charset=utf-8
Connection: keep-alive
strict-transport-security: max-age=31536000; includeSubDomains; preload
x-content-type-options: nosniff
x-request-id: b0ce104b-5040-4800-a388-09717d585a16
x-frame-options: SAMEORIGIN
ratelimit-remaining: 9
ratelimit-value: 10

```

Show More
