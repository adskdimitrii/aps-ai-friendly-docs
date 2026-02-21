# ViewCubeUi

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/ViewCubeUi/

---

Autodesk.Viewing.Extensions

# ViewCubeUi

## [new ViewCubeUi(viewer, options)](#new-viewcubeui-viewer-options)

Create the UI for the view cube.

The extension id is: `Autodesk.ViewCubeUi`

### Parameters

| viewer*   [Autodesk.Viewing.Viewer3D](/en/docs/viewer/v7/reference/Viewing/Viewer3D/) | Viewer instance. |
| --- | --- |
| options*   object | Not used. |

* Required

### Examples

```
viewer.loadExtension('Autodesk.ViewCubeUi');

```

---

# Methods

## [setVisible(show)](#setvisible-show)

Show or hide the view cube element. This also applies to the home button.

### Parameters

| show*   boolean | If set to false, the view cube and the home button will become invisible. |
| --- | --- |

* Required

## [showTriad(show)](#showtriad-show)

Show the x,y,z axes of the view cube.

### Parameters

| show*   boolean | if set to true, the view cube axes will be shown. |
| --- | --- |

* Required

## [setViewCube(face)](#setviewcube-face)

Set the face of ViewCube and apply camera transformation according to it.

### Parameters

| face*   string | The face name of ViewCube. The name can contain multiple face names, the format should be `"[front/back], [top/bottom], [left/right]"`. |
| --- | --- |

* Required

### Examples

```
viewer.setViewCube('front top right');
 viewer.setViewCube('bottom left');
 viewer.setViewCube('back');

```

---

## [displayHomeButton(show)](#displayhomebutton-show)

Hides the Home button next to the ViewCube.

### Parameters

| show*   boolean |  |
| --- | --- |

* Required

## [displayViewCube(display, updatePrefs)](#displayviewcube-display-updateprefs)

Display the view cube. This will not effect the home button.

### Parameters

| display*   boolean | if set to false the view cube element will be invisible |
| --- | --- |
| updatePrefs*   boolean | update the view cube preference |

* Required

## [localize()](#localize)

Localize the view cube

## [refreshCube()](#refreshcube)

Refresh the view cube
