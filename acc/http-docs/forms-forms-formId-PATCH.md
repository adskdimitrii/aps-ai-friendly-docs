# v1/projects/{projectId}/form-templates/{templateId}/forms/{formId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/forms-forms-formId-PATCH/

---

# v1/projects/{projectId}/form-templates/{templateId}/forms/{formId}

Updates a formâs form details. Note that we do not currently support updating PDF forms.

To edit a form, it must be in draft or inReview status and the user must have permissions to edit the form. See the Forms help documentation for information about template configurations.

See the Manage Forms tutorial for details about updating form details.

To update the formâs main form fields (tabular and non-tabular) use PUT values:batch-upsert API .

## Resource Information

Method and URI PATCH https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/form-templates/:templateId/forms/:formId Authentication Context user context required Required OAuth Scopes data:write Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json

### Request

## URI Parameters

projectId string The ID of the project. Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. templateId string The unique identifier of the form template. Use GET forms to retrieve a formâs template ID. formId string The unique identifier of the form. Use GET forms to retrieve the form ID.

Use the Data Management API to retrieve the project ID. For more information, see the Retrieve a Project ID tutorial. You need to convert the project ID into a project ID for the ACC API by removing the â b. " prefix. For example, a project ID of b. a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.

Use GET forms to retrieve a formâs template ID.

Use GET forms to retrieve the form ID.

### Request

## Body Structure

assigneeId string The unique identifier of the company, role, or user the form is assigned to. Note that the assignee must be a contributor of the template. assigneeType enum:string Type of entity the form is assigned to.
Possible values: company , role , user description string Text for the formâs description field. Max length: 8000 name string The name of the form instance. If the specified value is null or empty, it defaults to the formâs template name. Max length: 100 formDate string Date the form pertains to, must be after 1950-01-01. locationId string: UUID Location identifier associated with the form. For more information about the location, see GET nodes . notes string Text for the formâs notes section. Max length: 8000 status enum:string New status for the form. "draft" (in progress) forms may be edited. "inReview" forms may not be edited but may be approved by the form reviewers. "submitted" forms are closed and no longer editable. "archived" forms are not editable and hidden in the ui Possible values: draft , discarded , submitted , archived , in_review submitterSignature string Signature of the reviewer who is submitting the form (should be included when submitting an inReview form) as a base64 encoded SVG. Note: the SVG will be sanitized: tags and attributes are limited to the basics (<path>, <g>, <polyline>, etc) needed to represent a signature.

Max length: 8000

Max length: 100

Max length: 8000

"draft" (in progress) forms may be edited.

"inReview" forms may not be edited but may be approved by the form reviewers.

"submitted" forms are closed and no longer editable.

"archived" forms are not editable and hidden in the ui

Possible values: draft , discarded , submitted , archived , in_review

Note: the SVG will be sanitized: tags and attributes are limited to the basics (<path>, <g>, <polyline>, etc) needed to represent a signature.

### Response

## HTTP Status Code Summary

200 OK The updated Form 400 Bad Request The request could not be understood by the server due to malformed syntax or missing request header 401 Unauthorized The request was not accepted because it lacked valid authentication credentials 403 Forbidden The request was not accepted because the client is authenticated, but is not authorized to access the target resource 404 Not Found The resource cannot be found 409 Conflict The request could not be completed due to a conflict with the current state of the target resource 429 Too Many Requests The request could not be completed due to a conflict with the current state of the target resource 500 Internal Server Error The request could not be completed due to a conflict with the current state of the target resource

### Response

## Body Structure (200)

status enum:string The current status of the form. Note that forms are created in draft status. Possible values: draft : you can edit forms. inReview : you cannot edit forms, however, they can be approved by form reviewers. submitted : forms are closed and no longer editable. archived forms are not edtiable and hidden in the UI. id string The unique identifier of the form. projectId string The unique identifier of the project the form belongs to. formNum int A chronological user-fiendly identifier of the form within the project e.g. form #5. formDate string Date the form pertains to. assigneeId string The unique identifier of the user, role, or company the form is assigned to. assigneeType enum:string Type of entity the form is assigned to.
Possible values: company , role , user locationId string Location identifier associated with the form. For more information about the location, see GET nodes . updatedAt datetime: ISO 8601 When form was last updated, UTC date and time in ISO-8601 format. createdBy string The unique identifier of the user who created the form. notes string Text for the formâs notes section. description string Text for the formâs description section. name string The name of the form instance. Max length: 100 formTemplate object Information about the formâs template. status enum:string Possible values: active , inactive , deleted id string The unique identifier of the template. projectId string Unique indentifier of the project the template belongs to. name string Name of the form template. templateType string User defined type of the form template. pdfValues array: object For PDF forms, values extracted from fields in the PDF. name string The name of the PDF field. value string The value of the PDF field. pdfUrl string For PDF forms, the URL to download the formâs PDF. weather object Weather forecast captured on the form. summaryKey string A code describing the the weather (e.g. Clear, PartlyCloudy). precipitationAccumulation number Amount of precipitation accumulated throughout the day. precipitationAccumulationUnit string Indicates the measurement unit of the precipitationAccumulation . temperatureMin number Minimum temperature during the day. temperatureMax number Maximum temperature during the day. temperatureUnit string Indicates the measurement unit of the temperature values e.g. temperatureMin , temperatureMax , temp . humidity number A percentage value indicating the humidity over the course of the day. windSpeed number Average wind speed observed throughout the day. windGust number Maximum wind speed observed throughout the day. speedUnit string Indicates the measurement unit of the windSpeed and windGust . windBearing number Direction of the wind, in degrees. hourlyWeather array: object Weather information for specific hours (07:00:00, 12:00:00, 16:00:00). id int Unique identifier. hour string Hour of the day for this forecast. temp number Temperature during specified hour. windSpeed number Average wind speed. windBearing int Direction of the wind, in degrees. humidity number A percentage value indicating the humidity. fetchedAt datetime: ISO 8601 Date when weather was fetched from weather API. createdAt datetime: ISO 8601 Date when weather was first fetched. updatedAt datetime: ISO 8601 When the weather was last updated. provider enum:string Indicates the source of the weather data.
Possible values: darksky , weatherkit tabularValues object For non-PDF forms, data stored in the tables on the form. worklogEntries array: object Entries associated with work log table in a Form. id string Unique identifier for the work log row. deleted boolean Indicates if the work log row has been deleted. trade string A text field indicating the workerâs trade. timespan int Total duration of work performed (in milliseconds). headcount int Number of workers. description string A text description of the work performed. materialsEntries array: object Entries associated with materials table in a Form. id string Unique identifier for the material log row. deleted boolean Indicates if the material log row has been deleted. item string Text indicating the material used. quantity number The quantity of material that was used. unit string The unit of measure for the quantity specified. description string Additional description of the materials. equipmentEntries array: object Entries associated with equipment table in a Form. id string Unique identifier for the equipment log row. deleted boolean Indicates if the equipment log row has been deleted. item string Text indicating the equipment utilized. timespan int The total time all equipment was utilized (in milliseconds). quantity number The amount of equipment utilized. description string Text describing the equipment utilized. customValues array: object For non-PDF forms, data stored in the form fields. fieldId string The unique identifier of the field. sectionLabel string Name of the section containing this field. itemLabel string The fieldâs label or question text. valueName enum:string Indicates the type of value used for this item.
Possible values: textVal , toggleVal , arrayVal , numberVal , choiceVal , dateVal , svgVal toggleVal enum:string A boolean like enum value.
Possible values: Yes , No , False , True , Minus , Plus , Fail , Pass , NA textVal string A text value. arrayVal string Multi select values. numberVal number A numeric value. choiceVal string A single select value. dateVal string A date value. svgVal string A signature value (base64 encoded SVG). notes string Text for the fieldâs notes section. Max length: 8000 lastReopenedBy string Unique identifier for the user that last re-opened the Form (if applicable). lastSubmitterSignature string Signature of the reviewer who last submitted the Form (if applicable). Signature value (base64 encoded SVG). userCreatedAt datetime: ISO 8601 When form was created on the client, UTC date and time in ISO-8601 format. createdAt datetime: ISO 8601 When form was created on the server, UTC date and time in ISO-8601 format.

draft : you can edit forms.

inReview : you cannot edit forms, however, they can be approved by form reviewers.

submitted : forms are closed and no longer editable.

archived forms are not edtiable and hidden in the UI.

Max length: 100

Max length: 8000

## Example

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/form-templates/:templateId/forms/:formId' \
-X 'PATCH' \
-H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
-H 'Content-Type: application/json' \
-d '{
      "assigneeId": "USER123A",
      "assigneeType": "user",
      "name": "Daily Safety Inspection",
      "description": "For Sam Subcontractor",
      "formDate": "2020-11-20",
      "locationId": "cee45678-fcc4-43ae-80a2-8ca819dfa70d",
      "notes": "Installed 25 units",
      "status": "submitted",
      "submitterSignature": "PHN2ZyBoZWlnaHQ9IjIwMCIgd2lkdGg9IjUwMCI+PHBvbHlsaW5lIHBvaW50cz0iMjAsMjAgNDAsMjUgNjAsNDAgODAsMTIwIDEyMCwxNDAgMjAwLDE4MCIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2U6YmxhY2s7c3Ryb2tlLXdpZHRoOjMiIC8+PC9zdmc+"
    }'
```

### Response

```
{ "status" : "submitted" , "id" : "932da979-e537-4530-b8aa-18607ac6db37" , "projectId" : "9ba6681e-1952-4d54-aac4-9de6d9858dd4" , "formNum" : 1 , "name" : "Daily Safety Inspection" , "formDate" : "2020-11-20" , "assigneeId" : "fc830fd8-f1ef-4cd6-9163-fb115dc698d7" , "assigneeType" : "company" , "locationId" : "d14ce3a6-e61b-4ab0-a9be-5acf7b5366df" , "updatedAt" : "2020-11-20T16:14:27.615127+00:00" , "createdBy" : "USER123A" , "notes" : "Form notes" , "description" : "Form description" , "formTemplate" : { "status" : "active" , "id" : "2f634a22-779d-4930-9f08-8391a41fea05" , "projectId" : "9ba6681e-1952-4d54-aac4-9de6d9858dd4" , "name" : "Daily Report" , "templateType" : "pg.template_type.daily_report" }, "pdfValues" : [ { "name" : "CommentsRow1" , "value" : "Observed Masks and Face Covering" } ], "pdfUrl" : "https://link.to/form.pdf" , "weather" : { "summaryKey" : "Clear" , "precipitationAccumulation" : 2.3 , "precipitationAccumulationUnit" : "in" , "temperatureMin" : 47.1 , "temperatureMax" : 65.1 , "temperatureUnit" : "Fahrenheit" , "humidity" : 0.2 , "windSpeed" : 12.5 , "windGust" : 34.6 , "speedUnit" : "km/h" , "windBearing" : 18 , "hourlyWeather" : [ { "id" : 1234 , "hour" : "07:00:00" , "temp" : 54.12 , "windSpeed" : 14.2 , "windBearing" : 14 , "humidity" : 0.24 , "fetchedAt" : null , "createdAt" : "2021-01-20T20:38:32+00:00" , "updatedAt" : "2021-01-20T20:38:32+00:00" } ], "provider" : "weatherkit" }, "tabularValues" : { "worklogEntries" : null , "materialsEntries" : null , "equipmentEntries" : null }, "customValues" : [], "lastReopenedBy" : "USER123A" , "lastSubmitterSignature" : "PHN2ZyBoZWlnaHQ9IjIwMCIgd2lkdGg9IjUwMCI+PHBvbHlsaW5lIHBvaW50cz0iMjAsMjAgNDAsMjUgNjAsNDAgODAsMTIwIDEyMCwxNDAgMjAwLDE4MCIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2U6YmxhY2s7c3Ryb2tlLXdpZHRoOjMiIC8+PC9zdmc+" , "userCreatedAt" : "2019-01-20T12:14:27.615127+00:00" , "createdAt" : "2019-01-20T12:14:28.000000+00:00" }
```
