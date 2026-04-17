# service-accounts/{serviceAccountId}

Source: https://aps.autodesk.com/en/docs/ssa/reference/http/ssa-delete-service-account-DELETE/

---

Delete Service Account

DELETE

# service-accounts/{serviceAccountId}

Deletes an existing service account. When a service account is deleted, all associated keys will also be deleted.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/authentication/v2/service-accounts/{serviceAccountId} |
| --- | --- |
| Authentication Context | app only |
| Required OAuth Scopes | `application:service_account:write` |
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

| 204   No Content | The service account was successfully deleted. |
| --- | --- |
| 401   Unauthorized | The access token is invalid. It may have either expired or may not be a two-legged access token. Please verify the token and retry the request. |
| 403   Forbidden | The request was successfully validated but lacked the required permissions. Verify your credentials and permissions before you send this request again. |
| 404   Not Found | The service account is not found. Please verify the account details and retry the request. |
| 500   Internal Server Error | An unknown server-side error occurred. Please try again later. If the problem persists, please contact support. |

### Response

## [Body Structure (204)](#body-structure-204)

Response for 204 has no body.

## [Example](#example)

This example illustrates the successful deletion of a service account. This request has no response body. It only has a response header.

### Request

```
curl \
  --location \
  --request DELETE 'https://developer.api.autodesk.com/authentication/v2/service-accounts/6BNJQT7RR7GTJ5QY' \
  --header 'Authorization: Bearer eyJh....' \

```

### Response (204)

```
HTTP/1.1 204 No Content
Date: Wed, 26 Mar 2025 07:14:57 GMT
Content-Type: application/json; charset=utf-8
Connection: keep-alive
strict-transport-security: max-age=31536000; includeSubDomains; preload
x-content-type-options: nosniff
x-request-id: 4e20cbb3-dd9e-4729-bb59-d923a6e87531
x-frame-options: SAMEORIGIN
ratelimit-remaining: 9
ratelimit-value: 10

```

Show More
