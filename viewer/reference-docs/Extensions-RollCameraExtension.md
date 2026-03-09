# RollCameraExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/RollCameraExtension/

---

Autodesk.Viewing.Extensions

# RollCameraExtension

Provides UI controls to perform rotation of camera view.

The extension id is: `Autodesk.BIM360.RollCamera`

## [new RollCameraExtension()](#new-rollcameraextension)

### Examples

```
viewer.loadExtension('Autodesk.BIM360.RollCamera')

```

---

# Methods

## [load()](#load)

Load the roll camera extension.

## [unload()](#unload)

Unload the roll camera extension.

## [onToolbarCreated(toolbar)](#ontoolbarcreated-toolbar)

Invoked by the viewer when the toolbar UI is available.

### Parameters

| toolbar*   [Autodesk.Viewing.UI.ToolBar](UI-ToolBar.md) | toolbar instance. |
| --- | --- |

* Required

## [roll(clockwise)](#roll-clockwise)

Roll the camera 90 degrees.

### Parameters

| clockwise*   boolean | True to rotate clockwise, false to rotate counter clockwise. |
| --- | --- |

* Required
