# projects/{projectId}/naming-standards/{id}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/document-management-naming-standards-id-GET/

---

# projects/{projectId}/naming-standards/{id}

Retrieves the file naming standard for a project.

You need to configure the file naming standard in the UI. For more information, see the BIM 360 File Naming Standard help documentation.

Note that the order of the objects that the endpoint returns in the response corresponds to the order of the fields that you set for the naming standard in the UI.

Note that we currently support one file naming standard per project.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/bim360/docs/v1/projects/:projectId/naming-standards/:id Authentication Context user context optional Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. x-ads-region string The region to which your request should be routed. If not set, the request is routed automatically but may incur a small latency increase. Possible values: US , EMEA .

Possible values: US , EMEA .

### Request

## URI Parameters

projectId string: UUID The ID of the project. This corresponds to project ID in the Data Management API . To convert a project ID in the Data Management API into a project ID in the BIM 360 API you need to remove the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. To learn how to find the project ID, see the Retrieve BIM 360 Account and Project ID tutorial. id string: UUID The ID of the file naming standard. The file naming standard is applied to the project files folder or its subfolders. To find the ID: For the project files folder, call GET hubs/:hub_id/projects/:project_id/topFolders . For subfolders, call GET projects/:project_id/folders/:folder_id/contents . For a specific folder, call GET projects/:project_id/folders/:folder_id . The ID is under data.attributes.extension.data.namingStandardIds .

This corresponds to project ID in the Data Management API . To convert a project ID in the Data Management API into a project ID in the BIM 360 API you need to remove the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

To learn how to find the project ID, see the Retrieve BIM 360 Account and Project ID tutorial.

The file naming standard is applied to the project files folder or its subfolders. To find the ID:

- For the project files folder, call GET hubs/:hub_id/projects/:project_id/topFolders .

- For subfolders, call GET projects/:project_id/folders/:folder_id/contents .

- For a specific folder, call GET projects/:project_id/folders/:folder_id .

The ID is under data.attributes.extension.data.namingStandardIds .

### Response

## HTTP Status Code Summary

200 OK Successfully retrieved the file naming standard. 400 Bad Request The parameters of the requested operation are invalid. 403 Forbidden The user or service represented by the bearer token does not have permission to perform this operation. 404 Not Found The file naming standard does not exist. 500 Internal Server Error An unknown error occurred on the server.

### Response

## Body Structure (200)

id string: UUID The ID of file naming standard. name string The name of the file naming standard. definition object The file naming standard format. delimiter string A specified character, separating between multiple fields of a file name. Possible values: - : Hyphen. _ : Underscore. . : Point. Note that you cannot use the delimiter within a field name. fields array: object A list of objects defining a fileâs field names. Note that the order of the objects that the endpoint returns in the response corresponds to the order of the fields that you set for the naming standard in the UI. name string The name of the field. Max length: 32 type enum:string The field type. Possible values: ALPHANUMERIC : Accepts all characters. NONNUMERIC_TEXT : Accepts all characters, excluding 0-9 . NUMERIC : Accepts 0-9 , comma ',' , plus '+' , minus '-' , percent '%' , period '.' , underscore '_' . ARRAY : A drop-down list. Note that the minLength and maxLength properties are not included in the response for the ARRAY type. attributeId number The ID of the field. optional boolean true : this field is required in the file naming convention. false : this field is not required in the file naming convention. minLength number The minimum length of the field name. Min number of characters: 1 maxLength number The maximum length of the field name. Max number of characters: 10 defaultValue string The default value of the field. For example, PROJ . options array: object A drop-down list of possible values for the field. Only relevant for a field of type ARRAY (drop-down list). value string A drop-down list value. description string A description of the drop-down list value. description string A description of the field. Max length: 255 metadata array: object A list of objects defining a fileâs related attributes. These attributes do not appear in the file name. attributeId number The ID of the related attribute. name string The name of the related attribute. Max length: 32 type enum:string The related attribute type. Possible values: ALPHANUMERIC : Accepts all characters. NONNUMERIC_TEXT : Accepts all characters, excluding 0-9 . NUMERIC : Includes 0-9 , comma ',' , plus '+' , minus '-' , percent '%' , period '.' , underscore '_' . ARRAY : A drop-down list. CLASSIFICATION : Only relevant for a classification attribute. Note that the minLength and maxLength properties are not included in the response for the ARRAY type. optional boolean true : this related attribute is required. false : this related attribute is not required. minLength number The minimum length of the related attribute. Min number of characters: 1 maxLength number The maximum length of the related attribute. Max number of characters: 10 defaultValue string The default value of the related attribute. options array: object A drop-down list of possible values for the related attribute. Only relevant for a related attribute of type ARRAY (drop-down list). value string A drop-down list value. description string A description of the drop-down list value. description string A description of the related attribute. Max length: 255

Possible values:

- - : Hyphen.

- _ : Underscore.

- . : Point.

Note that you cannot use the delimiter within a field name.

Note that the order of the objects that the endpoint returns in the response corresponds to the order of the fields that you set for the naming standard in the UI.

Max length: 32

Possible values:

- ALPHANUMERIC : Accepts all characters.

- NONNUMERIC_TEXT : Accepts all characters, excluding 0-9 .

- NUMERIC : Accepts 0-9 , comma ',' , plus '+' , minus '-' , percent '%' , period '.' , underscore '_' .

- ARRAY : A drop-down list.

Note that the minLength and maxLength properties are not included in the response for the ARRAY type.

false : this field is not required in the file naming convention.

Min number of characters: 1

Max number of characters: 10

For example, PROJ .

Only relevant for a field of type ARRAY (drop-down list).

Max length: 255

Max length: 32

Possible values:

- ALPHANUMERIC : Accepts all characters.

- NONNUMERIC_TEXT : Accepts all characters, excluding 0-9 .

- NUMERIC : Includes 0-9 , comma ',' , plus '+' , minus '-' , percent '%' , period '.' , underscore '_' .

- ARRAY : A drop-down list.

- CLASSIFICATION : Only relevant for a classification attribute.

Note that the minLength and maxLength properties are not included in the response for the ARRAY type.

false : this related attribute is not required.

Min number of characters: 1

Max number of characters: 10

Only relevant for a related attribute of type ARRAY (drop-down list).

Max length: 255

## Example

Successfully retrieved the file naming standard.

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/docs/v1/projects/c0337487-5b66-422b-a284-c273b424af54/naming-standards/68097e38-bcae-4fb6-9da2-89eca69bccc8' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "id" : "68097e38-bcae-4fb6-9da2-89eca69bccc8" , "name" : "Default - ISO 19650" , "definition" : { "fields" : [ { "attributeId" : 333879 , "name" : "Project" , "type" : "ALPHANUMERIC" , "description" : "Project code." , "optional" : false , "maxLength" : 6 , "minLength" : 2 , "defaultValue" : "PROJ" }, { "attributeId" : 333880 , "name" : "Originator" , "type" : "ARRAY" , "description" : "Code representing the organization creating the file." , "options" : [ { "value" : "XXX" , "description" : "Example Organization" }, { "value" : "ARC" , "description" : "Architect" } ], "optional" : false , "defaultValue" : null }, { "attributeId" : 333881 , "name" : "Volume/System" , "type" : "ARRAY" , "description" : "Code for System reference" , "options" : [ { "value" : "ZZ" , "description" : "All Volumes/Systems" }, { "value" : "XX" , "description" : "No Volume/System applicable" } ], "optional" : false }, { "attributeId" : 333882 , "name" : "Level/Location" , "type" : "ARRAY" , "description" : "Code representing the Level/Location relevant to the file." , "options" : [ { "value" : "ZZ" , "description" : "Multiple Levels/Locations" }, { "value" : "XX" , "description" : "No Level/Location applicable" }, { "value" : "00" , "description" : "Base Level" }, { "value" : "01" , "description" : "Level 01" }, { "value" : "02" , "description" : "Level 02" }, { "value" : "M1" , "description" : "Mezzanine above Level 01" }, { "value" : "M2" , "description" : "Mezzanine above Level 02" }, { "value" : "B1" , "description" : "Basement Level 1" }, { "value" : "B2" , "description" : "Basement Level 2" } ], "optional" : false , "defaultValue" : null }, { "attributeId" : 333883 , "name" : "Type" , "type" : "ARRAY" , "description" : "Code representing the type of file." , "options" : [ { "value" : "AF" , "description" : "Animation File (of a model)" }, { "value" : "BQ" , "description" : "Bill of Quantities" }, { "value" : "CA" , "description" : "Calculations" }, { "value" : "CM" , "description" : "Combined Model (combined multidiscipline model)" }, { "value" : "CO" , "description" : "Correspondence" }, { "value" : "CP" , "description" : "Cost Plan" }, { "value" : "CR" , "description" : "Clash Rendition" }, { "value" : "DB" , "description" : "Database" }, { "value" : "DR" , "description" : "Drawing Rendition" }, { "value" : "FN" , "description" : "File Note" }, { "value" : "HS" , "description" : "Health and Safety" }, { "value" : "IE" , "description" : "Information Exchange file" }, { "value" : "M2" , "description" : "2D model" }, { "value" : "M3" , "description" : "3D model" }, { "value" : "MI" , "description" : "Minutes / Action Notes" }, { "value" : "MR" , "description" : "Model Rendition for other renditions" }, { "value" : "MS" , "description" : "Method Statement" }, { "value" : "PP" , "description" : "Presentation" }, { "value" : "PR" , "description" : "Programme" }, { "value" : "RD" , "description" : "Room Data sheet" }, { "value" : "RI" , "description" : "Request for Information" }, { "value" : "RP" , "description" : "Report" }, { "value" : "SA" , "description" : "Schedule of Accommodation" }, { "value" : "SH" , "description" : "Schedule" }, { "value" : "SN" , "description" : "Snagging List" }, { "value" : "SP" , "description" : "Specification" }, { "value" : "SU" , "description" : "Survey" }, { "value" : "VS" , "description" : "Visualization" } ], "optional" : false , "defaultValue" : null }, { "attributeId" : 333884 , "name" : "Role" , "type" : "ARRAY" , "description" : "Codes for disciplines and roles." , "options" : [ { "value" : "A" , "description" : "Architect" }, { "value" : "B" , "description" : "Building Surveyor" }, { "value" : "C" , "description" : "Civil Engineer" }, { "value" : "D" , "description" : "Drainage Engineer" }, { "value" : "E" , "description" : "Electrical Engineer" }, { "value" : "F" , "description" : "Facilities Manager" }, { "value" : "G" , "description" : "Geographical and Land Surveyor" }, { "value" : "H" , "description" : "Heating and Ventilation Designer (deprecated)" }, { "value" : "I" , "description" : "Interior Designer" }, { "value" : "K" , "description" : "Client" }, { "value" : "L" , "description" : "Landscape Architect" }, { "value" : "M" , "description" : "Mechanical Engineer" }, { "value" : "P" , "description" : "Public Health Engineer" }, { "value" : "Q" , "description" : "Quantity Surveyor" }, { "value" : "S" , "description" : "Structural Engineer" }, { "value" : "T" , "description" : "Town and Country Planner" }, { "value" : "W" , "description" : "Contractor" }, { "value" : "X" , "description" : "Subcontractor" }, { "value" : "Y" , "description" : "Specialist Designer" }, { "value" : "Z" , "description" : "General (non-disciplinary)" } ], "optional" : false , "defaultValue" : null }, { "attributeId" : 333885 , "name" : "Number" , "type" : "NUMERIC" , "description" : "Sequential Number." , "optional" : false , "maxLength" : 6 , "minLength" : 4 , "defaultValue" : "1111" } ], "metadata" : [ { "attributeId" : 333886 , "name" : "Status" , "type" : "ARRAY" , "description" : "The Suitability Code." , "options" : [ { "value" : "S0" , "description" : "Initial status" }, { "value" : "S1" , "description" : "Suitable for coordination" }, { "value" : "S2" , "description" : "Suitable for information" }, { "value" : "S3" , "description" : "Suitable for review and comment" }, { "value" : "S4" , "description" : "Suitable for stage approval" }, { "value" : "S6" , "description" : "Suitable for PIM authorization" }, { "value" : "S7" , "description" : "Suitable for AIM authorization" }, { "value" : "A0" , "description" : "Authorized and accepted for Strategy work stage" }, { "value" : "A1" , "description" : "Authorized and accepted for Brief work stage" }, { "value" : "A2" , "description" : "Authorized and accepted for Concept work stage" }, { "value" : "A3" , "description" : "Authorized and accepted for Definition work stage" }, { "value" : "A4" , "description" : "Authorized and accepted for Design work stage" }, { "value" : "A5" , "description" : "Authorized and accepted for Construct and Commission work stage" }, { "value" : "A6" , "description" : "Authorized and accepted for Handover and Close-out work stage" }, { "value" : "A7" , "description" : "Authorized and accepted for Operation and End-of-Life work stage" }, { "value" : "B0" , "description" : "Partial sign-off for Strategy work stage" }, { "value" : "B1" , "description" : "Partial sign-off for Brief work stage" }, { "value" : "B2" , "description" : "Partial sign-off for Concept work stage" }, { "value" : "B3" , "description" : "Partial sign-off for Definition work stage" }, { "value" : "B4" , "description" : "Partial sign-off for Design work stage" }, { "value" : "B5" , "description" : "Partial sign-off for Construct and Commission work stage" }, { "value" : "B6" , "description" : "Partial sign-off for Handover and Close-out work stage" }, { "value" : "B7" , "description" : "Partial sign-off for Operation and End-of-Life work stage" }, { "value" : "CR" , "description" : "As constructed record document" } ], "optional" : true , "defaultValue" : null }, { "attributeId" : 333887 , "name" : "Revision" , "type" : "ALPHANUMERIC" , "description" : "Code for revision of data." , "optional" : true , "maxLength" : 8 , "minLength" : 3 , "defaultValue" : "S01" }, { "attributeId" : 333888 , "name" : "Classification" , "type" : "CLASSIFICATION" , "description" : "Code to reference asset." , "optional" : true , "defaultValue" : null } ], "delimiter" : "-" } }
```
