# FileLoader

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/FileLoader/

---

Autodesk.Viewing

# FileLoader

## [new FileLoader(viewer)](#new-fileloader-viewer)

Base class for file loaders.

It is highly recommended that file loaders use worker threads to perform the actual loading in order to keep the UI thread free. Once loading is complete, the loader should call viewer.impl.onLoadComplete(). During loading, the loader can use viewer.impl.signalProgress(int) to indicate how far along the process is.

To add geometry to the viewer, `viewer.impl.addMeshInstance(geometry, meshId, materialId, matrix)` should be used. Geometry must be THREE.BufferGeometry, meshId is a number, materialId is a string, and matrix is the THREE.Matrix4 transformation matrix to be applied to the geometry.

Remember to add draw calls to the BufferGeometry if the geometry has more than 65535 faces.

### Parameters

| viewer*   [Autodesk.Viewing.Viewer3D](Viewing-Viewer3D.md) | The viewer instance. |
| --- | --- |

* Required

# Methods

## [loadFile(url, options, onSuccess, onError)](#loadfile-url-options-onsuccess-onerror)

Initiates the loading of a file from the given URL.

This method must be overridden.

### Parameters

Expand all

| url*   string | The url for the file. |
| --- | --- |
| options   object | An optional dictionary of options. |
| ids   string | A list of object id to load. |
| sharedPropertyDbPath   string | Optional path to shared property database. |
| onSuccess   function | Callback function when the file begins loading successfully. Takes no arguments. |
| onError   function | Callback function when an error occurs. Passed an integer error code and a string description of the error. |

* Required

## [is3d()](#is3d)

Returns true only for a 3D models FileLoader implementation.
