# Settings

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/globals/TypeDefs/Settings/

---

Type Definitions

# Settings

Object used to apply the preferences by a Profile

# Properties

| viewCube   boolean | Sets the visibility of the viewcube. |
| --- | --- |
| viewCubeCompass   boolean | Sets the visibility of the viewcube compass. The compass will only be displayed if model contains orientation data. |
| viewType   number | Sets the view to default (0), orthographic (1), perspective (2) or perspective with ortho faces (3). |
| alwaysUsePivot   boolean | Orbit controls always orbit around the currently set pivot point. |
| zoomTowardsPivot   boolean | default direction for camera dolly (zoom) operations to be towards the camera pivot point. |
| reverseHorizontalLookDirection   boolean | Sets a view navigation option to reverse the default direction for horizontal look operations. |
| reverseVerticalLookDirection   boolean | Sets a view navigation option to reverse the default direction for vertical look operations. |
| orbitPastWorldPoles   boolean | Set a view navigation option to allow the orbit controls to move the camera beyond the north and south poles (world up/down direction). |
| clickToSetCOI   boolean | Modify the default click behavior for the viewer. |
| ghosting   boolean | Toggles ghosting during search and isolate. |
| optimizeNavigation   boolean | Toggles whether the navigation should be optimized for performance. |
| ambientShadows   boolean | Enables or disables ambient shadows. |
| antialiasing   boolean | Enables or disables antialiasing. |
| groundShadow   boolean | Toggles ground shadow. |
| groundReflection   boolean | Toggles ground reflection. |
| lineRendering   boolean | Hides all lines in the scene. |
| edgeRendering   boolean | Turns edge topology display on/off (where available). |
| lightPreset   number, string | Sets the Light Presets (Environments) for the Viewer. |
| envMapBackground   boolean | Toggles environment map for background. |
| bimWalkToolPopup   boolean | Toggles the bimwalk tool popup. |
| grayscale   boolean | Overrides line colors in 2D models to render in shades of gray. |
| swapBlackAndWhite   boolean | Will switch to white lines on a black background. |
| progressiveRendering   boolean | Toggles whether progressive rendering is used. |
| openPropertiesOnSelect   boolean | Open property panel when selecting an object (Only for GuiViewer3D). |
| pointRendering   boolean | Hides all points in the scene. |
| backgroundColorPreset   <br> | Sets a color to the background. |
| reverseMouseZoomDir   boolean | Reverse the default direction for camera dolly (zoom) operations. |
| leftHandedMouseSetup   boolean | Reverse mouse buttons from their default assignment (i.e. Left mouse operation becomes right mouse and vice versa). |
| fusionOrbit   boolean | Sets the orbit to fusion orbit. |
| fusionOrbitConstrained   boolean | Sets the the orbit to the contrained fusion orbit. |
| wheelSetsPivot   boolean | Sets wheel-zoom action to automatically reset the orbit pivot to the location under the cursor. |
| selectionSetsPivot   boolean | Sets selection / un-selection action to automatically reset the orbit pivot to be the center of the multiple selection. |
| bimWalkNavigatorType   string | Sets the BimWalk tool navigator. |
| bimWalkGravity   boolean | Toggles the BimWalk toolâs gravity. |
| defaultNavigationTool3D   string | Sets which navigation tool will be used by the viewer. (ie: âextractor_definedâ \|\| âbimwalkâ) |
| explodeStrategy   string | Sets which algorithm is used when exploding a model. Supported values are âhierarchyâ (default) and âradialâ. Other values are treated as âradialâ. |
| loadingAnimation   boolean | Toggles loading animation for 2D Models. |
| forcePDFCalibration   boolean | Force PDF calibration before measuring. |
| forceLeafletCalibration   boolean | Force Leaflet calibration before measuring. |
| restoreMeasurements   boolean | When opening the measure tool restore any existing measurements that where created during the session. |
| forceDoubleSided   boolean | Force the render to use double sided materials. |
| keyMapCmd   boolean | Force mapping CMD key to Ctrl in Mac. |
| displaySectionHatches   boolean | Display the hatch pattern for planes in the section tool. This does not apply to the section box. |
| zoomDragSpeed   number | Sets a sensitivity of mouse movement with the zoom tool. |
| zoomScrollSpeed   number | Sets a sensitivity of the mouse scroll wheel when zooming. |
