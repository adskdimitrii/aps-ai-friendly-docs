# Preferences

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Private/Preferences/

---

Autodesk.Viewing.Private

# Preferences

Application preferences.

Optionally uses web storage.

Each preference value can have tags associated to them. Developer supported tags are:

- ‘ignore-producer’
- ‘no-storage’
- ‘shared-storage’
- ‘2d’
- ‘3d’

Use tag ‘ignore-producer’ in extensions to avoid having developer-defined render settings overridden by the loaded file.

Use tag ‘no-storage’ in extensions to avoid having User Preferences (from Settings Panel) override default or developer-defined preferences. Useful for render settings.

Use tag ‘shared-storage’ to always store the preference in a shared storage instead of the current profile storage. This is useful for preferences that should be shared across different storage profiles.

Preferences may apply to all model types, only 2D models (with tag ‘2d’) or 3D models only (with tag ‘3d’).

## [new Preferences(options)](#new-preferences-options)

### Parameters

Expand all

| options*   object | Contains configuration parameters used to do initializations. |
| --- | --- |
| localStorage   boolean | Whether values get stored and loaded back from localStorage. Defaults to `true`. |
| prefix   string | A string to prefix preference names in web storage. Defaults to `'Autodesk.Viewing.Preferences.'`. |

* Required
