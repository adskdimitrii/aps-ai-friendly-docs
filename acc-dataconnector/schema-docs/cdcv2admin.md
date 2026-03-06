# cdcv2admin Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=cdcv2admin&format=html

---

# cdcv2admin Schema Description

**Documentation Updated:** 2025-11-17  

- [account_services](#account_services)
- [accounts](#accounts)
- [companies](#companies)
- [project_companies](#project_companies)
- [project_products](#project_products)
- [project_roles](#project_roles)
- [project_services](#project_services)
- [project_user_companies](#project_user_companies)
- [project_user_roles](#project_user_roles)
- [project_users](#project_users)
- [projects](#projects)
- [roles](#roles)
- [users](#users)

**Beta Release**  
This is a Beta release of the cdcv2admin data set and schema definitions are subject to change or even possibly be removed from the final data set release. Thank you for your understanding with any future schema updates.

## account_services

Service List for the Account - This is the Change Data Capture (CDC) enabled version of the admin.account_services table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | service | enum: string | Possible Values: documentManagement projectManagement costManagement designCollaboration fieldManagement modelCoordination field glue plan insight | BIM 360 Service |
| 3 | created_at | timestamp: SQL |  | Timestamp when the account_service was created Column used for filtering Date Range Extraction requests |
| 4 | updated_at | timestamp: SQL |  | Timestamp when the account_service was updated Column used for filtering Date Range Extraction requests |
| 5 | deleted_at | timestamp: SQL |  | Timestamp when the account_service was deleted Column used for filtering Date Range Extraction requests |
| 6 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## accounts

This is a list of accounts in BIM 360. For individual customer exports, this table will only include the single customer's information. - This is the Change Data Capture (CDC) enabled version of the admin.accounts table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 7 | bim360_account_id | string: UUID |  | Account Identifier |
| 8 | display_name | string | Max length: 255 | Display name of the account |
| 9 | start_date | timestamp: SQL |  | Start of the account availability |
| 10 | end_date | timestamp: SQL |  | End of the account availability |
| 11 | created_at | timestamp: SQL |  | Timestamp when the account was created Column used for filtering Date Range Extraction requests |
| 12 | updated_at | timestamp: SQL |  | Timestamp when the account was updated Column used for filtering Date Range Extraction requests |
| 13 | deleted_at | timestamp: SQL |  | Timestamp when the account was deleted Column used for filtering Date Range Extraction requests |
| 14 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## companies

Company organizations for use in BIM 360. - This is the Change Data Capture (CDC) enabled version of the admin.companies table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 15 | id | string: UUID |  | Company ID |
| 16 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 17 | name | string | Max length: 255 | Name of the company |
| 18 | trade | enum: string | Max length: 255 | Trade of the company |
| 19 | category | string | Max length: 255 | Category for the company |
| 20 | address_line1 | string | Max length: 255 | Company specified address |
| 21 | address_line2 | string | Max length: 255 | Company specified address |
| 22 | city | string | Max length: 255 | City for the Company address |
| 23 | state_or_province | string | Max length: 255 | State for the Company address |
| 24 | postal_code | string | Max length: 255 | Postal code for the address |
| 25 | country | string | Max length: 255 | Country of the address |
| 26 | phone | string | Max length: 255 | Phone for the company |
| 27 | website_url | string | Max length: 255 | Web site for the company |
| 28 | description | string | Max length: 255 | Description of the company |
| 29 | erp_id | string | Max length: 255 | ERP Id |
| 30 | tax_id | string | Max length: 255 | Tax ID |
| 31 | status | enum: string | Possible Values: deleted active | Status of the company |
| 32 | created_at | timestamp: SQL |  | Date company created Column used for filtering Date Range Extraction requests |
| 33 | project_size | number |  | Size of project |
| 34 | user_size | number |  | User size of project |
| 35 | custom_properties | string | Max length: 255 | Customer defined properties |
| 36 | updated_at | timestamp: SQL |  | Timestamp when the companie was updated Column used for filtering Date Range Extraction requests |
| 37 | deleted_at | timestamp: SQL |  | Timestamp when the companie was deleted Column used for filtering Date Range Extraction requests |
| 38 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## project_companies

The company list for projects in BIM 360. - This is the Change Data Capture (CDC) enabled version of the admin.project_companies table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 39 | project_id | string: UUID |  | Project ID |
| 40 | company_id | string: UUID |  | The company ID for the company that is a part of the project |
| 41 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 42 | company_oxygen_id | string |  | Oxygen ID for the company |
| 43 | created_at | timestamp: SQL |  | Timestamp when the project_companie was created Column used for filtering Date Range Extraction requests |
| 44 | updated_at | timestamp: SQL |  | Timestamp when the project_companie was updated Column used for filtering Date Range Extraction requests |
| 45 | deleted_at | timestamp: SQL |  | Timestamp when the project_companie was deleted Column used for filtering Date Range Extraction requests |
| 46 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## project_products

The Product List for the Project - This is the Change Data Capture (CDC) enabled version of the admin.project_products table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 47 | bim360_project_id | string: UUID |  | Project ID |
| 48 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 49 | product_key | enum: string | Possible Values: autoSpecs build buildingConnected capitalPlanning cost designCollaboration docs financials insight modelCoordination projectAdministration takeoff | Bim360/Acc Product |
| 50 | status | enum: string | Possible Values: active activating inactive activationFailed deactivationFailed deactivating | Status of the product |
| 51 | created_at | timestamp: SQL |  | Date/time service was added Column used for filtering Date Range Extraction requests |
| 52 | updated_at | timestamp: SQL |  | Timestamp when the project_product was updated Column used for filtering Date Range Extraction requests |
| 53 | deleted_at | timestamp: SQL |  | Timestamp when the project_product was deleted Column used for filtering Date Range Extraction requests |
| 54 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## project_roles

The project roles for projects in BIM 360. - This is the Change Data Capture (CDC) enabled version of the admin.project_roles table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 55 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 56 | bim360_project_id | string: UUID |  | Project ID |
| 57 | role_oxygen_id | string |  | Oxygen ID for the role |
| 58 | name | string |  | Name for the role |
| 59 | status | enum: string | Possible Values: active inactive | Status of the role |
| 60 | role_id | string: UUID |  | Admin ID for the role |
| 61 | created_at | timestamp: SQL |  | Timestamp when the project_role was created Column used for filtering Date Range Extraction requests |
| 62 | updated_at | timestamp: SQL |  | Timestamp when the project_role was updated Column used for filtering Date Range Extraction requests |
| 63 | deleted_at | timestamp: SQL |  | Timestamp when the project_role was deleted Column used for filtering Date Range Extraction requests |
| 64 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## project_services

The Service List for the Account - This is the Change Data Capture (CDC) enabled version of the admin.project_services table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 65 | project_id | string: UUID |  | Project ID |
| 66 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 67 | service | enum: string | Possible Values: documentManagement projectManagement costManagement designCollaboration fieldManagement modelCoordination field glue plan insight | BIM 360 Service |
| 68 | status | enum: string | Possible Values: active inactive archived | Status of the service |
| 69 | created_at | timestamp: SQL |  | Date/time service was added Column used for filtering Date Range Extraction requests |
| 70 | updated_at | timestamp: SQL |  | Timestamp when the project_service was updated Column used for filtering Date Range Extraction requests |
| 71 | deleted_at | timestamp: SQL |  | Timestamp when the project_service was deleted Column used for filtering Date Range Extraction requests |
| 72 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## project_user_companies

The company list for projects in BIM 360. - This is the Change Data Capture (CDC) enabled version of the admin.project_user_companies table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 73 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 74 | company_oxygen_id | string: UUID |  | Oxygen ID for the company |
| 75 | project_id | string: UUID |  | Project ID |
| 76 | user_id | string: UUID |  | The user ID for the member of the company |
| 77 | status | string |  | Status of the user |
| 78 | created_at | timestamp: SQL |  | Date/time user was added Column used for filtering Date Range Extraction requests |
| 79 | updated_at | timestamp: SQL |  | Timestamp when the user was updated Column used for filtering Date Range Extraction requests |
| 80 | deleted_at | timestamp: SQL |  | Timestamp when the user was deleted Column used for filtering Date Range Extraction requests |
| 81 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## project_user_roles

The list of roles for the user in a particular project - This is the Change Data Capture (CDC) enabled version of the admin.project_user_roles table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 82 | project_id | string: UUID |  | Project ID |
| 83 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 84 | user_id | string: UUID |  | The user ID for the member of the project |
| 85 | role_id | string: UUID |  | The role the user has for this particular project |
| 86 | created_at | timestamp: SQL |  | Date user added to project Column used for filtering Date Range Extraction requests |
| 87 | bim360_project_id | string: UUID |  | Project ID for the user role |
| 88 | updated_at | timestamp: SQL |  | Timestamp when the user role was updated Column used for filtering Date Range Extraction requests |
| 89 | deleted_at | timestamp: SQL |  | Timestamp when the user role was deleted Column used for filtering Date Range Extraction requests |
| 90 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## project_users

The user list for projects - This is the Change Data Capture (CDC) enabled version of the admin.project_users table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 91 | bim360_project_id | string: UUID |  | Project ID |
| 92 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 93 | user_id | string: UUID |  | The user ID for the member of the project |
| 94 | status | string | Possible Values: active activating deleted | The user's status for the project |
| 95 | company_id | string: UUID |  | The user's assigned company for the project |
| 96 | access_level | string | Possible Values: project_user project_admin | The user's access level for the project |
| 97 | created_at | timestamp: SQL |  | Created date project_users table is a new table created at the database level in November, 2020 as part of the effort to unify BIM 360 and ACC. A data migration was performed that migrated the records of BIM 360 users to this new table, and as a result the created_at reflects the date when the user records were written into this new table Users added after November, 2020 should have a consistent date between project_user_services and project_users table. Column used for filtering Date Range Extraction requests |
| 98 | updated_at | timestamp: SQL |  | Updated date Column used for filtering Date Range Extraction requests |
| 99 | deleted_at | timestamp: SQL |  | Timestamp when the project_user was deleted Column used for filtering Date Range Extraction requests |
| 100 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## projects

Projects in BIM 360 - This is the Change Data Capture (CDC) enabled version of the admin.projects table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 101 | id | string: UUID |  | Project ID |
| 102 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 103 | name | string | Max length: 255 | Name of the project |
| 104 | start_date | timestamp: SQL |  | Start date for the project |
| 105 | end_date | timestamp: SQL |  | End date for the project |
| 106 | type | string | Possible Values: <userDefinedValue> Convention Center Data Center Hotel / Motel Office Parking Structure / Garage Performing Arts Restaurant Retail Stadium / Arena Theme Park Warehouse (non-manufacturing) Assisted Living / Nursing Home Hospital Medical Laboratory Medical Office OutPatient Surgery Center Court House Dormitory Education Facility Government Building Library Military Facility Museum Prison / Correctional Facility Recreation Building Religious Building Research Facility / Laboratory Multi-Family Housing Single-Family Housing Airport Bridge Canal / Waterway Dams / Flood Control / Reservoirs Harbor / River Development Rail Seaport Streets / Roads / Highways Transportation Building Tunnel Waste Water / Sewers Water Supply Manufacturing / Factory Mining Facility Oil & Gas Plant Power Plant Solar Farm Utilities Wind Farm Demonstration Project Template Project Training Project | Project type definition |
| 107 | value | number |  | Project Value |
| 108 | currency | enum: string | Possible Values: USD AUD CAD EUR GBP ALL AZN BYR BRL BGN CNY HRK CZK DKK EEK HKD HUF ISK INR IRR ILS JPY KZT KRW KPW KGS LVL LTL MKD MNT ANG NOK PKR PLN RON RUB SAR RSD SGD ZAR SEK CHF TWD TRL UAH UZS YER PHP NZD MYR THB IDR VND | Value currency |
| 109 | status | enum: string | Possible Values: active pending expired archived deleted | Status of the project |
| 110 | job_number | string | Max length: 100 | Job number of the project |
| 111 | address_line1 | string | Max length: 255 | Address of the project |
| 112 | address_line2 | string | Max length: 255 | Address of the project |
| 113 | city | string | Max length: 255 | City of the project |
| 114 | state_or_province | string | Max length: 255 | State of the project |
| 115 | postal_code | string | Max length: 255 | Postal code for the project |
| 116 | country | string | Max length: 255 | Country for the project |
| 117 | timezone | enum: string | Possible Values: Pacific/Honolulu America/Juneau America/Los_Angeles America/Phoenix America/Denver America/Chicago America/New_York America/Indiana/Indianapolis Pacific/Pago_Pago Pacific/Midway America/Tijuana America/Chihuahua America/Mazatlan America/Guatemala America/Mexico_City America/Monterrey America/Regina America/Bogota America/Lima America/Caracas America/Halifax America/Guyana America/La_Paz America/Santiago America/St_Johns America/Sao_Paulo America/Argentina/Buenos_Aires America/Godthab Atlantic/South_Georgia Atlantic/Azores Atlantic/Cape_Verde Africa/Casablanca Europe/Dublin Europe/Lisbon Europe/London Africa/Monrovia Etc/UTC Europe/Amsterdam Europe/Belgrade Europe/Berlin Europe/Bratislava Europe/Brussels Europe/Budapest Europe/Copenhagen Europe/Ljubljana Europe/Madrid Europe/Paris Europe/Prague Europe/Rome Europe/Sarajevo Europe/Skopje Europe/Stockholm Europe/Vienna Europe/Warsaw Africa/Algiers Europe/Zagreb Europe/Athens Europe/Bucharest Africa/Cairo Africa/Harare Europe/Helsinki Europe/Istanbul Asia/Jerusalem Europe/Kiev Africa/Johannesburg Europe/Riga Europe/Sofia Europe/Tallinn Europe/Vilnius Asia/Baghdad Asia/Kuwait Europe/Minsk Africa/Nairobi Asia/Riyadh Asia/Tehran Asia/Muscat Asia/Baku Europe/Moscow Asia/Tbilisi Asia/Yerevan Asia/Kabul Asia/Karachi Asia/Tashkent Asia/Kolkata Asia/Colombo Asia/Kathmandu Asia/Almaty Asia/Dhaka Asia/Yekaterinburg Asia/Rangoon Asia/Bangkok Asia/Jakarta Asia/Novosibirsk Asia/Shanghai Asia/Chongqing Asia/Hong_Kong Asia/Krasnoyarsk Asia/Kuala_Lumpur Australia/Perth Asia/Singapore Asia/Taipei Asia/Ulaanbaatar Asia/Urumqi Asia/Irkutsk Asia/Tokyo Asia/Seoul Australia/Adelaide Australia/Darwin Australia/Brisbane Australia/Melbourne Pacific/Guam Australia/Hobart Pacific/Port_Moresby Australia/Sydney Asia/Yakutsk Pacific/Noumea Asia/Vladivostok Pacific/Auckland Pacific/Fiji Asia/Kamchatka Asia/Magadan Pacific/Majuro Pacific/Guadalcanal Pacific/Tongatapu Pacific/Apia Pacific/Fakaofo | Timezone for the project |
| 118 | construction_type | enum: string | Possible Values: New Construction Renovation | Construction type |
| 119 | contract_type | enum: string | Possible Values: Construction Management (CM) at Risk Design-Bid Design-Bid-Build Design-Build-Operate IPD | Contract type for the project |
| 120 | business_unit_id | string: UUID |  | Business Unit ID for the project Foreign Key: Table: business_units Column: id |
| 121 | last_sign_in | timestamp: SQL |  | Last access / sign in for the project. Currently, this field is updated when a user logs into the following services on the Web: (BIM 360) Account Admin, (BIM 360) Project Admin, Document Management, Classic Field, Classic Plan. No other services or mobile applications update Last Sign-in at this time. |
| 122 | created_at | timestamp: SQL |  | Time project was created Column used for filtering Date Range Extraction requests |
| 123 | acc_project | boolean |  | Indicator if this is an ACC Project versus a BIM 360 Project |
| 124 | latitude | number |  | Latitude for the project site |
| 125 | longitude | number |  | Longitude for the project site |
| 126 | updated_at | timestamp: SQL |  | Time project was last updated Column used for filtering Date Range Extraction requests |
| 127 | status_reason | string |  | Reason for the current project status |
| 128 | total_member_size | number |  | Total active members within the project. NOTE: This is not real time data |
| 129 | total_company_size | number |  | Total active companies within the project. NOTE: This is not real time data |
| 130 | classification | string | Possible Values: component production sample template | Project Classification |
| 131 | deleted_at | timestamp: SQL |  | Timestamp when the project was deleted Column used for filtering Date Range Extraction requests |
| 132 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## roles

The industry roles for use in BIM 360. - This is the Change Data Capture (CDC) enabled version of the admin.roles table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 133 | id | string: UUID |  | The ID of the Role |
| 134 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 135 | name | string | Max length: 255 | The Name of the Role |
| 136 | status | enum: string | Possible Values: active inactive | Status of the Role |
| 137 | created_at | timestamp: SQL |  | Timestamp when the role was created Column used for filtering Date Range Extraction requests |
| 138 | updated_at | timestamp: SQL |  | Timestamp when the role was updated Column used for filtering Date Range Extraction requests |
| 139 | deleted_at | timestamp: SQL |  | Timestamp when the role was deleted Column used for filtering Date Range Extraction requests |
| 140 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## users

Users in BIM 360. - This is the Change Data Capture (CDC) enabled version of the admin.users table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 141 | id | string: UUID |  | The HQ User ID |
| 142 | autodesk_id | string | Max length: 255 | Autodesk User ID |
| 143 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 144 | email | string | Max length: 255 | Email address for the user |
| 145 | name | string | Max length: 255 | Name for the user |
| 146 | first_name | string | Max length: 255 | First name of the user |
| 147 | last_name | string | Max length: 255 | Last name of the user |
| 148 | address_line1 | string | Max length: 255 | User specified address |
| 149 | address_line2 | string | Max length: 255 | User specified address |
| 150 | city | string | Max length: 255 | City for the user address |
| 151 | state_or_province | string | Max length: 255 | State for the user address |
| 152 | postal_code | string | Max length: 255 | Postal code for the address |
| 153 | country | string | Max length: 255 | Country for the user |
| 154 | last_sign_in | timestamp: SQL |  | Last time the user has signed in to BIM 360. Currently, this field is updated when a user logs into the following services on the Web: (BIM 360) Account Admin, (BIM 360) Project Admin, Document Management, Classic Field, Classic Plan. No other services or mobile applications update Last Sign-in at this time. |
| 155 | phone | string | Max length: 255 | Phone number for the user |
| 156 | job_title | string | Max length: 255 | User specified job title |
| 157 | access_level_account_admin | boolean |  | Account Administrator |
| 158 | access_level_project_admin | boolean |  | Indicates the user is a project admin for at least 1 active project |
| 159 | access_level_project_member | boolean |  | Indicates the user is participating in at least 1 active project in which they are not an admin |
| 160 | access_level_executive | boolean |  | Account Executive |
| 161 | default_role_id | string: UUID | Max length: 255 | ID of the account role to set when adding users to additional projects. For example if this ID is for 'Architect' then by default the user will be set to an 'Architect' role in any projects. |
| 162 | default_company_id | string: UUID | Max length: 255 | ID of the company ID to set when adding users to additional projects. |
| 163 | status | string | Possible Values: active inactive | Current status of a user in the account |
| 164 | status_reason | string |  | Reason for the current user status in the account |
| 165 | created_at | timestamp: SQL |  | Time user was added to the account Column used for filtering Date Range Extraction requests |
| 166 | updated_at | timestamp: SQL |  | Last time the user record was updated Column used for filtering Date Range Extraction requests |
| 167 | deleted_at | timestamp: SQL |  | Timestamp when the user was deleted Column used for filtering Date Range Extraction requests |
| 168 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

© Copyright 2025 Autodesk Inc. | [Autodesk Construction Cloud](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
