# VersionFilterInput

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/inputs/versionfilterinput/

---

Inputs

# VersionFilterInput

[](#)

Filter input for specifying version resolution behavior.

## [Fields](#fields)

| versionType   [VersionTypeEnum](objects-versiontypeenum.md) | Specifies which version number to use. Defaults to PUBLISHED if not provided. |
| --- | --- |

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Argument for Query | [elementGroupByVersionNumber](queries-elementgroupbyversionnumber.md) | Retrieves elementGroup by version number and ID. |
| Argument for Query | [elementsByElementGroupAtVersion](queries-elementsbyelementgroupatversion.md) | Retrieves elements from given elementGroup at given elementGroup version, using additional RSQL filters if provided. |
| Argument for Query | [diffElementGroupByVersionWithLatest](queries-diffelementgroupbyversionwithlatest.md) | Returns a list of element differences and their difference type from target elementGroup. |
| Argument for Query | [diffElementByVersionWithLatest](queries-diffelementbyversionwithlatest.md) | Returns the element difference from target element. |
| Argument for Field | [ElementGroupVersionHistory](objects-elementgroupversionhistory.md) | Information related to versions of an elementGroup. |
