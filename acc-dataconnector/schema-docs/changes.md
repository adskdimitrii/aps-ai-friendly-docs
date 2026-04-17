# ACC Data Schema Changes

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=changes&format=html

---

# ACC Data Schema Changes

This document details changes made to the ACC Data Schema. The changes are listed chronologically in descending order so changes that are listed first are the most recent.
The following describes the columns included for each schema change and the meanings of tag values for the changes:

- **service_group**: name of the service group
- **table**: table definition
- **column**: specific data column
- **change_type**: type of change being made, with the change options being as follows:
  * ADDED: an entity was added
  * MODIFIED: an entity was modified
  * DEPRECATED: an entity was deprecated - it will still appear in the schema, but the data can no longer be relied upon
  * DELETED: an entity was removed from the schema
  * NOTICE: a general notice that informs users of upcoming changes to the schema
- **notes**: additional notes for the schema change
- **watermark**: watermark number for the change set - this can be used to see the changes that were grouped together in a release  
*Note: the colors have no meaning other than to to help visually group changes*

## March, 2026

The following changes were made to the ACC Data Schema during the month of March, 2026

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
| cdcschedule | plan_tasks |  | ADDED | plan_tasks table added to the schema. | 1773188741 |
| cdcschedule | plan_task_comments |  | ADDED | plan_task_comments table added to the schema. | 1773188741 |
| cdcschedule | plan_project_settings |  | ADDED | plan_project_settings table added to the schema. | 1773188741 |
| cdcschedule | plan_plans |  | ADDED | plan_plans table added to the schema. | 1773188741 |
| cdcschedule | plan_handoffs |  | ADDED | plan_handoffs table added to the schema. | 1773188741 |
| cdcschedule | plan_commitments |  | ADDED | plan_commitments table added to the schema. | 1773188741 |
| schedule | plan_tasks |  | ADDED | plan_tasks table added to the schema. | 1773188741 |
| schedule | plan_task_comments |  | ADDED | plan_task_comments table added to the schema. | 1773188741 |
| schedule | plan_project_settings |  | ADDED | plan_project_settings table added to the schema. | 1773188741 |
| schedule | plan_plans |  | ADDED | plan_plans table added to the schema. | 1773188741 |
| schedule | plan_handoffs |  | ADDED | plan_handoffs table added to the schema. | 1773188741 |
| schedule | plan_commitments |  | ADDED | plan_commitments table added to the schema. | 1773188741 |
| admin | business_units | path | ADDED | Column added to the business_units table in the schema. | 1773188741 |

## February, 2026

The following changes were made to the ACC Data Schema during the month of February, 2026

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| forms | weather_hours | hour | MODIFIED | Changed data type from string to time | 1770238801 |
| cdcissues | viewables | guid | MODIFIED | Changed data type to string | 1770238801 |
| cdcissues | viewables | file_version | MODIFIED | Changed data type from string to number | 1770238801 |
| cdcissues | placements | created_at_version | MODIFIED | Changed data type from string to number | 1770238801 |
| issues | viewables | file_version | MODIFIED | Changed data type from string to number | 1770238801 |
| issues | placements | created_at_version | MODIFIED | Changed data type from string to number | 1770238801 |
| cost | cost_items | unit | ADDED | Column added to the cost_items table in the schema. | 1770238801 |
| cost | cost_items | quantity | ADDED | Column added to the cost_items table in the schema. | 1770238801 |
| forms | layouts | sequential_section_completion | ADDED | Column added to the layouts table in the schema. | 1770238801 |
| cost | expenses | payment_due | ADDED | Column added to the expenses table in the schema. | 1770238801 |
| cost | contracts | response_due | ADDED | Column added to the contracts table in the schema. | 1770238801 |
| issues | viewables |  | ADDED | viewables table added to the schema. | 1770238801 |
| issues | placements |  | ADDED | placements table added to the schema. | 1770238801 |
| cdcissues | viewables |  | ADDED | viewables table added to the schema. | 1770238801 |
| cdcissues | placements |  | ADDED | placements table added to the schema. | 1770238801 |
| cost | budgets | forecast_adjustment_qty | ADDED | Column added to the budgets table in the schema. | 1770238801 |
| forms | native_form_tabular_values | time_val | MODIFIED | Documentation has been updated to specify the column type as time | 1770238801 |
| cost | change_orders | compliance_status | ADDED | Column added to the change_orders table in the schema. | 1770238801 |
| cdcsubmittalsacc | parameters_collections | parameter_select_options | ADDED | Column added to the parameters_collections table in the schema. | 1770238801 |
| cdcsubmittalsacc | item_custom_attribute_value | select_value | ADDED | Column added to the item_custom_attribute_value table in the schema. | 1770238801 |
| cdccost | cost_items | is_markup | ADDED | Column added to the cost_items table in the schema. | 1770238801 |
| cdccost | budgets | locations | ADDED | Column added to the budgets table in the schema. | 1770238801 |

## December, 2025

The following changes were made to the ACC Data Schema during the month of December, 2025

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| classifications |  |  | ADDED | New service group added to the ACC Data Schema. | 1764879867 |
| cost | cost_items | is_markup | ADDED | Column added to the cost_items table in the schema. | 1764879867 |
| cost | cost_items | type | ADDED | Column added to the cost_items table in the schema. | 1764879867 |
| cost | budgets | locations | ADDED | Column added to the budgets table in the schema. | 1764879867 |
| submittalsacc | parameters_collections | parameter_select_options | ADDED | Column added to the parameters_collections table in the schema. | 1764879867 |
| submittalsacc | item_custom_attribute_value | select_value | ADDED | Column added to the item_custom_attribute_value table in the schema. | 1764879867 |

## November, 2025

The following changes were made to the ACC Data Schema during the month of November, 2025

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| cost | change_orders | committed | ADDED | Column added to the change_orders table in the schema. | 1762487866 |
| cost | change_orders | approved | ADDED | Column added to the change_orders table in the schema. | 1762487866 |
| cost | change_orders | submitted | ADDED | Column added to the change_orders table in the schema. | 1762487866 |
| cost | change_orders | proposed | ADDED | Column added to the change_orders table in the schema. | 1762487866 |
| cost | change_orders | estimated | ADDED | Column added to the change_orders table in the schema. | 1762487866 |
| cost | change_orders | unit | ADDED | Column added to the change_orders table in the schema. | 1762487866 |
| cost | change_orders | quantity | ADDED | Column added to the change_orders table in the schema. | 1762487866 |
| cost | cost_payments | compliance_status | ADDED | Column added to the cost_payments table in the schema. | 1762487866 |
| forms | native_form_values | field_id_v2 | ADDED | Column added to the native_form_values table in the schema. | 1762487866 |
| forms | native_form_tabular_values | field_id_v2 | ADDED | Column added to the native_form_tabular_values table in the schema. | 1762487866 |
| forms | layout_section_items | field_id_v2 | ADDED | Column added to the layout_section_items table in the schema. | 1762487866 |
| estimates |  |  | ADDED | New service group added to the ACC Data Schema. | 1762487866 |

## October, 2025

The following changes were made to the ACC Data Schema during the month of October, 2025

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| forms | native_form_values | updated_by | ADDED | Column added to the native_form_values table in the schema. | 1761069013 |
| forms | native_form_values | updated_at | ADDED | Column added to the native_form_values table in the schema. | 1761069013 |
| forms | native_form_tabular_values | time_val | ADDED | Column added to the native_form_tabular_values table in the schema. | 1761069013 |
| forms | native_form_tabular_values | date_val | ADDED | Column added to the native_form_tabular_values table in the schema. | 1761069013 |

## September, 2025

The following changes were made to the ACC Data Schema during the month of September, 2025

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| takeoff | classifications | parent_id | ADDED | Column added to the classifications table in the schema. | 1757008377 |
| cost | schedule_of_values_properties |  | ADDED | schedule_of_values_properties table added to the schema. | 1757008377 |

## August, 2025

The following changes were made to the ACC Data Schema during the month of August, 2025

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| reviews | reviews | is_archived | ADDED | Column added to the reviews table in the schema. | 1754496411 |
| admin | project_roles | role_id | ADDED | Column added to the project_roles table in the schema. | 1754496411 |
| submittalsacc | items | pending_actions_from | ADDED | Column added to the items table in the schema. | 1754496411 |
| cost | contracts | awarded_tax_total | ADDED | Column added to the contracts table in the schema. | 1754496411 |
| submittalsacc | parameters_collections |  | ADDED | parameters_collections table added to the schema. | 1754496411 |
| submittalsacc | item_custom_attribute_value |  | ADDED | item_custom_attribute_value table added to the schema. | 1754496411 |
| cost | distribution_item_curves | updated_at | ADDED | Column added to the distribution_item_curves table in the schema. | 1754496411 |
| cost | distribution_item_curves | created_at | ADDED | Column added to the distribution_item_curves table in the schema. | 1754496411 |

## July, 2025

The following changes were made to the ACC Data Schema during the month of July, 2025

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| issues | attachments |  | MODIFIED | Table now returns attachments information for ACC | 1751484544 |
| cost | sub_distribution_items | periods_input_qty | ADDED | Column added to the sub_distribution_items table in the schema. | 1751484544 |
| cost | sub_distribution_items | distribution_total_input_qty | ADDED | Column added to the sub_distribution_items table in the schema. | 1751484544 |
| cost | sub_distribution_items | actual_total_input_qty | ADDED | Column added to the sub_distribution_items table in the schema. | 1751484544 |
| cost | distribution_item_curves | periods_input_qty | ADDED | Column added to the distribution_item_curves table in the schema. | 1751484544 |
| cost | distribution_item_curves | distribution_total_input_qty | ADDED | Column added to the distribution_item_curves table in the schema. | 1751484544 |
| cost | distribution_item_curves | actual_total_input_qty | ADDED | Column added to the distribution_item_curves table in the schema. | 1751484544 |
| admin | users | last_sign_in | ADDED | Column added to the users table in the schema. Updated documentation | 1751484544 |
| admin | projects | last_sign_in | MODIFIED | Updated documentation | 1751484544 |
| activities | submittals_activities | target_package_spec_identifier | MODIFIED | Updated documentation | 1751484544 |
| takeoff |  |  | ADDED | New service group added to the ACC Data Schema. | 1751484544 |

## June, 2025

The following changes were made to the ACC Data Schema during the month of June, 2025

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| forms | native_form_tabular_values |  | ADDED | native_form_tabular_values table added to the schema. | 1749601965 |
| forms | layout_table_columns | expression | ADDED | Column added to the layout_table_columns table in the schema. | 1749601965 |
| forms | layout_table_columns | column_type | ADDED | Column added to the layout_table_columns table in the schema. | 1749601965 |
| forms | layout_table_columns | column_key | ADDED | Column added to the layout_table_columns table in the schema. | 1749601965 |
| cost | budgets | approved_budget_payment_application | ADDED | Column added to the budgets table in the schema. | 1749601965 |
| cost | budgets | approved_cost_payment_application | ADDED | Column added to the budgets table in the schema. | 1749601965 |

## May, 2025

The following changes were made to the ACC Data Schema during the month of May, 2025

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| cost | budgets | main_contract_item_amount | ADDED | Column added to the budgets table in the schema. | 1746644418 |
| cost | cost_items | submitted_tax_summary | ADDED | Column added to the cost_items table in the schema. | 1746644418 |
| cost | cost_items | proposed_tax_summary | ADDED | Column added to the cost_items table in the schema. | 1746644418 |
| cost | cost_items | estimated_tax_summary | ADDED | Column added to the cost_items table in the schema. | 1746644418 |

## April, 2025

The following changes were made to the ACC Data Schema during the month of April, 2025

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| submittalsacc | item_revision |  | ADDED | item_revision table added to the schema. | 1741976317 |
| cost | contracts | compliance_status | ADDED | Column added to the contracts table in the schema. | 1741976317 |
| issuesbim360 |  |  | ADDED | New service group added to the ACC Data Schema. Schema will only return BIM 360 project data. | 1741976317 |

## March, 2025

The following changes were made to the ACC Data Schema during the month of March, 2025

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| activities | bridge_activities |  | ADDED | bridge_activities table added to the schema. | 1741267987 |
| cost | budgets | code_segment_values | ADDED | Column added to the budgets table in the schema. | 1741267987 |
| cost | cost_payments | tax_summary | ADDED | Column added to the cost_payments table in the schema. | 1741267987 |
| cost | cost_payment_items | tax_summary | ADDED | Column added to the cost_payment_items table in the schema. | 1741267987 |
| cost | cost_items | committed_tax_summary | ADDED | Column added to the cost_items table in the schema. | 1741267987 |
| cost | cost_items | approved_tax_summary | ADDED | Column added to the cost_items table in the schema. | 1741267987 |

## February, 2025

The following changes were made to the ACC Data Schema during the month of February, 2025

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| activities | submittals_activities | target_type_identifier | MODIFIED | Documentation correction | 1739194331 |
| activities | submittals_activities | target_spec_identifier | MODIFIED | Documentation correction | 1739194331 |
| activities | submittals_activities | object_type_identifier | MODIFIED | Documentation correction | 1739194331 |
| activities | submittals_activities | object_spec_identifier | MODIFIED | Documentation correction | 1739194331 |
| forms | forms | last_submitted_by | ADDED | Column added to the forms table in the schema. | 1738769525 |
| packages | packages | version_resource_option | ADDED | Column added to the packages table in the schema. | 1738769525 |
| activities | assets_activities | object_before_category_id | MODIFIED | Documentation has been updated specify column type as string | 1738769525 |
| activities | assets_activities | object_deleted_entity_category_id | MODIFIED | Documentation has been updated specify column type as string | 1738769525 |
| activities | assets_activities | object_created_entity_category_id | MODIFIED | Documentation has been updated specify column type as string | 1738769525 |
| activities | assets_activities | object_category_id | MODIFIED | Documentation has been updated specify column type as string | 1738769525 |
| activities | assets_activities | object_before_entity_category_id | MODIFIED | Documentation has been updated specify column type as string | 1738769525 |
| transmittals | transmittal_non_members |  | ADDED | transmittal_non_members table added to the schema. | 1738769525 |
| cost | transferences | creator_id | MODIFIED | Documentation has been updated specify column type as string:UUID | 1738769525 |
| rfis | rfi_responses | state | ADDED | Column added to the rfi_responses table in the schema. | 1738769525 |
| rfis | rfis | bridged_target | ADDED | Column added to the rfis table in the schema. | 1738769525 |
| rfis | rfis | bridged_source | ADDED | Column added to the rfis table in the schema. | 1738769525 |

## January, 2025

The following changes were made to the ACC Data Schema during the month of January, 2025

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| cost | budgets | pending_internal_budget_transfer_input_qty | ADDED | Column added to the budgets table in the schema. | 1735843500 |
| cost | budgets | pending_internal_budget_transfer_qty | ADDED | Column added to the budgets table in the schema. | 1735843500 |
| cost | budgets | pending_internal_budget_transfer | ADDED | Column added to the budgets table in the schema. | 1735843500 |
| cost | contracts | pending_internal_budget_transfer | ADDED | Column added to the contracts table in the schema. | 1735843500 |
| cost | change_orders | main_contract_id | ADDED | Column added to the change_orders table in the schema. | 1735843500 |
| cost | change_orders | status_changed_at | ADDED | Column added to the change_orders table in the schema. | 1735843500 |
| cost | change_orders | approved_at | ADDED | Column added to the change_orders table in the schema. | 1735843500 |
| cost | transferences |  | ADDED | transferences table added to the schema. | 1735843500 |
| cost | budget_transfers |  | ADDED | budget_transfers table added to the schema. | 1735843500 |

## November, 2024

The following changes were made to the ACC Data Schema during the month of November, 2024

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| clashes | issue_clash_group |  | DELETED | Table has been removed from the schema | 1732120522 |
| clashes | closed_clash_group |  | MODIFIED | Schema design has been updated | 1732120522 |
| clashes | clash_test |  | MODIFIED | Schema design has been updated | 1732120522 |
| clashes | clash_group_to_clash_id |  | MODIFIED | Schema design has been updated | 1732120522 |
| clashes | assigned_clash_group |  | MODIFIED | Schema design has been updated | 1732120522 |
| cost | cost_items | schedule_change | ADDED | Column added to the cost_items table in the schema. | 1732120522 |

## October, 2024

The following changes were made to the ACC Data Schema during the month of October, 2024

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| cost | change_orders | source_type | ADDED | Column added to the change_orders table in the schema. | 1729864636 |
|  |
| cost | main_contracts | schedule_change | ADDED | Column added to the main_contracts table in the schema. | 1729018055 |
| cost | main_contracts | revised_completion_date | ADDED | Column added to the main_contracts table in the schema. | 1729018055 |
| cost | change_orders | proposed_revised_completion_date | ADDED | Column added to the change_orders table in the schema. | 1729018055 |

## September, 2024

The following changes were made to the ACC Data Schema during the month of September, 2024

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| rfis | rfi_transitions |  | ADDED | rfi_transitions table added to the schema. | 1727363823 |
|  |
| forms | native_form_section_item_attachments |  | ADDED | native_form_section_item_attachments table added to the schema. | 1725993657 |
| forms | form_field_attachments |  | ADDED | form_field_attachments table added to the schema. | 1725993657 |
|  |
| packages | package_associations | package_id | ADDED | Column added to the package_associations table in the schema. | 1725457146 |
| rfis | acc_attachments |  | ADDED | acc_attachments table added to the schema. | 1725457146 |
| cost | cost_payments | last_sync_time | ADDED | Column added to the cost_payments table in the schema. | 1725457146 |
| cost | cost_payments | message | ADDED | Column added to the cost_payments table in the schema. | 1725457146 |
| cost | cost_payments | external_system | ADDED | Column added to the cost_payments table in the schema. | 1725457146 |
| cost | cost_payments | external_id | ADDED | Column added to the cost_payments table in the schema. | 1725457146 |
| cost | cost_payments | integration_state_changed_at | ADDED | Column added to the cost_payments table in the schema. | 1725457146 |
| cost | cost_payments | integration_state | ADDED | Column added to the cost_payments table in the schema. | 1725457146 |
| cost | budget_payments | last_sync_time | ADDED | Column added to the budget_payments table in the schema. | 1725457146 |
| cost | budget_payments | message | ADDED | Column added to the budget_payments table in the schema. | 1725457146 |
| cost | budget_payments | external_system | ADDED | Column added to the budget_payments table in the schema. | 1725457146 |
| cost | budget_payments | external_id | ADDED | Column added to the budget_payments table in the schema. | 1725457146 |
| cost | budget_payments | integration_state_changed_at | ADDED | Column added to the budget_payments table in the schema. | 1725457146 |
| cost | budget_payments | integration_state | ADDED | Column added to the budget_payments table in the schema. | 1725457146 |

## August, 2024

The following changes were made to the ACC Data Schema during the month of August, 2024

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| activities | assets_activities | object_after_category_id | MODIFIED | Data type fix for documentation | 1722357095 |
| cost | sub_distribution_items |  | ADDED | sub_distribution_items table added to the schema. | 1722357095 |
| cost | distribution_items |  | ADDED | distribution_items table added to the schema. | 1722357095 |
| cost | distribution_item_curves |  | ADDED | distribution_item_curves table added to the schema. | 1722357095 |
| cost | main_contract_items |  | ADDED | main_contract_items table added to the schema. | 1722357095 |
| cost | expenses | last_sync_time | ADDED | Column added to the expenses table in the schema. | 1722357095 |
| cost | expenses | message | ADDED | Column added to the expenses table in the schema. | 1722357095 |
| cost | expenses | external_system | ADDED | Column added to the expenses table in the schema. | 1722357095 |
| cost | expenses | external_id | ADDED | Column added to the expenses table in the schema. | 1722357095 |
| cost | expenses | integration_state_changed_at | ADDED | Column added to the expenses table in the schema. | 1722357095 |
| cost | expenses | integration_state_changed_by | ADDED | Column added to the expenses table in the schema. | 1722357095 |
| cost | expenses | integration_state | ADDED | Column added to the expenses table in the schema. | 1722357095 |
| cost | contracts | last_sync_time | ADDED | Column added to the contracts table in the schema. | 1722357095 |
| cost | contracts | message | ADDED | Column added to the contracts table in the schema. | 1722357095 |
| cost | contracts | external_system | ADDED | Column added to the contracts table in the schema. | 1722357095 |
| cost | contracts | external_id | ADDED | Column added to the contracts table in the schema. | 1722357095 |
| cost | contracts | integration_state_changed_at | ADDED | Column added to the contracts table in the schema. | 1722357095 |
| cost | contracts | integration_state_changed_by | ADDED | Column added to the contracts table in the schema. | 1722357095 |
| cost | contracts | integration_state | ADDED | Column added to the contracts table in the schema. | 1722357095 |
| cost | change_orders | last_sync_time | ADDED | Column added to the change_orders table in the schema. | 1722357095 |
| cost | change_orders | message | ADDED | Column added to the change_orders table in the schema. | 1722357095 |
| cost | change_orders | external_system | ADDED | Column added to the change_orders table in the schema. | 1722357095 |
| cost | change_orders | external_id | ADDED | Column added to the change_orders table in the schema. | 1722357095 |
| cost | change_orders | integration_state_changed_at | ADDED | Column added to the change_orders table in the schema. | 1722357095 |
| cost | change_orders | integration_state_changed_by | ADDED | Column added to the change_orders table in the schema. | 1722357095 |
| cost | change_orders | integration_state | ADDED | Column added to the change_orders table in the schema. | 1722357095 |
| cost | budgets | last_sync_time | ADDED | Column added to the budgets table in the schema. | 1722357095 |
| cost | budgets | message | ADDED | Column added to the budgets table in the schema. | 1722357095 |
| cost | budgets | external_system | ADDED | Column added to the budgets table in the schema. | 1722357095 |
| cost | budgets | external_id | ADDED | Column added to the budgets table in the schema. | 1722357095 |
| cost | budgets | integration_state_changed_at | ADDED | Column added to the budgets table in the schema. | 1722357095 |
| cost | budgets | integration_state_changed_by | ADDED | Column added to the budgets table in the schema. | 1722357095 |
| cost | budgets | integration_state | ADDED | Column added to the budgets table in the schema. | 1722357095 |

## July, 2024

The following changes were made to the ACC Data Schema during the month of July, 2024

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| assets | systems |  | ADDED | systems table added to the schema. | 1721766926 |
| assets | system_memberships |  | ADDED | system_memberships table added to the schema. | 1721766926 |
| assets | category_status_set_assignments | category_type | ADDED | Column added to the category_status_set_assignments table in the schema. | 1721766926 |
| assets | categories | category_type | ADDED | Column added to the categories table in the schema. | 1721766926 |
| assets | categories | uid | ADDED | Column added to the categories table in the schema. | 1721766926 |
| transmittals | transmittal_recipients | downloaded_at | ADDED | Column added to the transmittal_recipients table in the schema. | 1721766926 |
| transmittals | transmittal_recipients | viewed_at | ADDED | Column added to the transmittal_recipients table in the schema. | 1721766926 |
| cost | permissions |  | ADDED | permissions table added to the schema. | 1721766926 |
|  |
| forms | forms | name | ADDED | Column added to the forms table in the schema. | 1719585181 |
| submittalsacc | attachments | urn | ADDED | Column added to the attachments table in the schema. | 1719427442 |

## June, 2024

The following changes were made to the ACC Data Schema during the month of June, 2024

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| cost | change_orders | schedule_change | ADDED | Column added to the change_orders table in the schema. | 1718126192 |
| reviews | reviews | total_steps | ADDED | Column added to the reviews table in the schema. | 1718126192 |
| reviews | reviews | current_step | ADDED | Column added to the reviews table in the schema. | 1718126192 |

## May, 2024

The following changes were made to the ACC Data Schema during the month of May, 2024

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| cost | contracts | exchange_rate | ADDED | Column added to the contracts table in the schema. | 1715086269 |
| cost | contracts | currency | ADDED | Column added to the contracts table in the schema. | 1715086269 |
| issues | root_causes | is_active | MODIFIED | Column changed to always returns TRUE, regardless of the real value. Will be deprecated in the future. | 1714668701 |
| issues | root_cause_categories | is_active | MODIFIED | Column changed to always returns TRUE, regardless of the real value. Will be deprecated in the future. | 1714668701 |

## April, 2024

The following changes were made to the ACC Data Schema during the month of April, 2024

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| checklists | checklist_sections_signatures |  | ADDED | checklist_sections_signatures table added to the schema. | 1713209433 |
|  |
| rfis | rfis | rfi_type | ADDED | Column added to the rfis table in the schema. | 1712926111 |
|  |
| reviews | review_steps | step_display_name | ADDED | Column added to the review_steps table in the schema. | 1712243795 |

## March, 2024

The following changes were made to the ACC Data Schema during the month of March, 2024

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| forms | forms | status | MODIFIED | "submitted" status is now reported as "closed", "draft" is now reported as "in_progress" | 1711394933 |
|  |
| transmittals | workflow_transmittals | create_user_company_name | ADDED | Column added to the workflow_transmittals table in the schema. | 1710765628 |
| transmittals | workflow_transmittals | create_user_company_id | ADDED | Column added to the workflow_transmittals table in the schema. | 1710765628 |
| transmittals | transmittal_recipients | company_name | ADDED | Column added to the transmittal_recipients table in the schema. | 1710765628 |
|  |
| markups | placement | placement_text | MODIFIED | Semantic Update: Text content for the given markup-placement. THIS WILL OVERRIDE TEXT IN MARKUP.MARKUP_TEXT. If there is text present in this column, it is the current text of the given placement. If this field is blank, check the markup_text column by merging with the markup table to get text (if there is any for this placement). NOTE: if the markup is a feature bound markup (feature_bound_type is present), the text here is inaccurate and should be ignored. | 1710430398 |
| markups | markup | markup_text | MODIFIED | Semantic Update: Text content for the given markup. This is the initial text that the markup was created with, THIS MAY BE OVERRIDDEN BY TEXT ON THE PLACEMENT OF THIS MARKUP. Merge with the placement table and check placement_text to identify the text of a given placement of this markup. if placement_text is blank, then markup_text holds the current text content. NOTE: if the markup is a feature bound markup (feature_bound_type is present), the text here is inaccurate and should be ignored. | 1710430398 |
| rfis | rfi_custom_attributes |  | ADDED | rfi_custom_attributes table added to the schema. | 1710430398 |
| rfis | project_custom_attributes_enums |  | ADDED | project_custom_attributes_enums table added to the schema. | 1710430398 |
| rfis | project_custom_attributes |  | ADDED | project_custom_attributes table added to the schema. | 1710430398 |
| rfis | rfi_types |  | ADDED | rfi_types table added to the schema. | 1710430398 |
| activities | submittals_target_watchers |  | ADDED | submittals_target_watchers table added to the schema. | 1710430398 |
| activities | submittals_target_transition_attachments |  | ADDED | submittals_target_transition_attachments table added to the schema. | 1710430398 |
| activities | submittals_target_tasks |  | ADDED | submittals_target_tasks table added to the schema. | 1710430398 |
| activities | submittals_target_steps |  | ADDED | submittals_target_steps table added to the schema. | 1710430398 |
| activities | submittals_target_ball_in_court_users |  | ADDED | submittals_target_ball_in_court_users table added to the schema. | 1710430398 |
| activities | submittals_target_ball_in_court_roles |  | ADDED | submittals_target_ball_in_court_roles table added to the schema. | 1710430398 |
| activities | submittals_target_ball_in_court_companies |  | ADDED | submittals_target_ball_in_court_companies table added to the schema. | 1710430398 |
| activities | submittals_object_ball_in_court_users |  | ADDED | submittals_object_ball_in_court_users table added to the schema. | 1710430398 |
| activities | submittals_object_ball_in_court_roles |  | ADDED | submittals_object_ball_in_court_roles table added to the schema. | 1710430398 |
| activities | submittals_object_ball_in_court_companies |  | ADDED | submittals_object_ball_in_court_companies table added to the schema. | 1710430398 |
| activities | submittals_activities |  | ADDED | submittals_activities table added to the schema. | 1710430398 |

## February, 2024

The following changes were made to the ACC Data Schema during the month of February, 2024

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| forms | layout_sections | display_index | ADDED | Column added to the layout_sections table in the schema. | 1707252074 |
| forms | layout_section_items | display_index | ADDED | Column added to the layout_section_items table in the schema. | 1707252074 |
| reviews | workflow_notes | round_num | ADDED | Column added to the workflow_notes table in the schema. | 1707252074 |
| reviews | reviews | current_round_num | ADDED | Column added to the reviews table in the schema. | 1707252074 |
| reviews | review_documents | round_num | ADDED | Column added to the review_documents table in the schema. | 1707252074 |
| reviews | review_comments | round_num | ADDED | Column added to the review_comments table in the schema. | 1707252074 |
|  |
| clashes |  |  | ADDED | New service group added to the ACC Data Schema. | 1706631943 |
| packages |  |  | ADDED | New service group added to the ACC Data Schema. | 1706631943 |

## December, 2023

The following changes were made to the ACC Data Schema during the month of December, 2023

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| activities | docs_activities | object_version_set_issuance_date | MODIFIED | Corrected documentation from [timestamp: SQL] to [date: string] | 1702494972 |
| activities | docs_activities | object_old_issuance_date | MODIFIED | Corrected documentation from [timestamp: SQL] to [date: string] | 1702494972 |
| activities | docs_activities | object_new_issuance_date | MODIFIED | Corrected documentation from [timestamp: SQL] to [date: string] | 1702494972 |
| activities | docs_activities | object_issuance_date | MODIFIED | Corrected documentation from [timestamp: SQL] to [date: string] | 1702494972 |
| activities | cost_activities | object_billing_period_start_date | MODIFIED | Corrected documentation from [timestamp: SQL] to [date: string] | 1702494972 |
| activities | cost_activities | object_billing_period_end_date | MODIFIED | Corrected documentation from [timestamp: SQL] to [date: string] | 1702494972 |
| activities | sheets_activities | target_issuance_date | MODIFIED | timestamp formatting corrected | 1702494972 |
| activities | sheets_activities | object_version_set_issuance_date | MODIFIED | timestamp formatting corrected | 1702494972 |
| activities | sheets_activities | object_issuance_date | MODIFIED | timestamp formatting corrected | 1702494972 |
| activities | issues_activities | object_updated_at | MODIFIED | timestamp formatting corrected | 1702494972 |
| activities | issues_activities | object_created_at | MODIFIED | timestamp formatting corrected | 1702494972 |
| activities | assets_activities | object_patch_entity_updated_at | MODIFIED | timestamp formatting corrected | 1702494972 |
| activities | assets_activities | object_deleted_entity_updated_at | MODIFIED | timestamp formatting corrected | 1702494972 |
| activities | assets_activities | object_deleted_entity_deleted_at | MODIFIED | timestamp formatting corrected | 1702494972 |
| activities | assets_activities | object_deleted_entity_created_at | MODIFIED | timestamp formatting corrected | 1702494972 |
| activities | assets_activities | object_created_entity_updated_at | MODIFIED | timestamp formatting corrected | 1702494972 |
| activities | assets_activities | object_created_entity_created_at | MODIFIED | timestamp formatting corrected | 1702494972 |
| activities | assets_activities | object_before_entity_updated_at | MODIFIED | timestamp formatting corrected | 1702494972 |
| activities | assets_activities | object_before_entity_created_at | MODIFIED | timestamp formatting corrected | 1702494972 |
|  |
| issues | issues | deleted_by | ADDED | Column added to the issues table in the schema. | 1701795966 |
|  |
| submittalsacc | tasks | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | tasks | started_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | tasks | responded_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | tasks | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | tasks | completed_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | steps | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | steps | started_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | steps | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | steps | completed_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | specs | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | specs | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | packages | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | packages | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | itemtype | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | itemtype | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | items | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | items | sent_to_submitter | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | items | sent_to_review | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | items | responded_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | items | received_from_submitter | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | items | received_from_review | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | items | published_date | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | items | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | custom_identifier_settings | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | comments | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | comments | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | attachments | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittalsacc | attachments | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | specs | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | specs | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | specs | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | packages | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | packages | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | packages | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | items | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | items | sent_to_submitter | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | items | sent_to_reviewer | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | items | responded_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | items | received_from_submitter | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | items | received_from_reviewer | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | items | published_date | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | items | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | comments | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | comments | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | comments | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | attachments | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | attachments | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| submittals | attachments | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| sheets | sheets | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| sheets | sheets | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| sheets | sheets | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| sheets | sets | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| sheets | sets | issuance_date | MODIFIED | timestamp formatting corrected | 1701717685 |
| sheets | sets | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| schedule | schedules | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| schedule | schedules | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| schedule | resources | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| schedule | resources | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| schedule | dependencies | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| schedule | dependencies | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| schedule | comments | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| schedule | activity_codes | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| schedule | activity_codes | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| schedule | activities | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| schedule | activities | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | topics | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | topics | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | topics | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | participants | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | participants | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | participants | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | non_member_participants | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | non_member_participants | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | non_member_participants | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | meetings | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | meetings | starts_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | meetings | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | meetings | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | items | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | items | due_date | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | items | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | items | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | attachments | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | attachments | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | attachments | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | assignees | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | assignees | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| meetingminutes | assignees | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| locations | trees | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| locations | trees | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| locations | nodes | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| locations | nodes | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | payment_references | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | payment_references | paid_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | payment_references | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | main_contracts | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | main_contracts | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | expenses | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | expenses | received_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | expenses | paid_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | expenses | issued_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | expenses | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | expenses | approved_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | expense_items | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | expense_items | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | cost_payments | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | cost_payments | submitted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | cost_payments | paid_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | cost_payments | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | cost_payments | approved_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | cost_payment_items | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | cost_payment_items | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | cost_items | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | cost_items | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | contracts | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | contracts | status_changed_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | contracts | sent_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | contracts | returned_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | contracts | responded_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | contracts | procured_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | contracts | onsite_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | contracts | offsite_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | contracts | executed_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | contracts | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | contracts | awarded_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | contracts | approved_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | change_orders | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | change_orders | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | change_orders | applied_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | budgets | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | budgets | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | budget_payments | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | budget_payments | submitted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | budget_payments | paid_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | budget_payments | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | budget_payments | approved_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | budget_payment_items | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | budget_payment_items | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | budget_code_segments | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | budget_code_segments | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | budget_code_segment_codes | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | budget_code_segment_codes | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | approval_workflows | current_due_date | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | approval_workflows | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| cost | approval_workflows | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | templates_versions | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | templates_versions | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | templates_versions | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | templates | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | templates | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | templates | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | template_signatures_all | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | template_signatures_all | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | template_signatures | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | template_signatures | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | template_sections_all | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | template_sections_all | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | template_sections | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | template_sections | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | template_items_all | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | template_items_all | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | template_items | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | template_items | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | template_item_instructions | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | template_item_instructions | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | checklists | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | checklists | started_on | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | checklists | scheduled_date | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | checklists | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | checklists | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | checklists | completed_on | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | checklists | archived_on | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | checklist_sections | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | checklist_sections | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | checklist_section_assignees | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | checklist_section_assignees | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | checklist_section_assignees | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | checklist_items | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | checklist_items | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | checklist_assignees | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | checklist_assignees | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| checklists | checklist_assignees | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | status_sets | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | status_sets | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | status_sets | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | model_sync_containers | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | model_sync_containers | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | model_sync_containers | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | custom_attributes | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | custom_attributes | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | custom_attributes | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | custom_attribute_selection_values | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | custom_attribute_selection_values | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | custom_attribute_selection_values | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | category_status_set_assignments | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | category_status_set_assignments | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | category_status_set_assignments | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | category_custom_attribute_assignments | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | category_custom_attribute_assignments | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | category_custom_attribute_assignments | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | asset_statuses | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | asset_statuses | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | asset_statuses | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | asset_permissions | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | asset_permissions | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | asset_permissions | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | asset_model_sync_records | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | asset_model_sync_records | deleted_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | asset_model_sync_records | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | categories | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | assets | updated_at | MODIFIED | timestamp formatting corrected | 1701717685 |
| assets | assets | created_at | MODIFIED | timestamp formatting corrected | 1701717685 |
|  |
| issues | changesets |  | DELETED |  | 1701092668 |

## November, 2023

The following changes were made to the ACC Data Schema during the month of November, 2023

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| forms | native_forms | layout_uid | ADDED | Column added to the native_forms table in the schema. | 1699452795 |
| forms | layouts |  | ADDED | layouts table added to the schema. | 1699452795 |
| forms | layout_table_columns |  | ADDED | layout_table_columns table added to the schema. | 1699452795 |
| forms | layout_sections |  | ADDED | layout_sections table added to the schema. | 1699452795 |
| forms | layout_section_items |  | ADDED | layout_section_items table added to the schema. | 1699452795 |

## October, 2023

The following changes were made to the ACC Data Schema during the month of October, 2023

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| forms | form_sections |  | ADDED | form_sections table added to the schema. | 1698700370 |
|  |
| submittalsacc | custom_identifier_settings |  | ADDED | custom_identifier_settings table added to the schema. Added support for custom identifiers | 1696529432 |
| submittalsacc | items | custom_identifier_human_readable | ADDED | Column added to the items table in the schema. Added support for custom identifiers | 1696529432 |
| submittalsacc | items | custom_identifier_sort | ADDED | Column added to the items table in the schema. Added support for custom identifiers | 1696529432 |
| submittalsacc | items | custom_identifier | ADDED | Column added to the items table in the schema. Added support for custom identifiers | 1696529432 |
| activities | assets_activities | object_before_category_path | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_before_category_is_valid | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_before_category_is_missing | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_before_category_is_active | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_before_category_id | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_before_category_entity_type | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_before_category_display_name | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_before_asset_status_is_valid | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_before_asset_status_is_missing | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_before_asset_status_is_active | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_before_asset_status_id | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_before_asset_status_entity_type | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_before_asset_status_display_name | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_before_asset_status_color | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_asset_status_is_valid | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_asset_status_is_missing | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_asset_status_is_active | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_asset_status_id | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_asset_status_entity_type | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_asset_status_display_name | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |
| activities | assets_activities | object_asset_status_color | ADDED | Column added to the assets_activities table in the schema. | 1696529432 |

## September, 2023

The following changes were made to the ACC Data Schema during the month of September, 2023

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
|  |
| rfis | rfis | location_id | ADDED | Column added to the rfis table in the schema. | 1695408731 |
| rfis | rfis | opened_at | ADDED | Column added to the rfis table in the schema. | 1695408731 |
| reviews | reviews | next_action_claimed_by | ADDED | Column added to the reviews table in the schema. | 1695408731 |
| reviews | reviews | next_action_candidates_companies | ADDED | Column added to the reviews table in the schema. | 1695408731 |
| reviews | reviews | next_action_candidates_roles | ADDED | Column added to the reviews table in the schema. | 1695408731 |
| reviews | reviews | next_action_candidates_users | ADDED | Column added to the reviews table in the schema. | 1695408731 |

## August, 2023

The following changes were made to the ACC Data Schema during the month of August, 2023

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
| issues | custom_attributes | attribute_value | MODIFIED | Quotations may be added if the attribute value contains a comma (,) | 1695408731 |
| reviews | reviews | next_action_claimed_by | ADDED | Column added to the reviews table in the schema. List of strings | 1695408731 |
| reviews | reviews | next_action_candidates_companies | ADDED | Column added to the reviews table in the schema. List of strings | 1695408731 |
| reviews | reviews | next_action_candidates_roles | ADDED | Column added to the reviews table in the schema. List of strings | 1695408731 |
| reviews | reviews | next_action_candidates_users | ADDED | Column added to the reviews table in the schema. List of strings | 1695408731 |

## July, 2023

The following changes were made to the ACC Data Schema during the month of July, 2023

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
| cost | cost_payments | materials_retention | ADDED | Column added to the cost_payments table in the schema. | 1695408731 |
| cost | cost_payments | materials_billed | ADDED | Column added to the cost_payments table in the schema. | 1695408731 |
| issues | issues | gps_coordinates | ADDED | Column added to the issues table in the schema. | 1695408731 |
| submittalsacc | tasks | assigned_to_type | ADDED | Column added to the tasks table in the schema. On July 14, 2023, the submittalsacc schema has been updated to support multiple reviewers. This is a new column | 1695408731 |
| submittalsacc | items | ball_in_court_companies | ADDED | Column added to the items table in the schema. On July 14, 2023, the submittalsacc schema has been updated to support multiple reviewers. This is a new list field, list of companies | 1695408731 |
| submittalsacc | items | ball_in_court_roles | ADDED | Column added to the items table in the schema. On July 14, 2023, the submittalsacc schema has been updated to support multiple reviewers. This is a new list field, list of roles | 1695408731 |
| submittalsacc | items | ball_in_court_users | ADDED | Column added to the items table in the schema. On July 14, 2023, the submittalsacc schema has been updated to support multiple reviewers. This is a new list field, list of users | 1695408731 |
| submittalsacc | items | ball_in_court | DEPRECATED | On July 14, 2023, the submittalsacc schema has been updated to support multiple reviewers. This is a deprecated field, will be replaced by ball_in_court_users | 1695408731 |
| submittalsacc | items | subcontractor_type | ADDED | Column added to the items table in the schema. On July 14, 2023, the submittalsacc schema has been updated to support multiple reviewers. This is a new enum field | 1695408731 |
| submittalsacc | items | manager_type | ADDED | Column added to the items table in the schema. On July 14, 2023, the submittalsacc schema has been updated to support multiple reviewers. This is a new enum field | 1695408731 |
| cost | main_contract_properties |  | ADDED | main_contract_properties table added to the schema. | 1695408731 |
| cost | main_contracts |  | ADDED | main_contracts table added to the schema. | 1695408731 |

## June, 2023

The following changes were made to the ACC Data Schema during the month of June, 2023

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
| forms | forms | assignee_type | ADDED | Column added to the forms table in the schema. | 1695408731 |
| forms | forms | assignee_type_id | ADDED | Column added to the forms table in the schema. | 1695408731 |
| forms | forms | last_submitted_at | ADDED | Column added to the forms table in the schema. | 1695408731 |
| forms | forms | created_at | ADDED | Column added to the forms table in the schema. | 1695408731 |
| forms | forms | due_date | ADDED | Column added to the forms table in the schema. | 1695408731 |
| markups | placement | placement_text | ADDED | Column added to the placement table in the schema. | 1695408731 |
| markups | layer | base_entity_uid | ADDED | Column added to the layer table in the schema. | 1695408731 |
| markups | layer | base_entity_urn | ADDED | Column added to the layer table in the schema. | 1695408731 |
| markups | layer | surface_type | ADDED | Column added to the layer table in the schema. | 1695408731 |
| markups | markup | markup_text | ADDED | Column added to the markup table in the schema. | 1695408731 |
| checklists | template_signatures_all |  | ADDED | template_signatures_all table added to the schema. This table will return ALL data versions instead of latest versions of the table items. This is only available for project level extracts. | 1695408731 |
| checklists | template_items_all |  | ADDED | template_items_all table added to the schema. This table will return ALL data versions instead of latest versions of the table items. This is only available for project level extracts. | 1695408731 |
| checklists | template_sections_all |  | ADDED | template_sections_all table added to the schema. This table will return ALL data versions instead of latest versions of the table items. This is only available for project level extracts. | 1695408731 |
| rfis |  |  | MODIFIED | On June 18, 2023, the RFIs schema has been updated to support multiple reviewers for an RFI | 1695408731 |
| admin | projects | classification | ADDED | Column added to the projects table in the schema. | 1695408731 |
| cost | budgets | compounded | ADDED | Column added to the budgets table in the schema. | 1695408731 |

## May, 2023

The following changes were made to the ACC Data Schema during the month of May, 2023

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
| issues | issues | status | MODIFIED | 4 additional statuses have been added: pending, in_progress, completed, in_review | 1695408731 |
| progresstracking |  |  | DELETED | On May 12, 2023, the Progress Tracking Beta has ending and the Progress Tracking dataset is no longer be available for download from Data Connector. Progress tracking functionality is available now in the Assets tool. Learn more about why we merged Progress Tracking functionality into Assets here. More details of this change can be seen on the Autodesk Build Help Site. | 1695408731 |

## April, 2023

The following changes were made to the ACC Data Schema during the month of April, 2023

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
| cost | approval_workflows | current_due_date | ADDED | Column added to the approval_workflows table in the schema. | 1695408731 |
| admin | projects | total_company_size | ADDED | Column added to the projects table in the schema. | 1695408731 |
| admin | projects | total_member_size | ADDED | Column added to the projects table in the schema. | 1695408731 |
| submittals | attachments | upload_urn | ADDED | Column added to the attachments table in the schema. | 1695408731 |
| cost |  |  | MODIFIED | A recent update was made to the data extractions to be more consistent with the UI behavior. The result of this change is that nulls/empty string will be returned in cost values instead of zeros. In general, null / empty / should all be treated in the same manner | 1695408731 |

## March, 2023

The following changes were made to the ACC Data Schema during the month of March, 2023

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
| activities | cost_changes |  | ADDED | cost_changes table added to the schema. A beta release of the activities service group is available via API extracts. This is be a Beta release and is subject to change. | 1695408731 |
| activities | cost_activities |  | ADDED | cost_activities table added to the schema. A beta release of the activities service group is available via API extracts. This is be a Beta release and is subject to change. | 1695408731 |
| activities | sheets_activities |  | ADDED | sheets_activities table added to the schema. A beta release of the activities service group is available via API extracts. This is be a Beta release and is subject to change. | 1695408731 |
| activities | rfis_changes |  | ADDED | rfis_changes table added to the schema. A beta release of the activities service group is available via API extracts. This is be a Beta release and is subject to change. | 1695408731 |
| activities | rfis_activities |  | ADDED | rfis_activities table added to the schema. A beta release of the activities service group is available via API extracts. This is be a Beta release and is subject to change. | 1695408731 |
| activities | issues_changes |  | ADDED | issues_changes table added to the schema. A beta release of the activities service group is available via API extracts. This is be a Beta release and is subject to change. | 1695408731 |
| activities | issues_activities |  | ADDED | issues_activities table added to the schema. A beta release of the activities service group is available via API extracts. This is be a Beta release and is subject to change. | 1695408731 |
| activities | docs_standard_attributes |  | ADDED | docs_standard_attributes table added to the schema. A beta release of the activities service group is available via API extracts. This is be a Beta release and is subject to change. | 1695408731 |
| activities | docs_permissions |  | ADDED | docs_permissions table added to the schema. A beta release of the activities service group is available via API extracts. This is be a Beta release and is subject to change. | 1695408731 |
| activities | docs_naming_standards |  | ADDED | docs_naming_standards table added to the schema. A beta release of the activities service group is available via API extracts. This is be a Beta release and is subject to change. | 1695408731 |
| activities | docs_custom_attribute_constraints |  | ADDED | docs_custom_attribute_constraints table added to the schema. A beta release of the activities service group is available via API extracts. This is be a Beta release and is subject to change. | 1695408731 |
| activities | docs_custom_attributes |  | ADDED | docs_custom_attributes table added to the schema. A beta release of the activities service group is available via API extracts. This is be a Beta release and is subject to change. | 1695408731 |
| activities | docs_activities |  | ADDED | docs_activities table added to the schema. A beta release of the activities service group is available via API extracts. This is be a Beta release and is subject to change. | 1695408731 |
| activities | assets_activities |  | ADDED | assets_activities table added to the schema. A beta release of the activities service group is available via API extracts. This is be a Beta release and is subject to change. | 1695408731 |
| activities | admin_activities |  | ADDED | admin_activities table added to the schema. A beta release of the activities service group is available via API extracts. This is be a Beta release and is subject to change. | 1695408731 |
| cost | cost_payments |  | MODIFIED | Budget calculation changes and new columns (submitted_at, note) | 1695408731 |
| cost | budget_payments |  | MODIFIED | Budget calculation changes and new columns (submitted_at, note) | 1695408731 |
| admin | project_user_roles | created_at | MODIFIED | Data correction for column to report the proper date | 1695408731 |
| admin | project_users |  | ADDED | project_users table added to the schema. | 1695408731 |
| cost | approval_workflows |  | ADDED | approval_workflows table added to the schema. | 1695408731 |
| cost | cost_payment_properties |  | ADDED | cost_payment_properties table added to the schema. | 1695408731 |
| cost | budget_payment_properties |  | ADDED | budget_payment_properties table added to the schema. | 1695408731 |
| cost | expense_properties |  | ADDED | expense_properties table added to the schema. | 1695408731 |
| cost | payment_references |  | ADDED | payment_references table added to the schema. | 1695408731 |

## January, 2023

The following changes were made to the ACC Data Schema during the month of January, 2023

| service_group | table | column | change_type | notes | watermark |
| --- | --- | --- | --- | --- | --- |
| admin | project_user_services |  | MODIFIED | On January 24, 2023 a change was made to a service identifier column being reported by Data Connector in the Admin schema. This change was made to bring the actual data extracted in compliance with the documentation. The service identifier for Document Management should have been documentManagement, but was being reported as doc_manager. This was fixed on the 24th, but was not communicated in our product documentation as per our standard practice and for this, we apologize. | 1695408731 |
| admin | project_services |  | MODIFIED | On January 24, 2023 a change was made to a service identifier column being reported by Data Connector in the Admin schema. This change was made to bring the actual data extracted in compliance with the documentation. The service identifier for Document Management should have been documentManagement, but was being reported as doc_manager. This was fixed on the 24th, but was not communicated in our product documentation as per our standard practice and for this, we apologize. | 1695408731 |
| admin | account_services |  | MODIFIED | On January 24, 2023 a change was made to a service identifier column being reported by Data Connector in the Admin schema. This change was made to bring the actual data extracted in compliance with the documentation. The service identifier for Document Management should have been documentManagement, but was being reported as doc_manager. This was fixed on the 24th, but was not communicated in our product documentation as per our standard practice and for this, we apologize. | 1695408731 |
| assets | assets_permissions |  | MODIFIED | The new assets permissions schema will accommodate both project-wide and per-category permissions. The resource_type and resource_id columns indicate the resource to which a permission applies (the project or a category). All existing permissions in ACC Build and BIM 360 will be present in the new permissions schema and will have a resource_type equal to project. The permission_policy_type column replaces the notion of permission levels. It is an enum that can take on the values view, edit, create, create_only, or manage. It no longer results in repeated rows. This enum corresponds to the available options on the Assets Permissions page in the web application. Note that create_only is only available in BIM 360 and manage is only available in ACC Build. | 1695408731 |
| admin | project_user_products | created_at | ADDED | Column added to the project_user_products table in the schema. | 1695408731 |
| forms | native_form_values |  | ADDED | native_form_values table added to the schema. | 1695408731 |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
