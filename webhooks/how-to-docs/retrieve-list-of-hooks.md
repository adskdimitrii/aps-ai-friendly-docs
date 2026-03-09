# Retrieve your Webhooks

Source: https://aps.autodesk.com/en/docs/webhooks/tutorials/retrieve-list-of-hooks/

---

# Retrieve your Webhooks

This walkthrough demonstrates how to retrieve your webhooks.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps)
- Successfully [acquire an OAuth token](../../oauth/how-to-docs/get-2-legged-token.md) with appropriate authentication scopes.

## [Retrieve your webhooks](#id1)

List of webhooks can be retrieved by sending a `GET` request to `webhooks/v1/systems/:system/events/:event/hooks`

Note: There are multiple ways to retrieve list of webhooks.

| Endpoint | Description |
| --- | --- |
| [GET systems/:system/events/:event/hooks/:hook_id](https://aps.autodesk.com/en/docs/webhooks/v1/reference/http/systems-system-events-event-hooks-hook_id-GET/) | Retrieves the details about a webhook for a specified event. |
| [GET systems/:system/events/:event/hooks](https://aps.autodesk.com/en/docs/webhooks/v1/reference/http/systems-system-events-event-hooks-GET/) | Retrieves a paginated list of all the webhooks for a specified event in a system. |
| [GET systems/:system/hooks](https://aps.autodesk.com/en/docs/webhooks/v1/reference/http/systems-system-hooks-GET/) | Retrieves a paginated list of all the webhooks of a specified system. |
| [GET hooks](https://aps.autodesk.com/en/docs/webhooks/v1/reference/http/hooks-GET/) | Retrieves a paginated list of all the webhooks. |

You can find additional details in [API Reference](https://aps.autodesk.com/en/docs/webhooks/v1/reference/http/systems-system-events-event-hooks-GET/) section.

## [Example](#example)

### Request

```
curl -v 'https://developer.api.autodesk.com/webhooks/v1/systems/data/events/dm.version.added/hooks?scopeName=folder&scopeValue=urn:adsk.wipprod:fs.folder:co.wT5lCWlXSKeo3razOfHJAw&pageState=BNNBEACAtgALYWRzay53aXBkZXYNZnMuZmlsZS5hZGRlZAZmb2xkZXIydXJuOmFkc2sud2lwcWE6ZnMuZm9sZGVyOmNvLlRSM253QUtoVFNDQ0x0azY0VE52Q2cydXJuOmFkc2sud2lwcWE6ZnMuZm9sZGVyOmNvLlRSM253QUtoVFNDQ0x0azY0VE52Q2ctaHR0cDovL2FwaS53ZWJob29raW5ib3guY29tL2kvM0l6eGlLZndmL2luL3gy8H____3wf____Twpc5_2RqlBtCsLMPJlT9kABA=='\
     -H 'Authorization: Bearer bNU4P0trbQKNSzxWksLPTzSbbmUz'

```

### Response

```
HTTP/1.1 200
Content-Type: application/json
Date: Fri, 14 Sep 2017 17:14:09 GMT
Content-Length: 662
Connection: keep-alive
{
  "links": {
    "next": "/systems/data/events/dm.version.added/hooks?pageState=AMMAEACAtgALYWRzay53aXBkZXYNZnMuZmlsZS5hZGRlZAZmb2xkZXIydXJuOmFkc2sud2lwcWE6ZnMuZm9sZGVyOmNvLlRSM253QUtoVFNDQ0x0azY0VE52Q2cydXJuOmFkc2sud2lwcWE6ZnMuZm9sZGVyOmNvLlRSM253QUtoVFNDQ0x0azY0VE52Q2ctaHR0cDovL2FwaS53ZWJob29raW5ib3guY29tL2kvM0l6eGlLZndmL2luL3gy8H____3wf____Twpc5_2RqlBtCsLMPJlT9kABA=="
  },
  "data": [{
    "hookId" : "0f60f6a0-996c-11e7-abf3-51d68cff984c",
    "tenant" : "urn:adsk.wipprod:fs.folder:co.wT5lCWlXSKeo3razOfHJAw",
    "callbackUrl" : "http://bf067e05.ngrok.io/callback",
    "createdBy" : "*********",
    "event" : "dm.version.added",
    "createdDate" : "2017-09-14T17:04:10.444+0000",
    "lastUpdatedDate" : "2020-09-14T17:04:10.444+0000",
    "system" : "data",
    "creatorType": "Application",
    "status" : "active",
    "autoReactivateHook": false,
    "scope" : {
      "folder" : "urn:adsk.wipprod:fs.folder:co.wT5lCWlXSKeo3razOfHJAw"
    },
    "urn" : "urn:adsk.webhooks:events.hook:0f60f6a0-996c-11e7-abf3-51d68cff984c",
    "__self__" : "/systems/data/events/dm.version.added/hooks/0f60f6a0-996c-11e7-abf3-51d68cff984c"
  }]
}

```

Show More
