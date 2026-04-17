# Creating a Webhook and Listening to Forma Issue Events

Source: https://aps.autodesk.com/en/docs/webhooks/tutorials/create-a-hook-issues/

---

# Creating a Webhook and Listening to Forma Issue Events

This walkthrough demonstrates how to create a webhook to register callbacks for [Forma Issue events](https://aps.autodesk.com/en/docs/webhooks/v1/reference/events/issues_events/). The steps include finding the scope ID for the events, choosing the event type for the webhook to listen for, preparing to handle callbacks, and creating the webhook.

For more details about the Forma Issues API, see the [Issues API Field Guide](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/issues/).

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps) and select the Forma Issues API.
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:read` and `data:create` scopes. These are required to access the Webhooks API and to create a webhook. For more information about scopes, see the [Scopes section](../../oauth/developers-guide-docs/scopes.md) in the Authentication API.
- Only users with **Project Admin** permissions can successfully create webhooks for Forma Issues.

## [Step 1 : Find the Scope ID for Events](#step-1-find-the-scope-id-for-events)

The Webhooks service uses the project ID as the scope for Forma Issue events. To find the project ID, see the [`Retrieve Project ID /en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/>`_](#id2) tutorial.

For more information about webhook scopes, see the [Field Guide](https://aps.autodesk.com/en/docs/webhooks/v1/developers_guide/field-guide/).

## [Step 2 : Select an Event Type for Webhook Registration](#step-2-select-an-event-type-for-webhook-registration)

The Webhooks service currently supports the events listed on the [Forma Issue Events](https://aps.autodesk.com/en/docs/webhooks/v1/reference/events/issues_events/) page.

You can specify multiple event types by including wildcards in the event type name using the asterisk (`*`) character, which matches zero or more characters in the name. For example:

- `issue.*` matches all issue-related events
- `*` matches all events in the system

For more information about event types and wildcards, see [Supported Events](https://aps.autodesk.com/en/docs/webhooks/v1/reference/events/).

## [Step 3 : Prepare to Manage Callbacks](#step-3-prepare-to-manage-callbacks)

A webhook requires a callback URL to which it will send the event data. To get started with setting up a local server, see [Configuring Your Server](configuring-your-server.md).

## [Step 4 : Create a Webhook](#step-4-create-a-webhook)

Create a webhook by calling [POST events/:event/hooks](https://aps.autodesk.com/en/docs/webhooks/v1/reference/http/systems-system-events-event-hooks-POST/).

### Hook Attribute

In some situations, specific data (such as the `projectId`) might not be included in the event notification. To include such custom information in the callback payload, you can configure the webhook accordingly.

Supply the `hookAttribute` property with a JSON object that you want to include in the callback, such as the `projectId` or any other details from your app.

For more information, see the [Webhooks Field Guide](https://aps.autodesk.com/en/docs/webhooks/v1/developers_guide/field-guide/).

### Filter

You might want to filter the callbacks you receive based on the payload of the callback.

Provide the `filter` attribute in the endpoint request payload with a JSONPath expression that specifies the callback payload field values you want to filter on.

For more information, see [Callback Filtering](https://aps.autodesk.com/en/docs/webhooks/v1/developers_guide/callback-filtering/).

### Example Input Values

The input values used in this example are as follows:

### Request

```
curl -X 'POST'
     -v 'https://developer.api.autodesk.com/webhooks/v1/systems/autodesk.construction.issues/events/issue.created-1.0/hooks'
     -H 'Content-Type: application/json'
     -H 'authorization: Bearer bNU4P0trbQKNSzxWksLPTzSbbmUz'
     -d '{
           "callbackUrl": "http://bf067e05.ngrok.io/callback",
           "scope": {
             "project": "d6a37470-0539-40eb-89ff-9aeb8680066d"
           },
           "hookAttribute": {
             "projectId": "d6a37470-0539-40eb-89ff-9aeb8680066d"
           }
         }'

```

Show More

### Response

Upon completion, you should receive a `201` status response from the server. The response will also include a `Location` header, which you need to use if you plan to delete the webhook in the future.

To verify and view the properties of the newly-created webhook, navigate to the URL provided in the `Location` field.

```
HTTP/1.1 201
Date: Sun, 20 Apr 2025 16:45:05 GMT
Location: https://developer.api.autodesk.com/webhooks/v1/systems/autodesk.construction.issues/events/issue.created-1.0/hooks/0f60f6a0-996c-11e7-abf3-51d68cff984c
Content-Length: 0
Connection: keep-alive

```

Note that creating a webhook for Forma Issues requires Project Admin permissions for the target project.

Your configured `callbackUrl` should receive the notifications when a new issue is created in the project `d6a37470-0539-40eb-89ff-9aeb8680066d`.
