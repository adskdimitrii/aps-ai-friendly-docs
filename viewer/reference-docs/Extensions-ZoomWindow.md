# ZoomWindow

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/ZoomWindow/

---

Autodesk.Viewing.Extensions

# ZoomWindow

Extends the dolly (zoom) button on the toolbar with a tool for end users to specify a rectangular section for the camera to zoom into and adjust accordingly.

The extension id is: `Autodesk.Viewing.ZoomWindow`

## [new ZoomWindow()](#new-zoomwindow)

### Examples

```
viewer.loadExtension('Autodesk.Viewing.ZoomWindow')

```

---

# Methods

## [activate(mode)](#activate-mode)

Activates either ZoomWindow or dolly/zoom tool.

### Parameters

| mode   string | Either ‘zoomwindow’ or ‘dolly’ |
| --- | --- |

## [deactivate()](#deactivate)

Deactivates the tool and resets the navigation tool.
