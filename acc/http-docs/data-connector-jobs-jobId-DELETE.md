# accounts/{accountId}/jobs/{jobId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/data-connector-jobs-jobId-DELETE/

---

# accounts/{accountId}/jobs/{jobId}

Cancels the specified running job spawned by a data request created by the authenticated user. The user must have project administrator or executive overview permissions.

Use GET requests/:requestId/jobs to get the jobs spawned by a request along with their job IDs. A cancelled job will still appear as a spawned job with a completion status of cancelled .

To understand the basics of requests, the jobs they spawn, and the data extracts returned by the jobs, see the Data Connector API Field Guide .

## Resource Information

Method and URI DELETE https://developer.api.autodesk.com/data-connector/v1/accounts/:accountId/jobs/:jobId Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow.

### Request

## URI Parameters

accountId string: UUID The account ID. You can derive it from your hub ID if necessary: Use GET hubs in the Data Management API to retrieve your hub ID. Remove the initial âb.â from the hub ID to get your account ID. jobId string: UUID The job ID

### Response

## HTTP Status Code Summary

204 No Content The specified object is successfully deleted. 400 Bad Request The parameters are invalid. 401 Unauthorized The provided bearer token is invalid. 403 Forbidden Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The resource or endpoint cannot be found. 429 Too Many Requests Rate limited exceeded; wait some time before retrying. 500 Internal Server Error An unexpected error occurred on the server. 503 Service Unavailable Service unavailable.

### Response

## Body Structure (204)

Response for 204 has no body.

## Example

The specified object is successfully deleted.

### Request

```
curl -v 'https://developer.api.autodesk.com/data-connector/v1/accounts/:accountId/jobs/:jobId' \ -X 'DELETE' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
204 No Content
```
