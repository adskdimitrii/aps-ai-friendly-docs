# Create an App

Source: https://aps.autodesk.com/en/docs/oauth/v2/tutorials/create-app/

---

# Create an App

Before an app can use APS APIs, you must register that app. APS then assigns a Client ID and a Client Secret to the app. The Client ID uniquely identifies the app. The Client Secret is similar to a password. You use it to validate your Client ID when obtaining an access token.

## Step 1: Log in to the APS developer portal

- Go to the APS developer portal .

- Click SIGN IN . The Sign in page displays.

- If you already have an Autodesk account: Specify your email address and click NEXT . In the next screen, specify your password and click SIGN IN . If you donât have an Autodesk account: Click the CREATE ACCOUNT link. The Create account page displays. Fill out the form and click CREATE ACCOUNT . The verification required screen displays. Check your email, and click the verification link on the email sent to you by Autodesk. The Account verified page is displayed. Click DONE . You are redirected to a Welcome Page. Specify your details and click SUBMIT . The APS Account Details page displays.

- Specify your email address and click NEXT .

- In the next screen, specify your password and click SIGN IN .

If you donât have an Autodesk account:

- Click the CREATE ACCOUNT link. The Create account page displays.

- Fill out the form and click CREATE ACCOUNT . The verification required screen displays.

- Check your email, and click the verification link on the email sent to you by Autodesk. The Account verified page is displayed.

- Click DONE . You are redirected to a Welcome Page.

- Specify your details and click SUBMIT . The APS Account Details page displays.

## Step 2: Register an App

- From the Profile menu on the top right of the page, click Applications .

- Click Create application . The Create Application page displays.

- Enter a name for the app and select an application type. For more information, see Application Types .
Note: The application (APS app) created by selecting the application type âDesktop, Mobile, Single-Page Appâ is for a client with public keys, and âTraditional Web App, Server-to-Server Appâ is for a client with private keys.

- Click Create . A page to capture the details of your app is displayed.

- Enter the details of your app as follows: In the Description box, enter a short description of the app. In the Callback URL box, enter the URL of the app that is designated to receive the authorization code on behalf of your app. For more information see API Basics . From the API Access drop-down, select the APIs that you want to use in your app.

- In the Description box, enter a short description of the app.

- In the Callback URL box, enter the URL of the app that is designated to receive the authorization code on behalf of your app. For more information see API Basics .

- From the API Access drop-down, select the APIs that you want to use in your app.

- Click Save changes .

## Step 3: Note down Client ID and Client Secret

Once you register an app, you will see a Client ID and Client Secret in your newly created app page. You will need these in all other OAuth flows and, by extension, to complete every other walkthrough on this site.
