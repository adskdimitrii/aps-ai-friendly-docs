# Ellipse

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/ellipse/

---

Objects

# Ellipse

[](#)

Represents an Ellipse geometry

## [Fields](#fields)

| range*   [ParamRange!](objects-paramrange.md) `non-null` | The parameter range of the Ellipse. |
| --- | --- |
| center*   [Point!](objects-point.md) `non-null` | The center point of the Ellipse. |
| normal*   [Vector!](objects-vector.md) `non-null` | The normal vector of the Ellipse’s plane. |
| majorRadius*   [Vector!](objects-vector.md) `non-null` | The major radius vector of the Ellipse. |
| radiusRatio*   [Float!](scalars.md) `non-null` | The radius ratio of the Ellipse. |
| type*   [CurveType!](objects-curvetype.md) `non-null` | The curve type. |

* Required

## [Implements](#implements)

| Usage | Used By | Description |
| --- | --- | --- |
| Interface | [Curve](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/interfaces/curve/) | Interface for all curve types. |
