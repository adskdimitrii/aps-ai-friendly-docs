# ProfileManager

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/ProfileManager/

---

Autodesk.Viewing

# ProfileManager

The ProfileManager provides a mechanism for registering [profile settings](globals-TypeDefs-ProfileSettings.md) with a specific file type. Any of the registered profiles can be set by using [viewer.setProfile()](Viewing-Viewer3D.md#setProfile/).

## [new ProfileManager()](#new-profilemanager)

### Examples

```
const profileManager = new Autodesk.Viewing.ProfileManager();
// or
// const profileManger = viewer.profileManager;
const profileSettings = {
   name: "DWF",
   settings: {
       swapBlackAndWhite: true
   },
   // ...
}
// Registers the specified profile settings for dwf models.
profileManager.registerProfile('dwf', profileSettings);
const profile = profileManager.getProfile('dwf'); // others: 'default', 'nwc', 'nwd', 'rvt', 'ifc'
viewer.setProfile(profile);

```

Show More

---

# Methods

## [registerProfile(fileExt, profileSettings)](#registerprofile-fileext-profilesettings)

Registers a profile. The profile will be overridden if a profile was already registered with the ProfileManager.

### Parameters

| fileExt*   String | file extension to register the profile settings with. |
| --- | --- |
| profileSettings*   [ProfileSettings](globals-TypeDefs-ProfileSettings.md), [Autodesk.Viewing.Profile](Viewing-Profile.md) | profile settings object or profile instance to register |

* Required

## [unregisterProfile(fileExt)](#unregisterprofile-fileext)

Unregister the profile associated with a file type

### Parameters

| fileExt*   String | file type |
| --- | --- |

* Required

## [getProfileOrDefault(fileExt)](#getprofileordefault-fileext)

Returns a profile that is registered with the specific file type. If the file type is not registered, then the default profile is returned.

### Parameters

| fileExt*   String | file extension |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| [Autodesk.Viewing.Profile](Viewing-Profile.md) | Profile associated with the file extension. |
