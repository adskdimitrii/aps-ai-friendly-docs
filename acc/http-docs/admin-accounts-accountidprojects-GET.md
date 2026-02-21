# accounts/{accountId}/projects

Source: https://aps.autodesk.com/en/docs/acc/reference/http/admin-accounts-accountidprojects-GET/

---

accounts/:account_id/projects

GET

# accounts/{accountId}/projects

Retrieves a list of the projects in the specified account. If the user is an account admin or executive then all projects are returned; otherwise only projects that the user is assigned to are returned.

You can also use this endpoint to retrieve a list of project templates by setting the `filter[classification]` parameter to `template` or the `filter[type]` parameter to `Template Project`.

  Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/admin/v1/accounts/:accountId/projects |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `account:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via either a [two-legged](/en/docs/oauth/v2/tutorials/get-2-legged-token) or [three-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token) OAuth flow. |
| --- | --- |
| Region   string | Specifies the region where your request should be routed. If not set, the request is routed automatically, which may result in a slight increase in latency. <br>Possible values: `US`, `EMEA`. For a complete list of supported regions, see the [Regions](/en/docs/acc/v1/overview/acc-regions/) page. |
| User-Id   string | The ID of a user on whose behalf your request is acting. <br>Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.<br>You can use either the userâs ACC ID (`id`), or their Autodesk ID (`autodeskId`).<br>Note that this header is required for Account Admin POST, PATCH, and DELETE endpoints if you want to use a 2-legged authentication context. This header is optional for Account Admin GET endpoints. |

* Required

### Request

## [URI Parameters](#uri-parameters)

| accountId   string: UUID | The ID of the ACC account that contains the project being created or the projects being retrieved. This corresponds to the hub ID in the [Data Management API](/en/docs/data/v2/). To convert a hub ID into an account ID, remove the â**b.**" prefix. For example, a hub ID of `b.c8b0c73d-3ae9` translates to an account ID of `c8b0c73d-3ae9`. |
| --- | --- |

### Request

## [Query String Parameters](#query-string-parameters)

| fields   array: string | A comma-separated list of the project fields to include in the response. Default value: all fields. <br>Possible values: `accountId`, `addressLine1`, `addressLine2`, `businessUnitId`, `city`, `companyCount`, `constructionType`, `country`, `createdAt`, `deliveryMethod`, `endDate`, `imageUrl`, `jobNumber`, `lastSignIn`, `latitude`, `longitude`, `memberCount`, `name`, `platform`, `postalCode`, `products`, `projectValue`, `sheetCount`, `startDate`, `stateOrProvince`, `status`, `thumbnailImageUrl`, `timezone`, `type` and `updatedAt`. |
| --- | --- |
| filter[classification]   array: string | Filters projects by classification. Possible values: <br>`production` â Standard production projects. `template` â Project templates that can be cloned to create production projects. `component` â Placeholder projects that contain standardized components (e.g., forms) for use across projects. Only one component project is permitted per account. Known as a library in the ACC unified products UI. `sample` â The single sample project automatically created upon ACC trial setup. Only one sample project is permitted per account.<br>Max length: 255 |
| filter[platform]   array: string | Filters by platform. Possible values: `acc` (Autodesk Construction Cloud) and `bim360` (BIM 360). <br>Max length: 255 |
| filter[products]   array: string | A comma-separated list of the products that the returned projects must use. Only projects that use one or more of the listed products are returned. <br>Note that every product that can be used in a project on the same platform (ACC or BIM 360) is activated for the project. All products associated with the project are returned in the response.<br>Some products are exclusive to ACC or to BIM 360, others are available on both platforms. Specify only the products on the appropriate platform for the projects you want to retrieve.<br>Possible ACC values: `accountAdministration`, `autoSpecs`, `build`, `buildingConnected`, `capitalPlanning`, `cloudWorksharing`, `cost`, `designCollaboration`, `docs`, `financials`, `insight`, `modelCoordination`, `projectAdministration`, `takeoff`, and `workshopxr`.<br>Possible BIM 360 values: `accountAdministration`, `assets`, `cloudWorksharing`, `costManagement`, `designCollaboration`, `documentManagement`, `field`, `fieldManagement`, `glue`, `insight`, `modelCoordination`, `plan`, `projectAdministration`, `projectHome`, `projectManagement`, and `quantification`. |
| filter[name]   string | Filters projects by name. Supports partial matches when used with `filterTextMatch`. For example `filter[name]=ABCco&filterTextMatch=startsWith` returns projects whose names start with âABCcoâ. <br>Max length: 255 |
| filter[type]   array: string | Filters by project type. To exclude a type, prefix it with `-` (e.g., `-Bridge` excludes bridge projects). <br>Possible values: `Airport`, `Assisted Living / Nursing Home`, `Bridge`, `Canal / Waterway`, `Convention Center`, `Court House`, `Data Center`, `Dams / Flood Control / Reservoirs`, `Demonstration Project`, `Dormitory`, `Education Facility`, `Government Building`, `Harbor / River Development`, `Hospital`, `Hotel / Motel`, `Library`, `Manufacturing / Factory`, `Medical Laboratory`, `Medical Office`, `Military Facility`, `Mining Facility`, `Multi-Family Housing`, `Museum`, `Oil & Gas`,``Plant``, `Office`, `OutPatient Surgery Center`, `Parking Structure / Garage`, `Performing Arts`, `Power Plant`, `Prison / Correctional Facility`, `Rail`, `Recreation Building`, `Religious Building`, `Research Facility / Laboratory`, `Restaurant`, `Retail`, `Seaport`, `Single-Family Housing`, `Solar Farm`, `Stadium/Arena`, `Streets / Roads / Highways`, `Template Project`, `Theme Park`, `Training Project`, `Transportation Building`, `Tunnel`, `Utilities`, `Warehouse (non-manufacturing)`, `Waste Water / Sewers`, `Water Supply`, `Wind Farm`. |
| filter[status]   array: string | Filters projects by status. Possible values: `active`, `pending`, `archived`, `suspended`. |
| filter[businessUnitId]   string: UUID | The ID of the business unit that returned projects must be associated with. <br>Note that you can obtain this ID value by calling the [GET business_units_structure](/en/docs/acc/v1/reference/http/business_units_structure-GET/) endpoint to retrieve a list of business units. Use the `id` field of the returned business unit that you want to filter by.<br>Max length: 255 |
| filter[jobNumber]   string | Filters by a user-defined project identifier. Supports partial matches when used with `filterTextMatch`. For example, `filter[jobNumber]=HP-0002&filterTextMatch=equals` returns projects where the job number is exactly âHP-0002â. <br>Max length: 255 |
| filter[updatedAt]   string | Filters projects updated within a specific date range in ISO 8601 format. For example: <br>Date range: `2023-03-02T00:00:00.000Z..2023-03-03T23:59:59 .999Z` Specific start date: `2023-03-02T00:00:00.000Z..` Specific end date: `..2023-03-02T23:59:59.999Z`<br>For more details, see [JSON API Filtering](https://jsonapi.org/format/#fetching-filtering).<br>Max length: 100 |
| filterTextMatch   enum:string | Specifies how text-based filters should match values in supported fields. <br>This parameter can be used in any endpoint that supports text-based filtering (e.g., `filter[name]`, `filter[jobNumber]`, `filter[companyName]`, etc.).<br>Possible values:<br>`contains` (default) â Matches if the field contains the specified text anywhere<br>`startsWith` â Matches if the field starts with the specified text<br>`endsWith` â Matches if the field ends with the specified text<br>`equals` â Matches only if the field exactly matches the specified text<br>Matching is case-insensitive.<br>Wildcards and regular expressions are not supported. |
| sort   array: string | Sorts results by specified fields. Multiple fields can be used in order of priority. Each field can be followed by `asc` (ascending) or `desc` (descending). Default: `asc`. <br>For example, `sort=name,createdAt desc` sorts projects by name, then by creation date (newest first).<br>Possible values: `name` (the default), `startDate`, `endDate`, `type`, `status`, `jobNumber`, `constructionType`, `deliveryMethod`, `contractType`, `currentPhase`, `companyCount`, `memberCount`, `createdAt` and `updatedAt`. |
| limit   int | The maximum number of records to return in the response. <br>Default: `20`<br>Minimum: `1`<br>Maximum: `200` (If a larger value is provided, only 200 records are returned) |
| offset   int | The index of the first record to return. <br>Used for pagination in combination with the `limit` parameter.<br>Example: `limit=20` and `offset=40` returns records 41â60. |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | A list of requested projects. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax. |
| 401   Unauthorized | Request has not been applied because it lacks valid authentication credentials for the target resource. |
| 403   Forbidden | The server understood the request but refuses to authorize it. |
| 404   Not Found | The resource could not be found. |
| 406   Not Acceptable | The server cannot produce a response matching the list of acceptable values defined in the request. |
| 410 | Access to the target resource is no longer available. |
| 429   Too Many Requests | User has sent too many requests in a given amount of time. |
| 500   Internal Server Error | An unexpected error occurred on the server. |
| 503   Service Unavailable | Server is not ready to handle the request. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| pagination   object | Contains pagination details for the records returned by the endpoint. |
| --- | --- |
| limit   int | The maximum number of records returned per page. The last page may contain fewer records than the specified limit. |
| offset   int | The index of the first record in the returned page. Used for pagination. |
| totalResults   int | The total number of records matching the request. |
| nextUrl   string | The URL for the next page of records, if more results are available. Max length: 2000 characters. <br>Max length: 2000 |
| previousUrl   string | The URL for the previous page of records, if applicable. Max length: 2000 characters. <br>Max length: 2000 |
| results   array: object | The requested page of projects. |
| id   string: UUID | The internally generated ID for the project. |
| name   string | The name of the project. <br>Max length: 255 |
| startDate   null,string | The estimated start date for the project, in ISO 8601 format. |
| endDate   null,string | The estimated end date for the project, in ISO 8601 format. |
| type   string | The type of the project. Any value is accepted, but the following are recommended: <br>Possible values: `Convention Center`, `Data Center`, `Hotel / Motel`, `Office`, `Parking Structure / Garage`, `Performing Arts`, `Restaurant`, `Retail`, `Stadium / Arena`, `Theme Park`, `Warehouse (non-manufacturing)`, `Assisted Living / Nursing Home`, `Hospital`, `Medical Laboratory`, `Medical Office`, `OutPatient Surgery Center`, `Court House`, `Dormitory`, `Education Facility`, `Government Building`, `Library`, `Military Facility`, `Museum`, `Prison / Correctional Facility`, `Recreation Building`, `Religious Building`, `Research Facility / Laboratory`, `Multi-Family Housing`, `Single-Family Housing`, `Airport`, `Bridge`, `Canal / Waterway`, `Dams / Flood Control / Reservoirs`, `Harbor / River Development`, `Rail`, `Seaport`, `Streets / Roads / Highways`, `Transportation Building`, `Tunnel`, `Waste Water / Sewers`, `Water Supply`, `Manufacturing / Factory`, `Mining Facility`, `Oil & Gas`, `Plant`, `Power Plant`, `Solar Farm`, `Utilities`, `Wind Farm`, `Demonstration Project`, `Template Project` and `Training Project`.<br>Max length: 255 |
| classification   enum:string | The classification of the project. Possible values: <br>`production` â Standard project.`template` â A project that serves as a template for creating new projects.`component` â A placeholder project containing reusable components (e.g., forms). Only one component project is allowed per account. Known as a library in the ACC UI.`sample` â A single sample project automatically created for ACC trials (limited to one per account). |
| projectValue   object | Contains details about the estimated cost of the project, including the amount (`value`) and the currency (`currency`). |
| value   number | The estimated cost of the project, based on the `currency` specified in the currency field. Default: `0`. |
| currency   enum:string | The currency of the project value. Default: `USD`. Possible values: `AED`, `AFN`, `ALL`, `AMD`, `ANG`, `AOA`, `ARS`, `AUD`, `AWG`, `AZN`, `BAM`, `BBD`, `BDT`, `BGN`, `BHD`, `BIF`, `BMD`, `BND`, `BOB`, `BOV`, `BRL`, `BSD`, `BTN`, `BWP`, `BYN`, `BYR`, `BZD`, `CAD`, `CDF`, `CHE`, `CHF`, `CHW`, `CLF`, `CLP`, `CNY`, `COP`, `COU`, `CRC`, `CUC`, `CUP`, `CVE`, `CZK`, `DJF`, `DKK`, `DOP`, `DZD`, `EEK`, `EGP`, `ERN`, `ETB`, `EUR`, `FJD`, `FKP`, `GBP`, `GEL`, `GHS`, `GIP`, `GMD`, `GNF`, `GTQ`, `GYD`, `HKD`, `HNL`, `HRK`, `HTG`, `HUF`, `IDR`, `ILS`, `INR`, `IQD`, `IRR`, `ISK`, `JMD`, `JOD`, `JPY`, `KES`, `KGS`, `KHR`, `KMF`, `KPW`, `KRW`, `KWD`, `KYD`, `KZT`, `LAK`, `LBP`, `LKR`, `LRD`, `LSL`, `LTL`, `LVL`, `LYD`, `MAD`, `MDL`, `MGA`, `MKD`, `MMK`, `MNT`, `MOP`, `MRU`, `MUR`, `MVR`, `MWK`, `MXN`, `MXV`, `MYR`, `MZN`, `NAD`, `NGN`, `NIO`, `NOK`, `NPR`, `NZD`, `OMR`, `PAB`, `PEN`, `PGK`, `PHP`, `PKR`, `PLN`, `PYG`, `QAR`, `RON`, `RSD`, `RUB`, `RWF`, `SAR`, `SBD`, `SCR`, `SDG`, `SEK`, `SGD`, `SHP`, `SLE`, `SLL`, `SOS`, `SRD`, `SSP`, `STN`, `SVC`, `SYP`, `SZL`, `THB`, `TJS`, `TMT`, `TND`, `TOP`, `TRL`, `TRY`, `TTD`, `TWD`, `TZS`, `UAH`, `UGX`, `USD`, `USN`, `UYI`, `UYU`, `UYW`, `UZS`, `VED`, `VES`, `VND`, `VUV`, `WST`, `XAF`, `XAG`, `XAU`, `XBA`, `XBB`, `XBC`, `XBD`, `XCD`, `XDR`, `XOF`, `XPD`, `XPF`, `XPT`, `XSU`, `XTS`, `XUA`, `XXX`, `YER`, `ZAR`, `ZMW`, `ZWL` |
| status   enum:string | The status of the project. <br>Possible values: `active`, `pending`, `archived` and `suspended`. |
| jobNumber   string | A user-defined identifier for the project. This value is assigned when the project is created and can be used to filter projects. It supports partial matches when used with `filterTextMatch`. <br>Max length: 100 |
| addressLine1   null,string | The first line of the projectâs address. <br>Max length: 255 |
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
| imageUrl   string | The URL of the main image associated with the project. This field can be `null`. <br>Max length: 255 |
| thumbnailImageUrl   string | The URL of the projectâs thumbnail image. This field can be `null`. <br>Max length: 255 |
| createdAt   datetime: ISO 8601 | The timestamp when the project was created, in ISO 8601 format. This value is set at creation and does not change. |
| updatedAt   datetime: ISO 8601 | The timestamp when the project was last updated, in ISO 8601 format. This reflects changes to project fields but not updates to resources within the project. |
| accountId   string: UUID | The account ID associated with the project. |
| sheetCount   null,integer | The total number of sheets associated with the project. <br>Note that this field is relevant only in responses. It is ignored in requests. |
| platform   enum:string | The APS platform where the project is stored. Possible values: `acc`, `bim360`. <br>Note that this field is relevant only in responses. It is ignored in requests. |
| businessUnitId   string: UUID | The ID of the business unit that the project is associated with. |
| lastSignIn   datetime: ISO 8601 | The timestamp of the last time someone signed into the project. |
| memberGroupId   string | Not relevant <br>Max length: 25 |
| adminGroupId   string | Not relevant <br>Max length: 25 |
| products   array | An array of the product objects associated with the project. <br>Note that this array is relevant only in responses. It is ignored in requests.<br>When a project is created, every product in the same account as the project is activated for the project. You can call [PATCH users/:userId](/en/docs/acc/v1/reference/http/admin-projects-projectId-users-userId-PATCH/) to separately activate one or more of the returned products for each user assigned to the project. |
| key   enum:string | A machine-readable identifier for the product (e.g., docs, build). <br>Each product has a unique key used throughout the API for identification, filtering, and integration logic (e.g., in query parameters like `filter[key]`).<br>Possible values: ACC - `autoSpecs`, `build`, `cost`, `designCollaboration`, `docs`, `insight`, `modelCoordination`, `projectAdministration`, and `takeoff`.<br>BIM 360 - `assets`, `costManagement`, `designCollaboration`, `documentManagement`, `field`, `fieldManagement`, `glue`, `insight`, `modelCoordination`, `plan`, `projectAdministration`, `projectHome`, `projectManagement`, and `quantification`.<br>Note that this endpoint returns only ACC products. Other endpoints, such as [GET projects](/en/docs/acc/v1/reference/http/admin-accountsaccountidprojects-GET/) and [GET projects/:projectId](/en/docs/acc/v1/reference/http/admin-projects-projectId-GET/), may return both ACC and BIM 360 projects. In those responses, product keys may include BIM 360 values. |
| icon   string | The URL of the icon associated with the product. |
| name   string | The name of the product. |
| language   enum:string | The language for the project. Only valid for the `field` product. Possible values: `en`, `de`, `nl`, `zh`, `de-CH` |
| status   enum:string | The current status of the product. Possible values: <br>`activating`: Product activation is in progress.`activationFailed`: Product activation has failed.`active`: Product activation is completed.`deactivating`: Product deactivation is in progress. (Applicable to BIM 360 only)`deactivationFailed`: Product deactivation has failed. (Applicable to BIM 360 only)`inactive`: Product deactivation is completed. (Applicable to BIM 360 only)`available`: Product is available for activation. (Applicable to BIM 360 only) |
| companyCount   int | The total number of companies associated with the project. <br>Note that this field is relevant only in responses. It is ignored in requests. |
| memberCount   int | The total number of members on the project. <br>Note that this field is relevant only in responses. It is ignored in requests. |
| templateId   string: UUID | The ID of the project that was used as a template to create this project. |

## [Example 1](#example-1)

A list of requested projects.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/admin/v1/accounts/d73fc742-4538-401c-8d0f-853b49b750b2/projects?fields=name,platform&filter[classification]=production,sample&filter[products]=build,docs&filter[name]=Sample Project&filter[type]=Convention Center,-Bridge&filter[status]=active,pending&filter[businessUnitId]=802a4a61-3507-4d4e-8e3c-242a31cc0549&filter[dataServiceId]=bd44763a-5184-483f-85e7-5d97fe589d55&filter[jobNumber]=HP-0002&filter[updatedAt]=2019-06-01T00:00:00.000Z..&filterTextMatch=contains&sort=name desc&limit=20' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 20,
    "offset": 10,
    "totalResults": 121,
    "nextUrl": "https://resource?limit=20&offset=30",
    "previousUrl": "https://resource?limit=20&offset=0"
  },
  "results": [
    {
      "id": "3e354e66-ac8b-41dd-9bc1-93fc182c25dd",
      "accountId": "d73fc742-4538-401c-8d0f-853b49b750b2",
      "addressLine1": "123 Main Street",
      "addressLine2": "Suite 2",
      "adminGroupId": "3456543",
      "businessUnitId": "802a4a61-3507-4d4e-8e3c-242a31cc0549",
      "city": "San Francisco",
      "classification": "production",
      "companyCount": 10,
      "constructionType": "New Construction",
      "contractType": "Unit Price",
      "country": "United States",
      "createdAt": "2018-01-01T12:45:00.000Z",
      "currentPhase": "Design",
      "deliveryMethod": "Design-Bid",
      "endDate": "2015-12-31",
      "imageUrl": "https://s3.us-east-1.amazonaws.com/project_image.png",
      "jobNumber": "HP-0002",
      "lastSignIn": "2019-01-01T12:45:00.000Z",
      "latitude": "37.773972",
      "longitude": "-122.431297",
      "memberCount": 100,
      "memberGroupId": "3456542",
      "name": "Sample Project",
      "platform": "bim360",
      "postalCode": "94001",
      "projectValue": {
        "value": 1650000,
        "currency": "USD"
      },
      "products": [
        {
          "key": "documentManagement",
          "status": "active",
          "icon": "https://s3.us-east-1.amazonaws.com/documentManagement.png",
          "name": "Document Management"
        },
        {
          "key": "fieldManagement",
          "status": "activating",
          "icon": "https://s3.us-east-1.amazonaws.com/fieldManagement.png",
          "name": "Field Management"
        }
      ],
      "sheetCount": 512,
      "startDate": "2010-01-01",
      "stateOrProvince": "California",
      "status": "active",
      "templateId": "10d18e9e-22ae-4186-a79c-819097afb646",
      "thumbnailImageUrl": "https://s3.us-east-1.amazonaws.com/project_thumbnail_image.png",
      "timezone": "America/Los_Angeles",
      "type": "Hospital",
      "updatedAt": "2019-01-01T12:45:00.000Z"
    }
  ]
}

```

Show More

## [Example 2](#example-2)

A list of requested project templates.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/admin/v1/accounts/063da365-32e5-452b-ac9a-b760635d42f3/projects?filter[classification]=template&filter[type]=Template%20Project&filter[updatedAt]=2019-06-01T00:00:00.000Z..&filterTextMatch=contains&sort=name desc&limit=20' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 20,
    "offset": 0,
    "totalResults": 5
  },
  "results": [
    {
      "id": "32a14c32-4916-4992-a33d-6d0b41c434a9",
      "accountId": "063da365-32e5-452b-ac9a-b760635d42f3",
      "addressLine1": null,
      "addressLine2": null,
      "adminGroupId": "226779812",
      "businessUnitId": null,
      "city": null,
      "classification": "template",
      "companyCount": 1,
      "constructionType": null,
      "contractType": null,
      "country": "US",
      "createdAt": "2022-11-29T07:40:52.109Z",
      "currentPhase": null,
      "deliveryMethod": null,
      "endDate": null,
      "imageUrl": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/project-default-1.0.png",
      "jobNumber": null,
      "lastSignIn": null,
      "latitude": null,
      "longitude": null,
      "memberCount": 2,
      "memberGroupId": "226779811",
      "name": "ACC_Template",
      "platform": "acc",
      "postalCode": null,
      "projectValue": {
        "value": 0,
        "currency": "USD"
      },
      "products": [
        {
          "key": "docs",
          "name": "Docs",
          "status": "active",
          "language": "en",
          "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/docs.svg"
        },
        {
          "key": "designCollaboration",
          "name": "Design Collaboration",
          "status": "active",
          "language": "en",
          "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/dc.svg"
        },
        {
          "key": "modelCoordination",
          "name": "Model Coordination",
          "status": "active",
          "language": "en",
          "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/model.svg"
        }
      ],
      "sheetCount": null,
      "startDate": null,
      "stateOrProvince": null,
      "status": "active",
      "templateId": null,
      "thumbnailImageUrl": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/project-default-1.0.png",
      "timezone": null,
      "type": "Template Project",
      "updatedAt": "2022-11-29T07:40:56.661Z"
    }
  ]
}

```

Show More
