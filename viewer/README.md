# APS Viewer Friendly Docs

This document does not link to all references. If you can't find what you're looking for here, look in the `./http-docs/` to see ALL API endpoints.

<!-- GENERATED:CONTENT_SUMMARY:START -->
## Content Summary

This folder contains documentation for the **APS Model Viewer** — a client-side JavaScript library for rendering and interacting with 2D/3D models in the browser. It covers viewer setup, extensions, UI components, and the full API reference.

### Overview & Viewer Basics (7 files)

Getting started with the Viewer: initialization, HTML embedding, event handling, extensions, toolbar customization, glTF support, and the diff tool for comparing model versions.

- [Overview](developers-guide-docs/overview.md) — introduction to the Viewer
- [Starting with HTML](developers-guide-docs/viewer_basics-starting-html.md) — embedding the viewer
- [Events](developers-guide-docs/viewer_basics-events.md) — viewer event system
- [Extensions](developers-guide-docs/viewer_basics-extensions.md) — loading and using extensions
- [Toolbar Buttons](developers-guide-docs/viewer_basics-toolbar-button.md) — custom toolbar UI
- [glTF Extension](developers-guide-docs/viewer_basics-GLTFExtension.md) — glTF model support
- [Diff Tool](developers-guide-docs/viewer_basics-difftool.md) — model version comparison
- [Glossary](developers-guide-docs/glossary.md)

### Advanced Options (10 files)

In-depth guides on advanced viewer features: aggregated views, custom geometry, 2D editing (Edit2D setup, usage, customization, manual mode), viewer profiles, property database queries, scene builder, and selective model loading.

- [Aggregated View](developers-guide-docs/advanced_options-aggregated-view.md)
- [Custom Geometry](developers-guide-docs/advanced_options-custom-geometry.md)
- [Edit2D Setup](developers-guide-docs/advanced_options-edit2d-setup.md), [Use](developers-guide-docs/advanced_options-edit2d-use.md), [Customize](developers-guide-docs/advanced_options-edit2d-customize.md), [Manual](developers-guide-docs/advanced_options-edit2d-manual.md)
- [Property DB Queries](developers-guide-docs/advanced_options-propdb-queries.md)
- [Scene Builder](developers-guide-docs/advanced_options-scene-builder.md)
- [Selective Loading](developers-guide-docs/advanced_options-selective-loading.md)
- [Profiles](developers-guide-docs/advanced_options-profiles.md)

### Interactive Examples (6 files)

Step-by-step code examples demonstrating viewer capabilities: [Example 1](developers-guide-docs/interactive_examples-example_1.md) through [Example 6](developers-guide-docs/interactive_examples-example_6.md).

### Core Viewer API Reference (20 files)

Reference docs for the main Viewer classes including viewer initialization, model handling, navigation, overlays, and utilities.

- [Viewer3D](reference-docs/Viewing-Viewer3D.md), [GuiViewer3D](reference-docs/Viewing-GuiViewer3D.md) — primary viewer classes
- [Document](reference-docs/Viewing-Document.md), [BubbleNode](reference-docs/Viewing-BubbleNode.md) — model document traversal
- [Model](reference-docs/Viewing-Model.md) — model data access
- [Navigation](reference-docs/Viewing-Navigation.md) — camera and navigation control
- [AggregatedView](reference-docs/Viewing-AggregatedView.md) — multi-model viewing
- [Extension](reference-docs/Viewing-Extension.md), [ExtensionManager](reference-docs/Viewing-ExtensionManager.md) — extension framework
- [ToolController](reference-docs/Viewing-ToolController.md), [ToolInterface](reference-docs/Viewing-ToolInterface.md) — input tool management
- [OverlayManager](reference-docs/Viewing-OverlayManager.md), [HotkeyManager](reference-docs/Viewing-HotkeyManager.md)
- [Profile](reference-docs/Viewing-Profile.md), [ProfileManager](reference-docs/Viewing-ProfileManager.md), [ProfileSettings](reference-docs/ProfileSettings.md)
- Plus: [PropertySet](reference-docs/Viewing-PropertySet.md), [FileLoader](reference-docs/Viewing-FileLoader.md), [FeatureFlags](reference-docs/Viewing-FeatureFlags.md), [EventUtils](reference-docs/Viewing-EventUtils.md), [ViewingUtilities](reference-docs/Viewing-ViewingUtilities.md), [ScreenModeDelegate](reference-docs/Viewing-ScreenModeDelegate.md)

### Extensions Reference (34 files)

API reference for all built-in viewer extensions including measurement, markup, navigation, section planes, and more.

- Measurement & Snapping: [MeasureExtension](reference-docs/Extensions-MeasureExtension.md), [SnappingExtension](reference-docs/Extensions-SnappingExtension.md), [Snapper](reference-docs/Snapping-Snapper.md), [SnapResult](reference-docs/MeasureCommon-SnapResult.md)
- Navigation: [BimWalkExtension](reference-docs/Extensions-BimWalkExtension.md), [FusionOrbitExtension](reference-docs/Extensions-FusionOrbitExtension.md), [NavToolsExtension](reference-docs/Extensions-NavToolsExtension.md), [GoHomeExtension](reference-docs/Extensions-GoHomeExtension.md)
- Visualization: [ExplodeExtension](reference-docs/Extensions-ExplodeExtension.md), [SectionExtension](reference-docs/Extensions-SectionExtension.md), [CrossFadeEffects](reference-docs/Extensions-CrossFadeEffects.md), [NPR](reference-docs/Extensions-NPR.md), [WireframesExtension](reference-docs/Extensions-WireframesExtension.md)
- Editing & Markup: [Edit2DExtension](reference-docs/Extensions-Edit2DExtension.md), [MarkupsCore](reference-docs/Extensions-MarkupsCore.md), [SceneBuilder](reference-docs/Extensions-SceneBuilder.md), [ModelBuilder](reference-docs/Extensions-ModelBuilder.md)
- UI: [ViewCubeUi](reference-docs/Extensions-ViewCubeUi.md), [MinimapExtension](reference-docs/Extensions-MinimapExtension.md), [DocumentBrowser](reference-docs/Extensions-DocumentBrowser.md), [ViewerSettingsExtension](reference-docs/Extensions-ViewerSettingsExtension.md), [PropertiesManagerExtension](reference-docs/Extensions-PropertiesManagerExtension.md)
- Plus 12 more extensions: Animation, FullScreen, Geolocation, glTF, Hyperlink, LayerManager, ModelStructure, PDF, Popout, RollCamera, SplitScreen, ZoomWindow

### UI Components Reference (13 files)

Reference for viewer UI widget classes used to build custom panels and toolbars.

- [ToolBar](reference-docs/UI-ToolBar.md), [Button](reference-docs/UI-Button.md), [ComboButton](reference-docs/UI-ComboButton.md), [RadioButtonGroup](reference-docs/UI-RadioButtonGroup.md)
- [DockingPanel](reference-docs/UI-DockingPanel.md), [PropertyPanel](reference-docs/UI-PropertyPanel.md), [SettingsPanel](reference-docs/UI-SettingsPanel.md), [ModelStructurePanel](reference-docs/UI-ModelStructurePanel.md)
- [Control](reference-docs/UI-Control.md), [ControlGroup](reference-docs/UI-ControlGroup.md), [DataTable](reference-docs/UI-DataTable.md), [Tree](reference-docs/UI-Tree.md)
- [ObjectContextMenu](reference-docs/UI-ObjectContextMenu.md), [Filterbox](reference-docs/UI-Filterbox.md)

### Globals, Types & Internal APIs (26 files)

Global functions, properties, type definitions, and internal/private APIs.

- **Functions** (6): [create](reference-docs/globals-Functions-create.md), [SearchResults](reference-docs/globals-Functions-SearchResults.md), [setViewType](reference-docs/globals-Functions-setViewType.md), [setCompassRotation](reference-docs/globals-Functions-setCompassRotation.md), and others
- **TypeDefs** (18): [InitOptions](reference-docs/globals-TypeDefs-InitOptions.md), [Prefs](reference-docs/globals-TypeDefs-Prefs.md)/[Prefs2D](reference-docs/globals-TypeDefs-Prefs2D.md)/[Prefs3D](reference-docs/globals-TypeDefs-Prefs3D.md), [ProfileSettings](reference-docs/globals-TypeDefs-ProfileSettings.md), [Intersection](reference-docs/globals-TypeDefs-Intersection.md), [SelectionDef](reference-docs/globals-TypeDefs-SelectionDef.md), [VIEW_TYPES](reference-docs/globals-TypeDefs-VIEW_TYPES.md), and more
- **Properties**: [LMV_VIEWER_VERSION](reference-docs/globals-Properties-LMV_VIEWER_VERSION.md), [AttributeType](reference-docs/globals-Properties-AttributeType.md), PDF flags
- **Private APIs** (5): [PropertyDatabase](reference-docs/Private-PropertyDatabase.md), [PropDbLoader](reference-docs/Private-PropDbLoader.md), [InstanceTree](reference-docs/Private-InstanceTree.md), [Preferences](reference-docs/Private-Preferences.md), [ViewerPreferences](reference-docs/Private-ViewerPreferences.md)
- [ErrorCodes](reference-docs/ErrorCodes.md)
<!-- GENERATED:CONTENT_SUMMARY:END -->
