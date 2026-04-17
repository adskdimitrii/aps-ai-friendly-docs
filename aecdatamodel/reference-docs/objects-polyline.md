# Polyline

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/polyline/

---

Objects

# Polyline

[](#)

Represents a polyline geometry.

## [Fields](#fields)

| range*   [ParamRange!](objects-paramrange.md) `non-null` | The parameter range of the Polyline. |
| --- | --- |
| points*   [[Point!]!](/en/docs/aecdatamodel/v1/reference/objects/point) `non-null` | The list of control points that define the polyline. |
| closed*   [Boolean!](scalars.md) `non-null` | Indicates whether the polyline is closed (forms a loop). |
| type*   [CurveType!](objects-curvetype.md) `non-null` | The curve type. |

* Required

## [Implements](#implements)

| Usage | Used By | Description |
| --- | --- | --- |
| Interface | [Curve](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/interfaces/curve/) | Interface for all curve types. |
