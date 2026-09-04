# Authentication

Source: https://aps.autodesk.com/en/docs/tokenflex/developers_guide/authentication/

---

# Authentication

## [Authentication and Scopes](#authentication-and-scopes)

The Token Flex Usage Data API requires the use of 3-legged OAuth2 tokens. See the [OAuth documentation](https://aps.autodesk.com/en/docs/oauth/v2/) for more information on authentication, obtaining a bearer token, and scopes.

If your use case requires the use of 2-legged OAuth, such as for server to server integrations, please reach out to your Customer Success Manager to associate your Client ID directly with one of your admins.
Once the Client ID has been associated with an admin, you can use that Client ID to access all usage data available to that admin. You must *not* use this Client ID in a 3-legged flow.

HTTP GET requests to the Token Flex Usage Data API require the `data:read` scope.
HTTP POST, PUT, DELETE requests to the Token Flex Usage Data API require the `data:write` scope except [POST usage/:contract_number/query](../http-docs/http-usage-contract_number-query-POST.md).
