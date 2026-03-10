# Adding Custom Geometry with Scene Builder

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/advanced_options/scene-builder/

---

# Adding Custom Geometry with Scene Builder

Using the Scene Builder extension, you can create models and add your own objects to Viewer SDK. These objects are treated just like data from a downloaded model with a few restrictions:

- Only 3D objects are supported, including 3D lines and other geometry.
- Only THREE.BufferGeometry objects can be used.
- Lines are not rendered using THREE.Line objects. You must set the property `isLine: true` on the BufferGeometry.
- The same BufferGeometry can’t be used for lines and triangles.
- Similarly, use the BufferGeometry property `isPoint: true` to draw points.
- The model doesn’t have a property database. You can assign database ids and they can be used to collect multiple objects together, but there are no properties associated with the objects.
- The model is flat and doesn’t have an instance tree.
- The only materials that you can use with the Scene Builder are MeshPhong, MeshBasic, LineBasic and Prism.

The objects you add using the SceneBuilder render just like models that are downloaded. Unlike using overlays,
the framerate is not impacted when you add objects. However, it takes longer to fully render the model if you are rendering many objects. It should be noted that the spatial accelerator
hasn’t been implemented for the Scene Builder models.

In this tutorial, you will:

- Load the Scene Builder extension, which provides access to the ModelBuilder API.
- Use the ModelBuilder API to create custom models.
- Add custom geometry to your models.

## [Step 1: Loading the Extension](#step-1-loading-the-extension)

Like other extensions, the Scene Builder extension is loaded using [loadExtension](../reference-docs/Viewing-Viewer3D.md#loadextension-extensionid-options).

```
await viewer.loadExtension('Autodesk.Viewing.SceneBuilder');

```

Once the extension is loaded get the extension by using [getExtension](../reference-docs/Viewing-Viewer3D.md#getextension-extensionid-callback).

```
ext = viewer.getExtension('Autodesk.Viewing.SceneBuilder');

```

## [Step 2: Creating a Model](#step-2-creating-a-model)

After the extension is loaded, you must create a model to hold the objects that you want to display.
To do that, use the extension method [addNewModel](../reference-docs/Extensions-SceneBuilder.md#addnewmodel-options). This method creates the model and returns a [ModelBuilder](../reference-docs/Extensions-ModelBuilder.md) API you can use to update the model.

```
modelBuilder = await ext.addNewModel({
    conserveMemory: false,
    modelNameOverride: 'My Model Name'
});

```

Notice the two optional arguments to addNewModel, `conserveMemory` and `modelNameOverride`. This is the effect of the
arguments on the new model:

- conserveMemory: Changes the way LMV stores meshes. This defaults to false and setting it to true will cause lmv to conserve memory by sharing a single mesh object for all of the fragments in the model. If you set this to true, then the `addMesh()` method cannot be used to add fragments.
- modelNameOverride: Sets a name that you want to display in the model browser panel. If you don’t set this option LMV will generate a name - `Scene Builder Model n` - where n is the model id of the new model.

## [Step 3: Adding custom graphics to the model](#step-3-adding-custom-graphics-to-the-model)

LMV identifies objects using their property database id. Each object can consist of multiple `fragments`. Each fragment
has some geometry, a material, and a transform to position the geometry in 3D.

There are three ways to add graphics using the ModelBuilder:

- Create and add materials and geometry with THREE separately and then add fragments using the material name and the geometry id.
- Create the materials and geometry with THREE and add fragments using the javascript objects.
- Create a THREE Mesh and add fragments using the THREE Mesh object.

You can use the different methods separately or together as needed. Methods on the ModelBuilder that require a material accept the
name of a material added to a model or a THREE material. If the THREE material does not exist, it is added to the model.
Similarly, a geometry id or a THREE geometry object can be used interchangeably.

### 3.1 Adding graphics separately

When you add a material to the model you assign it a name. If the name is already in use or the material was added to a different model, the operation fails to add the material.

```
purple = new THREE.MeshPhongMaterial({
    color: new THREE.Color(1, 0, 1)
});
modelBuilder.addMaterial('purple', purple);

```

When you add geometry to the model, the ModelBuilder assigns and returns an id for the geometry. However, if the geometry was already added to the model, the operation fails.

```
box = new THREE.BufferGeometry().fromGeometry(new THREE.BoxGeometry(10, 10, 10));
let id = modelBuilder.addGeometry(box);

```

After the material and geometry are added, you can add a fragment using the material name and geometry id.

```
const transform = new THREE.Matrix4().compose(
    new THREE.Vector3(-15, 0, 0),
    new THREE.Quaternion(0, 0, 0, 1),
    new THREE.Vector3(1, 1, 1)
);
modelBuilder.addFragment(1, 'purple', transform);

```

The `addFragment` method returns an id that you can use to delete or change the display of the fragment.

### 3.2 Adding graphics using THREE objects

An alternate mechanism for adding graphics is using THREE objects. ModelBuilder checks to see if the objects have
been added and adds them if they haven’t. You can’t share THREE objects between models and the operation fails if any of the objects were added to a different
model. ModelBuilder generates a name to use when adding the material. The generated name is `!!mtl-n`, where n is the value of the `id` property of the material.

```
red = new THREE.MeshPhongMaterial({
    color: new THREE.Color(1, 0, 0)
});
torus = new THREE.BufferGeometry().fromGeometry(new THREE.TorusGeometry(10, 2, 32, 32));

const transform = new THREE.Matrix4().compose(
    new THREE.Vector3(19, 0, 0),
    new THREE.Quaternion(0, 0, 0, 1),
    new THREE.Vector3(1, 1, 1)
);
modelBuilder.addFragment(torus, red, transform);

```

Show More

### 3.3 Adding graphics using THREE Mesh

Adding graphics using THREE Mesh is like adding graphics using THREE objects, and the same limitations apply to both. Using THREE Mesh is a good option when you want to hold all of the THREE objects in the THREE mesh. This option only works if the conserveMemory method is not present–or is set to false–when calling a new model.

```
mesh = new THREE.Mesh(torus, purple);
mesh.matrix = new THREE.Matrix4().compose(
    new THREE.Vector3(0, 12, 12),
    new THREE.Quaternion(0, 0, 0, 1),
    new THREE.Vector3(1, 1, 1)
);
mesh.dbId = 100;    // Set the database id for the mesh
modelBuilder.addMesh(mesh);

```

Show More

## [What’s next?](#what-s-next)

Check out the [ModelBuilder](../reference-docs/Extensions-ModelBuilder.md) API documentation page to see all available methods.
