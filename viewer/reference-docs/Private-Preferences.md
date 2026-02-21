# Preferences

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Private/Preferences/

---

Autodesk.Viewing.Private

# Preferences

Application preferences.

Optionally uses web storage.

Each preference value can have tags associated to them. Developer supported tags are:

- âignore-producerâ
- âno-storageâ
- âshared-storageâ
- â2dâ
- â3dâ

Use tag âignore-producerâ in extensions to avoid having developer-defined render settings overridden by the loaded file.

Use tag âno-storageâ in extensions to avoid having User Preferences (from Settings Panel) override default or developer-defined preferences. Useful for render settings.

Use tag âshared-storageâ to always store the preference in a shared storage instead of the current profile storage. This is useful for preferences that should be shared across different storage profiles.

Preferences may apply to all model types, only 2D models (with tag â2dâ) or 3D models only (with tag â3dâ).

## [new Preferences(options)](#new-preferences-options)

### Parameters

Expand all

| options*   object | Contains configuration parameters used to do initializations. |
| --- | --- |
| localStorage   boolean | Whether values get stored and loaded back from localStorage. Defaults to `true`. |
| prefix   string | A string to prefix preference names in web storage. Defaults to `'Autodesk.Viewing.Preferences.'`. |

* Required
