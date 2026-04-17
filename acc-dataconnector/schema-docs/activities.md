# activities Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=activities&format=html

---

# activities Schema Description

**Documentation Updated:** 2025-06-11  

- [admin_activities](#admin_activities)
- [assets_activities](#assets_activities)
- [bridge_activities](#bridge_activities)
- [cost_activities](#cost_activities)
- [cost_changes](#cost_changes)
- [docs_activities](#docs_activities)
- [docs_custom_attribute_constraints](#docs_custom_attribute_constraints)
- [docs_custom_attributes](#docs_custom_attributes)
- [docs_naming_standards](#docs_naming_standards)
- [docs_permissions](#docs_permissions)
- [docs_standard_attributes](#docs_standard_attributes)
- [issues_activities](#issues_activities)
- [issues_changes](#issues_changes)
- [rfis_activities](#rfis_activities)
- [rfis_changes](#rfis_changes)
- [sheets_activities](#sheets_activities)
- [submittals_activities](#submittals_activities)
- [submittals_object_ball_in_court_companies](#submittals_object_ball_in_court_companies)
- [submittals_object_ball_in_court_roles](#submittals_object_ball_in_court_roles)
- [submittals_object_ball_in_court_users](#submittals_object_ball_in_court_users)
- [submittals_target_ball_in_court_companies](#submittals_target_ball_in_court_companies)
- [submittals_target_ball_in_court_roles](#submittals_target_ball_in_court_roles)
- [submittals_target_ball_in_court_users](#submittals_target_ball_in_court_users)
- [submittals_target_steps](#submittals_target_steps)
- [submittals_target_tasks](#submittals_target_tasks)
- [submittals_target_transition_attachments](#submittals_target_transition_attachments)
- [submittals_target_watchers](#submittals_target_watchers)

## admin_activities

Activities generated in ACC Build User Administration  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_by | string |  | Autodesk ID of the user performing the activity action |
| 6 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 7 | object_access_change_list | string |  | Access change list in JSON Array Format |
| 8 | object_added_services | string |  | Allowed services |
| 9 | object_allow_edit_company | string |  | Allow company edit |
| 10 | object_default_access_level | string |  | Default level of access for the object |
| 11 | object_display_name | string |  | Display name for the target being acted on |
| 12 | object_id | string: UUID |  | ID for the object being acted on - if the object_object_type is user, this ID is the admin_users id column, not the Autodesk ID |
| 13 | object_name | string |  | Name of the object being acted on |
| 14 | object_name_was | string |  | Previous name for the object being acted on |
| 15 | object_object_type | string |  | Type of the object being acted on |
| 16 | object_removed_services | string |  | Removed services from the object |
| 17 | object_service_name | string |  | Service name for the object being acted on |
| 18 | object_services_list | string |  | Service listing in JSON Array Format |
| 19 | object_size | number |  | Size of the object being acted on |
| 20 | object_status | string |  | Status of the object being acted on |
| 21 | object_status_was | string |  | Old status of the object being acted on |
| 22 | object_update_image | string |  | Image defintion |
| 23 | target_display_name | string |  | Display name for the object being acted on |
| 24 | target_id | string: UUID |  | ID for the target being acted on - if the target_object_type is user, this ID is the admin_users id column, not the Autodesk ID |
| 25 | target_object_type | string |  | Object type for the target being acted on |

## assets_activities

Activities generated in ACC Build Issues Service  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_by | string |  | Autodesk ID of the user performing the activity action |
| 6 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 7 | object_activity_source | string |  | Object Activity Source |
| 8 | object_after_asset_status_color | string |  | Object After Asset Status Color |
| 9 | object_after_asset_status_display_name | string |  | Object After Asset Status Display Name |
| 10 | object_after_asset_status_entity_type | string |  | Object After Asset Status Entity Type |
| 11 | object_after_asset_status_id | string: UUID |  | Object After Asset Status ID |
| 12 | object_after_asset_status_is_active | boolean |  | Object After Status Is Active |
| 13 | object_after_asset_status_is_missing | boolean |  | Object After Asset Status is Missing |
| 14 | object_after_asset_status_is_valid | boolean |  | Object After Asset Status is Valid |
| 15 | object_after_category_display_name | string |  | Object After Category Display Name |
| 16 | object_after_category_entity_type | string |  | Object After Category Entity Type |
| 17 | object_after_category_id | string |  | Object After Category ID |
| 18 | object_after_category_is_active | boolean |  | Object After Category Is Active |
| 19 | object_after_category_is_missing | boolean |  | Object After Category Is Missing |
| 20 | object_after_category_is_valid | boolean |  | Object After Category Is Valid |
| 21 | object_after_category_path | string |  | Object After Category Path |
| 22 | object_after_location_display_name | string |  | Object After Location Display Name |
| 23 | object_after_location_entity_type | string |  | Object After Location Entity Type |
| 24 | object_after_location_id | string: UUID |  | Object After Location ID |
| 25 | object_after_location_is_active | boolean |  | Object After Location Is Active |
| 26 | object_after_location_is_missing | boolean |  | Object After Location Is Missing |
| 27 | object_after_location_is_valid | boolean |  | Object After Location Is Valid |
| 28 | object_after_location_path | string |  | Object After Location Path |
| 29 | object_before_entity_category_id | string |  | Object Before Entity Category Id |
| 30 | object_before_entity_client_asset_id | string |  | Object Before Entity Client Asset Id |
| 31 | object_before_entity_created_at | timestamp: SQL |  | Object Before Entity Created At |
| 32 | object_before_entity_created_by | string |  | Object Before Entity Created By |
| 33 | object_before_entity_custom_attributes | string |  | Object Before Entity Custom Attributes |
| 34 | object_before_entity_id | string: UUID |  | Object Before Entity Id |
| 35 | object_before_entity_is_active | boolean |  | Object Before Entity Is Active |
| 36 | object_before_entity_location_id | string: UUID |  | Object Before Entity Location Id |
| 37 | object_before_entity_status_id | string: UUID |  | Object Before Entity Status Id |
| 38 | object_before_entity_updated_at | timestamp: SQL |  | Object Before Entity Updated At |
| 39 | object_before_entity_updated_by | string |  | Object Before Entity Updated By |
| 40 | object_before_entity_version | number |  | Object Before Entity Version |
| 41 | object_before_location_display_name | string |  | Object Before Location Display Name |
| 42 | object_before_location_entity_type | string |  | Object Before Location Entity Type |
| 43 | object_before_location_id | string: UUID |  | Object Before Location Id |
| 44 | object_before_location_is_active | boolean |  | Object Before Location Is Active |
| 45 | object_before_location_is_missing | boolean |  | Object Before Location Is Missing |
| 46 | object_before_location_is_valid | boolean |  | Object Before Location Is Valid |
| 47 | object_before_location_path | string |  | Object Before Location Path |
| 48 | object_category_display_name | string |  | Object Category Display Name |
| 49 | object_category_entity_type | string |  | Object Category Entity Type |
| 50 | object_category_id | string |  | Object Category Id |
| 51 | object_category_is_active | boolean |  | Object Category Is Active |
| 52 | object_category_is_missing | boolean |  | Object Category Is Missing |
| 53 | object_category_is_valid | boolean |  | Object Category Is Valid |
| 54 | object_category_path | string |  | Object Category Path |
| 55 | object_created_entity_category_id | string |  | Object Created Entity Category Id |
| 56 | object_created_entity_client_asset_id | string |  | Object Created Entity Client Asset Id |
| 57 | object_created_entity_created_at | timestamp: SQL |  | Object Created Entity Created At |
| 58 | object_created_entity_created_by | string |  | Object Created Entity Created By |
| 59 | object_created_entity_id | string: UUID |  | Object Created Entity Id |
| 60 | object_created_entity_is_active | boolean |  | Object Created Entity Is Active |
| 61 | object_created_entity_status_id | string: UUID |  | Object Created Entity Status Id |
| 62 | object_created_entity_updated_at | timestamp: SQL |  | Object Created Entity Updated At |
| 63 | object_created_entity_updated_by | string |  | Object Created Entity Updated By |
| 64 | object_created_entity_version | number |  | Object Created Entity Version |
| 65 | object_deleted_entity_category_id | string |  | Object Deleted Entity Category Id |
| 66 | object_deleted_entity_client_asset_id | string |  | Object Deleted Entity Client Asset Id |
| 67 | object_deleted_entity_created_at | timestamp: SQL |  | Object Deleted Entity Created At |
| 68 | object_deleted_entity_created_by | string |  | Object Deleted Entity Created By |
| 69 | object_deleted_entity_deleted_at | timestamp: SQL |  | Object Deleted Entity Deleted At |
| 70 | object_deleted_entity_deleted_by | string |  | Object Deleted Entity Deleted By |
| 71 | object_deleted_entity_id | string: UUID |  | Object Deleted Entity Id |
| 72 | object_deleted_entity_is_active | boolean |  | Object Deleted Entity Is Active |
| 73 | object_deleted_entity_location_id | string: UUID |  | Object Deleted Entity Location Id |
| 74 | object_deleted_entity_status_id | string: UUID |  | Object Deleted Entity Status Id |
| 75 | object_deleted_entity_updated_at | timestamp: SQL |  | Object Deleted Entity Updated At |
| 76 | object_deleted_entity_updated_by | string |  | Object Deleted Entity Updated By |
| 77 | object_deleted_entity_version | number |  | Object Deleted Entity Version |
| 78 | object_display_name | string |  | Object Display Name |
| 79 | object_id | string: UUID |  | Object Id |
| 80 | object_location_display_name | string |  | Object Location Display Name |
| 81 | object_location_entity_type | string |  | Object Location Entity Type |
| 82 | object_location_id | string: UUID |  | Object Location Id |
| 83 | object_location_is_active | boolean |  | Object Location Is Active |
| 84 | object_location_is_missing | boolean |  | Object Location Is Missing |
| 85 | object_location_is_valid | boolean |  | Object Location Is Valid |
| 86 | object_location_path | string |  | Object Location Path |
| 87 | object_patch_entity_custom_attributes | string |  | Object Patch Entity Custom Attributes |
| 88 | object_patch_entity_updated_at | timestamp: SQL |  | Object Patch Entity Updated At |
| 89 | object_patch_entity_updated_by | string |  | Object Patch Entity Updated By |
| 90 | object_asset_status_color | string |  | Object asset status color |
| 91 | object_asset_status_display_name | string |  | Object asset status display name |
| 92 | object_asset_status_entity_type | string |  | Object asset status entity type |
| 93 | object_asset_status_id | string: UUID |  | Object asset status ID |
| 94 | object_asset_status_is_active | boolean |  | Object asset status is active |
| 95 | object_asset_status_is_missing | boolean |  | Object asset status is missing |
| 96 | object_asset_status_is_valid | boolean |  | Object asset status is valid |
| 97 | object_before_asset_status_color | string |  | Object before asset status color |
| 98 | object_before_asset_status_display_name | string |  | Object before asset status display name |
| 99 | object_before_asset_status_entity_type | string |  | Object before asset status entity type |
| 100 | object_before_asset_status_id | string: UUID |  | Object before asset status id |
| 101 | object_before_asset_status_is_active | boolean |  | Object before asset status is active |
| 102 | object_before_asset_status_is_missing | boolean |  | Object before asset status is missing |
| 103 | object_before_asset_status_is_valid | boolean |  | Object before asset status is valid |
| 104 | object_before_category_display_name | string |  | Object before category display name |
| 105 | object_before_category_entity_type | string |  | Object before category entity type |
| 106 | object_before_category_id | string |  | Object before category id |
| 107 | object_before_category_is_active | boolean |  | Object before category is active |
| 108 | object_before_category_is_missing | boolean |  | Object before category is missing |
| 109 | object_before_category_is_valid | boolean |  | Object before category is valid |
| 110 | object_before_category_path | string |  | Object before category path |

## bridge_activities

Activities generated for ACC Bridge  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_by | string |  | Autodesk ID of the user performing the activity action |
| 6 | created_at | timestamp: SQL |  | The timestamp when the activity was created Column used for filtering Date Range Extraction requests |
| 7 | object_automation_type | string |  | Specifies the type of automation applied to an object. For example, 'acs_folder' for folder-based automations and 'acs_sheet' for sheet automations. To identify Design Collaboration team automations, look for entries where 'automationType' = 'acs_folder' and 'owner' = 'dc'. |
| 8 | object_initiator_project_id | string |  | Represents the ID of the ACC project where the user initiated the action. |
| 9 | object_item_name | string |  | Specifies the name of the item (such as a folder, sheet or team) that has an automation applied to it. |
| 10 | object_origin | string |  | Indicates the method by which the Bridged Project connection was established. For example, if the connection was made using the 'Bridge to a project' flow, the 'origin' field will be empty. For connections created through folder or sheet automation setup, the 'origin' field will contain 'create-bridge-automation'. |
| 11 | object_owner | string |  | Contains the value 'dc' for Design Collaboration team automations. This helps users distinguish between folder and team automations when the 'automationType' = 'acs_folder'. |
| 12 | object_reason | string |  | Provides context on why an automation was deleted. For example, values may include 'AUTOMATION_DELETED', 'FOLDER_DELETED', 'SHEETS_COLLECTION_DELETED', 'SHEET_DELETED'. |
| 13 | object_recipient_email | string |  | The email address of the recipient invited to create a Bridge between projects. |
| 14 | object_source_project_account_id | string |  | The account ID associated with the source project. |
| 15 | object_source_project_display_name | string |  | The project name associated with the source project. |
| 16 | object_source_project_id | string |  | The project ID associated with the source project. |
| 17 | object_target_project_account_id | string |  | The account ID associated with the target project. |
| 18 | object_target_project_display_name | string |  | The project name associated with the target project. |
| 19 | object_target_project_id | string |  | The project ID associated with the target project. |

## cost_activities

Activities generated in ACC Build Cost Service  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_by | string |  | Autodesk ID of the user performing the activity action |
| 6 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 7 | object_cost_payment_display_name | string |  | Object cost payment display name |
| 8 | object_cost_payment_id | string: UUID |  | Object cost payment id |
| 9 | object_uom_display_name | string |  | Object uom display name |
| 10 | object_uom_id | string |  | Object uom id |
| 11 | object_uom_type | string |  | Object uom type |
| 12 | object_abbr | string |  | Object abbr |
| 13 | object_association_association_type | string |  | Object association association type |
| 14 | object_association_display_name | string |  | Object association display name |
| 15 | object_association_id | string: UUID |  | Object association id |
| 16 | object_association_number | string |  | Object association number |
| 17 | object_association_type | string |  | Object association type |
| 18 | object_attachment_display_name | string |  | Object attachment display name |
| 19 | object_attachment_id | string: UUID |  | Object attachment id |
| 20 | object_attachment_type | string |  | Object attachment type |
| 21 | object_billing_period_display_name | string: UUID |  | Object billing period display name |
| 22 | object_billing_period_end_date | date: string |  | Object billing period end date |
| 23 | object_billing_period_id | string: UUID |  | Object billing period id |
| 24 | object_billing_period_start_date | date: string |  | Object billing period start date |
| 25 | object_budget_code | string |  | Object budget code |
| 26 | object_budget_display_name | string |  | Object budget display name |
| 27 | object_budget_id | string: UUID |  | Object budget id |
| 28 | object_budget_payment_display_name | string |  | Object budget payment display name |
| 29 | object_budget_payment_id | string: UUID |  | Object budget payment id |
| 30 | object_budget_payment_type | string |  | Object budget payment type |
| 31 | object_budgetpayment_display_name | string |  | Object budgetpayment display name |
| 32 | object_budgetpayment_id | string: UUID |  | Object budgetpayment id |
| 33 | object_budgets | string |  | Object budgets |
| 34 | object_calendar_configuration_display_name | string |  | Object calendar configuration display name |
| 35 | object_calendar_configuration_id | string |  | Object calendar configuration id |
| 36 | object_code | number |  | Object code |
| 37 | object_comment_display_name | string |  | Object comment display name |
| 38 | object_comment_id | string: UUID |  | Object comment id |
| 39 | object_compliance_definition_display_name | string |  | Object compliance definition display name |
| 40 | object_compliance_definition_id | string |  | Object compliance definition id |
| 41 | object_compliance_definition_type | string |  | Object compliance definition type |
| 42 | object_compliance_requirement_display_name | string |  | Object compliance requirement display name |
| 43 | object_compliance_requirement_id | string |  | Object compliance requirement id |
| 44 | object_compliance_requirement_type | string |  | Object compliance requirement type |
| 45 | object_container_setting_display_name | string |  | Object container setting display name |
| 46 | object_container_setting_id | string: UUID |  | Object container setting id |
| 47 | object_contract_display_name | string |  | Object contract display name |
| 48 | object_contract_id | string: UUID |  | Object contract id |
| 49 | object_cost_item_display_name | string |  | Object cost item display name |
| 50 | object_cost_item_id | string: UUID |  | Object cost item id |
| 51 | object_custom_column_display_name | string: UUID |  | Object custom column display name |
| 52 | object_custom_column_id | string: UUID |  | Object custom column id |
| 53 | object_default_value_display_name | string |  | Object default value display name |
| 54 | object_default_value_id | string |  | Object default value id |
| 55 | object_display_name | string |  | Object display name |
| 56 | object_distribution_display_name | string: UUID |  | Object distribution display name |
| 57 | object_distribution_id | string: UUID |  | Object distribution id |
| 58 | object_distribution_item_display_name | string |  | Object distribution item display name |
| 59 | object_distribution_item_id | string |  | Object distribution item id |
| 60 | object_document_package_display_name | string |  | Object document package display name |
| 61 | object_document_package_id | string: UUID |  | Object document package id |
| 62 | object_document_template_display_name | string |  | Object document template display name |
| 63 | object_document_template_id | string: UUID |  | Object document template id |
| 64 | object_document_template_type | string |  | Object document template type |
| 65 | object_document_package_item_display_name | string: UUID |  | Object document package item display name |
| 66 | object_document_package_item_id | string: UUID |  | Object document package item id |
| 67 | object_email_notification_display_name | string: UUID |  | Object email notification display name |
| 68 | object_email_notification_id | string: UUID |  | Object email notification id |
| 69 | object_exchange_rate_display_name | string |  | Object exchange rate display name |
| 70 | object_exchange_rate_id | string |  | Object exchange rate id |
| 71 | object_expense_code | string |  | Object expense code |
| 72 | object_expense_display_name | string |  | Object expense display name |
| 73 | object_expense_id | string: UUID |  | Object expense id |
| 74 | object_expense_type | string |  | Object expense type |
| 75 | object_expense_item_code | number |  | Object expense item code |
| 76 | object_expense_item_display_name | string |  | Object expense item display name |
| 77 | object_expense_item_id | string: UUID |  | Object expense item id |
| 78 | object_forecast_adjustment_display_name | string |  | Object forecast adjustment display name |
| 79 | object_forecast_adjustment_id | string: UUID |  | Object forecast adjustment id |
| 80 | object_form_definition_display_name | string |  | Object form definition display name |
| 81 | object_form_definition_id | string: UUID |  | Object form definition id |
| 82 | object_form_instance_code | number |  | Object form instance code |
| 83 | object_form_instance_display_name | string |  | Object form instance display name |
| 84 | object_form_instance_id | string: UUID |  | Object form instance id |
| 85 | object_form_instance_type | string |  | Object form instance type |
| 86 | object_form_item_display_name | string: UUID |  | Object form item display name |
| 87 | object_form_item_id | string: UUID |  | Object form item id |
| 88 | object_from_display_name | string |  | Object from display name |
| 89 | object_from_id | string: UUID |  | Object from id |
| 90 | object_group_key | string |  | Object group key |
| 91 | object_id | string: UUID |  | Object id |
| 92 | object_key | string |  | Object key |
| 93 | object_main_contract_code | number |  | Object main contract code |
| 94 | object_main_contract_display_name | string |  | Object main contract display name |
| 95 | object_main_contract_id | string: UUID |  | Object main contract id |
| 96 | object_main_contract_is_mile_stone | string |  | Object main contract is mile stone |
| 97 | object_main_contract_type | string |  | Object main contract type |
| 98 | object_main_contract_item_code | number |  | Object main contract item code |
| 99 | object_main_contract_item_display_name | string |  | Object main contract item display name |
| 100 | object_main_contract_item_id | string: UUID |  | Object main contract item id |
| 101 | object_maincontract_display_name | string |  | Object maincontract display name |
| 102 | object_maincontract_id | string: UUID |  | Object maincontract id |
| 103 | object_markup_formula_display_name | string |  | Object markup formula display name |
| 104 | object_markup_formula_id | string: UUID |  | Object markup formula id |
| 105 | object_milestone_display_name | string |  | Object milestone display name |
| 106 | object_milestone_id | string: UUID |  | Object milestone id |
| 107 | object_milestone_type | string |  | Object milestone type |
| 108 | object_oco_display_name | string |  | Object oco display name |
| 109 | object_oco_id | string: UUID |  | Object oco id |
| 110 | object_parent_display_name | string |  | Object parent display name |
| 111 | object_parent_id | string: UUID |  | Object parent id |
| 112 | object_payment_display_name | string |  | Object payment display name |
| 113 | object_payment_id | string: UUID |  | Object payment id |
| 114 | object_payment_item_code | number |  | Object payment item code |
| 115 | object_payment_item_display_name | string |  | Object payment item display name |
| 116 | object_payment_item_id | string: UUID |  | Object payment item id |
| 117 | object_payment_reference_display_name | string |  | Object payment reference display name |
| 118 | object_payment_reference_id | string |  | Object payment reference id |
| 119 | object_payment_reference_is_mile_stone | string |  | Object payment reference is mile stone |
| 120 | object_payment_reference_paid_amount | string |  | Object payment reference paid amount |
| 121 | object_payment_reference_reference | string |  | Object payment reference reference |
| 122 | object_pco_display_name | string |  | Object pco display name |
| 123 | object_pco_id | string: UUID |  | Object pco id |
| 124 | object_permission_display_name | string: UUID |  | Object permission display name |
| 125 | object_permission_id | string: UUID |  | Object permission id |
| 126 | object_permission_level | string |  | Object permission level |
| 127 | object_preset | string |  | Object preset |
| 128 | object_proceed_step_display_name | string |  | Object proceed step display name |
| 129 | object_proceed_step_id | string |  | Object proceed step id |
| 130 | object_proceed_step_index | number |  | Object proceed step index |
| 131 | object_proceed_step_task_definition_key | string |  | Object proceed step task definition key |
| 132 | object_property_definition_display_name | string |  | Object property definition display name |
| 133 | object_property_definition_id | string: UUID |  | Object property definition id |
| 134 | object_property_definition_type | string |  | Object property definition type |
| 135 | object_property_value_display_name | string: UUID |  | Object property value display name |
| 136 | object_property_value_id | string: UUID |  | Object property value id |
| 137 | object_rco_code | string |  | Object rco code |
| 138 | object_rco_display_name | string |  | Object rco display name |
| 139 | object_rco_id | string: UUID |  | Object rco id |
| 140 | object_rco_is_mile_stone | string |  | Object rco is mile stone |
| 141 | object_recipient | string |  | Object recipient |
| 142 | object_resource_type | string |  | Object resource type |
| 143 | object_rfq_display_name | string |  | Object rfq display name |
| 144 | object_rfq_id | string: UUID |  | Object rfq id |
| 145 | object_schedule_of_value_code | number |  | Object schedule of value code |
| 146 | object_schedule_of_value_display_name | string |  | Object schedule of value display name |
| 147 | object_schedule_of_value_id | string: UUID |  | Object schedule of value id |
| 148 | object_sco_display_name | string |  | Object sco display name |
| 149 | object_sco_id | string: UUID |  | Object sco id |
| 150 | object_segment_display_name | string |  | Object segment display name |
| 151 | object_segment_id | string: UUID |  | Object segment id |
| 152 | object_segment_value_code | number |  | Object segment value code |
| 153 | object_segment_value_display_name | number |  | Object segment value display name |
| 154 | object_segment_value_id | string: UUID |  | Object segment value id |
| 155 | object_source | string |  | Object source |
| 156 | object_source_type | string |  | Object source type |
| 157 | object_sub_cost_item_code | number |  | Object sub cost item code |
| 158 | object_sub_cost_item_display_name | string |  | Object sub cost item display name |
| 159 | object_sub_cost_item_id | string: UUID |  | Object sub cost item id |
| 160 | object_sub_cost_item_type | string |  | Object sub cost item type |
| 161 | object_subject_id | number |  | Object subject id |
| 162 | object_subject_type | string |  | Object subject type |
| 163 | object_tax_display_name | string: UUID |  | Object tax display name |
| 164 | object_tax_id | string: UUID |  | Object tax id |
| 165 | object_tax_association_association_type | string |  | Object tax association association type |
| 166 | object_tax_association_display_name | string |  | Object tax association display name |
| 167 | object_tax_association_id | string |  | Object tax association id |
| 168 | object_tax_association_number | string |  | Object tax association number |
| 169 | object_tax_formula_display_name | string |  | Object tax formula display name |
| 170 | object_tax_formula_id | string: UUID |  | Object tax formula id |
| 171 | object_tax_formula_item_display_name | string |  | Object tax formula item display name |
| 172 | object_tax_formula_item_id | string |  | Object tax formula item id |
| 173 | object_tax_formula_item_type | string |  | Object tax formula item type |
| 174 | object_tax_item_display_name | string |  | Object tax item display name |
| 175 | object_tax_item_id | string |  | Object tax item id |
| 176 | object_template_display_name | string |  | Object template display name |
| 177 | object_template_id | string: UUID |  | Object template id |
| 178 | object_terminated_step_display_name | string |  | Object terminated step display name |
| 179 | object_terminated_step_id | string |  | Object terminated step id |
| 180 | object_terminated_step_index | number |  | Object terminated step index |
| 181 | object_terminated_step_task_definition_key | string |  | Object terminated step task definition key |
| 182 | object_terminology_display_name | string: UUID |  | Object terminology display name |
| 183 | object_terminology_id | string: UUID |  | Object terminology id |
| 184 | object_terminology_type | string |  | Object terminology type |
| 185 | object_to | string |  | Object to |
| 186 | object_tracking_item_instance_code | string |  | Object tracking item instance code |
| 187 | object_tracking_item_instance_display_name | string |  | Object tracking item instance display name |
| 188 | object_tracking_item_instance_id | string |  | Object tracking item instance id |
| 189 | object_transference_display_name | string: UUID |  | Object transference display name |
| 190 | object_transference_id | string: UUID |  | Object transference id |
| 191 | object_type | string |  | Object type |
| 192 | object_undefined_display_name | string |  | Object undefined display name |
| 193 | object_undefined_id | string |  | Object undefined id |
| 194 | object_verb_key | string |  | Object verb key |
| 195 | object_workflow_condition_display_name | string: UUID |  | Object workflow condition display name |
| 196 | object_workflow_condition_id | string: UUID |  | Object workflow condition id |
| 197 | object_workflow_definition_display_name | string |  | Object workflow definition display name |
| 198 | object_workflow_definition_id | string: UUID |  | Object workflow definition id |
| 199 | object_workflow_instance_display_name | string |  | Object workflow instance display name |
| 200 | object_workflow_instance_id | string: UUID |  | Object workflow instance id |

## cost_changes

Change for values of a Cost object  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 3 | activity_id | string |  | Activity ID for this event |
| 4 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 5 | activity_verb | string |  | Activity performed by the user |
| 6 | change_type | string |  | Type identifier for the change |
| 7 | before_value | string |  | Value of the changed field before the change |
| 8 | after_value | string |  | Value of the changed field after the change |

## docs_activities

Activities generated in ACC Build Document Management  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_by | string |  | Autodesk ID of the user performing the activity action |
| 6 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 7 | object_approval_status | string |  | Approval status for this object |
| 8 | object_collection_display_name | string |  | Collection Display name for this object |
| 9 | object_collection_id | string: UUID |  | Collection id for this object |
| 10 | object_collection_instance_index | number |  | Collection Instance index for this object |
| 11 | object_collection_size | number |  | Collection size for this object |
| 12 | object_display_name | string |  | Display name for this object |
| 13 | object_file_name | string |  | File name for this object |
| 14 | object_folder_display_name | string |  | Folder Display name for this object |
| 15 | object_folder_id | string |  | Folder id for this object |
| 16 | object_from_set_display_name | string |  | From Set Display name for this object |
| 17 | object_from_set_id | string |  | From Set id for this object |
| 18 | object_hyperlink_display_name | string |  | Hyperlink Display name for this object |
| 19 | object_hyperlink_hyperlink_id | string |  | Hyperlink id for this object |
| 20 | object_hyperlink_id | string |  | Hyperlink id for this object |
| 21 | object_hyperlink_object_type | string |  | Hyperlink Object type for this object |
| 22 | object_hyperlink_parent_folder_urn | string |  | Hyperlink Parent Folder urn for this object |
| 23 | object_id | string |  | Id id for this object |
| 24 | object_issuance_date | date: string |  | Issuance date for this object |
| 25 | object_new_description | string |  | New description for this object |
| 26 | object_new_issuance_date | date: string |  | New Issuance date for this object |
| 27 | object_object_type | string |  | Object type for this object |
| 28 | object_observer_id | string |  | Observer id for this object |
| 29 | object_observer_name | string |  | Observer name for this object |
| 30 | object_observer_type | string |  | Observer type for this object |
| 31 | object_old_description | string |  | Old description for this object |
| 32 | object_old_issuance_date | date: string |  | Old Issuance date for this object |
| 33 | object_old_name | string |  | Old name for this object |
| 34 | object_parent_folder_urn | string |  | Parent Folder urn for this object |
| 35 | object_pending_name | string |  | Pending name for this object |
| 36 | object_remove_reason | string |  | Remove reason for this object |
| 37 | object_resource_type | string |  | Resource type for this object |
| 38 | object_review_display_name | string |  | Review Display name for this object |
| 39 | object_review_id | string: UUID |  | Review id for this object |
| 40 | object_review_sequence_id | number |  | Review Sequence id for this object |
| 41 | object_reviewer_id | string |  | Reviewer id for this object |
| 42 | object_reviewer_name | string |  | Reviewer name for this object |
| 43 | object_reviewer_type | string |  | Reviewer type for this object |
| 44 | object_revision_number | string |  | Revision number for this object |
| 45 | object_sequence_id | number |  | Sequence id for this object |
| 46 | object_source_display_name | string |  | Source Display name for this object |
| 47 | object_source_id | string |  | Source id for this object |
| 48 | object_source_object_type | string |  | Source Object type for this object |
| 49 | object_source_parent_folder_urn | string |  | Source Parent Folder urn for this object |
| 50 | object_source_version | number |  | Source version for this object |
| 51 | object_status | string |  | Status status for this object |
| 52 | object_task_name | string |  | Task name for this object |
| 53 | object_version | number |  | Version version for this object |
| 54 | object_version_set_display_name | string |  | Version Set Display name for this object |
| 55 | object_version_set_id | string: UUID |  | Version Set id for this object |
| 56 | object_version_set_issuance_date | date: string |  | Version Set Issuance date for this object |
| 57 | object_version_urn | string |  | Version urn for this object |
| 58 | object_version_number | number |  | Version number for this object |
| 59 | target_display_name | string |  | Display name for this target |
| 60 | target_folder_display_name | string |  | Folder Display name for this target |
| 61 | target_folder_id | string |  | Folder id for this target |
| 62 | target_id | string |  | Id id for this target |
| 63 | target_object_type | string |  | Object type for this target |
| 64 | target_parent_folder_urn | string |  | Parent Folder urn for this target |
| 65 | target_project_account_id | string: UUID |  | Project Account id for this target |
| 66 | target_project_id | string: UUID |  | Project id for this target |
| 67 | target_sequence_id | number |  | Sequence id for this target |
| 68 | target_version | number |  | Version version for this target |
| 69 | target_viewer_display_name | string |  | Viewer Display name for this target |
| 70 | target_viewer_id | string |  | Viewer id for this target |

## docs_custom_attribute_constraints

Document Management custom attribute constraints  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 3 | activity_id | string |  | Activity ID for this event |
| 4 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 5 | activity_verb | string |  | Activity performed by the user |
| 6 | id | number |  | ID for the custom attribute constraint |
| 7 | attribute_id | number |  | ID of the attribute |
| 8 | type | string |  | Type for the attribute |
| 9 | length_type | string |  | Length type for the attribute |
| 10 | max_length | number |  | Maximum length for the attribute |
| 11 | min_length | number |  | Minimum length for the attribute |
| 12 | default_value | string |  | Default value for the attribute |

## docs_custom_attributes

Document Management custom attributes  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 3 | activity_id | string |  | Activity ID for this event |
| 4 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 5 | activity_verb | string |  | Activity performed by the user |
| 6 | id | number |  | ID for the custom attribute |
| 7 | name | string |  | Name of the custom attribute |
| 8 | value | string |  | New value of the custom attribute |
| 9 | old_value | string |  | Old value of the custom attribute |
| 10 | created_by | string |  | Autodesk ID of the user creating the custom attribute |
| 11 | updated_by | string |  | Autodesk ID of the user updating the custom attribute |
| 12 | attribute_type | string |  | Custom attribute type |

## docs_naming_standards

Document Management Naming Standards  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 3 | activity_id | string |  | Activity ID for this event |
| 4 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 5 | activity_verb | string |  | Activity performed by the user |
| 6 | module | string |  | Module name for the naming standard |
| 7 | name | string |  | Name of the naming standard |
| 8 | old_name | string |  | Previous name of the naming standard |
| 9 | new_name | string |  | New name of the naming standard |
| 10 | upload_rule | string |  | Upload rule |
| 11 | attribute_name | string |  | Attribute name |

## docs_permissions

Document Management Permissions  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 3 | activity_id | string |  | Activity ID for this event |
| 4 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 5 | activity_verb | string |  | Activity performed by the user |
| 6 | permission | string |  | Permission name |

## docs_standard_attributes

Document Management Standard Attributes  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 3 | activity_id | string |  | Activity ID for this event |
| 4 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 5 | activity_verb | string |  | Activity performed by the user |
| 6 | id | number |  | ID of the attribute |
| 7 | name | string |  | Name of the attribute |
| 8 | attribute_type | string |  | Type for the attribute |
| 9 | value | string |  | Value of the attribute |

## issues_activities

Activities generated in ACC Build Issues Service  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_by | string |  | Autodesk ID of the user performing the activity action |
| 6 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 7 | object_answer | string |  | Answer of the issue |
| 8 | object_assigned_to | string |  | Assigned to user for the issue |
| 9 | object_assigned_to_type | string |  | Assigned to type for the issue |
| 10 | object_attachment_attachment_type | string |  | Attachement type for the issue |
| 11 | object_attachment_display_name | string |  | Attachment Display name for the issue |
| 12 | object_attachment_id | string: UUID |  | Attachement id for the issue |
| 13 | object_attachment_name | string |  | Attachment name for the issue |
| 14 | object_attachment_urn | string |  | Attachement urn type for the issue |
| 15 | object_attachment_urn_type | string |  | Attachement urn for the issue |
| 16 | object_comment_id | string: UUID |  | Comment ID for the issue |
| 17 | object_created_at | timestamp: SQL |  | Created at timestamp for the issue |
| 18 | object_display_name | number |  | Display name for the issue |
| 19 | object_id | string: UUID |  | ID of the issue |
| 20 | object_status | string |  | Status of the issue |
| 21 | object_title | string |  | Title for the issue |
| 22 | object_updated_at | timestamp: SQL |  | Updated timestamp for the issue |

## issues_changes

Change for values of an Issue  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 3 | activity_id | string |  | Activity ID for this event |
| 4 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 5 | activity_verb | string |  | Activity performed by the user |
| 6 | change_type | string |  | Type identifier for the change |
| 7 | before_value | string |  | Value of the changed field before the change |
| 8 | after_value | string |  | Value of the changed field after the change |

## rfis_activities

Activities generated in ACC Build RFI Service  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_by | string |  | Autodesk ID of the user performing the activity action |
| 6 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 7 | object_comment_body | string |  | Comment body for the RFI Comment |
| 8 | object_comment_id | string: UUID |  | Comment ID for the RFI Comment |
| 9 | object_comment_mentions | string |  | Mentions for the RFI Comment |
| 10 | object_comment_rfi_id | string: UUID |  | ID of the RFI Comment |
| 11 | object_comment_source | string |  | Source client of the RFI Comment |
| 12 | object_display_name | string |  | RFI display name |
| 13 | object_id | string: UUID |  | ID of the RFI |

## rfis_changes

Change for values of an RFI  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 3 | activity_id | string |  | Activity ID for this event |
| 4 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 5 | activity_verb | string |  | Activity performed by the user |
| 6 | change_type | string |  | Type identifier for the change |
| 7 | before_value | string |  | Value of the changed field before the change |
| 8 | after_value | string |  | Value of the changed field after the change |

## sheets_activities

Activities generated in ACC Build Sheets Service  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_by | string |  | Autodesk ID of the user performing the activity action |
| 6 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 7 | object_acc_collection_display_name | string |  | Object ACC Colledtion Display Name |
| 8 | object_acc_collection_id | string |  | Object ACC Collection Id |
| 9 | object_collection_display_name | string |  | Object Collection Display Name |
| 10 | object_collection_id | string: UUID |  | Object Collection Id |
| 11 | object_collection_instance_index | number |  | Object Collection Instance Index |
| 12 | object_collection_size | number |  | Object Collection Size |
| 13 | object_display_name | string |  | Object Display Name |
| 14 | object_history_display_name | string |  | Object History Display Name |
| 15 | object_history_id | string: UUID |  | Object History Id |
| 16 | object_id | string: UUID |  | Object ID |
| 17 | object_indirect | boolean |  | Object Indirect |
| 18 | object_issuance_date | timestamp: SQL |  | Object Issuance Date |
| 19 | object_object_type | string |  | Object Object Type |
| 20 | object_source_file | string |  | Object Source File |
| 21 | object_source_object_display_name | string |  | Object Source Collection Display Name |
| 22 | object_source_object_history | string |  | Object Source Object History |
| 23 | object_source_object_id | string: UUID |  | Object Source Object Id |
| 24 | object_source_object_object_type | string |  | Object Source Collection Object Type |
| 25 | object_source_object_project | string |  | Object Source Object Project |
| 26 | object_source_object_version_set | string |  | Object Source Collection Version Set |
| 27 | object_target_object_display_name | string |  | Object Target Collection Display Name |
| 28 | object_target_object_history | string |  | Object Target Object History |
| 29 | object_target_object_id | string: UUID |  | Object Target Object Id |
| 30 | object_target_object_object_type | string |  | Object Target Collection Object Type |
| 31 | object_target_object_project | string |  | Object Target Object Project |
| 32 | object_target_object_version_set | string |  | Object Target Collection Version Set |
| 33 | object_title | string |  | Object Title |
| 34 | object_version_set_display_name | string |  | Object Version Collection Display Name |
| 35 | object_version_set_id | string: UUID |  | Object Version Set Id |
| 36 | object_version_set_issuance_date | timestamp: SQL |  | Object Version Collection Issuance Date |
| 37 | target_acc_collection_display_name | string |  | Target ACC Collection Display Name |
| 38 | target_acc_collection_id | string |  | Target ACC Collection Id |
| 39 | target_display_name | string |  | Target Display Name |
| 40 | target_history_display_name | string |  | Target History Display Name |
| 41 | target_history_id | string |  | Target History Id |
| 42 | target_id | string: UUID |  | Target ID |
| 43 | target_issuance_date | timestamp: SQL |  | Target Issuance Date |
| 44 | target_object_type | string |  | Target Object Type |

## submittals_activities

Activities generated in ACC Build Submittals Service  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_by | string |  | Autodesk ID of the user performing the activity action |
| 6 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 7 | object_assigned_to | string |  | The id of the assignee (Deprecated field, use ball in court fields instead) |
| 8 | object_assigned_to_field | string |  | Indicator which field is ball in court (Deprecated field, use ball in court fields instead) |
| 9 | object_attachment_category | string |  | ID of the attachment category |
| 10 | object_attribute_object_type | string |  | The object type of the entity |
| 11 | object_attribute_type | string |  | The type of the attribute |
| 12 | object_ball_in_court_type | string |  | Indicator which field is ball in court |
| 13 | object_body | string |  | Body of the comment |
| 14 | object_container_custom_identifier_sequence_type | enum: string | Possible Values: 1 - global 2 - spec | Project current sequence type |
| 15 | object_container_display_name | string |  | The display name of the entity |
| 16 | object_container_id | string: UUID |  | ID of the container |
| 17 | object_container_object_type | string |  | The object type of the entity |
| 18 | object_created_by | string |  | Autodesk ID of the user performing the activity action |
| 19 | object_created_on | timestamp: SQL |  | The timestamp when the activity created |
| 20 | object_custom_identifier | string |  | The custom identifier of the item. |
| 21 | object_custom_identifier_sort | string |  | Same value as 'custom_identifier' but this column has db collation in order to enable sorting by the custom identifier value. |
| 22 | object_description | string |  | Description of the item |
| 23 | object_display_name | string |  | The display name of the entity |
| 24 | object_entities_0_created_on | timestamp: SQL |  | The timestamp when the activity created |
| 25 | object_entities_0_display_name | string |  | The display name of the entity |
| 26 | object_entities_0_domain | string |  | The domain of the entity |
| 27 | object_entities_0_id | string |  | ID of the entity |
| 28 | object_entities_0_type | string |  | type of the entity |
| 29 | object_entities_1_created_on | timestamp: SQL |  | The timestamp when the activity created |
| 30 | object_entities_1_display_name | string |  | The display name of the entity |
| 31 | object_entities_1_domain | string |  | The domain of the entity |
| 32 | object_entities_1_id | string |  | id of the entity |
| 33 | object_entities_1_type | string |  | type of the entity |
| 34 | object_entities_display_name | string |  | The display name of the entity |
| 35 | object_entities_id | string |  | id of the entity |
| 36 | object_entity_created_on | timestamp: SQL |  | The timestamp when the activity created |
| 37 | object_entity_display_name | string |  | The display name of the entity |
| 38 | object_entity_domain | string |  | The domain of the entity |
| 39 | object_entity_id | string |  | id of the entity |
| 40 | object_entity_type | string |  | type of the entity |
| 41 | object_id | string: UUID |  | id of the entity |
| 42 | object_identifier | number |  | identifier of the entity |
| 43 | object_item_assigned_to_field | string |  | Indicator which field is ball in court |
| 44 | object_item_ball_in_court_type | string |  | Indicator which field is ball in court |
| 45 | object_item_custom_identifier | string |  | The custom identifier of the item. |
| 46 | object_item_custom_identifier_sort | string |  | Same value as 'custom_identifier' but this column has db collation in order to enable sorting by the custom identifier value. |
| 47 | object_item_description | string |  | Description of the item |
| 48 | object_item_display_name | string |  | The display name of the entity |
| 49 | object_item_id | string: UUID |  | The ID for the Submittal. |
| 50 | object_item_identifier | number |  | Identifier of the item. Created automatically |
| 51 | object_item_lead_time | number |  | item's lead time |
| 52 | object_item_object_type | string |  | The object type of the entity |
| 53 | object_item_priority | string |  | The item priority |
| 54 | object_item_required_approval_date | date: string |  | item's required approval date |
| 55 | object_item_required_date | date: string |  | item's required date |
| 56 | object_item_required_on_job_date | date: string |  | Date and time for the item to be done on site |
| 57 | object_item_response_comment | string |  | Response comment of the item (in addition to response id) |
| 58 | object_item_response_id | string: UUID |  | ID of the response, if was added. |
| 59 | object_item_revision | number |  | Revision of the item |
| 60 | object_item_sequence_type_change | string |  | 'sequence_before_change::sequence_after_change' sequence type |
| 61 | object_item_state_id | string |  | State of the item |
| 62 | object_item_status_id | enum: string | Possible Values: 1 - Required 2 - Open 3 - Closed 4 - Void 5 - Empty 6 - Draft | Status ID |
| 63 | object_item_submitter_due_date | date: string |  | When the responsible contractor submission is due |
| 64 | object_item_subsection | string |  | Sub spec section |
| 65 | object_item_title | string |  | Title (name) of the item |
| 66 | object_item_type_id | string: UUID |  | ID for the item type |
| 67 | object_lead_time | number |  | item's lead time |
| 68 | object_name_for_activity | string |  | The name of the activity |
| 69 | object_new_value | string |  | The new value |
| 70 | object_object_type | string |  | The object type of the entity |
| 71 | object_old_value | string |  | The old value |
| 72 | object_package | string |  | The related package of the item |
| 73 | object_priority | string |  | The priority of the item |
| 74 | object_required_approval_date | date: string |  | item's required approval date |
| 75 | object_required_date | date: string |  | item's required date |
| 76 | object_required_on_job_date | date: string |  | Date and time for the item to be done on site |
| 77 | object_resource_urns | string |  | URNS of the attachments |
| 78 | object_response_comment | string |  | Response comment of the item (in addition to response id) |
| 79 | object_response_id | string: UUID |  | ID of the response, if was added. |
| 80 | object_revision | number |  | Revision of the item |
| 81 | object_sequence_type_change | string |  | 'sequence_before_change::sequence_after_change' sequence type |
| 82 | object_spec_container_custom_identifier_sequence_type | string | Possible Values: 1 - global 2 - spec | Project current sequence type |
| 83 | object_spec_container_display_name | string |  | The display name of the entity |
| 84 | object_spec_container_id | string |  | Id of the container |
| 85 | object_spec_container_object_type | string |  | The object type of the entity |
| 86 | object_spec_display_name | string |  | The display name of the entity |
| 87 | object_spec_id | string: UUID |  | id of the spec |
| 88 | object_spec_identifier | string |  | Identifier of the spec |
| 89 | object_spec_object_type | string |  | The object type of the entity |
| 90 | object_state_from_display_name | string |  | The display name of the entity |
| 91 | object_state_from_id | string |  | The old state of the item |
| 92 | object_state_from_object_type | string |  | The object type of the entity |
| 93 | object_state_id | string |  | State of the item |
| 94 | object_state_to_display_name | string |  | The display name of the entity |
| 95 | object_state_to_id | string |  | The new state of the item |
| 96 | object_state_to_object_type | string |  | The object type of the entity |
| 97 | object_status_id | enum: string | Possible Values: 1 - Required 2 - Open 3 - Closed 4 - Void 5 - Empty 6 - Draft | Status ID |
| 98 | object_step_id | string: UUID |  | ID of the parent step |
| 99 | object_step_number | number |  | The order of the step in the review workflow |
| 100 | object_steps | string |  | Array of steps |
| 101 | object_submitter_due_date | date: string |  | When the responsible contractor submission is due |
| 102 | object_subsection | string |  | Sub spec section |
| 103 | object_task_id | string: UUID |  | ID of the task |
| 104 | object_tasks | string |  | Array of tasks |
| 105 | object_title | string |  | Title (name) of the item |
| 106 | object_type_container_custom_identifier_sequence_type | string | Possible Values: 1 - global 2 - spec | Project current sequence type |
| 107 | object_type_container_display_name | string |  | The display name of the entity |
| 108 | object_type_container_id | string |  | Id of the container |
| 109 | object_type_container_object_type | string |  | The object type of the entity |
| 110 | object_type_display_name | string |  | The display name of the entity |
| 111 | object_type_id | string: UUID |  | ID for the type |
| 112 | object_type_is_active | boolean |  | Is the type active |
| 113 | object_type_key | string |  | The key of the object |
| 114 | object_type_object_type | string |  | The object type of the entity |
| 115 | object_type_platform_id | string |  | For default types |
| 116 | object_type_value | string |  | Value of the type |
| 117 | object_type_identifier | string: UUID |  | Identifier of the type |
| 118 | object_urn | string |  | URN of the attachment |
| 119 | object_urn_type | enum: string | Possible Values: 1 - oss 2 - dm | The type of the urn |
| 120 | object_watchers | string |  | Watchers array |
| 121 | target_assigned_to_display_name | string |  | The display name of the entity |
| 122 | target_assigned_to_human_readable_company | string |  | Human readable company name of the assignee (Deprecated field, use ball in court fields instead) |
| 123 | target_assigned_to_human_readable_name | string |  | Human readable name of the assignee (Deprecated field, use ball in court fields instead) |
| 124 | target_assigned_to_id | string |  | The id of the assignee (Deprecated field, use ball in court fields instead) |
| 125 | target_assigned_to_object_type | string |  | The object type of the entity |
| 126 | target_assigned_to_autodesk_id | string |  | The id of the assignee (Deprecated field, use ball in court fields instead) |
| 127 | target_assigned_to_roles | string |  | The array of related roles (Deprecated field, use ball in court fields instead) |
| 128 | target_assigned_to_field | string |  | Indicator which field is ball in court (Deprecated field, use ball in court fields instead) |
| 129 | target_ball_in_court_type | string |  | Indicator which field is ball in court |
| 130 | target_container_custom_identifier_sequence_type | enum: string | Possible Values: 1 - global 2 - spec | Project current sequence type |
| 131 | target_container_display_name | string |  | The display name of the entity |
| 132 | target_container_id | string: UUID |  | ID of the container |
| 133 | target_container_object_type | string |  | The object type of the entity |
| 134 | target_custom_identifier | string |  | The custom identifier of the item. |
| 135 | target_custom_identifier_sort | string |  | Same value as 'custom_identifier' but this column has db collation in order to enable sorting by the custom identifier value. |
| 136 | target_description | string |  | Description of the item |
| 137 | target_display_name | string |  | The display name of the entity |
| 138 | target_id | string |  | ID of the target |
| 139 | target_identifier | number |  | Identifier of the target |
| 140 | target_lead_time | number |  | item's lead time |
| 141 | target_object_type | string |  | The object type of the entity |
| 142 | target_package_container_custom_identifier_sequence_type | string | Possible Values: 1 - global 2 - spec | Project current sequence type |
| 143 | target_package_container_display_name | string |  | The display name of the entity |
| 144 | target_package_container_id | string: UUID |  | Id of the container |
| 145 | target_package_container_object_type | string |  | The object type of the entity |
| 146 | target_package_display_name | string |  | The display name of the entity |
| 147 | target_package_id | string: UUID |  | Id of the package |
| 148 | target_package_identifier | number |  | Identifier of the package |
| 149 | target_package_is_deleted | boolean |  | is the package deleted |
| 150 | target_package_object_type | string |  | The object type of the entity |
| 151 | target_package_spec_display_name | string |  | The display name of the entity |
| 152 | target_package_spec_id | string: UUID |  | Related spec id of the package |
| 153 | target_package_spec_identifier | string |  | Related spec identifier of the package |
| 154 | target_package_spec_object_type | string |  | The object type of the entity |
| 155 | target_priority | string |  | The priority of the item |
| 156 | target_required_approval_date | date: string |  | item's required approval date |
| 157 | target_required_date | date: string |  | item's required date |
| 158 | target_required_on_job_date | date: string |  | Date and time for the item to be done on site |
| 159 | target_response_comment | string |  | Response comment of the item (in addition to response id) |
| 160 | target_response_id | string |  | ID of the response, if was added. |
| 161 | target_revision | number |  | Revision of the item |
| 162 | target_sequence_type_change | string |  | 'sequence_before_change::sequence_after_change' sequence type |
| 163 | target_spec_container_custom_identifier_sequence_type | string | Possible Values: 1 - global 2 - spec | Project current sequence type |
| 164 | target_spec_container_display_name | string |  | The display name of the entity |
| 165 | target_spec_container_id | string: UUID |  | Id of the container |
| 166 | target_spec_container_object_type | string |  | The object type of the entity |
| 167 | target_spec_display_name | string |  | The display name of the entity |
| 168 | target_spec_id | string |  | Id of the spec |
| 169 | target_spec_identifier | string |  | Identifier of the spec |
| 170 | target_spec_object_type | string |  | The object type of the entity |
| 171 | target_state_id | string |  | State of the item |
| 172 | target_status_id | enum: string | Possible Values: 1 - Required 2 - Open 3 - Closed 4 - Void 5 - Empty 6 - Draft | Status ID |
| 173 | target_submitter_due_date | date: string |  | When the responsible contractor submission is due |
| 174 | target_subsection | string |  | Sub spec section |
| 175 | target_title | string |  | Title (name) of the item |
| 176 | target_type_container_custom_identifier_sequence_type | string | Possible Values: 1 - global 2 - spec | Project current sequence type |
| 177 | target_type_container_display_name | string |  | The display name of the entity |
| 178 | target_type_container_id | string: UUID |  | ID of the container |
| 179 | target_type_container_object_type | string |  | The object type of the entity |
| 180 | target_type_display_name | string |  | The display name of the entity |
| 181 | target_type_id | string: UUID |  | ID for the type |
| 182 | target_type_is_active | boolean |  | Is the type active |
| 183 | target_type_key | string |  | The key of the target |
| 184 | target_type_object_type | string |  | The object type of the entity |
| 185 | target_type_platform_id | string |  | For default types |
| 186 | target_type_value | string |  | Value of the type |
| 187 | target_type_identifier | string: UUID |  | Identifier of the target |

## submittals_object_ball_in_court_companies

The object ball in court companies of the activity  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 6 | display_name | string |  | The display name of the entity |
| 7 | human_readable_name | string |  | Human readable name of the company |
| 8 | id | string |  | Member group id of the company |
| 9 | object_type | string |  | The object type of the entity |
| 10 | autodesk_id | string |  | Member group id of the company |

## submittals_object_ball_in_court_roles

The object ball in court roles of the activity  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 6 | display_name | string |  | The display name of the entity |
| 7 | human_readable_name | string |  | Human readable name of the role |
| 8 | id | string |  | Member group id of the role |
| 9 | object_type | string |  | The object type of the entity |
| 10 | autodesk_id | string |  | Member group id of the role |

## submittals_object_ball_in_court_users

The object ball in court users of the activity  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 6 | display_name | string |  | The display name of the entity |
| 7 | human_readable_company | string |  | Human readable company name of the related user |
| 8 | human_readable_name | string |  | Human readable name of the user |
| 9 | id | string |  | Autodesk id of the user |
| 10 | object_type | string |  | The object type of the entity |
| 11 | autodesk_id | string |  | Autodesk id of the user |
| 12 | roles | string |  | The array of related roles of the user |

## submittals_target_ball_in_court_companies

The target ball in court companies of the activity  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 6 | display_name | string |  | The display name of the entity |
| 7 | human_readable_name | string |  | Human readable name of the company |
| 8 | id | string |  | Member group id of the company |
| 9 | object_type | string |  | The object type of the entity |
| 10 | autodesk_id | string |  | Member group id of the company |

## submittals_target_ball_in_court_roles

The target ball in court roles of the activity  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 6 | display_name | string |  | The display name of the entity |
| 7 | human_readable_name | string |  | Human readable name of the role |
| 8 | id | string |  | Member group id of the role |
| 9 | object_type | string |  | The object type of the entity |
| 10 | autodesk_id | string |  | Member group id of the role |

## submittals_target_ball_in_court_users

The target ball in court users of the activity  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 6 | display_name | string |  | The display name of the entity |
| 7 | human_readable_company | string |  | Human readable company name of the related user |
| 8 | human_readable_name | string |  | Human readable name of the user |
| 9 | id | string |  | Autodesk id of the user |
| 10 | object_type | string |  | The object type of the entity |
| 11 | autodesk_id | string |  | Autodesk id of the user |
| 12 | roles | string |  | The array of related roles of the user |

## submittals_target_steps

Review steps for ACC Build Submittal items  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_by | string |  | Autodesk ID of the user performing the activity action |
| 6 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 7 | completed_at | timestamp: SQL |  | Date and time when the step finished |
| 8 | days_to_respond | number |  | Number of days that the reviewers have to respond |
| 9 | display_name | string |  | The display name of the entity |
| 10 | due_date | date: string |  | Date for the item to be done with current state |
| 11 | id | string: UUID |  | ID for the step |
| 12 | object_type | string |  | The object type of the entity |
| 13 | started_at | timestamp: SQL |  | Date and time when the step started |
| 14 | status | enum: string | Possible Values: not-started in-progress completed | The status of the step |
| 15 | step_number | number |  | The order of the step in the review workflow |

## submittals_target_tasks

Review tasks for ACC Build Submittal items.  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 6 | assigned_to | string |  | Autodesk User ID / Role member group ID / Company member group ID that the task is assigned to |
| 7 | assigned_to_type | enum: string | Possible Values: 1 - user 2 - company 3 - role | Indication for assigned_to id type |
| 8 | display_name | string |  | The display name of the entity |
| 9 | id | string: UUID |  | ID for the task |
| 10 | is_required | boolean |  | Is the task a required task in the review step |
| 11 | object_type | string |  | The object type of the entity |
| 12 | response_comment | string |  | Response comment of the task (in addition to response id) |
| 13 | response_id | string: UUID |  | ID of the response, if was added. |
| 14 | started_at | timestamp: SQL |  | Date and time when the task started |
| 15 | status | enum: string | Possible Values: not-started in-progress completed | The status of the task |
| 16 | step | string: UUID |  | ID of the parent step |

## submittals_target_transition_attachments

The target transition attachments of the activity  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_by | string |  | Autodesk ID of the user performing the activity action |
| 6 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 7 | attachment_category | string |  | ID of the attachment category |
| 8 | display_name | string |  | The display name of the entity |
| 9 | id | string: UUID |  | The id of the attachment |
| 10 | item | string |  | object string id of related item |
| 11 | object_type | string |  | The object type of the entity |
| 12 | resource_urns | string |  | URNS of the attachments |
| 13 | revision | number |  | Revision of the item |
| 14 | urn | string |  | URN of the attachment |
| 15 | urn_type | enum: string | Possible Values: 1 - oss 2 - dm | The type of the urn |

## submittals_target_watchers

The target watchers of the activity  Date Range Extractions Supported - Maximum Date Range Allowed: 31 days - Default Date Range: YESTERDAY

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | activity_id | string |  | Activity ID for this event |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | activity_verb | string |  | Activity performed by the user |
| 5 | created_at | timestamp: SQL |  | The timestamp when the activity created Column used for filtering Date Range Extraction requests |
| 6 | display_name | string |  | The display name of the entity |
| 7 | human_readable_company | string |  | The human readable company name of the watcher entity |
| 8 | human_readable_name | string |  | The human readable name of the watcher entity |
| 9 | id | string |  | The id of the watcher entity |
| 10 | object_type | string |  | The object type of the entity |
| 11 | autodesk_id | string |  | The id of the watcher entity |
| 12 | roles | string |  | The array of related roles if the watcher is user |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
