# introspect

Source: https://aps.autodesk.com/en/docs/oauth/v2/reference/http/introspect-POST/

---

Token

POST

# introspect

If the token is active, additional information is returned.

If the token is expired, invalid or revoked, it returns the response as `status: inactive`.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/authentication/v2/introspect |
| --- | --- |
| Data Format | Form encoding (request); JSON (response) |
| Rate Limit | 100 calls per minute |

## [Section 1 - For Public clients](#section-1-for-public-clients)

### Request

## [Headers](#headers)

| Content-Type*   string | Must be `application/x-www-form-urlencoded` |
| --- | --- |

* Required

### Request

## [Body Structure](#body-structure)

The request body is a URL-encoded string of ampersand-concatenated, name-value pairs of the following parameters:

| token*   string | The token to be introspected |
| --- | --- |
| client_id*   string | This field is only required for public clients |

* Required

### Response

## [Body Structure (200)](#body-structure-200)

| active   boolean | The status of this operation |
| --- | --- |
| scope   string | A URL-encoded, space-separated list of requested scopes |
| exp   string | Expiration timestamp of the token |
| client_id   string | The ID of the client associated with the token |

## [Example](#example)

### Request

```
curl -v 'https://developer.api.autodesk.com/authentication/v2/introspect'
     -X 'POST'
     -H 'Content-Type:application/x-www-form-urlencoded'
     -d '{
           'token=eyJraWQiOiJubkFKZm82T2lMRHhINXZkbDhBT0lQeVBpcjRLTEJsTUZEZzFXOEFMa3A0IiwiYWxnIjoiUlMyNTYifQ.
            eyJ2ZXIiOjEsImp0aSI6IkFULklSakNLM3VIZUdvQWtxVXRfTUtBdDV6RE1laUJBaUtlMURYb3pJck9jNGcub2Fyd2liYTly
            M2MyYUwxWW0waDYiLCJpc3MiOiJodHRwczovL2F1dG9kZXNrLXRlc3Qub2t0YXByZXZpZXcuY29tL29hdXRoMi9k
            ZWZhdWx0IiwiYXVkIjoiYXBpOi8vZGVmYXVsdCIsImlhdCI6MTYxMjk0OTM2MSwiZXhwIjoxNjEyOTUyOTYxLC
            JjaWQiOiIwb2F3djE4dzYzaTAzQ2dtWjBoNyIsInVpZCI6IjAwdXd2Nm05dm1jb1RNTE9GMGg3Iiwic2NwI
            jpbIm9mZmxpbmVfYWNjZXNzIiwib3BlbmlkIl0sInN1YiI6ImFrYXNodGVzdEBtYWlsaW5hdG9yLmNvbSJ9.
            CyxjzWiaxV1ybLGPsQPvjg5nUlb4pl6wnWvWp2Q_kNd8Z6o5-lvJWr2HyrJIG2Qtodb3RPz
            b0gc4lNue7oqXz8kQMECjgG62MZ31RBN_J98JSKvnCubWJAYmdITpbOSXGuUwEf1eB8FyHR-
            Wc6epk1rRT-ZoHMd42zCygmYKFDY_w2EDnxIvP-6lEfhz4fgT5mj5jOlomZJDrUfWEMO10Sjzs
            N7G5utuTh025EUpQza2JoI1baJun0jNR5eO-NhBHmGTJl8biHpd7gDfscVKmPQDeLoOgUda7hPiZXHbEuovr1_
            ybkr26k8ab24gVqVK9HIxsl3w8KKPw-CoBoO38A'\
            'client_id=0oawv18w63i03CgmZ0h7'
         }'

```

Show More

Note that line breaks have been added to the cURL command above for ease of reading.
Make sure to remove them before executing any code in your terminal.

### Response

## [Status - Active](#status-active)

```
{
  "active": true,
  "scope": "offline_access openid",
  "client_id": "0oawv18w63i03CgmZ0h7",
  "exp": 1612952961,
  "userid": "T8SLL89JABCK"
}

```

## [Status - Invalid](#status-invalid)

```
{
   "active": false
}

```

## [Status - Inactive](#status-inactive)

```
{
   "active": false
}

```

## [Section 2 - For Private clients](#section-2-for-private-clients)

### Request

## [Headers](#id5)

| Content-Type*   string | Must be `application/x-www-form-urlencoded` |
| --- | --- |
| Authorization*   string | Must be in the form Basic `${Base64(<client_id>:<client_secret>)}` |

* Required

### Request

## [Body Structure](#id7)

The request body is a URL-encoded string of ampersand-concatenated, name-value pairs of the following parameters:

| token*   string | The token to be introspected |
| --- | --- |

* Required

### Response

## [Body Structure (200)](#id9)

| active   boolean | The status of this operation |
| --- | --- |
| scope   string | A URL-encoded, space-separated list of requested scopes |
| client_id   string | The ID of the client associated with the token |
| exp   string | Expiration timestamp of the token |

## [Example](#id10)

### Request

## [JWT](#jwt)

```
curl -v 'https://developer.api.autodesk.com/authentication/v2/introspect'
     -X 'POST'
     -H 'Content-Type: application/x-www-form-urlencoded'
     -H 'Authorization: Basic RjZEbjh5cGVtMWo4UDZzVXo4SVgzcG1Tc09BOTlHVVQ6QVNOa3c4S3F6MXQwV1hISw==' \
     -d '{
           'token=eyJhbGciOiJSUzI1NiIsImtpZCI6IlpxUnVxc1hheWU5dmpIVTYyU2R6Y3N0anRDUFJkR0owIn0.
           eyJzY29wZSI6WyJ1c2VyOnJlYWQiXSwiY2xpZW50X2lkIjoiYWthc2h0ZXN0IiwiYXVkIjoiaHR0cHM6Ly
           9hdXRvZGVzay5jb20vYXVkL2Fqd3RleHA2MCIsImp0aSI6InczTjA5ZUloWWdWMnQwRDFueGxneGd6cW04
           UzRoN2d2aDhLZTM4VzZCa3QzOXhPbTRmRXZpbWIzZEhkODQ0TjAiLCJ1c2VyaWQiOiJFN0M5TjU1SFpXS0
           EiLCJleHAiOjE2MTI5NDk0NDN9.PCmyIn_My9C_4Srii_b5mCf0qPb9UIcxlQvhtc7aM_c76Ub4FoVm_
           wSSecgbe4KEU0B9QqDnPcW49M1Hg3-lgGAd-HkIolv_duFRi0f9l6Yqqd0RCyQR0-7sJHx9XvqoYW7sEYY7
           lQcjbeOAWLiw6ufoOzGXnad5SaK6lgVfnK5i7jELNp5UAtlk2Y-ULEH8cp-QB_NZGneTwmJYw72U5b7uY-
           wxrhIA0y-zZOXLTRIQDW9E_rhahRV51sT7mUn8ltQ8owRPFGkdkJ1YwkXIES6KN7QXjER2PQdc8q9G58Vz
           RAISYqxKioJV3uyds8cF87T6uWXgy2EQnc8QdDTmtA'
         }'

```

Show More

## [Reference token](#reference-token)

```
curl -v 'https://developer.api.autodesk.com/authentication/v2/introspect'
     -X 'POST'
     -H 'Content-Type: application/x-www-form-urlencoded'
     -H 'Authorization: Basic RjZEbjh5cGVtMWo4UDZzVXo4SVgzcG1Tc09BOTlHVVQ6QVNOa3c4S3F6MXQwV1hISw==' \
     -d '{
           'token=QNuvfgORVpUlbhaKvQZC6yhPF43p'
         }'

```

Note that line breaks have been added to the cURL command above for ease of reading.
Make sure to remove them before executing any code in your terminal.

### Response

## [Status - Active](#id13)

```
{
  "active": true,
  "scope": "user:read",
  "client_id": "0oawv18w63i03CgmZ0h7",
  "exp": 1612949443,
  "userid": "T8SLL89JABCK"
}

```

## [Status - Invalid](#id14)

```
{
   "active": false
}

```

## [Status - Inactive](#id15)

```
{
   "active": false
}

```

### Response

List of errors

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Successful request; information of token returned. |
| --- | --- |
| 400   Invalid Request | The request is missing a required parameter âtokenâ. |
| 400   Invalid Request | The âclient_idâ is not supported in the request body when Authorization headers are present. |
| 401   Invalid credentials | The client credentials are invalid. |
| 500   Internal Server Error | Generic internal server error. |
