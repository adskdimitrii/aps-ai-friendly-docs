# Creating a Webhook and Listening to Events

Source: https://aps.autodesk.com/en/docs/webhooks/tutorials/create-a-hook-cost-management/

---

# Creating a Webhook and Listening to Events

This walkthrough demonstrates how to create a Webhook to register callbacks for specified types of Autodesk Construction Cloud (ACC) and BIM 360 Cost Management events . The steps include finding the scope ID for the events, choosing the event type for the webhook to listen for, preparing to handle callbacks, and creating the webhook.

For more details about the Cost Management API, see the Cost Management Field Guide .

## Before You Begin

- Make sure that you have registered an app and successfully acquired an OAuth token .

- See the Authentication and Scopes section on the Data Management APIâs API Basics page for the appropriate token based on the data that youâre accessing.

- All requests to the Webhooks Service require the data:read scope.

- You need the data:create scope to create a webhook.

## Step 1 : Find the scope ID for events

A projectâs ID is used as the project level scope. Retrieve the project/container ID for your project as described in the Retrieve project id walkthrough.

### Field Guide

For more information about webhook scope, see the Webhooks Field Guide .

## Step 2 : Choose an event type to register the webhook on

The Webhooks service currently supports the events listed on the Cost Management Events page.

You can specify multiple event types by including wildcards in the event type name using the asterisk ( * ) character, which matches zero or more characters in the name. For example, specifying budget.*-1.0 will match budget.created-1.0 , budget.deleted-1.0 , and budget.updated-1.0 .

For more information about event types and wildcards, see Supported Events .

## Step 3 : Prepare to handle callbacks

A webhook requires a callback URL to which the event data can be sent. See Configuring Your Server to get started with a local server setup.

## Step 4 : Create a webhook

A webhook is created by making a POST request to webhooks/v1/systems/:system/events/:event/hooks . You can find additional details in the endpoint documentation .

### Hook Attribute

In some scenarios, certain data (such as projectId ) are not included in the event notification. You can define the webhook to include such custom information in the callback payload.

Provide the hookAttribute property with a JSON object that you want to include in the callback, such as the projectId or any other information from your app.

For more information, see the Webhooks Field Guide .

### Filter

You might want to filter the callbacks you receive based on the payload of the callback.

Provide the filter attribute in the endpoint request payload with a JSONPath expression that specifies the callback payload field values to filter on.

For more information, see Callback Filtering

### Example Input Values

Values used in this example are:

system autodesk.construction.cost event budget.created-1.0 (Wildcards can be used here, e.g. budget.* or * ) callback URL http://bf067e05.ngrok.io/callback scope key project (scope name for Cost Management events) scope value d6a37470-0539-40eb-89ff-9aeb8680066d (UUID of the project) hookAttribute { "projectId": "d6a37470-0539-40eb-89ff-9aeb8680066d" } Authorization token Bearer bNU4P0trbQKNSzxWksLPTzSbbmUz

### Request

```
curl -X 'POST' -v 'https://developer.api.autodesk.com/webhooks/v1/systems/autodesk.construction.cost/events/budget.created-1.0/hooks' -H 'Content-Type: application/json' -H 'authorization: Bearer bNU4P0trbQKNSzxWksLPTzSbbmUz' -d '{ "callbackUrl": "http://bf067e05.ngrok.io/callback", "scope": { "project": "d6a37470-0539-40eb-89ff-9aeb8680066d" }, "hookAttribute": { "projectId": "d6a37470-0539-40eb-89ff-9aeb8680066d" } }'
```

### Response

You should receive a successful response from the server with status of 201 . Additionally, the response includes a Location header. The Location information is required to delete a webhook.

Navigate to the Location URL to validate and obtain the properties of the newly-created webhook.

```
HTTP/1.1 201 Date: Thu, 14 Sep 2017 16 :45:05 GMT
Location: https://developer.api.autodesk.com/webhooks/v1/systems/autodesk.construction.cost/events/budget.created-1.0/hooks/0f60f6a0-996c-11e7-abf3-51d68cff984c
Content-Length: 0 Connection: keep-alive
```

Your configured callbackUrl should receive the notifications when a new budget item is added to project d6a37470-0539-40eb-89ff-9aeb8680066d .
