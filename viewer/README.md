# APS Viewer Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Overview & Glossary

Introductory and terminology docs for the APS Viewer.

- [Overview](developers-guide-docs/overview.md)
- [Glossary](developers-guide-docs/glossary.md)

### Viewer Basics

Foundational guides for embedding and configuring the viewer. Covers the startup HTML page, events, extensions lifecycle, toolbar customization, the diff tool, and GLTF integration. 6 files.

- [Starting HTML](developers-guide-docs/viewer_basics-starting-html.md)
- [Events](developers-guide-docs/viewer_basics-events.md)
- [Extensions](developers-guide-docs/viewer_basics-extensions.md)
- [Toolbar Button](developers-guide-docs/viewer_basics-toolbar-button.md)
- [Diff Tool](developers-guide-docs/viewer_basics-difftool.md)
- [GLTF Extension](developers-guide-docs/viewer_basics-GLTFExtension.md)

### Advanced Options

In-depth guides for power users. Topics include aggregated views, custom geometry, property database queries, selective loading, scene builder, profiles, and the Edit2D framework (setup, usage, manual mode, customization). 10 files.

- [Aggregated View](developers-guide-docs/advanced_options-aggregated-view.md)
- [Custom Geometry](developers-guide-docs/advanced_options-custom-geometry.md)
- [Scene Builder](developers-guide-docs/advanced_options-scene-builder.md)
- [Property DB Queries](developers-guide-docs/advanced_options-propdb-queries.md)
- [Selective Loading](developers-guide-docs/advanced_options-selective-loading.md)
- [Profiles](developers-guide-docs/advanced_options-profiles.md)
- Edit2D: [Setup](developers-guide-docs/advanced_options-edit2d-setup.md), [Use](developers-guide-docs/advanced_options-edit2d-use.md), [Manual](developers-guide-docs/advanced_options-edit2d-manual.md), [Customize](developers-guide-docs/advanced_options-edit2d-customize.md)

### Interactive Examples

Six hands-on code examples demonstrating viewer capabilities. 6 files.

- [Example 1](developers-guide-docs/interactive_examples-example_1.md) through [Example 6](developers-guide-docs/interactive_examples-example_6.md)

### Core Viewer API Reference

API reference for the primary `Autodesk.Viewing` namespace classes. Covers the main viewer objects, document/model loading, navigation, overlays, profiles, tools, and screen mode delegates. ~20 files.

- [Viewer3D](reference-docs/Viewing-Viewer3D.md)
- [GuiViewer3D](reference-docs/Viewing-GuiViewer3D.md)
- [Document](reference-docs/Viewing-Document.md)
- [Model](reference-docs/Viewing-Model.md)
- [BubbleNode](reference-docs/Viewing-BubbleNode.md)
- [Extension](reference-docs/Viewing-Extension.md) / [ExtensionManager](reference-docs/Viewing-ExtensionManager.md)
- [Navigation](reference-docs/Viewing-Navigation.md), [ToolController](reference-docs/Viewing-ToolController.md), [ToolInterface](reference-docs/Viewing-ToolInterface.md)
- [AggregatedView](reference-docs/Viewing-AggregatedView.md), [Profile](reference-docs/Viewing-Profile.md), [ProfileManager](reference-docs/Viewing-ProfileManager.md)
- Plus: `CoordinateSystem`, `EventUtils`, `FeatureFlags`, `FileLoader`, `HotkeyManager`, `OverlayManager`, `PropertySet`, `ScreenModeDelegate`, `ViewingUtilities`

### Extensions Reference

API reference for all built-in viewer extensions. Covers 2D/3D tools, visualization, navigation, markup, measurement, model structure, PDF, and more. 34 files.

- [BimWalkExtension](reference-docs/Extensions-BimWalkExtension.md)
- [Edit2DExtension](reference-docs/Extensions-Edit2DExtension.md)
- [MarkupsCore](reference-docs/Extensions-MarkupsCore.md)
- [MeasureExtension](reference-docs/Extensions-MeasureExtension.md)
- [SceneBuilder](reference-docs/Extensions-SceneBuilder.md) / [ModelBuilder](reference-docs/Extensions-ModelBuilder.md)
- [SectionExtension](reference-docs/Extensions-SectionExtension.md), [ExplodeExtension](reference-docs/Extensions-ExplodeExtension.md)
- [PDFExtension](reference-docs/Extensions-PDFExtension.md), [glTF](reference-docs/Extensions-glTF.md)
- Plus: `AnimationExtension`, `CrossFadeEffects`, `DocumentBrowser`, `FullScreenExtension`, `FusionOrbitExtension`, `GeolocationExtension`, `GoHomeExtension`, `HyperlinkExtension`, `LayerManagerExtension`, `MinimapExtension`, `ModelStructureExtension`, `NPR`, `NavToolsExtension`, `PopoutExtension`, `PropertiesManagerExtension`, `RollCameraExtension`, `SnappingExtension`, `SplitScreenExtension`, `ViewCubeUi`, `ViewerSettingsExtension`, `WireframesExtension`, `ZoomWindow`, and gesture/navigation extensions

### UI Components Reference

API reference for the viewer's built-in UI toolkit — panels, toolbars, controls, and data display widgets. 15 files.

- [ToolBar](reference-docs/UI-ToolBar.md), [Button](reference-docs/UI-Button.md), [ComboButton](reference-docs/UI-ComboButton.md), [RadioButtonGroup](reference-docs/UI-RadioButtonGroup.md)
- [DockingPanel](reference-docs/UI-DockingPanel.md), [PropertyPanel](reference-docs/UI-PropertyPanel.md), [SettingsPanel](reference-docs/UI-SettingsPanel.md), [ModelStructurePanel](reference-docs/UI-ModelStructurePanel.md)
- [Control](reference-docs/UI-Control.md), [ControlGroup](reference-docs/UI-ControlGroup.md), [DataTable](reference-docs/UI-DataTable.md), [Filterbox](reference-docs/UI-Filterbox.md), [Tree](reference-docs/UI-Tree.md), [ObjectContextMenu](reference-docs/UI-ObjectContextMenu.md)

### Global API — Types, Functions & Properties

Global-scope classes, factory functions, constants, and TypeDefs used across the viewer API. ~25 files.

- Functions: [create](reference-docs/globals-Functions-create.md), [setViewType](reference-docs/globals-Functions-setViewType.md), [showCompass](reference-docs/globals-Functions-showCompass.md), `setCompassRotation`, `cloneHTMLElementsToWrapperElement`, `GlobalManagerMixin`
- Classes: [GlobalManagerProvider](reference-docs/globals-Classes-GlobalManagerProvider.md), [SearchResults](reference-docs/globals-Classes-SearchResults.md)
- Properties/Constants: [LMV_VIEWER_VERSION](reference-docs/globals-Properties-LMV_VIEWER_VERSION.md), `LMV_RASTER_PDF`, `LMV_VECTOR_PDF`, `LMV_THIRD_PARTY_COOKIE`, `AttributeType`, `InitParametersSetting`
- TypeDefs: [InitOptions](reference-docs/globals-TypeDefs-InitOptions.md), [Prefs](reference-docs/globals-TypeDefs-Prefs.md), [Prefs2D](reference-docs/globals-TypeDefs-Prefs2D.md), [Prefs3D](reference-docs/globals-TypeDefs-Prefs3D.md), [ProfileSettings](reference-docs/globals-TypeDefs-ProfileSettings.md), `Extensions`, `FPS_TARGET_MODES`, `VIEW_TYPES`, and more

### Private APIs, Utilities & Error Codes

Internal/advanced APIs and diagnostics. 10 files.

- [ErrorCodes](reference-docs/ErrorCodes.md), [ProfileSettings](reference-docs/ProfileSettings.md)
- [MeasureCommon-SnapResult](reference-docs/MeasureCommon-SnapResult.md), [Snapping-Snapper](reference-docs/Snapping-Snapper.md)
- Private: [InstanceTree](reference-docs/Private-InstanceTree.md), [PropertyDatabase](reference-docs/Private-PropertyDatabase.md), [PropDbLoader](reference-docs/Private-PropDbLoader.md), [Preferences](reference-docs/Private-Preferences.md), [ViewerPreferences](reference-docs/Private-ViewerPreferences.md)
<!-- GENERATED:CONTENT_SUMMARY:END -->
