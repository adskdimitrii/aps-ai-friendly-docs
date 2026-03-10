# projects/{projectId}/settings

Source: https://aps.autodesk.com/en/docs/acc/reference/http/takeoff-projects-project_id-settings-PATCH/

---

Settings

PATCH

# projects/{projectId}/settings

Updates the measurement system settings for a project.

For more information about measurement system settings, see the [ACC Configure Takeoff Settings](https://help.autodesk.com/view/TAKEOFF/ENU/?guid=Configure_Takeoff_Settings) help documentation.

Note that settings for Takeoff cannot be changed once takeoff types and items have been created in the project.

To check if a project contains takeoff types and items, call [GET packages](http-takeoff-projects-project_id-packages-GET.md) and use the package IDs (`results[i].id`) to call [GET takeoff-types](http-takeoff-projects-project_id-packages-package_id-takeoff-types-GET.md).

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | PATCH https://developer.api.autodesk.com/construction/takeoff/v1/projects/{projectId}/settings |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| region   string | Specifies the region where the service is located. <br>Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string: UUID | The ID of the project. <br>This corresponds to project ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/), and can be specified in the form of “UUID” or b.”UUID”.<br>To learn how to find the project ID, see the [Retrieve ACC Account and project ID](../how-to-docs/getting-started-retrieve-account-and-project-id.md) tutorial. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

| measurementSystem*   enum:string | The project measurement system. <br>Possible values: `IMPERIAL`, `METRIC`. |
| --- | --- |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successfully updated the measurement system settings. |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource could not be found. |
| 429   Too Many Requests | Rate limit exceeded; wait some time before retrying. The ‘Retry-After’ header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

| measurementSystem   enum:string | The project measurement system. <br>Possible values: `IMPERIAL`, `METRIC`. |
| --- | --- |

## [Example](#example)

Successfully updated the measurement system settings.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/takeoff/v1/projects/:projectId/settings' \
  -X 'PATCH' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "measurementSystem": "IMPERIAL"
      }'

```

### Response

```
{
  "measurementSystem": "IMPERIAL"
}

```
