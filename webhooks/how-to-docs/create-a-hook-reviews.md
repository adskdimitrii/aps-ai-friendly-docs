# Creating a Webhook and Listening to ACC Reviews Events

Source: https://aps.autodesk.com/en/docs/webhooks/tutorials/create-a-hook-reviews/

---

# Creating a Webhook and Listening to ACC Reviews Events

This walkthrough demonstrates how to create a Webhook to register callbacks for specified types of [Autodesk Construction Cloud (ACC) Reviews events](/en/docs/webhooks/v1/reference/events/reviews_events). The steps include finding the scope ID for the events, choosing the event type for the webhook to listen for, preparing to handle callbacks, and creating the webhook.

For more details about the Reviews API, see the [Reviews Field Guide](/en/docs/acc/v1/overview/field-guide/reviews).

## [Before You Begin](#before-you-begin)

- Make sure that you have [registered an app](/myapps) and successfully [acquired an OAuth token](/en/docs/oauth/v2/tutorials/create-app) .
- The Reviews Webhook supports only 3-legged OAuth tokens. See [Get a 3-legged OAuth token](/en/docs/oauth/v2/tutorials/get-3-legged-token) to acquire a 3-legged OAuth token with scopes.
- All requests to the Webhooks Service require the `data:read` scope.
- You need the `data:create` scope to create a webhook.
- Specify the `region` header to indicate the region in which the request is executed. The default value is `US`. You can also provide a specific region API value. For more details, see [Region](/en/docs/acc/v1/overview/acc-regions). The region parameter must remain consistent with the value used at creation time when listing, querying, or deleting webhooks.

## [Step 1: Find the Scope ID for Events](#step-1-find-the-scope-id-for-events)

The Webhooks service uses the project ID as the scope for ACC Reviews events. To find the project ID, see the [Retrieve Project ID](/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial.

For more information about webhook scopes, see the [Field Guide](/en/docs/webhooks/v1/developers_guide/field-guide/).

## [Step 2: Select an Event Type for Webhook Registration](#step-2-select-an-event-type-for-webhook-registration)

The Webhooks service currently supports the events listed on the [Reviews Events](/en/docs/webhooks/v1/reference/events/reviews_events) page.

You can specify multiple event types by including wildcards in the event type name using the asterisk (`*`) character, which matches zero or more characters in the name. For example, specifying `review.*-1.0` will match `review.created-1.0` and `review.closed-1.0`.

For more information about event types and wildcards, see [Supported Events](/en/docs/webhooks/v1/reference/events).

## [Step 3: Prepare to Manage Callbacks](#step-3-prepare-to-manage-callbacks)

A webhook requires a callback URL to which the event data can be sent. See [Configuring Your Server](/en/docs/webhooks/v1/tutorials/configuring-your-server) to get started with a local server setup.

## [Step 4: Create a Webhook](#step-4-create-a-webhook)

A webhook is created by making a `POST` request to `webhooks/v1/systems/:system/events/:event/hooks`. You can find additional details in the [endpoint documentation](/en/docs/webhooks/v1/reference/http/webhooks/systems-system-events-event-hooks-POST).

### Hook Attribute

In some scenarios, certain data (such as `projectId`) are not included in the event notification. You can define the webhook to include such custom information in the callback payload.

Provide the `hookAttribute` property with a JSON object that you want to include in the callback, such as the `projectId` or any other information from your app.

For more information, see the [Webhooks Field Guide](/en/docs/webhooks/v1/developers_guide/field-guide).

### Filter

You might want to filter the callbacks you receive based on the payload of the callback.

Provide the `filter` attribute in the endpoint request payload with a JSONPath expression that specifies the callback payload field values to filter on.

For more information, see [Callback Filtering](/en/docs/webhooks/v1/developers_guide/callback-filtering).

### Example Input Values

Values used in this example are:

| system | `autodesk.construction.reviews` |
| --- | --- |
| event | `review.created-1.0` (Wildcards can be used here, e.g. `review.*` or `*`) |
| callback URL | `http://bf067e05.ngrok.io/callback` |
| scope key | `project` (Scope name for Reviews events) |
| scope value | `d6a37470-0539-40eb-89ff-9aeb8680066d` (The ID of the project, in UUID format) |
| hookAttribute | `{ "projectId": "d6a37470-0539-40eb-89ff-9aeb8680066d" }` (The ID of the project, in UUID format) |
| Authorization token | `Bearer bNU4P0trbQKNSzxWksLPTzSbbmUz` |

### Request

```
curl -X 'POST'
     -v 'https://developer.api.autodesk.com/webhooks/v1/systems/autodesk.construction.reviews/events/review.created-1.0/hooks'
     -H 'Content-Type: application/json'
     -H 'authorization: Bearer bNU4P0trbQKNSzxWksLPTzSbbmUz'
     -H 'region: US'
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

You should receive a successful response from the server with status of `201`. Additionally, the response includes a `Location` header. The `Location` information is required to delete a webhook.

Navigate to the `Location` URL to validate and obtain the properties of the newly-created webhook.

```
HTTP/1.1 201
Date: Thu, 14 Sep 2017 16:45:05 GMT
Location: https://developer.api.autodesk.com/webhooks/v1/systems/autodesk.construction.reviews/events/review.created-1.0/hooks/0f60f6a0-996c-11e7-abf3-51d68cff984c
Content-Length: 0
Connection: keep-alive

```

Your configured `callbackUrl` should receive the notifications when a new review item is added to project `d6a37470-0539-40eb-89ff-9aeb8680066d`.

### Receive the Callback Events

After a review is created, the callback event is sent to the `callbackUrl` with the following payload:

```
{
  "version": "1.0",
  "resourceUrn": "a4a3613c-c9dd-4e59-9d38-7b5a9857db9d",
  "hook": {
      "hookId": "9872fd3e-e2d0-44f0-845e-44b4ec9a16e8",
      "tenant": "d6a37470-0539-40eb-89ff-9aeb8680066d",
      "callbackUrl": "http://bf067e05.ngrok.io/callback",
      "createdBy": "GTMMJRRXST63",
      "event": "review.created-1.0",
      "createdDate": "2024-09-05T06:02:40.925+00:00",
      "lastUpdatedDate": "2024-09-05T06:02:40.921+00:00",
      "system": "autodesk.construction.reviews",
      "creatorType": "O2User",
      "status": "active",
      "scope": {
          "project": "d6a37470-0539-40eb-89ff-9aeb8680066d"
      },
      "hookAttribute": {
          "projectId": "d6a37470-0539-40eb-89ff-9aeb8680066d"
      },
      "autoReactivateHook": true,
      "urn": "urn:adsk.webhooks:events.hook:9872fd3e-e2d0-44f0-845e-44b4ec9a16e8",
      "callbackWithEventPayloadOnly": false,
      "__self__": "/systems/autodesk.construction.reviews/events/review.created-1.0/hooks/9872fd3e-e2d0-44f0-845e-44b4ec9a16e8"
  },
  "payload": {
    "roundNum": 1,
    "sequenceId": "16",
    "status": "OPEN"
  }

```

Show More

}

### Receive Events Restrictions

The user who creates a webhook can only receive notifications for Reviews that they have permission to view within the project.
> - If the user is a project admin, they will receive all Review creation and closure events.
> - If the user is a project member:
> * If the user is listed in the Reviewer or Approver candidates, they will receive creation and closure events for those Reviews.
> * If the user is only listed in the Initiator candidates, they will receive creation and closure events only for the Reviews they initiated.
> * As a project member, the user will not receive events for Reviews that are unrelated to them.
