# APS Webhooks Friendly Docs

Lightweight, local Markdown mirror of Autodesk APS Webhooks documentation.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

The Webhooks documentation covers creating, managing, and consuming webhook notifications across various APS services. It includes 22 files spanning API endpoints and practical how-to guides.

### Webhook Management API (12 files)

Core REST API for managing webhook subscriptions. Endpoints cover the full lifecycle of hooks — creating, listing, updating, and deleting — scoped by system and event type.

- **Create hooks:** [POST hook by system/event](http-docs/http-webhooks-systems-system-events-event-hooks-POST.md), [POST hook by system](http-docs/http-webhooks-systems-system-hooks-POST.md)
- **List hooks:** [GET all app hooks](http-docs/http-webhooks-app-hooks-GET.md), [GET all hooks](http-docs/http-webhooks-hooks-GET.md), [GET hooks by system](http-docs/http-webhooks-systems-system-hooks-GET.md), [GET hooks by system/event](http-docs/http-webhooks-systems-system-events-event-hooks-GET.md)
- **Single hook operations:** [GET hook by ID](http-docs/http-webhooks-systems-system-events-event-hooks-hook_id-GET.md), [PATCH hook](http-docs/http-webhooks-systems-system-events-event-hooks-hook_id-PATCH.md), [DELETE hook](http-docs/http-webhooks-systems-system-events-event-hooks-hook_id-DELETE.md)

### Webhook Tokens API (3 files)

Manage authentication tokens used for webhook callback verification.

- [POST create token](http-docs/http-tokens-tokens-POST.md)
- [PUT update token](http-docs/http-tokens-tokens-me-PUT.md)
- [DELETE token](http-docs/http-tokens-tokens-me-DELETE.md)

### Creating Hooks by Service (6 files)

Step-by-step guides for setting up webhooks for specific APS services:

- [Data Management](how-to-docs/create-a-hook-data-management.md) — file/folder events in BIM 360 and ACC
- [Model Derivative](how-to-docs/create-a-hook-model-derivative.md) — translation job events
- [Cost Management](how-to-docs/create-a-hook-cost-management.md) — cost-related events
- [Issues](how-to-docs/create-a-hook-issues.md) — issue creation/update events
- [Reviews](how-to-docs/create-a-hook-reviews.md) — review workflow events
- [BuildingConnected](how-to-docs/create-a-hook-buildingconnected.md) — BuildingConnected events

### Hook Lifecycle & Security (4 files)

Guides for managing hooks and securing webhook payloads:

- [Configure your server](how-to-docs/configuring-your-server.md) — setting up a callback endpoint
- [Verify payload signature](how-to-docs/how-to-verify-payload-signature.md) — validating webhook authenticity
- [Retrieve list of hooks](how-to-docs/retrieve-list-of-hooks.md) — querying existing subscriptions
- [Delete a hook](how-to-docs/delete-a-hook.md) — removing webhook subscriptions
<!-- GENERATED:CONTENT_SUMMARY:END -->

## Source

Autodesk APS Webhooks docs:
- https://aps.autodesk.com/en/docs/webhooks/v1/tutorials/
- https://aps.autodesk.com/en/docs/webhooks/v1/reference/http/
