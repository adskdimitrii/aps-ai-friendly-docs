# CurveType

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/curvetype/

---

Objects

# CurveType

[](#) Enum which represents the possible types of a Curve.

## [Valid Values](#valid-values)

| Value | Description |
| --- | --- |
| CIRCLE | Circle Type |
| LINE | Line Type |
| POLYLINE | Polyline Type |
| BCURVE | BCurve Type |
| ELLIPSE | Ellipse Type |

## [Where Used](#where-used)

| Object/Input | Field | Description |
| --- | --- | --- |
| [BCurve](objects-bcurve.md) | `type`. | Represents a BCurve geometry. |
| [Circle](objects-circle.md) | `type`. | Represents a circle geometry |
| [Curve](scalars.md) | `type`. | Interface for all curve types. |
| [Ellipse](objects-ellipse.md) | `type`. | Represents an Ellipse geometry |
| [Line](objects-line.md) | `type`. | Represents a Line geometry |
| [Polyline](objects-polyline.md) | `type`. | Represents a polyline geometry. |
