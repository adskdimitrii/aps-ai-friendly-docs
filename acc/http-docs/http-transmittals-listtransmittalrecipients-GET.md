# projects/{projectId}/transmittals/{transmittalId}/recipients

Source: https://aps.autodesk.com/en/docs/acc/reference/http/transmittals-listtransmittalrecipients-GET/

---

List Transmittal Recipients

GET

# projects/{projectId}/transmittals/{transmittalId}/recipients

Retrieves all recipients of a specific transmittal, including project members and external members.
> Recipient visibility in the response depends on the transmittalâs recipient visibility setting, which is configured in the Transmittals UI:

- If the visibility setting is `ALL`, project members can see all recipients.
- If the visibility setting is `LIMITED`, project members can see only their own recipient information.

Project Admins and the sender always see the full list of recipients, regardless of the visibility setting.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/transmittals/v1/projects/{projectId}/transmittals/{transmittalId}/recipients |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) or [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| x-user-id   string | The Autodesk ID of the user on whose behalf the request is made. <br>This header is required only when using two-legged authentication. It is not needed for three-legged authentication.<br>Your application can access only those users who are assigned to it in the SaaS Integrations UI.<br>Only user Autodesk IDs (`autodeskId`) are supported. |

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring: UUID The ID of the project. You can retrieve the project ID using the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/). For more details, see the [Retrieve a Project ID](../how-to-docs/getting-started-retrieve-account-and-project-id.md) tutorial.You may provide the project ID with or without the `b.` prefix:

- With prefix: `b.657a5565-09b7-48e0-bd03-acacfe42efaf`
- Without prefix: `657a5565-09b7-48e0-bd03-acacfe42efaf`
- transmittalIdstring: UUID The ID of the transmittal. To find the ID, call [GET transmittals](http-transmittals-listtransmittals-GET.md).

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the recipients of the transmittal. |
| --- | --- |
| 202   Accepted | The transmittal has been created and is currently being processed but is not yet ready for review. The `recipients` and `externalMembers` lists are empty. |
| 400   Bad Request | Operation failed because of bad user input |
| 401   Unauthorized | Unauthorized error |
| 403   Forbidden | The user does not have permission to perform this operation. |
| 404   Not Found | The project or transmittal does not exist |
| 500   Internal Server Error | Internal server error |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| recipients   array: object | The list of project-member recipients included in the transmittal. |
| --- | --- |
| autodeskId   string | The Autodesk ID of the recipient. |
| email   string | The recipients email address. |
| name   string | The recipientâs name. |
| companyAutodeskId   string | The Autodesk ID of the recipientâs company at the time the transmittal was issued. |
| companyName   string | The name of the recipientâs company at the time the transmittal was issued. |
| receivedAt   datetime: ISO 8601 | The date and time when the recipient received the transmittal (ISO 8601 format). |
| viewedAt   datetime: ISO 8601 | The date and time when the recipient first viewed the transmittal (ISO 8601 format). |
| downloadedAt   datetime: ISO 8601 | The date and time when the recipient first downloaded the transmittal (ISO 8601 format). |
| externalMembers   array: object | A list of external recipients included in the transmittal. |
| email   string | The email address of the external recipient. |
| name   string | The name of the external recipient. |
| companyName   string | The company name of the external recipient. This value may change if the external user later updates their company information. |
| role   string | The role name of the external recipient. |
| receivedAt   datetime: ISO 8601 | The date and time when the external recipient received the transmittal notification, in ISO 8601 format. |
| viewedAt   datetime: ISO 8601 | The date and time when the external recipient first viewed the transmittal, in ISO 8601 format. |
| downloadedAt   datetime: ISO 8601 | The date and time when the external recipient first downloaded the transmittal, in ISO 8601 format. |

### Response

## [Body Structure (202)](#body-structure-202)

| recipients   array: object | An empty array of recipients while the transmittal is still being processed. |
| --- | --- |
| externalMembers   array: object | An empty array of external recipients while the transmittal is still being processed. |

## [Example](#example)

Successfully retrieved transmittal recipients

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/transmittals/v1/projects/657a5565-09b7-48e0-bd03-acacfe42efaf/transmittals/88c286a3-4100-4251-8d0e-830e7726fc17/recipients' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response (200)

```
{
  "recipients": [
    {
      "autodeskId": "HWUBNU689CRH",
      "email": "john.smith@email.com",
      "name": "John Smith",
      "companyAutodeskId": "156891388",
      "companyName": "Autodesk Inc.",
      "receivedAt": "2025-04-19T01:38:27.306Z",
      "viewedAt": "2025-04-19T01:38:27.306Z",
      "downloadedAt": "2025-04-19T01:38:27.306Z"
    }
  ],
  "externalMembers": [
    {
      "email": "john.smith@email.com",
      "name": "John Smith",
      "companyName": "Autodesk Inc.",
      "role": "Construction",
      "receivedAt": "2025-04-19T01:38:27.306Z",
      "viewedAt": "2025-04-19T01:38:27.306Z",
      "downloadedAt": "2025-04-19T01:38:27.306Z"
    }
  ]
}

```

Show More

### Response (202 when transmittal is being processed)

```
{
  "recipients": [],
  "externalMembers": []
}

```
