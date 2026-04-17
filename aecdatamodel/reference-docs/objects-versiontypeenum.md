# VersionTypeEnum

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/versiontypeenum/

---

Objects

# VersionTypeEnum

[](#) Specifies whether a version number refers to a WIP (timeline) version or a PUBLISHED (lineage) version.

## [Valid Values](#valid-values)

| Value | Description |
| --- | --- |
| WIP | WIP version number from the document timeline. |
| PUBLISHED | Published (lineage) version number. |

## [Where Used](#where-used)

| Object/Input | Field | Description |
| --- | --- | --- |
| [versionfilterinput](inputs-versionfilterinput.md) | `versionType`. | Specifies which version number to use. Defaults to PUBLISHED if not provided. |
