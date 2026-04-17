# iq Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=iq&format=html

---

# iq Schema Description

**Documentation Updated:** 2023-12-04  

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

## company_daily_quality_risk_changes

Company Daily Risk Changes Description

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Id |
| 2 | company_id | string: UUID |  | Company Id |
| 3 | bim360_account_id | string: UUID |  | Account Id |
| 4 | bim360_project_id | string: UUID |  | Project Id |
| 5 | start_time | timestamp: SQL |  | Start Time |
| 6 | daily_risk | string |  | Daily Risk |
| 7 | daily_risk_indicator | number |  | Daily Risk Indicator |
| 8 | created_at | timestamp: SQL |  | Created At |
| 9 | updated_at | timestamp: SQL |  | Updated At |

## company_daily_safety_risk_changes

Company Daily Safety Risk Changes Description

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Id |
| 2 | company_id | string: UUID |  | Company Id |
| 3 | bim360_account_id | string: UUID |  | Account Id |
| 4 | bim360_project_id | string: UUID |  | Project Id |
| 5 | start_date | timestamp: SQL |  | Start Date |
| 6 | daily_safety_risk | number |  | Daily Safety Risk |
| 7 | daily_safety_risk_indicator | number |  | Daily Safety Risk Indicator |
| 8 | created_at | timestamp: SQL |  | Created At |
| 9 | updated_at | timestamp: SQL |  | Updated At |

## cost_impact_issues

Cost Impact Issues Description

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Issue Id |
| 2 | updated_at | timestamp: SQL |  | Updated At |
| 3 | predicted_at | timestamp: SQL |  | Predicted At |
| 4 | cost_impact | string |  | Cost Impact: High Medium Low |
| 5 | bim360_account_id | string: UUID |  | Account Id |
| 6 | bim360_project_id | string: UUID |  | Project Id |

## design_issues_building_components

Design Issues Building Components Description

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Issue Id |
| 2 | updated_at | timestamp: SQL |  | Updated At |
| 3 | predicted_at | timestamp: SQL |  | Predicted At |
| 4 | building_component | string |  | Building Components |
| 5 | user_building_component | string |  | Building Components ser by user |
| 6 | building_component_keyword | string |  | Building Components Keywords |
| 7 | bim360_account_id | string: UUID |  | Account Id |
| 8 | bim360_project_id | string: UUID |  | Project Id |

## design_issues_root_cause

Design Issues Root Cause Description

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Issue Id |
| 2 | updated_at | timestamp: SQL |  | Updated At |
| 3 | predicted_at | timestamp: SQL |  | Predicted At |
| 4 | root_cause | string |  | Root Causes |
| 5 | user_root_cause | string |  | Root Causes set by user |
| 6 | bim360_account_id | string: UUID |  | Account Id |
| 7 | bim360_project_id | string: UUID |  | Project Id |

## inspection_risk_issues

Inspection Risk Issues Description

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Issue Id |
| 2 | updated_at | timestamp: SQL |  | Updated At |
| 3 | predicted_at | timestamp: SQL |  | Predicted At |
| 4 | inspection_risk | boolean |  | Inspection Risk |
| 5 | user_category | string |  | Categories set by user |
| 6 | bim360_account_id | string: UUID |  | Account Id |
| 7 | bim360_project_id | string: UUID |  | Project Id |

## issues_quality_categories

Issues Categories Description

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Issue Id |
| 2 | predicted_at | timestamp: SQL |  | Predicted At |
| 3 | updated_at | timestamp: SQL |  | Updated At |
| 4 | category | string |  | Categories |
| 5 | user_category | string |  | Categories set by user |
| 6 | bim360_account_id | string: UUID |  | Account Id |
| 7 | bim360_project_id | string: UUID |  | Project Id |

## issues_quality_risks

Issues Risks Description

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Issue Id |
| 2 | predicted_at | timestamp: SQL |  | Predicted At |
| 3 | risk | string |  | Risk |
| 4 | updated_at | timestamp: SQL |  | Updated At |
| 5 | bim360_account_id | string: UUID |  | Account Id |
| 6 | bim360_project_id | string: UUID |  | Project Id |
| 7 | user_risk | string |  | User Risk |

## issues_safety_hazard

Issues Safety Hazard Description

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Issue Id |
| 2 | updated_at | timestamp: SQL |  | Updated At |
| 3 | predicted_at | timestamp: SQL |  | Predicted At |
| 4 | safety_hazard_category | string |  | Safety Hazard Categories |
| 5 | bim360_account_id | string: UUID |  | Account Id |
| 6 | bim360_project_id | string: UUID |  | Project Id |

## issues_safety_observations

Issues Safety Observations Description

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Issue Id |
| 2 | updated_at | timestamp: SQL |  | Updated At |
| 3 | predicted_at | timestamp: SQL |  | Predicted At |
| 4 | safety_observation_category | string |  | Safety Observation Category |
| 5 | bim360_account_id | string: UUID |  | Account Id |
| 6 | bim360_project_id | string: UUID |  | Project Id |

## issues_safety_risk

Issues Safety Risk Description

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Issue Id |
| 2 | updated_at | timestamp: SQL |  | Updated At |
| 3 | predicted_at | timestamp: SQL |  | Predicted At |
| 4 | safety_risk_category | string |  | Safety Risk Category: Fall, Electrocution, Struck by, caught in between, fire, other |
| 5 | bim360_account_id | string: UUID |  | Account Id |
| 6 | bim360_project_id | string: UUID |  | Project Id |

## project_daily_quality_risk_changes

Project Daily Risk Changes Description

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Id |
| 2 | bim360_account_id | string: UUID |  | Account Id |
| 3 | bim360_project_id | string: UUID |  | Project Id |
| 4 | start_time | timestamp: SQL |  | Project Start Time |
| 5 | daily_risk | string |  | Daily Risk: Low, Medium, High |
| 6 | daily_risk_indicator | number |  | Daily Risk Indicator |
| 7 | created_at | timestamp: SQL |  | Created At |
| 8 | updated_at | timestamp: SQL |  | Updated At |

## rfis_building_components

RFIs Building Components Description

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | RFI Id |
| 2 | updated_at | timestamp: SQL |  | Updated At |
| 3 | predicted_at | timestamp: SQL |  | Predicted At |
| 4 | building_component | string |  | Building Components |
| 5 | building_component_keyword | string |  | Building Components Keywords |
| 6 | bim360_account_id | string: UUID |  | Account Id |
| 7 | bim360_project_id | string: UUID |  | Project Id |

## rfis_disciplines

RFIs Disciplines Description

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | RFI Id |
| 2 | updated_at | timestamp: SQL |  | Updated At |
| 3 | predicted_at | timestamp: SQL |  | Predicted At |
| 4 | discipline | string |  | Disciplines |
| 5 | bim360_account_id | string: UUID |  | Account Id |
| 6 | bim360_project_id | string: UUID |  | Project Id |

## rfis_high_risk

RFIs High Risk Description

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | RFI Id |
| 2 | updated_at | timestamp: SQL |  | Updated At |
| 3 | predicted_at | timestamp: SQL |  | Predicted At |
| 4 | risk | string |  | Risk |
| 5 | score | number |  | Score |
| 6 | bim360_account_id | string: UUID |  | Account Id |
| 7 | bim360_project_id | string: UUID |  | Project Id |

## rfis_root_cause

RFIs Root Cause Description

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | RFI Id |
| 2 | updated_at | timestamp: SQL |  | Updated At |
| 3 | predicted_at | timestamp: SQL |  | Predicted At |
| 4 | root_cause | string |  | Root Causes |
| 5 | bim360_account_id | string: UUID |  | Account Id |
| 6 | bim360_project_id | string: UUID |  | Project Id |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
