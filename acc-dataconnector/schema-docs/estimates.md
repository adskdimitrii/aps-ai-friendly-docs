# estimates Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=estimates&format=html

---

# estimates Schema Description

**Documentation Updated:** 2025-10-21  

- [cost_markup_formula_bond_levels](#cost_markup_formula_bond_levels)
- [cost_markup_formula_items](#cost_markup_formula_items)
- [cost_markup_formula_sections](#cost_markup_formula_sections)
- [cost_markup_formulas](#cost_markup_formulas)
- [equipment_cost_calculations](#equipment_cost_calculations)
- [estimation_instances](#estimation_instances)
- [labor_cost_calculations](#labor_cost_calculations)
- [material_cost_calculations](#material_cost_calculations)
- [settings](#settings)

**Beta Release**  
This is a Beta release of the estimates data set and schema definitions are subject to change or even possibly be removed from the final data set release. Thank you for your understanding with any future schema updates.

## cost_markup_formula_bond_levels

Table for cost markup formula bond levels

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Resource Identifier |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. This column is added to enable simple data extraction by the Data. |
| 4 | item_id | string: UUID |  | Foreign Key: Table: cost_markup_formula_items Column: id |
| 5 | order | number |  | The order of the bond level within the parent markup item. The first bond level in the item starts with a value of 0. |
| 6 | amount | number |  | The amount for the bond level. This column is nullable. If the value is null, it means no amount has been specified and this level will not contribute to markup calculation. If specified, the valid range for this is: 0 < x < 100000000 |
| 7 | percentage | number |  | The percentage for the bond level. This column is nullable. If the value is null, it means no percentage has been specified and this level will not contribute to markup calculation. If specified, the valid range for this is: 0 <= x <= 999 |
| 8 | created_at | timestamp: SQL |  | UTC timestamp when the row was created. |
| 9 | updated_at | timestamp: SQL |  | UTC timestamp when the row was last updated. |

## cost_markup_formula_items

Table for cost markup formula items

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Resource identifier |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. This column is added to enable simple data extraction by the Data. This column is nullable. If the value is null, it means this is an account-level settings. |
| 4 | section_id | string: UUID |  | Foreign Key: Table: cost_markup_formula_sections Column: id |
| 5 | description | string: null |  | Item description This column is nullable. If the value is null, it means no description has been specified. |
| 6 | order | number |  | The order of the current item within the parent markup section. The first item in the formula starts with an value of 0. |
| 7 | markup_type | enum: string | Possible Values: MARKUP MARGIN LUMP_SUM BOND | Cost markup type |
| 8 | cost_basis_source | enum: string | Possible Values: CURRENT PRECEDING PRECEDING_MARKUP ESTIMATE SECTION PROJECT. | Cost basis source |
| 9 | cost_basis_section_id | string: UUID |  | The section id if the cost_basis_source is SECTION. Otherwise, this column will be set to null. FOREIGN_KEY: cost_markup_formula_sections, id |
| 10 | amount | number |  | The amount to apply when the markup type is LUMP_SUM. This column is nullable. If the value is null, it means the amount has not been specified. If specified, the valid range for the value is: 0 <= x <= 100000000 |
| 11 | percentage | number |  | The percentage to apply when the markup type is MARKUP or MARGIN. This column is nullable. If the value is null, it means the percentage has not been specified. If specified, the valid range for the value is: 0 <= x <= 999 |
| 12 | total | number |  | Total markup for the item. This column is nullable. If this value is null, it means the total is not available. If specified, the valid range for the value is: 0 <= x <= 100000000 |
| 13 | created_at | timestamp: SQL |  | UTC timestamp when the row was created. |
| 14 | updated_at | timestamp: SQL |  | UTC timestamp when the row was last updated. |

## cost_markup_formula_sections

Table for cost markup formula sections

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Resource identifier |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. This column is added to enable simple data extraction by the Data. |
| 4 | formula_id | string: UUID |  | Foreign Key: Table: cost_markup_formulas Column: id |
| 5 | description | string |  | Description of the markup section This column is nullable. If the value is null, it means no description has been specified. |
| 6 | order | number |  | The order of the current section within the parent markup formula. The first section in the formula starts with an value of 0. |
| 7 | total | number |  | Total markup for the section. This column is nullable. If the value is null, it means the total is not available. If specified, the valid range for the value is: 0 <= x <= 100000000 |
| 8 | created_at | timestamp: SQL |  | UTC timestamp when the row was created. |
| 9 | updated_at | timestamp: SQL |  | UTC timestamp when the row was last updated. |

## cost_markup_formulas

Table for cost markup formulas

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Resource identifier |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. This column is added to enable simple data extraction by the Data. |
| 4 | total | number |  | Total markup for the project. This column is nullable. If the value is null, it means the total is not available. If specified, the valid range for the value is: 0 <= x <= 100000000 |
| 5 | created_at | timestamp: SQL |  | UTC timestamp when the row was created. |
| 6 | updated_at | timestamp: SQL |  | UTC timestamp when the row was last updated. |

## equipment_cost_calculations

Table for equipment cost calculations

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Resource identifier |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. This column is added to enable simple data extraction by the Data. |
| 4 | equipment_type | string: null |  | Equipment type This column is nullable. If the value is null, it means no equipment type has been selected. |
| 5 | rate | number |  | The cost rate. This column is nullable. If the value is null, it means no rate has been specified. |
| 6 | productivity | number |  | The productivity for equipment cost. This column is nullable. If the value is null, it means no productivity has been specified. |
| 7 | productivity_unit | enum: string | Possible Values: H D | The unit of time measurement. This column is nullable. If the value is null, it means no unit has been specified. |
| 8 | rounding | enum: string | Possible Values: UP DOWN NONE | Rounding method. This column is nullable. If the value is null, then rounding will be default to NONE |
| 9 | created_at | timestamp: SQL |  | UTC timestamp when the row was created. |
| 10 | updated_at | timestamp: SQL |  | UTC timestamp when the row was last updated. |

## estimation_instances

Table for estimation instances

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Resource identifier |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. This column is added to enable simple data extraction by the Data. |
| 4 | name | string |  | Name / description for the instance |
| 5 | unit_of_measure | enum: string | Possible Values: EA LF SF CY TON YD SY CF LBS M M2 M3 T KG | The unit of measurement for the quantity |
| 6 | part_number | string: null |  | Part number associated with this instance |
| 7 | barcode | string: null |  | Bar code associated with this instance |
| 8 | quantity | number |  | Amount of material associated with this instance |
| 9 | takeoff_instance_count | number |  | Number of takeoff items associated with this instance. This column is nullable. If this value is null, it means this instance is not synced with any takeoff items. |
| 10 | material_cost_calculation_id | string: UUID |  | Foreign Key: Table: material_cost_calculations Column: id |
| 11 | material_cost_total | number |  | Total material cost for the instance. This column is nullable. If the value is null, it means the calculated material cost is not available. |
| 12 | labor_cost_calculation_id | string: UUID |  | Foreign Key: Table: labor_cost_calculations Column: id |
| 13 | labor_cost_total | number |  | Total labor cost for the instance. This column is nullable. If the value is null, it means the calculated labor cost is not available. |
| 14 | equipment_cost_calculation_id | string: UUID |  | Foreign Key: Table: equipment_cost_calculations Column: id |
| 15 | equipment_cost_total | number |  | Total equipment cost for this instance. This column is nullable. If the value is null, it means the calculated equipment cost is not available. |
| 16 | other_cost_rate | number |  | Other cost rate. This column is nullable. If the value is null, it means the cost rate has not been specified. If specified, the valid range for the value is: 0 <= x <= 100000000 |
| 17 | other_cost_total | number |  | Total other cost for this instance. This column is nullable. If the value is null, it means the total other cost is not available. |
| 18 | subcontractor_cost_rate | number |  | Subcontractor cost rate. This column is nullable. If the value is null, it means the subcontractor cost rate has not been not specified. If specified, the valid range for the value is: 0 <= x <= 100000000 |
| 19 | subcontractor_cost_total | number |  | Total subcontractor cost for his instance. This column is nullable. If the value is null, it means the total cost is not available. If it is not null, then the valid range for the value is: 0 <=x <= 100000000 |
| 20 | total_cost | number |  | Total cost for the instance. This column is nullable. If the value is null, it means the total cost is not available. |
| 21 | markup_total | number |  | Total markup applied for this specific instance. This column is nullable. If the value is null, it means the instance specific markup is not available. |
| 22 | classification1_id | string: UUID |  | Foreign Key: Table: classifications Column: id (takeoff) |
| 23 | classification2_id | string: UUID |  | Foreign Key: Table: classifications Column: id (takeoff) |
| 24 | content_lineage_id | string: UUID |  | Foreign Key: Table: classifications Column: id (takeoff) |
| 25 | package_id | string: UUID |  | Foreign Key: Table: packages Column: id (takeoff) |
| 26 | location_id | string: UUID |  | Foreign Key: Table: locations_id (locations) Column: |
| 27 | created_at | timestamp: SQL |  | UTC timestamp when the row was created. |
| 28 | updated_at | timestamp: SQL |  | UTC timestamp when the row was last updated. |

## labor_cost_calculations

Table for labor cost calculations

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Resource identifier |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. This column is added to enable simple data extraction by the Data. |
| 4 | labor_type | string: null |  | Labor type This column is nullable. If the value is null, it means no labor type has been selected. |
| 5 | rate_type | enum: string | Possible Values: STANDARD UNION PREVAILING | Labor cost rate type. This column is nullable. If the value is null, it means the rate type has not been specified. |
| 6 | rate | number |  | Labor cost rate. This column is nullable. If this value is null, it means the cost rate has not been specified. If specified, the valid range for the value is: 0 <= X <= 100000000 |
| 7 | daily_hours | number |  | Daily hours for the labor cost. This column is nullable. If this value is null, it means the daily hours has not been specified. If specified, the valid range for the value is: 0 <= x <= 24 |
| 8 | productivity | number |  | Productivity for labor cost. This column is nullable. If the value is null, it means no productivity has been specified. If specified, the valid range for the value is: x <= 0 <= 999.99 |
| 9 | productivity_unit | enum: string | Possible Values: H D | Unit of time measurement. This column is nullable. If the value is null, it means no unit has been specified. |
| 10 | created_at | timestamp: SQL |  | UTC timestamp when the row was created. |
| 11 | updated_at | timestamp: SQL |  | UTC timestamp when the row was last updated. |

## material_cost_calculations

Table for material cost calculations

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Resource identifier |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. This column is added to enable simple data extraction by the Data. |
| 4 | rate | number |  | The cost rate. The valid range for the value is: 0 <= X <= 100000000 |
| 5 | factor | number |  | The cost factor. |
| 6 | factor_unit | enum: string | Possible Values: EA IN LF YD SI SF SY CI CF CY LBS TON MM M M2 M3 KG T | The unit of measurement for the factor. |
| 7 | waste_percentage | number |  | The cost waster percentage. The valid range for the value is: 0 <= x <= 100 |
| 8 | rounding | enum: string | Possible Values: UP DOWN NONE | The rounding method. This column is nullable. If the value is null, then rounding will be default to NONE |
| 9 | created_at | timestamp: SQL |  | UTC timestamp when the row was created. |
| 10 | updated_at | timestamp: SQL |  | UTC timestamp when the row was last updated. |

## settings

Table for estimate settings

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. This column is added to enable simple data extraction by the Data. This column is nullable. If the value is null, it means this is an account-level settings. |
| 3 | measurement_system | enum: string | Possible Values: IMPERIAL METRIC | The project measurement system. This column is nullable. If the value is null, it means the measurement system for the project has not been configured. |
| 4 | currency | enum: string | Possible Values: USD AED AFN ALL AMD ANG AOA ARS AUD AWG AZN BAM BBD BDT BGN BHD BIF BMD BND BOB BOV BRL BSD BTN BWP BYN BYR BZD CAD CDF CHE CHF CHW CLF CLP CNY COP COU CRC CUC CUP CVE CZK DJF DKK DOP DZD EEK EGP ERN ETB EUR FJD FKP GBP GEL GHS GIP GMD GNF GTQ GYD HKD HNL HRK HTG HUF IDR ILS INR IQD IRR ISK JMD JOD JPY KES KGS KHR KMF KPW KRW KWD KYD KZT LAK LBP LKR LRD LSL LTL LVL LYD MAD MDL MGA MKD MMK MNT MOP MRU MUR MVR MWK MXN MXV MYR MZN NAD NGN NIO NOK NPR NZD OMR PAB PEN PGK PHP PKR PLN PYG QAR RON RSD RUB RWF SAR SBD SCR SDG SEK SGD SHP SLE SLL SOS SRD SSP STN SVC SYP SZL THB TRL TJS TMT TND TOP TRY TTD TWD TZS UAH UGX USN UYI UYU UYW UZS VED VES VND VUV WST XAF XAG XAU XBA XBB XBC XBD XCD XDR XOF XPD XPF XPT XSU XTS XUA XXX YER ZAR ZMW ZWL | The project currency code in ISO 4217 format. This column is nullable. If the value is null, it means the currency code for the project has not been configured. |
| 5 | created_at | timestamp: SQL |  | UTC timestamp when the row was created. |
| 6 | updated_at | timestamp: SQL |  | UTC timestamp when the row was last updated. |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
