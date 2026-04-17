# OriginComponentFilterInput

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/inputs/origincomponentfilterinput/

---

Inputs

# OriginComponentFilterInput

[](#)

Filter input for querying elements by their origin component location and existence.

## [Fields](#fields)

| originRange   [OriginRange](inputs-originrange.md) | Spatial area defined by start and end coordinates to filter elements within a specific 3D range |
| --- | --- |
| exists   [Boolean](scalars.md) | When true, returns only elements that have origin component data; when false, returns elements without origin components |

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Argument for Input | [elementfilterinput](inputs-elementfilterinput.md) | Query input for filtering Elements. |
