# Snapper

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Snapping/Snapper/

---

Autodesk.Viewing.Extensions.Snapping

# Snapper

## [new Snapper(viewer, options)](#new-snapper-viewer-options)

A tool that lets users attach pointer events to vertices and edges. It supports 2D and 3D models.

### Parameters

| viewer*   [Viewer3D](Viewing-Viewer3D.md) | Viewer instance |
| --- | --- |
| options*   object | Configurations for the extension |

* Required

# Methods

## [isActive()](#isactive)

### Returns

| type | description |
| --- | --- |
| boolean | true when the tool is active |

## [activate()](#activate)

Starts intercepting pointer events. Invoked automatically by the [ToolController](Viewing-ToolController.md).

## [deactivate()](#deactivate)

Stops intercepting pointer events. Invoked automatically by the [ToolController](Viewing-ToolController.md).

## [getSnapResult()](#getsnapresult)

### Returns

| type | description |
| --- | --- |
| [SnapResult](MeasureCommon-SnapResult.md) | The snapping status of the last pointer event performed. |

## [isSnapped()](#issnapped)

Checks whether the toolâs last update resulted on a snap.

### Returns

| type | description |
| --- | --- |
| boolean | true when the last pointer event got snapped. |

## [snapping3D(result)](#snapping3d-result)

3D Snapping

### Parameters

| result* | Result of Hit Test. |
| --- | --- |

* Required

## [extractLineGeometry(edge, geometry)](#extractlinegeometry-edge-geometry)

Get Edge geometry for the case that the hittest result contained a 3D lines. For this case, we have no Face3, so that faceSnapping and edgeSnapping donât work.

### Parameters

| edge*   Object | {a, b} with vertex indices a,b of lineStart/lineEnd vertex |
| --- | --- |
| geometry*   GeometryBuffer |  |

* Required

### Returns

| type | description |
| --- | --- |
| THREE.Geometry, THREE.BufferGeometry | Geometry with simple line |

## [faceIsCurved(face)](#faceiscurved-face)

Checks if the given geometry is curved

### Parameters

| face*   THREE.BufferGeometry | The geometry |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the any of the faces composing the geometry is curved |

## [snapping2D(hitResult, options)](#snapping2d-hitresult-options)

Snap to a 2D model.

### Parameters

Expand all

| hitResult*   object | a result of a ray intersection. |
| --- | --- |
| options   object | Options object. |
| enumSegments   function | Enumerates all segments within a given bbox in model-space. |

* Required
