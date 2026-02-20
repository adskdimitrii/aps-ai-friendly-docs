# v1/containers/{containerId}/attachments:batch-create

Source: https://aps.autodesk.com/en/docs/acc/reference/http/cost-attachmentsbatch-create-POST/

---

# v1/containers/{containerId}/attachments:batch-create

Creates an attachment in a specific project.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/cost/v1/containers/:containerId/attachments:batch-create Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json region string Specifies the region where the project data resides. By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead. Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page. To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

By default, the request is routed automatically. However, specifying the region can improve performance by avoiding lookup overhead.

Possible values: country or region codes such as US or EMEA . For the full list of supported regions, see the ACC Regions page.

To verify your projectâs region, refer to the Working with BIM 360 Services in Different Regions section on the API Basics page.

### Request

## URI Parameters

containerId string: UUID The ID of the project (the container ID is the same as the project ID). To obtain the project ID, see GET projects .

### Request

## Body Structure

The Attachment:batch-create

folderId string: UUID The unique identifier (UUID) of the folder named attachment-folder where the attachment is stored. This ID is automatically retrieved by the backend and returned in the response. urn string The object version URN of the attachment in the Autodesk Data Management service. pdfOssUrn string,null Not relevant pdfUrn string,null Not relevant type enum:string The type of attachment.
Possible values: Upload : is a locally uploaded file. DocsFile is a file referenced from BIM 360 Docs. Reference is a file referenced form report. Document is for document generation. Max length: 64 name string The name of the attachment. Max length: 1024 replaceIfExists boolean Determines whether an existing attachment with a matching name should be replaced. status string The status of the attachment. Max length: 1024 associationId string: UUID The object ID of the item associated with the actions, such as a budget, contract, or cost item. associationType enum:string The type of item to which it is associated.
Possible values: Budget , Contract , ScheduleOfValue , FormInstance , CostItem , Payment , MainContract , BudgetPayment , Expense , CostPayment , ExpenseItem , PaymentItem , OCO , RCO , SCO , PCO , RFQ , DistributionItem , BudgetTransfer , Fee

Upload : is a locally uploaded file.

DocsFile is a file referenced from BIM 360 Docs.

Reference is a file referenced form report.

Document is for document generation.

Max length: 64

Max length: 1024

Max length: 1024

### Response

## HTTP Status Code Summary

201 Created Success 400 Bad Request The parameters are invalid. 401 Unauthorized The provided bearer token is invalid. 403 Forbidden Forbidden. The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The resource or endpoint cannot be found. 409 Conflict The request could not be completed due to a conflict with the current state of the resource. 429 Too Many Requests Rate limit exceeded. Retry your request after a few minutes. 500 Internal Server Error An unexpected error occurred on the server. 503 Service Unavailable Service unavailable.

### Response

## Body Structure (201)

id string: UUID The unique auto-generated identifier of the attachment. folderId string: UUID The unique identifier (UUID) of the folder named attachment-folder where the attachment is stored. This ID is automatically retrieved by the backend and returned in the response. urn string The object version URN of the attachment in the Autodesk Data Management service. pdfOssUrn string,null Not relevant pdfUrn string,null Not relevant type enum:string The type of attachment.
Possible values: Upload : is a locally uploaded file. DocsFile is a file referenced from BIM 360 Docs. Reference is a file referenced form report. Document is for document generation. Max length: 64 name string The name of the attachment. Max length: 1024 replaceIfExists boolean Determines whether an existing attachment with a matching name should be replaced. status string The status of the attachment. Max length: 1024 associationId string: UUID The object ID of the item associated with the actions, such as a budget, contract, or cost item. associationType enum:string The type of item to which it is associated.
Possible values: Budget , Contract , ScheduleOfValue , FormInstance , CostItem , Payment , MainContract , BudgetPayment , Expense , CostPayment , ExpenseItem , PaymentItem , OCO , RCO , SCO , PCO , RFQ , DistributionItem , BudgetTransfer , Fee createdAt datetime: ISO 8601 The date and time that the item was created, in ISO 8601 format. updatedAt datetime: ISO 8601 The date and time that the item was last updated, in ISO 8601 format.

Upload : is a locally uploaded file.

DocsFile is a file referenced from BIM 360 Docs.

Reference is a file referenced form report.

Document is for document generation.

Max length: 64

Max length: 1024

Max length: 1024

## Example

Success

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/attachments:batch-create' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '[ { "folderId": "8E34872D-A56F-4096-B675-476F50F4EF51", "urn": "urn:adsk.wipprod:fs.file:vf.PMbRnoPZR2mKDhau2uw4SQ?version=1", "pdfOssUrn": "urn:adsk.wipprod:fs.file:vf.PMbRnoPZR2mKDhau2uw4SQ?version=1", "pdfUrn": "urn:adsk.wipprod:fs.file:vf.PMbRnoPZR2mKDhau2uw4SQ?version=1", "type": "Upload", "name": "Architecture", "replaceIfExists": true, "status": "Pending", "associationId": "EDC42DF6-277A-436A-A50D-EF57F35E1248", "associationType": "Budget" } ]'
```

### Response

```
{ "id" : "F2D2ED17-C763-465B-8FAB-251C5A35D42F" , "folderId" : "8E34872D-A56F-4096-B675-476F50F4EF51" , "urn" : "urn:adsk.wipprod:fs.file:vf.PMbRnoPZR2mKDhau2uw4SQ?version=1" , "pdfOssUrn" : "urn:adsk.wipprod:fs.file:vf.PMbRnoPZR2mKDhau2uw4SQ?version=1" , "pdfUrn" : "urn:adsk.wipprod:fs.file:vf.PMbRnoPZR2mKDhau2uw4SQ?version=1" , "type" : "Upload" , "name" : "Architecture" , "replaceIfExists" : true , "status" : "Pending" , "associationId" : "EDC42DF6-277A-436A-A50D-EF57F35E1248" , "associationType" : "Budget" , "createdAt" : "2019-01-06T01:24:22.678Z" , "updatedAt" : "2019-09-05T01:00:12.989Z" }
```
