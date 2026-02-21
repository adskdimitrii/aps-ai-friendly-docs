# FeatureFlags

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/FeatureFlags/

---

Autodesk.Viewing

# FeatureFlags

Static class that manages feature flags. Feature flags enable or expose capabilities in the viewer. After initialization, the flags become immutable. We are currently using two types of feature flags:

- enabling a functionality: checked in the code to toggle/modify/patch certain functionality
- exposing a capability: checked in the code to expose a capability to the user, with the actual capability not being enabled until the user explicitly enables it Additionally,initialization callbacks can be used to verify client support or automatically enable a feature.

## [new FeatureFlags()](#new-featureflags)

### Examples

```
FeatureFlags.set('ENABLE_FEATURE', true);

```

FeatureFlags.registerInitializationCallback(âEXPOSE_FEATUREâ, (enable, initializationData) => { â¦ });

---

# Methods

## [set(name, enable)](#set-name-enable)

Sets the value of a given feature flag. If the flag does not exist, nothing happens. If feature flags are already initialized, the change listener is not called.

### Parameters

| name*   string | Feature flag identifier |
| --- | --- |
| enable*   boolean | New value of the feature flag |

* Required

## [isEnabled(name)](#isenabled-name)

Returns whether a given feature flag is enabled.

### Parameters

| name*   string | Feature flag identifier |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean, undefined | Feature flag enabled state or undefined if the flag does not exist. |

## [print()](#print)

Prints all public feature flags and their values to the console
