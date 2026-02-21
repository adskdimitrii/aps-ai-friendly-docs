# Creating a Webhook and Listening to BuildingConnected Events

Source: https://aps.autodesk.com/en/docs/webhooks/tutorials/create-a-hook-buildingconnected/

---

# Creating a Webhook and Listening to BuildingConnected Events

This walkthrough demonstrates how to create a webhook to register callbacks for BuildingConnected events . The steps include finding the scope ID for the events, choosing the event type for the webhook to listen for, preparing to handle callbacks, and creating the webhook.

For more details about the BuildingConnected API, see the BuildingConnected Field Guide .

## Before You Begin

- Create a BuildingConnecteed account.

- Link the BuildingConnected user to an Autodesk ID. See How to connect your Autodesk ID to BuildingConnected for details.

- Subscribe to the relevant BuildingConnected product for each event:

- For Bid events subcribe to BuildingConnected Pro.

- For Opportunity events subcribe to Bid Board Pro.

- Register an app , and select the BuildingConnected API.

- Acquire a 3-legged OAuth token with data:read and data:create authentication scopes. For information about authentication scopes, see the Scopes section in the Data Management API Basics page.

## Step 1 : Find the Scope ID for BuildingConnected Events

The Webhooks service uses the company ID as the scope for BuildingConnected events. To retrieve the company ID ( results.companyId ), call GET users/me </en/docs/buildingconnected/v2/reference/http/buildingconnected-users-me-GET/>`_.

For more information about webhook scopes, see the Field Guide .

## Step 2 : Select an Event Type for Webhook Registration

The Webhooks service currently supports the events listed on the BuildingConnected Events page.

You can specify multiple event types by including wildcards in the event type name. This is done using the asterisk (*) character, which represents zero or more characters in the name. For example, if you specify opportunity.comment.*-1.0 , it will correspond to opportunity.comment.created-1.0 , opportunity.comment.deleted-1.0 , and opportunity.comment.updated-1.0 .

For more information about event types and wildcards, see Supported Events .

## Step 3 : Prepare to Manage Callbacks

A webhook requires a callback URL to which it will send the event data. To get started with setting up a local server, see Configuring Your Server .

## Step 4 : Create a Webhook

Create a webhook by calling POST events/:event/hooks .

### Hook Attribute

In some situations, specific data (such as salesforceId ) might not be included in the event notification. To include such custom information in the callback payload, you can configure the webhook accordingly.

Supply the hookAttribute property with a JSON object that you want to include in the callback, such as the salesforceId , or any other details from your app.

For more information, see the Field Guide .

### Filter

You might want to filter the callbacks you receive based on the payload of the callback.

Provide the filter attribute in the endpoint request payload with a JSONPath expression that specifies the callback payload field values you want to filter on.

For more information, see Callback Filtering .

### Example Input Values

The input values used in this example are as follows:

system autodesk.construction.bc event opportunity.comment.created (You can use wildcards here, such as opportunity.comment.* or * ) callback URL http://bf067e05.ngrok.io/callback scope key project (This is the scope name for BuildingConnected events) scope value d6a37470-0539-40eb-89ff-9aeb8680066d (This is the UUID of the project) hookAttribute { "projectId": "d6a37470-0539-40eb-89ff-9aeb8680066d" } Authorization token Bearer bNU4P0trbQKNSzxWksLPTzSbbmUz

### Request

```
curl -X 'POST' -v 'https://developer.api.autodesk.com/webhooks/v1/systems/autodesk.construction.bc/events/opportunity.comment.created/hooks' -H 'Content-Type: application/json' -H 'authorization: Bearer bNU4P0trbQKNSzxWksLPTzSbbmUz' -d '{ "callbackUrl": "http://bf067e05.ngrok.io/callback", "scope": { "companyId": "594206015caedd954831e5b8" }, "hookAttribute": { "projectId": "d6a37470-0539-40eb-89ff-9aeb8680066d" } }'
```

### Response

Upon completion, you should receive a 201 status response from the server. The response will also include a Location header, which you need to use if you plan to delete the webhook in the future.

To verify and view the properties of the newly-created webhook, navigate to the URL provided in the Location field.

```
HTTP/1.1 201 Date: Thu, 14 Sep 2017 16 :45:05 GMT
Location: https://developer.api.autodesk.com/webhooks/v1/systems/autodesk.construction.bc/events/opportunity.comment.created/hooks/0f60f6a0-996c-11e7-abf3-51d68cff984c
Content-Length: 0 Connection: keep-alive
```

Your configured callbackUrl should receive the notifications when a new comment is added to an opportunity for your company 594206015caedd954831e5b8 .
