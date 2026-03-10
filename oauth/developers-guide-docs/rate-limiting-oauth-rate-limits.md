# Authentication Rate Limits

Source: https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/rate-limiting/oauth-rate-limits/

---

# Authentication Rate Limits

The Authentication service observes a rate limit to ensure that all clients get sufficient service and that runaway applications do not consume excessive resources. [APS Rate Limits and Quotas](https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/forge-rate-limits/) describes rate limits and quotas in general.

## [Rate Limits](#rate-limits)

Rate limits specify a maximum number of API requests an Authentication service can make per minute. Authentication Rate limits may vary by endpoints as shown in the table below.

### Scope

The Authentication service sets a separate rate limit for each application making requests (specified by client ID) per API endpoint.

### Violation Notification

If an application exceeds an endpoint’s rate limit, the Authentication service returns an `HTTP 429` error (Refer to Notification section of Rate Limits in [APS Rate Limits and Quotas](https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/forge-rate-limits/)).

### Endpoint Rate Limits

Note that these rates are not service guaranteed. Uncommonly, when total service consumption is too high across all clients, then the accepted request rates may drop until traffic further subsides.

For detailed API default rate limits, please kindly refer to [Default API Rate Limit](https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/faq-overview/faq-defaultratelimit/).
