# Scopes

Source: https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/scopes/

---

# Scopes

A scope is a permission that is set on a token, a context in which that token may act. For example, a token with the `data:read` scope is permitted to read data within the APS ecosystem and can be used on those endpoints that require that scope. Tokens without that scope would be denied access to such endpoints. (Individual endpoint reference pages list the required scopes.)

Scopes serve two principal functions:

1. Privacy and Control: In a three-legged context, they act as a mechanism for requesting and securing permission to act on an end user’s behalf in specified ways.
2. Security: In both two- and three-legged contexts, they ensure that if you lose control of your token, it cannot be misused to access resources for which it was not intended.

Expanding on the “Common Authentication and Authorization Flows” section of the [API Basics](https://aps.autodesk.com/en/docs/oauth/v2/overview/basics/) page, scopes are requested through the following endpoints:

- [GET authorize](../http-docs/http-authorize-GET.md): This is the Autodesk login and authorization page that an end user is redirected to in order to explicitly consent to granting the app the requested scopes.
- [POST gettoken](../http-docs/http-gettoken-POST.md): This obtains a new three-legged token with either all or a subset of the scopes granted to the original token.

Note that scopes are mandatory for all access tokens; calls without scopes will be rejected.

## [Scope Values](#scope-values)

The structure of scope values is `<namespace>:<operation>`, where `<namespace>` refers to a coarse resource or entity categorization and `<operation>` refers to the action to be performed on the resource or entity.

| Value | Display Message on Consent Page   (in three-legged OAuth flow) | Meaning |
| --- | --- | --- |
| `user-profile:read` | View your profile info | The application will be able to read the end user’s profile data (not including associated products and services). |
| `user:read` | View your profile info | The application will be able to read the end user’s profile data, including associated products and services. |
| `user:write` | Manage your profile info | The application will be able to create, update, and delete the end user’s profile data, including associated products and services. |
| `viewables:read` | View your viewable data | The application will only be able to read the end user’s viewable data (e.g., PNG and SVF files) within the Autodesk ecosystem. |
| `data:read` | View your data | The application will be able to read all the end user’s data (viewable and non-viewable) within the Autodesk ecosystem. |
| `data:write` | Manage your data | The application will be able to create, update, and delete data on behalf of the end user within the Autodesk ecosystem. |
| `data:create` | Write data | The application will be able to create data on behalf of the end user within the Autodesk ecosystem. |
| `data:search` | Search across your data | The application will be able to search the end user’s data within the Autodesk ecosystem. |
| `bucket:create` | Create new buckets | The application will be able to create an OSS bucket it will own. |
| `bucket:read` | View your buckets | The application will be able to read the metadata and list contents for OSS buckets that it has access to. |
| `bucket:update` | Update your buckets | The application will be able to set permissions and entitlements for OSS buckets that it has permission to modify. |
| `bucket:delete` | Delete your buckets | The application will be able to delete a bucket that it has permission to delete. |
| `code:all` | Author or execute your codes | The application will be able to author and execute code on behalf of the end user (e.g., scripts processed by the Design Automation API). |
| `account:read` | View your product and service accounts | For Product APIs, the application will be able to read the account data the end user has entitlements to. |
| `account:write` | Manage your product and service accounts | For Product APIs, the application will be able to update the account data the end user has entitlements to. |
| `openid` | Authorize the call | The application requires this scope to generate an id_token. |
| `data:read:<URN_OF_RESOURCE>` | data:read dynamic scope which allow client to access the specific resource | The application will be able to read only the resource with the URN/Object ID specified by `<URN_OF_RESOURCE>`.   `<URN_OF_RESOURCE>` takes the form `urn:adsk.*`. It can contain all characters (including unicode charcters) except `*`, `\`, `"`.       Example: `urn:adsk.objects:os.object:jp-220520/box.ipt`       **Note:** `<URN_OF_RESOURCE>` must be a raw URN and not a Base64 encoded URN. |

## [Scopes and Viewer Security Vulnerability](#scopes-and-viewer-security-vulnerability)

The [Viewer](https://aps.autodesk.com/en/docs/viewer/v7/) requires that the server hosting it (the REST API app) pass it a valid token, so that it can communicate with the [Model Derivative API](https://aps.autodesk.com/en/docs/model-derivative/v2/) directly via JavaScript to acquire the assets it needs to manifest design files in the browser. Because this means that the token is exposed on the client-side, it is important to make sure that the token is restricted for Viewer calls to the `viewables:read` scope, which limits access to the end user’s viewable output files (SVF, PNG, etc). This is particularly important in a two-legged context, where a malicious end user could use an unscoped token to take actions across the platform on the developer’s behalf and compromise the developer’s data.
