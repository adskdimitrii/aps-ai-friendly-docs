# v1/projects/{projectId}/forms/{formId}/values:batch-update

Source: https://aps.autodesk.com/en/docs/acc/reference/http/forms-valuesbatch-update-(Deprecated)-PUT/

---

Forms

PUT

# v1/projects/{projectId}/forms/{formId}/values:batch-update

Deprecated

Updates a form’s main form fields, both tabular and non-tabular. Note that we do not currently support updating PDF forms.

To edit form values, the form needs to be in draft status and the user must have permissions to edit the form. See the [Forms help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Build_Forms_templates_html) for information about template configuration.

To update non-tabular fields you need to use the relevant value type. For example, to update a number field you need to use `numberVal`. To find the value type for the field, call GET forms and check the `valueName`.

See the [Manage Forms tutorial](../how-to-docs/forms-create-update-forms.md) for more details about how to update forms.

To update the form’s details, use [PATCH forms/:formId API](http-forms-forms-formId-PATCH.md).

Note that we do not currently support adding issues or photos.

## [Resource Information](#resource-information)

| Method and URI | PUT https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). <br>The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the Forma API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.
- formIdstring The unique identifier of the form. Use [GET forms](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-forms-(Deprecated/)-GET/) to retrieve the form ID.

### Request

## [Body Structure](#body-structure)

Expand all

| customValues   array: object | The list of non-tabular fields. Maximum 10 items per request. |
| --- | --- |
| fieldId*   string: UUID | The unique identifier of the field. |
| notes   string | Text for the field’s notes section. This is relevant for all fields. <br>Max length: 8000 |
| textVal   string | The attribute used for updating text value fields, For example, `textVal: This is my response!`. <br>Each non-tabular field is assigned a specific value type, which you need to specify when updating the field. `textVal` is only relevant for updating text value fields. To verify whether the field you want to update is a text value field, call GET forms and check the field’s `valueName`.<br>Max length: 8000 |
| choiceVal   string | The attribute used for updating single-select and dropdown fields. For example, `choiceVal: Answer 3`. <br>Each non-tabular field is assigned a specific value type, which you need to specify when updating the field. `choiceVal` is only relevant for updating single-select and dropdown fields. To verify whether the field you want to update is a single-select or dropdown field, call GET forms and check the field’s `valueName`. |
| arrayVal   array: string | The attribute used for updating multi-select fields. For example, `arrayVal:` `["Answer 1", "Answer 2"]`. <br>Each non-tabular field is assigned a specific value type, which you need to specify when updating the field. `arrayVal` is only relevant for updating multi-select fields. To verify whether the field you want to update is a multi-select field, call GET forms and check the field’s `valueName`. |
| dateVal   string | The attribute used for updating date fields, in the following format `(YYYY-MM-DD)`. For example, `"dateVal": "1999-12-31"`. <br>Each non-tabular field is assigned a specific value type, which you need to specify when updating the field. `dateVal` is only relevant for updating date fields. To verify whether the field you want to update is a date field, call GET forms and check the field’s `valueName`. |
| numberVal   number | The attribute used for updating number fields. For example, `"numberVal": "42"`. <br>Each non-tabular field is assigned a specific value type, which you need to specify when updating the field. `numberVal` is only relevant for updating number fields. To verify whether the field you want to update is a number field, call GET forms and check the field’s `valueName`. |
| toggleVal   enum:string | The attribute used for updating preconfigured fields. For example, “toggleVal”: “Yes”. <br>Each non-tabular field is assigned a specific value type, which you need to specify when updating the field. `toggleVal` is only relevant for updating preconfigured fields. To verify whether the field you want to update is a preconfigured field, call GET forms and check the field’s `valueName`. Possible values: `Yes`, `No`, `False`, `True`, `Minus`, `Plus`, `Fail`, `Pass`, `NA` |
| svgVal   string | The attribute used for updating signature fields. <br>Each non-tabular field is assigned a specific value type, which you need to specify when updating the field. `svgVal` is only relevant for updating signature fields. To verify whether the field you want to update is a signature field, call GET forms and check the field’s `valueName`.<br>The signature needs to be in SVG format and it needs to be base64 encoded. |
| name   string | The name of the person who signed the form. By default, it is the name of the logged in user. It is only relevant for signature fields. To update the name you need to use the signature field ID. |
| tabularValues   array: object | The list of tabular fields. Maximum 10 items per request. |
| id*   string: UUID | The ID of the table row. You need to generarte the ID (UUID) for the row. |
| table*   enum:string | The table to update. Possible values: `worklogEntries`, `materialsEntries`, `equipmentEntries` |
| columns   array: object | The set of values for the columns in the row. |
| columnId   string: UUID | Unique identifier for the column. Either `columnId` or `columnName` must be provided, but not both. |
| columnName   enum:string | The name of the column to update. Either `columnId` or `columnName` must be provided, but not both. <br>For the Work Log table:<br>`trade` (Crew) - use `textVal`, `timespan` (Total hours) - use `timespanVal`, `headcount` (workers) - use `numberVal`, `description` (work performed) - use `textVal`<br>For the Equipment table:<br>`item` (equipment) - use `textVal`, `timespan` (Hours used) - use `timespanVal`, `quantity` (Quantity) - use `numberVal`, `description` (comment) - use `textVal`<br>For the Materials table:<br>`item` (Material) - use `textVal`, `quantity` (Quantity) - use `numberVal`, `unit` (Unit) - use `textVal`, `description` (Comment) - use `textVal`. Possible values: `companyId`, `description`, `headcount`, `item`, `quantity`, `roleId`, `timespan`, `trade`, `unit` |
| numberVal   number | The attribute used for updating number columns. For example, `"numberVal": "42"`. <br>Each tabular field is assigned a specific value type, which you need to specify when updating the field. `numberVal` is relevant for updating the following columns: `headcount` (Workers) and `quantity` (Quantity). |
| integerVal   int | The attribute used for updating integer columns. |
| textVal   string | The attribute used for updating text value columns. <br>Each tabular field is assigned a specific value type, which you need to specify when updating the field. `textVal` is relevant for updating the following columns: `description` (Work performed), `description` (comment), `item` (Equipment), `item` (Material), `trade` (Crew), and `unit` (Unit).<br>Note: When using `svgVal` for signatures, `textVal` should contain the name of the person who signed.<br>Max length: 8000 |
| svgVal   string | Base64 encoded SVG string used for signature fields. When providing a signature, you must also include the signer’s name in `textVal`. |
| arrayVal   array: string | Array of strings for dropdown or multi-select answers. |
| timespanVal   number | The attribute used for updating time-related columns. Value represents amount of time in milliseconds. <br>Each tabular field is assigned a specific value type, which you need to specify when updating the field. `timespanVal` is relevant for updating the following columns: `timespan` (Total hours), `timespan` (Hours used). |
| uidVal   string | UUID value for fields that store unique identifiers. |
| dateVal   string | Date value without timezone. |
| timeVal   string | Time value without timezone. |
| datetimeLocalVal   string | Datetime value in local time. When providing this field, you must also include `datetimeUtcVal`, `timezoneVal`, and `timezoneRulesVal`. Optionally include `latVal` and `lngVal` for more accurate timezone handling. |
| datetimeUtcVal   string | Datetime value in UTC. Required when `datetimeLocalVal` is provided. |
| timezoneVal   string | Timezone identifier. Required when `datetimeLocalVal` is provided. |
| timezoneRulesVal   string | Timezone rules data. Required when `datetimeLocalVal` is provided. |
| latVal   number | Latitude value. Optional but recommended when using datetime fields for accurate timezone handling during daylight saving transitions. |
| lngVal   number | Longitude value. Optional but recommended when using datetime fields for accurate timezone handling during daylight saving transitions. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The updated Form |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request header |
| 401   Unauthorized | The request was not accepted because it lacked valid authentication credentials |
| 403   Forbidden | The request was not accepted because the client is authenticated, but is not authorized to access the target resource |
| 404   Not Found | The resource cannot be found |
| 409   Conflict | The request could not be completed due to a conflict with the current state of the target resource |
| 429   Too Many Requests | The request could not be completed due to the rate limit of the target resource |
| 500   Internal Server Error | The request could not be completed due to an internal server error |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| status   enum:string | The current status of the form. Note that forms are created in `draft` status. Possible values: <br>`draft`: you can edit forms.<br>`inReview`: you cannot edit forms, however, they can be approved by form reviewers.<br>`submitted`: forms are closed and no longer editable.<br>`archived` forms are not edtiable and hidden in the UI. |
| --- | --- |
| id   string | The unique identifier of the form. |
| projectId   string | The unique identifier of the project the form belongs to. |
| formNum   int | A chronological user-fiendly identifier of the form within the project e.g. form #5. |
| formDate   string | Date the form pertains to. |
| assigneeId   string | The unique identifier of the user, role, or company the form is assigned to. |
| assigneeType   enum:string | Type of entity the form is assigned to. Possible values: `company`, `role`, `user` |
| locationId   string | Location identifier associated with the form. For more information about the location, see [GET nodes](http-locations-nodes-GET.md). |
| updatedAt   datetime: ISO 8601 | The date when the form was last updated, UTC date and time in ISO-8601 format. |
| createdBy   string | The unique identifier of the user who created the form. |
| notes   string | Text for the form’s notes section. |
| description   string | Text for the form’s description section. |
| name   string | The name of the form instance. <br>Max length: 100 |
| formTemplate   object | Information about the form’s template. |
| status   enum:string | Possible values: `active`, `inactive`, `deleted` |
| id   string | The unique identifier of the template. |
| projectId   string | Unique indentifier of the project the template belongs to. |
| name   string | Name of the form template. |
| templateType   string | User defined type of the form template. |
| pdfValues   array: object | For PDF forms, values extracted from fields in the PDF. |
| name   string | The name of the PDF field. |
| value   string | The value of the PDF field. |
| pdfUrl   string | For PDF forms, the URL to download the form’s PDF. |
| weather   object | Weather forecast captured on the form. |
| summaryKey   string | A code describing the weather conditions. For weather data from DarkSky (legacy), possible values are: `clear`, `rain`, `snow`, `sleet`, `wind`, `fog`, `cloudy`, `partlyCloudy`. For weather data from WeatherKit, values come from Apple’s WeatherCondition codes and include: `Clear`, `MostlyClear`, `PartlyCloudy`, `MostlyCloudy`, `Cloudy`, `Rain`, `HeavyRain`, `Drizzle`, `Snow`, `HeavySnow`, `Flurries`, `Sleet`, `FreezingRain`, `FreezingDrizzle`, `Hail`, `Thunderstorms`, `IsolatedThunderstorms`, `ScatteredThunderstorms`, `StrongStorms`, `Windy`, `Breezy`, `Foggy`, `Haze`, `Smoky`, `Blizzard`, `BlowingDust`, `BlowingSnow`, `TropicalStorm`, `Hurricane`, `SunShowers`, `Hot`, `Frigid`, `WintryMix`. Check the `provider` field to determine which value set to expect. Additional values may appear as Apple’s WeatherKit condition codes evolve. |
| precipitationAccumulation   number | Amount of precipitation accumulated throughout the day. |
| precipitationAccumulationUnit   string | Indicates the measurement unit of the `precipitationAccumulation`. |
| temperatureMin   number | Minimum temperature during the day. |
| temperatureMax   number | Maximum temperature during the day. |
| temperatureUnit   string | Indicates the measurement unit of the temperature values e.g. `temperatureMin`, `temperatureMax`, `temp`. |
| humidity   number | A percentage value indicating the humidity over the course of the day. |
| windSpeed   number | Average wind speed observed throughout the day. |
| windGust   number | Maximum wind speed observed throughout the day. |
| speedUnit   string | Indicates the measurement unit of the `windSpeed` and `windGust`. |
| windBearing   number | Direction of the wind, in degrees. |
| hourlyWeather   array: object | Weather information for specific hours (07:00:00, 12:00:00, 16:00:00). |
| id   int | Unique identifier. |
| hour   string | Hour of the day for this forecast. |
| temp   number | Temperature during specified hour. |
| windSpeed   number | Average wind speed. |
| windBearing   int | Direction of the wind, in degrees. |
| humidity   number | A percentage value indicating the humidity. |
| fetchedAt   datetime: ISO 8601 | The date when weather was fetched from weather API. |
| createdAt   datetime: ISO 8601 | The date when weather was first fetched. |
| updatedAt   datetime: ISO 8601 | The date when the weather was last updated. |
| provider   enum:string | Indicates the source of the weather data. Possible values: `darksky`, `weatherkit` |
| customValues   array: object | For non-PDF forms, data stored in the form fields. |
| fieldId   string | The unique identifier of the field. |
| sectionLabel   string | Name of the section containing this field. |
| itemLabel   string | The field’s label or question text. |
| valueName   enum:string | Indicates the type of value used for this item. Possible values: `textVal`, `toggleVal`, `arrayVal`, `numberVal`, `choiceVal`, `dateVal`, `svgVal` |
| toggleVal   enum:string | A boolean like enum value. Possible values: `Yes`, `No`, `False`, `True`, `Minus`, `Plus`, `Fail`, `Pass`, `NA` |
| textVal   string | A text value. |
| arrayVal   string | Multi select values. |
| numberVal   number | A numeric value. |
| choiceVal   string | A single select value. |
| dateVal   string | A date value. |
| svgVal   string | A signature value (base64 encoded SVG). |
| notes   string | Text for the field’s notes section. <br>Max length: 8000 |
| lastReopenedBy   string | Unique identifier for the user that last re-opened the Form (if applicable). |
| lastSubmitterSignature   string | Signature of the reviewer who last submitted the Form (if applicable). Signature value (base64 encoded SVG). |
| userCreatedAt   datetime: ISO 8601 | Timestamp when the form was created on the client device or external system. This may differ from createdAt if the form was created offline and synced later. UTC date and time in ISO-8601 format. |
| createdAt   datetime: ISO 8601 | Timestamp when the form was received and stored on the server. UTC date and time in ISO-8601 format. |
