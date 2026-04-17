# service-accounts/{serviceAccountId}

Source: https://aps.autodesk.com/en/docs/ssa/reference/http/ssa-get-service-account-GET/

---

Get Service Account

GET

# service-accounts/{serviceAccountId}

Retrieves the details for a service account.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/authentication/v2/service-accounts/{serviceAccountId} |
| --- | --- |
| Authentication Context | app only |
| Required OAuth Scopes | `application:service_account:read` |
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

| 200   OK | The service account was successfully retrieved. |
| --- | --- |
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
| createdAt   datetime: ISO 8601 | The creation time of the service account, in UTC format |
| accessedAt   datetime: ISO 8601 | This is the most recent time an access token was generated for this service account, in UTC format |
| expiresAt   datetime: ISO 8601 | The expiration time of the service account, in UTC format |

## [Example 1](#example-1)

This example illustrates the successful retrieval of a service account.

### Request

```
curl \
  --location 'https://developer.api.autodesk.com/authentication/v2/service-accounts/6BNJQT7RR7GTJ5QY' \
  --header 'Authorization: Bearer eyJh....' \

```

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

## [Example 2](#example-2)

This example illustrates what happens when the service account ID is not specified correctly.

### Request

```
curl \
  --location 'https://developer.api.autodesk.com/authentication/v2/service-accounts/6BNJQT7RR7GTJ5QN' \
  --header 'Authorization: Bearer eyJh....' \

```

### Response (404)

```
{
  "title": "not_found",
  "detail": "The service account is not found."
}

```
