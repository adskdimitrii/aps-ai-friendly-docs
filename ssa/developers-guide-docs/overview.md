# About the Secure Service Account API

Source: https://aps.autodesk.com/en/docs/ssa/developers_guide/overview/

---

# About the Secure Service Account API

When applications need to authenticate and access cloud services automatically—without user intervention or embedded credentials—they require specialized identity management. This functionality goes by different names across platforms:

- **Non-human identities** or **non-human users** (general terminology)
- **Application Managed Service** accounts (enterprise systems)
- **Service accounts** (Google Cloud, general usage)
- **Managed identities** or **service principals** (Microsoft Azure)
- **IAM roles for applications** (AWS)

Autodesk Platform Services provides this capability through the **Secure Service Account API (SSA)**. SSA allows applications to securely authenticate using secure service accounts instead of requiring a user to sign in. This API ensures the security of digital assets, enables automation, and offer robust access controls through fine-grained permissions.

SSAs use a private key to generate a JWT, which is then exchanged for a three-legged access token. This token can then be used to interact with other Autodesk Platform Services (APS) APIs securely.

The SSA API enables:

- A simple and secure server-to-server mechanism to automate existing three-legged access token workflows
- Creation and management of service accounts and RSA key pairs
- Exchange a secure JWT for a user-context three-legged access token

Client ID and SSA API usage are the app’s unique identifiers used in the OAuth flow. All API activity performed by an SSA is linked to its associated Client ID. If multiple SSA accounts are created under a single Client ID, then all their API usage is aggregated and attributed to that Client ID.

## [Common uses](#common-uses)

With the Secure Service Account API, applications can authenticate automatically without human intervention, achieving secure interactions and data transfers through APIs between clients and servers connected over public networks.

- **Enhanced Security**: By creating service accounts bound to specific applications, SSAs reduce the risk of unauthorized access and overexposure of project data.
- **Refined Access Control**: SSAs offer fine-grained control over access permissions, ensuring that applications only access the resources they need.
- **Improved User Experience**: Customers can confidently integrate third-party applications without compromising security, reducing the need to decline integrations or remove existing ones.
- **Seamless Automation**: SSAs enable applications to perform automated tasks without human interference, streamlining workflows and increasing efficiency.
- **Third-Party Application Support**: SSAs allow third-party applications to interact securely within the Autodesk ecosystem, facilitating more robust and secure integrations.
- **Sign in**: The Secure Service Account never needs to sign in, and can never “lose” their refresh token.

## [Supported APIs and Integrations](#supported-apis-and-integrations)

SSA provides comprehensive support for Autodesk Platform Services APIs:

- **Forma Build Module APIs**: Complete support for all Forma Build modules including Sheets, Costs, and Forms APIs.

- **Forma/BIM 360 APIs**: Full support for three-legged Forma APIs including BIM 360 Docs, Forma Data Management, Cost, Build, Issues, Forms, and more.

- **Revit Cloud Worksharing (RCW)**: Full compatibility with Revit Cloud Worksharing models through the RCM API.
    **Note:** A license of either BIM Collaborate (READ) or BIM Collaborate Pro (READ/WRITE) is required to access RCW Models when using the RCM API with an SSA user. Additionally, the SSA user must be assigned “view+download” permissions to the folder where the model is located.

- **Autodesk App Store**: SSAs work seamlessly with applications published on the Autodesk App Store. During the app publishing process, provide the same Client ID associated with your service account.

## [Behavior notes](#behavior-notes)

- **Application Identity Management:** SSAs represent applications or services rather than individual users, enabling automated workflows to operate without human sign-in requirements.
- **Multiple SSAs per Application:** A single Client ID can have multiple SSAs, each with isolated access permissions and specific role assignments for different services.
- **SSA Limits:** Each Client ID has a default limit of 10 SSAs. Higher limits require contacting Autodesk support via [ssa-requests@autodesk.com](mailto:ssa-requests%40autodesk.com) with specific requirements.
- **SSA Inactivity Policy:** SSAs that remain idle for 12 consecutive months are subject to deactivation and subsequent removal.
- **Two-Legged Token Restrictions:** Data Management and Admin APIs accept both two-legged and three-legged access tokens by default. Client IDs can be restricted to only three-legged tokens (SSA access) for enhanced security by contacting [ssa-requests@autodesk.com](mailto:ssa-requests%40autodesk.com). Your request must include:
  * The Client ID
  * Proof of ownership using one of these methods:
    + Request via the email address on file
    + Confirmation from your Autodesk Customer Success Manager (CSM) via Enterprise Business Agreement (EBA)
    + Involvement of an Autodesk Technical Solution Expert (TSE)
- **App Store Integration**: SSAs are fully compatible with applications published on the Autodesk App Store, enabling secure automated workflows for marketplace applications.

## [Known issues](#known-issues)

- **Admin API** – not yet supported for user-authorized operations (three-legged OAuth).
- **Fusion Hubs** – not yet supported for SSA access.
- **Automation API (Formerly Design Automation API)** – does not currently support the management of WorkItems with a three-legged access token. However, you can use three-legged access tokens obtained via SSAs to access ACC/BIM360 data.

## [Next steps](#next-steps)

- Get started with the [How-to guide.](https://aps.autodesk.com/en/docs/ssa/v1/tutorials/)
- Explore [Code Samples](https://aps.autodesk.com/en/docs/ssa/v1/code_samples/code_samples/) to discover how the Secure Service Account API is used in applications.

## [Terms of service](#terms-of-service)

The **Secure Service Account API** is subject to [Autodesk Platform Services Terms of Service.](https://www.autodesk.com/company/legal-notices-trademarks/terms-of-service-autodesk360-web-services/forge-platform-web-services-api-terms-of-service)
