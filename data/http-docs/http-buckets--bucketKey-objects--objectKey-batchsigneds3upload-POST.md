# buckets/:bucketKey/objects/batchsigneds3upload

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-batchsigneds3upload-POST/

---

Objects

POST

# buckets/:bucketKey/objects/batchsigneds3upload

Requests a batch of S3 signed URL with which to upload multiple objects or chunks of multiple objects.

As with the Batch Get Download URL equivalent, the requests within the batch are evaluated independently and individual requests can be rejected even if the overall request returns a 200 response code, the signed URL/s returned by this endpoint will expire after 2 minutes as default (** longer expiration times can be set using the minutesExpiration param up to 60 minutes). S3 evaluates the validity of a URL when it first receives the headers / query parameters of the request; if it evaluates the signed URL to be valid, the actual data transfer can take any amount of time past 2 minutes. If the upload fails after 2 minutes have occurred, you can call this endpoint again to request new signed URL/s. When requesting new signed URLs for a multipart upload, you must provide the same uploadKey provided in the response to the original request; otherwise, OSS cannot know how to associate the new chunks with the old ones.

You can request a maximum of 25 URLs in a single request.

You can successfully call the batch upload endpoint if you are managing your own OSS buckets (e.g. you are the bucket creator)

** DISCLAIMER When generating signed URLs, itâs important to use the smallest possible expiration time, in order to avoid longer access in case of exposure of the URL.

## [Resource Information](#resource-information)

| Method and URI | POST https://developer.api.autodesk.com/oss/v2/buckets/:bucketKey/objects/batchsigneds3upload |
| --- | --- |
| Authentication Context | user context optional |
| Required OAuth Scopes | `data:write` `data:create` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be âBearer `<token>`â, where `<token>` is obtained via [POST token](/en/docs/oauth/v2/reference/http/gettoken-POST). |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

| bucketKey*   string | The URL-encoded name/key of the bucket containing the object for which to complete the upload |
| --- | --- |

* Required

### Request

## [Query String Parameters](#query-string-parameters)

| useAcceleration   boolean | Whether or not to generate an accelerated signed URL (ie: URLs of the form â¦s3-accelerate.amazonaws.comâ¦ vs â¦s3.amazonaws.comâ¦). When not specified, defaults to true. Providing non-boolean values will result in a 400 error. |
| --- | --- |
| minutesExpiration   integer | The custom expiration time within the 1 to 60 minutes range, if not specified, default is 2 minutes. |

### Request

## [Body Structure](#body-structure)

| requests*   array: object | An array of objects, each of which represents an upload to complete. See requests object structure. |
| --- | --- |

* Required

## [Requests object Structure](#requests-object-structure)

| objectKey*   string | The key/name of the object for which to create an S3 upload URL. If neither the âpartâ nor âpartsâ attribute is provided, OSS will return a single upload URL with which to upload the entire object. |
| --- | --- |
| firstPart   integer | The index of an individual part for which to retrieve a chunk upload URL. |
| parts   integer | For a multipart upload, the number of chunk URLs to return. If X is provided, the response will include chunk URLs from 1 to X. If none provided, the response will include only a single URL with which to upload an entire object. |
| uploadKey   string | The identifier of a previously-initiated upload, in order to request more chunk upload URLs for the same upload. This must match the uploadKey returned by a previous call to this endpoint where the client requested more than one part URL. |

* Required

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK |  |
| --- | --- |
| 400   BAD REQUEST | The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. |
| 401   UNAUTHORIZED | The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify Authentication and try again. |
| 403   FORBIDDEN | The Authorization was successfully validated but permission is not granted. Donât try again unless you solve permissions first. |
| 404   NOT FOUND | The bucket does not exist. |
| 429   RATE-LIMIT EXCEEDED | The maximum number of API calls that an app can make per minute was exceeded. |
| 500   INTERNAL SERVER ERROR | Internal failure while processing the request, reason depends on error |

### Response

## [Body Structure (200)](#body-structure-200)

| results   object | A map of the returned results; each key in the map corresponds to an object key in the batch, and the value includes the results for that object. See results object structure |
| --- | --- |

## [Results object Structure](#results-object-structure)

| uploadKey   string | The identifier of the upload session, to differentiate multiple attempts to upload data for the same object. This must be provided when re-requesting chunk URLs for the same blob if they expire, and when calling the Complete Upload endpoint. |
| --- | --- |
| uploadExpiration   string | Time Stamp representing the upload abort date for which all parts must be uploaded for the object and the complete upload endpoint must be called. |
| urlExpiration   string | Time Stamp representing the expiration of the generated signed URLs. Note that when multiple parts/URLs are requested, there is a chance that this time stamp does not represent the expiration of all URLs in the group. Consider this expiration a very close approximation of the expiration of the URLs in the group |
| urls   array: string | An array of signed URLs. For a single-part upload, this will only include a single URL. For a multipart upload, there will be one for each chunk of a multipart upload. The index of the URL in the array corresponds to the part number of the chunk. |
| status   string | Appears when object is in error state |
| reason   string | Accompanies error state for the object and describes the error encountered |

## [Example 1](#example-1)

Basic Request for 3 objects (200).

### Request

```
curl -X POST
  -H 'Authorization: Bearer {YOUR_TOKEN}'
  -H 'Content-Type: application/json'
  --data-raw '{
      "requests":[
        {
          "objectKey":"testbatch01.txt"
        },
        {
          "objectKey":"testbatch02.txt"
        },
        {
          "objectKey":"testbatch03.txt"
        }
      ]
    }'
  'https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/batchsigneds3upload'

```

Show More

### Response

```
{
  "results": {
    "testbatch01.txt": {
      "uploadKey": "{UPLOAD_KEY_1}",
      "uploadExpiration": "2021-09-04T00:00:00Z",
      "urlExpiration": "2021-09-02T18:01:26Z",
      "urls": [
        "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/cb2b4dc1-efd5-485a-a96c-c4ae3da968b6?uploadId=EB0BRf_9GiHg3AJbIppFnIUrTkFtpQqaLviRvDl7LkgA.u3.fRyv4UFR9S03xSYA2zCxpTLSwy82B29fA56CG4Khij1YsT_qOAOI3XVyZkO4wxUOt3bdnkX.Wt9IJ7GDmzW.gW.dF41cLymm2jnTfQ--&partNumber=1&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCICzziJFVpJJaq%2B5YOdNHRrR%2B0d9llx4VJBPeqOBQxIRiAiBwj%2Fx568QpyK5MCNeGmYgk%2BFUPFw894lwwiJuEYscUmCr6AwgaEAAaDDczNTIyMTAwNDg5NSIMSa2IRHeLEPYR1CXfKtcDt7qri4HAV6fuIfkRRc9os7DTixmhVrcdScYHpQcugBeFjzbKduPsUi3SUdfU8QNAu5I1LtuLSAKpXaG9kD%2BAK%2BtxiLZndT%2B3vwIdQgR19P5nII9MJYC0uzPW25T46N7W8aOEjTCRVARjpFY%2B6xvda5tVqIglaiRP4u%2FPRZSgnBLj5uOzV8K52MyzNoCj1IA5N%2FAkP5F21YiCdiCsmE2kaArYg4OAx1oduBDrUjcwgp%2BPQZfR%2FQM2aDA2IRIyLrQnWGN8HdHWEgTnPR%2FIQ5a5jMQW%2F0h%2B28th341XlRdfNTz%2BF3T3CQHt4cUnBCuOGm5auorCO%2FEMnS%2F9lpL5KF9Fy8V8n2EelA0m9TeRPXEh8lO2UigZufBR7WDemH%2Bx99KZEOtVWlP9lZMK%2FnGbegoJWY5tpLbGOkPBWvPnYHoitHDwiPOWKhdfnL7szjC8z2HeWIfmvRUg54oScBKMc9ijD1XANEz4rTVftpOZlAY9g3L%2B%2FIv2t8vemHebnYlpQlF1Rmu28Hgqz9VWj2hwBURrRJwoRXys5qmR7GggwfSaR2keOUUVGA9ryslMmIbM9sAHOMresXyTtY6eV08UYovs8Kcb9o5gTOvpuAygUDYXw2AlwWmIIRvmMLD2w4kGOqYB78qTOQRFBixpjD3jKnDioO7pqC4mY95WSJayppI1D4sX1MhMZCctvZHNmoPpCBZSYzp9se7At48TEY5ave8Sa6T0coTEhEfnpzop01llqWDCxan%2BwGscDWZ1WDdwA%2FtWCfyE1NEbXP7%2FgagbsFT8PFb2%2BhLhmt1EmU7jhfY7uAapLz5QzfO9wKkgp2yQbQ4eGZA1Ahq3nIugLiJC0Ddd55%2BUoynDyg%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210902T180027Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=00e003b267eba402bd4bcb37d72164910360b6f0ad0e5da0e7bc4ee4d7f44f0b"
      ]
    },
    "testbatch02.txt": {
      "uploadKey": "{UPLOAD_KEY_2}",
      "uploadExpiration": "2021-09-04T00:00:00Z",
      "urlExpiration": "2021-09-02T18:01:26Z",
      "urls": [
        "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/ecd06570-36ce-4261-9c46-e5cb8d61a5d2?uploadId=Ep9b5hNlWKEbsEaR6MZDKn_W0V3dSkHRim49sy0QIOoAV3ENMcq_2HlgRrsEaoTxW6Sc0wdhZgDOdiTO09Q31YDWR.BV6E0MQKeA9Kl4POGS02tQkQ_Cn5ThJk18P0rps2nyl5PQXxpJLjWFkDgCcw--&partNumber=1&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCICzziJFVpJJaq%2B5YOdNHRrR%2B0d9llx4VJBPeqOBQxIRiAiBwj%2Fx568QpyK5MCNeGmYgk%2BFUPFw894lwwiJuEYscUmCr6AwgaEAAaDDczNTIyMTAwNDg5NSIMSa2IRHeLEPYR1CXfKtcDt7qri4HAV6fuIfkRRc9os7DTixmhVrcdScYHpQcugBeFjzbKduPsUi3SUdfU8QNAu5I1LtuLSAKpXaG9kD%2BAK%2BtxiLZndT%2B3vwIdQgR19P5nII9MJYC0uzPW25T46N7W8aOEjTCRVARjpFY%2B6xvda5tVqIglaiRP4u%2FPRZSgnBLj5uOzV8K52MyzNoCj1IA5N%2FAkP5F21YiCdiCsmE2kaArYg4OAx1oduBDrUjcwgp%2BPQZfR%2FQM2aDA2IRIyLrQnWGN8HdHWEgTnPR%2FIQ5a5jMQW%2F0h%2B28th341XlRdfNTz%2BF3T3CQHt4cUnBCuOGm5auorCO%2FEMnS%2F9lpL5KF9Fy8V8n2EelA0m9TeRPXEh8lO2UigZufBR7WDemH%2Bx99KZEOtVWlP9lZMK%2FnGbegoJWY5tpLbGOkPBWvPnYHoitHDwiPOWKhdfnL7szjC8z2HeWIfmvRUg54oScBKMc9ijD1XANEz4rTVftpOZlAY9g3L%2B%2FIv2t8vemHebnYlpQlF1Rmu28Hgqz9VWj2hwBURrRJwoRXys5qmR7GggwfSaR2keOUUVGA9ryslMmIbM9sAHOMresXyTtY6eV08UYovs8Kcb9o5gTOvpuAygUDYXw2AlwWmIIRvmMLD2w4kGOqYB78qTOQRFBixpjD3jKnDioO7pqC4mY95WSJayppI1D4sX1MhMZCctvZHNmoPpCBZSYzp9se7At48TEY5ave8Sa6T0coTEhEfnpzop01llqWDCxan%2BwGscDWZ1WDdwA%2FtWCfyE1NEbXP7%2FgagbsFT8PFb2%2BhLhmt1EmU7jhfY7uAapLz5QzfO9wKkgp2yQbQ4eGZA1Ahq3nIugLiJC0Ddd55%2BUoynDyg%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210902T180027Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=d8fdcfd6e7c2d38cb304d7dc7a92d9ebbac99879b6434e23d5097577687cd16f"
      ]
    },
    "testbatch03.txt": {
      "uploadKey": "{UPLOAD_KEY_3}",
      "uploadExpiration": "2021-09-04T00:00:00Z",
      "urlExpiration": "2021-09-02T18:01:26Z",
      "urls": [
        "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/3c3d3fc2-1550-4c45-871d-20be74a5b41d?uploadId=PnJ4woE85386r2fqn447Rw7PSzhyY5LIRkutENAsAjq9eb6fBbwr.1iJSot.t3dS4UShLG4DUcF9Vy8LUiZDLku5kOmmw7w1mb.u5fWOS.tvAuif_8fhPVn3C60297zyPuq_E.J4qAo1Fcs_RLk.aQ--&partNumber=1&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCICzziJFVpJJaq%2B5YOdNHRrR%2B0d9llx4VJBPeqOBQxIRiAiBwj%2Fx568QpyK5MCNeGmYgk%2BFUPFw894lwwiJuEYscUmCr6AwgaEAAaDDczNTIyMTAwNDg5NSIMSa2IRHeLEPYR1CXfKtcDt7qri4HAV6fuIfkRRc9os7DTixmhVrcdScYHpQcugBeFjzbKduPsUi3SUdfU8QNAu5I1LtuLSAKpXaG9kD%2BAK%2BtxiLZndT%2B3vwIdQgR19P5nII9MJYC0uzPW25T46N7W8aOEjTCRVARjpFY%2B6xvda5tVqIglaiRP4u%2FPRZSgnBLj5uOzV8K52MyzNoCj1IA5N%2FAkP5F21YiCdiCsmE2kaArYg4OAx1oduBDrUjcwgp%2BPQZfR%2FQM2aDA2IRIyLrQnWGN8HdHWEgTnPR%2FIQ5a5jMQW%2F0h%2B28th341XlRdfNTz%2BF3T3CQHt4cUnBCuOGm5auorCO%2FEMnS%2F9lpL5KF9Fy8V8n2EelA0m9TeRPXEh8lO2UigZufBR7WDemH%2Bx99KZEOtVWlP9lZMK%2FnGbegoJWY5tpLbGOkPBWvPnYHoitHDwiPOWKhdfnL7szjC8z2HeWIfmvRUg54oScBKMc9ijD1XANEz4rTVftpOZlAY9g3L%2B%2FIv2t8vemHebnYlpQlF1Rmu28Hgqz9VWj2hwBURrRJwoRXys5qmR7GggwfSaR2keOUUVGA9ryslMmIbM9sAHOMresXyTtY6eV08UYovs8Kcb9o5gTOvpuAygUDYXw2AlwWmIIRvmMLD2w4kGOqYB78qTOQRFBixpjD3jKnDioO7pqC4mY95WSJayppI1D4sX1MhMZCctvZHNmoPpCBZSYzp9se7At48TEY5ave8Sa6T0coTEhEfnpzop01llqWDCxan%2BwGscDWZ1WDdwA%2FtWCfyE1NEbXP7%2FgagbsFT8PFb2%2BhLhmt1EmU7jhfY7uAapLz5QzfO9wKkgp2yQbQ4eGZA1Ahq3nIugLiJC0Ddd55%2BUoynDyg%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210902T180027Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=5987bab2c4e97713a246cce60ab4291ab213df0dd413fd0c46b42f851e97f874"
      ]
    }
  }
}

```

Show More

## [Example 2](#example-2)

Get Upload URLs for additional parts with uploadKey specified (200).

### Request

```
curl -X POST
  -H'Authorization: Bearer {YOUR_TOKEN}' \
  -H'Content-Type: application/json' \
  --data-raw '{
    "requests": [
      {
        "objectKey": "testbatch01.txt",
        "parts": 2,
        "firstPart": 2,
        "uploadKey": "{UPLOAD_KEY}"
      },
      {
        "objectKey": "testbatch02.txt",
        "parts": 3,
        "firstPart": 4,
        "uploadKey": "{UPLOAD_KEY}"
      },
      {
        "objectKey": "testbatch03.txt",
        "parts": 1,
        "uploadKey": "{UPLOAD_KEY}"
      }
    ]
  }'
'https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/batchsigneds3upload' \

```

Show More

### Response

```
{
  "results": {
    "testbatch01.txt": {
      "uploadKey": "{UPLOAD_KEY}"
      "uploadExpiration": "2021-09-10T00:00:00Z",
      "urlExpiration": "2021-09-08T17:54:09Z",
      "urls": [
        "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/9e2b0465-e301-49cd-8cb7-87deadfe74fd?uploadId=t_ulGuqkBRf.qM0OMLAD3ruXW3UV7XPJWWEc6RlM8JHp33fZqzr0u2id9Rqp3hrbTySEU9yXK74Z1Vv8OnuugW0bOHqsh8F6PNtd1wYZ6gXV.muHUEMFJJ7.kdPmShYT.7BQqr0UybcpHueQLRBdcg--&partNumber=2&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLWVhc3QtMSJGMEQCIE2FGHeC8zrputJkxBO8P9zTvrMYQJnGLuTOD2DjBTBzAiAf20aup8ZrXuQtS%2FD2Tp3i2ziKartriVp3RkiwIhIMxyqDBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDczNTIyMTAwNDg5NSIM9yHJCBzAgcUbR83nKtcD9snWn%2F5z57rdc14R0j%2BIRu%2Bop8lFu7byed7QbW5gcQ9bLTdQNZXVLPrvvUGozLVdH%2FNVNll%2FGUZ4%2BYRGe3fl%2BdYBJFy4RPyFY4H0%2Fxn98VtTpVH3KkJw7Z1CIYfGIp9%2B1th1fUSt7lAHIKcVxYlBYkjHQks4Elt0xlV%2Fg5qHaeSxZhdoFkllXcyjVPnvBHc1khlYdZcUCXk5WWEYdujCxdPFIQm%2BsNzLrS5U1gLNeRYDBjy3fB4jT47EMMoTm1YbCh0rCzeaxv98YV5I1i2NecYl0N%2BPk973%2FQxU6pG9Y%2F1N1aHXcG%2FDAxWWn%2BGV2caGqMqXgUa7ubhHbEkmHmXQ8VnguvhaRwkLVUWclAVVMTHe232t0YWeeS55TN53%2BIGHeQRRxLFr6j0uydAiPruSHgsNnA7QSbaMaZC245UZZ1hfSoRVKPTp2LRJ62qvP%2BoTC3m8KJ0Yc3lLBw%2BmFR6Q5ooace9OcfGIuouowm327nsLDBK2W6tDmI32zWBb8foJWJpzkUXBbB%2FkZjvAbhzU8aOF9u6yVWv1QFw%2BjR5OVX%2FiQWqBKwlXaZloq4ghHzn9u54OemqRWiOf3tnciWrJzSBEBi%2BEqHa1zq70JCiZHZzMwiled%2BaOMP7L44kGOqYBeVnCwBNFIFAR0sdeXSr26zfZh5LEZZo5gWICI6m3MMxPa%2BqUuDyxdD%2FSwhIZ0lw%2FbaiAwiDWXDxH%2BhfQJTcrzgXvottrU%2BxZZFEEQ%2FzUwV6u839Nyc%2FCIulapfSXCjtr52SXvdfOUh1W79JWnhtxWH1u8DyoUE7yF4CpbSLjk4dIoJ0N2MBQawI5Q0icjGm4FdpnP5FQE8H%2FivdYHK74rLiaKWgU7Q%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210908T175310Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=3bbd115516618b9249a7441aa1787c4e9638c96aab536934651814725d0c38a5",
        "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/9e2b0465-e301-49cd-8cb7-87deadfe74fd?uploadId=t_ulGuqkBRf.qM0OMLAD3ruXW3UV7XPJWWEc6RlM8JHp33fZqzr0u2id9Rqp3hrbTySEU9yXK74Z1Vv8OnuugW0bOHqsh8F6PNtd1wYZ6gXV.muHUEMFJJ7.kdPmShYT.7BQqr0UybcpHueQLRBdcg--&partNumber=3&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLWVhc3QtMSJGMEQCIE2FGHeC8zrputJkxBO8P9zTvrMYQJnGLuTOD2DjBTBzAiAf20aup8ZrXuQtS%2FD2Tp3i2ziKartriVp3RkiwIhIMxyqDBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDczNTIyMTAwNDg5NSIM9yHJCBzAgcUbR83nKtcD9snWn%2F5z57rdc14R0j%2BIRu%2Bop8lFu7byed7QbW5gcQ9bLTdQNZXVLPrvvUGozLVdH%2FNVNll%2FGUZ4%2BYRGe3fl%2BdYBJFy4RPyFY4H0%2Fxn98VtTpVH3KkJw7Z1CIYfGIp9%2B1th1fUSt7lAHIKcVxYlBYkjHQks4Elt0xlV%2Fg5qHaeSxZhdoFkllXcyjVPnvBHc1khlYdZcUCXk5WWEYdujCxdPFIQm%2BsNzLrS5U1gLNeRYDBjy3fB4jT47EMMoTm1YbCh0rCzeaxv98YV5I1i2NecYl0N%2BPk973%2FQxU6pG9Y%2F1N1aHXcG%2FDAxWWn%2BGV2caGqMqXgUa7ubhHbEkmHmXQ8VnguvhaRwkLVUWclAVVMTHe232t0YWeeS55TN53%2BIGHeQRRxLFr6j0uydAiPruSHgsNnA7QSbaMaZC245UZZ1hfSoRVKPTp2LRJ62qvP%2BoTC3m8KJ0Yc3lLBw%2BmFR6Q5ooace9OcfGIuouowm327nsLDBK2W6tDmI32zWBb8foJWJpzkUXBbB%2FkZjvAbhzU8aOF9u6yVWv1QFw%2BjR5OVX%2FiQWqBKwlXaZloq4ghHzn9u54OemqRWiOf3tnciWrJzSBEBi%2BEqHa1zq70JCiZHZzMwiled%2BaOMP7L44kGOqYBeVnCwBNFIFAR0sdeXSr26zfZh5LEZZo5gWICI6m3MMxPa%2BqUuDyxdD%2FSwhIZ0lw%2FbaiAwiDWXDxH%2BhfQJTcrzgXvottrU%2BxZZFEEQ%2FzUwV6u839Nyc%2FCIulapfSXCjtr52SXvdfOUh1W79JWnhtxWH1u8DyoUE7yF4CpbSLjk4dIoJ0N2MBQawI5Q0icjGm4FdpnP5FQE8H%2FivdYHK74rLiaKWgU7Q%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210908T175310Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=b54c9f2d671b88a123f8b747164804103247f21c2b41002d609d2e8a636e2b24"
      ]
    },
    "testbatch02.txt": {
      "uploadKey": "{UPLOAD_KEY}"
      "uploadExpiration": "2021-09-10T00:00:00Z",
      "urlExpiration": "2021-09-08T17:54:09Z",
      "urls": [
        "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/251418e4-472a-4505-9c11-2b2d6f129c3f?uploadId=ZkTJLztKw3CAmg2yoMa_A0pE07rq1DFBqWb6Eb1LwBDAWmJTrA6WkKnMhTM1P310fVCNXV5GFFUFmcGseETlh8OiOkyUye4dio2PfdvLm4.6QJ78vQNBHTEPNQCVtij6LTc7x9b9Wg6TbpvDakQ9Vw--&partNumber=4&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLWVhc3QtMSJGMEQCIE2FGHeC8zrputJkxBO8P9zTvrMYQJnGLuTOD2DjBTBzAiAf20aup8ZrXuQtS%2FD2Tp3i2ziKartriVp3RkiwIhIMxyqDBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDczNTIyMTAwNDg5NSIM9yHJCBzAgcUbR83nKtcD9snWn%2F5z57rdc14R0j%2BIRu%2Bop8lFu7byed7QbW5gcQ9bLTdQNZXVLPrvvUGozLVdH%2FNVNll%2FGUZ4%2BYRGe3fl%2BdYBJFy4RPyFY4H0%2Fxn98VtTpVH3KkJw7Z1CIYfGIp9%2B1th1fUSt7lAHIKcVxYlBYkjHQks4Elt0xlV%2Fg5qHaeSxZhdoFkllXcyjVPnvBHc1khlYdZcUCXk5WWEYdujCxdPFIQm%2BsNzLrS5U1gLNeRYDBjy3fB4jT47EMMoTm1YbCh0rCzeaxv98YV5I1i2NecYl0N%2BPk973%2FQxU6pG9Y%2F1N1aHXcG%2FDAxWWn%2BGV2caGqMqXgUa7ubhHbEkmHmXQ8VnguvhaRwkLVUWclAVVMTHe232t0YWeeS55TN53%2BIGHeQRRxLFr6j0uydAiPruSHgsNnA7QSbaMaZC245UZZ1hfSoRVKPTp2LRJ62qvP%2BoTC3m8KJ0Yc3lLBw%2BmFR6Q5ooace9OcfGIuouowm327nsLDBK2W6tDmI32zWBb8foJWJpzkUXBbB%2FkZjvAbhzU8aOF9u6yVWv1QFw%2BjR5OVX%2FiQWqBKwlXaZloq4ghHzn9u54OemqRWiOf3tnciWrJzSBEBi%2BEqHa1zq70JCiZHZzMwiled%2BaOMP7L44kGOqYBeVnCwBNFIFAR0sdeXSr26zfZh5LEZZo5gWICI6m3MMxPa%2BqUuDyxdD%2FSwhIZ0lw%2FbaiAwiDWXDxH%2BhfQJTcrzgXvottrU%2BxZZFEEQ%2FzUwV6u839Nyc%2FCIulapfSXCjtr52SXvdfOUh1W79JWnhtxWH1u8DyoUE7yF4CpbSLjk4dIoJ0N2MBQawI5Q0icjGm4FdpnP5FQE8H%2FivdYHK74rLiaKWgU7Q%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210908T175310Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=c92df9626311d1bb589be439ec53d8a66a8e6d36618ffeb7026e8a28645c5ec7",
        "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/251418e4-472a-4505-9c11-2b2d6f129c3f?uploadId=ZkTJLztKw3CAmg2yoMa_A0pE07rq1DFBqWb6Eb1LwBDAWmJTrA6WkKnMhTM1P310fVCNXV5GFFUFmcGseETlh8OiOkyUye4dio2PfdvLm4.6QJ78vQNBHTEPNQCVtij6LTc7x9b9Wg6TbpvDakQ9Vw--&partNumber=5&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLWVhc3QtMSJGMEQCIE2FGHeC8zrputJkxBO8P9zTvrMYQJnGLuTOD2DjBTBzAiAf20aup8ZrXuQtS%2FD2Tp3i2ziKartriVp3RkiwIhIMxyqDBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDczNTIyMTAwNDg5NSIM9yHJCBzAgcUbR83nKtcD9snWn%2F5z57rdc14R0j%2BIRu%2Bop8lFu7byed7QbW5gcQ9bLTdQNZXVLPrvvUGozLVdH%2FNVNll%2FGUZ4%2BYRGe3fl%2BdYBJFy4RPyFY4H0%2Fxn98VtTpVH3KkJw7Z1CIYfGIp9%2B1th1fUSt7lAHIKcVxYlBYkjHQks4Elt0xlV%2Fg5qHaeSxZhdoFkllXcyjVPnvBHc1khlYdZcUCXk5WWEYdujCxdPFIQm%2BsNzLrS5U1gLNeRYDBjy3fB4jT47EMMoTm1YbCh0rCzeaxv98YV5I1i2NecYl0N%2BPk973%2FQxU6pG9Y%2F1N1aHXcG%2FDAxWWn%2BGV2caGqMqXgUa7ubhHbEkmHmXQ8VnguvhaRwkLVUWclAVVMTHe232t0YWeeS55TN53%2BIGHeQRRxLFr6j0uydAiPruSHgsNnA7QSbaMaZC245UZZ1hfSoRVKPTp2LRJ62qvP%2BoTC3m8KJ0Yc3lLBw%2BmFR6Q5ooace9OcfGIuouowm327nsLDBK2W6tDmI32zWBb8foJWJpzkUXBbB%2FkZjvAbhzU8aOF9u6yVWv1QFw%2BjR5OVX%2FiQWqBKwlXaZloq4ghHzn9u54OemqRWiOf3tnciWrJzSBEBi%2BEqHa1zq70JCiZHZzMwiled%2BaOMP7L44kGOqYBeVnCwBNFIFAR0sdeXSr26zfZh5LEZZo5gWICI6m3MMxPa%2BqUuDyxdD%2FSwhIZ0lw%2FbaiAwiDWXDxH%2BhfQJTcrzgXvottrU%2BxZZFEEQ%2FzUwV6u839Nyc%2FCIulapfSXCjtr52SXvdfOUh1W79JWnhtxWH1u8DyoUE7yF4CpbSLjk4dIoJ0N2MBQawI5Q0icjGm4FdpnP5FQE8H%2FivdYHK74rLiaKWgU7Q%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210908T175310Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=c39f8b84546aeb8fea2b61659467b2f6c44592fecc674f3d7a75d7ed8db9721b",
        "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/251418e4-472a-4505-9c11-2b2d6f129c3f?uploadId=ZkTJLztKw3CAmg2yoMa_A0pE07rq1DFBqWb6Eb1LwBDAWmJTrA6WkKnMhTM1P310fVCNXV5GFFUFmcGseETlh8OiOkyUye4dio2PfdvLm4.6QJ78vQNBHTEPNQCVtij6LTc7x9b9Wg6TbpvDakQ9Vw--&partNumber=6&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLWVhc3QtMSJGMEQCIE2FGHeC8zrputJkxBO8P9zTvrMYQJnGLuTOD2DjBTBzAiAf20aup8ZrXuQtS%2FD2Tp3i2ziKartriVp3RkiwIhIMxyqDBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDczNTIyMTAwNDg5NSIM9yHJCBzAgcUbR83nKtcD9snWn%2F5z57rdc14R0j%2BIRu%2Bop8lFu7byed7QbW5gcQ9bLTdQNZXVLPrvvUGozLVdH%2FNVNll%2FGUZ4%2BYRGe3fl%2BdYBJFy4RPyFY4H0%2Fxn98VtTpVH3KkJw7Z1CIYfGIp9%2B1th1fUSt7lAHIKcVxYlBYkjHQks4Elt0xlV%2Fg5qHaeSxZhdoFkllXcyjVPnvBHc1khlYdZcUCXk5WWEYdujCxdPFIQm%2BsNzLrS5U1gLNeRYDBjy3fB4jT47EMMoTm1YbCh0rCzeaxv98YV5I1i2NecYl0N%2BPk973%2FQxU6pG9Y%2F1N1aHXcG%2FDAxWWn%2BGV2caGqMqXgUa7ubhHbEkmHmXQ8VnguvhaRwkLVUWclAVVMTHe232t0YWeeS55TN53%2BIGHeQRRxLFr6j0uydAiPruSHgsNnA7QSbaMaZC245UZZ1hfSoRVKPTp2LRJ62qvP%2BoTC3m8KJ0Yc3lLBw%2BmFR6Q5ooace9OcfGIuouowm327nsLDBK2W6tDmI32zWBb8foJWJpzkUXBbB%2FkZjvAbhzU8aOF9u6yVWv1QFw%2BjR5OVX%2FiQWqBKwlXaZloq4ghHzn9u54OemqRWiOf3tnciWrJzSBEBi%2BEqHa1zq70JCiZHZzMwiled%2BaOMP7L44kGOqYBeVnCwBNFIFAR0sdeXSr26zfZh5LEZZo5gWICI6m3MMxPa%2BqUuDyxdD%2FSwhIZ0lw%2FbaiAwiDWXDxH%2BhfQJTcrzgXvottrU%2BxZZFEEQ%2FzUwV6u839Nyc%2FCIulapfSXCjtr52SXvdfOUh1W79JWnhtxWH1u8DyoUE7yF4CpbSLjk4dIoJ0N2MBQawI5Q0icjGm4FdpnP5FQE8H%2FivdYHK74rLiaKWgU7Q%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210908T175310Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=b56b51fcfe6565968f4e668f1a60e0a909cf0f924aa5e5d4d4962356a0648e8d"
      ]
    },
    "testbatch03.txt": {
      "uploadKey": "{UPLOAD_KEY}"
      "uploadExpiration": "2021-09-10T00:00:00Z",
      "urlExpiration": "2021-09-08T17:54:09Z",
      "urls": [
        "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/3d021f09-3929-46ab-851c-267b1d0f9c6f?uploadId=FalunWDsubGWEtIU4xX_ldLhXxfZaY7QvYb_BFjRsM9AYlKCkaDvcwNog4EoslB0f_x_co71JzIuiD7yyryu.lxMy2loPJBF1nn6XeCcmgYTSDGtjVKI3l6Z8DjhICVX9kcxJO4TH_UGUp.ne9CBhg--&partNumber=1&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLWVhc3QtMSJGMEQCIE2FGHeC8zrputJkxBO8P9zTvrMYQJnGLuTOD2DjBTBzAiAf20aup8ZrXuQtS%2FD2Tp3i2ziKartriVp3RkiwIhIMxyqDBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDczNTIyMTAwNDg5NSIM9yHJCBzAgcUbR83nKtcD9snWn%2F5z57rdc14R0j%2BIRu%2Bop8lFu7byed7QbW5gcQ9bLTdQNZXVLPrvvUGozLVdH%2FNVNll%2FGUZ4%2BYRGe3fl%2BdYBJFy4RPyFY4H0%2Fxn98VtTpVH3KkJw7Z1CIYfGIp9%2B1th1fUSt7lAHIKcVxYlBYkjHQks4Elt0xlV%2Fg5qHaeSxZhdoFkllXcyjVPnvBHc1khlYdZcUCXk5WWEYdujCxdPFIQm%2BsNzLrS5U1gLNeRYDBjy3fB4jT47EMMoTm1YbCh0rCzeaxv98YV5I1i2NecYl0N%2BPk973%2FQxU6pG9Y%2F1N1aHXcG%2FDAxWWn%2BGV2caGqMqXgUa7ubhHbEkmHmXQ8VnguvhaRwkLVUWclAVVMTHe232t0YWeeS55TN53%2BIGHeQRRxLFr6j0uydAiPruSHgsNnA7QSbaMaZC245UZZ1hfSoRVKPTp2LRJ62qvP%2BoTC3m8KJ0Yc3lLBw%2BmFR6Q5ooace9OcfGIuouowm327nsLDBK2W6tDmI32zWBb8foJWJpzkUXBbB%2FkZjvAbhzU8aOF9u6yVWv1QFw%2BjR5OVX%2FiQWqBKwlXaZloq4ghHzn9u54OemqRWiOf3tnciWrJzSBEBi%2BEqHa1zq70JCiZHZzMwiled%2BaOMP7L44kGOqYBeVnCwBNFIFAR0sdeXSr26zfZh5LEZZo5gWICI6m3MMxPa%2BqUuDyxdD%2FSwhIZ0lw%2FbaiAwiDWXDxH%2BhfQJTcrzgXvottrU%2BxZZFEEQ%2FzUwV6u839Nyc%2FCIulapfSXCjtr52SXvdfOUh1W79JWnhtxWH1u8DyoUE7yF4CpbSLjk4dIoJ0N2MBQawI5Q0icjGm4FdpnP5FQE8H%2FivdYHK74rLiaKWgU7Q%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210908T175310Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=4dfab039dcb3cfa7257dfc04e6417d40a696ef6ab5be13048e0e148eab6e3a62"
      ]
    }
  }
}

```

Show More

## [Example 3](#example-3)

Get Upload URLs for additional parts with minutesExpiration parameter specified (200).

### Request

```
curl -X POST
  -H 'Authorization: Bearer {YOUR_TOKEN}'
  -H 'Content-Type: application/json'
  --data-raw '{
      "requests":[
        {
          "objectKey":"testbatch01.txt"
        },
        {
          "objectKey":"testbatch02.txt"
        },
        {
          "objectKey":"testbatch03.txt"
        }
      ]
    }'
  'https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/batchsigneds3upload?minutesExpiration=20'

```

Show More

### Response

```
{
  "results": {
    "testbatch01.txt": {
      "uploadKey": "{UPLOAD_KEY_1}",
      "uploadExpiration": "2021-09-04T00:00:00Z",
      "urlExpiration": "2021-09-02T18:01:26Z",
      "urls": [
        "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/cb2b4dc1-efd5-485a-a96c-c4ae3da968b6?uploadId=EB0BRf_9GiHg3AJbIppFnIUrTkFtpQqaLviRvDl7LkgA.u3.fRyv4UFR9S03xSYA2zCxpTLSwy82B29fA56CG4Khij1YsT_qOAOI3XVyZkO4wxUOt3bdnkX.Wt9IJ7GDmzW.gW.dF41cLymm2jnTfQ--&partNumber=1&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCICzziJFVpJJaq%2B5YOdNHRrR%2B0d9llx4VJBPeqOBQxIRiAiBwj%2Fx568QpyK5MCNeGmYgk%2BFUPFw894lwwiJuEYscUmCr6AwgaEAAaDDczNTIyMTAwNDg5NSIMSa2IRHeLEPYR1CXfKtcDt7qri4HAV6fuIfkRRc9os7DTixmhVrcdScYHpQcugBeFjzbKduPsUi3SUdfU8QNAu5I1LtuLSAKpXaG9kD%2BAK%2BtxiLZndT%2B3vwIdQgR19P5nII9MJYC0uzPW25T46N7W8aOEjTCRVARjpFY%2B6xvda5tVqIglaiRP4u%2FPRZSgnBLj5uOzV8K52MyzNoCj1IA5N%2FAkP5F21YiCdiCsmE2kaArYg4OAx1oduBDrUjcwgp%2BPQZfR%2FQM2aDA2IRIyLrQnWGN8HdHWEgTnPR%2FIQ5a5jMQW%2F0h%2B28th341XlRdfNTz%2BF3T3CQHt4cUnBCuOGm5auorCO%2FEMnS%2F9lpL5KF9Fy8V8n2EelA0m9TeRPXEh8lO2UigZufBR7WDemH%2Bx99KZEOtVWlP9lZMK%2FnGbegoJWY5tpLbGOkPBWvPnYHoitHDwiPOWKhdfnL7szjC8z2HeWIfmvRUg54oScBKMc9ijD1XANEz4rTVftpOZlAY9g3L%2B%2FIv2t8vemHebnYlpQlF1Rmu28Hgqz9VWj2hwBURrRJwoRXys5qmR7GggwfSaR2keOUUVGA9ryslMmIbM9sAHOMresXyTtY6eV08UYovs8Kcb9o5gTOvpuAygUDYXw2AlwWmIIRvmMLD2w4kGOqYB78qTOQRFBixpjD3jKnDioO7pqC4mY95WSJayppI1D4sX1MhMZCctvZHNmoPpCBZSYzp9se7At48TEY5ave8Sa6T0coTEhEfnpzop01llqWDCxan%2BwGscDWZ1WDdwA%2FtWCfyE1NEbXP7%2FgagbsFT8PFb2%2BhLhmt1EmU7jhfY7uAapLz5QzfO9wKkgp2yQbQ4eGZA1Ahq3nIugLiJC0Ddd55%2BUoynDyg%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210902T180027Z&X-Amz-SignedHeaders=host&X-Amz-Expires=1199&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=00e003b267eba402bd4bcb37d72164910360b6f0ad0e5da0e7bc4ee4d7f44f0b"
      ]
    },
    "testbatch02.txt": {
      "uploadKey": "{UPLOAD_KEY_2}",
      "uploadExpiration": "2021-09-04T00:00:00Z",
      "urlExpiration": "2021-09-02T18:01:26Z",
      "urls": [
        "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/ecd06570-36ce-4261-9c46-e5cb8d61a5d2?uploadId=Ep9b5hNlWKEbsEaR6MZDKn_W0V3dSkHRim49sy0QIOoAV3ENMcq_2HlgRrsEaoTxW6Sc0wdhZgDOdiTO09Q31YDWR.BV6E0MQKeA9Kl4POGS02tQkQ_Cn5ThJk18P0rps2nyl5PQXxpJLjWFkDgCcw--&partNumber=1&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCICzziJFVpJJaq%2B5YOdNHRrR%2B0d9llx4VJBPeqOBQxIRiAiBwj%2Fx568QpyK5MCNeGmYgk%2BFUPFw894lwwiJuEYscUmCr6AwgaEAAaDDczNTIyMTAwNDg5NSIMSa2IRHeLEPYR1CXfKtcDt7qri4HAV6fuIfkRRc9os7DTixmhVrcdScYHpQcugBeFjzbKduPsUi3SUdfU8QNAu5I1LtuLSAKpXaG9kD%2BAK%2BtxiLZndT%2B3vwIdQgR19P5nII9MJYC0uzPW25T46N7W8aOEjTCRVARjpFY%2B6xvda5tVqIglaiRP4u%2FPRZSgnBLj5uOzV8K52MyzNoCj1IA5N%2FAkP5F21YiCdiCsmE2kaArYg4OAx1oduBDrUjcwgp%2BPQZfR%2FQM2aDA2IRIyLrQnWGN8HdHWEgTnPR%2FIQ5a5jMQW%2F0h%2B28th341XlRdfNTz%2BF3T3CQHt4cUnBCuOGm5auorCO%2FEMnS%2F9lpL5KF9Fy8V8n2EelA0m9TeRPXEh8lO2UigZufBR7WDemH%2Bx99KZEOtVWlP9lZMK%2FnGbegoJWY5tpLbGOkPBWvPnYHoitHDwiPOWKhdfnL7szjC8z2HeWIfmvRUg54oScBKMc9ijD1XANEz4rTVftpOZlAY9g3L%2B%2FIv2t8vemHebnYlpQlF1Rmu28Hgqz9VWj2hwBURrRJwoRXys5qmR7GggwfSaR2keOUUVGA9ryslMmIbM9sAHOMresXyTtY6eV08UYovs8Kcb9o5gTOvpuAygUDYXw2AlwWmIIRvmMLD2w4kGOqYB78qTOQRFBixpjD3jKnDioO7pqC4mY95WSJayppI1D4sX1MhMZCctvZHNmoPpCBZSYzp9se7At48TEY5ave8Sa6T0coTEhEfnpzop01llqWDCxan%2BwGscDWZ1WDdwA%2FtWCfyE1NEbXP7%2FgagbsFT8PFb2%2BhLhmt1EmU7jhfY7uAapLz5QzfO9wKkgp2yQbQ4eGZA1Ahq3nIugLiJC0Ddd55%2BUoynDyg%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210902T180027Z&X-Amz-SignedHeaders=host&X-Amz-Expires=1199&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=d8fdcfd6e7c2d38cb304d7dc7a92d9ebbac99879b6434e23d5097577687cd16f"
      ]
    },
    "testbatch03.txt": {
      "uploadKey": "{UPLOAD_KEY_3}",
      "uploadExpiration": "2021-09-04T00:00:00Z",
      "urlExpiration": "2021-09-02T18:01:26Z",
      "urls": [
        "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/3c3d3fc2-1550-4c45-871d-20be74a5b41d?uploadId=PnJ4woE85386r2fqn447Rw7PSzhyY5LIRkutENAsAjq9eb6fBbwr.1iJSot.t3dS4UShLG4DUcF9Vy8LUiZDLku5kOmmw7w1mb.u5fWOS.tvAuif_8fhPVn3C60297zyPuq_E.J4qAo1Fcs_RLk.aQ--&partNumber=1&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCICzziJFVpJJaq%2B5YOdNHRrR%2B0d9llx4VJBPeqOBQxIRiAiBwj%2Fx568QpyK5MCNeGmYgk%2BFUPFw894lwwiJuEYscUmCr6AwgaEAAaDDczNTIyMTAwNDg5NSIMSa2IRHeLEPYR1CXfKtcDt7qri4HAV6fuIfkRRc9os7DTixmhVrcdScYHpQcugBeFjzbKduPsUi3SUdfU8QNAu5I1LtuLSAKpXaG9kD%2BAK%2BtxiLZndT%2B3vwIdQgR19P5nII9MJYC0uzPW25T46N7W8aOEjTCRVARjpFY%2B6xvda5tVqIglaiRP4u%2FPRZSgnBLj5uOzV8K52MyzNoCj1IA5N%2FAkP5F21YiCdiCsmE2kaArYg4OAx1oduBDrUjcwgp%2BPQZfR%2FQM2aDA2IRIyLrQnWGN8HdHWEgTnPR%2FIQ5a5jMQW%2F0h%2B28th341XlRdfNTz%2BF3T3CQHt4cUnBCuOGm5auorCO%2FEMnS%2F9lpL5KF9Fy8V8n2EelA0m9TeRPXEh8lO2UigZufBR7WDemH%2Bx99KZEOtVWlP9lZMK%2FnGbegoJWY5tpLbGOkPBWvPnYHoitHDwiPOWKhdfnL7szjC8z2HeWIfmvRUg54oScBKMc9ijD1XANEz4rTVftpOZlAY9g3L%2B%2FIv2t8vemHebnYlpQlF1Rmu28Hgqz9VWj2hwBURrRJwoRXys5qmR7GggwfSaR2keOUUVGA9ryslMmIbM9sAHOMresXyTtY6eV08UYovs8Kcb9o5gTOvpuAygUDYXw2AlwWmIIRvmMLD2w4kGOqYB78qTOQRFBixpjD3jKnDioO7pqC4mY95WSJayppI1D4sX1MhMZCctvZHNmoPpCBZSYzp9se7At48TEY5ave8Sa6T0coTEhEfnpzop01llqWDCxan%2BwGscDWZ1WDdwA%2FtWCfyE1NEbXP7%2FgagbsFT8PFb2%2BhLhmt1EmU7jhfY7uAapLz5QzfO9wKkgp2yQbQ4eGZA1Ahq3nIugLiJC0Ddd55%2BUoynDyg%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210902T180027Z&X-Amz-SignedHeaders=host&X-Amz-Expires=1199&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=5987bab2c4e97713a246cce60ab4291ab213df0dd413fd0c46b42f851e97f874"
      ]
    }
  }
}

```

Show More
