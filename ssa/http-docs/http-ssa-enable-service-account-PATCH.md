# service-accounts/{serviceAccountId}

Source: https://aps.autodesk.com/en/docs/ssa/reference/http/ssa-enable-service-account-PATCH/

---

Enable or Disable Service Account

PATCH

# service-accounts/{serviceAccountId}

Enables or disables a service account.

When a service account is in the disabled state, it loses its capability to manage its service account key.
Assertions signed by the key will be treated as invalid.

This operation allows enabling a service account that is in a diabled state.

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/authentication/v2/service-accounts/{serviceAccountId} |
| --- | --- |
| Authentication Context | app only |
| Required OAuth Scopes | `application:service_account:write` |
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

### Request

## [Body Structure](#body-structure)

| status*   enum:string | The status of the service account Possible values: `ENABLED`, `DISABLED` |
| --- | --- |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The service account was successfully updated. |
| --- | --- |
| 400   Bad Request | The request was invalid. The service account may already be in the requested state. Verify the current state of the service account and retry the request. |
| 401   Unauthorized | The access token is invalid. It may have either expired or may not be a two-legged access token. Please verify the token and retry the request. |
| 403   Forbidden | The request was successfully validated but lacked the required permissions. Verify your credentials and permissions before you send this request again. |
| 404   Not Found | The service account is not found. Please verify the account details and retry the request. |
| 500   Internal Server Error | An unknown server-side error occurred. Please try again later. If the problem persists, please contact support. |

### Response

## [Body Structure (200)](#body-structure-200)

| serviceAccountId   string | The Autodesk ID of the service account |
| --- | --- |
| email   string | The email address of the service account |
| createdBy   string | The client ID used to create the service account |
| status   enum:string | The status of the service account Possible values: `ENABLED`, `DISABLED`, `DEACTIVATED` |
| createdAt   string | The creation time of the service account |
| accessedAt   string | This is the most recent time an access token was generated for this service account |
| expiresAt   string | The expiration time of the service account |

## [Example 1](#example-1)

This example illustrates the successful disabling of a service account.

### Request

```
curl \
   --location \
   --request PATCH 'https://developer.api.autodesk.com/authentication/v2/service-accounts/6BNJQT7RR7GTJ5QY' \
   --header 'Authorization: Bearer eyJh....' \
   --header 'Content-Type: application/json' \
   --data '{
     "status": "DISABLED"
 }'

```

Show More

### Response (200)

```
{
  "serviceAccountId": "6BNJQT7RR7GTJ5QY",
  "email": "service-mycompany-filesync@Ycw2Usv4XY38AfkvTIJTtEUVx8xNUORpJm31IILNtPvTXwGu.adskserviceaccount.com",
  "createdBy": "Ycw2Usv4XY38AfkvTIJTtEUVx8xNUORpJm31IILNtPvTXwGu",
  "status": "DISABLED",
  "createdAt": "2025-03-26 04:58:26 +0000 UTC",
  "accessedAt": "2025-03-26 04:58:26 +0000 UTC",
  "expiresAt": "2026-03-26 04:58:26 +0000 UTC"
}

```

Show More

## [Example 2](#example-2)

This example illustrates what happens when you request disabling of a service account that is already disabled.

### Request

```
curl \
   --location \
   --request PATCH 'https://developer.api.autodesk.com/authentication/v2/service-accounts/6BNJQT7RR7GTJ5QY' \
   --header 'Authorization: Bearer eyJh....' \
   --header 'Content-Type: application/json' \
   --data '{
     "status": "DISABLED"
 }'

```

Show More

### Response (400)

```
{
  "title": "invalid_request",
  "detail": "The service account is already in a disabled state."
}

```

## [Example 3](#example-3)

This example illustrates the successful enabling of a disabled service account.

### Request

```
curl \
   --location \
   --request PATCH 'https://developer.api.autodesk.com/authentication/v2/service-accounts/6BNJQT7RR7GTJ5QY' \
   --header 'Authorization: Bearer eyJh....' \
   --header 'Content-Type: application/json' \
   --data '{
     "status": "ENABLED"
 }'

```

Show More

### Response (200)

```
{
  "serviceAccountId": "6BNJQT7RR7GTJ5QY",
  "email": "service-mycompany-filesync@Ycw2Usv4XY38AfkvTIJTtEUVx8xNUORpJm31IILNtPvTXwGu.adskserviceaccount.com",
  "createdBy": "Ycw2Usv4XY38AfkvTIJTtEUVx8xNUORpJm31IILNtPvTXwGu",
  "status": "ENABLED",
  "createdAt": "2025-03-26 04:58:26 +0000 UTC",
  "accessedAt": "2025-03-26 04:58:26 +0000 UTC",
  "expiresAt": "2026-03-26 04:58:26 +0000 UTC"
}

```

Show More
