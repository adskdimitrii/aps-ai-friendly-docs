# Profile

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/Profile/

---

Autodesk.Viewing

# Profile

## [new Profile(profileSettings)](#new-profile-profilesettings)

Profiles encapsulate viewer settings, extensions to unload, and extensions to load.

The `profileSettings.settings` parameter will override the existing [preferences](Private-Preferences.md) upon calling the [apply](Viewing-Profile.md#apply/) method. The `profileSettings.extensions.load` and `profileSettings.extensions.unload` arrays are used to load and unload extensions. Make sure to set the profile by using the [Autodesk.Viewing.Viewer3D#setProfile](Viewing-Viewer3D.md#setProfile/) method.

### Parameters

| profileSettings*   [ProfileSettings](globals-TypeDefs-ProfileSettings.md) | the profile settings. |
| --- | --- |

* Required

### Examples

```
const profileSettings = {
 name: "mySettings",
 description: "My personal settings.",
 settings: {
     ambientShadows: false,
     groundShadows: true
 }
 persistent: ['ambientShadows'],
 extensions: {
     load: ["Autodesk.BimWalk"],   // Extensions to load
     unload: ["Autodesk.ViewCubeUi"]  // Extensions to unload and to not load
 }

```

Show More

};
const profile = new Autodesk.Viewing.Profile(profileSettings);

---

# Methods

## [apply(prefs, override)](#apply-prefs-override)

Applies the profileâs settings to the viewer preferences. To make the viewer react to the updated preferences please reference [Autodesk.Viewing.Viewer3D#setProfile](Viewing-Viewer3D.md#setProfile/).

### Parameters

| prefs*   [Autodesk.Viewing.Private.Preferences](Private-Preferences.md) | preferences instance. |
| --- | --- |
| override   boolean | Override all existing preferences with the profileâs preferences. |

* Required
