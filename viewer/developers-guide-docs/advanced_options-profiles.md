# Using Profile APIs

Source: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/advanced_options/profiles/

---

# Using Profile APIs

The Profile API lets you specify the *preference* values and *extensions* that you want to load or unload in the Viewer.

This tutorial covers the following:
:   - Using built-in profiles to apply settings to the Viewer.
    - Creating a custom profile.
    - Registering custom profiles with a specific file type.
    - Overriding the default profile with a custom one.

## [Using built-in profiles](#using-built-in-profiles)

The Viewer provides built-in, ready-to-use profiles that offer the same user experience as desktop products such as Navisworks and Revit.

For more information, see [ProfileSettings](../reference-docs/ProfileSettings.md)

The following snippet shows how to use the Navisworks profile.

```
const profileSettings = Autodesk.Viewing.ProfileSettings.Navis;
const profile = new Autodesk.Viewing.Profile(profileSettings);
viewer.setProfile(profile);

```

The following snippet shows how to use the AEC profile.

```
const profileSettings = Autodesk.Viewing.ProfileSettings.AEC;
const profile = new Autodesk.Viewing.Profile(profileSettings);
viewer.setProfile(profile);

```

## [Create a custom profile](#create-a-custom-profile)

You can also set a custom profile. A custom profile can override existing preferences, load or unload specific extensions, and set preferences to be persistent.

For more information, see [Profile](../reference-docs/Viewing-Profile.md)

The following snippet overrides a couple of preferences, adds new preferences, unloads two extensions, and sets some preferences to be persistent between browser sessions.

```
const customProfileSettings = {
    settings: {
        reverseMouseZoomDir: true, // override existing
        reverseHorizontalLookDirection: true, // override existing
        customSettingOne: true, // new preference
        customSettingTwo: 2, // new preference
        customSettingThree: 'test' // new preference
    },
    extensions: {
        unload: ['Autodesk.ViewCubeUi', 'Autodesk.BimWalk']
    }
};
const customProfile = new Autodesk.Viewing.Profile(customProfileSettings);
// Updates viewer settings encapsulated witihn a Profile.
// This method will also load and unload extensions referenced by the Profile.
viewer.setProfile(customProfile);

```

Show More

Custom profiles can be cloned from existing profile settings. In the following snippet, the profile settings are cloned from the AEC profile settings.
In addition to the AEC profile settings, the properties panel opens when selecting an object and progressive rendering is turned off.

```
const aecProfileSettings = Autodesk.Viewing.ProfileSettings.AEC;
// The custom profile settings are cloned from the AEC profile settings.
const customProfileSettings = Autodesk.Viewing.ProfileSettings.clone(aecProfileSettings);
// Turn off progressive rendering
customProfileSettings.settings.progressiveRendering = false;
// Open the properties panel when selecting an object.
customProfileSettings.settings.openPropertiesOnSelect = true;

const customProfile = new Autodesk.Viewing.Profile(customProfileSettings);
viewer.setProfile(customProfile);

```

Show More

## [Registering a custom profile for a specific file type](#registering-a-custom-profile-for-a-specific-file-type)

Use the ProfileManager (`viewer.profileManager`) to register a custom profile with a specific file type.

For more information, see [ProfileManager](../reference-docs/Viewing-ProfileManager.md)

To use the registered file profiles be sure to set the following config flag:

```
const config3d = {
    useFileProfile: true
};
const viewer = new Autodesk.Viewing.GuiViewer3D(viewerElement, config3d);

```

During initialization, register the custom profile with the dwf file type.

```
Autodesk.Viewing.Initializer(initOptions, function() {
    const profileSettings = {
        name: 'DWF',
        settings: {
            // Turn off progressive rendering
            progressiveRendering: false,
            // Open the properties panel when selecting an object.
            openPropertiesOnSelect: true
        }
    };
    viewer.profileManager.registerProfile('dwf', profileSettings);
    viewer.start();
    // The urn should be a bubble node derived from a dwf model.
    Autodesk.Viewing.Document.load(urn, (lmvDocument) => {
        const geometryItems = lmvDocument.getRoot().search({ type: 'geometry' });
        const defaultItem = geometryItems[0];
        viewer.loadDocumentNode(lmvDocument, defaultItem, config3d);
    });
});

```

Show More

## [Use custom profile regardless of the file type loaded](#use-custom-profile-regardless-of-the-file-type-loaded)

You can make a custom profile the default for any file type. The following code sample demonstrates how to override the default profile with the custom profile.

```
viewer.profileManager.registerProfile('default', profileSettings);

```

## [Restore default profile](#restore-default-profile)

The following snippet restores the default profile available in the Viewer.

```
// Get the registered default profile
const defaultProfile = viewer.profileManager.getProfileOrDefault();
// Set the default profile
viewer.setProfile(defaultProfile);

```
