# ExtensionManager

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/Viewing/ExtensionManager/

---

Autodesk.Viewing

# ExtensionManager

The ExtensionManager manages all the extensions available to the viewer. Register, retrieve, and unregister your extension using the singleton `Autodesk.Viewing.theExtensionManager`.

You can load/unload your registered extension into a Viewer by invoking [viewer.loadExtension(id, options)](#loadExtension/) and [viewer.unloadExtension(id)](#unloadExtension/), respectively.

## [new ExtensionManager()](#new-extensionmanager)

# Methods

## [registerExtension(extensionId, extensionClass)](#registerextension-extensionid-extensionclass)

Registers a new extension with the given id.

### Parameters

| extensionId*   string | The string id of the extension. |
| --- | --- |
| extensionClass*   [Extension](/en/docs/viewer/v7/reference/Viewing/Extension/) | The Extension-derived class representing the extension. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the extension was successfully registered. |

## [getExtension(extensionId)](#getextension-extensionid)

Returns the class representing the extension with the given id.

### Parameters

| extensionId*   string | The string id of the extension. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| [Extension](/en/docs/viewer/v7/reference/Viewing/Extension/), null | The Extension-derived class if one was registered; null otherwise. |

## [unregisterExtension(extensionId)](#unregisterextension-extensionid)

Unregisters an existing extension with the given id.

### Parameters

| extensionId*   string | The string id of the extension. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the extension was successfully unregistered. |

## [registerExternalExtension(extensionId, urlPathOrCallback, dependencies)](#registerexternalextension-extensionid-urlpathorcallback-dependencies)

Registers an extension that needs to be downloaded before using it. The Viewer ships with some extensions that are not bundled, but can be runtime-fetched.

### Parameters

| extensionId*   string | The string id of the extension. |
| --- | --- |
| urlPathOrCallback*   string, function | The url from where it needs to be pulled from. Can be a relative or an absolute path. Optionally, this can be a callback function that defers the loading to the client application. Useful for webpack import style loading. Callback must return a promise that resolves when loading is finished. |
| dependencies*   Array.<string> | Optional list of extension IDs, whose bundles are needed before this extension can be built. |

* Required

### Returns

| type | description |
| --- | --- |
| boolean | True if the extension was successfully registered. |

## [getExternalPath(extensionId)](#getexternalpath-extensionid)

Returns the url path from where to download the extension; null if not registered through registerExternalExtension().

### Parameters

| extensionId*   string | The string id of the extension. |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| url, null | The url from where to download the extension; null if not download is needed. |

## [getRegisteredExtensions()](#getregisteredextensions)

Gets a list of all the extensions that are available for usage. Some are already available in memory, while others may require an additional file to be downloaded prior to its usage.

### Returns

| type | description |
| --- | --- |
| Array.<string> |  |

## [downloadExtension(extensionId)](#downloadextension-extensionid)

Download the extension and return its downloading promise

### Parameters

| extensionId*   string |  |
| --- | --- |

* Required

### Returns

| type | description |
| --- | --- |
| Promise | resolves when the extension class is ready for usage. |

## [isDownloading(extensionId)](#isdownloading-extensionid)

Is the extension being downloaded?

### Parameters

| extensionId*   string |  |
| --- | --- |

* Required

## [isAvailable(extensionId)](#isavailable-extensionid)

Is the extension class available?

### Parameters

| extensionId*   string |  |
| --- | --- |

* Required
