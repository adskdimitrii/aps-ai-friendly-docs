# projects/{projectId}/transmittals/{transmittalId}/folders

Source: https://aps.autodesk.com/en/docs/acc/reference/http/transmittals-listtransmittalfolders-GET/

---

List Transmittal Folders

GET

# projects/{projectId}/transmittals/{transmittalId}/folders

Retrieves all folders associated with the documents included in a specific transmittal.

The response lists the folder information as it existed when the transmittal was issued.

If the transmittal is still being processed, the endpoint returns status code `202` until the folder list becomes available.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/transmittals/v1/projects/{projectId}/transmittals/{transmittalId}/folders |
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

### Request

## [Query String Parameters](#query-string-parameters)

| limit   int | The maximum number of results to return per page. <br>Acceptable values: 1-200.<br>Default value: 20.<br>For example, to limit the response to two results per page, use `limit=2`. |
| --- | --- |
| offset   int | The index from which the response starts returning results. <br>Default value: 0.<br>For example, to skip the first three results, use `offset=3`. |
| sort   enum:string | Sorts the folders by a supported field and order. <br>By default, folders are sorted in ascending order by `name` (`name asc`).<br>To sort in descending order, add `desc` after the field name.<br>Format: `sort=<field> [asc or desc]`<br>Supported fields: `name`, `lastUpdatedAt`, `updatedByName`.<br>Examples:<br>`sort=name asc` â sorts folders alphabetically by name.`sort=lastUpdatedAt desc` â sorts folders by last updated time in descending order.<br>Possible values: `name`, `lastUpdatedAt`, `updatedByName`, `name asc`, `lastUpdatedAt asc`, `updatedByName asc`, `name desc`, `lastUpdatedAt desc`, `updatedByName desc` |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the folders of the transmittal |
| --- | --- |
| 202   Accepted | The transmittal has been created and is currently being processed but not ready for review yet. The folders list will be empty. |
| 400   Bad Request | Operation failed because of bad user input |
| 401   Unauthorized | Unauthorized error |
| 403   Forbidden | The user does not have permission to perform this operation. |
| 404   Not Found | The project or transmittal does not exist. |
| 500   Internal Server Error | Internal server error |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| results   array: object | The list of folders included in the transmittal. |
| --- | --- |
| urn   string | The URN of the folder. |
| name   string | The name of the folder. |
| description   string | The description of the folder. |
| lastUpdatedAt   datetime: ISO 8601 | The date and time when the folder was last modified, in ISO 8601 format. |
| updatedByName   string | The Autodesk ID of the user who last modified the folder. |
| updatedBy   string | The Autodesk ID of the user who last modified the folder. For details about the user, call [GET user](http-admin-projectsprojectId-users-userId-GET.md). |
| isDeleted   boolean | Indicates whether the folder is deleted. <br>`true` â The folder is deleted, either directly or because its parent folder was deleted.<br>`false` â The folder is not deleted. |
| pagination   object | The list of pagination details for the response. |
| limit   int | The maximum number of results returned per page. |
| offset   int | The number of results skipped before the current page, starting from zero. |
| totalResults   int | The total number of results that match the query, regardless of pagination. |
| nextUrl   string | The URL to retrieve the next page of transmittal folders. If not included, this is the last page. |

### Response

## [Body Structure (202)](#body-structure-202)

| results   array: object | This list of folders will be empty. |
| --- | --- |

## [Example](#example)

Successfully retrieved transmittal folders

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/transmittals/v1/projects/657a5565-09b7-48e0-bd03-acacfe42efaf/transmittals/88c286a3-4100-4251-8d0e-830e7726fc17/folders' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response (200)

```
{
  "results": [
    {
      "urn": "urn:adsk.wipprod:fs.folder:co.93vIs_WjTw2aynKiXkYVKA",
      "name": "Building Design",
      "description": "Design PDF files",
      "lastUpdatedAt": "2025-04-19T01:38:27.306Z",
      "updatedByName": "John Smith",
      "updatedBy": "8T4JUUX7NCG726NJ",
      "isDeleted": false
    }
  ],
  "pagination": {
    "limit": 1,
    "offset": 0,
    "totalResults": 10,
    "nextUrl": "https://developer.api.autodesk.com/construction/transmittals/v1/projects/657a5565-09b7-48e0-bd03-acacfe42efaf/transmittals/88c286a3-4100-4251-8d0e-830e7726fc17/folders?limit=1&offset=1"
  }
}

```

Show More

### Response (202 when transmittal is being processed)

```
{
  "results": [],
  "pagination": {
    "limit": 1,
    "offset": 0,
    "totalResults": 0,
    "nextUrl": null
  }
}

```

Show More
