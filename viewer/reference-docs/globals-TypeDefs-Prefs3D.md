# Prefs3D

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/globals/TypeDefs/Prefs3D/

---

Type Definitions

# Prefs3D

Contains viewer setting preference names for 3D models.

# Properties

| VIEW_CUBE   string | Sets the visibility of the viewcube. |
| --- | --- |
| VIEW_CUBE_COMPASS   string | Sets the visibility of the viewcube compass. The compass will only be displayed if model contains orientation data. |
| VIEW_TYPE   string | Sets the view to orthographic or perspective. |
| ALWAYS_USE_PIVOT   string | Orbit controls always orbit around the currently set pivot point. |
| ZOOM_TOWARDS_PIVOT   string | Default direction for camera dolly (zoom) operations to be towards the camera pivot point. |
| SELECTION_SETS_PIVOT   string | Sets selection / un-selection action to automatically reset the orbit pivot to be the center of the multiple selection. |
| REVERSE_HORIZONTAL_LOOK_DIRECTION   string | Sets a view navigation option to reverse the default direction for horizontal look operations. |
| REVERSE_VERTICAL_LOOK_DIRECTION   string | Sets a view navigation option to reverse the default direction for vertical look operations. |
| ORBIT_PAST_WORLD_POLES   string | Set a view navigation option to allow the orbit controls to move the camera beyond the north and south poles (world up/down direction). |
| CLICK_TO_SET_COI   string | Modify the default click behavior for the viewer. |
| GHOSTING   string | Toggles ghosting during search and isolate. |
| OPTIMIZE_NAVIGATION   string | Toggles whether the navigation should be optimized for performance. |
| AMBIENT_SHADOWS   string | Enables or disables ambient shadows. |
| ANTIALIASING   string | Enables or disables antialiasing. |
| GROUND_SHADOW   string | Toggles ground shadow. |
| GROUND_REFLECTION   string | Toggles ground reflection. |
| LINE_RENDERING   string | Hides all lines in the scene. |
| EDGE_RENDERING   string | Turns edge topology display on/off (where available). |
| LIGHT_PRESET   string | Sets the Light Presets (Environments) for the Viewer. |
| ENV_MAP_BACKGROUND   string | Toggles environment map for background. |
| BIM_WALK_TOOL_POPUP   string | Toggles the bimwalk tool popup. |
| BIM_WALK_NAVIGATOR_TYPE   string | Identifier for the bimWalkNavigatorType preference. This is used to set the BimWalk tool navigator. |
| BIM_WALK_GRAVITY   string | Identifier for the bimWalkGravity preference. This is used to toggle the BimWalk tool’s gravity. |
| DEFAULT_NAVIGATION_TOOL_3D   string | identifier for the toolToUse preference. This is used to set which navigation tool will be used. |
| SELECTION_MODE   string | identifier for the selectionMode preference. This is used to set which selection mode (Leaf, First, Last object) wil be used by the viewer. |
| ENABLE_CUSTOM_ORBIT_TOOL_CURSOR   string | identifier for whether the OrbitDollyPanTool will customize the cursor visuals. |
| EXPLODE_STRATEGY   string | Specifies which algorithm is used when exploding the model. Supported values are ‘hierarchy’ (default) and ‘radial’. Other values are treated as ‘radial’. |
| FORCE_DOUBLE_SIDED   string | Forces the viewer to render materials as double sided. Otherwise it uses the model specified value. |
| GPU_MEMORY_LIMIT   string | Sets the maximum amount of GPU memory that can be used by the viewer. (WEBGPU only) |
