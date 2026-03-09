# Task 2 â Create a Nickname for the app

Source: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/inventor/task2-create-nickname/

---

# Task 2 â Create a Nickname for the app

APS uses the Client ID that was generated in the previous task to uniquely identify the app you created. The Client ID can be long and cryptic, and hence a source of irritation when you reference data you add to your app.

A Nickname is a way to map an appâs Client ID to an easy-to-use name that you can use in place of the Client ID.

You can assign a nickname to an app only if there is no data associated with that app. That is why we are creating the nickname before we do anything else with the app.

By the end of this task, you will know how to create a nickname to reference an app.

You will use the following API endpoint in this task:

| HTTP Request | Description |
| --- | --- |
| [PATCH /forgeapps/{id}](../http-docs/http-forgeapps-id-PATCH.md) | Creates/updates the nickname for the current app. |

## [Step 1 - Create a nickname](#step-1-create-a-nickname)

### Request

```
curl -X PATCH \
  'https://developer.api.autodesk.com/da/us-east/v3/forgeapps/me' \
  -H 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d ' {"nickname": "<YOUR_NICKNAME>"}'

```

**Notes:**

- `<YOUR_ACCESS_TOKEN>` is the Access Token returned by the authentication request in the previous task.
- If your app doesnât have any data, you can map the app to another Nickname. The new nickname will overwrite the old one. If your app has data, you cannot `PATCH` a Nickname for your app anymore. This is true even if you have not yet assigned a Nickname for the app. The only way you can assign a Nickname to an app with data is by first calling [[DELETE] /forgeapps/me](/en/docs/design-automation/v3/reference/http/forgeapps-id-DELETE). This deletes all data associated with that app, including the Nickname.
- Nicknames must be globally unique. If the Nickname you provided is already in use, even by someone else, the PATCH request will return a `409 Conflict` error.

### Response

```
Date âFri, 19 Jul 2019 10:08:35 GMT
Strict-Transport-Security âmax-age=31536000; includeSubDomains
Via â1.1 58b224f0fcba4846d5699ecad6c6829f.cloudfront.net (CloudFront)
x-amz-apigw-id âdER5lECTIAMFeZQ=
X-Amz-Cf-Id âhgM0PhBQoDdAocVAEZx48V-T1Iyu5MeAwNPVHF4OWDD-y1dBUsVgwA==
X-Amz-Cf-Pop âSEA19
x-amzn-RequestId â2bd002d9-aa0d-11e9-bdcc-db9443c1afd8
X-Amzn-Trace-Id âRoot=1-5d3196a3-e2043246cf1cfa27b9d85aee
X-Cache âMiss from cloudfront
Content-Length â0
Connection âkeep-alive

```

Show More
