# GeolocationExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/GeolocationExtension/

---

Autodesk.Viewing.Extensions

# GeolocationExtension

Provides functions for converting GPS coordinates in WGS-84 format { x: Longitude, y: Latitude, z: Height(m) } into Viewer scene coordinates, and back. Supports a single model loaded into the scene.

The extension id is: `Autodesk.Geolocation`

## [new GeolocationExtension(viewer, options)](#new-geolocationextension-viewer-options)

### Parameters

| viewer*   [Autodesk.Viewing.Viewer3D](/en/docs/viewer/v7/reference/Viewing/Viewer3D/) | The Viewer instance |
| --- | --- |
| options   object | Not used |

* Required

### Examples

```
viewer.loadExtension('Autodesk.Geolocation')

```

---

# Methods

## [activate()](#activate)

When active, the extension will detect clicks on the model and will place a marker on the model. A panel will be displayed containing vertices clicked on the model. Each point-entry will also contain GPS its associated GPS position.

## [deactivate()](#deactivate)

Stops detecting click events on the canvas and closes the Panel.

## [isActive()](#isactive)

Whether the extension is active. When the extension is active, click events will be processed and added into a Panel.

### Returns

| type | description |
| --- | --- |
| boolean | True if the extension is active. |

## [hasGeolocationData()](#hasgeolocationdata)

### Returns

| type | description |
| --- | --- |
| boolean | true when the model contains geolocation data. |

## [lmvToLonLat(lmvPoint)](#lmvtolonlat-lmvpoint)

Converts viewer coordinates (obtained with something like `viewer.clientToWorld()`) into { x: Longitude, y: Latitude, z: Height (meters) } in WGS-84 format.

### Parameters

| lmvPoint*   THREE.Vector3 | 3D point in the scene |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| THREE.Vector3 | GPS coordinate in WGS-84 format: { x: Longitude, y: Latitude, z: Height } |

## [lonLatToLmv(lonLat)](#lonlattolmv-lonlat)

Converts coordinates from { x: Longitude, y: Latitude, z: Height (meters) } in WGS-84 format into viewer scene coordinates.

### Parameters

| lonLat*   THREE.Vector3 | GPS coordinate in WGS-84 format: { x: Longitude, y: Latitude, z: Height } |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| THREE.Vector3 | 3D point in the scene |

## [openGoogleMaps(pointLL84)](#opengooglemaps-pointll84)

Returns a Google Maps URL with a PIN on the specified GPS location. When no argument is provided, the URL will use the Modelâs geolocation if available.

### Parameters

| pointLL84   THREE.Vector3 | GPS location in WGS-84 format: { x: Longitude, y: Latitude }. Height is ignored. |
| --- | --- |

## [getCurrentPositionLmv()](#getcurrentpositionlmv)

Returns a Promise that resolves with a position in Viewer-space coordinates based on the deviceâs real world GPS position.

### Returns

| type | description |
| --- | --- |
| Promise | that resolves with a THREE.Vector3 containing Viewer-space coordinates. It rejects if deviceâs real world GPS position is not available. |
