# GeometryPiece

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/geometrypiece/

---

Objects

# GeometryPiece

[](#)

Represents a Geometry Piece.

## [Fields](#fields)

| type*   [GeometryComponentType!](objects-geometrycomponenttype.md) `non-null` | The type of the geometry component. |
| --- | --- |
| geometry   [GeometryPieceData](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/unions/geometrypiecedata/) | The actual geometry piece data. |
| storageLengthUnit   [String](scalars.md) | The storage length unit of the geometry piece. |
| transform   [Transform](objects-transform.md) | The transform of the geometry piece. |

* Required
