# Token Flex Rate Limits and Quota

Source: https://aps.autodesk.com/en/docs/tokenflex/developers_guide/rate-limits/tokenflex-rate-limits/

---

# Token Flex Rate Limits and Quota

The Token Flex service observes rate limits and a quota to ensure that all clients get sufficient service and that runaway applications don’t consume excessive resources. [APS Rate Limits and Quotas](rate-limits-forge-rate-limits.md) describes rate limits and quotas in general.

## [Rate Limits](#rate-limits)

The Token Flex service limits requests per user (identified by their Autodesk account user name). In other words, the rate limits measure the total number of requests made by all applications belonging to each user.

Token Flex’s sustained rate limit is five requests per minute per user as measured over an eight hour period. During that period, a user may have a single burst of 50 transactions per minute over the period of a minute.

If a customer exceeds the rate limit, the customer’s applications receive an HTTP 429 error (described in detail in [APS Rate Limits and Quotas](rate-limits-forge-rate-limits.md)).

## [Quota](#quota)

Token Flex has a single quota affecting a single endpoint.

### Scope

Token Flex’s quota is enforced in scope the same way its rate limits are enforced: across all applications belonging to a single user.

### Endpoint

Token Flex’s quota affects this endpoint:

| Method | Endpoint | Limit Description | Limit | Units | Notification |
| --- | --- | --- | --- | --- | --- |
| POST | /export/:contract_number/requests | The maximum number of outstanding export requests (requests currently running) | 50 | Outstanding export requests | HTTP 429 response |

### Quota Violation Notification

The Token Flex service returns an HTTP 429 error (described in detail in [APS Rate Limits and Quotas](rate-limits-forge-rate-limits.md)) if an application attempts to go past the quota.

## [Changing Limits](#changing-limits)

[APS Rate Limits and Quotas](rate-limits-forge-rate-limits.md) describes how to request rate limit changes for APS APIs.
