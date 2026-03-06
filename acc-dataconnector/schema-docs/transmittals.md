# transmittals Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=transmittals&format=html

---

# transmittals Schema Description

**Documentation Updated:** 2025-02-05  

- [transmittal_documents](#transmittal_documents)
- [transmittal_non_members](#transmittal_non_members)
- [transmittal_recipients](#transmittal_recipients)
- [workflow_transmittals](#workflow_transmittals)

## transmittal_documents

Object to define a transmittal document

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique id for the transmittal document |
| 2 | workflow_transmittal_id | string: UUID |  | Id for the transmittal the document belongs to |
| 3 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 4 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 5 | urn | string |  | The URN of the document |
| 6 | file_name | string |  | File name of the document |
| 7 | version_number | number |  | The specific version of the document |
| 8 | revision_number | number |  | The specific revision of the document |
| 9 | parent_folder_urn | string |  | The URN of the folder that the document belongs to |
| 10 | last_modified_time | timestamp: SQL |  | Last modified time of the document |
| 11 | last_modified_user_id | string |  | Id of the last modified user |
| 12 | last_modified_user_name | string |  | Name of the last modified user |
| 13 | created_at | timestamp: SQL |  | Creation time of the transmittal document |
| 14 | updated_at | timestamp: SQL |  | Update time of the transmittal document |

## transmittal_non_members

Object to define a transmittal external recipient

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique id for the transmittal external recipient |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | email | string |  | External user inputed email. |
| 5 | first_name | string |  | External user inputed first name. |
| 6 | last_name | string |  | External user inputed last name. |
| 7 | company_name | string |  | External user inputed company name. |
| 8 | role | string |  | External user inputed role name. |
| 9 | workflow_transmittal_id | string: UUID |  | Id for the transmittal the recipient belongs to |
| 10 | viewed_at | timestamp: SQL |  | The first time of when the recipient is viewed this transmittal |
| 11 | downloaded_at | timestamp: SQL |  | The first time of when the recipient is downloaded this transmittal |
| 12 | created_at | timestamp: SQL |  | Creation time of the transmittal non member |
| 13 | updated_at | timestamp: SQL |  | Update time of the transmittal non member |

## transmittal_recipients

Object to define a transmittal recipient

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique id for the transmittal recipient |
| 2 | workflow_transmittal_id | string: UUID |  | Id for the transmittal the recipient belongs to |
| 3 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 4 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 5 | user_id | string: UUID |  | Id of user who owns the document |
| 6 | user_name | string |  | Name of user who owns the document |
| 7 | email | string |  | Email of user who owns the document |
| 8 | created_at | timestamp: SQL |  | Creation time of the transmittal recipient |
| 9 | updated_at | timestamp: SQL |  | Update time of the transmittal recipient |
| 10 | company_name | string |  | The name of recipient's company |
| 11 | viewed_at | timestamp: SQL |  | The first time of when the recipient is viewed this transmittal |
| 12 | downloaded_at | timestamp: SQL |  | The first time of when the recipient is downloaded this transmittal |

## workflow_transmittals

Object to define a transmittal with the basic information

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique id for the transmittal |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | sequence_id | number |  | The sequence id of the transmittal |
| 5 | title | string |  | Title of the transmittal |
| 6 | status | number |  | Status of the transmittal, 1 => SENDING, 2 => COMPLETED, 3 => FAILED |
| 7 | create_user_id | string: UUID |  | Id of user who create the transmittal |
| 8 | create_user_name | string |  | Name of user who create the transmittal |
| 9 | docs_count | number |  | The count of documents that belong to the transmittal |
| 10 | created_at | timestamp: SQL |  | Creation time of the transmittal |
| 11 | updated_at | timestamp: SQL |  | Update time of the transmittal |
| 12 | create_user_company_id | string |  | Company id of the user who create the transmittal |
| 13 | create_user_company_name | string |  | Company name of the user who create the transmittal |

© Copyright 2026 Autodesk Inc. | [Autodesk Construction Cloud](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
