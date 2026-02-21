# WireframesExtension

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Extensions/WireframesExtension/

---

Autodesk.Viewing.Extensions

# WireframesExtension

Provides the ability of rendering the model in wireframe mode. The method implemented is not very performant, so itâs best to avoid using it with large models.

The extension id is: `Autodesk.Viewing.Wireframes`

## [new WireframesExtension()](#new-wireframesextension)

### Examples

```
viewer.loadExtension('Autodesk.Viewing.Wireframes')

```

---

# Methods

## [activate()](#activate)

Enters wireframe mode.

## [deactivate()](#deactivate)

Exits wireframe mode.

## [showSolidMaterial(show)](#showsolidmaterial-show)

Whether to replace the standard materials with a solid one, or not.

### Parameters

| show*   boolean |  |
| --- | --- |

* Required

## [showLines(show)](#showlines-show)

Whether to render line edges or not.

### Parameters

| show*   boolean |  |
| --- | --- |

* Required

## [setSolidMaterial(material)](#setsolidmaterial-material)

Replaces the solid material.

### Parameters

| material*   THREE.Material |  |
| --- | --- |

* Required

## [setLinesMaterial(material)](#setlinesmaterial-material)

Replaces the line material.

### Parameters

| material*   THREE.Material |  |
| --- | --- |

* Required

## [setLightPreset(name)](#setlightpreset-name)

Specifies the light preset to use when wireframe mode is activated.

### Parameters

| name*   string | the name of the light preset |
| --- | --- |

* Required
