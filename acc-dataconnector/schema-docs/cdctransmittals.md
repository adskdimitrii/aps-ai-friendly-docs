# cdctransmittals Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=cdctransmittals&format=html

---

# cdctransmittals Schema Description

**Documentation Updated:** 2025-12-08  

- [transmittal_documents](#transmittal_documents)
- [transmittal_non_members](#transmittal_non_members)
- [transmittal_recipients](#transmittal_recipients)
- [workflow_transmittals](#workflow_transmittals)

**Beta Release**  
This is a Beta release of the cdctransmittals data set and schema definitions are subject to change or even possibly be removed from the final data set release. Thank you for your understanding with any future schema updates.

## transmittal_documents

Object to define a transmittal document - This is the Change Data Capture (CDC) enabled version of the transmittals.transmittal_documents table.  Date Range Extractions Supported

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
| 13 | created_at | timestamp: SQL |  | Creation time of the transmittal document Column used for filtering Date Range Extraction requests |
| 14 | updated_at | timestamp: SQL |  | Update time of the transmittal document Column used for filtering Date Range Extraction requests |
| 15 | deleted_at | timestamp: SQL |  | Timestamp when the transmittal_document was deleted Column used for filtering Date Range Extraction requests |
| 16 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## transmittal_non_members

Object to define a transmittal external recipient - This is the Change Data Capture (CDC) enabled version of the transmittals.transmittal_non_members table.  Date Range Extractions Supported

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
| 12 | created_at | timestamp: SQL |  | Creation time of the transmittal non member Column used for filtering Date Range Extraction requests |
| 13 | updated_at | timestamp: SQL |  | Update time of the transmittal non member Column used for filtering Date Range Extraction requests |
| 14 | deleted_at | timestamp: SQL |  | Timestamp when the transmittal_non_member was deleted Column used for filtering Date Range Extraction requests |
| 15 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## transmittal_recipients

Object to define a transmittal recipient - This is the Change Data Capture (CDC) enabled version of the transmittals.transmittal_recipients table.  Date Range Extractions Supported

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique id for the transmittal recipient |
| 2 | workflow_transmittal_id | string: UUID |  | Id for the transmittal the recipient belongs to |
| 3 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 4 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 5 | user_id | string: UUID |  | Id of user who owns the document |
| 6 | user_name | string |  | Name of user who owns the document |
| 7 | email | string |  | Email of user who owns the document |
| 8 | created_at | timestamp: SQL |  | Creation time of the transmittal recipient Column used for filtering Date Range Extraction requests |
| 9 | updated_at | timestamp: SQL |  | Update time of the transmittal recipient Column used for filtering Date Range Extraction requests |
| 10 | company_name | string |  | The name of recipient's company |
| 11 | viewed_at | timestamp: SQL |  | The first time of when the recipient is viewed this transmittal |
| 12 | downloaded_at | timestamp: SQL |  | The first time of when the recipient is downloaded this transmittal |
| 13 | deleted_at | timestamp: SQL |  | Timestamp when the transmittal_recipient was deleted Column used for filtering Date Range Extraction requests |
| 14 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

## workflow_transmittals

Object to define a transmittal with the basic information - This is the Change Data Capture (CDC) enabled version of the transmittals.workflow_transmittals table.  Date Range Extractions Supported

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
| 10 | created_at | timestamp: SQL |  | Creation time of the transmittal Column used for filtering Date Range Extraction requests |
| 11 | updated_at | timestamp: SQL |  | Update time of the transmittal Column used for filtering Date Range Extraction requests |
| 12 | create_user_company_id | string |  | Company id of the user who create the transmittal |
| 13 | create_user_company_name | string |  | Company name of the user who create the transmittal |
| 14 | deleted_at | timestamp: SQL |  | Timestamp when the workflow_transmittal was deleted Column used for filtering Date Range Extraction requests |
| 15 | adsk_row_id | string |  | Unique row identifier to be used in CDC operations |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
