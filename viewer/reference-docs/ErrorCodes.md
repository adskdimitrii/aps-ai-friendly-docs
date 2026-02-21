# ErrorCodes

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/ErrorCodes/

---

Autodesk.Viewing

# ErrorCodes

Error code constants These constants will be used in [Callbacks#onGenericError](/en/docs/viewer/v7/reference/Callbacks/onGenericError/) functions.

# Constants

## [UNKNOWN_FAILURE](#unknown-failure)

An unknown failure has occurred.

| type |
| --- |
| number |

## [BAD_DATA](#bad-data)

Bad data (corrupted or malformed) was encountered.

| type |
| --- |
| number |

## [NETWORK_FAILURE](#network-failure)

A network failure was encountered.

| type |
| --- |
| number |

## [NETWORK_ACCESS_DENIED](#network-access-denied)

Access was denied to a network resource (HTTP 403)

| type |
| --- |
| number |

## [NETWORK_FILE_NOT_FOUND](#network-file-not-found)

A network resource could not be found (HTTP 404)

| type |
| --- |
| number |

## [NETWORK_SERVER_ERROR](#network-server-error)

A server error was returned when accessing a network resource (HTTP 5xx)

| type |
| --- |
| number |

## [NETWORK_UNHANDLED_RESPONSE_CODE](#network-unhandled-response-code)

An unhandled response code was returned when accessing a network resource (HTTP âeverything elseâ)

| type |
| --- |
| number |

## [BROWSER_WEBGL_NOT_SUPPORTED](#browser-webgl-not-supported)

Browser error = webGL is not supported by the current browser

| type |
| --- |
| number |

## [BAD_DATA_NO_VIEWABLE_CONTENT](#bad-data-no-viewable-content)

There is nothing viewable in the fetched document

| type |
| --- |
| number |

## [BROWSER_WEBGL_DISABLED](#browser-webgl-disabled)

Browser error = webGL is supported, but not enabled

| type |
| --- |
| number |

## [BAD_DATA_MODEL_IS_EMPTY](#bad-data-model-is-empty)

There is no geometry in loaded model

| type |
| --- |
| number |

## [UNSUPORTED_FILE_EXTENSION](#unsuported-file-extension)

The extension of the loaded file is not supported

| type |
| --- |
| number |

## [VIEWER_INTERNAL_ERROR](#viewer-internal-error)

Viewer error: wrong or forbidden usage of the viewer

| type |
| --- |
| number |

## [WEBGL_LOST_CONTEXT](#webgl-lost-context)

WebGL error while loading a model, typically due to IE11 limitations

| type |
| --- |
| number |

## [LOAD_CANCELED](#load-canceled)

Viewer error because loading a resource was canceled

| type |
| --- |
| number |

## [WEBGPU_LOST_CONTEXT](#webgpu-lost-context)

WebGPU error while loading a model

| type |
| --- |
| number |
