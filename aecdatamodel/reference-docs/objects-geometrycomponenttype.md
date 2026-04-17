# GeometryComponentType

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/geometrycomponenttype/

---

Objects

# GeometryComponentType

[](#) Enum which represents the possible types of a Geometry Component.

## [Valid Values](#valid-values)

| Value | Description |
| --- | --- |
| PRIMITIVE | Primitive Type |
| BINARYDATA | Binary Data Type |
| INSTANCE | Instance Type |

## [Where Used](#where-used)

| Object/Input | Field | Description |
| --- | --- | --- |
| [GeometryPiece](objects-geometrypiece.md) | `type`. | Represents a Geometry Piece. |
| [GeometryComponentsFilterInput](inputs-geometrycomponentsfilterinput.md) | `types`. | Types of components |
