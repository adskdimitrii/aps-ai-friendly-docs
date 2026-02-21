# ProfileSettings

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/ProfileSettings/

---

Autodesk.Viewing

# ProfileSettings

ProfileSettings are used to set the viewerâs profile.

To generate a profile from the supplied profile settings, please reference [Autodesk.Viewing.Profile](/en/docs/viewer/v7/reference/Viewing/Profile/). To set the viewerâs profile, use [viewer.setProfile(profile)](/en/docs/viewer/v7/reference/Viewing/Viewer3D/#setProfile/).

# Properties

| clone   function | This function is used to clone an existing ProfileSetting. |
| --- | --- |

# Constants

## [Default](#default)

Default profile settings. It uses the preferences described in [Autodesk.Viewing.DefaultSettings](/en/docs/viewer/v7/reference/Viewing#DefaultSettings/). The following preferences will be persisted: alwaysUsePivot, zoomTowardsPivot, reverseHorizontalLookDirection, reverseVerticalLookDirection, orbitPastWorldPoles, clickToSetCOI, ghosting, optimizeNavigation, ambientShadows, antialiasing, groundShadows, groundReflections, bimWalkToolPopup, swapBlackAndWhite, openPropertiesOnSelect, reverseMouseZoomDir, leftHandedMouseSetup, wheelSetsPivot

| type |
| --- |
| [ProfileSettings](/en/docs/viewer/v7/reference/globals/TypeDefs/ProfileSettings/) |

## [AEC](#aec)

AEC profile settings. It inherits the settings from [Autodesk.Viewing.ProfileSettings.Default](/en/docs/viewer/v7/reference/ProfileSettings#Default/). The following preferences differ from the Default settings: { edgeRendering: true, // on desktop, false on mobile. lightPreset: âBoardwalkâ, envMapBackground: true }

| type |
| --- |
| [ProfileSettings](/en/docs/viewer/v7/reference/globals/TypeDefs/ProfileSettings/) |

## [Fluent](#fluent)

Design Collaboration profile settings. Inherits the settings from [Autodesk.Viewing.ProfileSettings.AEC](/en/docs/viewer/v7/reference/ProfileSettings#AEC/). The following preferences differ from the AEC settings: { reverseMouseZoomDir: true, wheelSetsPivot: true, alwaysUsePivot: true, enableCustomOrbitToolCursor: false }

| type |
| --- |
| [ProfileSettings](/en/docs/viewer/v7/reference/globals/TypeDefs/ProfileSettings/) |

## [Navis](#navis)

Navisworks profile settings. Inherits the settings from [Autodesk.Viewing.ProfileSettings.AEC](/en/docs/viewer/v7/reference/ProfileSettings#AEC/). The following preferences differ from the AEC settings: { bimWalkToolPopup: false, bimWalkNavigatorType: âaecâ, defaultNavigationTool3D: âextractor_definedâ }

| type |
| --- |
| [ProfileSettings](/en/docs/viewer/v7/reference/globals/TypeDefs/ProfileSettings/) |
