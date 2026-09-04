# APS Token Flex Friendly Docs

Documentation for the Token Flex Usage Data API (query and export token consumption data for Token Flex contracts).

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Developer's Guide

Orientation, authentication, rate limits, and error handling for the Token Flex API.

- [Overview](developers-guide-docs/overview.md)
- [API Basics](developers-guide-docs/basics.md)
- [Authentication](developers-guide-docs/authentication.md)
- [APS Rate Limits and Quotas](developers-guide-docs/rate-limits-forge-rate-limits.md)
- [Token Flex Rate Limits and Quota](developers-guide-docs/rate-limits-tokenflex-rate-limits.md)
- [Error Handling](developers-guide-docs/error_handling.md)

### Tutorials

Step-by-step guides for querying and exporting usage data.

- [Query Usage Information](how-to-docs/query.md)
- [Export Usage Information](how-to-docs/export.md)

### Contracts API

HTTP reference for retrieving contract metadata and enrichment data.

- [GET /contract](http-docs/http-contract-GET.md) — all contracts
- [GET /contract/{contract_number}](http-docs/http-contract-contract_number-GET.md)
- [GET /contract/{contract_number}/{field}](http-docs/http-contract-contract_number-field-GET.md)
- [GET /contract/{contract_number}/enrichment](http-docs/http-contract-contract_number-enrichment-GET.md)
- [GET /contract/{contract_number}/enrichment/{enrichment_category}](http-docs/http-contract-contract_number-enrichment-enrichment_category-GET.md)

### Usage API

HTTP reference for querying token usage summaries and running asynchronous usage queries.

- [GET /usage/{contract_number}/summary](http-docs/http-usage-contract_number-summary-GET.md)
- [GET /usage/{contract_number}/last](http-docs/http-usage-contract_number-last-GET.md)
- [POST /usage/{contract_number}/query](http-docs/http-usage-contract_number-query-POST.md) — submit an async usage query
- [GET /usage/{contract_number}/query/{query_id}](http-docs/http-usage-contract_number-query-query_id-GET.md) — poll for query results

### Export API

HTTP reference for scheduling and requesting bulk usage-data exports.

- [POST /export/{contract_number}/requests](http-docs/http-export-contract_number-requests-POST.md) — create an export request
- [GET /export/{contract_number}/requests](http-docs/http-export-contract_number-requests-GET.md) — list export requests
- [GET /export/{contract_number}/requests/{request_key}](http-docs/http-export-contract_number-requests-request_key-GET.md), [DELETE](http-docs/http-export-contract_number-requests-request_key-DELETE.md)
- [POST /export/{contract_number}/requests/{request_key}/refreshUrl](http-docs/http-export-contract_number-requests-request_key-refreshUrl-POST.md) — refresh a signed download URL
- [POST /export/{contract_number}/requests/{request_key}/retry](http-docs/http-export-contract_number-requests-request_key-retry-POST.md) — retry a failed export
- [POST /export/{contract_number}/requests/markRead](http-docs/http-export-contract_number-requests.markRead-POST.md) — mark requests as read
- [GET /export/{contract_number}/schedules](http-docs/http-export-contract_number-schedules-GET.md), [POST](http-docs/http-export-contract_number-schedules-POST.md) — recurring export schedules
- [GET /export/{contract_number}/schedules/{schedule_id}](http-docs/http-export-contract_number-schedules-schedule_id-GET.md), [PUT](http-docs/http-export-contract_number-schedules-schedule_id-PUT.md), [DELETE](http-docs/http-export-contract_number-schedules-schedule_id-DELETE.md)
<!-- GENERATED:CONTENT_SUMMARY:END -->

## Source

Autodesk APS Token Flex docs:
- https://aps.autodesk.com/en/docs/tokenflex/v1/developers_guide/overview/
- https://aps.autodesk.com/en/docs/tokenflex/v1/tutorials/query/
- https://aps.autodesk.com/en/docs/tokenflex/v1/reference/http/
