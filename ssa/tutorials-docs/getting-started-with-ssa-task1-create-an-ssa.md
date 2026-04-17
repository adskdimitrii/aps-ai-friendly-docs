# Task 1 – Create an SSA

Source: https://aps.autodesk.com/en/docs/ssa/tutorials/getting-started-with-ssa/task1-create-an-ssa/

---

# Task 1 – Create an SSA

This task demonstrates how to create a secure service account. The steps are as follows:
> 

- Get an Access Token
- Create SSA
- Create RSA private key

The operations used in this task are as follows:

| Operation | HTTP Request |
| --- | --- |
| [Token](../../oauth/http-docs/http-gettoken-POST.md) | POST/Token |
| [Create Service Account](../http-docs/http-ssa-create-service-account-POST.md) | POST/service-accounts |
| [Create Keys](../http-docs/http-ssa-create-service-account-key-POST.md) | POST/service-accounts/{serviceAccountId}/keys |

## [Step 1 - Get an Access Token](#step-1-get-an-access-token)

1. Combine the Client ID with the Client Secret and convert it to a Base64 encoded string before requesting a two-legged OAuth access token:

- Concatenate the Client ID and Client Secret with a colon (:) character in between:

> ```
> <CLIENT_ID>:<CLIENT_SECRET>
>
> ```

- Use the appropriate function or method in your preferred programming language to encode the combined string to the Base64 format. For example:

> | Programming Language | Method/Function |
> | --- | --- |
> | JavaScript | `btoa()` function |
> | Python | `b64encode()` function from the `base64` module |
> | C# | `Convert.ToBase64String()` method |
>
> **Note:** Online tools exist to convert the combined string to a Base64-encoded string. However, it is not recommended to use such tools. Exposing the Client ID and Client Secret to an online tool poses a serious security threat.
>
> A string is received that looks like `RjZEbjh5cGVtMWo4UDZzVXo4SVgzcG1Tc09BOTlHVVQ6QVNOa3c4S3F6MXQwV1hISw==`.

2. Call the [Token](../../oauth/http-docs/http-gettoken-POST.md) operation.

### Request

```
curl -v 'https://developer.api.autodesk.com/authentication/v2/token' \
  -X 'POST' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json' \
  -u 'YOUR_CLIENT_ID:YOUR_CLIENT_SECRET' \
  -d 'grant_type=client_credentials' \
  -d 'scope=application:service_account:read application:service_account:write application:service_account_key:write'

```

### Response

```
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 19 Mar 2025 13:40:11 GMT
Content-Type: application/json;charset=UTF-8
Content-Length: 965
Connection: keep-alive
Cache-Control: no-store
pragma: no-cache
strict-transport-security: max-age=31536000; includeSubDomains; preload
x-content-type-options: nosniff
X-Frame-Options: SAMEORIGIN
ratelimit-remaining: 499
ratelimit-value: 500

{
  "access_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IlhrUFpfSmhoXzlTYzNZS01oRERBZFBWeFowOF9SUzI1NiIsInBpLmF0bSI6ImFzc2MifQ.eyJzY29wZSI6WyJhcHBsaWNhdGlvbjpzZXJ2aWNlX2FjY291bnQ6cmVhZCIsImFwcGxpY2F0aW9uOnNlcnZpY2VfYWNjb3VudDp3cml0ZSIsImFwcGxpY2F0aW9uOnNlcnZpY2VfYWNjb3VudF9rZXk6d3JpdGUiXSwiY2xpZW50X2lkIjoicFlpbnpMRzBydGRHRWlqQklsRGFSNjMwWjB2V1FiMnZNTkY3cHFqMDZMSGRjVjBaIiwiaXNzIjoiaHR0cHM6Ly9kZXZlbG9wZXIuYXBpLmF1dG9kZXNrLmNvbSIsImF1ZCI6Imh0dHBzOi8vYXV0b2Rlc2suY29tIiwianRpIjoiam1YYVJ4RzlRN21PQzIzOXREcmdwbmpMYlJvaTVWQTNrZEpQemZ5b3gzODBuMHVEZHlBWVlyblFKRnBDZFRlYiIsImV4cCI6MTc0MjM5NTIxMX0.awBC4Tl2QiP7GCxVLvbK9gfL2QLjfdJGfayEar0Y_M0WlpRxMo-J9NRdv2wPtXq9l6pdr_1gupDJDbbhywfF6pCgxJQ6wSq4NFekjQTX3qNyK7ok0qHJY8zwyNYUehGstKzjUpOi_Rc9xyXnzP-PfPKEkZYrM2O1HIziYbmNYDx6AVgBVVdQ7XfS6LtQ5dHfvoiVVjH5R8j9_yehziCuhYuKvhOeBqgEmrGY6XODgpokzQCzjsErI7wIy1jzFidcI9MODcOkWrQ0c-gLJC5-nxOSiSOUGPqkYCFIQIYGJBaZ_Njal1Rxo71pGzi5aF8_SbuxEvy4NgPAuYZtjKQgGA",
  "token_type": "Bearer",
  "expires_in": 3599
}

```

Show More

This access token is now used to make calls to other API endpoints.

## [Step 2 - Create SSA](#step-2-create-ssa)

Call the [Create Service Account](../http-docs/http-ssa-create-service-account-POST.md) operation.

**Notes:**

- Use the access token obtained in [Step 1 - Get an Access Token](getting-started-with-ssa-task1-create-an-ssa.md).
- Base the SSA name on the guidelines provided in the [Naming Guidelines](../developers-guide-docs/naming-guidelines.md) Developer’s Guide topic.

### Request

```
curl -v 'https://developer.api.autodesk.com/authentication/v2/service-accounts' \
   -X 'POST' \
   -H 'Accept: application/json'  \
   -H 'Authorization: Bearer eyJh...'  \
   -H 'Content-Type: application/json' \
   -d '{
    "name": "service-mycompany-filesync",
    "firstName" : "service",
    "lastName" : "mycompany-filesync"
  }'

```

Show More

### Response

```
HTTP/1.1 201 Created

{
  "serviceAccountId":"6BNJQT7RR7GTJ5QY",
  "email":"service-mycompany-filesync@Ycw2Usv4XY38AfkvTIJTtEUVx8xNUORpJm31IILNtPvTXwGu.adskserviceaccount.com"
}

```

A system-generated email address is created for the SSA.

## [Step 3 - Create RSA private key](#step-3-create-rsa-private-key)

Call the [Create Keys](../http-docs/http-ssa-create-service-account-key-POST.md) operation.

**Note:** Use the access token obtained in [Step 1 - Get an Access Token](getting-started-with-ssa-task1-create-an-ssa.md).

### Request

```
curl -v 'https://developer.api.autodesk.com/authentication/v2/service-accounts/{serviceAccountId}/keys' \
   -X 'POST' \
   -H 'Authorization: Bearer eyJh...'

```

### Response

```
{
  "kid": "17ec4ec4-b733-4416-89ac-86f465b63f64",
  "privateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIIEow......\n-----END RSA PRIVATE KEY-----\n"
}

```

Note down the following values from the response:

- SSA email
- Service Account ID
- RSA private key
- Key ID

## [Code Sample](#code-sample)

The following code sample demonstrates how to create an SSA and RSA private key.

Install Python libraries and provide appropriate inputs before running the script.

```
# Install dependencies
# > pip install requests
import requests

# Configuration
APS_CLIENT_ID = "your_client_id"
APS_SECRET_ID = "your_client_secret"
FIRST_NAME = "service"                    # Service account first name
LAST_NAME = "mycompany-filesync"          # Service account last name
BASE_URL = "https://developer.api.autodesk.com/authentication/v2"
SCOPE_ADMIN = [
    "application:service_account:read",
    "application:service_account:write",
    "application:service_account_key:write"
]

# Get admin token using client credentials.
def get_admin_token():
    url = f"{BASE_URL}/token"
    data = {
        "grant_type": "client_credentials",
        "scope": " ".join(SCOPE_ADMIN)
    }
    response = requests.post(url, data=data, auth=(APS_CLIENT_ID, APS_SECRET_ID))
    response.raise_for_status()
    return response.json()["access_token"]

# Create a new service account with firstName, lastName, and concatenated name.
def create_service_account(admin_token):
    url = f"{BASE_URL}/service-accounts"
    headers = {"Authorization": f"Bearer {admin_token}"}
    payload = {
        "name": f"{FIRST_NAME}-{LAST_NAME}",
        "firstName": FIRST_NAME,
        "lastName": LAST_NAME
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        print("Error creating service account:", response.text)
    response.raise_for_status()
    return response.json()

# Create a key for the specified service account.
def create_service_account_key(admin_token, service_account_id):
    url = f"{BASE_URL}/service-accounts/{service_account_id}/keys"
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = requests.post(url, headers=headers)
    if response.status_code != 200:
        print("Error creating service account key:", response.text)
    response.raise_for_status()
    return response.json()

def main():
    admin_token = get_admin_token()
    account_data = create_service_account(admin_token)
    SSA_EMAIL = account_data["email"]
    SERVICE_ACCOUNT_ID = account_data["serviceAccountId"]
    key_data = create_service_account_key(admin_token, SERVICE_ACCOUNT_ID)
    KEY_ID = key_data["kid"]
    PRIVATE_KEY = key_data["privateKey"]

    print(f'''
APS_CLIENT_ID="{APS_CLIENT_ID}"
APS_SECRET_ID="{APS_SECRET_ID}"
SERVICE_ACCOUNT_ID="{SERVICE_ACCOUNT_ID}"
KEY_ID="{KEY_ID}"
SSA_EMAIL="{SSA_EMAIL}"
PRIVATE_KEY="{PRIVATE_KEY}"''')

if __name__ == "__main__":
    main()

```

Show More
