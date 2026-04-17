# service-accounts

Source: https://aps.autodesk.com/en/docs/ssa/reference/http/ssa-create-service-account-POST/

---

Create Service Account

POST

# service-accounts

Creates a service account. Only a [server-to-server application](../../oauth/developers-guide-docs/App-types-Machine-to-machine.md) can own service accounts.

An application can have up to 10 service accounts at any given time.

Upon a successful response, the operation returns the service account ID and email address.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/authentication/v2/service-accounts |
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

## [Body Structure](#body-structure)

| name*   string | The name of the service account. Must be 5-100 characters long, contain only alphanumeric characters and dashes, and include at least one alphanumeric character. |
| --- | --- |
| firstName*   string | The first name of the service account. For display purposes only. <br>Must meet the following conditions:<br>Length between 5 and 100 charactersContain only alphanumeric characters, dashes, and underscoresInclude at least one alphanumeric characterAvoid inappropriate wordsExclude invalid characters such as the special characters `%` and `/`. Avoid the character pattern of `&#` even though the characters are allowed individually.<br>For more information, see [Naming Guidelines](../developers-guide-docs/naming-guidelines.md). |
| lastName*   string | The last name of the service account. For display purposes only. <br>Must meet the following conditions:<br>Length between 5 and 100 charactersContain only alphanumeric characters and dashesInclude at least one alphanumeric characterAvoid inappropriate wordsExclude invalid characters such as the special characters `%` and `/`. Avoid the character pattern of `&#` even though the characters are allowed individually.<br>For more information, see [Naming Guidelines](../developers-guide-docs/naming-guidelines.md). |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 201   Created | The service account was successfully created. |
| --- | --- |
| 400   Bad Request | The request was invalid due to one or more of the following issues: <br>The `name` attribute is incorrect or is already in use. Verify the `name` attribute adheres to the required constraints and is unique.The profile data, specifically `firstName` and `lastName`, is either empty or invalid. Ensure both attributes contain valid data.<br>Please correct the identified issues and resubmit the request. The response body may provide more details. |
| 401   Unauthorized | The access token is invalid. It may have either expired or may not be a two-legged access token. Please verify the token and retry the request. |
| 403   Forbidden | The provided Client ID is wrong or the number of service accounts that the application can have has reached the limit. Please verify the Client ID. If you’ve reached the limit, delete unused service accounts to create capacity. |
| 500   Internal Server Error | An unknown server-side error occurred. Please try again later. If the problem persists, please contact support. |

### Response

## [Body Structure (201)](#body-structure-201)

| serviceAccountId   string | The Autodesk ID of the service account. |
| --- | --- |
| email   string | The email address of the service account. It is of the form `<serviceAccountName>@<clientID>.adskserviceaccount.autodesk.com`. |

## [Example 1](#example-1)

This example illustrates the successful creation of a service account.

### Request

```
curl \
  --location 'https://developer.api.autodesk.com/authentication/v2/service-accounts' \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer eyJh...' \
  --header 'Content-Type: application/json' \
  --data '{
      "name": "service-mycompany-filesync",
      "firstName" : "service",
      "lastName" : "mycompany-filesync"
  }'

```

Show More

### Response (201)

```
{
  "serviceAccountId":"6BNJQT7RR7GTJ5QY",
  "email":"service-mycompany-filesync@Ycw2Usv4XY38AfkvTIJTtEUVx8xNUORpJm31IILNtPvTXwGu.adskserviceaccount.com"
}

```

## [Example 2](#example-2)

This example illustrates what happens when you try to create an account with a name that already exists.

### Request

```
curl \
  --location 'https://developer.api.autodesk.com/authentication/v2/service-accounts' \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer eyJh...' \
  --header 'Content-Type: application/json' \
  --data '{
      "name": "service-mycompany-filesync",
      "firstName" : "service",
      "lastName" : "mycompany-filesync"
  }'

```

Show More

### Response (400)

```
{
  "title": "invalid_request",
  "detail": "The 'name' already exists."
}

```
