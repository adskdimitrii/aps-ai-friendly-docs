# cost Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=cost&format=html

---

# cost Schema Description

**Documentation Updated:** 2026-01-29  

- [approval_workflows](#approval_workflows)
- [budget_code_segment_codes](#budget_code_segment_codes)
- [budget_code_segments](#budget_code_segments)
- [budget_payment_items](#budget_payment_items)
- [budget_payment_properties](#budget_payment_properties)
- [budget_payments](#budget_payments)
- [budget_properties](#budget_properties)
- [budget_transfers](#budget_transfers)
- [budgets](#budgets)
- [change_order_cost_items](#change_order_cost_items)
- [change_order_properties](#change_order_properties)
- [change_orders](#change_orders)
- [contract_properties](#contract_properties)
- [contracts](#contracts)
- [cost_item_properties](#cost_item_properties)
- [cost_items](#cost_items)
- [cost_payment_items](#cost_payment_items)
- [cost_payment_properties](#cost_payment_properties)
- [cost_payments](#cost_payments)
- [distribution_item_curves](#distribution_item_curves)
- [distribution_items](#distribution_items)
- [expense_items](#expense_items)
- [expense_properties](#expense_properties)
- [expenses](#expenses)
- [main_contract_items](#main_contract_items)
- [main_contract_properties](#main_contract_properties)
- [main_contracts](#main_contracts)
- [payment_references](#payment_references)
- [permissions](#permissions)
- [schedule_of_values_properties](#schedule_of_values_properties)
- [sub_distribution_items](#sub_distribution_items)
- [transferences](#transferences)

## approval_workflows

The in-progress approval workflows.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The uniq ID of the approval workflow. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | name | string |  | The name of. the approval worflow. |
| 5 | association_id | string: UUID |  | The ID of the entity the approval workflow is associated to. |
| 6 | association_type | string |  | The type of the entity the approval workflow is associated to. |
| 7 | current_step_name | string |  | The name of the current review step. |
| 8 | current_assigned_users | string |  | The Autodesk IDs of the users that are assgined to in current step. |
| 9 | current_assigned_groups | string |  | The Autodesk IDs of the companies or roles that are assgined to in current step. |
| 10 | reviewed_users | string |  | The IDs of the users that have completed the review. |
| 11 | created_at | timestamp: SQL |  | The date/time the item is created. |
| 12 | updated_at | timestamp: SQL |  | The date/time the item is last modified. |
| 13 | current_due_date | timestamp: SQL |  | The due date of the current review step. |

## budget_code_segment_codes

Segment codes of the budget code template in Cost Management

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The ID of the code in the budget code segment. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | parent_id | string: UUID |  | The parent ID of the code. |
| 5 | segment_id | string: UUID |  | The segment ID of the code. |
| 6 | code | string |  | The display code, with appended # if the segment is fixed length. |
| 7 | original_code | string |  | The original code when it's imported from Excel. |
| 8 | description | string |  | The description of the code. |
| 9 | created_at | timestamp: SQL |  | The date/time the code is created. |
| 10 | updated_at | timestamp: SQL |  | The date/time the code is last modified. |

## budget_code_segments

Segments of the budget code template in Cost Management

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The ID of the budget code segment. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | name | string |  | The name of the budget code segment. |
| 5 | length | number |  | The length of the code in the segment. |
| 6 | position | number |  | The position of the segment in the template. |
| 7 | type | string |  | The type of the segment. Possible values: code, info, column |
| 8 | delimiter | string |  | The delimiter of the code of this segment to the code of the next segment. |
| 9 | sample_code | string |  | The sample code of the segment. |
| 10 | is_variable_length | boolean |  | The flag to indicate whether the code of this segment is fixed or variable length. |
| 11 | is_locked | boolean |  | The flag to indicate whether the segment is locked to disable editing or adding new codes. |
| 12 | created_at | timestamp: SQL |  | The date/time the segment is created. |
| 13 | updated_at | timestamp: SQL |  | The date/time the segment is last modified. |

## budget_payment_items

Budget Payment Item as defined in BIM 360

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique identifier of a budget payment item - auto generated. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | payment_id | string: UUID |  | The ID of the payment that the item is in. |
| 5 | parent_id | string: UUID |  | The parend item ID if current item is a child. |
| 6 | number | string | Max length: 1024 | Number of an budget payment item. |
| 7 | name | string | Max length: 1024 | Name of a budget payment item. |
| 8 | description | string | Max length: 2048 | Detail description of a budget payment item. |
| 9 | unit | string |  | The unit of measure of the payment item. |
| 10 | original_amount | number |  | The amount of the scheduled of value. |
| 11 | original_qty | number |  | The quantity of the scheduled of value. |
| 12 | original_unit_price | number |  | The unit price of the scheduled of value. |
| 13 | amount | number |  | The amount of work completed for this scheduled of value. |
| 14 | unit_price | number |  | The unit price of work completed for this scheduled of value. |
| 15 | qty | number |  | The quantity of work completed for this scheduled of value. |
| 16 | materials_on_store | number |  | The amount on store quanity for this schedule of value. |
| 17 | materials_on_store_qty | number |  | The quantity on store quanity for this schedule of value. |
| 18 | materials_on_store_unit_price | number |  | The unit price on store quanity for this schedule of value. |
| 19 | previous_amount | number |  | The previous amount of work completed. |
| 20 | previous_qty | number |  | The previous quantity of work completed. |
| 21 | previous_unit_price | number |  | The unit price of previous work complete. |
| 22 | previous_materials_on_store | number |  | The material on store of previus period. |
| 23 | completed_work_retention_percent | number |  | The retention % of work complete. |
| 24 | materials_on_store_retention_percent | number |  | The retention % of material on store. |
| 25 | completed_work_released | number |  | The released amount for work completed in this period. |
| 26 | materials_on_store_released | number |  | The released amount for material on store in this period. |
| 27 | net_amount | number |  | The net amount: work completed + material on store - retention + release. |
| 28 | status | string |  | The status of the the payment item. |
| 29 | creator_id | string |  | Autodesk User ID of a user managed by BIM 360 Admin |
| 30 | changed_by | string |  | Autodesk User ID of a user managed by BIM 360 Admin |
| 31 | created_at | timestamp: SQL |  | The date/time the payment item is created. |
| 32 | updated_at | timestamp: SQL |  | The date/time the payment item is last modified. |

## budget_payment_properties

Custom properties for Budget Payment

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | budget_payment_id | string: UUID |  | The budget payment ID for this custom property Foreign Key: Table: budget_payments Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | name | string |  | The name of the custom attribute. Inherited from the custom attribute definition. |
| 5 | built_in | boolean |  | A flag to indicate whether this is a pre-defined attribute or not. Inherited from the custom attribute definition. |
| 6 | position | number |  | The order of the custom attribute displayed in the BIM 360 Cost Management. Inherited from the custom attribute definition. |
| 7 | property_definition_id | string: UUID |  | The ID of the custom attribute definition. |
| 8 | type | string |  | The type of the custom attribute. Inherited from the custom attribute definition. |
| 9 | value | string |  | The value of the custom attribute. |

## budget_payments

Budget Payment as defined in BIM 360

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique identifier of the budget payment. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | main_contract_id | string: UUID |  | The ID of the main contract the payment is pursuant to. |
| 5 | start_date | timestamp: SQL |  | The start date of the payment billing period. |
| 6 | end_date | timestamp: SQL |  | The end date of the payment billing period. |
| 7 | due_date | timestamp: SQL | Max length: 255 | The due date of the payment. |
| 8 | number | string | Max length: 1024 | Number of an budget payment. |
| 9 | name | string | Max length: 1024 | Name of a budget payment. |
| 10 | description | string | Max length: 2048 | Detail description of a budget payment. |
| 11 | original_amount | number |  | The origianl contracted amount of th |
| 12 | amount | number |  | Work completed of this period of the payment. |
| 13 | previous_amount | number |  | Work completed in previous payment. |
| 14 | materials_on_store | number |  | Materials on site of this billing period. |
| 15 | previous_materials_on_store | number |  | Materials on site of previous billing period. |
| 16 | approved_change_orders | number |  | The total of approved change orders. |
| 17 | contract_amount | number |  | The current total of the contracted amount: orginal_amount + approved_change_orders |
| 18 | completed_work_retention | number |  | Total of the retention for total work complete. |
| 19 | materials_on_store_retention | number |  | Total of the retention for material on site |
| 20 | net_amount | number |  | Net amount of current work completed + material on site - retentions. |
| 21 | paid_amount | number |  | The amount paid by owner. |
| 22 | status | string |  | The status of the budget payment. |
| 23 | company_id | string |  | The Autodesk ID of the owner company. |
| 24 | payment_type | string |  | How is the expense paid, e.g. Cash, Check, Electronic Transfer |
| 25 | payment_reference | string |  | The reference info how the expense is paid. |
| 26 | creator_id | string |  | Autodesk User ID of a user managed by BIM 360 Admin |
| 27 | changed_by | string |  | Autodesk User ID of a user managed by BIM 360 Admin |
| 28 | contact_id | string |  | Autodesk User ID of a user managed by BIM 360 Admin |
| 29 | created_at | timestamp: SQL |  | The date/time the payment is created. |
| 30 | updated_at | timestamp: SQL |  | The date/time the payment is last modified. |
| 31 | approved_at | timestamp: SQL |  | The date/time the payment is approved. |
| 32 | paid_at | timestamp: SQL |  | The date/time the payment is paid. |
| 33 | submitted_at | timestamp: SQL |  | The date/time the payment is submitted. |
| 34 | note | string |  | The additional note. |
| 35 | materials_billed | number |  | The amount of the materials billed in this period. |
| 36 | materials_retention | number |  | The percentage of the retention for the materials billed. |
| 37 | integration_state | string |  | A field indicate the record integration status, possible values: "integrated", "locked", "failed", null |
| 38 | integration_state_changed_by | string |  | The integration user who changed the integration state |
| 39 | integration_state_changed_at | timestamp: SQL |  | The timestamp when the integration state changed |
| 40 | external_id | string |  | The ID of the entity in external system. |
| 41 | external_system | string |  | The name of the external system. |
| 42 | message | string |  | The comment added by the integration. |
| 43 | last_sync_time | timestamp: SQL |  | The timestamp of last time when the sync happened between cost management and external system |

## budget_properties

Custom properties for a Budget

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | budget_id | string: UUID |  | The budget ID for this custom property Foreign Key: Table: budgets Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | name | string |  | Name of the custom attribute. Inherited from the custom attribute definition. |
| 5 | built_in | boolean |  | A flag to indicate whether this is a pre-defined attribute or not. Inherited from the custom attribute definition. |
| 6 | position | number |  | The order of the custom attribute displayed in the BIM 360 Cost Management. Inherited from the custom attribute definition. |
| 7 | property_definition_id | string: UUID |  | The ID of the custom attribute definition. |
| 8 | type | string |  | The type of the custom attribute. Inherited from the custom attribute definition. |
| 9 | value | string |  | The value of the custom attribute. |

## budget_transfers

Transfers between budgets in cost management

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The Id of the budget transfer. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data. |
| 4 | number | string |  | The number of the budget transfer. |
| 5 | name | string |  | The name of the budget transfer. |
| 6 | note | string |  | Notes about the budget transfer. |
| 7 | status | string |  | The status of the budget transfer. Possible values are "open", "inReview", "approved", "reviseAndResubmit", "rejected" |
| 8 | approved_at | timestamp: SQL |  | The time when the budget transfer approved |
| 9 | creator_id | string |  | Autodesk User ID for the user who created the main contract - referring to an id of a user managed by BIM 360 Admin |
| 10 | changed_by | string |  | Autodesk User ID for the user who made the last change - referring to an id of a user managed by BIM 360 Admin |
| 11 | created_at | timestamp: SQL |  | The date/time the budget transfer is created. |
| 12 | updated_at | timestamp: SQL |  | The date/time the budget transfer is updated. |
| 13 | integration_state | string |  | A field indicate the record integration status, possible values: "integrated", "locked", "failed", null |
| 14 | integration_state_changed_by | string |  | The integration user who changed the integration state |
| 15 | integration_state_changed_at | timestamp: SQL |  | The timestamp when the integration state changed |
| 16 | external_id | string |  | The ID of the entity in external system. |
| 17 | external_system | string |  | The name of the external system. |
| 18 | message | string |  | The comment added by the integration. |
| 19 | last_sync_time | timestamp: SQL |  | The timestamp of last time when the sync happened between cost management and external system |

## budgets

Budgets defined in a BIM 360 Project.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique identifier of budget item. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | parent_id | string: UUID |  | Id of a parent budget item - null for root items. |
| 5 | code | string | Max length: 255 | Unique code compliant to the Budget Code Template defined by the Project Admin. |
| 6 | name | string | Max length: 1024 | Name of the Budget. |
| 7 | description | string | Max length: 2048 | Detail description of the Budget. |
| 8 | quantity | number |  | Quantity of a Budget. |
| 9 | unit_price | number |  | Unit price of a Budget. |
| 10 | unit | string |  | Unit of measures of the Budget. |
| 11 | original_amount | number |  | Original amount of the Budget - equals quantity * unitPrice |
| 12 | internal_adjustment | number |  | Internal transfers between budgets |
| 13 | approved_owner_changes | number |  | Total of changes approved by Owner |
| 14 | pending_owner_changes | number |  | Total of changes waiting for the approval of Owner |
| 15 | original_commitment | number |  | The original amount committed to the supplier contract. |
| 16 | approved_change_orders | number |  | Total of changes committed to Supplier. |
| 17 | approved_in_scope_change_orders | number |  | Total of in-scope changes committed to Supplier. |
| 18 | pending_change_orders | number |  | Total of changes not committed. |
| 19 | reserves | number |  | Total of changes under estimation. |
| 20 | actual_cost | number |  | Total of actual cost. |
| 21 | main_contract_id | string: UUID |  | Id of the Main Contract that the budget belongs to. |
| 22 | contract_id | string: UUID |  | ID of the Contract that the budget is awarded to. |
| 23 | adjustments_total | number |  | Total of all the actual cost adjustments. |
| 24 | uncommitted | number |  | The amount that has been approved by owner but not committed to Supplier: approvedOwnerChanges - (approvedChangeOrders - approvedInScopeChangeOrders) |
| 25 | revised | number |  | Total of the approved budget from owner - equals originalAmount + internalAdjustment + approvedOwnerChanges |
| 26 | projected_cost | number |  | For budget - it is equal to originalCommitment + approvedChangeOrders + pendingChangeOrders + reserves. For contract - it is equal to awarded + approvedChangeOrders + pendingChangeOrders + reserves |
| 27 | projected_budget | number |  | revised + pending_owner_changes |
| 28 | forecast_final_cost | number |  | projectedCost + adjustmentsTotal |
| 29 | forecast_variance | number |  | projectedBudget - forecastFinalCost |
| 30 | forecast_cost_complete | number |  | forecastFinalCost - actualCost |
| 31 | variance_total | number |  | Variance of a budget - equals projectedBudget - projectedCost |
| 32 | created_at | timestamp: SQL |  | The timestamp when the item was created. |
| 33 | updated_at | timestamp: SQL |  | The timestamp when the item was last updated. |
| 34 | original_contracted | number |  | The original amount contracted to the supplier. |
| 35 | compounded | string |  | A JSON string contains a collection of customized column values. |
| 36 | integration_state | string |  | A field indicate the record integration status, possible values: "integrated", "locked", "failed", null |
| 37 | integration_state_changed_by | string |  | The integration user who changed the integration state |
| 38 | integration_state_changed_at | timestamp: SQL |  | The timestamp when the integration state changed |
| 39 | external_id | string |  | The ID of the entity in external system. |
| 40 | external_system | string |  | The name of the external system. |
| 41 | message | string |  | The comment added by the integration. |
| 42 | last_sync_time | timestamp: SQL |  | The timestamp of last time when the sync happened between cost management and external system |
| 43 | pending_internal_budget_transfer | number |  | The amount of the budget transfers that are not approved yet. |
| 44 | pending_internal_budget_transfer_qty | number |  | The quantity of the budget transfers that are not approved yet. |
| 45 | pending_internal_budget_transfer_input_qty | number |  | The input quantity(hours) of the budget transfers that are not approved yet. |
| 46 | code_segment_values | string |  | The composition of the code of the budget. |
| 47 | main_contract_item_amount | number |  | Total amount of associated main contract items |
| 48 | approved_cost_payment_application | number |  | Total net amount of approved or paid cost payment applications |
| 49 | approved_budget_payment_application | number |  | Total net amount of approved or paid budget payment applications |
| 50 | locations | string |  | Locations assigned to the budget |
| 51 | forecast_adjustment_qty | number |  | Cost Forecast Adjustments Qty of the budget |

## change_order_cost_items

Relationship between Change Orders and Cost Items.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | change_order_id | string: UUID |  | The change order ID for this cost item Foreign Key: Table: change_orders Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | cost_item_id | string: UUID |  | System ID of a Cost Item |

## change_order_properties

Custom properties for a Change Order

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | change_order_id | string: UUID |  | The change order ID for this custom property Foreign Key: Table: change_orders Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | name | string |  | Name of the custom attribute. Inherited from the custom attribute definition. |
| 5 | built_in | boolean |  | A flag to indicate whether this is a pre-defined attribute or not. Inherited from the custom attribute definition. |
| 6 | position | number |  | The order of the custom attribute displayed in the BIM 360 Cost Management. Inherited from the custom attribute definition. |
| 7 | property_definition_id | string: UUID |  | The ID of the custom attribute definition. |
| 8 | type | string |  | The type of the custom attribute. Inherited from the custom attribute definition. |
| 9 | value | string |  | The value of the custom attribute. |

## change_orders

Change Orders as defined in BIM 360

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique identifier of a Change Order - auto generated. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | number | string | Max length: 255 | System generated sequence. |
| 5 | name | string | Max length: 1024 | Name of a Change Order |
| 6 | description | string | Max length: 2048 | Detail description of a Change Order. |
| 7 | creator_id | string |  | Autodesk User ID of a user managed by BIM 360 Admin |
| 8 | owner_id | string |  | Autodesk User ID of a user managed by BIM 360 Admin |
| 9 | changed_by | string |  | Autodesk User ID of a user managed by BIM 360 Admin |
| 10 | contract_id | string: UUID |  | ID of the Contract that the budget is awarded to. |
| 11 | form_type | string | Possible Values: pco rfq rco oco sco | Type of this change order: pco, rfq, rco, oco, sco |
| 12 | markup_formula_id | string: UUID |  | ID of Markup formula applied to this Change Order. |
| 13 | applied_by | string |  | The user id who applied markups to this Change Order. The id is a project user from BIM 360 Admin |
| 14 | applied_at | timestamp: SQL |  | The time when the markup is applied. |
| 15 | budget_status | string |  | The status of a PCO - RCO and OCO: PCO: [draft - open - submitted - accepted - approved - executed - rejected] RCO: [draft - open - submitted - accepted - rejected] - OCO: [draft - open - submitted - approved - executed - rejected]. Empty for RFQ - SCO The status of the change order should not be updated directly - but triggered by the action that will perform on it. |
| 16 | cost_status | string |  | The cost status of a PCO - RCO and OCO: PCO: [draft - open - pricing - proposed - approved - executed - rejected] RFQ: [draft - open - pricing - proposed - rejected] SCO: [draft - open - sent - executed] Empty for RCO - OCO The status of the change order should not be updated directly - but triggered by the action that will perform on it. |
| 17 | scope_of_work | string |  | Draftjs formatted rich text(https://draftjs.org/) |
| 18 | note | string |  | Draftjs formatted rich text(https://draftjs.org/) |
| 19 | created_at | timestamp: SQL |  | The timestamp when the item was created. |
| 20 | updated_at | timestamp: SQL |  | The timestamp when the item was last updated. |
| 21 | type | string |  | Customized type of the change order, e.g. Back Change, Budget Transfer, Owner Change Order, Owner Directive... |
| 22 | schedule_change | number |  | The schedule change of this change order. |
| 23 | integration_state | string |  | A field indicate the record integration status, possible values: "integrated", "locked", "failed", null |
| 24 | integration_state_changed_by | string |  | The integration user who changed the integration state |
| 25 | integration_state_changed_at | timestamp: SQL |  | The timestamp when the integration state changed |
| 26 | external_id | string |  | The ID of the entity in external system. |
| 27 | external_system | string |  | The name of the external system. |
| 28 | message | string |  | The comment added by the integration. |
| 29 | last_sync_time | timestamp: SQL |  | The timestamp of last time when the sync happened between cost management and external system |
| 30 | proposed_revised_completion_date | timestamp: SQL |  | the proposed revised completion date |
| 31 | source_type | string |  | the source type of change order |
| 32 | approved_at | timestamp: SQL |  | the approved date |
| 33 | status_changed_at | timestamp: SQL |  | the status change date |
| 34 | main_contract_id | string: UUID |  | the main contract id |
| 35 | quantity | number |  | the quantity of change order |
| 36 | unit | string |  | the unit of change order |
| 37 | estimated | number |  | the estimated of change order |
| 38 | proposed | number |  | the proposed of change order |
| 39 | submitted | number |  | the submitted of change order |
| 40 | approved | number |  | the approved of change order |
| 41 | committed | number |  | the committed of change order |
| 42 | compliance_status | enum: string | Possible Values: compliant notApplicable notRequired pending | The compliance status of the change order |

## contract_properties

Custom properties for a Contract

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | contract_id | string: UUID |  | The contract ID for this custom property Foreign Key: Table: contracts Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | name | string |  | Name of the custom attribute. Inherited from the custom attribute definition. |
| 5 | built_in | boolean |  | A flag to indicate whether this is a pre-defined attribute or not. Inherited from the custom attribute definition. |
| 6 | position | number |  | The order of the custom attribute displayed in the BIM 360 Cost Management. Inherited from the custom attribute definition. |
| 7 | property_definition_id | string: UUID |  | The ID of the custom attribute definition. |
| 8 | type | string |  | The type of the custom attribute. Inherited from the custom attribute definition. |
| 9 | value | string |  | The value of the custom attribute. |

## contracts

Supplier Contract defined in the project.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique identifier of the Contract. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | code | string | Max length: 255 | Human readable code of the Contract. |
| 5 | name | string | Max length: 1024 | Name of the Contract. |
| 6 | description | string | Max length: 2048 | Detail description of a Contract |
| 7 | company_id | string |  | Id of a supplier company managed by BIM 360 Admin |
| 8 | type | string |  | Type of the contract - e.g. consultant - purchase order - which is customizable by Project Admin. |
| 9 | contact_id | string |  | Autodesk User ID for the default contact of the supplier - referring to an id of a user managed by BIM 360 Admin |
| 10 | creator_id | string |  | Autodesk User ID of a user managed by BIM 360 Admin |
| 11 | signed_by | string |  | Autodesk User ID of a user managed by BIM 360 Admin |
| 12 | owner_id | string |  | Autodesk User ID of a user managed by BIM 360 Admin |
| 13 | changed_by | string |  | Autodesk User ID id of a user managed by BIM 360 Admin |
| 14 | status | string |  | The status of this contract - status includes [draft - closed - open - executed - sent]. |
| 15 | awarded | number |  | Amount of the original Contract |
| 16 | original_budget | number |  | Original amount of budgets associated to this Contract. |
| 17 | internal_adjustment | number |  | Internal transfers of budgets associated to this Contract. |
| 18 | approved_owner_changes | number |  | Changes approved by Owner. |
| 19 | pending_owner_changes | number |  | Changes pending approval from Owner. |
| 20 | approved_change_orders | number |  | Total of changes committed to Supplier. |
| 21 | approved_in_scope_change_orders | number |  | Total of in-scope changes committed to Supplier. |
| 22 | pending_change_orders | number |  | Total of changes not committed. |
| 23 | reserves | number |  | Total of changes under estimating. |
| 24 | actual_cost | number |  | Total of actual cost. |
| 25 | uncommitted | number |  | The amount that has been approved by owner but not committed to Supplier: approvedOwnerChanges - (approvedChangeOrders - approvedInScopeChangeOrders) |
| 26 | revised | number |  | Total of the approved budget from owner - equals originalAmount + internalAdjustment + approvedOwnerChanges |
| 27 | projected_cost | number |  | For budget - it is equal to originalCommitment + approvedChangeOrders + pendingChangeOrders + reserves. For contract - it is equal to awarded + approvedChangeOrders + pendingChangeOrders + reserves |
| 28 | projected_budget | number |  | revised + pending_owner_changes |
| 29 | forecast_final_cost | number |  | projectedCost + adjustmentsTotal |
| 30 | forecast_variance | number |  | projectedBudget - forecastFinalCost |
| 31 | forecast_cost_complete | number |  | forecastFinalCost - actualCost |
| 32 | variance_total | number |  | Variance of a budget - equals projectedBudget - projectedCost |
| 33 | awarded_at | timestamp: SQL |  | The time when the Contract is awarded. |
| 34 | status_changed_at | timestamp: SQL |  | The last time when the status is updated. |
| 35 | sent_at | timestamp: SQL |  | The time when the Contract is sent to the Supplier. |
| 36 | responded_at | timestamp: SQL |  | The time when the Supplier responds. |
| 37 | returned_at | timestamp: SQL |  | The time when the Contract is signed and returned. |
| 38 | onsite_at | timestamp: SQL |  | The time when the Supplier on-site to the job. |
| 39 | offsite_at | timestamp: SQL |  | The time when the Supplier completes the job. |
| 40 | procured_at | timestamp: SQL |  | The time for Purchase Order. |
| 41 | approved_at | timestamp: SQL |  | The time when the Contract is approved. |
| 42 | created_at | timestamp: SQL |  | The timestamp when the item was created. |
| 43 | updated_at | timestamp: SQL |  | The timestamp when the item was last updated. |
| 44 | scope_of_work | string |  | Draftjs formatted rich text(https://draftjs.org/) |
| 45 | note | string |  | Draftjs formatted rich text(https://draftjs.org/) |
| 46 | adjustments_total | number |  | Total of all the actual cost adjustments. |
| 47 | executed_at | timestamp: SQL |  | The timestamp when the item was executed. |
| 48 | currency | string |  | The code of the currency specified for the contract if it's awarded in a foreign currency. |
| 49 | exchange_rate | number |  | The exchange rate for the specified currency, applied as a multiplier of the contract's base currency. For example, 1 base currency = 0.7455 foreign currency. |
| 50 | integration_state | string |  | A field indicate the record integration status, possible values: "integrated", "locked", "failed", null |
| 51 | integration_state_changed_by | string |  | The integration user who changed the integration state |
| 52 | integration_state_changed_at | timestamp: SQL |  | The timestamp when the integration state changed |
| 53 | external_id | string |  | The ID of the entity in external system. |
| 54 | external_system | string |  | The name of the external system. |
| 55 | message | string |  | The comment added by the integration. |
| 56 | last_sync_time | timestamp: SQL |  | The timestamp of last time when the sync happened between cost management and external system |
| 57 | pending_internal_budget_transfer | number |  | The amount of the budget transfers that are not approved yet. |
| 58 | compliance_status | enum: string | Possible Values: compliant notApplicable notRequired pending | The compliance status of the contract |
| 59 | awarded_tax_total | number |  | Tax Amount of the original Contract |
| 60 | response_due | timestamp: SQL |  | The time when the response is due |

## cost_item_properties

Custom properties for a Cost Item

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | cost_item_id | string: UUID |  | The cost_item ID for this custom property Foreign Key: Table: cost_items Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | name | string |  | Name of the custom attribute. Inherited from the custom attribute definition. |
| 5 | built_in | boolean |  | A flag to indicate whether this is a pre-defined attribute or not. Inherited from the custom attribute definition. |
| 6 | position | number |  | The order of the custom attribute displayed in the BIM 360 Cost Management. Inherited from the custom attribute definition. |
| 7 | property_definition_id | string: UUID |  | The ID of the custom attribute definition. |
| 8 | type | string |  | The type of the custom attribute. Inherited from the custom attribute definition. |
| 9 | value | string |  | The value of the custom attribute. |

## cost_items

Cost items

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique identifier of a Cost Item. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | number | string |  | System generated sequence number. |
| 5 | name | string | Max length: 255 | Name of a Cost Item. |
| 6 | description | string |  | Detail description of a Cost Item. |
| 7 | budget_id | string: UUID |  | The contract ID for this adjustment entry Foreign Key: Table: budgets Column: id |
| 8 | budget_status | string |  | The budget status of a Cost Item: [draft - open - submitted - accepted - approved - executed - rejected]. The status of the cost item should not be updated directly - but controlled by the change order containing it. |
| 9 | cost_status | string |  | The cost status of a Cost Item: [draft - open - pricing - proposed - approved - executed - rejected]. The status of the cost item should not be updated directly - but controlled by the change order containing it. |
| 10 | scope | enum: string |  | Scope of a Cost Item. Possible values: out - in - tbd |
| 11 | type | enum: string |  | Cost item type |
| 12 | estimated | number |  | Rough estimation of this item without quotation. |
| 13 | proposed | number |  | Quotated cost of the item. |
| 14 | submitted | number |  | Amount sent to Owner for approval. |
| 15 | approved | number |  | Amount approved by Owner. |
| 16 | committed | number |  | Amount committed to the Supplier. |
| 17 | scope_of_work | string |  | Draftjs formatted rich text(https://draftjs.org/) |
| 18 | note | string |  | Draftjs formatted rich text(https://draftjs.org/) |
| 19 | created_at | timestamp: SQL |  | The timestamp when the item was created. |
| 20 | updated_at | timestamp: SQL |  | The timestamp when the item was last updated. |
| 21 | schedule_change | number |  | The schedule change days |
| 22 | approved_tax_summary | string |  | A JSON string which contains oco tax of the cost item |
| 23 | committed_tax_summary | string |  | A JSON string which contains sco tax of the cost item |
| 24 | estimated_tax_summary | string |  | A JSON string which contains pco tax of the cost item |
| 25 | proposed_tax_summary | string |  | A JSON string which contains rfq tax of the cost item |
| 26 | submitted_tax_summary | string |  | A JSON string which contains cor tax of the cost item |
| 27 | is_markup | boolean |  | Is markup cost item or not |
| 28 | quantity | number |  | The quantity for the cost item |
| 29 | unit | enum: string |  | The unit for the cost item |

## cost_payment_items

Budget Payment Items as defined in BIM 360

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique identifier of a payment item - auto generated. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | payment_id | string: UUID |  | The ID of the payment that the item is in. |
| 5 | parent_id | string: UUID |  | The parend item ID if current item is a child. |
| 6 | number | string | Max length: 1024 | Number of an budget payment item. |
| 7 | name | string | Max length: 1024 | Name of a budget payment item. |
| 8 | description | string | Max length: 2048 | Detail description of a budget payment item. |
| 9 | unit | string |  | The unit of measure of the payment item. |
| 10 | original_amount | number |  | The amount of the scheduled of value. |
| 11 | original_qty | number |  | The quantity of the scheduled of value. |
| 12 | original_unit_price | number |  | The unit price of the scheduled of value. |
| 13 | amount | number |  | The amount of work completed for this scheduled of value. |
| 14 | unit_price | number |  | The unit price of work completed for this scheduled of value. |
| 15 | qty | number |  | The quantity of work completed for this scheduled of value. |
| 16 | materials_on_store | number |  | The amount on store quanity for this schedule of value. |
| 17 | materials_on_store_qty | number |  | The quantity on store quanity for this schedule of value. |
| 18 | materials_on_store_unit_price | number |  | The unit price on store quanity for this schedule of value. |
| 19 | previous_amount | number |  | The previous amount of work completed. |
| 20 | previous_qty | number |  | The previous quantity of work completed. |
| 21 | previous_unit_price | number |  | The unit price of previous work complete. |
| 22 | previous_materials_on_store | number |  | The material on store of previus period. |
| 23 | completed_work_retention_percent | number |  | The retention % of work complete. |
| 24 | materials_on_store_retention_percent | number |  | The retention % of material on store. |
| 25 | completed_work_released | number |  | The released amount for work completed in this period. |
| 26 | materials_on_store_released | number |  | The released amount for material on store in this period. |
| 27 | net_amount | number |  | The net amount: work completed + material on store - retention + release. |
| 28 | status | string |  | The status of the the payment item. |
| 29 | creator_id | string |  | Autodesk User ID of a user managed by BIM 360 Admin |
| 30 | changed_by | string |  | Autodesk User ID of a user managed by BIM 360 Admin |
| 31 | created_at | timestamp: SQL |  | The date/time the payment item is created. |
| 32 | updated_at | timestamp: SQL |  | The date/time the payment item is last modified. |
| 33 | tax_summary | string |  | A JSON string which contains tax on the payment item |

## cost_payment_properties

Custom properties for a Cost Payment

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | cost_payment_id | string: UUID |  | The cost ID for this custom property Foreign Key: Table: cost_payments Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | name | string |  | Name of the custom attribute. Inherited from the custom attribute definition. |
| 5 | built_in | boolean |  | A flag to indicate whether this is a pre-defined attribute or not. Inherited from the custom attribute definition. |
| 6 | position | number |  | The order of the custom attribute displayed in the BIM 360 Cost Management. Inherited from the custom attribute definition. |
| 7 | property_definition_id | string: UUID |  | The ID of the custom attribute definition. |
| 8 | type | string |  | The type of the custom attribute. Inherited from the custom attribute definition. |
| 9 | value | string |  | The value of the custom attribute. |

## cost_payments

Cost Payment as defined in BIM 360

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique identifier of a budget payment - auto generated. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | contract_id | string: UUID |  | The ID of the supplier contract the payment is pursuant to. |
| 5 | start_date | timestamp: SQL |  | The start date of the payment billing period. |
| 6 | end_date | timestamp: SQL |  | The end date of the payment billing period. |
| 7 | due_date | timestamp: SQL | Max length: 255 | The due date of the payment. |
| 8 | number | string | Max length: 1024 | Number of a payment. |
| 9 | name | string | Max length: 1024 | Name of a payment. |
| 10 | description | string | Max length: 2048 | Detail description of a payment. |
| 11 | original_amount | number |  | The origianl contracted amount of th |
| 12 | amount | number |  | Work completed of this period of the payment. |
| 13 | previous_amount | number |  | Total of work completed of before this billing period. |
| 14 | materials_on_store | number |  | Material on site of this billing period. |
| 15 | previous_materials_on_store | number |  | Material on site of the previous billing period. |
| 16 | approved_change_orders | number |  | The total of approved change orders. |
| 17 | contract_amount | number |  | The current total of the contracted amount: orginal_amount + approved_change_orders |
| 18 | completed_work_retention | number |  | Total of the retention for total work complete. |
| 19 | materials_on_store_retention | number |  | Total of the retention for material on site |
| 20 | net_amount | number |  | Net amount of current work completed + material on site - retentions. |
| 21 | paid_amount | number |  | The amount paid by owner. |
| 22 | status | string |  | The status of the budget payment. |
| 23 | company_id | string |  | The Autodesk ID of the supplier company. |
| 24 | payment_type | string |  | How is the expense paid, e.g. Cash, Check, Electronic Transfer |
| 25 | payment_reference | string |  | The reference info how the expense is paid. |
| 26 | creator_id | string |  | Autodesk User ID of a user managed by BIM 360 Admin |
| 27 | changed_by | string |  | Autodesk User ID of a user managed by BIM 360 Admin |
| 28 | contact_id | string |  | Autodesk User ID of a user managed by BIM 360 Admin |
| 29 | created_at | timestamp: SQL |  | The date/time the payment is created. |
| 30 | updated_at | timestamp: SQL |  | The date/time the payment is last modified. |
| 31 | approved_at | timestamp: SQL |  | The date/time the payment is approved. |
| 32 | paid_at | timestamp: SQL |  | The date/time the payment is paid. |
| 33 | submitted_at | timestamp: SQL |  | The date/time the payment is submitted. |
| 34 | note | string |  | The additinal note of the payment. |
| 35 | materials_billed | number |  | The amount of the materials billed in this period. |
| 36 | materials_retention | number |  | The percentage of the retention for the materials billed. |
| 37 | integration_state | string |  | A field indicate the record integration status, possible values: "integrated", "locked", "failed", null |
| 38 | integration_state_changed_by | string |  | The integration user who changed the integration state |
| 39 | integration_state_changed_at | timestamp: SQL |  | The timestamp when the integration state changed |
| 40 | external_id | string |  | The ID of the entity in external system. |
| 41 | external_system | string |  | The name of the external system. |
| 42 | message | string |  | The comment added by the integration. |
| 43 | last_sync_time | timestamp: SQL |  | The timestamp of last time when the sync happened between cost management and external system |
| 44 | tax_summary | string |  | A JSON string which contains tax on the payment |
| 45 | compliance_status | enum: string | Possible Values: compliant notApplicable notRequired pending | The compliance status of the payment |

## distribution_item_curves

The period data for a distribution item's curve

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique identifier of the distribution item curve - auto generated. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data. |
| 4 | distribution_item_id | string: UUID |  | The ID of the distribution item. |
| 5 | actual_total | number |  | The actual total amount for this distribution curve. |
| 6 | distribution_total | number |  | The total distributed amount for this distribution curve. |
| 7 | curve | string | Max length: 255 | Distribution curve. Possible values are "revisedBudget", "workCompleted", "actualCost", "forecastFinalCost", "projectedBudget", "revisedCost". |
| 8 | periods | string |  | The JSON object that contains the periods of the distribution item curve. The key is period, value is amount. |
| 9 | actual_total_input_qty | number |  | The actual total input quantity for this distribution curve. |
| 10 | distribution_total_input_qty | number |  | The total distributed input quantity for this distribution curve. |
| 11 | periods_input_qty | string |  | The JSON object that contains the periods of the distribution item curve. The key is period, value is input quantity. |
| 12 | created_at | timestamp: SQL |  | The date/time the distribution curve is created. |
| 13 | updated_at | timestamp: SQL |  | The date/time the distribution item is last updated. |

## distribution_items

Distribution items as defined in BIM 360

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique identifier of the distribution item - auto generated. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data. |
| 4 | budget_id | string |  | The ID of budgets associated with this distribution item. |
| 5 | association_id | string: UUID |  | The ID of the entity which the distribution item is associated to. |
| 6 | association_type | string | Max length: 255 | The type of the entity which the distribution item is associated to. |
| 7 | number | string | Max length: 1024 | The number of the distribution item. |
| 8 | name | string | Max length: 1024 | The name of the distribution item. |
| 9 | status | string | Max length: 64 | The status of the distribution item. |
| 10 | due_date | timestamp: SQL |  | The due date of the distribution item. |
| 11 | company_id | string: UUID |  | The Autodesk ID of the owner company. |
| 12 | contact_id | string | Max length: 128 | Autodesk User ID of a user managed by BIM 360 Admin. |
| 13 | creator_id | string | Max length: 128 | Autodesk User ID of a user managed by BIM 360 Admin. |
| 14 | changed_by | string | Max length: 128 | Autodesk User ID of a user managed by BIM 360 Admin. |
| 15 | submitted_at | timestamp: SQL |  | The date/time the distribution item is submitted. |
| 16 | accepted_at | timestamp: SQL |  | The date/time the distribution item is accepted. |
| 17 | created_at | timestamp: SQL |  | The date/time the distribution item is created. |
| 18 | updated_at | timestamp: SQL |  | The date/time the distribution item is updated. |

## expense_items

Expense items as defined in BIM 360

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique identifier of an expense detail item - auto generated. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | expense_id | string: UUID |  | The ID of the expense the item is in. |
| 5 | budget_id | string: UUID |  | The ID of the budget. |
| 6 | contract_id | string: UUID |  | The ID of the contract. |
| 7 | number | string | Max length: 255 | System generated sequence. |
| 8 | name | string | Max length: 1024 | Name of an Expense |
| 9 | description | string | Max length: 2048 | Detail description of an expense |
| 10 | unit | string |  | The unit of measure of the expense item. |
| 11 | unit_price | number |  | The price of the item. |
| 12 | quantity | number |  | The quantity of the item. |
| 13 | amount | number |  | The amount of the item. |
| 14 | tax | number |  | The tax amount of the item. |
| 15 | created_at | timestamp: SQL |  | The date/time the expens item is created. |
| 16 | updated_at | timestamp: SQL |  | The date/time the expens item is last modified. |

## expense_properties

Custom properties for an Expense

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | expense_id | string: UUID |  | The expense ID for this custom property Foreign Key: Table: expenses Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | name | string |  | Name of the custom attribute. Inherited from the custom attribute definition. |
| 5 | built_in | boolean |  | A flag to indicate whether this is a pre-defined attribute or not. Inherited from the custom attribute definition. |
| 6 | position | number |  | The order of the custom attribute displayed in the BIM 360 Cost Management. Inherited from the custom attribute definition. |
| 7 | property_definition_id | string: UUID |  | The ID of the custom attribute definition. |
| 8 | type | string |  | The type of the custom attribute. Inherited from the custom attribute definition. |
| 9 | value | string |  | The value of the custom attribute. |

## expenses

Expenses as defined in BIM 360

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique identifier of an Expense - auto generated. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | number | string | Max length: 255 | System generated sequence. |
| 5 | name | string | Max length: 1024 | Name of an Expense |
| 6 | description | string | Max length: 2048 | Detail description of an expense |
| 7 | creator_id | string |  | Autodesk User ID of a user managed by BIM 360 Admin |
| 8 | changed_by | string |  | Autodesk User ID of a user managed by BIM 360 Admin |
| 9 | supplier_id | string |  | Autodesk group ID of the supplier company |
| 10 | supplier_name | string |  | The name of the supplier company. |
| 11 | amount | number |  | The total amount of the expense. |
| 12 | paid_amount | number |  | The total paid amount of the expense. |
| 13 | status | string |  | The stauts of the expense. |
| 14 | type | string |  | The type of the expense. |
| 15 | payment_type | string |  | How is the expense paid, e.g. Cash, Check, Electronic Transfer |
| 16 | payment_reference | string |  | The reference info how the expense is paid. |
| 17 | created_at | timestamp: SQL |  | The date/time the expense is created. |
| 18 | updated_at | timestamp: SQL |  | The date/time the expense is last modified. |
| 19 | issued_at | timestamp: SQL |  | The date/time the expense is issued. |
| 20 | received_at | timestamp: SQL |  | The date/time the expense is recieved. |
| 21 | approved_at | timestamp: SQL |  | The date/time the expense is approved. |
| 22 | paid_at | timestamp: SQL |  | The date/time the expense is paid. |
| 23 | reference_number | string |  | The references to the expense, e.g. the invoice number. |
| 24 | integration_state | string |  | A field indicate the record integration status, possible values: "integrated", "locked", "failed", null |
| 25 | integration_state_changed_by | string |  | The integration user who changed the integration state |
| 26 | integration_state_changed_at | timestamp: SQL |  | The timestamp when the integration state changed |
| 27 | external_id | string |  | The ID of the entity in external system. |
| 28 | external_system | string |  | The name of the external system. |
| 29 | message | string |  | The comment added by the integration. |
| 30 | last_sync_time | timestamp: SQL |  | The timestamp of last time when the sync happened between cost management and external system |
| 31 | payment_due | timestamp: SQL |  | The timestamp of the payment of the expense is due |

## main_contract_items

Main contract items in cost management

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique identifier of a main contract item |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | main_contract_id | string: UUID |  | The ID of the main contract the item belongs |
| 5 | budget_id | string: UUID |  | The ID of the budget |
| 6 | parent_id | string: UUID |  | The ID of the parent of the item |
| 7 | code | string |  | The code of the item |
| 8 | name | string |  | The name of the item |
| 9 | description | string |  | The description of the item |
| 10 | qty | number |  | The quantity of the item |
| 11 | unit_price | number |  | The unit price of the item |
| 12 | unit | string |  | The unit of the item |
| 13 | amount | number |  | The amount of the item |
| 14 | changed_by | string |  | The ID of the one changed the item |
| 15 | is_private | boolean |  | The flag to indicate whether the item is hidden to owners. |
| 16 | created_at | timestamp: SQL |  | The date/time the item is created |
| 17 | updated_at | timestamp: SQL |  | The date/time the item is last modified |

## main_contract_properties

Custom properties for a Main Contract

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | main_contract_id | string: UUID |  | The main contract ID for this custom property Foreign Key: Table: main_contracts Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | name | string |  | Name of the custom attribute. Inherited from the custom attribute definition. |
| 5 | built_in | boolean |  | A flag to indicate whether this is a pre-defined attribute or not. Inherited from the custom attribute definition. |
| 6 | position | number |  | The order of the custom attribute displayed in the BIM 360 Cost Management. Inherited from the custom attribute definition. |
| 7 | property_definition_id | string: UUID |  | The ID of the custom attribute definition. |
| 8 | type | string |  | The type of the custom attribute. Inherited from the custom attribute definition. |
| 9 | value | string |  | The value of the custom attribute. |

## main_contracts

The main or owner contracts of the project.

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The uniq ID of the approval workflow. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | code | string |  | The code of the main contract. |
| 5 | name | string |  | The name of the main contract. |
| 6 | description | string |  | The description of the main contract. |
| 7 | type | string |  | The type of the main contract. |
| 8 | status | string |  | The status of the main contract. |
| 9 | amount | number |  | The total amount of the main contract. |
| 10 | retention_cap | number |  | The max retention of % of main contract sum to date. |
| 11 | contact_id | string |  | Autodesk User ID for the default contact of the main contract - referring to an id of a user managed by BIM 360 Admin |
| 12 | creator_id | string |  | Autodesk User ID for the user who created the main contract - referring to an id of a user managed by BIM 360 Admin |
| 13 | owner_id | string |  | Autodesk User ID for the user who will pay the main contract - referring to an id of a user managed by BIM 360 Admin |
| 14 | changed_by | string |  | Autodesk User ID for the user who made the last change - referring to an id of a user managed by BIM 360 Admin |
| 15 | scope_of_work | string |  | The scope of the work of the main contract. |
| 16 | note | string |  | The note of the work of the main contract. |
| 17 | start_date | timestamp: SQL |  | The start date of the main contract. |
| 18 | executed_date | timestamp: SQL |  | The execute date of the main contract. |
| 19 | planned_completion_date | timestamp: SQL |  | The planned completion date of the main contract. |
| 20 | actual_completion_date | timestamp: SQL |  | The actual completion date of the main contract. |
| 21 | close_date | timestamp: SQL |  | The closed date of the main contract. |
| 22 | created_at | timestamp: SQL |  | The date/time the item is created. |
| 23 | updated_at | timestamp: SQL |  | The date/time the item is last modified. |
| 24 | revised_completion_date | timestamp: SQL |  | The revised completion date |
| 25 | schedule_change | number |  | The days that the schedule was impacted by changes. |

## payment_references

Payment references used by Budget Payment, Cost Payment and Expense in Cost Management

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The ID of the payment reference. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | amount | number |  | The amount being paid. |
| 5 | type | string |  | The payment method, e.g. cash, check. |
| 6 | reference | string |  | The reference/note to the payment, e.g. check NO. |
| 7 | paid_at | timestamp: SQL |  | The date/time the Payment or Expense is paid. |
| 8 | association_id | string: UUID |  | The ID of the Payment or Expense the payment reference associated to. |
| 9 | association_type | string |  | The type of the payment reference is associated to: Expense or Payment. |
| 10 | created_at | timestamp: SQL |  | The date/time the item is created. |
| 11 | updated_at | timestamp: SQL |  | The date/time the item is last modified. |

## permissions

Permission in cost management

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The ID of the permission. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | policy_id | string: UUID |  | The related policy in ACM. |
| 5 | subject_id | string |  | Autodesk ID for the user or user group who will be applied this permission - referring to an id of a user or user group managed by BIM 360 Admin |
| 6 | subject_type | string |  | The type of the subject, possible values: User, Company, Role. |
| 7 | permission_level | string |  | The permission level, possible values:fullControl, viewAll, collaborate, collaborateCreate, noAccess. |
| 8 | resource_type | string |  | The resource of permission. |
| 9 | created_at | timestamp: SQL |  | The date/time the item is created. |
| 10 | updated_at | timestamp: SQL |  | The date/time the item is last modified. |

## schedule_of_values_properties

Custom properties for a Schedule of Value

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | schedule_of_value_id | string: UUID |  | The schedule of value ID for this custom property Foreign Key: Table: schedule_of_values Column: id |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data |
| 4 | name | string |  | Name of the custom attribute. Inherited from the custom attribute definition. |
| 5 | built_in | boolean |  | A flag to indicate whether this is a pre-defined attribute or not. Inherited from the custom attribute definition. |
| 6 | position | number |  | The order of the custom attribute displayed in the BIM 360 Cost Management. Inherited from the custom attribute definition. |
| 7 | property_definition_id | string: UUID |  | The ID of the custom attribute definition. |
| 8 | type | string |  | The type of the custom attribute. Inherited from the custom attribute definition. |
| 9 | value | string |  | The value of the custom attribute. |

## sub_distribution_items

Sub distribution items in cost management

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique identifier of this sub distribution item. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data. |
| 4 | distribution_item_id | string: UUID |  | The ID of distribution item. |
| 5 | association_id | string |  | The ID of the entity which the sub distribution item is associated to. |
| 6 | association_type | string | Max length: 255 | The type of the entity which the sub distribution item is associated to. |
| 7 | number | string | Max length: 1024 | The number of the sub distribution item. |
| 8 | name | string | Max length: 1024 | The name of the sub distribution item. |
| 9 | start_date | date: string |  | The planned start day of this sub distribution item. |
| 10 | end_date | date: string |  | The planned end day of this sub distribution item. |
| 11 | actual_total | number |  | The actual total amount to be distributed. |
| 12 | distribution_total | number |  | The total distributed amount for this sub distribution item. |
| 13 | type | string | Max length: 255 | The type of this sub distribution item. |
| 14 | curve | string | Max length: 255 | Distribution curve. Possible values are "revisedBudget", "workCompleted", "actualCost", "forecastFinalCost", "projectedBudget", "revisedCost". |
| 15 | periods | string |  | The JSON object that contains the periods of this sub distribution items. The key is period, value is amount. |
| 16 | created_at | timestamp: SQL |  | The date/time the sub distribution item is created. |
| 17 | updated_at | timestamp: SQL |  | The date/time the sub distribution item is deleted. |
| 18 | actual_total_input_qty | number |  | The actual total input quantity to be distributed. |
| 19 | distribution_total_input_qty | number |  | The total distributed input quantity for this sub distribution item. |
| 20 | periods_input_qty | string |  | The JSON object that contains the periods of this sub distribution items. The key is period, value is input quantity. |

## transferences

Budget transference details in cost management

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | The Id of the budget transfer details. |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | Added for project scoping of issues data. |
| 4 | budget_id | string: UUID |  | The budget id where it transfers from |
| 5 | relating_budget_id | string: UUID |  | The relating budget id where it transfers to |
| 6 | contract_id | string: UUID |  | The contract id of the budget where it transfers from |
| 7 | relating_contract_id | string: UUID |  | The relating contract id of the budget where it transfers to |
| 8 | transaction_id | string: UUID |  | The transaction Id of the transference |
| 9 | amount | number |  | The amount of the budget transfer |
| 10 | unit_price | number |  | The unit price of the budget transfer |
| 11 | qty | number |  | The QTY of the budget transfer |
| 12 | input_qty | number |  | The input QTY of the budget transfer |
| 13 | relating_unit_price | number |  | The relating unit price of the budget transfer |
| 14 | relating_qty | number |  | The relating QTY of the budget transfer |
| 15 | relating_input_qty | number |  | The relating input QTY of the budget transfer |
| 16 | creator_id | string |  | Autodesk User ID for the user who created the main contract - referring to an id of a user managed by BIM 360 Admin |
| 17 | note | string |  | The notes about the budget transfer when creating |
| 18 | main_contract_id | string: UUID |  | The main contract Id that the budget associated where it transfer out |
| 19 | created_at | timestamp: SQL |  | The date/time the budget transfer is created. |
| 20 | updated_at | timestamp: SQL |  | The date/time the budget transfer is updated. |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
