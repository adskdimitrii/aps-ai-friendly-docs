# APS OAuth Friendly Docs

Lightweight, local Markdown mirror of Autodesk APS OAuth documentation.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Overview & Fundamentals
Core concepts and general guidance for working with APS OAuth services. Includes an [Overview](developers-guide-docs/overview.md) of the authentication system, [Basics](developers-guide-docs/basics.md) of OAuth flows, a [Field Guide](developers-guide-docs/field-guide.md) for quick reference, [Scopes](developers-guide-docs/scopes.md) reference for permission management, and [Error Handling](developers-guide-docs/error_handling.md) guidance. (5 files)

### Application Types
Guidance on choosing and configuring the right OAuth application type for your use case. Covers an [App Types Overview](developers-guide-docs/App-types-App-types.md), [Machine-to-Machine](developers-guide-docs/App-types-Machine-to-machine.md) (service accounts/server-side), [Native Apps](developers-guide-docs/App-types-native.md) (desktop/mobile), and [Traditional Web Apps](developers-guide-docs/App-types-traditionalweb.md). (4 files)

### Authentication Flows & Token Acquisition
Step-by-step how-to guides and API endpoints for obtaining tokens:
- [Create an App](how-to-docs/create-app.md) — register your application
- [Get 2-Legged Token](how-to-docs/get-2-legged-token.md) — client credentials flow (machine-to-machine)
- [Get 3-Legged Token](how-to-docs/get-3-legged-token.md) — authorization code flow (user context)
- [Get 3-Legged Token with PKCE](how-to-docs/get-3-legged-token-pkce-get-3-legged-token-pkce.md) and [PKCE (Private)](how-to-docs/get-3-legged-token-pkce-get-3-legged-token-pkce-private.md) — PKCE variants for public and confidential clients
- [Code Challenge](how-to-docs/code-challenge.md) — generating PKCE code challenges
- [Get ID Token](how-to-docs/get-ID-token.md) — OpenID Connect identity tokens
- [GET /authorize](http-docs/http-authorize-GET.md) — authorization endpoint
- [POST /gettoken](http-docs/http-gettoken-POST.md) — token endpoint

(9 files across how-to-docs and http-docs)

### Token Management
API endpoints for managing issued tokens:
- [POST /introspect](http-docs/http-introspect-POST.md) — inspect token validity and metadata
- [POST /revoke](http-docs/http-revoke-POST.md) — revoke an access or refresh token

(2 files)

### Security & Asymmetric Encryption
Resources for key-based authentication and token verification:
- [Asymmetric Encryption Guide](developers-guide-docs/asymmetric-encryption.md) — concepts and usage
- [GET /asymmetrickeys](http-docs/http-asymmetrickeys-GET.md) — retrieve public keys for token verification

(2 files)

### OpenID Connect & Session Management
- [GET /openid](http-docs/http-openid-GET.md) — OpenID Connect discovery/configuration
- [GET /logout](http-docs/http-logout-GET.md) — end user sessions

(2 files)

### Rate Limiting
Throttling and quota details for API calls:
- [OAuth Rate Limits](developers-guide-docs/rate-limiting-oauth-rate-limits.md)
- [Forge Rate Limits](developers-guide-docs/rate-limiting-forge-rate-limits.md)

(2 files)
<!-- GENERATED:CONTENT_SUMMARY:END -->
