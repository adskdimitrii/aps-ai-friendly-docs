# APS OAuth Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Overview & Fundamentals

Introductory and conceptual material for understanding APS OAuth. Covers the OAuth basics, a developer field guide, and a high-level overview of the authentication system.

- [Overview](developers-guide-docs/overview.md)
- [Basics](developers-guide-docs/basics.md)
- [Field Guide](developers-guide-docs/field-guide.md)

### App Types & Authentication Patterns

Explains the different application types supported by APS and how to choose the right OAuth flow for each.

- [App Types Overview](developers-guide-docs/App-types-App-types.md)
- [Machine-to-Machine](developers-guide-docs/App-types-Machine-to-machine.md)
- [Native Apps](developers-guide-docs/App-types-native.md)
- [Traditional Web Apps](developers-guide-docs/App-types-traditionalweb.md)

### Authentication Flows (How-To Guides)

Step-by-step tutorials for obtaining tokens and setting up your application. Covers 2-legged, 3-legged, PKCE, and ID token flows.

- [Create an App](how-to-docs/create-app.md)
- [Get a 2-Legged Token](how-to-docs/get-2-legged-token.md)
- [Get a 3-Legged Token](how-to-docs/get-3-legged-token.md)
- [Get a 3-Legged Token (PKCE)](how-to-docs/get-3-legged-token-pkce-get-3-legged-token-pkce.md)
- [Get a 3-Legged Token (PKCE – Private)](how-to-docs/get-3-legged-token-pkce-get-3-legged-token-pkce-private.md)
- [Get an ID Token](how-to-docs/get-ID-token.md)
- [Code Challenge](how-to-docs/code-challenge.md)

### API Endpoints (HTTP Reference)

Full HTTP reference for all OAuth endpoints — authorization, token issuance, introspection, revocation, logout, OpenID configuration, and asymmetric keys.

- [GET /authorize](http-docs/http-authorize-GET.md)
- [POST /gettoken](http-docs/http-gettoken-POST.md)
- [POST /introspect](http-docs/http-introspect-POST.md)
- [POST /revoke](http-docs/http-revoke-POST.md)
- [GET /logout](http-docs/http-logout-GET.md)
- [GET /openid-configuration](http-docs/http-openid-GET.md)
- [GET /asymmetrickeys](http-docs/http-asymmetrickeys-GET.md)

### Scopes & Security

Covers the available OAuth scopes and asymmetric encryption details used in token signing and verification.

- [Scopes](developers-guide-docs/scopes.md)
- [Asymmetric Encryption](developers-guide-docs/asymmetric-encryption.md)

### Rate Limiting & Error Handling

Guidance on API rate limits specific to OAuth and the Forge platform, plus error handling strategies.

- [OAuth Rate Limits](developers-guide-docs/rate-limiting-oauth-rate-limits.md)
- [Forge Rate Limits](developers-guide-docs/rate-limiting-forge-rate-limits.md)
- [Error Handling](developers-guide-docs/error_handling.md)
<!-- GENERATED:CONTENT_SUMMARY:END -->
