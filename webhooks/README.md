# APS Webhooks Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Server Setup & Security

Guides for setting up a webhook-receiving server and verifying the integrity of incoming payloads.

- [Configuring Your Server](how-to-docs/configuring-your-server.md)
- [Verify Payload Signature](how-to-docs/how-to-verify-payload-signature.md)

### Hook Lifecycle Management

How-to guides and HTTP reference for creating, retrieving, updating, and deleting hooks.

- [Retrieve List of Hooks](how-to-docs/retrieve-list-of-hooks.md)
- [Delete a Hook](how-to-docs/delete-a-hook.md)
- [GET /app/hooks](http-docs/http-webhooks-app-hooks-GET.md) — all hooks for an app
- [GET /hooks](http-docs/http-webhooks-hooks-GET.md) — all hooks across systems
- [GET /systems/{system}/hooks](http-docs/http-webhooks-systems-system-hooks-GET.md), [POST](http-docs/http-webhooks-systems-system-hooks-POST.md)
- [GET /systems/{system}/events/{event}/hooks](http-docs/http-webhooks-systems-system-events-event-hooks-GET.md), [POST](http-docs/http-webhooks-systems-system-events-event-hooks-POST.md)
- [GET /…/hooks/{hook_id}](http-docs/http-webhooks-systems-system-events-event-hooks-hook_id-GET.md), [PATCH](http-docs/http-webhooks-systems-system-events-event-hooks-hook_id-PATCH.md), [DELETE](http-docs/http-webhooks-systems-system-events-event-hooks-hook_id-DELETE.md)

### Service-Specific Hook Creation

Step-by-step guides for registering hooks against specific APS services (6 guides).

- [Data Management](how-to-docs/create-a-hook-data-management.md)
- [Model Derivative](how-to-docs/create-a-hook-model-derivative.md)
- [Issues](how-to-docs/create-a-hook-issues.md)
- [Cost Management](how-to-docs/create-a-hook-cost-management.md)
- [Reviews](how-to-docs/create-a-hook-reviews.md)
- [BuildingConnected](how-to-docs/create-a-hook-buildingconnected.md)

### Tokens API

HTTP reference for managing webhook secret tokens used for payload signature verification.

- [POST /tokens](http-docs/http-tokens-tokens-POST.md) — create a token
- [PUT /tokens/me](http-docs/http-tokens-tokens-me-PUT.md) — update current token
- [DELETE /tokens/me](http-docs/http-tokens-tokens-me-DELETE.md) — delete current token
<!-- GENERATED:CONTENT_SUMMARY:END -->

## Source

Autodesk APS Webhooks docs:
- https://aps.autodesk.com/en/docs/webhooks/v1/tutorials/
- https://aps.autodesk.com/en/docs/webhooks/v1/reference/http/
