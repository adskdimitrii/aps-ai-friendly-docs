# dailylogs Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=dailylogs&format=html

---

# dailylogs Schema Description

**Documentation Updated:** 2023-12-04  

- [dailylogs](#dailylogs)
- [labor_items](#labor_items)
- [labors](#labors)
- [notes](#notes)
- [weather_logs](#weather_logs)

## dailylogs

BIM 360 Daily Logs

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The unique identifier of the dailylog. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | date | timestamp: SQL |  | The date for the daily log data |
| 5 | company_id | string |  | Company Identifier |
| 6 | status | string | Possible Values: NEW IN_PROGRESS PUBLISHED | Status of the daily log |
| 7 | created_by | string |  | Autodesk ID of the user who created the dailylog. |
| 8 | updated_by | string |  | Autodesk ID of the user who last modified the dailylog. |
| 9 | published_by | string |  | Autodesk ID of the user who published the dailylog. |
| 10 | created_at | timestamp: SQL |  | Date and time the resource was last created in ISO8601 format. |
| 11 | updated_at | timestamp: SQL |  | Date and time the resource was last updated in ISO8601 format. |
| 12 | published_at | timestamp: SQL |  | Date and time the resource was last published in ISO8601 format. |

## labor_items

Labor items for the labor in the Daily Log

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The unique identifier of the labor information. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | company_id | string: UUID |  | The company ID for the labor item - details for the company are available in admin::companies table |
| 5 | labor_id | string |  | ID of the labor for this labor item information Foreign Key: Table: labors Column: id |
| 6 | company_oxygen_id | string |  | Oxygen ID for the labor company |
| 7 | workers_count | number |  | Workers hours |
| 8 | total_hours | number |  | Total hours |
| 9 | comment | string |  | Comment for the labor item |
| 10 | created_by | string |  | Autodesk ID of the user who created the labo item information. |
| 11 | updated_by | string |  | Autodesk ID of the user who last modified the labor item information. |
| 12 | created_at | timestamp: SQL |  | Date and time the resource was last created in ISO8601 format. |
| 13 | updated_at | timestamp: SQL |  | Date and time the resource was last updated in ISO8601 format. |

## labors

Labor information for the Daily Log

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The unique identifier of the labor information. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | daily_log_id | string |  | ID of the dailylog for this labor information Foreign Key: Table: dailylogs Column: id |
| 5 | title | string |  | Title of the labor |
| 6 | created_by | string |  | Autodesk ID of the user who created the labor information. |
| 7 | updated_by | string |  | Autodesk ID of the user who last modified the labor information. |
| 8 | created_at | timestamp: SQL |  | Date and time the resource was last created in ISO8601 format. |
| 9 | updated_at | timestamp: SQL |  | Date and time the resource was last updated in ISO8601 format. |

## notes

Notes for the Daily Log

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The unique identifier of the note. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | daily_log_id | string |  | ID of the dailylog for this note Foreign Key: Table: dailylogs Column: id |
| 5 | title | string |  | Title for the note |
| 6 | content | string |  | Content of the note |
| 7 | created_by | string |  | Autodesk ID of the user who created the note. |
| 8 | updated_by | string |  | Autodesk ID of the user who last modified the note. |
| 9 | created_at | timestamp: SQL |  | Date and time the resource was last created in ISO8601 format. |
| 10 | updated_at | timestamp: SQL |  | Date and time the resource was last updated in ISO8601 format. |

## weather_logs

Weather information for a Daily Log

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The unique identifier of the weather information. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | daily_log_id | string |  | ID of the dailylog for this weather information Foreign Key: Table: dailylogs Column: id |
| 5 | title | string |  | Title of the weather reading |
| 6 | location | string |  | Location for the weather reading |
| 7 | description | string |  | Description of the weather reading |
| 8 | highest_temperature | number |  | High Temperature for the dailylog |
| 9 | highest_temperature_time | timestamp: SQL |  | Date and time of the highest temperature reading. |
| 10 | lowest_temperature | number |  | Low Temperature for the dailylog |
| 11 | lowest_temperature_time | timestamp: SQL |  | Date and time of the lowest temperature reading. |
| 12 | visibility | number |  | Visibility reading |
| 13 | humidity | number |  | Humidity reading |
| 14 | wind | number |  | Wind speed reading |
| 15 | precipitation | number |  | Precipitation in dailylog |
| 16 | notes | string |  | Various informational notes |
| 17 | created_by | string |  | Autodesk ID of the user who created the weather information. |
| 18 | updated_by | string |  | Autodesk ID of the user who last modified the weather information. |
| 19 | created_at | timestamp: SQL |  | Date and time the resource was last created in ISO8601 format. |
| 20 | updated_at | timestamp: SQL |  | Date and time the resource was last updated in ISO8601 format. |

© Copyright 2026 Autodesk Inc. | [Autodesk Construction Cloud](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
