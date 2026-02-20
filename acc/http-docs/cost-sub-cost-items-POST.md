# v1/containers/{containerId}/cost-items/{costItemId}/sub-cost-items

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-sub-cost-items-POST/

---

# v1/containers/{containerId}/cost-items/{costItemId}/sub-cost-items

Creates a sub cost item within a specific cost item in a project. Sub cost items store detailed cost breakdowns and can be used for tracking and categorization.
For more information about cost and sub cost items, see the Help documentation .

## Resource Information

Method and URI POST https://developer.api.autodesk.com/cost/v1/containers/:containerId/cost-items/:costItemId/sub-cost-items Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json region string Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead. Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page. To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.

Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page.

To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

### Request

## URI Parameters

containerId string: UUID The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see GET projects . costItemId string: UUID The ID of the cost item to which the sub cost item belongs. To find the cost item ID, call GET cost-items .

### Request

## Body Structure

parentId string,null The unique ID of the parent sub cost item. Set this to null if there is no parent sub cost item.
To find the parent ID, call GET sub-cost-items . type enum:string The classification of the sub cost item that indicates its role in cost tracking and approval workflows. Possible values: estimated , proposed , submitted , approved , committed . Max length: 255 code * string A user-defined identifier for the sub cost item, used for categorization or identification.
If the sub cost item is created by copying from another model, for example, Contract SOV , it will inherit the code from the source model. Otherwise, it must be manually assigned.
To verify the code is unique, call GET sub-cost-items . Max length: 255 name string The name to give to the sub cost item. Max length: 1024 quantity number,string,null The planned number of units for the sub cost item. inputQuantity number,string,null The recorded input quantity, typically used in performance tracking. For example, in labor tracking, inputQuantity represents man-hours utilized. unitPrice number,string,null The price per unit of the sub cost item. unit string The unit of measurement for the sub cost item. This value is configured in the Unit of measure settings for the project. Common units include ea (Each), gal (Gallon), and various volume, length, and time measurements. Max length: 1024 value number,string,null The total value of the sub cost item, calculated as quantity * unitPrice . position number,null Determines the order in which the sub cost item appears relative to its sibling sub cost items in the UI. It is used for display purposes only. If a new sub cost item is assigned a position that already exists, the system shifts existing items downward to maintain order.

Max length: 255

Max length: 255

Max length: 1024

Max length: 1024

### Response

## HTTP Status Code Summary

201 Created The sub cost item was successfully created. 400 Bad Request The parameters are invalid. 401 Unauthorized The provided bearer token is invalid. 403 Forbidden Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The resource or endpoint cannot be found. 409 Conflict The request could not be completed due to a conflict with the current state of the resource. 429 Too Many Requests Rate limit exceeded. Retry your request after a few minutes. 500 Internal Server Error An unexpected error occurred on the server. 503 Service Unavailable Service unavailable.

### Response

## Body Structure (201)

id string: UUID The unique ID of the sub cost item. parentId string,null The unique ID of the parent sub cost item. A sub cost item has a parent Id when it is part of a hierarchical cost structure. Root sub cost items do not have a parent ID. type enum:string The classification of the sub cost item that indicates its role in cost tracking and approval workflows. Possible values: estimated , proposed , submitted , approved , committed . Max length: 255 costItemId string The ID of the cost item to which the sub cost item belongs. code string The identifier for the sub cost item. If copied from another model, for example, a Contract SOV , it inherits the code. Otherwise, it is manually assigned. Max length: 255 position number,null The position of the sub cost item relative to its sibling sub cost items. If a new sub cost item is assigned a position that already exists, the system shifts existing items downward to maintain order. name string The name of the sub cost item. Max length: 1024 quantity number,string,null The planned number of units allocated for the sub cost item. inputQuantity number,string,null The recorded input quantity, typically used in performance tracking. For example, in labor tracking, inputQuantity represents man-hours utilized. unitPrice number,string,null The price per individual unit of the sub cost item. unit string The unit of measurement for the sub cost item. This value is configured in the Unit of measure settings for the project. Common units include ea (Each), gal (Gallon), and various volume, length, and time measurements. Max length: 1024 value number,string,null The total value of the sub cost item, calculated as quantity * unitPrice . createdAt datetime: ISO 8601 The date and time that the item was created, in ISO 8601 format. updatedAt datetime: ISO 8601 The date and time that the item was last updated, in ISO 8601 format.

Max length: 255

Max length: 255

Max length: 1024

Max length: 1024

## Example

The sub cost item was successfully created.

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/cost-items/eb284d80-f026-11e7-98ee-cb31483cc0ac/sub-cost-items' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "parentId": null, "type": "estimated", "code": "0002", "name": "concrete flooring", "quantity": "1.0000", "inputQuantity": "1000.0000", "unitPrice": "1000.0000", "unit": "ea", "value": "1000.0000", "position": 1 }'
```

### Response

```
[ { "id" : "8f127780-96d6-11e8-81a8-cd51c63a9484" , "parentId" : null , "type" : "estimated" , "costItemId" : "eb284d80-f026-11e7-98ee-cb31483cc0ac" , "code" : "0002" , "position" : 1 , "name" : "concrete flooring" , "quantity" : "1.0000" , "inputQuantity" : "1000.0000" , "unitPrice" : "1000.0000" , "unit" : "ea" , "value" : "1000.0000" , "createdAt" : "2019-01-06T01:24:22.678Z" , "updatedAt" : "2019-09-05T01:00:12.989Z" } ]
```
