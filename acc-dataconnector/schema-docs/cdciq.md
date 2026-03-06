# cdciq Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=cdciq&format=html

---

# cdciq Schema Description

**Documentation Updated:** 2025-11-21  

- [company_daily_quality_risk_changes](#company_daily_quality_risk_changes)
- [company_daily_safety_risk_changes](#company_daily_safety_risk_changes)
- [cost_impact_issues](#cost_impact_issues)
- [design_issues_building_components](#design_issues_building_components)
- [design_issues_root_cause](#design_issues_root_cause)
- [inspection_risk_issues](#inspection_risk_issues)
- [issues_quality_categories](#issues_quality_categories)
- [issues_quality_risks](#issues_quality_risks)
- [issues_safety_hazard](#issues_safety_hazard)
- [issues_safety_observations](#issues_safety_observations)
- [issues_safety_risk](#issues_safety_risk)
- [project_daily_quality_risk_changes](#project_daily_quality_risk_changes)
- [rfis_building_components](#rfis_building_components)
- [rfis_disciplines](#rfis_disciplines)
- [rfis_high_risk](#rfis_high_risk)
- [rfis_root_cause](#rfis_root_cause)

**Beta Release**  
This is a Beta release of the cdciq data set and schema definitions are subject to change or even possibly be removed from the final data set release. Thank you for your understanding with any future schema updates.

## company_daily_quality_risk_changes

Company Daily Risk Changes Description - This is the Change Data Capture (CDC) enabled version of the iq.company_daily_quality_risk_changes table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Id |
| 2 | company_id | string: UUID |  | Company Id |
| 3 | bim360_account_id | string: UUID |  | Account Id |
| 4 | bim360_project_id | string: UUID |  | Project Id |
| 5 | start_time | timestamp: SQL |  | Start Time |
| 6 | daily_risk | string |  | Daily Risk |
| 7 | daily_risk_indicator | number |  | Daily Risk Indicator |
| 8 | created_at | timestamp: SQL |  | Created At Column used for filtering Date Range Extraction requests |
| 9 | updated_at | timestamp: SQL |  | Updated At Column used for filtering Date Range Extraction requests |
| 10 | deleted_at | timestamp: SQL |  | Timestamp when the company_daily_quality_risk_change was deleted Column used for filtering Date Range Extraction requests |
| 11 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## company_daily_safety_risk_changes

Company Daily Safety Risk Changes Description - This is the Change Data Capture (CDC) enabled version of the iq.company_daily_safety_risk_changes table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Id |
| 2 | company_id | string: UUID |  | Company Id |
| 3 | bim360_account_id | string: UUID |  | Account Id |
| 4 | bim360_project_id | string: UUID |  | Project Id |
| 5 | start_date | timestamp: SQL |  | Start Date |
| 6 | daily_safety_risk | number |  | Daily Safety Risk |
| 7 | daily_safety_risk_indicator | number |  | Daily Safety Risk Indicator |
| 8 | created_at | timestamp: SQL |  | Created At Column used for filtering Date Range Extraction requests |
| 9 | updated_at | timestamp: SQL |  | Updated At Column used for filtering Date Range Extraction requests |
| 10 | deleted_at | timestamp: SQL |  | Timestamp when the company_daily_safety_risk_change was deleted Column used for filtering Date Range Extraction requests |
| 11 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## cost_impact_issues

Cost Impact Issues Description - This is the Change Data Capture (CDC) enabled version of the iq.cost_impact_issues table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Issue Id |
| 2 | issue_updated_at | timestamp: SQL |  | Issues score timestamp |
| 3 | updated_at | timestamp: SQL |  | Updated At Column used for filtering Date Range Extraction requests |
| 4 | cost_impact | string |  | Cost Impact: High Medium Low |
| 5 | bim360_account_id | string: UUID |  | Account Id |
| 6 | bim360_project_id | string: UUID |  | Project Id |
| 7 | created_at | timestamp: SQL |  | Timestamp when the cost_impact_issue was created Column used for filtering Date Range Extraction requests |
| 8 | deleted_at | timestamp: SQL |  | Timestamp when the cost_impact_issue was deleted Column used for filtering Date Range Extraction requests |
| 9 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## design_issues_building_components

Design Issues Building Components Description - This is the Change Data Capture (CDC) enabled version of the iq.design_issues_building_components table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Issue Id |
| 2 | issue_updated_at | timestamp: SQL |  | Issue score updated at |
| 3 | updated_at | timestamp: SQL |  | Updated At Column used for filtering Date Range Extraction requests |
| 4 | building_components_keywords | string |  | Building components keywords |
| 5 | bim360_account_id | string: UUID |  | Account Id |
| 6 | bim360_project_id | string: UUID |  | Project Id |
| 7 | building_components | string |  | Building Components set by user |
| 8 | user_building_components | string |  | User building components |
| 9 | created_at | timestamp: SQL |  | Timestamp when the design_issues_building_component was created Column used for filtering Date Range Extraction requests |
| 10 | deleted_at | timestamp: SQL |  | Timestamp when the design_issues_building_component was deleted Column used for filtering Date Range Extraction requests |
| 11 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## design_issues_root_cause

Design Issues Root Cause Description - This is the Change Data Capture (CDC) enabled version of the iq.design_issues_root_cause table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Issue Id |
| 2 | issue_updated_at | timestamp: SQL |  | Timestamp when root cause set |
| 3 | updated_at | timestamp: SQL |  | Updated At Column used for filtering Date Range Extraction requests |
| 4 | bim360_account_id | string: UUID |  | Account Id |
| 5 | bim360_project_id | string: UUID |  | Project Id |
| 6 | root_causes | string |  | Root causes |
| 7 | user_root_causes | string |  | User root causes |
| 8 | created_at | timestamp: SQL |  | Timestamp when the design_issues_root_cause was created Column used for filtering Date Range Extraction requests |
| 9 | deleted_at | timestamp: SQL |  | Timestamp when the design_issues_root_cause was deleted Column used for filtering Date Range Extraction requests |
| 10 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## inspection_risk_issues

Inspection Risk Issues Description - This is the Change Data Capture (CDC) enabled version of the iq.inspection_risk_issues table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Issue Id |
| 2 | issue_updated_at | timestamp: SQL |  | Issue updated at |
| 3 | updated_at | timestamp: SQL |  | Updated At Column used for filtering Date Range Extraction requests |
| 4 | inspection_risk | boolean |  | Inspection Risk |
| 5 | bim360_account_id | string: UUID |  | Account Id |
| 6 | bim360_project_id | string: UUID |  | Project Id |
| 7 | user_categories | string |  | Categories set by user |
| 8 | created_at | timestamp: SQL |  | Timestamp when the inspection_risk_issue was created Column used for filtering Date Range Extraction requests |
| 9 | deleted_at | timestamp: SQL |  | Timestamp when the inspection_risk_issue was deleted Column used for filtering Date Range Extraction requests |
| 10 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## issues_quality_categories

Issues Categories Description - This is the Change Data Capture (CDC) enabled version of the iq.issues_quality_categories table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Issue Id |
| 2 | updated_at | timestamp: SQL |  | Updated At Column used for filtering Date Range Extraction requests |
| 3 | issue_updated_at | timestamp: SQL |  | Issue updated at |
| 4 | category | string |  | Categories |
| 5 | user_category | string |  | Categories set by user |
| 6 | bim360_account_id | string: UUID |  | Account Id |
| 7 | bim360_project_id | string: UUID |  | Project Id |
| 8 | created_at | timestamp: SQL |  | Timestamp when the issues_quality_categorie was created Column used for filtering Date Range Extraction requests |
| 9 | deleted_at | timestamp: SQL |  | Timestamp when the issues_quality_categorie was deleted Column used for filtering Date Range Extraction requests |
| 10 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## issues_quality_risks

Issues Risks Description - This is the Change Data Capture (CDC) enabled version of the iq.issues_quality_risks table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Issue Id |
| 2 | updated_at | timestamp: SQL |  | Updated At Column used for filtering Date Range Extraction requests |
| 3 | risk | string |  | Risk |
| 4 | issue_updated_at | timestamp: SQL |  | Issues updated at |
| 5 | bim360_account_id | string: UUID |  | Account Id |
| 6 | bim360_project_id | string: UUID |  | Project Id |
| 7 | user_risk | string |  | User Risk |
| 8 | created_at | timestamp: SQL |  | Timestamp when the issues_quality_risk was created Column used for filtering Date Range Extraction requests |
| 9 | deleted_at | timestamp: SQL |  | Timestamp when the issues_quality_risk was deleted Column used for filtering Date Range Extraction requests |
| 10 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## issues_safety_hazard

Issues Safety Hazard Description - This is the Change Data Capture (CDC) enabled version of the iq.issues_safety_hazard table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Issue Id |
| 2 | issue_updated_at | timestamp: SQL |  | Issue updated at |
| 3 | updated_at | timestamp: SQL |  | Updated At Column used for filtering Date Range Extraction requests |
| 4 | safety_hazard_categories | string |  | Safety Hazard Categories |
| 5 | bim360_account_id | string: UUID |  | Account Id |
| 6 | bim360_project_id | string: UUID |  | Project Id |
| 7 | created_at | timestamp: SQL |  | Timestamp when the issues_safety_hazard was created Column used for filtering Date Range Extraction requests |
| 8 | deleted_at | timestamp: SQL |  | Timestamp when the issues_safety_hazard was deleted Column used for filtering Date Range Extraction requests |
| 9 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## issues_safety_observations

Issues Safety Observations Description - This is the Change Data Capture (CDC) enabled version of the iq.issues_safety_observations table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Issue Id |
| 2 | issue_updated_at | timestamp: SQL |  | Issues updated at |
| 3 | updated_at | timestamp: SQL |  | Updated At Column used for filtering Date Range Extraction requests |
| 4 | safety_observation_category | string |  | Safety Observation Category |
| 5 | bim360_account_id | string: UUID |  | Account Id |
| 6 | bim360_project_id | string: UUID |  | Project Id |
| 7 | created_at | timestamp: SQL |  | Timestamp when the issues_safety_observation was created Column used for filtering Date Range Extraction requests |
| 8 | deleted_at | timestamp: SQL |  | Timestamp when the issues_safety_observation was deleted Column used for filtering Date Range Extraction requests |
| 9 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## issues_safety_risk

Issues Safety Risk Description - This is the Change Data Capture (CDC) enabled version of the iq.issues_safety_risk table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Issue Id |
| 2 | issue_updated_at | timestamp: SQL |  | Issue updated at |
| 3 | updated_at | timestamp: SQL |  | Updated At Column used for filtering Date Range Extraction requests |
| 4 | safety_risk_category | string |  | Safety Risk Category: Fall, Electrocution, Struck by, caught in between, fire, other |
| 5 | bim360_account_id | string: UUID |  | Account Id |
| 6 | bim360_project_id | string: UUID |  | Project Id |
| 7 | created_at | timestamp: SQL |  | Timestamp when the issues_safety_risk was created Column used for filtering Date Range Extraction requests |
| 8 | deleted_at | timestamp: SQL |  | Timestamp when the issues_safety_risk was deleted Column used for filtering Date Range Extraction requests |
| 9 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## project_daily_quality_risk_changes

Project Daily Risk Changes Description - This is the Change Data Capture (CDC) enabled version of the iq.project_daily_quality_risk_changes table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Id |
| 2 | bim360_account_id | string: UUID |  | Account Id |
| 3 | bim360_project_id | string: UUID |  | Project Id |
| 4 | start_time | timestamp: SQL |  | Project Start Time |
| 5 | daily_risk | string |  | Daily Risk: Low, Medium, High |
| 6 | daily_risk_indicator | number |  | Daily Risk Indicator |
| 7 | created_at | timestamp: SQL |  | Created At Column used for filtering Date Range Extraction requests |
| 8 | updated_at | timestamp: SQL |  | Updated At Column used for filtering Date Range Extraction requests |
| 9 | deleted_at | timestamp: SQL |  | Timestamp when the project_daily_quality_risk_change was deleted Column used for filtering Date Range Extraction requests |
| 10 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## rfis_building_components

RFIs Building Components Description - This is the Change Data Capture (CDC) enabled version of the iq.rfis_building_components table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | RFI Id |
| 2 | rfi_updated_at | timestamp: SQL |  | RFI updated at |
| 3 | updated_at | timestamp: SQL |  | Updated At Column used for filtering Date Range Extraction requests |
| 4 | building_components | string |  | Building Components |
| 5 | building_components_keywords | string |  | Building Components Keywords |
| 6 | bim360_account_id | string: UUID |  | Account Id |
| 7 | bim360_project_id | string: UUID |  | Project Id |
| 8 | created_at | timestamp: SQL |  | Timestamp when the rfis_building_component was created Column used for filtering Date Range Extraction requests |
| 9 | deleted_at | timestamp: SQL |  | Timestamp when the rfis_building_component was deleted Column used for filtering Date Range Extraction requests |
| 10 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## rfis_disciplines

RFIs Disciplines Description - This is the Change Data Capture (CDC) enabled version of the iq.rfis_disciplines table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | RFI Id |
| 2 | rfi_updated_at | timestamp: SQL |  | RFI updated at |
| 3 | updated_at | timestamp: SQL |  | Updated At Column used for filtering Date Range Extraction requests |
| 4 | disciplines | string |  | Disciplines |
| 5 | bim360_account_id | string: UUID |  | Account Id |
| 6 | bim360_project_id | string: UUID |  | Project Id |
| 7 | created_at | timestamp: SQL |  | Timestamp when the rfis_discipline was created Column used for filtering Date Range Extraction requests |
| 8 | deleted_at | timestamp: SQL |  | Timestamp when the rfis_discipline was deleted Column used for filtering Date Range Extraction requests |
| 9 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## rfis_high_risk

RFIs High Risk Description - This is the Change Data Capture (CDC) enabled version of the iq.rfis_high_risk table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | RFI Id |
| 2 | rfi_updated_at | timestamp: SQL |  | RFI updated at |
| 3 | updated_at | timestamp: SQL |  | Updated At Column used for filtering Date Range Extraction requests |
| 4 | risk | string |  | Risk |
| 5 | score | number |  | Score |
| 6 | bim360_account_id | string: UUID |  | Account Id |
| 7 | bim360_project_id | string: UUID |  | Project Id |
| 8 | created_at | timestamp: SQL |  | Timestamp when the rfis_high_risk was created Column used for filtering Date Range Extraction requests |
| 9 | deleted_at | timestamp: SQL |  | Timestamp when the rfis_high_risk was deleted Column used for filtering Date Range Extraction requests |
| 10 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## rfis_root_cause

RFIs Root Cause Description - This is the Change Data Capture (CDC) enabled version of the iq.rfis_root_cause table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | RFI Id |
| 2 | rfi_updated_at | timestamp: SQL |  | RFI updated at |
| 3 | updated_at | timestamp: SQL |  | Updated At Column used for filtering Date Range Extraction requests |
| 4 | root_causes | string |  | Root causes |
| 5 | bim360_account_id | string: UUID |  | Account Id |
| 6 | bim360_project_id | string: UUID |  | Project Id |
| 7 | created_at | timestamp: SQL |  | Timestamp when the rfis_root_cause was created Column used for filtering Date Range Extraction requests |
| 8 | deleted_at | timestamp: SQL |  | Timestamp when the rfis_root_cause was deleted Column used for filtering Date Range Extraction requests |
| 9 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

© Copyright 2026 Autodesk Inc. | [Autodesk Construction Cloud](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
