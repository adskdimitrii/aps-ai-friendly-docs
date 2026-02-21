# Intersection

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/globals/TypeDefs/Intersection/

---

Type Definitions

# Intersection

Object that is returned by the ray cast and hit test methods for each scene object under the given canvas coordinates.

# Properties

| dbId   number | Internal ID of the scene object. |
| --- | --- |
| distance   number | Distance of the intersection point from camera. All intersections returned by the ray casting method are sorted from the smallest distance to the largest. |
| face   THREE.Face3 | THREE.Face3 object representing the triangular mesh face that has been intersected. |
| faceIndex   number | Index of the intersected face, if available. |
| fragId   number | ID of Viewer SDK fragment that was intersected. |
| point   THREE.Vector3 | THREE.Vector3 point of intersection. |
| model   [Autodesk.Viewing.Model](/en/docs/viewer/v7/reference/Viewing/Model/) | Model instance the dbId belongs to. |
