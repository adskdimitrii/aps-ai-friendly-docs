# projects/{projectId}/exports

Source: https://aps.autodesk.com/en/docs/acc/reference/http/sheets-exports-POST/

---

Exports

POST

# projects/{projectId}/exports

Exports up to 1000 sheets from the from the Sheets tool in Forma Build into a new downloadble PDF file.

You can export any published sheets. For details about publishing sheets, see the [Add and Publish Sheets to the Field](https://help.autodesk.com/view/BUILD/ENU/?guid=Upload_And_Publish_Sheets) help documentation.

To perform the export operation, a user must have at least export permission. For more information on permissions, see the [Sheets Permissions](https://help.autodesk.com/view/BUILD/ENU/?guid=Sheet_Permissions) help documentation.

The POST export endpoint enables the export of PDFs with both standard and feature markups. The supported features currently include Issues and Photos. For additional details on feature markups, see the [Feature Markups](https://help.autodesk.com/view/BUILD/ENU/?guid=Feature_Markups) help documentation.

This endpoint provides the flexibility to designate which types of markups you would like to export. This can be published, unpublished, or both, and is applicable to each markup type including standard, Issues, and Photos. For more information about published and unpublished markups, see the [Create and Style Markups](https://help.autodesk.com/view/BUILD/ENU/?guid=Create_Style_Markups) help documentation.

This endpoint gives you the flexibility to decide which types of markups to export, be it published, unpublished, or both. This is applicable to each markup type including standard, Issues, and Photos. For more information about published and unpublished markups, see the [Create and Style Markups](https://help.autodesk.com/view/BUILD/ENU/?guid=Create_Style_Markups) help documentation.

In the case of standard markups, the endpoint also allows the inclusion of attached links to relevant Sheets, Files, RFIs, Forms, Submittals, and Assets. For more information about markup links, see the [Add References to Markups](https://help.autodesk.com/view/BUILD/ENU/?guid=Markups_References) help documentation.

Note that this endpoint is asynchronous and initiates a job that runs in the background, rather than halting execution of your program. The response returns an export ID which you can use to poll [GET exports/:exportId](http-sheets-exports-exportId-GET.md) to check the job’s status. When the job is complete, you can retrieve the data you need to download the exported sheets.

For more details about exporting sheets, see the [Export and Print Sheets](https://help.autodesk.com/view/BUILD/ENU/?guid=Export_Sheets) tutorial.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/sheets/v1/projects/{projectId}/exports |
| --- | --- |
| Authentication Context | User context optional |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a two-legged access token obtained via a [Client Credentials Grant flow](../../oauth/how-to-docs/get-2-legged-token.md), or a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). <br>The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context. |
| --- | --- |
| x-user-id   string | The ID of the user on whose behalf the API request is made. This header is optional when using a 2-legged OAuth2, but required if using 2-legged OAuth2 with user impersonation. <br>When using 2-legged OAuth2 without user impersonation, your app has access to all users defined by the administrator in the SaaS integrations UI. However, when user impersonation is enabled, the API call is restricted to act only on behalf of the specified user. This header is not relevant for 3-legged OAuth2.<br>You can use either the user’s Forma ID (id), or their Autodesk ID (autodeskId). |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](../how-to-docs/getting-started-retrieve-account-and-project-id.md). You can use a project ID either with a “b.” prefix or without a “b.” prefix. For instance, a project ID of “b.a4be0c34a-4ab7” can also be referred to as “a4be0c34a-4ab7”. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

Expand all

| options   object | The criteria for the markups and links that should be included with the exported sheets. <br>Note that unpublished markups are only visible to their creator. |
| --- | --- |
| outputFileName   string | The name of the file that will be generated by the export process. Note that this name should not include the file extension. The maximum character limit for this field is 255 characters. |
| standardMarkups   object | The list of types of standard markups and their associated links that you want to include in the export. <br>By default markups will be exported and hyperlinks will not be exported. |
| includePublishedMarkups   boolean | `true`: (default) include all published standard markups in the exported sheets. Note that published markups are visible to all project members. <br>`false`: export sheets without including published standard markups. |
| includeUnpublishedMarkups   boolean | `true`: (default) standard markups that are visible only to their creators will be included in the exported sheets. <br>`false`: exported sheets will exclude unpublished markups. |
| includeMarkupLinks   boolean | `true`: include links in the markups. Supported links are links to Sheets, Files, RFIs, Forms, Submittals, and Assets. <br>`false`: (default) do not include links in markups.<br>Note that if both `includePublishedMarkups` and `includeUnpublishedMarkups` are set to `false`, this parameter will be treated as `false`. |
| issueMarkups   object | The list of types of issue markups to export. |
| includePublishedMarkups   boolean | `true`: published issue markups will be included in the exported sheets. <br>`false`: (default) published issue markups will not be included in the exported sheets. |
| includeUnpublishedMarkups   boolean | `true`: include issue markups in the exported sheets that are visible only to their creators or assignees. <br>`false`: (default) export sheets without including unpublished issue markups. |
| photoMarkups   object | The list of types of photo markups to export. |
| includePublishedMarkups   boolean | `true`: published photo markups will be included in the exported sheets. <br>`false`: (default) published photo markups will not be included in the exported sheets. |
| includeUnpublishedMarkups   boolean | `true`: include photo markups in the exported sheets that are visible only to their creators or assignees. <br>`false`: (default) export sheets without including unpublished photo markups. |
| sheets   array: string | The list of sheet UUIDs that you want to include in the export. A maximum of 1000 sheets can be included. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 202   Accepted | Successfully created an export job |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. <br>Sample error code with possible messages:<br>ERR_BAD_INPUT: <br>  Failed to parse the token  User id is required |
| 401   Unauthorized | The provided bearer token is not valid. <br>Sample error code with possible messages:<br>ERR_AUTHENTICATED_ERROR: <br>  Authentication header is not correct |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. <br>Sample error code with possible messages:<br>ERR_NOT_ALLOWED: <br>  Hub inactive  Project inactive  User inactive  API access denied  User {userId} does not have download permission on resource {resource} |
| 404   Not Found | The requested resources, such as the project, hub, user, or sheet do not exist. <br>Sample error code with possible messages:<br>ERR_RESOURCE_NOT_EXIST: <br>  Some resources are not found  Hub not found  Project not found  Project user not found |
| 500   Internal Server Error | An unknown error occurred on the server. <br>Sample error code with possible messages:<br>ERR_INTERNAL_SERVER_ERROR: <br>  Request failed for internal exception xxx  Failed to get hub  Failed to get project  Failed to get user |

### Response

## [Body Structure (202)](#body-structure-202)

| id   string: UUID | The ID of the export job. Use the ID to poll [GET exports/:exportId](http-sheets-exports-exportId-GET.md) to check the job’s status. When the job is complete, you can retrieve the data you need to download the exported sheets. |
| --- | --- |
| status   enum:string | The status of the export job; will always be: `processing` |

## [Example](#example)

Successfully created an export job

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/sheets/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/exports' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "options": {
          "outputFileName": "output_file_name",
          "standardMarkups": {
            "includePublishedMarkups": true,
            "includeUnpublishedMarkups": true,
            "includeMarkupLinks": false
          },
          "issueMarkups": {
            "includePublishedMarkups": false,
            "includeUnpublishedMarkups": false
          },
          "photoMarkups": {
            "includePublishedMarkups": false,
            "includeUnpublishedMarkups": false
          }
        },
        "sheets": [
          ""
        ]
      }'

```

Show More

### Response

```
{
  "id": "5b4bb914-c123-4f10-87e3-579ef934aaf9",
  "status": "processing"
}

```
