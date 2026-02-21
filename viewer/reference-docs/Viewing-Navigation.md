# Navigation

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/Navigation/

---

Autodesk.Viewing

# Navigation

## [new Navigation(camera)](#new-navigation-camera)

This is the core interface to camera controls and navigation. The active navigation object can normally be obtained from the ânavigationâ property of the Viewer3D instance. Client implementations should not normally instantiate this class directly.

### Parameters

| camera*   THREE.Camera | The main camera object used to render the scene. |
| --- | --- |

* Required

# Methods

## [setCamera(camera)](#setcamera-camera)

Set or unset the current camera used for navigation. Normally set via the constructor. The camera should be of type Autodesk.Viewing.UnifiedCamera.

### Parameters

| camera*   Autodesk.Viewing.UnifiedCamera | the current camera object. |
| --- | --- |

* Required

## [getCamera()](#getcamera)

### Returns

| type | description |
| --- | --- |
| THREE.Camera | the current camera object. |

## [setScreenViewport(viewport)](#setscreenviewport-viewport)

Set the current canvas viewport in screen coordinates. Invoked internally on canvas resize.

### Parameters

| viewport*   object | Rectangle with properties left, top, width, height. |
| --- | --- |

* Required

## [getScreenViewport()](#getscreenviewport)

Get the current canvas viewport in screen coordinates.

### Returns

| type | description |
| --- | --- |
| object | with properties left, top, width, height. |

## [setView(from, to, up)](#setview-from-to-up)

Sets the current view to the given LookAt, while keeping other camera properties as is. Jumps to the new location, without camera path animation.

### Parameters

| from*   THREE.Vector3 | The desired camera position in world space. |
| --- | --- |
| to*   THREE.Vector3 | The desired camera target in world space. |
| up   THREE.Vector3 | The desired camera up direction in world space. |

* Required

## [orientCameraUp(force)](#orientcameraup-force)

Orient the cameraâs up direction with the current world up direction

### Parameters

| force*   boolean | if true, will orient camera up direction regardless of navigation lock |
| --- | --- |

* Required

## [getPivotPoint()](#getpivotpoint)

### Returns

| type | description |
| --- | --- |
| THREE.Vector3 | the world space position of the pivot point for orbit navigation. |

## [setPivotPoint(pivot)](#setpivotpoint-pivot)

Sets the Vector3 world space position of the pivot point for orbit navigation.

### Parameters

| pivot*   THREE.Vector3 | the new pivot position. |
| --- | --- |

* Required

## [getPosition()](#getposition)

### Returns

| type | description |
| --- | --- |
| THREE.Vector3 | the world space position of the camera. |

## [setPosition(pos)](#setposition-pos)

Sets the Vector3 world space position of camera.

### Parameters

| pos*   THREE.Vector3 | the new camera position. |
| --- | --- |

* Required

## [setTarget(target)](#settarget-target)

Sets the Vector3 world space position towards which the camera should be pointing.

### Parameters

| target*   THREE.Vector3 | the new camera look at point. |
| --- | --- |

* Required

## [getTarget()](#gettarget)

### Returns

| type | description |
| --- | --- |
| THREE.Vector3 | the world space position towards which the camera is pointing. |

## [getEyeVector()](#geteyevector)

Get the current camera view vector. This vector is not normalized and its length is the distance between the camera position and the camera look at point.

### Returns

| type | description |
| --- | --- |
| THREE.Vector3 | the current camera view vector in world space. |

## [getEyeToCenterOfBoundsVec(bounds)](#geteyetocenterofboundsvec-bounds)

Get a vector from the camera location to the center of the input bounding box.

### Parameters

| bounds*   THREE.Box3 | Bounding box. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| THREE.Vector3 | The vector from the camera location to the center of the input bounds. |

## [getFovMin()](#getfovmin)

### Returns

| type | description |
| --- | --- |
| number | the minimum allowed vertical field of view in degrees. |

## [getFovMax()](#getfovmax)

### Returns

| type | description |
| --- | --- |
| number | the maximum allowed vertical field of view in degrees. |

## [setZoomInLimitFactor(factor)](#setzoominlimitfactor-factor)

Limits zoom in to show 1/factor-th of the entire 2D page. Applies only on 2D vectorized models.

### Parameters

| factor*   number |  |
| --- | --- |

* Required

## [getZoomInLimitFactor()](#getzoominlimitfactor)

### Returns

| type | description |
| --- | --- |
| number | the current limit when zooming into 2D vectorized models. |

## [setZoomOutLimitFactor(factor)](#setzoomoutlimitfactor-factor)

Limits zoom out to a multiplier of the modelâs bounding box dimensions. Applies only on 2D vectorized models.

### Parameters

| factor*   number |  |
| --- | --- |

* Required

## [getZoomOutLimitFactor()](#getzoomoutlimitfactor)

### Returns

| type | description |
| --- | --- |
| number | the current limit when zooming out 2D vectorized models. |

## [isPointVisible(point)](#ispointvisible-point)

Returns true if the point is visible.

### Parameters

| point*   THREE.Vector3 | The point in world coordinates. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the point is within the cameraâs frustum. |

## [setVerticalFov(fov, adjustPosition)](#setverticalfov-fov-adjustposition)

Set the current vertical field of view.

### Parameters

| fov*   number | the new field of view in degrees (value is clamped to the minimum and maximum field of view values). |
| --- | --- |
| adjustPosition*   boolean | If true, the camera position will be modified to keep either the world space area of the view at the pivot point unchanged (if it is set and visible) or the world space area of view at the camera look at point unchanged. |

* Required

## [applyRotation(point, angle, pivot, viewVec)](#applyrotation-point-angle-pivot-viewvec)

Applies a rotation on a single point

### Parameters

| point*   THREE.Vector3 | Point to rotate |
| --- | --- |
| angle*   number | Angle of rotation (in radians) |
| pivot*   THREE.Vector3 | Pivot of rotation |
| viewVec*   THREE.Vector3 | Front vector |

* Required

## [getSignedAngle(v1, v2, viewVec)](#getsignedangle-v1-v2-viewvec)

Computes a signed angle between two vectors

### Parameters

| v1*   THREE.Vector3 | Vector #1 |
| --- | --- |
| v2*   THREE.Vector3 | Vector #2 |
| viewVec*   THREE.Vector3 | Front vector |

* Required

### Returns

| type | description |
| --- | --- |
| number | Signed angle between two vectors |

## [computeFit(oldpos, oldcoi, fov, bounds, aspect)](#computefit-oldpos-oldcoi-fov-bounds-aspect)

Compute camera position and look at point which will fit the given bounding box in the view frustum at the given field of view angle.

### Parameters

| oldpos*   THREE.Vector3 | existing camera position |
| --- | --- |
| oldcoi*   THREE.Vector3 | existing camera look at point |
| fov*   number | field of view (in degrees) to use for fit calculation in degrees |
| bounds*   THREE.Box3 | bounding box to fit |
| aspect*   number | optional aspect ratio of window, horizontal/vertical |

* Required

### Returns

| type | description |
| --- | --- |
| object | Object with properties âpositionâ and âtargetâ. |

## [computeOrthogonalUp(pos, coi)](#computeorthogonalup-pos-coi)

Compute a vector which is orthogonal to the given view and aligned with the world up direction.

### Parameters

| pos*   THREE.Vector3 | view position |
| --- | --- |
| coi*   THREE.Vector3 | center of interest (view look at point) |

* Required

### Returns

| type | description |
| --- | --- |
| THREE.Vector3 | up direction orthogonal to the given view |

## [fitBounds(immediate, bounds, reorient, force)](#fitbounds-immediate-bounds-reorient-force)

Causes the current camera position to be changed in order to fit the given bounds into the current view frustum.

### Parameters

| immediate*   boolean | if false the camera position will animate to the new location. |
| --- | --- |
| bounds*   THREE.Box3 | bounding box to fit |
| reorient*   boolean | if true the camera up direction will be reoriented with the world up. |
| force*   boolean | if true will perform regardless of gotoview enabled or not. |

* Required

### Returns

| type | description |
| --- | --- |
| object | Object with properties âpositionâ and âtargetâ. |

## [updateCamera()](#updatecamera)

Update the current camera projection matrix and orient the camera to the current look at point. Invoked internally prior to rendering a new frame with the current camera.

## [setConstraints2D(viewRegion, maxPixelPerUnit)](#setconstraints2d-viewregion-maxpixelperunit)

Applies zooming and panning restrictions when viewing 2D models. Invoke without parameters to clear any previous setting.

### Parameters

| viewRegion   THREE.Box3 | in world space. If specified, navigation is restricted so that this region always spans >= half of the screen extent in x and y. |
| --- | --- |
| maxPixelPerUnit   number | Restrict zoom-In, so that a single unit in world-space never exceeds maxPixelPerUnit on screen. |
