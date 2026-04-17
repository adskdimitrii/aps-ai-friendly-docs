# service-accounts

Source: https://aps.autodesk.com/en/docs/ssa/reference/http/ssa-get-service-accounts-GET/

---

Get All Service Accounts

GET

# service-accounts

Retrieves all service accounts associated with an application.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/authentication/v2/service-accounts |
| --- | --- |
| Authentication Context | app only |
| Required OAuth Scopes | `application:service_account:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via [OAuth](../../oauth/http-docs/http-gettoken-POST.md) |
| --- | --- |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The service accounts were successfully retrieved. |
| --- | --- |
| 401   Unauthorized | The access token is invalid. It may have either expired or may not be a two-legged access token. Please verify the token and retry the request. |
| 403   Forbidden | The request was successfully validated but lacked the required permissions. Verify your credentials and permissions before you send this request again. |
| 500   Internal Server Error | An unknown server-side error occurred. Please try again later. If the problem persists, please contact support. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| serviceAccounts   array: object | Contains details of a list of service accounts |
| --- | --- |
| serviceAccountId   string | The Autodesk ID of the service account |
| email   string | The email address of the service account |
| createdBy   string | The client ID used to create the service account |
| status   enum:string | The status of the service account Possible values: `ENABLED`, `DISABLED`, `DEACTIVATED` |
| createdAt   datetime: ISO 8601 | The creation time of the service account, in UTC format |
| accessedAt   datetime: ISO 8601 | This is the most recent time an access token was generated for this service account, in UTC format |
| expiresAt   datetime: ISO 8601 | The expiration time of the service account, in UTC format |

## [Example](#example)

This example illustrates the successful retrieval of all service accounts for the calling server-to-server app.

### Request

```
curl \
  --location 'https://developer.api.autodesk.com/authentication/v2/service-accounts' \
  --header 'Authorization: Bearer eyJh....' \

```

### Response

```
{
  "serviceAccounts": [
    {
      "serviceAccountId": "6BNJQT7RR7GTJ5QY",
      "email": "service-mycompany-filesync@Ycw2Usv4XY38AfkvTIJTtEUVx8xNUORpJm31IILNtPvTXwGu.adskserviceaccount.com",
      "createdBy": "Ycw2Usv4XY38AfkvTIJTtEUVx8xNUORpJm31IILNtPvTXwGu",
      "status": "ENABLED",
      "createdAt": "2025-03-26 04:58:26 +0000 UTC",
      "accessedAt": "2025-03-26 04:58:26 +0000 UTC",
      "expiresAt": "2026-03-26 04:58:26 +0000 UTC"
    },
    {
      "serviceAccountId": "DKS2BNRDMTFV4RMB",
      "email": "acmeasean-sales-reports@Ycw2Usv4XY38AfkvTIJTtEUVx8xNUORpJm31IILNtPvTXwGu.adskserviceaccount.com",
      "createdBy": "Ycw2Usv4XY38AfkvTIJTtEUVx8xNUORpJm31IILNtPvTXwGu",
      "status": "ENABLED",
      "createdAt": "2025-03-26 04:57:30 +0000 UTC",
      "accessedAt": "2025-03-26 04:57:30 +0000 UTC",
      "expiresAt": "2026-03-26 04:57:30 +0000 UTC"
    },
    {
      "serviceAccountId": "TFRJ7BPMM7R4YBKM",
      "email": "acmeasean-it-reports@Ycw2Usv4XY38AfkvTIJTtEUVx8xNUORpJm31IILNtPvTXwGu.adskserviceaccount.com",
      "createdBy": "Ycw2Usv4XY38AfkvTIJTtEUVx8xNUORpJm31IILNtPvTXwGu",
      "status": "ENABLED",
      "createdAt": "2025-03-26 04:57:10 +0000 UTC",
      "accessedAt": "2025-03-26 04:57:10 +0000 UTC",
      "expiresAt": "2026-03-26 04:57:10 +0000 UTC"
    }
  ]
}

```

Show More
