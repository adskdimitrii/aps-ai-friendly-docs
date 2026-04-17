# v1/projects/{projectId}/forms

Source: https://aps.autodesk.com/en/docs/acc/reference/http/forms-forms-(Deprecated)-GET/

---

Forms

GET

# v1/projects/{projectId}/forms

Deprecated

Returns a paginated list of forms in a project. Forms are sorted by updatedAt in ascending order by default (oldest first).

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). <br>The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| projectId   string | The ID of the project. <br>Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the Forma API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| offset   int | The number of records to skip before returning the result records. Defaults to 0. Increase this value in subsequent requests to continue getting results when the number of records exceeds the requested limit. |
| --- | --- |
| limit   int | The number of records to return in a single request. Can be a number between 1 and 50. Defaults to 50. |
| ids   array: string | An array of Form IDs to retrieve. |
| formDateMin   string | Return Forms with formDate at or after specified date. |
| formDateMax   string | Return Forms with formDate at or before specified date. |
| updatedAfter   datetime: ISO 8601 | Return Forms updated after a specified time. |
| updatedBefore   datetime: ISO 8601 | Return Forms updated before a specified time. |
| templateId   string | Return Forms on template with given ID. |
| statuses   array: string | Return Forms with given statuses. |
| sortBy   string | Return Forms sorted by specified attribute. |
| sortOrder   string | Return Forms in specified sorted order. |
| locationIds   array: string | A sequence of location IDs. Each returned object must be associated with one of the locations specified by the IDs. For example, ?locationId=123e102a-36de-14e7-8c56-1b1234ccbba8&locationId=cee45678-fcc4-43ae-80a2-8ca819dfa70d. See the usage example in the [Retrieve Forms Associated With Locations](../how-to-docs/forms-retrieve-forms-based-on-locations.md) tutorial. |
| includeInactiveFormTemplates   boolean | Set this value to true in order to include forms that were created using inactive form templates. Defaults to false. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Forms in project at specified page. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request header |
| 401   Unauthorized | The request was not accepted because it lacked valid authentication credentials |
| 403   Forbidden | The request was not accepted because the client is authenticated, but is not authorized to access the target resource |
| 404   Not Found | The resource cannot be found |
| 429   Too Many Requests | The request could not be completed due to the rate limit of the target resource |
| 500   Internal Server Error | The request could not be completed due to an internal server error |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| data   array: object | List of forms in the project. |
| --- | --- |
| status   enum:string | The current status of the form. Note that forms are created in `draft` status. Possible values: <br>`draft`: you can edit forms.<br>`inReview`: you cannot edit forms, however, they can be approved by form reviewers.<br>`submitted`: forms are closed and no longer editable.<br>`archived` forms are not edtiable and hidden in the UI. |
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
| pagination   object | Request pagination information. |
| offset   int | Number of items skipped. |
| limit   int | Number of items returned per page. |
| totalResults   int | Total number of items that can be returned. |
| nextUrl   string | URL for the next page of items. Next page url is null on the last page. |
