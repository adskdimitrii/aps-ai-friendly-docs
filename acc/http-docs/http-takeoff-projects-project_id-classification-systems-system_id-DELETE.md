# projects/{projectId}/classification-systems/{systemId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/takeoff-projects-project_id-classification-systems-system_id-DELETE/

---

Classification Systems

DELETE

# projects/{projectId}/classification-systems/{systemId}

Deletes a classification system from a project.

Note that this action will only succeed if there are no takeoff types and items associated with the classification system. The Takeoff API currently does not support dissociating types and items from a classification system. You dissociate takeoff types and items from a classification system in the UI.

To check if a classification system is associated with takeoff types and items, call [GET packages](http-takeoff-projects-project_id-packages-GET.md) and use the package IDs (`results[i].id`) to call [GET takeoff-types](http-takeoff-projects-project_id-packages-package_id-takeoff-types-GET.md). Iterate through the takeoff types and check if `classificationCodeOne` and `classificationCodeTwo` have a value for both `primaryQuantityDefinition` and `secondaryQuantityDefinition`.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | DELETE https://developer.api.autodesk.com/construction/takeoff/v1/projects/{projectId}/classification-systems/{systemId} |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| region   string | Specifies the region where the service is located. <br>Possible values: `US`, `EMEA`. For the full list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |

* Required

### Request

## [URI Parameters](#uri-parameters)

- systemIdstring: UUID The classification system ID. To find the ID, call [GET classification-systems](http-takeoff-projects-project_id-classification-systems-GET.md).
- projectIdstring: UUID The ID of the project. This corresponds to project ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/), and can be specified in the form of âUUIDâ or b.âUUIDâ.To learn how to find the project ID, see the [Retrieve ACC Account and project ID](../how-to-docs/getting-started-retrieve-account-and-project-id.md) tutorial.

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 204   No Content | Successfully deleted the classification system. |
| --- | --- |
| 400   Bad Request | The parameters of the requested operation are invalid. |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource could not be found. |
| 409   Conflict | Canât delete the classification system as some classifications are in use. |
| 429   Too Many Requests | Rate limit exceeded; wait some time before retrying. The âRetry-Afterâ header might provide the amount of the time to wait. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (204)](#body-structure-204)

Response for 204 has no body.

## [Example](#example)

Successfully deleted the classification system.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/takeoff/v1/projects/:projectId/classification-systems/:systemId' \
  -X 'DELETE' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
204 No Content

```
