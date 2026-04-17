# packages Schema Description

Source: https://developer.api.autodesk.com/data-connector/v1/doc/schema?name=packages&format=html

---

# packages Schema Description

**Documentation Updated:** 2025-01-15  

- [package_associations](#package_associations)
- [package_roles](#package_roles)
- [packages](#packages)
- [version_resources](#version_resources)

## package_associations

The data of package associations

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique id for the package association |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | package_id | string: UUID |  | The id of the package that the association belongs to |
| 5 | version_id | string: UUID |  | The id of the version file that the association belongs to |

## package_roles

The data of package managers

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique id for the package role |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | adsk_id | string |  | The Autodesk ID |
| 5 | adsk_id_type | enum: string | Possible Values: user role company | The Autodesk ID type |
| 6 | created_at | timestamp: SQL |  | The created time of the package |
| 7 | created_by | string |  | Id of user who create the package |
| 8 | updated_at | timestamp: SQL |  | The updated time of the package |
| 9 | updated_by | string |  | Id of user who update the package |
| 10 | status | enum: string | Possible Values: inactive active pending disable | detailed column 7 description |

## packages

The data of packages

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | id | string: UUID |  | Unique id for the package |
| 2 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 3 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 4 | locked | boolean |  | Indicating whether the package is locked |
| 5 | locked_at | timestamp: SQL |  | The lock time |
| 6 | locked_by | string |  | The user id who locked the package |
| 7 | name | string |  | The name of this package |
| 8 | description | string |  | The description of this package |
| 9 | resource_count | number |  | The count of the resources in the package |
| 10 | created_at | timestamp: SQL |  | The created time of the package |
| 11 | created_by | string |  | Id of user who create the package |
| 12 | updated_at | timestamp: SQL |  | The updated time of the package |
| 13 | updated_by | string |  | Id of user who update the package |
| 14 | version_resource_option | string |  | Indicates that versions under a package are fixed versions or keep up to date. |

## version_resources

The data of the version files in packages

| ordinal_position | column_name | data_type | constraints | notes |
| --- | --- | --- | --- | --- |
| 1 | bim360_account_id | string: UUID |  | BIM 360 HQ Account ID. |
| 2 | bim360_project_id | string: UUID |  | BIM 360 HQ Project ID. |
| 3 | version_id | string: UUID |  | The id of the version file |
| 4 | urn | string |  | The URN of the version file |
| 5 | version | number |  | The version number of this version file |
| 6 | revision | number |  | The revision number of this version file |
| 7 | file_type | string |  | The file type of this version file |
| 8 | path | string |  | The folder path of this version file |
| 9 | trashed | boolean |  | Indicating whether this file or its parent folder has been deleted |
| 10 | name | string |  | The file name of this version file |
| 11 | file_size | number |  | The file size of this version file |
| 12 | created_at | timestamp: SQL |  | The created time of the package |
| 13 | created_by | string |  | Id of user who create the package |
| 14 | updated_at | timestamp: SQL |  | The updated time of the package |
| 15 | updated_by | string |  | Id of user who update the package |

© Copyright 2026 Autodesk Inc. | [Autodesk Forma](https://construction.autodesk.com/) | [About Autodesk](https://www.autodesk.com/company)
