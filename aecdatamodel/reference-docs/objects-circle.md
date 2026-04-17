# Circle

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/circle/

---

Objects

# Circle

[](#)

Represents a circle geometry

## [Fields](#fields)

| range*   [ParamRange!](objects-paramrange.md) `non-null` | The parameter range of the circle. |
| --- | --- |
| center*   [Point!](objects-point.md) `non-null` | The center point of the circle. |
| normal*   [Vector!](objects-vector.md) `non-null` | The normal vector of the circle’s plane. |
| radius*   [Point!](objects-point.md) `non-null` | The radius of the circle. |
| type*   [CurveType!](objects-curvetype.md) `non-null` | The curve type. |

* Required

## [Implements](#implements)

| Usage | Used By | Description |
| --- | --- | --- |
| Interface | [Curve](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/interfaces/curve/) | Interface for all curve types. |
