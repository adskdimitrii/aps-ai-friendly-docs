# EventUtils

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/EventUtils/

---

Autodesk.Viewing

# EventUtils

Contains static utility functions for DOM and viewer events.

## [new EventUtils()](#new-eventutils)

# Methods

## [isRightClick(event)](#isrightclick-event)

### Parameters

| event*   DOMEvent | A browser-triggered event |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true when the event matches a secondary-button click. |

## [isMiddleClick(event)](#ismiddleclick-event)

### Parameters

| event*   DOMEvent | A browser-triggered event |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true when the event matches a middle-button mouse click. |

## [waitUntilTransitionEnded(viewer)](#waituntiltransitionended-viewer)

If thereâs no camera transition, return immediately. Otherwise, resolve when the camera transition is finished.

### Parameters

| viewer*   [Autodesk.Viewing.Viewer3D](Viewing-Viewer3D.md) |  |
| --- | --- |

* Required

## [waitUntilGeometryLoaded(viewer)](#waituntilgeometryloaded-viewer)

If geometry has been loaded, return immediately. Otherwise, resolve when the geometry loaded event is fired.

### Parameters

Expand all

| viewer*   [Autodesk.Viewing.Viewer3D](Viewing-Viewer3D.md) |  |
| --- | --- |
| Model | model - Default is viewer.model, if not provided |

* Required

## [waitUntilModelAdded(viewer)](#waituntilmodeladded-viewer)

If model has been already added, return immediately. Otherwise, resolve when the model is added.

### Parameters

Expand all

| viewer*   [Autodesk.Viewing.Viewer3D](Viewing-Viewer3D.md) |  |
| --- | --- |
| Model | model - Default is viewer.model, if not provided |

* Required
