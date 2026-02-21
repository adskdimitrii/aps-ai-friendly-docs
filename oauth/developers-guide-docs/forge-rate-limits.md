# APS Rate Limits and Quotas

Source: https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/rate-limiting/forge-rate-limits/

---

# APS Rate Limits and Quotas

The Autodesk Platform Service (APS) provides a set of cloud resources that are shared among many applications and services. Autodesk strives to ensure that there are plenty of cloud resources to serve all platform users. However, runaway applications and malicious attacks can quickly consume resources and diminish service. To avoid overconsumption and service degradation, APS sets rate limits and quotas for users of each of its services. This page describes how those rate limits and quotas work.

## [Rate Limits](#rate-limits)

Rate limits are simple: a rate limit sets the maximum number of API calls an application can make per minute. Rate limits help keep the number of API calls within the capacity of the service, and guard against instability and attacks such as denial-of-service attacks. This ensures availability and consistent quality of service for all users.

The rate limits may vary by each service or by endpoints within a service. Rate limits are currently placed at a generous level that shouldnât cause problems with applications running under normal circumstances. They may come into play and limit an application if the application generates an unusually high volume of API calls.

Rate limits are not guaranteed service levels. If a service is overloaded for any reason, request rate limits may effectively drop until the overload condition ends.

### Notification

When an application exceeds the published rate limit for a given endpoint, the API returns an `HTTP 429 "Too many requests"` response code. The response header has a parameter named `Retry-After` that specifies how many seconds to wait before making a new request. We strongly recommend that you retry a request only after the waiting period has elapsed.

The following example shows a typical 429 response.

#### Response Header (429)

```
HTTP/1.1 429 Too Many Requests
Content-Type: application/json
Retry-After: 25
Server: Apigee Router
Content-Length: 44

```

#### Response Body (429)

```
{"developerMessage":"Quota limit exceeded."}

```

## [Quotas](#quotas)

Quotas come into play after a service request is accepted. A quota limits an applicationâs use of resources as the application carries out activities within an APS service. Quotas may limit, for example, file sizes uploaded, downloaded, and processed; the amount of processing time allowed per job; an applicationâs monthly service consumption; and so on. Each APS service may have a set of built-in quotas. They may also offer custom quotas that a user or application can set to lower resource consumption below the built-in limits if desired to further restrict resource use.

Note again that quotas are not guaranteed service levels. Quota limits may drop temporarily if a service is overloaded.

### Notification

Exceeding a quota typically occurs when an API request specifies excessive resource use. The service receiving the request replies with an error response that specifies the quota violation. Sometimes, where resource use doesnât occur until after a request is received (the request places a job on a queue, for example), the quota violation occurs during later execution and throws an error there. In that case the requester may set up a callback to provide error notification. If a callback isnât possible, the requester can poll regularly (but not too frequently) to make sure that execution is carried out correctly.

## [Scope](#scope)

The scope of APS rate limits and quotas (how widely or narrowly they apply) varies across APIs and resource types. Scope is defined by how request rate or resource use is tallied: on the client side whether itâs tallied per user ID or application, for example, and on the service side whether itâs applied across an entire API, for example, or to individual endpoints or resources within an API.

### Rate Limit Scope

Rate limits on the client side may apply per user ID or per application. On the service side, a rate limit may apply across an entire API or to individual endpoints within an API, changing from one endpoint to another.

### Quota Scope

Quotas on the client side may apply per user ID or per application. On the service side, they may apply to a particular resource type, to the underlying engine servicing a request, to an endpoint, or other qualifying attributes. Because quotas are typically resource-specific, their scope is often narrowly defined.

API specific rate limit and quota pages spell out the scope for each APIâs rate limit and quota.

## [Requesting Rate Limit and Quota Changes](#requesting-rate-limit-and-quota-changes)

If a rate limit or quota causes problems for an application with reasonable resource use, you can request a limit or quota change by contacting support via <https://aps.autodesk.com/get-help>.
