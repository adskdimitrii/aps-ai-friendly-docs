# APS SSA (Secure Service Accounts) Friendly Docs

Documentation for the Secure Service Accounts (SSA) API, which allows applications to authenticate as a service identity rather than on behalf of a user.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Overview & Concepts

Foundational documentation for Service-to-Service Authentication (SSA), including architecture overview, API basics, naming conventions, and error handling.

- [Overview](developers-guide-docs/overview.md)
- [API Basics](developers-guide-docs/api-basics.md)
- [Error Handling](developers-guide-docs/error-handling.md)
- [Naming Guidelines](developers-guide-docs/naming-guidelines.md)
- [JWT Assertions](developers-guide-docs/jwt-assertions.md)

### Rate Limits

Rate limiting policies for both APS-wide and SSA-specific endpoints.

- [APS Rate Limits](developers-guide-docs/rate-limits-aps-rate-limits.md)
- [SSA Rate Limits](developers-guide-docs/rate-limits-ssa-rate-limits.md)

### Service Account Management (API Reference)

REST API endpoints for creating, retrieving, updating, and deleting service accounts and their keys (10 endpoints total).

- [POST Create Service Account](http-docs/http-ssa-create-service-account-POST.md)
- [GET Service Account](http-docs/http-ssa-get-service-account-GET.md)
- [GET Service Accounts](http-docs/http-ssa-get-service-accounts-GET.md)
- [PATCH Enable/Disable Service Account](http-docs/http-ssa-enable-service-account-PATCH.md)
- [DELETE Service Account](http-docs/http-ssa-delete-service-account-DELETE.md)
- [POST Create Service Account Key](http-docs/http-ssa-create-service-account-key-POST.md)
- [GET Private Keys](http-docs/http-ssa-get-private-keys-GET.md)
- [PATCH Enable/Disable Key](http-docs/http-ssa-enable-disable-key-PATCH.md)
- [DELETE Key](http-docs/http-ssa-delete-key-DELETE.md)
- [POST Exchange JWT Assertion](http-docs/http-ssa-exchange-jwt-assertion-POST.md)

### Getting Started & Tutorials

Step-by-step tutorials for onboarding with SSA, from initial setup through provisioning and token generation, plus ongoing account management guidance.

- [Before You Begin](tutorials-docs/getting-started-with-ssa-before-you-begin.md)
- [Task 1: Create an SSA](tutorials-docs/getting-started-with-ssa-task1-create-an-ssa.md)
- [Task 2: Provision the SSA to a Hub](tutorials-docs/getting-started-with-ssa-task2-provision-the-ssa-to-a-hub.md)
- [Task 3: Generate a 3-Legged Access Token](tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md)
- [Service Account Management](tutorials-docs/service-account-management.md)
<!-- GENERATED:CONTENT_SUMMARY:END -->
