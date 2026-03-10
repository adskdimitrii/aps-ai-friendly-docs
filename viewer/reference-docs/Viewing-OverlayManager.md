# OverlayManager

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/OverlayManager/

---

Autodesk.Viewing

# OverlayManager

Provides a mechanism for adding custom meshes. These meshes are added into their own overlay scenes, which are always rendered after the main scene.

## [new OverlayManager()](#new-overlaymanager)

# Methods

## [addScene(name)](#addscene-name)

Creates a scene that is always rendered after the main scene. It is rendered into a separate buffer when each frame of the main scene is drawn. The buffer is then composited over the main scene. If it is enabled, the overlay scenes use the main scene depth buffer for the depth testing, to allow the overlay to appear in the main scene.

### Parameters

| name*   string | scene identifier |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true if the overlay was added or already exists, false otherwise |

## [removeScene(name)](#removescene-name)

Removes a scene along with all the meshes in it.

### Parameters

| name*   string | scene identifier |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true if the overlay was removed or if it doesn’t exist |

## [clearScene(name)](#clearscene-name)

Removes all meshes from a scene.

### Parameters

| name*   string | scene identifier |
| --- | --- |

* Required

## [hasScene(name)](#hasscene-name)

Checks whether a scene already exists

### Parameters

| name*   string | scene identifier |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true the scene exists |

## [addMesh(mesh, sceneName)](#addmesh-mesh-scenename)

Inserts one or more custom THREE.Mesh into an existing scene.

### Parameters

| mesh*   THREE.Mesh, Array | A mesh instance or an Array of them. |
| --- | --- |
| sceneName*   string | Name of an existing scene. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true if the mesh was added to the scene |

### Examples

```
// Create a new mesh
   const geometry = new THREE.SphereGeometry(10, 8, 8);
   const material = new THREE.MeshBasicMaterial({ color: 0x336699 });
   const mesh = new THREE.Mesh(geometry, material);
   mesh.position.x = 1.0; mesh.position.y = 2.0; mesh.position.z = 3.0;
   // Add scene and mesh
   addScene('my_scene');
   addMesh([mesh], 'my_scene');

```

Show More

---

## [removeMesh(mesh, sceneName)](#removemesh-mesh-scenename)

Removes one or more custom THREE.Mesh from an existing scene. Developers are responsible for disposing the material and geometry after the mesh is removed.

### Parameters

| mesh*   THREE.Mesh, Array | A mesh instance or an Array of them. |
| --- | --- |
| sceneName*   string | Name of the scene the mesh(es) belong to. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true if the mesh (or meshes) was removed. |

## [hasMesh(mesh, sceneName)](#hasmesh-mesh-scenename)

Checks whether a mesh is already part of a scene.

### Parameters

| mesh*   THREE.Mesh | The mesh instance. |
| --- | --- |
| sceneName*   string | Name of the scene to check against. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | true if the mesh belongs to the scene. |
