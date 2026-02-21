# projects/{projectId}/settings

Source: https://aps.autodesk.com/en/docs/acc/reference/http/takeoff-projects-project_id-settings-GET/

---

Settings

GET

# projects/{projectId}/settings

Retrieves the measurement system settings for a project.

For more information about measurement system settings, see the [ACC Configure Takeoff Settings](https://help.autodesk.com/view/TAKEOFF/ENU/?guid=Configure_Takeoff_Settings) help documentation.

To configure the measurement system settings, call [PATCH settings](/en/docs/acc/v1/reference/http/takeoff-projects-project_id-settings-PATCH/).

Note that settings for Takeoff cannot be changed once takeoff types and items have been created in the project.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/takeoff/v1/projects/{projectId}/settings |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| region   string | Specifies the region where the service is located. <br>Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](/en/docs/acc/v1/overview/acc-regions) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>This corresponds to project ID in the [Data Management API](/en/docs/data/v2/), and can be specified in the form of âUUIDâ or b.âUUIDâ.<br>To learn how to find the project ID, see the [Retrieve ACC Account and project ID](/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. |
| --- | --- |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully retrieved the measurement system settings. |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource could not be found. |
| 429   Too Many Requests | Rate limit exceeded; wait some time before retrying. The âRetry-Afterâ header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

| measurementSystem   enum:string | The project measurement system. <br>Possible values: `IMPERIAL`, `METRIC`. |
| --- | --- |

## [Example](#example)

Successfully retrieved the measurement system settings.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/takeoff/v1/projects/:projectId/settings' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "measurementSystem": "IMPERIAL"
}

```
