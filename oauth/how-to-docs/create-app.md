# Create an App

Source: https://aps.autodesk.com/en/docs/oauth/v2/tutorials/create-app/

---

# Create an App

This walkthrough guides you through creating (registering) an app. The process generates a Client ID and Client Secret for your app, which you use to obtain access tokens and authenticate your API calls.

In APS, “create an app,” “register an app,” and “get a Client ID and Client Secret” all refer to the same process.

To complete this setup, you need:

- An APS account
- A developer hub

If you do not have an APS account, start with **Step 1: Create an APS account**.

If you already have an APS account, sign in at <https://aps.autodesk.com>, then continue to **Step 2: Set up a developer hub**.

## [Step 1: Create an APS account](#step-1-create-an-aps-account)

1. Visit the [Autodesk Platform Services portal](https://aps.autodesk.com).

2. Click **Sign in** in the upper-right corner.

3. Click **Create account**.

4. Follow the on-screen instructions to complete account setup. When finished, you will see a page titled **It seems you don’t have a hub yet**.


**Important:** During account setup, you will receive a backup code. Store it securely. You can use this code to access your account if you are unable to receive a one-time password.

## [Step 2: Set up a developer hub](#step-2-set-up-a-developer-hub)

Before you can register an app, you must have a developer hub.

### What is a developer hub?

A developer hub is a collaboration workspace where a team can build, share, and manage apps.

If you are part of a [team](https://www.autodesk.com/support/account/admin/users/manage-teams), your team may already have a developer hub. Ask your team admin to add you, then continue to **Step 3: Register an app**.

- If your team has an APS plan but has not created a developer hub yet:
  * If you are the team admin, continue to **Create a developer hub**.
  * Otherwise, ask your team admin to create one.
- If your team does not have an APS plan, or if you want your own developer hub, follow the steps below.

### Get an APS plan

1. If you see the **It seems you don’t have a hub yet** page, click **View options** in the **Get an APS plan** card.
If you do not see this page, visit <https://www.autodesk.com/products/autodesk-platform-services/overview>.

2. Scroll to the **Autodesk Platform Services cloud APIs** section.


3. Select your preferred plan tier.
    **Tip:** The Free tier provides monthly access to APS APIs with usage caps on paid APIs.

4. Follow the on-screen instructions to complete the purchase process. When finished, you will see a confirmation screen similar to the following:


### Create a developer hub

1. Visit <https://manage.autodesk.com>.
2. Navigate to **Products and Services** > **Hubs**.

3. Click **Create hub**, then:
  1. Select **APS developer hub**
  2. Enter a name and optional description
  3. Click **Create and Activate**

## [Step 3: Register an app](#step-3-register-an-app)

1. Visit <https://aps.autodesk.com> and sign in.

2. Open your profile menu and select **My applications**.


3. Select your developer hub from the **Developer Hub** dropdown.


4. Click **Create application**, then configure the following:
  - **Name**: Enter a descriptive name for your app.
  - **Application Type**: Select the application type for your app.

    For more information, see [Application Types](https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/App-types/).



5. Configure the app settings:
  - **Description**: Enter a short description of your app.
  - **API Access**: Select the APIs your app will use.



6. Click **Save changes**.

## [Step 4: Save your client credentials](#step-4-save-your-client-credentials)

After registering the app, copy the **Client ID** and **Client Secret** from **App settings**. You will use these credentials to obtain access tokens.

**Warning:** Store your Client Secret securely. Never commit it to source control, share it publicly, or include it in client-side code. For production environments, use a secure secrets manager.
