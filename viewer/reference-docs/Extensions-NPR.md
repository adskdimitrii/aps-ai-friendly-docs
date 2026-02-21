# NPR

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/NPR/

---

Autodesk.Viewing.Extensions

# NPR

## [new NPR(viewer, options)](#new-npr-viewer-options)

Provides UI controls for NPR settings

The extension id is: `Autodesk.NPR`

### Parameters

| viewer*   [Autodesk.Viewing.Viewer3D](/en/docs/viewer/v7/reference/Viewing/Viewer3D/) | Viewer instance. |
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

- âstyleâ: either âedgingâ, âcelâ, âgraphiteâ, âpencilâ or `null` to turn post-processing off.
- âedgesâ: `boolean`
- âidEdgesâ: `boolean`
- ânormalEdgesâ: `boolean`
- âdepthEdgesâ: `boolean`
- âbrightnessâ: `Number`
- âcontrastâ: `Number`
- âgrayscaleâ: `boolean`
- âpreserveColorâ: `boolean`
- âlevelsâ: `Number`
- ârepeatsâ: `Number`
- ârotationâ: `Number` between 0 and 1, around circle (e.g. 0.5 == pi radians, 1.0 == 2*pi)

Fires event [RENDER_OPTION_CHANGED_EVENT](/en/docs/viewer/v7/reference/Viewing/#render-option-changed-event/).

### Parameters

| param*   string | Either âstyleâ, âedgesâ, âidEdgesâ, ânormalEdgesâ, âdepthEdgesâ, âbrightnessâ, âcontrastâ, âgrayscaleâ, âpreserveColorâ, âlevelsâ, ârepeatsâ or ârotationâ. |
| --- | --- |
| value*   <br> | type depends on the specified `param`. |

* Required
