# Creating a Webhook and Listening to Events

Source: https://aps.autodesk.com/en/docs/webhooks/tutorials/create-a-hook-model-derivative/

---

# Creating a Webhook and Listening to Events

This walkthrough explains how to create a Webhook to register callbacks for [Model Derivative](https://aps.autodesk.com/en/docs/model-derivative/v2/overview/) events.

## [Before You Begin](#before-you-begin)

- Make sure that you have [registered an app](https://aps.autodesk.com/myapps) and successfully [acquired an OAuth token](https://aps.autodesk.com/en/docs/oauth/v2/tutorials/) .
- See the Authentication and Scopes section in the [API Basics](https://aps.autodesk.com/en/docs/data/v2/overview/basics/) for the appropriate token based on the data you are accessing.
- All requests to the Webhooks Service require the `data:read` scope.
- You need `data:create` scope to create a hook.

## [Step 1 : Deciding the Scope ID for events](#step-1-deciding-the-scope-id-for-events)

Webhooks service uses the workflow ID of a set of jobs as the scope for Model Derivative events. The workflow ID of the set of jobs is designated by you to indicate that all of the jobs belong to the same workflow.

### Field Guide

For more information about scope and webhook take a look at our [Field Guide](https://aps.autodesk.com/en/docs/webhooks/v1/overview/field-guide/).

## [Step 2 : Choose event type to register the Webhook on](#step-2-choose-event-type-to-register-the-webhook-on)

Webhooks service currently exposes the following types of Model Derivative events. Wildcards can also be specified by using the character “*” to represent the matching
placeholder to substitute zero or more characters in the event type.

See [Supported Events](https://aps.autodesk.com/en/docs/webhooks/v1/reference/events/) for more information about event types and wildcards.

## [Step 3 : Preparing to handle Callbacks](#step-3-preparing-to-handle-callbacks)

A webhook requires a callback URL where the event data is sent. See [Configuring Your Server](configuring-your-server.md) to get you started with a local server setup.

## [Step 4 : Create a Webhook](#step-4-create-a-webhook)

A webhook is created by making a `POST` request to `webhooks/v1/systems/:system/events/:event/hooks`.
You can find additional details in the [Reference Guide](https://aps.autodesk.com/en/docs/webhooks/v1/reference/http/systems-system-events-event-hooks-POST/).

### Example

Values used in this example are:

| system | `derivative` |
| --- | --- |
| event | `extraction.finished` wildcards can be used here like so: `extraction.*` |
| callback URL | `http://bf067e05.ngrok.io/callback` |
| scope key | `workflow` |
| scope value | `my-workflow-id` |
| Authorization token | `Bearer bNU4P0trbQKNSzxWksLPTzSbbmUz` |

### Request

```
curl -X 'POST'
     -v 'https://developer.api.autodesk.com/webhooks/v1/systems/derivative/events/extraction.finished/hooks'
     -H 'Content-Type: application/json'
     -H 'authorization: Bearer bNU4P0trbQKNSzxWksLPTzSbbmUz'
     -d '{
            "callbackUrl": "http://bf067e05.ngrok.io/callback",
            "scope": {
              "workflow": "my-workflow-id"
            }
      }'

```

Show More

### Response

You should receive a successful response from the server with status of `201`.
Additionally, you should receive `Location` header in the response. `Location` information is required to delete a webhook. Navigate to the `Location` URL to validate and obtain the properties of the newly-created webhook.

```
HTTP/1.1 201
Date: Thu, 14 Sep 2017 16:45:05 GMT
Location: https://developer.api.autodesk.com/webhooks/v1/systems/derivative/events/extraction.finished/hooks/0f60f6a0-996c-11e7-abf3-51d68cff984c
Content-Length: 0
Connection: keep-alive

```

Your configured `callbackUrl` should receive the notifications when a job is finished for the workflow `my-workflow-id`.

## [Step 5 : Posting a job](#step-5-posting-a-job)

Now you can call MD POST job endpoint to submit a job and specify a workflow id.
You will receive a notification whenever a job with the specified workflow id is completed.

```
curl -X 'POST'
     -v 'https://developer.api.autodesk.com/modelderivative/v2/designdata/job'
     -H 'Content-Type: application/json'
     -H 'authorization: Bearer bNU4P0trbQKNSzxWksLPTzSbbmUz'
     -d '{
            "input": {
              "urn": "dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6d2htZHRlc3RzdGcvQ2FzZUlubmVyLmlwdA"
            },
            "output": {
              "formats": [{
                "type": "obj"
              }]
            },
            "misc": {
              "workflow": "my-workflow-id"
            }
         }'

```

Show More

For more information please take a look at [POST job](../../model-derivative/http-docs/http-job-POST.md)
