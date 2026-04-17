# BCurve

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/bcurve/

---

Objects

# BCurve

[](#)

Represents a BCurve geometry.

## [Fields](#fields)

| range*   [ParamRange!](objects-paramrange.md) `non-null` | The parameter range of the BCurve. |
| --- | --- |
| degree*   [Int!](scalars.md) `non-null` | The degree of the BCurve. |
| knots*   [[Float!]!](/en/docs/aecdatamodel/v1/reference/scalars) `non-null` | The knots of the BCurve. |
| controlPoints*   [[Point!]!](/en/docs/aecdatamodel/v1/reference/objects/point) `non-null` | The control points that define the BCurve. |
| weights*   [[Float!]!](/en/docs/aecdatamodel/v1/reference/scalars) `non-null` | The weights of the BCurve. |
| type*   [CurveType!](objects-curvetype.md) `non-null` | The curve type. |

* Required

## [Implements](#implements)

| Usage | Used By | Description |
| --- | --- | --- |
| Interface | [Curve](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/interfaces/curve/) | Interface for all curve types. |
