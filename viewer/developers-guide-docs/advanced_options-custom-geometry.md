# Adding Custom Geometry

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/advanced_options/custom-geometry/

---

# Adding Custom Geometry

The Viewer lets you to add custom geometry into a scene by using the `viewer.overlay` api.

Use this feature to overlay more data to the loaded model. Every custom geometry
added into the overlay scene gets rendered on every frame, even when progressive rendering is on.

Frame rate declines when too many custom geometries are added into overlay scenes.

Custom geometry uses the main scene depth buffer for depth testing, allowing the custom geometry to appear within the loaded model.

Use the [SceneBuilder](advanced_options-scene-builder.md) API to add objects that can be rendered progressively.

## [Step 1: Create custom geometry](#step-1-create-custom-geometry)

The Viewer bundles version 71 of [three.js](https://threejs.org) library and exposes its functionality through the global variable `THREE`.
Let’s use it to create a red sphere.

```
var geom = new THREE.SphereGeometry(10, 8, 8);
var material = new THREE.MeshBasicMaterial({ color: 0xff0000 });
var sphereMesh = new THREE.Mesh(geom, material);
sphereMesh.position.set(1, 2, 3);

```

## [Step 2: Create overlay scene](#step-2-create-overlay-scene)

Custom geometry must be added to an overlay scene. Multiple custom geometries can coexist in the same scene.
Scenes are created and identified by name. Be sure to choose a name that won’t conflict with scenes created by the Viewer.

```
if (!viewer.overlays.hasScene('custom-scene')) {
    viewer.overlays.addScene('custom-scene');
}

```

## [Step 3: Add custom geometry to overlay scene](#step-3-add-custom-geometry-to-overlay-scene)

Custom geometry must be added into specific overlay scenes. In this example we are adding custom geometry `sphereMesh` into the scene named `'custom-scene'`.

```
viewer.overlays.addMesh(sphereMesh, 'custom-scene');

```

## [Step 4: Remove custom geometry from overlay scene](#step-4-remove-custom-geometry-from-overlay-scene)

You can remove the custom geometry and overlay scenes with `removeMesh()` and `removeScene()`.

```
viewer.overlays.removeMesh(sphereMesh, 'custom-scene');
viewer.overlays.removeScene('custom-scene');

```

The viewer doesn’t dispose of the geometry or material used with custom geometry. The application developer can use the following to release the memory.

```
// Once the material and geometries are no longer used by any other
// meshes, they need to be disposed to avoid memory leaks.
material.dispose();
geom.dispose();

```

## [What’s next?](#what-s-next)

To view an interactive example, check out [Customizing Viewer Scene](interactive_examples-example_5.md).

For all available methods, see the [OverlayManager](../reference-docs/Viewing-OverlayManager.md) API documentation page.
