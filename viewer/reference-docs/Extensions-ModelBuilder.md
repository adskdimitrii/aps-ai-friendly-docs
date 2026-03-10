# ModelBuilder

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/ModelBuilder/

---

Autodesk.Viewing.Extensions

# ModelBuilder

Class that implements the API for building models dynamically. An instance of this class can be obtained after the Promise returned by [Autodesk.Viewing.Extensions.SceneBuilder#addNewModel](Extensions-SceneBuilder.md#addNewModel/) is resolved.

## [new ModelBuilder(model, options)](#new-modelbuilder-model-options)

The constructor is invoked automatically by [Autodesk.Viewing.Extensions.SceneBuilder](Extensions-SceneBuilder.md).

### Parameters

Expand all

| model*   [Autodesk.Viewing.Model](Viewing-Model.md) | The model this build works on |
| --- | --- |
| options   object | Options for the ModelBuilder |
| conserveMemory   boolean | Set to true to turn on memory conservation mode. In this mode [addMesh()]`Autodesk.Viewing.Extensions.ModelBuilder#addMesh </en/docs/viewer/v7/reference/Extensions/ModelBuilder/#addMesh/>`_ is not available because a single mesh is shared among all of the fragments in the model. |

* Required

# Methods

## [isConservingMemory()](#isconservingmemory)

### Returns

| type | description |
| --- | --- |
| boolean | true when the model being manipulated is using the memory-optimized code path. |

## [addGeometry(geometry, numFragments)](#addgeometry-geometry-numfragments)

Add geometry to the model.

### Parameters

| geometry*   THREE.BufferGeometry | The geometry to add. This can be null or undefined to allocate a geometry id without geometry. |
| --- | --- |
| numFragments   number | The number of fragments you expect this geometry to be used in. Default is 1. This is used to prioritize placing geometry on the GPU. Geometry used by more fragments gets a higher priority. |

* Required

### Returns

| type | description |
| --- | --- |
| number | The id of the added geometry, or 0 if there was an error. |

## [changeGeometry(existingGeom, geometry, numFragments)](#changegeometry-existinggeom-geometry-numfragments)

Change geometry in a model.

### Parameters

| existingGeom*   number, THREE.BufferGeometry | The geometry or the id of the geometry to change |
| --- | --- |
| geometry*   THREE.BufferGeometry | Geometry that replaces the existing geometry |
| numFragments   number | The number of fragments using this geometry. If not given, then we will count the number in the model. This is used to prioritize placing geometry on the GPU. Geometry used by more fragments gets a higher priority. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the existing geometry is valid and the geometry was changed. |

## [findGeometryFragments(geometry)](#findgeometryfragments-geometry)

Find fragments using a specific geometry.

### Parameters

| geometry*   number, THREE.BufferGeometry, Array.<(number\|THREE.BufferGeometry)> | The geometry or id(s) of the geometry to use in the search |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| Array.<number> | An array with the fragment ids for all fragments that were using the geometry. Null is returned if any geometry is invalid. |

## [removeGeometry(geometry)](#removegeometry-geometry)

Remove geometry from the model.

### Parameters

| geometry*   number, THREE.BufferGeometry, Array.<(number\|THREE.BufferGeometry)> | The geometry or id(s) of the geometry to remomve |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if all of the ids are valid and the geometry is removed. |

## [addMaterial(name, material)](#addmaterial-name-material)

Add a material that can be used by a mesh in the model.

### Parameters

| name*   string | The name used for the material. This name must not be used for an existing material in the model. |
| --- | --- |
| material*   THREE.Material | The material to add. This material must not be used in the model. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the material was added. |

## [changeMaterial(existingMaterial, material)](#changematerial-existingmaterial-material)

Replaces an existing material with another one.

### Parameters

| existingMaterial*   string, THREE.Material | The material or name of the material to change. The material must be in the model. |
| --- | --- |
| material*   THREE.Material | The material to replace the existing material. This material must not be used in the model. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the material is valid and the material was changed. |

## [findMaterial(name)](#findmaterial-name)

Find a material

### Parameters

| name*   string | The name of the material |
| --- | --- |

* Required

## [findMaterialFragments(materials)](#findmaterialfragments-materials)

Return the fragments that are using materials.

### Parameters

| materials*   string, THREE.Material, Array.<(string\|THREE.Material)> | The materials or names of the materials to use in the search. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| Array.<number> | An array with the fragment ids for all fragments that were using the materials. Null is returned if any material name is invalid or all of the materials were not removed. |

## [removeMaterial(materials)](#removematerial-materials)

Remove a material from the model. The caller should dispose the material if needed.

### Parameters

| materials*   string, THREE.Material, Array.<(string\|THREE.Material)> | The materials or names of the materials to remove. All of the names must be used for materials in the model. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if all of the names are valid and all of the materials are removed. |

## [addMesh(mesh)](#addmesh-mesh)

Add a fragment to the model using a mesh. Meshes can only be added to the model when [Autodesk.Viewing.Extensions.ModelBuilder#isConservingMemory](Extensions-ModelBuilder.md#isConservingMemory/) is false. Note the following restrictions:

- A mesh cannot be used multiple times.
- The geometry for a mesh cannot be used in different models.
- The material for a mesh cannot be used in different models.

### Parameters

Expand all

| mesh*   THREE.Mesh | The mesh to be added. |
| --- | --- |
| isLine   boolean | Optional bool to mark line geometry |
| isWideLine   boolean | Optional bool to mark wide line geometry |
| isPoint   boolean | Optional bool to mark point geometry |
| fragId   number | The fragment id for the mesh. This must not be defined when addMesh() is called and the Viewer sets this property to the new fragment id. |
| modeId   number | The id of the model. This must not be defined when addMesh() is called and the Viewer will set this to the id of the model for this ModelBuilder. |
| dbId   number | An optional object id for the mesh. Meshes with the same object id are selected as a unit. Internal tables are maintained to link fragments and dbIds. If a mesh is in the scene you shouldn’t change this value direcly. Call [Autodesk.Viewing.Extensions.ModelBuilder#changeFragmentsDbId](Extensions-ModelBuilder.md#changeFragmentsDbId/) to change it to insure the tables are updated. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the mesh was added. |

## [removeMesh(meshes)](#removemesh-meshes)

Remove a mesh from the model. Meshes can only be removed from the model when [Autodesk.Viewing.Extensions.ModelBuilder#isConservingMemory](Extensions-ModelBuilder.md#isConservingMemory/) is false.

### Parameters

| meshes*   THREE.Mesh, Array.<THREE.Mesh> | The meshes to be removed. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the mesh was removed. |

## [updateMesh(meshes, skipGeom, skipTransform)](#updatemesh-meshes-skipgeom-skiptransform)

Use this method to inform the Viewer when you directly update a mesh you added to the model. If you change a mesh directly without calling this method, it may not display properly. You don’t need to call this if you use the ModelBuilder API to update a mesh.

### Parameters

| meshes*   THREE.Mesh, Array.<THREE.Mesh> | The meshes that were changed. |
| --- | --- |
| skipGeom   boolean | Set to true if the geometry in the meshes wasn’t updated |
| skipTransform   boolean | Set to true if the tranforms in the meshes weren’t update |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the viewer was updated |

## [sceneUpdated(objectsMoved, skipRepaint)](#sceneupdated-objectsmoved-skiprepaint)

Signal viewer that scene was modified.

### Parameters

| objectsMoved   boolean | True if transforms or geometry was changed |
| --- | --- |
| skipRepaint   boolean | True to skip repainting because of this change |

## [addFragment(geometry, material, transform, bbox)](#addfragment-geometry-material-transform-bbox)

Add a fragment to a model. A fragment is the combination of a geometry, a material, and a transform.

### Parameters

| geometry*   number, THREE.BufferGeometry | The geometry or the id of the geometry for the fragment. Use a falsey value if the geometry for the fragment isn’t ready. If the geometry hasn’t been added to the model, this method will add it. Geometry must not be used in a different model. |
| --- | --- |
| material*   string, THREE.material | The material or the name of the material instance for the fragment. A material name must be used by a material in the model, but a material will be added to the model if it hasn’t already. |
| transform   THREE.Matrix, Array.<number> | The transform for the fragment. Default is the identity transform. If an array is used it is a 4x3 matrix in column major order. |
| bbox   THREE.Box3, Array.<number> | Bounding box for the fragment. Default is calculated from the geometry bounding box and the transform. When [Autodesk.Viewing.Extensions.ModelBuilder#isConservingMemory](Extensions-ModelBuilder.md#isConservingMemory/) is true then this argument is ignored and the default is used. If an array is used it contains the minimum x, y, z followed by the maximum x, y, z. |

* Required

### Returns

| type | description |
| --- | --- |
| number | The fragment id added or 0 if there was an error. |

## [changeFragmentGeometry(fragment, geometry, transform, bbox)](#changefragmentgeometry-fragment-geometry-transform-bbox)

Change the geometry and transform for a fragment.

### Parameters

| fragment*   number, THREE.Mesh | The mesh or fragment id whose geometry is to be set. |
| --- | --- |
| geometry*   number, THREE.BufferGeometry | The geometry or the id of the geometry for the fragment. Use a falsey value if the geometry for the fragment isn’t ready. If the geometry hasn’t been added to the model, this method will add it. Geometry must not be used in a different model. |
| transform   THREE.Matrix, Array.<number> | The transform for the fragment. If not present the transform isn’t changed. If an array is used it is a 4x3 matrix in column major order. |
| bbox   THREE.Box3, Array.<number> | Bounding box for the fragment. Default is calculated from the geometry bounding box and the transform. When [Autodesk.Viewing.Extensions.ModelBuilder#isConservingMemory](Extensions-ModelBuilder.md#isConservingMemory/) is true then this argument is ignored and the default is used. If an array is used it contains the minimum x, y, z followed by the maximum x, y, z. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the geometry id is valid and the fragment is changed. |

## [changeFragmentMaterial(fragment, material)](#changefragmentmaterial-fragment-material)

Change the material for a fragment.

### Parameters

| fragment*   number, THREE.Mesh | The mesh or fragment id whose material is to be set. |
| --- | --- |
| material*   string, THREE.material | The material or the name of the material for the fragment. A material name must be used by a material in the model, but a material will be added to the model if it hasn’t been. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the material id is valid and the fragment is changed. |

## [changeFragmentTransform(fragment, transform, bbox)](#changefragmenttransform-fragment-transform-bbox)

Change the transform for a fragment.

### Parameters

| fragment*   number, THREE.Mesh | The mesh or fragment id whose material is to be set. |
| --- | --- |
| transform*   THREE.Matrix, Array.<number> | The transform for the fragment. If an array is used it is a 4x3 matrix in column major order. |
| bbox   THREE.Box3, Array.<number> | [bbox] Bounding box for the fragment. Default is calculated from the geometry bounding box and the transform. When [Autodesk.Viewing.Extensions.ModelBuilder#isConservingMemory](Extensions-ModelBuilder.md#isConservingMemory/) is true then this argument is ignored and the default is used. If an array is used it contains the minimum x, y, z followed by the maximum x, y, z. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the fragId is valid and the transform was changed. |

## [changeFragmentsDbId(fragments, dbId)](#changefragmentsdbid-fragments-dbid)

Change the dbId of one or more fragments

### Parameters

| fragments*   number, THREE.Mesh, Array.<(number\|THREE.Mesh)> | The meshes or ids of the fragments to be changed |
| --- | --- |
| dbId*   number | The new dbId of the fragments. A 0 dbId will prevent an object from being selected. All fragments with the same dbId are selected as a single object. Changing the dbids on fragments will not change the display of objects that are already selected. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if all of the fragment ids were valid and all of the fragments were changed. |

## [removeFragment(fragments)](#removefragment-fragments)

Remove fragments from the model

### Parameters

| fragments*   number, THREE.Mesh, Array.<(number\|THREE.Mesh)> | The meshes or ids of the fragments to be removed |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if all of the fragment ids were valid and all of the fragments were removed. |

## [packNormals(geometry)](#packnormals-geometry)

Pack normals for geometry. Utility method automatically used when [Autodesk.Viewing.Extensions.ModelBuilder#isConservingMemory](Extensions-ModelBuilder.md#isConservingMemory/) is true.

### Parameters

| geometry*   THREE.BufferGeometry |  |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| THREE.BufferGeometry | The geometry argument is returned |
