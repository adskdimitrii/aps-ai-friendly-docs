# Line

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/line/

---

Objects

# Line

[](#)

Represents a Line geometry

## [Fields](#fields)

| range*   [ParamRange!](objects-paramrange.md) `non-null` | The parameter range of the line. |
| --- | --- |
| position*   [Point!](objects-point.md) `non-null` | The position of the line. |
| direction*   [Vector!](objects-vector.md) `non-null` | The direction vector of the line. |
| type*   [CurveType!](objects-curvetype.md) `non-null` | The curve type. |

* Required

## [Implements](#implements)

| Usage | Used By | Description |
| --- | --- | --- |
| Interface | [Curve](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/interfaces/curve/) | Interface for all curve types. |
