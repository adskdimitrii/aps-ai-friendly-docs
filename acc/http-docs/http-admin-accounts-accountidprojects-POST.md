# accounts/{accountId}/projects

Source: https://aps.autodesk.com/en/docs/acc/reference/http/admin-accounts-accountidprojects-POST/

---

accounts/:account_id/projects

POST

# accounts/{accountId}/projects

Creates a new project in the specified account. You can create the project directly, or clone it from a project template.

- When you create a project directly (not from a template), this endpoint automatically adds all of the products that are associated with the current account to the project and activates them.
- To clone the project from a template, provide the `template` object in the request to specify the project template ID. The products and settings in the template are copied to the new project, and the products associated with the current account are ignored.

Note that currently, a project that is cloned from a template *does not* have *any* project members assigned initially. You can assign all of the template project members to the project in bulk by calling [POST projects/:projectId/users](http-admin-projects-project-Id-users-POST.md) to assign a project administrator to the project. This administrator can be any user who is currently in the same account as the project. This triggers the automatic process of assigning the template project members to the cloned project and activating them.

You can also create a project template. Include the `classification` field in the request with a value of `template`, and set the value of the `type` field to `Template Project`. You must provide both of these values, otherwise the request returns a `400` error. Use the ACC Build UI to edit the template details and permissions, add project members to the template, and configure the template’s notification settings.

Note that you cannot create a project template from another project template, but you can base it on a production project. Set the value of the `template.projectId` field to the `id` of the production project. The new project template is not completely configured for use, but it will get you started.

For more information about creating projects, see the [Create and Configure Projects](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/admin/) tutorial.

Note that the `Authorization` header token can be obtained either via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow, or via a [two-legged](../../oauth/how-to-docs/get-2-legged-token.md) Oauth flow *with user impersonation*, for which the `User-Id` header is required.

Note that the `products` array is ignored in the request. However, the products in the project do appear in the response for this and other endpoints.

Note that this endpoint is not compatible with BIM 360 projects.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/construction/admin/v1/accounts/:accountId/projects |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `account:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type*   string | Must be `application/json` |
| Region   string | Specifies the region where your request should be routed. If not set, the request is routed automatically, which may result in a slight increase in latency. <br>Possible values: `US`, `EMEA`. For a complete list of supported regions, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page. |
| User-Id   string | The ID of a user on whose behalf your request is acting. <br>Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.<br>You can use either the user’s ACC ID (`id`), or their Autodesk ID (`autodeskId`).<br>Note that this header is required for Account Admin POST, PATCH, and DELETE endpoints if you want to use a 2-legged authentication context. This header is optional for Account Admin GET endpoints. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| accountId   string: UUID | The ID of the ACC account that contains the project being created or the projects being retrieved. This corresponds to the hub ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/). To convert a hub ID into an account ID, remove the “**b.**" prefix. For example, a hub ID of `b.c8b0c73d-3ae9` translates to an account ID of `c8b0c73d-3ae9`. |
| --- | --- |

### Request

## [Body Structure](#body-structure)

The `name` and `type` fields are required. All other fields are optional.

If you include the `project.template` object in the request, the new project’s products and settings will match those of the template project. If you exclude `project.template`, the endpoint automatically activates all of the products associated with the ACC platform for the new project.

Note that the `products` array is ignored in the request. However, it does appear in the response for endpoints that return it (including this endpoint).

Expand all

| name*   string | The name of the project. <br>Max length: 255 |
| --- | --- |
| startDate   null,string | The estimated start date for the project, in ISO 8601 format. |
| endDate   null,string | The estimated end date for the project, in ISO 8601 format. |
| type*   string | The type of the project. Any value is accepted, but the following are recommended: <br>Possible values: `Convention Center`, `Data Center`, `Hotel / Motel`, `Office`, `Parking Structure / Garage`, `Performing Arts`, `Restaurant`, `Retail`, `Stadium / Arena`, `Theme Park`, `Warehouse (non-manufacturing)`, `Assisted Living / Nursing Home`, `Hospital`, `Medical Laboratory`, `Medical Office`, `OutPatient Surgery Center`, `Court House`, `Dormitory`, `Education Facility`, `Government Building`, `Library`, `Military Facility`, `Museum`, `Prison / Correctional Facility`, `Recreation Building`, `Religious Building`, `Research Facility / Laboratory`, `Multi-Family Housing`, `Single-Family Housing`, `Airport`, `Bridge`, `Canal / Waterway`, `Dams / Flood Control / Reservoirs`, `Harbor / River Development`, `Rail`, `Seaport`, `Streets / Roads / Highways`, `Transportation Building`, `Tunnel`, `Waste Water / Sewers`, `Water Supply`, `Manufacturing / Factory`, `Mining Facility`, `Oil & Gas`, `Plant`, `Power Plant`, `Solar Farm`, `Utilities`, `Wind Farm`, `Demonstration Project`, `Template Project` and `Training Project`.<br>Max length: 255 |
| classification   enum:string | The classification of the project. Possible values: <br>`production` – Standard project.`template` – A project that serves as a template for creating new projects.`component` – A placeholder project containing reusable components (e.g., forms). Only one component project is allowed per account. Known as a library in the ACC UI.`sample` – A single sample project automatically created for ACC trials (limited to one per account). |
| projectValue   object | Contains details about the estimated cost of the project, including the amount (`value`) and the currency (`currency`). |
| value*   number | The estimated cost of the project, based on the `currency` specified in the currency field. Default: `0`. |
| currency*   enum:string | The currency of the project value. Default: `USD`. Possible values: `AED`, `AFN`, `ALL`, `AMD`, `ANG`, `AOA`, `ARS`, `AUD`, `AWG`, `AZN`, `BAM`, `BBD`, `BDT`, `BGN`, `BHD`, `BIF`, `BMD`, `BND`, `BOB`, `BOV`, `BRL`, `BSD`, `BTN`, `BWP`, `BYN`, `BYR`, `BZD`, `CAD`, `CDF`, `CHE`, `CHF`, `CHW`, `CLF`, `CLP`, `CNY`, `COP`, `COU`, `CRC`, `CUC`, `CUP`, `CVE`, `CZK`, `DJF`, `DKK`, `DOP`, `DZD`, `EEK`, `EGP`, `ERN`, `ETB`, `EUR`, `FJD`, `FKP`, `GBP`, `GEL`, `GHS`, `GIP`, `GMD`, `GNF`, `GTQ`, `GYD`, `HKD`, `HNL`, `HRK`, `HTG`, `HUF`, `IDR`, `ILS`, `INR`, `IQD`, `IRR`, `ISK`, `JMD`, `JOD`, `JPY`, `KES`, `KGS`, `KHR`, `KMF`, `KPW`, `KRW`, `KWD`, `KYD`, `KZT`, `LAK`, `LBP`, `LKR`, `LRD`, `LSL`, `LTL`, `LVL`, `LYD`, `MAD`, `MDL`, `MGA`, `MKD`, `MMK`, `MNT`, `MOP`, `MRU`, `MUR`, `MVR`, `MWK`, `MXN`, `MXV`, `MYR`, `MZN`, `NAD`, `NGN`, `NIO`, `NOK`, `NPR`, `NZD`, `OMR`, `PAB`, `PEN`, `PGK`, `PHP`, `PKR`, `PLN`, `PYG`, `QAR`, `RON`, `RSD`, `RUB`, `RWF`, `SAR`, `SBD`, `SCR`, `SDG`, `SEK`, `SGD`, `SHP`, `SLE`, `SLL`, `SOS`, `SRD`, `SSP`, `STN`, `SVC`, `SYP`, `SZL`, `THB`, `TJS`, `TMT`, `TND`, `TOP`, `TRL`, `TRY`, `TTD`, `TWD`, `TZS`, `UAH`, `UGX`, `USD`, `USN`, `UYI`, `UYU`, `UYW`, `UZS`, `VED`, `VES`, `VND`, `VUV`, `WST`, `XAF`, `XAG`, `XAU`, `XBA`, `XBB`, `XBC`, `XBD`, `XCD`, `XDR`, `XOF`, `XPD`, `XPF`, `XPT`, `XSU`, `XTS`, `XUA`, `XXX`, `YER`, `ZAR`, `ZMW`, `ZWL` |
| jobNumber   string | A user-defined identifier for the project. This value is assigned when the project is created and can be used to filter projects. It supports partial matches when used with `filterTextMatch`. <br>Max length: 100 |
| addressLine1   null,string | The first line of the project’s address. <br>Max length: 255 |
| addressLine2   null,string | Additional address details for the project location. <br>Max length: 255 |
| city   null,string | The city wher the project is located. <br>Max length: 255 |
| stateOrProvince   null,string | The state or province where the project is located. It must be a valid name or an ISO 3166-2 code. The provided state or province must exist in the country of the project. <br>Max length: 255 |
| postalCode   null,string | The postal or ZIP code of the project location. <br>Max length: 255 |
| country   null,string | The country where the project is located, using an ISO 3166-1 code. <br>Max length: 255 |
| latitude   null,string | The latitude coordinate of the project location. <br>Max length: 25 |
| longitude   null,string | The longitude coordinate of the project location. <br>Max length: 25 |
| timezone   null,string | The time zone where the project is located. It must be a valid IANA time zone name from the [IANA Time Zone Database](https://www.iana.org/time-zones) (e.g., `America/New_York`). If no time zone is set, this field may be `null`. Possible values: `Pacific/Honolulu`, `America/Juneau`, `America/Los_Angeles`, `America/Phoenix`, `America/Denver`, `America/Chicago`, `America/New_York`, `America/Indiana/Indianapolis`, `Pacific/Pago_Pago`, `Pacific/Midway`, `America/Tijuana`, `America/Chihuahua`, `America/Mazatlan`, `America/Guatemala`, `America/Mexico_City`, `America/Monterrey`, `America/Regina`, `America/Bogota`, `America/Lima`, `America/Caracas`, `America/Halifax`, `America/Guyana`, `America/La_Paz`, `America/Santiago`, `America/St_Johns`, `America/Sao_Paulo`, `America/Argentina/Buenos_Aires`, `America/Godthab`, `Atlantic/South_Georgia`, `Atlantic/Azores`, `Atlantic/Cape_Verde`, `Africa/Casablanca`, `Europe/Dublin`, `Europe/Lisbon`, `Europe/London`, `Africa/Monrovia`, `Etc/UTC`, `Europe/Amsterdam`, `Europe/Belgrade`, `Europe/Berlin`, `Europe/Bratislava`, `Europe/Brussels`, `Europe/Budapest`, `Europe/Copenhagen`, `Europe/Ljubljana`, `Europe/Madrid`, `Europe/Paris`, `Europe/Prague`, `Europe/Rome`, `Europe/Sarajevo`, `Europe/Skopje`, `Europe/Stockholm`, `Europe/Vienna`, `Europe/Warsaw`, `Africa/Algiers`, `Europe/Zagreb`, `Europe/Athens`, `Europe/Bucharest`, `Africa/Cairo`, `Africa/Harare`, `Europe/Helsinki`, `Europe/Istanbul`, `Asia/Jerusalem`, `Europe/Kiev`, `Africa/Johannesburg`, `Europe/Riga`, `Europe/Sofia`, `Europe/Tallinn`, `Europe/Vilnius`, `Asia/Baghdad`, `Asia/Kuwait`, `Europe/Minsk`, `Africa/Nairobi`, `Asia/Riyadh`, `Asia/Tehran`, `Asia/Muscat`, `Asia/Baku`, `Europe/Moscow`, `Asia/Tbilisi`, `Asia/Yerevan`, `Asia/Kabul`, `Asia/Karachi`, `Asia/Tashkent`, `Asia/Kolkata`, `Asia/Colombo`, `Asia/Kathmandu`, `Asia/Almaty`, `Asia/Dhaka`, `Asia/Yekaterinburg`, `Asia/Rangoon`, `Asia/Bangkok`, `Asia/Jakarta`, `Asia/Novosibirsk`, `Asia/Shanghai`, `Asia/Chongqing`, `Asia/Hong_Kong`, `Asia/Krasnoyarsk`, `Asia/Kuala_Lumpur`, `Australia/Perth`, `Asia/Singapore`, `Asia/Taipei`, `Asia/Ulaanbaatar`, `Asia/Urumqi`, `Asia/Irkutsk`, `Asia/Tokyo`, `Asia/Seoul`, `Australia/Adelaide`, `Australia/Darwin`, `Australia/Brisbane`, `Australia/Melbourne`, `Pacific/Guam`, `Australia/Hobart`, `Pacific/Port_Moresby`, `Australia/Sydney`, `Asia/Yakutsk`, `Pacific/Noumea`, `Asia/Vladivostok`, `Pacific/Auckland`, `Pacific/Fiji`, `Asia/Kamchatka`, `Asia/Magadan`, `Pacific/Majuro`, `Pacific/Guadalcanal`, `Pacific/Tongatapu`, `Pacific/Apia`, `Pacific/Fakaofo` |
| constructionType   string | The type of construction for the project. Recommended values: `New Construction`, `Renovation`. Any value is accepted. |
| deliveryMethod   string | The method used to deliver the project. Recommended values include `Design-Bid-Build`, `Construction Management (CM) at Risk`, and `Integrated Project Delivery (IPD)`. Any value is accepted. |
| contractType   string | The type of contract for the project. For example, `Lump Sum`, `Cost Plus`, `Guaranteed Maximum Price`, `Unit Price`. Any value is accepted. |
| currentPhase   string | The current phase of the project. Recommended values include, `Concept`, `Design`, `Bidding`, `Planning`, `Preconstruction`, `Construction`, `Commissioning`, `Warranty`, `Complete`, `Facility Management`, `Operation`, `Strategic Definition`, `Preparation and Brief`, `Concept Design`, `Developed Design`, `Technical Design`, `Construction`, `Handover and Close Out` and `In Use`. <br>Any value is accepted. |
| businessUnitId   string: UUID | The ID of the business unit that the project is associated with. |
| sheetCount   null,integer | The total number of sheets associated with the project. <br>Note that this field is relevant only in responses. It is ignored in requests. |
| platform   enum:string | The APS platform where the project is stored. Possible values: `acc`, `bim360`. <br>Note that this field is relevant only in responses. It is ignored in requests. |
| companyCount   int | The total number of companies associated with the project. <br>Note that this field is relevant only in responses. It is ignored in requests. |
| memberCount   int | The total number of members on the project. <br>Note that this field is relevant only in responses. It is ignored in requests. |
| template   object | Information about a project in the current user’s account that is configured as a template from which to copy products and settings when creating a new project: <br>If you *include* this object in a [POST accounts/:accountId/projects](https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-accountsaccountidprojects-POST/) request, the cloned project’s products and settings will match those of the template project.If you *omit* this object from a [POST accounts/:accountId/projects](https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-accountsaccountidprojects-POST/) request, all of the current ACC account’s products are added to the cloned project and activated. |
| projectId*   string: UUID | The ID of a project template in the current ACC account from which to clone the new project and copy products and settings. <br>Note that you cannot create a project template from another project template, but you can base it on a production project. Set this field to the project `id` of the production project. The new project template is not completely configured for use, but it will get you started.<br>For more information about project templates, see [Project Templates](https://help.autodesk.com/view/BUILD/ENU/?guid=Account_Admin_Project_Templates) in the Build help. |
| options   object | Information about what to include when cloning a project template. |
| field   object | Project template options specific to classic field. |
| includeCompanies   boolean | Indicates whether to include company data when copying from the project template. <br>`true`: Include company data.`false`: Exclude company data. |
| includeLocations   boolean | Indicates whether to include location data when copying from the project template. <br>`true`: Include location data.`false`: Exclude location data. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 202   Accepted | APS has received the request but not yet completed it. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax. |
| 401   Unauthorized | Request has not been applied because it lacks valid authentication credentials for the target resource. |
| 403   Forbidden | The server understood the request but refuses to authorize it. |
| 404   Not Found | The resource could not be found. |
| 410 | Access to the target resource is no longer available. |
| 415 | The server refuses to accept the request because the payload format is in an unsupported format. |
| 429   Too Many Requests | User has sent too many requests in a given amount of time. |
| 500   Internal Server Error | An unexpected error occurred on the server. |
| 503   Service Unavailable | Server is not ready to handle the request. |

### Response

## [Body Structure (202)](#body-structure-202)

Expand all

| id   string: UUID | The internally generated ID for the project. |
| --- | --- |
| name   string | The name of the project. <br>Max length: 255 |
| startDate   null,string | The estimated start date for the project, in ISO 8601 format. |
| endDate   null,string | The estimated end date for the project, in ISO 8601 format. |
| type   string | The type of the project. Any value is accepted, but the following are recommended: <br>Possible values: `Convention Center`, `Data Center`, `Hotel / Motel`, `Office`, `Parking Structure / Garage`, `Performing Arts`, `Restaurant`, `Retail`, `Stadium / Arena`, `Theme Park`, `Warehouse (non-manufacturing)`, `Assisted Living / Nursing Home`, `Hospital`, `Medical Laboratory`, `Medical Office`, `OutPatient Surgery Center`, `Court House`, `Dormitory`, `Education Facility`, `Government Building`, `Library`, `Military Facility`, `Museum`, `Prison / Correctional Facility`, `Recreation Building`, `Religious Building`, `Research Facility / Laboratory`, `Multi-Family Housing`, `Single-Family Housing`, `Airport`, `Bridge`, `Canal / Waterway`, `Dams / Flood Control / Reservoirs`, `Harbor / River Development`, `Rail`, `Seaport`, `Streets / Roads / Highways`, `Transportation Building`, `Tunnel`, `Waste Water / Sewers`, `Water Supply`, `Manufacturing / Factory`, `Mining Facility`, `Oil & Gas`, `Plant`, `Power Plant`, `Solar Farm`, `Utilities`, `Wind Farm`, `Demonstration Project`, `Template Project` and `Training Project`.<br>Max length: 255 |
| classification   enum:string | The classification of the project. Possible values: <br>`production` – Standard project.`template` – A project that serves as a template for creating new projects.`component` – A placeholder project containing reusable components (e.g., forms). Only one component project is allowed per account. Known as a library in the ACC UI.`sample` – A single sample project automatically created for ACC trials (limited to one per account). |
| projectValue   object | Contains details about the estimated cost of the project, including the amount (`value`) and the currency (`currency`). |
| value   number | The estimated cost of the project, based on the `currency` specified in the currency field. Default: `0`. |
| currency   enum:string | The currency of the project value. Default: `USD`. Possible values: `AED`, `AFN`, `ALL`, `AMD`, `ANG`, `AOA`, `ARS`, `AUD`, `AWG`, `AZN`, `BAM`, `BBD`, `BDT`, `BGN`, `BHD`, `BIF`, `BMD`, `BND`, `BOB`, `BOV`, `BRL`, `BSD`, `BTN`, `BWP`, `BYN`, `BYR`, `BZD`, `CAD`, `CDF`, `CHE`, `CHF`, `CHW`, `CLF`, `CLP`, `CNY`, `COP`, `COU`, `CRC`, `CUC`, `CUP`, `CVE`, `CZK`, `DJF`, `DKK`, `DOP`, `DZD`, `EEK`, `EGP`, `ERN`, `ETB`, `EUR`, `FJD`, `FKP`, `GBP`, `GEL`, `GHS`, `GIP`, `GMD`, `GNF`, `GTQ`, `GYD`, `HKD`, `HNL`, `HRK`, `HTG`, `HUF`, `IDR`, `ILS`, `INR`, `IQD`, `IRR`, `ISK`, `JMD`, `JOD`, `JPY`, `KES`, `KGS`, `KHR`, `KMF`, `KPW`, `KRW`, `KWD`, `KYD`, `KZT`, `LAK`, `LBP`, `LKR`, `LRD`, `LSL`, `LTL`, `LVL`, `LYD`, `MAD`, `MDL`, `MGA`, `MKD`, `MMK`, `MNT`, `MOP`, `MRU`, `MUR`, `MVR`, `MWK`, `MXN`, `MXV`, `MYR`, `MZN`, `NAD`, `NGN`, `NIO`, `NOK`, `NPR`, `NZD`, `OMR`, `PAB`, `PEN`, `PGK`, `PHP`, `PKR`, `PLN`, `PYG`, `QAR`, `RON`, `RSD`, `RUB`, `RWF`, `SAR`, `SBD`, `SCR`, `SDG`, `SEK`, `SGD`, `SHP`, `SLE`, `SLL`, `SOS`, `SRD`, `SSP`, `STN`, `SVC`, `SYP`, `SZL`, `THB`, `TJS`, `TMT`, `TND`, `TOP`, `TRL`, `TRY`, `TTD`, `TWD`, `TZS`, `UAH`, `UGX`, `USD`, `USN`, `UYI`, `UYU`, `UYW`, `UZS`, `VED`, `VES`, `VND`, `VUV`, `WST`, `XAF`, `XAG`, `XAU`, `XBA`, `XBB`, `XBC`, `XBD`, `XCD`, `XDR`, `XOF`, `XPD`, `XPF`, `XPT`, `XSU`, `XTS`, `XUA`, `XXX`, `YER`, `ZAR`, `ZMW`, `ZWL` |
| status   enum:string | The status of the project. <br>Possible values: `active`, `pending`, `archived` and `suspended`. |
| jobNumber   string | A user-defined identifier for the project. This value is assigned when the project is created and can be used to filter projects. It supports partial matches when used with `filterTextMatch`. <br>Max length: 100 |
| addressLine1   null,string | The first line of the project’s address. <br>Max length: 255 |
| addressLine2   null,string | Additional address details for the project location. <br>Max length: 255 |
| city   null,string | The city wher the project is located. <br>Max length: 255 |
| stateOrProvince   null,string | The state or province where the project is located. It must be a valid name or an ISO 3166-2 code. The provided state or province must exist in the country of the project. <br>Max length: 255 |
| postalCode   null,string | The postal or ZIP code of the project location. <br>Max length: 255 |
| country   null,string | The country where the project is located, using an ISO 3166-1 code. <br>Max length: 255 |
| latitude   null,string | The latitude coordinate of the project location. <br>Max length: 25 |
| longitude   null,string | The longitude coordinate of the project location. <br>Max length: 25 |
| timezone   null,string | The time zone where the project is located. It must be a valid IANA time zone name from the [IANA Time Zone Database](https://www.iana.org/time-zones) (e.g., `America/New_York`). If no time zone is set, this field may be `null`. Possible values: `Pacific/Honolulu`, `America/Juneau`, `America/Los_Angeles`, `America/Phoenix`, `America/Denver`, `America/Chicago`, `America/New_York`, `America/Indiana/Indianapolis`, `Pacific/Pago_Pago`, `Pacific/Midway`, `America/Tijuana`, `America/Chihuahua`, `America/Mazatlan`, `America/Guatemala`, `America/Mexico_City`, `America/Monterrey`, `America/Regina`, `America/Bogota`, `America/Lima`, `America/Caracas`, `America/Halifax`, `America/Guyana`, `America/La_Paz`, `America/Santiago`, `America/St_Johns`, `America/Sao_Paulo`, `America/Argentina/Buenos_Aires`, `America/Godthab`, `Atlantic/South_Georgia`, `Atlantic/Azores`, `Atlantic/Cape_Verde`, `Africa/Casablanca`, `Europe/Dublin`, `Europe/Lisbon`, `Europe/London`, `Africa/Monrovia`, `Etc/UTC`, `Europe/Amsterdam`, `Europe/Belgrade`, `Europe/Berlin`, `Europe/Bratislava`, `Europe/Brussels`, `Europe/Budapest`, `Europe/Copenhagen`, `Europe/Ljubljana`, `Europe/Madrid`, `Europe/Paris`, `Europe/Prague`, `Europe/Rome`, `Europe/Sarajevo`, `Europe/Skopje`, `Europe/Stockholm`, `Europe/Vienna`, `Europe/Warsaw`, `Africa/Algiers`, `Europe/Zagreb`, `Europe/Athens`, `Europe/Bucharest`, `Africa/Cairo`, `Africa/Harare`, `Europe/Helsinki`, `Europe/Istanbul`, `Asia/Jerusalem`, `Europe/Kiev`, `Africa/Johannesburg`, `Europe/Riga`, `Europe/Sofia`, `Europe/Tallinn`, `Europe/Vilnius`, `Asia/Baghdad`, `Asia/Kuwait`, `Europe/Minsk`, `Africa/Nairobi`, `Asia/Riyadh`, `Asia/Tehran`, `Asia/Muscat`, `Asia/Baku`, `Europe/Moscow`, `Asia/Tbilisi`, `Asia/Yerevan`, `Asia/Kabul`, `Asia/Karachi`, `Asia/Tashkent`, `Asia/Kolkata`, `Asia/Colombo`, `Asia/Kathmandu`, `Asia/Almaty`, `Asia/Dhaka`, `Asia/Yekaterinburg`, `Asia/Rangoon`, `Asia/Bangkok`, `Asia/Jakarta`, `Asia/Novosibirsk`, `Asia/Shanghai`, `Asia/Chongqing`, `Asia/Hong_Kong`, `Asia/Krasnoyarsk`, `Asia/Kuala_Lumpur`, `Australia/Perth`, `Asia/Singapore`, `Asia/Taipei`, `Asia/Ulaanbaatar`, `Asia/Urumqi`, `Asia/Irkutsk`, `Asia/Tokyo`, `Asia/Seoul`, `Australia/Adelaide`, `Australia/Darwin`, `Australia/Brisbane`, `Australia/Melbourne`, `Pacific/Guam`, `Australia/Hobart`, `Pacific/Port_Moresby`, `Australia/Sydney`, `Asia/Yakutsk`, `Pacific/Noumea`, `Asia/Vladivostok`, `Pacific/Auckland`, `Pacific/Fiji`, `Asia/Kamchatka`, `Asia/Magadan`, `Pacific/Majuro`, `Pacific/Guadalcanal`, `Pacific/Tongatapu`, `Pacific/Apia`, `Pacific/Fakaofo` |
| constructionType   string | The type of construction for the project. Recommended values: `New Construction`, `Renovation`. Any value is accepted. |
| deliveryMethod   string | The method used to deliver the project. Recommended values include `Design-Bid-Build`, `Construction Management (CM) at Risk`, and `Integrated Project Delivery (IPD)`. Any value is accepted. |
| contractType   string | The type of contract for the project. For example, `Lump Sum`, `Cost Plus`, `Guaranteed Maximum Price`, `Unit Price`. Any value is accepted. |
| currentPhase   string | The current phase of the project. Recommended values include, `Concept`, `Design`, `Bidding`, `Planning`, `Preconstruction`, `Construction`, `Commissioning`, `Warranty`, `Complete`, `Facility Management`, `Operation`, `Strategic Definition`, `Preparation and Brief`, `Concept Design`, `Developed Design`, `Technical Design`, `Construction`, `Handover and Close Out` and `In Use`. <br>Any value is accepted. |
| businessUnitId   string: UUID | The ID of the business unit that the project is associated with. |
| lastSignIn   datetime: ISO 8601 | The timestamp of the last time someone signed into the project. |
| imageUrl   string | The URL of the main image associated with the project. This field can be `null`. <br>Max length: 255 |
| thumbnailImageUrl   string | The URL of the project’s thumbnail image. This field can be `null`. <br>Max length: 255 |
| createdAt   datetime: ISO 8601 | The timestamp when the project was created, in ISO 8601 format. This value is set at creation and does not change. |
| updatedAt   datetime: ISO 8601 | The timestamp when the project was last updated, in ISO 8601 format. This reflects changes to project fields but not updates to resources within the project. |
| memberGroupId   string | Not relevant <br>Max length: 25 |
| adminGroupId   string | Not relevant <br>Max length: 25 |
| accountId   string: UUID | The account ID associated with the project. |
| sheetCount   null,integer | The total number of sheets associated with the project. <br>Note that this field is relevant only in responses. It is ignored in requests. |
| products   array | An array of the product objects associated with the project. <br>Note that this array is relevant only in responses. It is ignored in requests.<br>When a project is created, every product in the same account as the project is activated for the project. You can call [PATCH users/:userId](https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-projects-projectId-users-userId-PATCH/) to separately activate one or more of the returned products for each user assigned to the project. |
| key   enum:string | A machine-readable identifier for the product (e.g., docs, build). <br>Each product has a unique key used throughout the API for identification, filtering, and integration logic (e.g., in query parameters like `filter[key]`).<br>Possible values: ACC - `autoSpecs`, `build`, `cost`, `designCollaboration`, `docs`, `insight`, `modelCoordination`, `projectAdministration`, and `takeoff`.<br>BIM 360 - `assets`, `costManagement`, `designCollaboration`, `documentManagement`, `field`, `fieldManagement`, `glue`, `insight`, `modelCoordination`, `plan`, `projectAdministration`, `projectHome`, `projectManagement`, and `quantification`.<br>Note that this endpoint returns only ACC products. Other endpoints, such as [GET projects](https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-accountsaccountidprojects-GET/) and [GET projects/:projectId](https://aps.autodesk.com/en/docs/acc/v1/reference/http/admin-projects-projectId-GET/), may return both ACC and BIM 360 projects. In those responses, product keys may include BIM 360 values. |
| icon   string | The URL of the icon associated with the product. |
| name   string | The name of the product. |
| language   enum:string | The language for the project. Only valid for the `field` product. Possible values: `en`, `de`, `nl`, `zh`, `de-CH` |
| status   enum:string | The current status of the product. Possible values: <br>`activating`: Product activation is in progress.`activationFailed`: Product activation has failed.`active`: Product activation is completed.`deactivating`: Product deactivation is in progress. (Applicable to BIM 360 only)`deactivationFailed`: Product deactivation has failed. (Applicable to BIM 360 only)`inactive`: Product deactivation is completed. (Applicable to BIM 360 only)`available`: Product is available for activation. (Applicable to BIM 360 only) |
| platform   enum:string | The APS platform where the project is stored. Possible values: `acc`, `bim360`. <br>Note that this field is relevant only in responses. It is ignored in requests. |
| companyCount   int | The total number of companies associated with the project. <br>Note that this field is relevant only in responses. It is ignored in requests. |
| memberCount   int | The total number of members on the project. <br>Note that this field is relevant only in responses. It is ignored in requests. |
| templateId   string: UUID | The ID of the project that was used as a template to create this project. |
| jobId   string: UUID | Not relevant - we don’t currently support this field. |

## [Example](#example)

APS has received the request but not yet completed it.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/admin/v1/accounts/d73fc742-4538-401c-8d0f-853b49b750b2/projects' \
  -X 'POST' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": "Sample Project",
        "classification": "production",
        "startDate": "2010-01-01",
        "endDate": "2015-12-31",
        "type": "Hospital",
        "projectValue": {
          "value": 1650000,
          "currency": "USD"
        },
        "jobNumber": "HP-0002",
        "addressLine1": "123 Main Street",
        "addressLine2": "Suite 2",
        "city": "San Francisco",
        "stateOrProvince": "California",
        "postalCode": "94001",
        "country": "United States",
        "latitude": "37.773972",
        "longitude": "-122.431297",
        "timezone": "America/Los_Angeles",
        "constructionType": "New Construction",
        "deliveryMethod": "Unit Price",
        "currentPhase": "Design",
        "businessUnitId": "802a4a61-3507-4d4e-8e3c-242a31cc0549",
        "products": [
          {
            "key": "docs"
          },
          {
            "key": "build"
          }
        ]
      }'

```

Show More

### Response

```
{
  "id": "3e354e66-ac8b-41dd-9bc1-93fc182c25dd",
  "name": "Sample Project",
  "startDate": "2010-01-01",
  "endDate": "2015-12-31",
  "type": "Hospital",
  "classification": "production",
  "projectValue": {
    "value": 1650000,
    "currency": "USD"
  },
  "status": "active",
  "jobNumber": "HP-0002",
  "addressLine1": "123 Main Street",
  "addressLine2": "Suite 2",
  "city": "San Francisco",
  "stateOrProvince": "California",
  "postalCode": "94001",
  "country": "United States",
  "latitude": "37.773972",
  "longitude": "-122.431297",
  "timezone": "America/Los_Angeles",
  "constructionType": "New Construction",
  "deliveryMethod": "Design-Bid",
  "contractType": "Unit Price",
  "currentPhase": "Design",
  "businessUnitId": "802a4a61-3507-4d4e-8e3c-242a31cc0549",
  "lastSignIn": "2019-01-01T12:45:00.000Z",
  "imageUrl": "https://s3.us-east-1.amazonaws.com/project_image.png",
  "thumbnailImageUrl": "https://s3.us-east-1.amazonaws.com/project_thumbnail_image.png",
  "createdAt": "2018-01-01T12:45:00.000Z",
  "updatedAt": "2019-01-01T12:45:00.000Z",
  "memberGroupId": "3456542",
  "adminGroupId": "3456543",
  "accountId": "d73fc742-4538-401c-8d0f-853b49b750b2",
  "sheetCount": 512,
  "products": [
    {
      "key": "docs",
      "status": "active",
      "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/docs.svg",
      "name": "Docs",
      "language": "en"
    },
    {
      "key": "designCollaboration",
      "status": "activating",
      "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/dc.svg",
      "name": "Design Collaboration",
      "language": "en"
    },
    {
      "key": "modelCoordination",
      "status": "activating",
      "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/model.svg",
      "name": "Model Coordination",
      "language": "en"
    },
    {
      "key": "takeoff",
      "status": "activating",
      "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/quantify.svg",
      "name": "Takeoff",
      "language": "en"
    },
    {
      "key": "autoSpecs",
      "status": "activating",
      "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/tools/autospecs.svg",
      "name": "AutoSpecs",
      "language": "en"
    },
    {
      "key": "build",
      "status": "activating",
      "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/build.svg",
      "name": "Build",
      "language": "en"
    },
    {
      "key": "cost",
      "status": "activating",
      "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/cost.svg",
      "name": "Cost Management",
      "language": "en"
    },
    {
      "key": "insight",
      "status": "activating",
      "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/insight.svg",
      "name": "Insight",
      "language": "en"
    },
    {
      "key": "projectAdministration",
      "status": "activating",
      "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/tools/settings.svg",
      "name": "Project Admin",
      "language": "en"
    },
    {
      "key": "accountAdministration",
      "status": "activating",
      "icon": "hhttps://bim360-ea-ue1-prod-storage.s3.amazonaws.com/tools/settings.svg",
      "name": "Account Admin",
      "language": "en"
    }
  ],
  "platform": "acc",
  "companyCount": 10,
  "memberCount": 100,
  "templateId": null,
  "jobId": "5d3bc131-c0dc-4222-9a2a-351363f437fa"
}

```

Show More
