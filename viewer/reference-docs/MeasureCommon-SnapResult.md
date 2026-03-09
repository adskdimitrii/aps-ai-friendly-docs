# SnapResult

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/MeasureCommon/SnapResult/

---

Autodesk.Viewing.MeasureCommon

# SnapResult

## [new SnapResult()](#new-snapresult)

Encapsulates the result of a Snap operation performed by the [Snapper](Snapping-Snapper.md).

# Methods

## [clear()](#clear)

Resets the object to its non-snapping state.

## [copyTo(destiny)](#copyto-destiny)

Copies the current state of the object into another.

### Parameters

| destiny*   [SnapResult](MeasureCommon-SnapResult.md) | target for the copy operation. |
| --- | --- |

* Required

## [clone()](#clone)

Creates a new instance and copies the current state into it.

### Returns

| type | description |
| --- | --- |
| [SnapResult](MeasureCommon-SnapResult.md) |  |

## [isEmpty()](#isempty)

### Returns

| type | description |
| --- | --- |
| boolean | true only when snapping information is available. |

## [getFace()](#getface)

Gets the snapped face, when available.

## [getEdge()](#getedge)

Gets the snapped edge, when available.

## [getVertex()](#getvertex)

Gets the snapped vertex, when available.

## [getGeometry()](#getgeometry)

Gets the snapped element, which differs depending on what kind of element it was snapped to, see [SnapType](#fixMe/).
