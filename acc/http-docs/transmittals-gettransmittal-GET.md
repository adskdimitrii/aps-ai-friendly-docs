# projects/{projectId}/transmittals/{transmittalId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/transmittals-gettransmittal-GET/

---

Get a Project Transmittal

GET

# projects/{projectId}/transmittals/{transmittalId}

Retrieves a transmittal by ID within the specified project.

The response includes the transmittalâs metadata, status, sender, recipients, and other related details.

If the transmittal is still being processed (`status = SENDING`), some fieldsâsuch as `recipients` and `externalMembers`âmay be temporarily empty until processing completes.

The visibility of recipient details also depends on the transmittalâs `displayRecipients` setting.

For information about creating transmittals, see the [Create Transmittals](https://help.autodesk.com/view/BUILD/ENU/?guid=Create_Transmittal&p=DOCS) tutorial.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/transmittals/v1/projects/{projectId}/transmittals/{transmittalId} |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](/en/docs/oauth/v2/tutorials/get-2-legged-token) or [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| x-user-id   string | The Autodesk ID of the user on whose behalf the request is made. <br>This header is required only when using two-legged authentication. It is not needed for three-legged authentication.<br>Your application can access only those users who are assigned to it in the SaaS Integrations UI.<br>Only user Autodesk IDs (`autodeskId`) are supported. |

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring: UUID The ID of the project. You can retrieve the project ID using the [Data Management API](/en/docs/data/v2/). For more details, see the [Retrieve a Project ID](/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial.You may provide the project ID with or without the `b.` prefix:

- With prefix: `b.657a5565-09b7-48e0-bd03-acacfe42efaf`
- Without prefix: `657a5565-09b7-48e0-bd03-acacfe42efaf`
- transmittalIdstring: UUID The ID of the transmittal. To find the ID, call [GET transmittals](/en/docs/acc/v1/reference/http/transmittals-listtransmittals-GET/).

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the transmittal details. <br>If the transmittal is still being processed, the `recipients` and `externalMembers` fields will be empty |
| --- | --- |
| 400   Bad Request | Operation failed because of bad user input |
| 401   Unauthorized | Unauthorized error |
| 403   Forbidden | The user does not have permission to perform this operation. |
| 404   Not Found | The project or transmittal does not exist |
| 500   Internal Server Error | Internal server error |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| id   string: UUID | The unique identifier of the transmittal. |
| --- | --- |
| sequenceId   string | A project-specific number automatically assigned when the transmittal is first submitted. It identifies the transmittal within the project and reflects the order in which it was created. |
| title   string | The title of the transmittal. |
| message   string | An optional message included with the transmittal. |
| status   enum:string | The current processing state of the transmittal. <br>`SENDING` â The transmittal is being processed or packaged; some fields may be temporarily empty. The `recipients` and `externalMembers` fields may be temporarily empty.`COMPLETED` â The transmittal has been successfully issued and all data is available.`FAILED` â The transmittal failed to process or send.<br>Possible values: `SENDING`, `COMPLETED`, `FAILED`. |
| sentBy   object | Information about the user who created and sent the transmittal. |
| autodeskId   string | The Autodesk ID of the transmittal creator. |
| email   string | The email of the transmittal creator. |
| name   string | The full name of the transmittal creator. |
| companyAutodeskId   string | The Autodesk ID of the creatorâs company at the time the transmittal was created. |
| companyName   string | The name of the creatorâs company at the time the transmittal was created. |
| recipients   object | The list of recipients included in the transmittal, grouped by user, company, and role. <br>For more information on how to add recipients to a transmittal, see the [Create Transmittals](https://help.autodesk.com/view/BUILD/ENU/?guid=Create_Transmittal&p=DOCS) documentation. |
| users   array: object | The list of individual users who were added as recipients. |
| autodeskId   string | The Autodesk ID of the user recipient. |
| name   string | The name of the user recipient. |
| companies   array: object | The list of companies that were added as recipients. |
| autodeskId   string | The Autodesk ID of the company recipient. |
| name   string | The name of the company recipient. |
| roles   array: object | The list of project roles that were added as recipients. |
| autodeskId   string | The Autodesk ID of the role recipient. |
| name   string | The name of the role recipient. |
| externalMembers   array: object | The list of external recipients who are not members of the project. |
| name   string | The name of the external recipient. |
| email   string | The email address of the external recipient. |
| createdAt   datetime: ISO 8601 | The date and time when the transmittal was created, in ISO 8601 format. |
| documentsCount   int | The total number of documents included in the transmittal. |
| packedStatus   enum:string | Indicates the progress of packaging transmittal files into a ZIP archive. Possible values: `SUCCESS`, `PARTIAL_SUCCESS`, `FAILED`, `PROCESSING`, `EXPIRED`, `NOT_ALLOWED` |
| displayRecipients   enum:string | Specifies how much recipient information each recipient can see.  > `ALL` â All recipients can view the full recipient list.`LIMITED` â Each recipient can view only their own recipient information.<br>Project Admins and the sender always see the full list. <br>Possible values: `ALL`, `LIMITED` |

## [Example](#example)

Successfully retrieved the transmittal details.

If the transmittal is still being processed, the `recipients` and `externalMembers` fields will be empty

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/transmittals/v1/projects/6fbcdf65-f2e4-4dd4-86bd-96febe58ff82/transmittals/88c286a3-4100-4251-8d0e-830e7726fc17' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "id": "88c286a3-4100-4251-8d0e-830e7726fc17",
  "sequenceId": "25",
  "title": "Building design",
  "message": "This is a building design pdf",
  "status": "COMPLETED",
  "sentBy": {
    "autodeskId": "HWUBNU689CRH",
    "email": "john.smith@email.com",
    "name": "John Smith",
    "companyAutodeskId": "156891388",
    "companyName": "BuildCo Ltd."
  },
  "recipients": {
    "users": [
      {
        "autodeskId": "HWUBNU689CRH",
        "name": "John Smith"
      }
    ],
    "companies": [
      {
        "autodeskId": "73758762",
        "name": "Autodesk Inc."
      }
    ],
    "roles": [
      {
        "autodeskId": "233404534",
        "name": "designer"
      }
    ]
  },
  "externalMembers": [
    {
      "name": "John Smith",
      "email": "john.smith@email.com"
    }
  ],
  "createdAt": "2025-04-03T09:42:17.476Z",
  "documentsCount": 2,
  "packedStatus": "SUCCESS",
  "displayRecipients": "ALL"
}

```

Show More
