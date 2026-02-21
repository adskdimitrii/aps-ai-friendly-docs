# JWKS

Source: https://aps.autodesk.com/en/docs/oauth/v2/reference/http/asymmetrickeys-GET/

---

Token

GET

# JWKS

Retrieves the list of public keys in the JWKS format (JSON Web Key Set). A public key is used to validate the asymmetric JWT signature of an OAuth 2.0 access token by an authorizing end user in both two-legged & three-legged context. From the list of keys returned in the response, identify the key to be used to validate a given token using the tokenâs kid (key ID) parameter.

Note: Refer to [asymmetric JWT encryption](/en/docs/oauth/v2/developers_guide/asymmetric-encryption), [key rotation](/en/docs/oauth/v2/developers_guide/asymmetric-encryption/#key-rotation) and [validate access token](/en/docs/oauth/v2/developers_guide/asymmetric-encryption/#validate-access-token) for more information.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/authentication/v2/keys |
| --- | --- |
| Required OAuth Scopes | *none* |
| Data Format | JSON |

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful request; user profile returned. |
| --- | --- |
| 500   Internal Server Error | Generic internal server error. |

### Response

## [Body Structure (200)](#body-structure-200)

The response body for a successful call is a flat JSON object with the following attributes:

| kid   string | Key ID |
| --- | --- |
| kty   string | Cryptographic algorithm family for the certificateâs Key pair. Valid Value: `RSA` |
| use   string | The use of the key. Valid Value: `sig` |
| n   string | RSA modulus value |
| e   string | RSA exponent value |

## [Example](#example)

Successful retrieval of the list of public keys (200)

### Request

```
curl -v 'https://developer.api.autodesk.com/authentication/v2/keys' \
     -X 'GET' \

```

### Response

```
HTTP/1.1 200 OK
Cache-Control: max-age=604800
Content-length: 438
Content-Type: application/json;charset=UTF-8
Date: Thu, 08 Oct 2020 06:09:30 GMT

{
  "keys": [
    {
      "kty": "RSA",
      "kid": "aah541xk44m0V6ZX1H9dTUTvqk1p7yfQ",
      "use": "sig",
      "n": "ycSJdq-vSSGhbZFuDO94t0zHI7p9ybZBFKTGR6zntx0YduwhxPHP72wdiZgCz88i2w8AhljbKGgn8UrMQtIrVs8JXMmDen_
           aGsgWoCBIzJc3fc7WSm_kZb0AokVeJio6tPJGFhOJrzSgG2BUktILh0CYWNXS54Qb8EUcrhmo6YOQ5onR3_
           LLXJ2yOnwHe1FLnZuprav-yNQYMcAvaK9IRwgZWE7Fqt7dFaoiG1K9A_SD0l5rano5CjSrdqBk90pO8Xlju_
           KXjpeNcPZmEVr3DJBzSfFE__6ss-pagnRe-FMqzYCPOQSo5tqjIzwad4aftnTtZpEQcjpM3L0vP_rriQ",
      "e": "AQAB"
    },

    {
     "kty" "RSA",
     "kid": "ZqRuqsXaye9vjHU62SdzcstjtCPRdGJ0",
     "use": "sig",
     "n": "i7ZOaqOmEgqz9RFUkv7mLTWpqwSoiqqTZCVTC7_xWq0w7a4m7l63nDRRsmdfA6S-7UEHbvMHsi9hqBoPdjOSutqeK5FgOhRc_
     swovMecrooOwNVUBAc0NS4cX5dcrOaqZfJShwF4Nk0ko-EUUbBNM0s2x0j4YvfjXqpIXb_yc7bfyH4H_
     MGVb4ddgWtqHxdSlqNMMOBDKsjZzlnr8tf20gDnMMjn_f3zNb-zX4p4il0lytStrzGdZXy7ZCBVkvoZmMzg-
     RIW4tzbPHPYakgNmKYfLibiu6CjV-L6cvS8NHgySeKQ87tlEw8jAuzyUEQjIQl3Rr84wpvvBoT0EtzEBQ",
     "e": "AQAB"
   }
   ]
 }

```

Show More
