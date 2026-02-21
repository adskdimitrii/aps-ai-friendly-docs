# ViewerPreferences

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Private/ViewerPreferences/

---

Autodesk.Viewing.Private

# ViewerPreferences

Viewer preferences.

extends Autodesk.Viewing.Private.Preferences

## [new ViewerPreferences(viewer, options)](#new-viewerpreferences-viewer-options)

### Parameters

Expand all

| viewer*   [Autodesk.Viewing.Viewer3D](/en/docs/viewer/v7/reference/Viewing/Viewer3D/) | Viewer instance. |
| --- | --- |
| options*   object | Contains configuration parameters used to do initializations. |
| localStorage   boolean | Whether values get stored and loaded back from localStorage. Defaults to `true`. |
| prefix   string | A string to prefix preference names in web storage. Defaults to `'Autodesk.Viewing.ViewerPreferences.'`. |

* Required
