# category-status-step-sets/status-step-sets:batch-get

Source: https://aps.autodesk.com/en/docs/acc/reference/http/assets-category-status-step-sets-status-step-sets-batch-get-POST/

---

# category-status-step-sets/status-step-sets:batch-get

Returns status set assignments associated with a specified set of categories. It can return just explicit
status set assignments or both explicitly and inherited status set assignments.

An explicitly-assigned status set is assigned to a category so that the status set overrides the status set
that would otherwise be inherited from the categoryâs parent.

When this endpoint is set to return both explicitly-defined and inherited status set assignments, it returns a
status set assignment for each of the specified categories. If some of these categories have inherited status
sets, it means that those inherited status sets may appear more than once in the return, but will each show a
different associated category. An additional field inheritedFromCategoryId will be added to the assignment
record to indicate which category the status set assignment is inherited from.

When this endpoint is set to return only explicit status set assignments, it ignores any specified categories
that inherit their status set. Returned status set assignments appear once each and show their category
associations with the category where the status set was assigned. Any specified categories with inherited
status sets donât return a status set.

To understand the basics of status sets, inheritance, and the Assets settings that define them, see the Assets Field Guide .

## Resource Information

Method and URI POST https://developer.api.autodesk.com/construction/assets/v1/projects/{projectId}/category-status-step-sets/status-step-sets:batch-get Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json

### Request

## URI Parameters

projectId string The Autodesk Construction Cloud project ID. Must be a UUID or a project ID of the form âb.{UUID}â.

### Request

## Query String Parameters

includeInherited boolean Specifies whether or not to return status sets for categories that inherit their status set. If true , returns a
status set (inherited or not) for each specified category. If false , returns only explicitly-defined status sets
associated with the specified categories. Default is false .

### Request

## Body Structure

ids array: string A set of unique IDs of categories to return status set assignments for.

### Response

## HTTP Status Code Summary

200 OK Successfully returned the status sets for the specified category IDs. 400 Bad Request The request could not be understood by the server due to malformed syntax or missing request header 401 Unauthorized The request was not accepted because it lacked valid authentication credentials 403 Forbidden The request was not accepted because the client is authenticated, but is not authorized to access the target resource 404 Not Found The resource cannot be found 429 Too Many Requests The request was not accepted because the rate limit was exceeded due to too many requests being made. 500 Internal Server Error An unexpected error occurred on the server

### Response

## Body Structure (200)

results array: object Returned status set category assignments. categoryId string The ID of the category to which the status set is assigned. statusStepSetId string: UUID The ID of the status set assigned to the category. inheritedFromCategoryId string The ID of the category from which this status set was inherited - that is, the ancestor category
to which the inherited status set was explicitly assigned. This field is only present when this
endpoint is set to return inherited status sets, and then only for inherited status sets.

## Example

Successfully returned the status sets for the specified category IDs.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/assets/v1/projects/:projectId/category-status-step-sets/status-step-sets:batch-get' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "ids": [ "123" ] }'
```

### Response

```
{ "results" : [ { "categoryId" : "124" , "statusStepSetId" : "6eb35939-e5fb-453a-98ed-e2e11f326e73" , "inheritedFromCategoryId" : "123" } ] }
```
