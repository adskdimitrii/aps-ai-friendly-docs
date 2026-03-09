# SectionExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/SectionExtension/

---

Autodesk.Viewing.Extensions

# SectionExtension

## [new SectionExtension(viewer, options)](#new-sectionextension-viewer-options)

The SectionExtension provides ways to cut the geometry using planes or a cube. The extension adds a toolbar button to access the feature.

The extension id is: `Autodesk.Section`

### Parameters

| viewer*   [Viewer3D](Viewing-Viewer3D.md) | Viewer instance |
| --- | --- |
| options*   object | Configurations for the extension |

* Required

### Examples

```
viewer.loadExtension('Autodesk.Section')

```

---

# Methods

## [toggle()](#toggle)

Toggles activeness of section planes.

### Returns

| type | description |
| --- | --- |
| boolean | Whether the section plane is active or not. |

## [getSectionStyle()](#getsectionstyle)

Returns the current type of plane that will cut-though the geometry.

### Returns

| type | description |
| --- | --- |
| null, string | Either âXâ or âYâ or âZâ or âBOXâ or null. |

## [setSectionStyle(style, preserveSection)](#setsectionstyle-style-preservesection)

Sets the Section plane style.

### Parameters

| style*   string | Accepted values are âXâ, âYâ, âZâ and âBOXâ (in Caps) |
| --- | --- |
| preserveSection   boolean | Whether sending the current style value resets the cut planes. |

* Required

## [getState(viewerState)](#getstate-viewerstate)

Gets the extension state as a plain object. Invoked automatically by viewer.getState()

### Parameters

| viewerState*   object | Object to inject extension values. |
| --- | --- |

* Required

## [restoreState(viewerState)](#restorestate-viewerstate)

Restores the extension state from a given object. Invoked automatically by viewer.restoreState()

### Parameters

| viewerState*   object | Viewer state. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if restore operation was successful. |

## [setSectionBox(box)](#setsectionbox-box)

Set a section box around the passed in THREE.Box3. This method will also enable the section tool.

### Parameters

| box*   THREE.Box3 | used to set the section box. |
| --- | --- |

* Required

## [setSectionPlane(normal, point, enableRotationGizmo)](#setsectionplane-normal-point-enablerotationgizmo)

Place a section plane on the Intersection. This method will also enable the section tool.

### Parameters

| normal*   THREE.Vector3 | plane normal. |
| --- | --- |
| point*   THREE.Vector3 | position to place the plane. |
| enableRotationGizmo* |  |

* Required

## [activate(mode)](#activate-mode)

Activates a section plane for user to interact with. It performs the same action as the UI button.

### Parameters

| mode*   string | Accepted values are âxâ, âyâ, âzâ and âboxâ (in lowercase) |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true if the activation was successful. |

## [deactivate(keepCutPlanes)](#deactivate-keepcutplanes)

Removes the section plane/box from the 3D canvas.

### Parameters

| keepCutPlanes* | keep existing cut planes when deactivating the tool. Default is false. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | returns true if deactivated, false otherwise. |
