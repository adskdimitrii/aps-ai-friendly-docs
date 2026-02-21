# InitOptions

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/globals/TypeDefs/InitOptions/

---

Type Definitions

# InitOptions

# Properties

| env   string | Can be `AutodeskProduction` (default), `AutodeskStaging`, or `AutodeskDevelopment`. |
| --- | --- |
| api   string | If automatic routing (the `DS_ENDPOINTS` feature flag) is enabled, must be `streamingV2` for SVF2 or `derivativeV2` for SVF. If automatic routing is disabled, must be `streamingV2` (SVF2) or `derivativeV2` (SVF) for models stored in a US data center, `streamingV2_EU` (SVF2) or `derivativeV2_EU` (SVF) for models stored in a European data center, or `streamingV2_AUS` (SVF2) or `derivativeV2_AUS` (SVF) for models stored in an Australian data center. Defaults to `derivativeV2` if left undefined. |
| getAccessToken   function | A function that provides an access token asynchronously. The function signature is `getAccessToken(onSuccess)`, where onSuccess is a callback that getAccessToken function should invoke when a token is granted, with the token being the first input parameter for the onSuccess function, and the token expire time (in seconds) being the second input parameter for the function. Viewer relies on both getAccessToken and the expire time to automatically renew token, so it is critical that getAccessToken must be implemented as described here. |
| language   string | Preferred language code as defined in RFC 4646, such as `en`, `de`, `fr` , etc. If no language is set, viewer will pick it up from the browser. If language is not as defined in RFC, viewer will fall back to `en` but the behavior is undefined. |
| logLevel   number | Specifies which types of messages will be logged into the console. Values are: 5 Debug, 4 Logs, 3 Info, 2 Warnings, 1 Errors, 0 None. Defaults to (1) for Errors only. All values can be found in Autodesk.Viewing.Private.LogLevels. |
| webGLHelpLink   string | A link url to a help page on webGL if itâs disabled. Supported only when using the GuiViewer3D instance; not supported in headless mode. |
