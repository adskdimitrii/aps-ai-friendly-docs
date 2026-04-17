# SSA API Rate Limits

Source: https://aps.autodesk.com/en/docs/ssa/developers_guide/rate-limits/ssa-rate-limits/

---

# SSA API Rate Limits

The Secure Service Account (SSA) API implements rate limiting to ensure fair access and prevent resource abuse. This page details the specific rate limits for each SSA operation.

**Note:** For general information about APS rate limits and quotas, see [APS Rate Limits and Quotas](rate-limits-aps-rate-limits.md).

## [Overview](#overview)

All SSA API operations are subject to rate limits that restrict the number of requests per minute. Rate limits are applied per application (identified by Client ID) and per API endpoint.

**Key Points:**

- **Current limit:** All operations are limited to **10 requests per minute**
- **Scope:** Limits apply per application per endpoint
- **Error response:** Exceeding limits returns `HTTP 429 Too Many Requests`
- **Service availability:** Rates may be further reduced during high system load

## [What Happens When You Exceed the Limit?](#what-happens-when-you-exceed-the-limit)

When your application exceeds a rate limit, the SSA service returns an `HTTP 429 Too Many Requests` error. Refer to the Rate Limits section in [APS Rate Limits and Quotas](rate-limits-aps-rate-limits.md) for details on handling these responses.

**Note:** Rate limits are not service-level guarantees. During periods of high system load, actual accepted request rates may be lower than the documented limits.

## [API Rate Limits by Category](#api-rate-limits-by-category)

### Account Management Operations

Operations for creating, reading, updating, and deleting service accounts.

| Operation | Method + Endpoint | Rate Limit |
| --- | --- | --- |
| [Create Service Account](../http-docs/http-ssa-create-service-account-POST.md) | POST /service-accounts | 10 requests per minute |
| [Get All Service Accounts](../http-docs/http-ssa-get-service-accounts-GET.md) | GET /service-accounts | 10 requests per minute |
| [Get Service Account](../http-docs/http-ssa-get-service-account-GET.md) | GET /service-accounts/{serviceAccountId} | 10 requests per minute |
| [Enable or Disable Service Account](../http-docs/http-ssa-enable-service-account-PATCH.md) | PATCH /service-accounts/{serviceAccountId} | 10 requests per minute |
| [Delete Service Account](../http-docs/http-ssa-delete-service-account-DELETE.md) | DELETE /service-accounts/{serviceAccountId} | 10 requests per minute |

### Key Management Operations

Operations for managing cryptographic keys associated with service accounts.

| Operation | Method + Endpoint | Rate Limit |
| --- | --- | --- |
| [Create Keys](../http-docs/http-ssa-create-service-account-key-POST.md) | POST /service-accounts/{serviceAccountId}/keys | 10 requests per minute |
| [Get All Keys](../http-docs/http-ssa-get-private-keys-GET.md) | GET /service-accounts/{serviceAccountId}/keys | 10 requests per minute |
| [Enable or Disable Key](../http-docs/http-ssa-enable-disable-key-PATCH.md) | PATCH /service-accounts/{serviceAccountId}/keys/{keyId} | 10 requests per minute |
| [Delete Key](../http-docs/http-ssa-delete-key-DELETE.md) | DELETE /service-accounts/{serviceAccountId}/keys/{keyId} | 10 requests per minute |

### Token Exchange Operations

Operations for exchanging JWT assertions for access tokens.

| Operation | Method + Endpoint | Rate Limit |
| --- | --- | --- |
| [`Exchange JWT Assertion for Token`_](#id1) | POST /token | 10 requests per minute |

### Best Practices

To effectively work within rate limits and ensure optimal API performance:

- **Implement retry logic** with exponential backoff when receiving `HTTP 429` responses
- **Cache responses** when appropriate to reduce unnecessary API calls
- **Monitor your usage** to stay within rate limits and avoid service disruptions
- **Distribute requests** evenly over time rather than making burst requests
- **Use efficient polling intervals** when checking for status changes
