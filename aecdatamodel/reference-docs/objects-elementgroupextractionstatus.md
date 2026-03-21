# ElementGroupExtractionStatus

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/elementgroupextractionstatus/

---

Objects

# ElementGroupExtractionStatus

[](#)

Information about elementGroup extraction status.

## [Fields](#fields)

| status*   [ExtractionStatus!](objects-extractionstatus.md) `non-null` | Extraction status. |
| --- | --- |
| details   [String](scalars.md) | Additional information about extraction status. |
| elementGroup   [ElementGroup](objects-elementgroup.md) | If available, the ElementGroup which corresponds to the extraction. |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Query By | [elementGroupExtractionStatus](queries-elementgroupextractionstatus.md) | Retrieves the extraction status of the given elementGroup. |
| Query By | [elementGroupExtractionStatusAtTip](queries-elementgroupextractionstatusattip.md) | Retrieves the extraction status for the latest version of elementGroup. |
