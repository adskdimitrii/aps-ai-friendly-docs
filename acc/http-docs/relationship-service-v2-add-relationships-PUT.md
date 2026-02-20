# containers/:containerId/relationships

Source: https://aps.autodesk.com/en/docs/acc/reference/http/relationship-service-v2-add-relationships-PUT/

---

# containers/:containerId/relationships

Creates a relationship between two entities (for example, asset and document). Relationships are stored in the project container, and are retrievable via the relationships search endpoints.

Note that not all entities may be compatible. To learn how to verify the compatibility of two entities, see the Create a Relationship tutorial .

Note that in order to create a relationship between two entities, the entities must already exist, and you must have permission to access both entities in the proposed relationship.

Note that one entity may be related to a batch of up to 20 entities within a single API call.

## Resource Information

Method and URI PUT https://developer.api.autodesk.com/bim360/relationship/v2/containers/:containerId/relationships Authentication Context user context required Required OAuth Scopes data:create , data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json x-ads-region enum: string The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

Possible values: US , EMEA . For the full list of supported regions, see the Regions page.

### Request

## URI Parameters

containerId string: UUID The project ID.

### Request

## Body Structure

id string: UUID The UUID that uniquely identifies the relationship. If no id is supplied, the system automatically allocates one. entities * array: object The entities to be contained in the relationship. Min items: 2 Max items: 2 domain * string The domain to which the entity belongs. To learn more about domains and entities, see the Relationship Service Field Guide . Max length: 128 type * string The type of entity. Max length: 128 id * string The unique identifier of the entity. Max length: 512

Min items: 2 Max items: 2

To learn more about domains and entities, see the Relationship Service Field Guide .

Max length: 128

Max length: 128

Max length: 512

### Response

## HTTP Status Code Summary

200 OK Success 400 Bad Request The parameters of the requested operation are invalid. 401 Unauthorized The provided bearer token is not valid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The requested resource could not be found. 409 Conflict Indicates that the request could not be carried out because of a conflict on the server. 415 Unsupported Media Type The Content-Type header must be application/json . 429 Too Many Requests Rate limit exceeded; wait some time before retrying. The Retry-After header might provide the amount of the time to wait. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

id string: UUID The UUID that uniquely identifies the relationship. createdOn datetime: ISO 8601 The date and time the relationship was created. isReadOnly boolean true if this relationship is read only for the current caller. false if this relationship is not read only for the current caller. isService boolean true if this relationship was created by a service. false if this relationship was not created by a service. isDeleted boolean true if this relationship is deleted. false if this relationship is not deleted. deletedOn datetime: ISO 8601 The date and time the relationship was deleted. entities array: object The entities contained in the relationship. Min items: 2 Max items: 2 createdOn datetime: ISO 8601 The date and time the entity was created. domain string The domain to which the entity belongs. To learn more about domains and entities, see the Relationship Service Field Guide . Max length: 128 type string The type of entity. Max length: 128 id string The unique identifier of the entity. Max length: 512

false if this relationship is not read only for the current caller.

false if this relationship was not created by a service.

false if this relationship is not deleted.

Min items: 2 Max items: 2

To learn more about domains and entities, see the Relationship Service Field Guide .

Max length: 128

Max length: 128

Max length: 512

### Response

## Body Structure (400)

type string The error code. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. errors array: object A set of specific validation errors that need to be fixed. field string The field that failed validation. title string A short title for the error. detail string A more detailed, human readable description of the error, assuming that this message is not localized and is therefore EN-US. UI consumers can use the error.type value to provide a localized version of this error for presentation. type string The error code.

### Response

## Body Structure (409)

success array: object Successfully created relationships. id string: UUID The UUID that uniquely identifies the relationship. createdOn datetime: ISO 8601 The date and time the relationship was created. isReadOnly boolean true if this relationship is read only for the current caller. false if this relationship is not read only for the current caller. isService boolean true if this relationship was created by a service. false if this relationship was not created by a service. isDeleted boolean true if this relationship is deleted. false if this relationship is not deleted. deletedOn datetime: ISO 8601 The date and time the relationship was deleted. entities array: object The entities contained in the relationship. Min items: 2 Max items: 2 createdOn datetime: ISO 8601 The date and time the entity was created. domain string The domain to which the entity belongs. To learn more about domains and entities, see the Relationship Service Field Guide . Max length: 128 type string The type of entity. Max length: 128 id string The unique identifier of the entity. Max length: 512 conflict array: object Conflicting relationships. A conflict between IDs of an existing relationship and a proposed relationship, or due to allocating an array of entity items two different IDs. id string: UUID The UUID of the conflict. actual object A set of related domain entities. id string: UUID The UUID that uniquely identifies the relationship. createdOn datetime: ISO 8601 The date and time the relationship was created. isReadOnly boolean true if this relationship is read only for the current caller. false if this relationship is not read only for the current caller. isService boolean true if this relationship was created by a service. false if this relationship was not created by a service. isDeleted boolean true if this relationship is deleted. false if this relationship is not deleted. deletedOn datetime: ISO 8601 The date and time the relationship was deleted. entities array: object The entities contained in the relationship. Min items: 2 Max items: 2 createdOn datetime: ISO 8601 The date and time the entity was created. domain string The domain to which the entity belongs. To learn more about domains and entities, see the Relationship Service Field Guide . Max length: 128 type string The type of entity. Max length: 128 id string The unique identifier of the entity. Max length: 512

false if this relationship is not read only for the current caller.

false if this relationship was not created by a service.

false if this relationship is not deleted.

Min items: 2 Max items: 2

To learn more about domains and entities, see the Relationship Service Field Guide .

Max length: 128

Max length: 128

Max length: 512

A conflict between IDs of an existing relationship and a proposed relationship, or due to allocating an array of entity items two different IDs.

false if this relationship is not read only for the current caller.

false if this relationship was not created by a service.

false if this relationship is not deleted.

Min items: 2 Max items: 2

To learn more about domains and entities, see the Relationship Service Field Guide .

Max length: 128

Max length: 128

Max length: 512

## Example

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/fbd6cb57-7d0e-4961-8c2c-69646514ef44/relationships' \ -X PUT \ -H 'Authorization: Bearer <token>' \ -H 'Content-Type: application/json' \ -d '[ { "entities": [ { "domain": "autodesk-bim360-asset", "type": "asset", "id": "2b95ba7a-3df5-4e99-a693-9c7cc15ee8c0", "createdOn": "2021-07-29T11:39:12+01:00" }, { "domain": "autodesk-bim360-documentmanagement", "type": "documentlineage", "id": "urn:adsk.wipprod:dm.lineage:hC6k4hndRWaeIVhIjvHu8w", "createdOn": "2021-07-29T13:39:12+01:00" } ] } ]'
```

### Response (200)

```
[ { "id" : "74b70bb8-8802-a1fd-f201-890375a60c8f" , "createdOn" : "2015-10-21T16:32:22Z" , "isReadOnly" : true , "isService" : false , "isDeleted" : false , "entities" : [ { "domain" : "autodesk-bim360-asset" , "type" : "asset" , "id" : "2b95ba7a-3df5-4e99-a693-9c7cc15ee8c0" , "createdOn" : "2021-07-29T11:39:12+01:00" }, { "domain" : "autodesk-bim360-documentmanagement" , "type" : "documentlineage" , "id" : "urn:adsk.wipprod:dm.lineage:hC6k4hndRWaeIVhIjvHu8w" , "createdOn" : "2021-07-29T13:39:12+01:00" } ] } ]
```

### Response (400)

```
{ "type" : "BadInput" , "title" : "One or more input values in the request were bad" , "detail" : "The following parameters are invalid: containerId" , "errors" : [ { "field" : "containerId" , "title" : "Invalid parameter" , "detail" : "The value 'testing' is not valid." , "type" : "BadInput" } ] }
```

### Response (409)

```
{ "success" : [ { "id" : "74b70bb8-8802-a1fd-f201-890375a60c8f" , "createdOn" : "2015-10-21T16:32:22Z" , "isReadOnly" : true , "isService" : false , "isDeleted" : false , "entities" : [ { "domain" : "autodesk-bim360-asset" , "type" : "asset" , "id" : "2b95ba7a-3df5-4e99-a693-9c7cc15ee8c0" , "createdOn" : "2021-07-29T11:39:12+01:00" }, { "domain" : "autodesk-bim360-documentmanagement" , "type" : "documentlineage" , "id" : "urn:adsk.wipprod:dm.lineage:hC6k4hndRWaeIVhIjvHu8w" , "createdOn" : "2021-07-29T13:39:12+01:00" } ] } ], "conflict" : [ { "id" : "74b70bb8-8802-a1fd-f201-890375a60c8f" , "actual" : { "id" : "74b70bb8-8802-a1fd-f201-890375a60c8f" , "createdOn" : "2015-10-21T16:32:22Z" , "isReadOnly" : true , "isService" : false , "isDeleted" : false , "entities" : [ { "domain" : "autodesk-bim360-asset" , "type" : "asset" , "id" : "2b95ba7a-3df5-4e99-a693-9c7cc15ee8c0" , "createdOn" : "2021-07-29T11:39:12+01:00" }, { "domain" : "autodesk-bim360-documentmanagement" , "type" : "documentlineage" , "id" : "urn:adsk.wipprod:dm.lineage:hC6k4hndRWaeIVhIjvHu8w" , "createdOn" : "2021-07-29T13:39:12+01:00" } ] } } ] }
```
