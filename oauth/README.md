# APS OAuth Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Overview & Fundamentals

Introductory and conceptual material covering OAuth basics, a developer field guide, and error handling guidance. 4 files.

- [Overview](developers-guide-docs/overview.md)
- [Basics](developers-guide-docs/basics.md)
- [Field Guide](developers-guide-docs/field-guide.md)
- [Error Handling](developers-guide-docs/error_handling.md)

### Application Types

Conceptual guides covering the different OAuth app types supported by APS: generic app types, machine-to-machine (2-legged), native/desktop, and traditional web apps. 4 files.

- [App Types Overview](developers-guide-docs/App-types-App-types.md)
- [Machine-to-Machine Apps](developers-guide-docs/App-types-Machine-to-machine.md)
- [Native Apps](developers-guide-docs/App-types-native.md)
- [Traditional Web Apps](developers-guide-docs/App-types-traditionalweb.md)

### Scopes & Security

Reference material on OAuth scopes and asymmetric encryption used in token signing. 2 files.

- [Scopes](developers-guide-docs/scopes.md)
- [Asymmetric Encryption](developers-guide-docs/asymmetric-encryption.md)

### Rate Limiting

Rate limit guidance specific to OAuth endpoints and the broader Forge/APS platform. 2 files.

- [OAuth Rate Limits](developers-guide-docs/rate-limiting-oauth-rate-limits.md)
- [Forge Rate Limits](developers-guide-docs/rate-limiting-forge-rate-limits.md)

### Authentication Flows (How-To)

Step-by-step guides for obtaining tokens and setting up an application. Covers 2-legged, 3-legged, PKCE, and ID token flows.

- [Create an App](how-to-docs/create-app.md)
- [Get 2-Legged Token](how-to-docs/get-2-legged-token.md)
- [Get 3-Legged Token](how-to-docs/get-3-legged-token.md)
- [Get 3-Legged Token (PKCE)](how-to-docs/get-3-legged-token-pkce-get-3-legged-token-pkce.md)
- [Get 3-Legged Token (PKCE – Private Client)](how-to-docs/get-3-legged-token-pkce-get-3-legged-token-pkce-private.md)
- [Generate Code Challenge](how-to-docs/code-challenge.md)
- [Get ID Token](how-to-docs/get-ID-token.md)

### HTTP API Reference

Full HTTP endpoint documentation for the OAuth API. 7 endpoints.

- [GET /authorize](http-docs/http-authorize-GET.md)
- [POST /gettoken](http-docs/http-gettoken-POST.md)
- [POST /revoke](http-docs/http-revoke-POST.md)
- [POST /introspect](http-docs/http-introspect-POST.md)
- [GET /logout](http-docs/http-logout-GET.md)
- [GET /openid-configuration](http-docs/http-openid-GET.md)
- [GET /asymmetrickeys](http-docs/http-asymmetrickeys-GET.md)
<!-- GENERATED:CONTENT_SUMMARY:END -->
