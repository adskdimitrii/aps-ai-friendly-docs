# Create an App

Source: https://aps.autodesk.com/en/docs/oauth/v2/tutorials/create-app/

---

# Create an App

Before an app can use APS APIs, you must register that app. APS then assigns a Client ID and a Client Secret to the app. The Client ID uniquely identifies the app. The Client Secret is similar to a password. You use it to validate your Client ID when obtaining an access token.

## [Step 1: Log in to the APS developer portal](#step-1-log-in-to-the-aps-developer-portal)

1. Go to the [APS developer portal](https://aps.autodesk.com).
![../../../_images/forge-home-new.png](../../../_images/forge-home-new.png)

2. Click **SIGN IN**. The Sign in page displays.
![../../../_images/signin-new.png](../../../_images/signin-new.png)

3. If you already have an Autodesk account:
  1. Specify your email address and click **NEXT**.
  2. In the next screen, specify your password and click **SIGN IN**.

    If you donât have an Autodesk account:

  1. Click the **CREATE ACCOUNT** link. The Create account page displays.
![../../../_images/signup-new.png](../../../_images/signup-new.png)
  2. Fill out the form and click **CREATE ACCOUNT**. The verification required screen displays.
  3. Check your email, and click the verification link on the email sent to you by Autodesk. The Account verified page is displayed.
  4. Click **DONE**. You are redirected to a Welcome Page.
  5. Specify your details and click **SUBMIT**. The APS Account Details page displays.

## [Step 2: Register an App](#step-2-register-an-app)

1. From the Profile menu on the top right of the page, click **Applications**.
![../../../_images/signed-in2.png](../../../_images/signed-in2.png)
2. Click **Create application**. The Create Application page displays.
![../../../_images/signed-in-new.png](../../../_images/signed-in-new.png)
3. Enter a name for the app and select an application type. For more information, see [Application Types](/en/docs/oauth/v2/developers_guide/App-types).
Note: The application (APS app) created by selecting the application type âDesktop, Mobile, Single-Page Appâ is for a client with public keys, and âTraditional Web App, Server-to-Server Appâ is for a client with private keys.
![../../../_images/create-app-new-int.png](../../../_images/create-app-new-int.png)
4. Click **Create**. A page to capture the details of your app is displayed.
![../../../_images/create-app2.png](../../../_images/create-app2.png)
5. Enter the details of your app as follows:
  1. In the **Description** box, enter a short description of the app.
  2. In the **Callback URL** box, enter the URL of the app that is designated to receive the authorization code on behalf of your app. For more information see [API Basics](/en/docs/oauth/v2/overview/basics).
  3. From the **API Access** drop-down, select the APIs that you want to use in your app.
6. Click **Save changes**.

## [Step 3: Note down Client ID and Client Secret](#step-3-note-down-client-id-and-client-secret)

Once you register an app, you will see a Client ID and Client Secret in your newly created app page. You will need these in all other OAuth flows and, by extension, to complete every other walkthrough on this site.

![../../../_images/create-app3-new.png](../../../_images/create-app3-new.png)
