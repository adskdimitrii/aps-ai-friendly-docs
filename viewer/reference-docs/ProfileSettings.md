# ProfileSettings

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/ProfileSettings/

---

Autodesk.Viewing

# ProfileSettings

ProfileSettings are used to set the viewer’s profile.

To generate a profile from the supplied profile settings, please reference [Autodesk.Viewing.Profile](Viewing-Profile.md). To set the viewer’s profile, use [viewer.setProfile(profile)](Viewing-Viewer3D.md#setProfile/).

# Properties

| clone   function | This function is used to clone an existing ProfileSetting. |
| --- | --- |

# Constants

## [Default](#default)

Default profile settings. It uses the preferences described in [Autodesk.Viewing.DefaultSettings](https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/#DefaultSettings/). The following preferences will be persisted: alwaysUsePivot, zoomTowardsPivot, reverseHorizontalLookDirection, reverseVerticalLookDirection, orbitPastWorldPoles, clickToSetCOI, ghosting, optimizeNavigation, ambientShadows, antialiasing, groundShadows, groundReflections, bimWalkToolPopup, swapBlackAndWhite, openPropertiesOnSelect, reverseMouseZoomDir, leftHandedMouseSetup, wheelSetsPivot

| type |
| --- |
| [ProfileSettings](globals-TypeDefs-ProfileSettings.md) |

## [AEC](#aec)

AEC profile settings. It inherits the settings from [Autodesk.Viewing.ProfileSettings.Default](ProfileSettings.md#Default/). The following preferences differ from the Default settings: { edgeRendering: true, // on desktop, false on mobile. lightPreset: ‘Boardwalk’, envMapBackground: true }

| type |
| --- |
| [ProfileSettings](globals-TypeDefs-ProfileSettings.md) |

## [Fluent](#fluent)

Design Collaboration profile settings. Inherits the settings from [Autodesk.Viewing.ProfileSettings.AEC](ProfileSettings.md#AEC/). The following preferences differ from the AEC settings: { reverseMouseZoomDir: true, wheelSetsPivot: true, alwaysUsePivot: true, enableCustomOrbitToolCursor: false }

| type |
| --- |
| [ProfileSettings](globals-TypeDefs-ProfileSettings.md) |

## [Navis](#navis)

Navisworks profile settings. Inherits the settings from [Autodesk.Viewing.ProfileSettings.AEC](ProfileSettings.md#AEC/). The following preferences differ from the AEC settings: { bimWalkToolPopup: false, bimWalkNavigatorType: ‘aec’, defaultNavigationTool3D: ‘extractor_defined’ }

| type |
| --- |
| [ProfileSettings](globals-TypeDefs-ProfileSettings.md) |
