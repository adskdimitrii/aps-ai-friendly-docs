# Manage API Access to ACC Services

Source: https://aps.autodesk.com/en/docs/acc/tutorials/getting-started/manage-access-to-acc/

---

# Manage API Access to ACC Services

This walkthrough explains how to enable API access for an application in Autodesk Construction Cloud (ACC). Provisioning API access allows your app to interact with ACC services.

## [Before You Begin](#before-you-begin)

Verify that you have Admin access to an Autodesk Construction Cloud (ACC) account.
- [Register an app](/en/docs/oauth/v2/tutorials/create-app), and note the [client ID](/myapps).

## [Step 1: Access Account Administration](#step-1-access-account-administration)

Log in to your **ACC account**, and go to **Account Admin**.

![../../../_images/acc-account.jpg](../../../_images/acc-account.jpg)

The **Projects** screen appears.

## [Step 2: Open Custom Integrations](#step-2-open-custom-integrations)

From the left navigation, select **Custom Integrations**.

![../../../_images/acc-integrations.jpg](../../../_images/acc-integrations.jpg)

Select the **Add custom integration** button.

![../../../_images/acc-add-integration.jpg](../../../_images/acc-add-integration.jpg)

## [Step 3: Enter App Details](#step-3-enter-app-details)

Enter the following information:

- **APS Client ID** (from APS registration).
- **Custom Integration Name**.
- *(Optional)* **Description** for clarity.

Note that the **APS Client ID** must match the [client ID](/myapps) generated when you created the app. The **Custom Integration Name** does not need to match the original app name.

![../../../_images/acc-add-custom-integration.jpg](../../../_images/acc-add-custom-integration.jpg)

## [Step 4: Save and Confirm](#step-4-save-and-confirm)

Click **âAddâ** to finalize the integration.

The name of the app will appear in the **Custom integrations** screen.
