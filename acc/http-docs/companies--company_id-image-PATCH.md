# companies/:company_id/image

Source: https://aps.autodesk.com/en/docs/acc/reference/http/companies-:company_id-image-PATCH/

---

# companies/:company_id/image

Create or update a specific partner companyâs image.

## Resource Information

Method and URI PATCH https://developer.api.autodesk.com/hq/v1/accounts/:account_id/companies/:company_id/image Method and URI (Legacy) PATCH https://developer.api.autodesk.com/hq/v1/regions/eu/accounts/:account_id/companies/:company_id/image Authentication Context app only Required OAuth Scopes account:write Data Formats JSON

### Request

## Headers

HTTP Headers Type Required Description Authorization string yes Must be Bearer <token> , where <token> is obtained via a two-legged OAuth flow. Region string no Specifies the region where the service is located.                                                                                                        Possible values: US , EMEA . For the full list of supported regions, see the Regions page. Content-Type string yes Must be multipart/form-data

### Request

## URI Parameters

account_id string: UUID The account ID of the company. This corresponds to hub ID in the Data Management API . To convert a hub ID into an account ID you need to remove the â b. " prefix. For example, a hub ID of b. c8b0c73d-3ae9 translates to an account ID of c8b0c73d-3ae9. company_id string: UUID Company ID

### Request

## Body Structure

The file to be uploaded as HTTP multipart (chunk) data. Supported MIME types are image/png , image/jpeg , image/jpg , image/bmp , and image/gif .

### Response

## HTTP Status Code Summary

200 OK The request has succeeded. 400 Bad Request The request could not be understood by the server due to malformed syntax. 403 Forbidden Unauthorized 404 Not Found The resource cannot be found. 409 Conflict The request could not be completed due to a conflict with the current state of the resource. 422 Unprocessable Entity The request was unable to be followed due to restrictions. 500 Internal Server Error An unexpected error occurred on the server.

### Response

## Body Structure (200)

A successful response is the updated company, a flat JSON object with the following attributes:

id string: UUID Company ID account_id string: UUID Account ID name string Company name should be unique under an account Max length: 255 trade string Trade type based on specialization Refer to the trade list in the Parameters guide. address_line_1 string Company address line 1 Max length: 255 address_line_2 string Company address line 2 Max length: 255 city string City in which company is located Max length: 255 state_or_province enum: string State or province in which company is located Max length: 255 Note that the state_or_province value depends on the selected country value;
see the valid values in the state_or_province list in
the Parameters guide. postal_code string Postal code for the company location Max length: 255 country enum: string Country for this company Refer to the country list in the Parameters guide. phone string Business phone number for the company Max length: 255 website_url string Company website Max length: 255 description string Short description or overview for company Max length: 255 erp_id string Used to associate a company in BIM 360 with the company data in an ERP system tax_id string Used to associate a company in BIM 360 with the company data from public and industry sources

## Example

Successful Updating Company Image (200)

### Request

```
curl 'https://developer.api.autodesk.com/hq/v1/accounts/80793a28-f9b1-4888-9533-5f00cddcd6fb/companies/fc830fd8-f1ef-4cd6-9163-fb115dc698d7/image' \ -X 'PATCH' \ -H 'Authorization: Bearer RVKtOysEJKtQh6RJDJF7oJBrBGc4' \ -H 'Content-Type: multipart/form-data' \ -F 'chunk=@/Users/test/Desktop/demo.png;type=image/png'
```

### Response

```
{ "id" : "fc830fd8-f1ef-4cd6-9163-fb115dc698d7" , "account_id" : "80793a28-f9b1-4888-9533-5f00cddcd6fb" , "name" : "Autodesk" , "trade" : "Concrete" , "address_line_1" : "The Fifth Avenue" , "address_line_2" : "#301" , "city" : "New York" , "postal_code" : "10011" , "state_or_province" : "New York" , "country" : "United States" , "phone" : "(503)623-1525" , "website_url" : "http://www.autodesk.com" , "description" : "Autodesk, Inc., is a leader in 3D design, engineering and entertainment software." , "created_at" : "2016-05-20T02:24:21.400Z" , "updated_at" : "2016-05-20T09:28:21.354Z" , "erp_id" : "c79bf096-5a3e-41a4-aaf8-a771ed329047" , "tax_id" : "213-73-8867" }
```
