# Error Handling

Source: https://aps.autodesk.com/en/docs/tokenflex/developers_guide/error_handling/

---

# Error Handling

## [Authentication Errors](#authentication-errors)

Authentication errors are typically indicated by a 4xx HTTP status code in the response header. The response body provides details of the error that occurred. The body structure of the error response for authentication errors is as below:

| developerMessage   string | A short explanation, typically meant to assist diagnose the cause of the error. |
| --- | --- |
| userMessage   string | A short, generic description of the error, meant for an end-user audience. |
| errorCode   string | A code that identifies the error type. |
| more info   string | A URL to a location that provides more information about the occurrence of the error. |

### Example

```
{
  "developerMessage":"The client_id specified does not have access to the api product",
  "userMessage":" ",
  "errorCode":"AUTH-001",
  "more info":"http://developer-stg.api.autodesk.co/documentation/v1/errors/AUTH-001"
}

```

## [List of Authentication Error Codes](#list-of-authentication-error-codes)

| Error Code | Description |
| --- | --- |
| AUTH-001 | The `client_id` is not authorized to access the specified API. |
| AUTH-002 | The `client_id` is not authorized to access the specified endpoint. |
| AUTH-003 | The `client_secret` does not match the client_id `client_id`. |
| AUTH-004 | One or more requested scopes are invalid. |
| AUTH-005 | The token has been rejected. The given ID does not match the User’s ID that authorized the token. |
| AUTH-006 | The access token is invalid. |
| AUTH-007 | The `Content-Type` header is missing or specifies a value other than `application/x-www-form-urlencoded`. |
| AUTH-008 | The request is missing one or more required parameters. |
| AUTH-009 | Unsupported `grant_type` specified. The `grant_type` must be `client_credentials`. |
| AUTH-010 | Token does not have the privilege for this request. |
| AUTH-011 | The `grant_type` is invalid for the corresponding endpoint. |
| AUTH-012 | The `Authorization` header is missing or invalid. |
| AUTH-013 | Unsupported `token_hint_type` specified. The `token_hint_type` must be `refresh_token`. |
| AUTH-016 | Invalid input found for query parameter `prompt`. The valid value must be `login`. |
| ERR-001 | Rate limit of this API request is exceeded. Retry after some time. |
| ERR-003 | Generic internal server error. |
| ERR-004 | Your trial period has expired. |
| ID-AUTH-005 | The token has been rejected. The given ID does not match the User’s ID that authorized the token. |
| ID-GE-004 | The application encountered an unexpected error. |
| ID-GE-005 | Unsupported media type. |
| ID-GE-006 | Invalid input. The input passed to the API was either null, empty or not of the expected type. |
| ID-GE-009 | User does not exist in the system. |
| ID-GE-011 | Invalid characters found in the input data. This will come user enters firstname or lastname within <script> tag. |
| ID-GP-001 | The Group does not exist in the system. TenantId or GroupId is wrong. |
| ID-GP-007 | The user cannot be found in the system. |
| ID-GP-014 | The value of user status is invalid. Allowed values are ‘enabled’, ‘disabled’, and ‘all’. |
| ID-GP-018 | The user is not included in any group. |
| ID-TN-020 | The domain name is already associated with other master tenant. |
| ID-UU-002 | The first name field was too long. The first name is longer than the maximum of 75 characters or 128 bytes in UTF-8 encoding. |
| ID-UU-003 | The first name field contains invalid characters.This error will occur only if user enters special characters. |
| ID-UU-004 | The first name should contain at least one alphanumeric character. |
| ID-UU-005 | The last name field was empty. |
| ID-UU-006 | The last name field was too long. The last name is longer than the maximum of 75 characters or 128 bytes in UTF-8 encoding. |
| ID-UU-007 | The last name field contains invalid characters. |
| ID-UU-008 | The last name should contain at least one alpha numeric character.This error will occur only if user enters special characters. |
| ID-UU-025 | The postal code field was too long. Maximum allowed length is 16. |
| ID-UU-026 | The postal code is invalid. |
| ID-UU-036 | The company field was too long. Maximum allowed length is 50. |
| ID-UU-037 | The job title field was too long. Maximum allowed length is 50. |
| ID-UU-040 | The country code is invalid. |
| ID-UU-064 | The website URL was too long. Maximum allowed length is 255. |
| ID-UU-067 | The website URL contains invalid characters. |
| ID-UU-070 | The website URL was not in a valid URL format. |
| ID-UUT-006 | User with given userid does not exist in the system. |
| ID-UUT-007 | Service with given service trial name does not exist in the system. |
| ID-UUT-011 | The service is not enabled for trial. |
| ID-UUT-012 | Trial is already enabled for user. |
| ID-UUT-013 | Trial is already disabled for the user. |
| ID-UUT-014 | Trial is not enabled for user. |
| ID-UUT-015 | The trial is already available as free trial. |
| ID-UUT-016 | Trial has expired for the user. |
| ID-UUT-020 | The trial does not support User Type as ‘enthusiast’. |
| ID-UUT-021 | Trial Modification does not work for users identified as student. |
| ID-UUT-022 | Maximum number reached for user trial extension. |
| ID-UI-001 | The user is not allowed to perform this action. |
| ID-UI-002 | The return URL was too long. The maximum allowed length is 255. |
| ID-UI-003 | The return URL field is invalid. |
| ID-UI-004 | The return URL is not trusted. |
| ID-UI-005 | The invitedby field is empty. |
| ID-UI-006 | The inviting user does not exist in the system. |
| ID-UI-007 | The inviting user cannot be a child user. |
| ID-UI-008 | The inviting user cannot be a provisioned user. |
| ID-LU-002 | LDAP user already exists. |
| ID-TN-019 | Invalid consumer key for master tenant. |
| ID-TN-036 | The tenant has been deleted from the system. |
| ID-CU-004 | Identity with name already exists. |
| ID-CU-005 | The first name field is empty. |
| ID-CU-006 | The first name field was too long. The first name is longer than the maximum of 75 characters or 128 bytes in UTF-8 encoding. |
| ID-CU-007 | The first name field contains invalid characters. For example: ufffd |
| ID-CU-008 | The first name should contain at least one alpha numeric character. |
| ID-CU-009 | The last name field is empty. |
| ID-CU-010 | The last name field was too long. The last name is longer than the maximum of 75 characters or 128 bytes in UTF-8 encoding. |
| ID-CU-011 | The last name field contains invalid characters. For example: ufffd |
| ID-CU-012 | The last name should contain at least one alpha numeric character. |
| ID-CU-013 | The email id field is empty. |
| ID-CU-014 | The email id provided is invalid. |
| ID-CU-015 | The email already exists in the system. |
| ID-CU-016 | The email id field contains invalid characters. For example, [&^&^&^abc@uffabcfd.com](mailto:&^&^&^abc%40uffabcfd.com) |
| ID-CU-025 | The country code is invalid |
| ID-CU-029 | Identity with display name already exists |
| ID-CU-064 | The first name field contains invalid words. For example: admin, autodesk etc |
| ID-CU-065 | The last name field contains invalid words. For example: admin, autodesk etc |
| ID-CU-069 | Invalid Language |

## [HTTP Status Response Codes](#http-status-response-codes)

APS services use standard HTTP status response codes in the response header to indicate whether a request completed successfully or not. A 2xx type response indicates success. A 4xx type response indicates a failure in handling a request. For example, an error caused by a request containing an invalid parameter. A 5xx type response usually indicates an internal server error.

| Status Code | Description |
| --- | --- |
| 200 | The request has succeeded. |
| 201 | The request has been fulfilled and has resulted in one or more new resources being created. |
| 202 | The request has been accepted for processing, but the processing has not been completed. |
| 204 | The server has successfully fulfilled the request, there is no additional content to send in the response payload body. |
| 207 | A Multi-Status response conveys information about multiple resources in situations where multiple status codes might be appropriate. |
| 304 | There was no new data to return. Typically used to indicate that the cached version of the response is still valid. |
| 400 | The request was invalid or cannot be otherwise served. Typical when there is a syntax error in the request. The response payload body provides further details of the error. |
| 401 | Missing or incorrect authentication credentials. |
| 403 | The request is understood, but it has been refused or access is not allowed. The response payload body provides further details of the error. |
| 404 | The requested resource does not exist. Sometimes, when it is prudent to hide the existence of a resource from an unauthorized client, a 403 error may be generated instead of this error. |
| 406 | An invalid format is specified in the request. |
| 429 | The application’s rate limit for the resource has been exhausted. |
| 500 | Something is broken. This is usually a temporary error, for example in a high load situation or if an endpoint is temporarily having issues. |
| 502 | API is down, or being upgraded. |

## [Token Flex Usage Data API Errors](#token-flex-usage-data-api-errors)

Token Flex Usage Data API errors are typically indicated by a 4xx HTTP status code in the response header. The JSON payload body may provide details of the error that occured. The body structure of the error response payload generated by a bad request is as below:

| Code   string | A code that identifies the error type. |
| --- | --- |
| Message   string | A short, human readable explanation of the error. |

### Example 1

JSON payload for a HTTP status code 400 error:

```
{
    "Code": "BadRequestError",
    "Message": "BadRequestError: Invalid request"
}

```

### Example 2

JSON payload for a HTTP status code 403 error:

```
{
    "Code": "ForbiddenError",
    "Message": "ForbiddenError: Invalid contract or access level"
}

```
