# APS Viewer Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

### Overview & Glossary

Introductory material for the APS Viewer, including a high-level overview and a reference glossary of key terms.

- [Overview](developers-guide-docs/overview.md)
- [Glossary](developers-guide-docs/glossary.md)

### Viewer Basics

Conceptual and setup guides covering how to embed and configure the viewer from scratch. (6 files)

- [Starting HTML Setup](developers-guide-docs/viewer_basics-starting-html.md)
- [Extensions](developers-guide-docs/viewer_basics-extensions.md)
- [Events](developers-guide-docs/viewer_basics-events.md)
- [Toolbar Button](developers-guide-docs/viewer_basics-toolbar-button.md)
- [GLTF Extension](developers-guide-docs/viewer_basics-GLTFExtension.md)
- [Diff Tool](developers-guide-docs/viewer_basics-difftool.md)

### Advanced Options

In-depth guides for advanced viewer features including 2D editing, profile customization, property database queries, selective loading, and more. (10 files)

- [Aggregated View](developers-guide-docs/advanced_options-aggregated-view.md)
- [Edit2D Setup](developers-guide-docs/advanced_options-edit2d-setup.md) — see also [manual](developers-guide-docs/advanced_options-edit2d-manual.md), [use](developers-guide-docs/advanced_options-edit2d-use.md), [customize](developers-guide-docs/advanced_options-edit2d-customize.md)
- [Custom Geometry](developers-guide-docs/advanced_options-custom-geometry.md)
- [Profiles](developers-guide-docs/advanced_options-profiles.md)
- [Property DB Queries](developers-guide-docs/advanced_options-propdb-queries.md)
- [Scene Builder](developers-guide-docs/advanced_options-scene-builder.md)
- [Selective Loading](developers-guide-docs/advanced_options-selective-loading.md)

### Interactive Examples

Six hands-on code examples demonstrating viewer capabilities in practice. (6 files)

- [Example 1](developers-guide-docs/interactive_examples-example_1.md), [Example 2](developers-guide-docs/interactive_examples-example_2.md), [Example 3](developers-guide-docs/interactive_examples-example_3.md), [Example 4](developers-guide-docs/interactive_examples-example_4.md), [Example 5](developers-guide-docs/interactive_examples-example_5.md), [Example 6](developers-guide-docs/interactive_examples-example_6.md)

### Extensions Reference

API reference for all built-in viewer extensions. (33 files)

- [BimWalk](reference-docs/Extensions-BimWalkExtension.md), [Animation](reference-docs/Extensions-AnimationExtension.md), [Explode](reference-docs/Extensions-ExplodeExtension.md), [Section](reference-docs/Extensions-SectionExtension.md)
- [Edit2D](reference-docs/Extensions-Edit2DExtension.md), [Markups Core](reference-docs/Extensions-MarkupsCore.md), [Measure](reference-docs/Extensions-MeasureExtension.md), [Snapping](reference-docs/Extensions-SnappingExtension.md)
- [Model Builder](reference-docs/Extensions-ModelBuilder.md), [Scene Builder](reference-docs/Extensions-SceneBuilder.md), [glTF](reference-docs/Extensions-glTF.md)
- [PDF](reference-docs/Extensions-PDFExtension.md), [Minimap](reference-docs/Extensions-MinimapExtension.md), [Split Screen](reference-docs/Extensions-SplitScreenExtension.md), [Full Screen](reference-docs/Extensions-FullScreenExtension.md)
- [Geolocation](reference-docs/Extensions-GeolocationExtension.md), [ViewCube UI](reference-docs/Extensions-ViewCubeUi.md), [NPR](reference-docs/Extensions-NPR.md)
- 14 additional extensions: CrossFadeEffects, DocumentBrowser, FusionOrbit, Gesture, GoHome, Hyperlink, LayerManager, ModelStructure, NavTools, PopOut, PropertiesManager, RollCamera, ViewerSettings, WireFrames, ZoomWindow

### Core Viewer API Reference

Reference documentation for the primary `Autodesk.Viewing` namespace classes and utilities. (26 files)

- [Viewer3D](reference-docs/Viewing-Viewer3D.md), [GuiViewer3D](reference-docs/Viewing-GuiViewer3D.md), [AggregatedView](reference-docs/Viewing-AggregatedView.md)
- [Document](reference-docs/Viewing-Document.md), [BubbleNode](reference-docs/Viewing-BubbleNode.md), [Model](reference-docs/Viewing-Model.md)
- [Extension](reference-docs/Viewing-Extension.md), [ExtensionManager](reference-docs/Viewing-ExtensionManager.md), [ToolController](reference-docs/Viewing-ToolController.md), [ToolInterface](reference-docs/Viewing-ToolInterface.md)
- [Navigation](reference-docs/Viewing-Navigation.md), [HotkeyManager](reference-docs/Viewing-HotkeyManager.md), [Profile](reference-docs/Viewing-Profile.md), [ProfileManager](reference-docs/Viewing-ProfileManager.md)
- [ProfileSettings](reference-docs/ProfileSettings.md), [MeasureCommon SnapResult](reference-docs/MeasureCommon-SnapResult.md), [Snapper](reference-docs/Snapping-Snapper.md)
- Additional: CoordinateSystem, EventUtils, FeatureFlags, FileLoader, OverlayManager, PropertySet, ViewingUtilities, ScreenModeDelegate variants

### UI Components Reference

Reference for the viewer's UI framework components. (14 files)

- [ToolBar](reference-docs/UI-ToolBar.md), [Button](reference-docs/UI-Button.md), [ComboButton](reference-docs/UI-ComboButton.md), [Control](reference-docs/UI-Control.md), [ControlGroup](reference-docs/UI-ControlGroup.md)
- [DockingPanel](reference-docs/UI-DockingPanel.md), [PropertyPanel](reference-docs/UI-PropertyPanel.md), [SettingsPanel](reference-docs/UI-SettingsPanel.md), [ModelStructurePanel](reference-docs/UI-ModelStructurePanel.md)
- [Tree](reference-docs/UI-Tree.md), [DataTable](reference-docs/UI-DataTable.md), [Filterbox](reference-docs/UI-Filterbox.md), [ObjectContextMenu](reference-docs/UI-ObjectContextMenu.md), [RadioButtonGroup](reference-docs/UI-RadioButtonGroup.md)

### Global Functions, Types & Properties

Top-level globals, type definitions, and constants used across the viewer API. (32 files)

- Functions: [create](reference-docs/globals-Functions-create.md), [setViewType](reference-docs/globals-Functions-setViewType.md), [showCompass](reference-docs/globals-Functions-showCompass.md), [SearchResults](reference-docs/globals-Functions-SearchResults.md), and 3 more
- Properties: [LMV_VIEWER_VERSION](reference-docs/globals-Properties-LMV_VIEWER_VERSION.md), [AttributeType](reference-docs/globals-Properties-AttributeType.md), [InitParametersSetting](reference-docs/globals-Properties-InitParametersSetting.md), and 3 more
- TypeDefs: [InitOptions](reference-docs/globals-TypeDefs-InitOptions.md), [Prefs3D](reference-docs/globals-TypeDefs-Prefs3D.md), [Prefs2D](reference-docs/globals-TypeDefs-Prefs2D.md), [SelectionDef](reference-docs/globals-TypeDefs-SelectionDef.md), and 14 more
- Classes: [GlobalManagerProvider](reference-docs/globals-Classes-GlobalManagerProvider.md)

### Error Codes & Private Internals

- [Error Codes](reference-docs/ErrorCodes.md) — enumeration of viewer error codes
- Private/internal APIs (5 files): [InstanceTree](reference-docs/Private-InstanceTree.md), [PropertyDatabase](reference-docs/Private-PropertyDatabase.md), [PropDbLoader](reference-docs/Private-PropDbLoader.md), [Preferences](reference-docs/Private-Preferences.md), [ViewerPreferences](reference-docs/Private-ViewerPreferences.md)
<!-- GENERATED:CONTENT_SUMMARY:END -->
