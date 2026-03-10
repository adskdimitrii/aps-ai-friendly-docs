# Creating a Webhook and Listening to Events

Source: https://aps.autodesk.com/en/docs/webhooks/tutorials/create-a-hook-data-management/

---

# Creating a Webhook and Listening to Events

This walkthrough explains how to create a Webhook to register callbacks for [Data Management](https://aps.autodesk.com/en/docs/data/v2/overview/) events.

## [Before You Begin](#before-you-begin)

- Make sure that you have [registered an app](https://aps.autodesk.com/myapps) and successfully [acquired an OAuth token](https://aps.autodesk.com/en/docs/oauth/v2/tutorials/) .
- See the Authentication and Scopes section in the [API Basics](https://aps.autodesk.com/en/docs/data/v2/overview/basics/) for the appropriate token based on the data you are accessing.
- All requests to the Webhooks Service require the `data:read` scope.
- You need `data:create` scope to create a hook.

## [Step 1 : Find the Scope ID for events](#step-1-find-the-scope-id-for-events)

The URNs for a particular *Folder* can be easily accessed using [Data Management](https://aps.autodesk.com/en/docs/data/v2/overview/) GET APIs. Please note that only folder is supported for webhooks, you can use root folder URN to create hook on the project level.

Example: [GET projects/:project_id/folders/:folder_id](../../data/http-docs/http-projects-project_id-folders-folder_id-GET.md)



### Field Guide

For more information about scope and webhook take a look at our [Field Guide](https://aps.autodesk.com/en/docs/webhooks/v1/overview/field-guide/).

## [Step 2 : Choose event type to register the Webhook on](#step-2-choose-event-type-to-register-the-webhook-on)

Webhooks service currently exposes the following types of Data Management events. Wildcards can also be specified by using the character “*” to represent the matching
placeholder to substitute zero or more characters in the event type.

See [Supported Events](https://aps.autodesk.com/en/docs/webhooks/v1/reference/events/) for more information about event types and wildcards.

## [Step 3 : Preparing to handle Callbacks](#step-3-preparing-to-handle-callbacks)

A webhook requires a callback URL where the event data is sent. See [Configuring Your Server](configuring-your-server.md) to get you started with a local server setup.

## [Step 4 : Create a Webhook](#step-4-create-a-webhook)

A webhook is created by making a `POST` request to `webhooks/v1/systems/:system/events/:event/hooks`.
You can find additional details in the [Reference Guide](https://aps.autodesk.com/en/docs/webhooks/v1/reference/http/systems-system-events-event-hooks-POST/).

### Example

Values used in this example are:

| system | `data` |
| --- | --- |
| event | `dm.version.added` wildcards can be used here like so: `dm.*` |
| callback URL | `http://bf067e05.ngrok.io/callback` |
| scope key | `folder` scope name for Data Management events |
| scope value | `urn:adsk.wipprod:fs.folder:co.wT5lCWlXSKeo3razOfHJAw` which is a Folder URN |
| hookAttribute | `{ "projectId": "a.cGVyc29uYWwGcGUy0WN1NTg41z1wNTcwOD1yNDA4NDgyNg" }` which is Project Id. |
| filter | `$[?(@.ext=='txt')]` which is the extension of the item. |
| Authorization token | `Bearer bNU4P0trbQKNSzxWksLPTzSbbmUz` |

### Hook Attribute

In some scenarios some data will not be available like projectId when receiving the event but you want to have it.
Use the hookAttribute property to include custom information, such as the projectId or any other information from your app.
When registering the hook, add a hookAttribute key with JSON object you want to have available on your callback payload.

For more information please take a look at [Field Guide](https://aps.autodesk.com/en/docs/webhooks/v1/overview/field-guide/)

### Filter

In some scenarios, you might want to filter the callbacks you receive based on the payload of the callback.
When registering the hook, add a filter key with a JsonPath expression string you want the events to be filtered with.

For more information please take a look at [Callback Filtering](https://aps.autodesk.com/en/docs/webhooks/v1/overview/callback-filtering/)

### Request

```
curl -X 'POST'
     -v 'https://developer.api.autodesk.com/webhooks/v1/systems/data/events/dm.version.added/hooks'
     -H 'Content-Type: application/json'
     -H 'authorization: Bearer bNU4P0trbQKNSzxWksLPTzSbbmUz'
     -d '{
            "callbackUrl": "http://bf067e05.ngrok.io/callback",
            "scope": {
                 "folder": "urn:adsk.wipprod:fs.folder:co.wT5lCWlXSKeo3razOfHJAw"
            },
            "hookAttribute": {
              "projectId": "a.cGVyc29uYWwGcGUy0WN1NTg41z1wNTcwOD1yNDA4NDgyNg"
            },
            "filter": "$[?(@.ext=='txt')]"
      }'

```

Show More

### Response

You should receive a successful response from the server with status of `201`.
Additionally, you should receive `Location` header in the response. `Location` information is required to delete a webhook. Navigate to the `Location` URL to validate and obtain the properties of the newly-created webhook.

```
HTTP/1.1 201
Date: Thu, 14 Sep 2017 16:45:05 GMT
Location: https://developer.api.autodesk.com/webhooks/v1/systems/data/events/dm.version.added/hooks/0f60f6a0-996c-11e7-abf3-51d68cff984c
Content-Length: 0
Connection: keep-alive

```

Your configured `callbackUrl` should receive the notifications when a file is added to the Folder `urn:adsk.wipprod:fs.folder:co.wT5lCWlXSKeo3razOfHJAw`.
