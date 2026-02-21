# Delete a Webhook

Source: https://aps.autodesk.com/en/docs/webhooks/tutorials/delete-a-hook/

---

# Delete a Webhook

This walkthrough demonstrates how to delete a webhook.

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps)
- Successfully [acquire an OAuth token](/en/docs/oauth/v2/tutorials/get-2-legged-token/) with appropriate authentication scopes.

## [Step 1 : Obtain the webhook ID](#step-1-obtain-the-webhook-id)

You must first obtain `hookId` or `Location` of the webhook that needs to be deleted. Note that `Location` URL contains webhook ID.

There are multiple ways to find `hookId` or `Location` URL of webhook:
> - When you [create a webhook](/en/docs/webhooks/v1/tutorials/create-a-hook-data-management), you receive `Location` URL in Header of HTTP response.
> - [List of your Webhooks](/en/docs/webhooks/v1/tutorials/retrieve-list-of-hooks) returns `Location` in `__self__` attribute of response-body. `hookID` attribute in response-body represents webhook ID.

## [Step 2 : Delete the webhook](#step-2-delete-the-webhook)

You can delete your webhooks by sending a `DELETE` request to `webhooks/v1/systems/:system/events/:event/hooks/:hook_id`.

You can find additional details in the [Reference Guide](/en/docs/webhooks/v1/reference/http/systems-system-events-event-hooks-hook_id-DELETE).

## [Example](#example)

### Request

```
curl -X DELETE\
     -v 'https://developer.api.autodesk.com/webhooks/v1/systems/data/events/dm.version.added/hooks/0f60f6a0-996c-11e7-abf3-51d68cff984c'\
     -H 'Authorization: Bearer bNU4P0trbQKNSzxWksLPTzSbbmUz'

```

### Response

```
HTTP/1.1 204
Date: Fri, 15 Sep 2017 16:26:40 GMT
Content-Length: 0
Connection: keep-alive

```

You should receive a delete successful response from the server with status of `204`.
