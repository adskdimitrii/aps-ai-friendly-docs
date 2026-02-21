# ViewingUtilities

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/ViewingUtilities/

---

Autodesk.Viewing

# ViewingUtilities

## [new ViewingUtilities(viewerImplIn, autocam, navapi)](#new-viewingutilities-viewerimplin-autocam-navapi)

Variety of utilities convenient to navigation and tool development.

This class is instantiated internally and made available to all registered interaction tools via their âutilitiesâ property.

### Parameters

| viewerImplIn*   object | The viewer implementation object. |
| --- | --- |
| autocam*   object | The Autocam interface object. |
| navapi*   object | The Navigation interface object. |

* Required

# Methods

## [transitionView(pos, coi, fov, up, worldUp, reorient, pivot)](#transitionview-pos-coi-fov-up-worldup-reorient-pivot)

This method triggers a camera view transition as specified by the parameters.

### Parameters

| pos*   THREE.Vector3 | The new world space position of the camera. |
| --- | --- |
| coi*   THREE.Vector3 | The new center of interest (look at point). |
| fov*   number | The new field of view for the camera in degrees. |
| up*   THREE.Vector3 | The new camera up direction. |
| worldUp*   THREE.Vector3 | The new world up direction. |
| reorient*   boolean | If true the given camera up parameter is ignored and a new up direction will be calculated to be aligned with the given world up direction. |
| pivot*   THREE.Vector3 | The new pivot point. |

* Required

## [goHome()](#gohome)

This method triggers a camera view transition to the registered home view for the current scene.

## [getHitPoint(x, y)](#gethitpoint-x-y)

This method performs a hit test with the current model using a ray cast from the given screen coordinates.

### Parameters

| x*   number | The normalized screen x coordinate in [0, 1]. |
| --- | --- |
| y*   number | The normalized screen y coordinate in [0, 1]. |

* Required

### Returns

| type | description |
| --- | --- |
| THREE.Vector3 | The world space hit position or null if no object was hit. |

## [activatePivot(fadeIt)](#activatepivot-fadeit)

This method activates the in scene pivot indicator. The pivot is positioned at the current cameraâs pivot point.

### Parameters

| fadeIt*   boolean | If true the indicator will be displayed and then fade away after a short period. |
| --- | --- |

* Required

## [pivotActive(state, fadeIt)](#pivotactive-state-fadeit)

This method changes the display state of the in scene pivot indicator. If the current scene is 2D this method has no effect.

### Parameters

| state*   boolean | The requested display state for the indicator. |
| --- | --- |
| fadeIt*   boolean | If true and âstateâ is also true, the indicator will be displayed and then fade away after a short period. |

* Required

## [pivotUpdate()](#pivotupdate)

Invoke this method to refresh the pivot indicator and continue its fading action if required.

## [setPivotPoint(newPivot, preserveView, isset)](#setpivotpoint-newpivot-preserveview-isset)

Set the current pivot point and pivot set flag. If the pivot indicator is active its position will be updated accordingly. If a temporary pivot was previously applied, its saved state will be cleared.

### Parameters

| newPivot*   THREE.Vector3 | The world space position of the new pivot point. |
| --- | --- |
| preserveView*   boolean | If false the cameraâs view direction will change to look at the new pivot point. If true the cameraâs view will not be changed. |
| isset*   boolean | The new state of the pivot set flag. |

* Required

## [savePivot(name)](#savepivot-name)

Save a copy of the current pivot point and pivot set flag.

### Parameters

| name*   string | Optional unique name of the saved location. |
| --- | --- |

* Required

## [restorePivot(name)](#restorepivot-name)

Restore the saved copy of the current pivot point and pivot set flag. Once restored the saved value is erased.

### Parameters

| name*   string | Optional unique name of the saved location. |
| --- | --- |

* Required

## [setTemporaryPivot(newPivot)](#settemporarypivot-newpivot)

Allows the caller to save the current pivot and replace it with a new location. If while the temporary pivot is active a new pivot is set via the setPivotPoint method, the saved pivot will be cleared to avoid restoring an out of date pivot location.

### Parameters

| newPivot*   THREE.Vector3 | The new pivot to be assigned or null to clear any previously saved pivot. |
| --- | --- |

* Required

## [removeTemporaryPivot()](#removetemporarypivot)

Restore a pivot value that was saved by a call to setTemporary Pivot.

## [setPivotSize(scale)](#setpivotsize-scale)

Changes the pivot graphic size.

### Parameters

| scale*   number | Default size value is 1 |
| --- | --- |

* Required

## [setPivotColor(color, opacity)](#setpivotcolor-color-opacity)

Change pivot color and opacity. Example, to get red 100% solid (non-transparent) use setPivotColor(0xFF0000, 1)

### Parameters

| color*   number | RBG Hex color. |
| --- | --- |
| opacity   number | Opacity value from 0 (transparent) to 1 (opaque). |

* Required

## [getBoundingBox(ignoreSelection)](#getboundingbox-ignoreselection)

Return the bounding box of the current model or model selection.

### Parameters

| ignoreSelection*   boolean | If true the current selection is ignored and the model bounds is returned. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| THREE.Box3 |  |

## [fitToView(immediate)](#fittoview-immediate)

Request a camera transition to fit the current model or model selection into the view frustum.

### Parameters

| immediate*   boolean | If true the transition will be immediate, otherwise animated over a short time period. |
| --- | --- |

* Required
