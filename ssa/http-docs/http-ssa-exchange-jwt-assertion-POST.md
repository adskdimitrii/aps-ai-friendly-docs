# token

Source: https://aps.autodesk.com/en/docs/ssa/reference/http/ssa-exchange-jwt-assertion-POST/

---

Exchange JWT Assertion for Token

POST

# token

Returns a three-legged access token for the JWT assertion you provide in the request body. See the Developer’s Guide topic [JWT Assertions](../developers-guide-docs/jwt-assertions.md) for information on how to generate a JWT assertion for this operation.

This operation is only for confidential clients. It requires Basic Authorization (`client_id`, `client_secret`). Authentication information (`client_id`, `client_secret`) can be included either in the header or the body, but not both simultaneously.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/authentication/v2/token |
| --- | --- |
| Authentication Context | Application context required |
| Required OAuth Scopes | No scopes required |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization   string | Must be `Basic <credentials>`, where `<credentials>` is a base64 encoded string of `client_id:client_secret`. This parameter is required only if `client_id` and `client_secret` are not provided in the request body. |
| --- | --- |
| Content-Type*   string | Must be `application/x-www-form-urlencoded` |

* Required

### Request

## [Body Structure](#body-structure)

| grant_type*   string | Must be `urn:ietf:params:oauth:grant-type:jwt-bearer`. |
| --- | --- |
| client_id   string | This attribute is optional; it serves as an additional option where the client can either use the authorization header or opt to send this information in the body. |
| client_secret   string | This attribute is optional; it serves as an additional option where the client can either use the authorization header or opt to send this information in the body. |
| assertion*   string | The value of the JWT assertion to exchange for a three-legged access-token. See [JWT Assertions](../developers-guide-docs/jwt-assertions.md#how-do-you-generate-a-jwt-assertion) for instructions on how to generate a JWT assertion. |
| scope   string | This is a space-delimited list of scopes. The scope in the token endpoint request body should be a subset of or the same as the scope specified in the assertion. If the scope is not present, then the returned access token will have the same scope as the assertion. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | The JWT assertion was successfully exchanged for a token. |
| --- | --- |
| 400   Bad Request | The request was invalid. The `grant_type` or `assertion` attribute may be missing or invalid, and the service account may not be in an enabled state. Verify the specified attributes and service account status, then retry the request. |
| 401   Unauthorized | The access token is invalid. It may have either expired or may not be a two-legged access token. Please verify the token and retry the request. |
| 403   Forbidden | The request was successfully validated but lacked the required permissions. Verify your credentials and permissions before you send this request again. |
| 500   Internal Server Error | An unknown server-side error occurred. Please try again later. If the problem persists, please contact support. |

### Response

## [Body Structure (200)](#body-structure-200)

| access_token   string | access token value |
| --- | --- |
| token_type   enum:string | type of token Will always be: `Bearer` |
| expires_in   number | access token expiry time in seconds |

## [Example](#example)

This example illustrates the successful exchange of JWT assertion for an access token.

**Tip**: Copy the JWT assertion provided in this example into a tool like [JWT.io](https://jwt.io/). Then modify the headers and claims as needed, and use your private key to generate a new JWT.

### Request

```
curl \
  --request POST \
  --url 'https://developer.api.autodesk.com/authentication/v2/token' \
  --header 'authorization: Basic xxx' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data 'grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer' \
  --data 'assertion=eyJraWQiOiI1ZGU5OTNmNC02MmIwLTQ5NWEtYTQzYS1iOTg5NmQ2ZTk1ODIiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJKbE85VEExempmSlFPR1hwSm1xOUpISlNJMEQ0VWtRNCIsInN1YiI6Ilo3NTJDVDVNS1cyUzlON0UiLCJhdWQiOiJodHRwczovL2RldmVsb3Blci5hcGkuYXV0b2Rlc2suY29tL2F1dGhlbnRpY2F0aW9uL3YyL3Rva2VuIiwiZXhwIjoxNzEwOTA3MTAwLCJzY29wZSI6WyJ1c2VyOnJlYWQiLCJkYXRhOnJlYWQiXX0.p9RNN28G38VCczbO6JgkTRfcb079_xDcDm2i4-HUqUdSZKre6jllx1IWhmwG0cm79EhC3OjJ0_zoPfKj2sP4lrPm27iXzd6x_SfD4LKS4zAJI2IERXjU05T9zWU4bfZWk0EinBysV0stvvEtZIBHczD_uAXCB5YLvyBX-O_kXqqkigNQupG9RsmE4GOjhG7pGLL_tdDYXkN46JAw-vMyXlhsdOntuZCjDOpcD4hsIueKwaqm6aLBKUTE1Htwpk0MUYmvl7AF03XDgWjhwRnJVOk_MkdF44bjSCAmsQ5uTYbWipUJjDqUy38b4xiRRRB0_qsg_kZ-DBOAFzUtYN6ilA'

```

### Response

```
{
  "expires_in": 3600,
  "token_type": "Bearer",
  "access_token": "eyJh...."
}

```
