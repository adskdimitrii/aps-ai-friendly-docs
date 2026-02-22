# APS Webhooks Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Hook Management (How-To Guides)

Tutorials for creating, retrieving, and deleting webhooks across various APS services. Covers setup for specific platforms and event types.

- [Create a Hook – Data Management](how-to-docs/create-a-hook-data-management.md)
- [Create a Hook – Model Derivative](how-to-docs/create-a-hook-model-derivative.md)
- [Create a Hook – Issues](how-to-docs/create-a-hook-issues.md)
- [Create a Hook – Cost Management](how-to-docs/create-a-hook-cost-management.md)
- [Create a Hook – BIM 360 Reviews](how-to-docs/create-a-hook-reviews.md)
- [Create a Hook – BuildingConnected](how-to-docs/create-a-hook-buildingconnected.md)
- [Retrieve List of Hooks](how-to-docs/retrieve-list-of-hooks.md)
- [Delete a Hook](how-to-docs/delete-a-hook.md)

### Security & Payload Verification (How-To Guides)

- [How to Verify Payload Signature](how-to-docs/how-to-verify-payload-signature.md) — guidance on validating webhook payload authenticity using signatures.
- [Configure Your Server](how-to-docs/configuring-your-server.md) — server setup requirements for receiving webhook events.

### Webhook API Reference (HTTP Endpoints)

Full HTTP reference for the Webhooks API, covering hook CRUD operations scoped by system and event.

- [GET /app/hooks](http-docs/http-webhooks-app-hooks-GET.md) — list all hooks for the current app
- [GET /hooks](http-docs/http-webhooks-hooks-GET.md) — list all hooks
- [GET /systems/{system}/hooks](http-docs/http-webhooks-systems-system-hooks-GET.md) — list hooks for a system
- [POST /systems/{system}/hooks](http-docs/http-webhooks-systems-system-hooks-POST.md) — create a system-level hook
- [GET /systems/{system}/events/{event}/hooks](http-docs/http-webhooks-systems-system-events-event-hooks-GET.md) — list hooks for a specific event
- [POST /systems/{system}/events/{event}/hooks](http-docs/http-webhooks-systems-system-events-event-hooks-POST.md) — create an event-scoped hook
- [GET /systems/{system}/events/{event}/hooks/{hook_id}](http-docs/http-webhooks-systems-system-events-event-hooks-hook_id-GET.md)
- [PATCH /systems/{system}/events/{event}/hooks/{hook_id}](http-docs/http-webhooks-systems-system-events-event-hooks-hook_id-PATCH.md)
- [DELETE /systems/{system}/events/{event}/hooks/{hook_id}](http-docs/http-webhooks-systems-system-events-event-hooks-hook_id-DELETE.md)

### Webhook Tokens API (HTTP Endpoints)

Endpoints for managing webhook secret tokens used for payload signature verification.

- [POST /tokens](http-docs/http-tokens-tokens-POST.md) — create a new token
- [PUT /tokens/me](http-docs/http-tokens-tokens-me-PUT.md) — update the current token
- [DELETE /tokens/me](http-docs/http-tokens-tokens-me-DELETE.md) — delete the current token
<!-- GENERATED:CONTENT_SUMMARY:END -->

## Source

Autodesk APS Webhooks docs:
- https://aps.autodesk.com/en/docs/webhooks/v1/tutorials/
- https://aps.autodesk.com/en/docs/webhooks/v1/reference/http/
