# NPR

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/NPR/

---

Autodesk.Viewing.Extensions

# NPR

## [new NPR(viewer, options)](#new-npr-viewer-options)

Provides UI controls for NPR settings

The extension id is: `Autodesk.NPR`

### Parameters

| viewer*   [Autodesk.Viewing.Viewer3D](Viewing-Viewer3D.md) | Viewer instance. |
| --- | --- |
| options*   Object | Not used. |

* Required

### Examples

```
viewer.loadExtension('Autodesk.NPR');

```

---

# Methods

## [onToolbarCreated()](#ontoolbarcreated)

Invoked by the viewer when the toolbar UI is available. Adds a button to the Settings panel.

## [openPanel()](#openpanel)

Opens the NPR Render Options panel.

## [setParameter(param, value)](#setparameter-param-value)

Changes post-processing setting parameters. The supported param/value combinations are:

- “style”: either “edging”, “cel”, “graphite”, “pencil” or `null` to turn post-processing off.
- “edges”: `boolean`
- “idEdges”: `boolean`
- “normalEdges”: `boolean`
- “depthEdges”: `boolean`
- “brightness”: `Number`
- “contrast”: `Number`
- “grayscale”: `boolean`
- “preserveColor”: `boolean`
- “levels”: `Number`
- “repeats”: `Number`
- “rotation”: `Number` between 0 and 1, around circle (e.g. 0.5 == pi radians, 1.0 == 2*pi)

Fires event [RENDER_OPTION_CHANGED_EVENT](https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/#render-option-changed-event/).

### Parameters

| param*   string | Either “style”, “edges”, “idEdges”, “normalEdges”, “depthEdges”, “brightness”, “contrast”, “grayscale”, “preserveColor”, “levels”, “repeats” or “rotation”. |
| --- | --- |
| value*   <br> | type depends on the specified `param`. |

* Required
