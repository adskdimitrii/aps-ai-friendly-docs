# ProfileSettings

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/globals/TypeDefs/ProfileSettings/

---

Type Definitions

# ProfileSettings

Object used for setting a viewer profile.

# Properties

| name   string | Name of the profile settings. |
| --- | --- |
| label   string | Optional. An end-user string to use instead of the name. |
| description   string | Optional. A description about the profile. |
| settings   [Settings](globals-TypeDefs-Settings.md) | Used by the Profile to apply to the viewer preferences. |
| persistent   Array.<String> | An array of setting ids to keep in localStorage. |
| sharedStorage   Array.<String> | An array of setting ids that share the persisted values across profiles. |
| extensions   [Extensions](globals-TypeDefs-Extensions.md) | Extensions that should or should not be loaded. |
