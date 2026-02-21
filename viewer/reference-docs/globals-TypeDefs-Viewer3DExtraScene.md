# Viewer3DExtraScene

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/globals/TypeDefs/Viewer3DExtraScene/

---

Type Definitions

# Viewer3DExtraScene

LMV has two extra scene it renders along with the models. One is rendered before the models, and the other is rendered after the models. These scenes are THREE.Scene objects and you can add custom meshes to be rendered to either of the scenes.

The objects you add to these scenes will be drawn using the same multiple render targets that are used when drawing the models. You may choose to either support multiple render targets or disable them.

To support multiple render targets you can only use Prism, MeshPhongMaterial, MeshBasicMaterial or LineBasicMaterial materials, and you must add all the materials to LMV.

To disable multiple render targets you can set the `skipIdTarget` and `skipDepthTarget` properties to `true`. If you disable multiple render targets your objects will not have rollover highlighting and will not contribute to ambient occlusion.

# Properties

| skipIdTarget   boolean | Set to true to prevent the id target from being rendered. |
| --- | --- |
| skipDepthTarget   boolean | Set to true to prevent the ambient occlusion depth target from being rendered. |
