# accounts/{accountId}/users/{userId}/projects

Source: https://aps.autodesk.com/en/docs/acc/reference/http/admin-usersuseridprojects-GET/

---

# accounts/{accountId}/users/{userId}/projects

Returns a list of projects for a specified user within an Autodesk Construction Cloud (ACC) or BIM 360 account. Only projects the user participates in will be returned. The calling user must be an account administrator.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/construction/admin/v1/accounts/:accountId/users/:userId/projects Authentication Context user context optional Required OAuth Scopes account:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via either a two-legged or three-legged OAuth flow. Region string Specifies the region where your request should be routed. If not set, the request is routed automatically, which may result in a slight increase in latency. Possible values: US , EMEA . For a complete list of supported regions, see the Regions page. User-Id string The ID of a user on whose behalf your request is acting. Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request. You can use either the userâs ACC ID ( id ), or their Autodesk ID ( autodeskId ). Note that this header is required for Account Admin POST, PATCH, and DELETE endpoints if you want to use a 2-legged authentication context. This header is optional for Account Admin GET endpoints.

Possible values: US , EMEA . For a complete list of supported regions, see the Regions page.

Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.

You can use either the userâs ACC ID ( id ), or their Autodesk ID ( autodeskId ).

Note that this header is required for Account Admin POST, PATCH, and DELETE endpoints if you want to use a 2-legged authentication context. This header is optional for Account Admin GET endpoints.

### Request

## URI Parameters

accountId string: UUID The ID of the ACC account that contains the project being created or the projects being retrieved. This corresponds to the hub ID in the Data Management API . To convert a hub ID into an account ID, remove the â b. " prefix. For example, a hub ID of b.c8b0c73d-3ae9 translates to an account ID of c8b0c73d-3ae9 . userId string The ID of the user. To find the ID call GET users . You can use either the ACC ID ( id ) or the Autodesk ID ( autodeskId ).

### Request

## Query String Parameters

filter[id] array: string: uuid A list of project IDs to filter by. fields array: string A comma-separated list of user project fields to include in the response. If not specified, all available fields are included by default. Possible values: accessLevels , accountId , addressLine1 , addressLine2 , city , constructionType , country , createdAt , classification , deliveryMethod , endDate , imageUrl , jobNumber , latitude , longitude , name , platform , postalCode , projectValue , sheetCount , startDate , stateOrProvince , status , thumbnailImageUrl , timezone , type , updatedAt , contractType and currentPhase . filter[classification] array: string Filters projects by classification. Possible values: production â Standard production projects. template â Project templates that can be cloned to create production projects. component â Placeholder projects that contain standardized components (e.g., forms) for use across projects. Only one component project is permitted per account. Known as a library in the ACC unified products UI. sample â The single sample project automatically created upon ACC trial setup. Only one sample project is permitted per account. Max length: 255 filter[name] string Filters projects by name. Supports partial matches when used with filterTextMatch . For example filter[name]=ABCco&filterTextMatch=startsWith returns projects whose names start with âABCcoâ. Max length: 255 filter[platform] array: string Filters by platform. Possible values: acc (Autodesk Construction Cloud) and bim360 (BIM 360). Max length: 255 filter[status] array: string Filters projects by status. Possible values: active , pending , archived , suspended . filter[type] array: string Filters by project type. To exclude a type, prefix it with - (e.g., -Bridge excludes bridge projects). Possible values: Airport , Assisted Living / Nursing Home , Bridge , Canal / Waterway , Convention Center , Court House , Data Center , Dams / Flood Control / Reservoirs , Demonstration Project , Dormitory , Education Facility , Government Building , Harbor / River Development , Hospital , Hotel / Motel , Library , Manufacturing / Factory , Medical Laboratory , Medical Office , Military Facility , Mining Facility , Multi-Family Housing , Museum , Oil & Gas ,``Plant``, Office , OutPatient Surgery Center , Parking Structure / Garage , Performing Arts , Power Plant , Prison / Correctional Facility , Rail , Recreation Building , Religious Building , Research Facility / Laboratory , Restaurant , Retail , Seaport , Single-Family Housing , Solar Farm , Stadium/Arena , Streets / Roads / Highways , Template Project , Theme Park , Training Project , Transportation Building , Tunnel , Utilities , Warehouse (non-manufacturing) , Waste Water / Sewers , Water Supply , Wind Farm . filter[jobNumber] string Filters by a user-defined project identifier. Supports partial matches when used with filterTextMatch . For example, filter[jobNumber]=HP-0002&filterTextMatch=equals returns projects where the job number is exactly âHP-0002â. Max length: 255 filter[updatedAt] string Filters projects updated within a specific date range in ISO 8601 format. For example: Date range: 2023-03-02T00:00:00.000Z..2023-03-03T23:59:59 .999Z Specific start date: 2023-03-02T00:00:00.000Z.. Specific end date: ..2023-03-02T23:59:59.999Z For more details, see JSON API Filtering . Max length: 100 filter[accessLevels] array: string Filters projects by user access level. Possible values: projectAdmin , projectMember . Max length: 255 filterTextMatch enum:string Specifies how text-based filters should match values in supported fields. This parameter can be used in any endpoint that supports text-based filtering (e.g., filter[name] , filter[jobNumber] , filter[companyName] , etc.). Possible values: contains (default) â Matches if the field contains the specified text anywhere startsWith â Matches if the field starts with the specified text endsWith â Matches if the field ends with the specified text equals â Matches only if the field exactly matches the specified text Matching is case-insensitive. Wildcards and regular expressions are not supported. sort array: string A list of fields to sort the returned user projects by. Multiple sort fields are applied in sequence order â each sort field produces groupings of projects with the same values of that field; the next sort field applies within the groupings produced by the previous sort field. Each property can be followed by a direction modifier of either asc (ascending) or desc (descending). The default is asc . Possible values: name (the default), startDate , endDate , type , status , jobNumber , constructionType , deliveryMethod , contractType , currentPhase , createdAt , updatedAt and platform . limit int The maximum number of records to return in the response. Default: 20 Minimum: 1 Maximum: 200 (If a larger value is provided, only 200 records are returned) offset int The index of the first record to return. Used for pagination in combination with the limit parameter. Example: limit=20 and offset=40 returns records 41â60.

Possible values: accessLevels , accountId , addressLine1 , addressLine2 , city , constructionType , country , createdAt , classification , deliveryMethod , endDate , imageUrl , jobNumber , latitude , longitude , name , platform , postalCode , projectValue , sheetCount , startDate , stateOrProvince , status , thumbnailImageUrl , timezone , type , updatedAt , contractType and currentPhase .

production â Standard production projects. template â Project templates that can be cloned to create production projects. component â Placeholder projects that contain standardized components (e.g., forms) for use across projects. Only one component project is permitted per account. Known as a library in the ACC unified products UI. sample â The single sample project automatically created upon ACC trial setup. Only one sample project is permitted per account.

Max length: 255

Max length: 255

Max length: 255

Possible values: Airport , Assisted Living / Nursing Home , Bridge , Canal / Waterway , Convention Center , Court House , Data Center , Dams / Flood Control / Reservoirs , Demonstration Project , Dormitory , Education Facility , Government Building , Harbor / River Development , Hospital , Hotel / Motel , Library , Manufacturing / Factory , Medical Laboratory , Medical Office , Military Facility , Mining Facility , Multi-Family Housing , Museum , Oil & Gas ,``Plant``, Office , OutPatient Surgery Center , Parking Structure / Garage , Performing Arts , Power Plant , Prison / Correctional Facility , Rail , Recreation Building , Religious Building , Research Facility / Laboratory , Restaurant , Retail , Seaport , Single-Family Housing , Solar Farm , Stadium/Arena , Streets / Roads / Highways , Template Project , Theme Park , Training Project , Transportation Building , Tunnel , Utilities , Warehouse (non-manufacturing) , Waste Water / Sewers , Water Supply , Wind Farm .

Max length: 255

Date range: 2023-03-02T00:00:00.000Z..2023-03-03T23:59:59 .999Z Specific start date: 2023-03-02T00:00:00.000Z.. Specific end date: ..2023-03-02T23:59:59.999Z

For more details, see JSON API Filtering .

Max length: 100

Max length: 255

This parameter can be used in any endpoint that supports text-based filtering (e.g., filter[name] , filter[jobNumber] , filter[companyName] , etc.).

Possible values:

contains (default) â Matches if the field contains the specified text anywhere

startsWith â Matches if the field starts with the specified text

endsWith â Matches if the field ends with the specified text

equals â Matches only if the field exactly matches the specified text

Matching is case-insensitive.

Wildcards and regular expressions are not supported.

Each property can be followed by a direction modifier of either asc (ascending) or desc (descending). The default is asc .

Possible values: name (the default), startDate , endDate , type , status , jobNumber , constructionType , deliveryMethod , contractType , currentPhase , createdAt , updatedAt and platform .

Default: 20

Minimum: 1

Maximum: 200 (If a larger value is provided, only 200 records are returned)

Used for pagination in combination with the limit parameter.

Example: limit=20 and offset=40 returns records 41â60.

### Response

## HTTP Status Code Summary

200 OK A list of requested user projects. 400 Bad Request The request could not be understood by the server due to malformed syntax. 401 Unauthorized Request has not been applied because it lacks valid authentication credentials for the target resource. 403 Forbidden The server understood the request but refuses to authorize it. 404 Not Found The resource could not be found. 406 Not Acceptable The server cannot produce a response matching the list of acceptable values defined in the request. 410 Access to the target resource is no longer available. 429 Too Many Requests User has sent too many requests in a given amount of time. 500 Internal Server Error An unexpected error occurred on the server. 503 Service Unavailable Server is not ready to handle the request.

### Response

## Body Structure (200)

pagination object Contains pagination details for the records returned by the endpoint. limit int The maximum number of records returned per page. The last page may contain fewer records than the specified limit. offset int The index of the first record in the returned page. Used for pagination. totalResults int The total number of records matching the request. nextUrl string The URL for the next page of records, if more results are available. Max length: 2000 characters. Max length: 2000 previousUrl string The URL for the previous page of records, if applicable. Max length: 2000 characters. Max length: 2000 results array: object A list of user projects matching the request criteria. id string: UUID The internally generated ID for the project. name string The name of the project. Max length: 255 startDate null,string The estimated start date for the project, in ISO 8601 format. endDate null,string The estimated end date for the project, in ISO 8601 format. type string The type of the project. Any value is accepted, but the following are recommended: Possible values: Convention Center , Data Center , Hotel / Motel , Office , Parking Structure / Garage , Performing Arts , Restaurant , Retail , Stadium / Arena , Theme Park , Warehouse (non-manufacturing) , Assisted Living / Nursing Home , Hospital , Medical Laboratory , Medical Office , OutPatient Surgery Center , Court House , Dormitory , Education Facility , Government Building , Library , Military Facility , Museum , Prison / Correctional Facility , Recreation Building , Religious Building , Research Facility / Laboratory , Multi-Family Housing , Single-Family Housing , Airport , Bridge , Canal / Waterway , Dams / Flood Control / Reservoirs , Harbor / River Development , Rail , Seaport , Streets / Roads / Highways , Transportation Building , Tunnel , Waste Water / Sewers , Water Supply , Manufacturing / Factory , Mining Facility , Oil & Gas , Plant , Power Plant , Solar Farm , Utilities , Wind Farm , Demonstration Project , Template Project and Training Project . Max length: 255 classification enum:string The classification of the project. Possible values: production â Standard project. template â A project that serves as a template for creating new projects. component â A placeholder project containing reusable components (e.g., forms). Only one component project is allowed per account. Known as a library in the ACC UI. sample â A single sample project automatically created for ACC trials (limited to one per account). projectValue object Contains details about the estimated cost of the project, including the amount ( value ) and the currency ( currency ). value number The estimated cost of the project, based on the currency specified in the currency field. Default: 0 . currency enum:string The currency of the project value. Default: USD .
Possible values: AED , AFN , ALL , AMD , ANG , AOA , ARS , AUD , AWG , AZN , BAM , BBD , BDT , BGN , BHD , BIF , BMD , BND , BOB , BOV , BRL , BSD , BTN , BWP , BYN , BYR , BZD , CAD , CDF , CHE , CHF , CHW , CLF , CLP , CNY , COP , COU , CRC , CUC , CUP , CVE , CZK , DJF , DKK , DOP , DZD , EEK , EGP , ERN , ETB , EUR , FJD , FKP , GBP , GEL , GHS , GIP , GMD , GNF , GTQ , GYD , HKD , HNL , HRK , HTG , HUF , IDR , ILS , INR , IQD , IRR , ISK , JMD , JOD , JPY , KES , KGS , KHR , KMF , KPW , KRW , KWD , KYD , KZT , LAK , LBP , LKR , LRD , LSL , LTL , LVL , LYD , MAD , MDL , MGA , MKD , MMK , MNT , MOP , MRU , MUR , MVR , MWK , MXN , MXV , MYR , MZN , NAD , NGN , NIO , NOK , NPR , NZD , OMR , PAB , PEN , PGK , PHP , PKR , PLN , PYG , QAR , RON , RSD , RUB , RWF , SAR , SBD , SCR , SDG , SEK , SGD , SHP , SLE , SLL , SOS , SRD , SSP , STN , SVC , SYP , SZL , THB , TJS , TMT , TND , TOP , TRL , TRY , TTD , TWD , TZS , UAH , UGX , USD , USN , UYI , UYU , UYW , UZS , VED , VES , VND , VUV , WST , XAF , XAG , XAU , XBA , XBB , XBC , XBD , XCD , XDR , XOF , XPD , XPF , XPT , XSU , XTS , XUA , XXX , YER , ZAR , ZMW , ZWL status enum:string The status of the project. Possible values: active , pending , archived and suspended . jobNumber string A user-defined identifier for the project. This value is assigned when the project is created and can be used to filter projects. It supports partial matches when used with filterTextMatch . Max length: 100 addressLine1 null,string The first line of the projectâs address. Max length: 255 addressLine2 null,string Additional address details for the project location. Max length: 255 city null,string The city wher the project is located. Max length: 255 stateOrProvince null,string The state or province where the project is located. It must be a valid name or an ISO 3166-2 code. The provided state or province must exist in the country of the project. Max length: 255 postalCode null,string The postal or ZIP code of the project location. Max length: 255 country null,string The country where the project is located, using an ISO 3166-1 code. Max length: 255 latitude null,string The latitude coordinate of the project location. Max length: 25 longitude null,string The longitude coordinate of the project location. Max length: 25 timezone null,string The time zone where the project is located. It must be a valid IANA time zone name from the IANA Time Zone Database (e.g., America/New_York ). If no time zone is set, this field may be null .
Possible values: Pacific/Honolulu , America/Juneau , America/Los_Angeles , America/Phoenix , America/Denver , America/Chicago , America/New_York , America/Indiana/Indianapolis , Pacific/Pago_Pago , Pacific/Midway , America/Tijuana , America/Chihuahua , America/Mazatlan , America/Guatemala , America/Mexico_City , America/Monterrey , America/Regina , America/Bogota , America/Lima , America/Caracas , America/Halifax , America/Guyana , America/La_Paz , America/Santiago , America/St_Johns , America/Sao_Paulo , America/Argentina/Buenos_Aires , America/Godthab , Atlantic/South_Georgia , Atlantic/Azores , Atlantic/Cape_Verde , Africa/Casablanca , Europe/Dublin , Europe/Lisbon , Europe/London , Africa/Monrovia , Etc/UTC , Europe/Amsterdam , Europe/Belgrade , Europe/Berlin , Europe/Bratislava , Europe/Brussels , Europe/Budapest , Europe/Copenhagen , Europe/Ljubljana , Europe/Madrid , Europe/Paris , Europe/Prague , Europe/Rome , Europe/Sarajevo , Europe/Skopje , Europe/Stockholm , Europe/Vienna , Europe/Warsaw , Africa/Algiers , Europe/Zagreb , Europe/Athens , Europe/Bucharest , Africa/Cairo , Africa/Harare , Europe/Helsinki , Europe/Istanbul , Asia/Jerusalem , Europe/Kiev , Africa/Johannesburg , Europe/Riga , Europe/Sofia , Europe/Tallinn , Europe/Vilnius , Asia/Baghdad , Asia/Kuwait , Europe/Minsk , Africa/Nairobi , Asia/Riyadh , Asia/Tehran , Asia/Muscat , Asia/Baku , Europe/Moscow , Asia/Tbilisi , Asia/Yerevan , Asia/Kabul , Asia/Karachi , Asia/Tashkent , Asia/Kolkata , Asia/Colombo , Asia/Kathmandu , Asia/Almaty , Asia/Dhaka , Asia/Yekaterinburg , Asia/Rangoon , Asia/Bangkok , Asia/Jakarta , Asia/Novosibirsk , Asia/Shanghai , Asia/Chongqing , Asia/Hong_Kong , Asia/Krasnoyarsk , Asia/Kuala_Lumpur , Australia/Perth , Asia/Singapore , Asia/Taipei , Asia/Ulaanbaatar , Asia/Urumqi , Asia/Irkutsk , Asia/Tokyo , Asia/Seoul , Australia/Adelaide , Australia/Darwin , Australia/Brisbane , Australia/Melbourne , Pacific/Guam , Australia/Hobart , Pacific/Port_Moresby , Australia/Sydney , Asia/Yakutsk , Pacific/Noumea , Asia/Vladivostok , Pacific/Auckland , Pacific/Fiji , Asia/Kamchatka , Asia/Magadan , Pacific/Majuro , Pacific/Guadalcanal , Pacific/Tongatapu , Pacific/Apia , Pacific/Fakaofo constructionType string The type of construction for the project. Recommended values: New Construction , Renovation . Any value is accepted. deliveryMethod string The method used to deliver the project. Recommended values include Design-Bid-Build , Construction Management (CM) at Risk , and Integrated Project Delivery (IPD) . Any value is accepted. contractType string The type of contract for the project. For example, Lump Sum , Cost Plus , Guaranteed Maximum Price , Unit Price . Any value is accepted. currentPhase string The current phase of the project. Recommended values include, Concept , Design , Bidding , Planning , Preconstruction , Construction , Commissioning , Warranty , Complete , Facility Management , Operation , Strategic Definition , Preparation and Brief , Concept Design , Developed Design , Technical Design , Construction , Handover and Close Out and In Use . Any value is accepted. imageUrl string The URL of the main image associated with the project. This field can be null . Max length: 255 thumbnailImageUrl string The URL of the projectâs thumbnail image. This field can be null . Max length: 255 createdAt datetime: ISO 8601 The timestamp when the project was created, in ISO 8601 format. This value is set at creation and does not change. updatedAt datetime: ISO 8601 The timestamp when the project was last updated, in ISO 8601 format. This reflects changes to project fields but not updates to resources within the project. accountId string: UUID The account ID associated with the project. sheetCount null,integer The total number of sheets associated with the project. Note that this field is relevant only in responses. It is ignored in requests. platform enum:string The APS platform where the project is stored. Possible values: acc , bim360 . Note that this field is relevant only in responses. It is ignored in requests. accessLevels object Information about the userâs access roles in the project. projectAdmin boolean Indicates whether the user is a project administrator for the project. Possible values: true : The user is a project administrator. false : The user is not a project administrator. projectMember boolean Indicates whether the user is a project member but not a project administrator. Possible values: true : The user is a project member but not an administrator. false : The user is not a project member.

Max length: 2000

Max length: 2000

Max length: 255

Possible values: Convention Center , Data Center , Hotel / Motel , Office , Parking Structure / Garage , Performing Arts , Restaurant , Retail , Stadium / Arena , Theme Park , Warehouse (non-manufacturing) , Assisted Living / Nursing Home , Hospital , Medical Laboratory , Medical Office , OutPatient Surgery Center , Court House , Dormitory , Education Facility , Government Building , Library , Military Facility , Museum , Prison / Correctional Facility , Recreation Building , Religious Building , Research Facility / Laboratory , Multi-Family Housing , Single-Family Housing , Airport , Bridge , Canal / Waterway , Dams / Flood Control / Reservoirs , Harbor / River Development , Rail , Seaport , Streets / Roads / Highways , Transportation Building , Tunnel , Waste Water / Sewers , Water Supply , Manufacturing / Factory , Mining Facility , Oil & Gas , Plant , Power Plant , Solar Farm , Utilities , Wind Farm , Demonstration Project , Template Project and Training Project .

Max length: 255

- production â Standard project.

- template â A project that serves as a template for creating new projects.

- component â A placeholder project containing reusable components (e.g., forms). Only one component project is allowed per account. Known as a library in the ACC UI.

- sample â A single sample project automatically created for ACC trials (limited to one per account).

Possible values: active , pending , archived and suspended .

Max length: 100

Max length: 255

Max length: 255

Max length: 255

Max length: 255

Max length: 255

Max length: 255

Max length: 25

Max length: 25

Any value is accepted.

Max length: 255

Max length: 255

Note that this field is relevant only in responses. It is ignored in requests.

Note that this field is relevant only in responses. It is ignored in requests.

- true : The user is a project administrator.

- false : The user is not a project administrator.

- true : The user is a project member but not an administrator.

- false : The user is not a project member.

## Example

A list of requested user projects.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/admin/v1/accounts/d73fc742-4538-401c-8d0f-853b49b750b2/users/6cc15635-2fbd-4f73-afbe-abd833408a1d/projects?filter[id]=39712a51-bd64-446a-9c72-48c4e43d0a0d,d1163421-e7eb-4862-ac15-b33777ba42de&fields=name,platform&filter[classification]=production,sample&filter[name]=Sample Project&filter[platform]=acc,bim360&filter[status]=active,pending&filter[type]=Convention Center,-Bridge&filter[jobNumber]=HP-0002&filter[updatedAt]=2019-06-01T00:00:00.000Z..&filter[accessLevels]=projectAdmin&filterTextMatch=contains&sort=name desc&limit=20' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
```

### Response

```
{ "pagination" : { "limit" : 20 , "offset" : 10 , "totalResults" : 121 , "nextUrl" : "https://resource?limit=20&offset=30" , "previousUrl" : "https://resource?limit=20&offset=0" }, "results" : [ { "id" : "3e354e66-ac8b-41dd-9bc1-93fc182c25dd" , "name" : "Sample Project" , "startDate" : "2010-01-01" , "endDate" : "2015-12-31" , "type" : "Hospital" , "classification" : "production" , "projectValue" : { "value" : 1650000 , "currency" : "USD" }, "status" : "active" , "jobNumber" : "HP-0002" , "addressLine1" : "123 Main Street" , "addressLine2" : "Suite 2" , "city" : "San Francisco" , "stateOrProvince" : "California" , "postalCode" : "94001" , "country" : "United States" , "latitude" : "37.773972" , "longitude" : "-122.431297" , "timezone" : "America/Los_Angeles" , "constructionType" : "New Construction" , "deliveryMethod" : "Design-Bid" , "contractType" : "Unit Price" , "currentPhase" : "Design" , "imageUrl" : "https://s3.us-east-1.amazonaws.com/project_image.png" , "thumbnailImageUrl" : "https://s3.us-east-1.amazonaws.com/project_thumbnail_image.png" , "createdAt" : "2018-01-01T12:45:00.000Z" , "updatedAt" : "2019-01-01T12:45:00.000Z" , "accountId" : "d73fc742-4538-401c-8d0f-853b49b750b2" , "sheetCount" : 512 , "platform" : "acc" , "accessLevels" : { "projectAdmin" : true , "projectMember" : true } } ] }
```
