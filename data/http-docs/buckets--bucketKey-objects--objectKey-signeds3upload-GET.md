# buckets/:bucketKey/objects/:objectKey/signeds3upload

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-GET/

---

# buckets/:bucketKey/objects/:objectKey/signeds3upload

Requests an S3 signed URL with which to upload an object, or an array of signed URLs with which to upload an object in multiple parts.

As with the download equivalent, the signed URL/s returned by this endpoint will expire after 2 minutes as default (** longer expiration times can be set using the minutesExpiration param up to 60 minutes). S3 evaluates the validity of a URL when it first receives the headers / query parameters of the request; if it evaluates the signed URL to be valid, the actual data transfer can take any amount of time past 2 minutes. If the upload fails after 2 minutes have occurred, you can call this endpoint again to request new signed URL/s. When requesting new signed URLs for a multipart upload, you must provide the same uploadKey provided in the response to the original request; otherwise, OSS cannot know how to associate the new chunks with the old ones.

You can successfully call the upload endpoint if you are managing your own OSS buckets (e.g. you are the bucket creator)

** DISCLAIMER When generating signed URLs, itâs important to use the smallest possible expiration time, in order to avoid longer access in case of exposure of the URL.

## Resource Information

Method and URI GET https://developer.api.autodesk.com/oss/v2/buckets/:bucketKey/objects/:objectKey/signeds3upload Authentication Context user context optional Required OAuth Scopes data:write data:create Data Format JSON

### Request

## Headers

Authorization * string Must be âBearer <token> â, where <token> is obtained
via POST token .

### Request

## URI Parameters

bucketKey * string URL-encoded bucket key objectKey * string URL-encoded object key to create signed URL for

### Request

## Query String Parameters

uploadKey string The identifier of a previously-initiated upload, in order to request more chunk upload URLs for the same upload. This must match the uploadKey returned by a previous call to this endpoint where the client requested more than one part URL. firstPart integer For a multipart upload, is the starting index when getting upload part URL. If this parameter is not specified the default value is firstPart = 1. Example: To retrieve the parts from 10 to 15 you should pass firstPart = 10 and parts = 6, this will retrieve the parts 10, 11, 12, 13, 14 and 15. parts integer For a multipart upload, the number of chunk URLs to return. If this parameter is not specified the default value is parts = 1. Maximum number of parts is 25. Example: To retrieve the parts from 1 to 5 you should pass parts = 5, this will retrieve 5 parts starting from 1 as follows 1, 2, 3, 4 and 5. useAcceleration boolean Whether or not to generate an accelerated signed URL (ie: URLs of the form â¦s3-accelerate.amazonaws.comâ¦ vs â¦s3.amazonaws.comâ¦). When not specified, defaults to true. Providing non-boolean values will result in a 400 error. minutesExpiration integer The custom expiration time within the 1 to 60 minutes range, if not specified, default is 2 minutes.

### Response

## HTTP Status Code Summary

200 OK 400 BAD REQUEST The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications. The response body may give an indication of what is wrong with the request. 401 UNAUTHORIZED The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify Authentication and try again. 403 FORBIDDEN The Authorization was successfully validated but permission is not granted. Donât try again unless you solve permissions first. 404 NOT FOUND Object or bucket does not exist 429 RATE-LIMIT EXCEEDED The maximum number of API calls that an app can make per minute was exceeded. 500 INTERNAL SERVER ERROR Internal failure while processing the request, reason depends on error

### Response

## Body Structure (200)

uploadKey string The identifier of the upload session, to differentiate multiple attempts to upload data for the same object. This must be provided when re-requesting chunk URLs for the same blob if they expire, and when calling the Complete Upload endpoint. urls array:string An array of signed URLs. For a single-part upload, this will only include a single URL. For a multipart upload, there will be one for each chunk of a multipart upload. The index of the URL in the array corresponds to the part number of the chunk. urlExpiration string Time Stamp representing the expiration of the generated signed URLs.  Note that when multiple parts/URLs are requested, there is a chance that this time stamp does not represent the expiration of all URLs in the group.  Consider this expiration a very close approximation of the expiration of the URLs in the group uploadExpiration string Time Stamp representing the upload abort date for which all parts must be uploaded for the object and the complete upload endpoint must be called.

## Example 1

Requests an array of signed URLs with which to upload an object in multiple parts. (200).

### Request

```
curl - X GET - H 'Authorization: Bearer eYeL5gYxAT2j3u9TEerxoJoToNbi' - H 'Content-Type: application/json' 'https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/objectKeyFoo/signeds3upload?parts=3'
```

### Response

```
{ "uploadKey" : "{UPLOAD_KEY}" , "uploadExpiration" : "2022-01-25T00:00:00Z" , "urlExpiration" : "2022-01-23T21:48:42Z" , "urls" : [ "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/647eac4c-538a-430f-aeb9-f9868c812f0a?uploadId=DMgAHXjzyxNyetLEdTxBOGmtAglxYcvCiSdzJGeXlxrELy6LV1u5sV1vJMomNA1ajJLU_Si7MYFsZ2mAvQbrgBl32AKD1ZQ25dgZl0DJsMbEqfC_AciKZWGryKcW.WwzlUXJrbqLSzzqAolhoGDm0A--&partNumber=1&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQD5Kzy1P6NLaYATv93vjMe4xlBvvYXZQCNjWMmASGM%2FKgIhAPQVE0Qjg4muudsXUCgp%2BMcR%2F6Xu8WSPDgEpsDN34m0EKoMECPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMOTkzNzg5OTkyMDYzIgz7JvvTxzNi3xf3K8Aq1wOKZgmdUjLUXjBwryTukT8udQWjmR7nTXydT09euWNE7Sh%2FVztSQhXDXpBXp%2B9%2Ffpyw7CyZJOoJJgqH0DfgqIglXTP%2FUnT7cG89AIryNVDa3Tndtb1P1IlLjf0T%2BWMCXw0U%2BryS5%2BMngDrw5O82e2qeAWPcCJjo0X1SWg%2FzWac44I6vqH02U0dZoQQ%2Bu3n9yiI4DtWMj60wjgt%2FgjGmSY5jD2mILpvOSJpHvtai6%2BMCbQOstEEc6OaY1LeOBlf3Pf8SEfrpHGsHw%2BhJQ5RlpEcudX2ZO8LdZjk44%2FH6INdISZJr4N8gKKBG5%2FiXmOI4qzwcydNgfYJ3lN7yt7YRntBPnJ2N3EmKOPMot%2B0OCk7DFS%2F0f2JbcJCEB%2Bmg2tWG5KqV9tu968SR%2FkC4l2LAyo4ZVRLhQTOWgSYbfhYTL1F%2BIGGWE%2Fi%2BzGYSXKthrVYpC4h7eSeFK%2B3FUQSb6lJ0yScRP%2B%2FRmy6W%2FynJC8F%2BFkYLT%2FJaFE8tKgTUdphHtat0zppFp5UzrOQePc1abSg2uMpKkjvUSt%2FrvJ3WuN7UBj2LQ1ruUV6nx7rS7fSOUazOXmP5ToY5SXbAEx5Dvc9hEyBkxct9ZhbaF5mJE4yQbfn20xaMw73%2Bzvsw0b%2FshwY6pAH8uiCdcXXWNsEYc2g0T7H6fuCFE19VflTSlmBVnGLRTho0y4kCX6k4VIn6xV2dbuTAZzB8U%2Fdms%2FkgIM29DXNdJuJgskulKDnMjK7rRQUe44MUQoxx2P20M8pX0Oq5epgKRGtqxi6%2F8XFh5mJRVhamJwu59WmvLdSvGVsbGJk3oYtTmyEJn4N0or2QWbZdFtfrBGhLlm%2FuTislKvcut0uDWixBfA%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210723T214743Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=269cde4288e380ce720b2a8a039b5e311cb9d4276ccf5e59582b32676a8f378b" , "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/647eac4c-538a-430f-aeb9-f9868c812f0a?uploadId=DMgAHXjzyxNyetLEdTxBOGmtAglxYcvCiSdzJGeXlxrELy6LV1u5sV1vJMomNA1ajJLU_Si7MYFsZ2mAvQbrgBl32AKD1ZQ25dgZl0DJsMbEqfC_AciKZWGryKcW.WwzlUXJrbqLSzzqAolhoGDm0A--&partNumber=2&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQD5Kzy1P6NLaYATv93vjMe4xlBvvYXZQCNjWMmASGM%2FKgIhAPQVE0Qjg4muudsXUCgp%2BMcR%2F6Xu8WSPDgEpsDN34m0EKoMECPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMOTkzNzg5OTkyMDYzIgz7JvvTxzNi3xf3K8Aq1wOKZgmdUjLUXjBwryTukT8udQWjmR7nTXydT09euWNE7Sh%2FVztSQhXDXpBXp%2B9%2Ffpyw7CyZJOoJJgqH0DfgqIglXTP%2FUnT7cG89AIryNVDa3Tndtb1P1IlLjf0T%2BWMCXw0U%2BryS5%2BMngDrw5O82e2qeAWPcCJjo0X1SWg%2FzWac44I6vqH02U0dZoQQ%2Bu3n9yiI4DtWMj60wjgt%2FgjGmSY5jD2mILpvOSJpHvtai6%2BMCbQOstEEc6OaY1LeOBlf3Pf8SEfrpHGsHw%2BhJQ5RlpEcudX2ZO8LdZjk44%2FH6INdISZJr4N8gKKBG5%2FiXmOI4qzwcydNgfYJ3lN7yt7YRntBPnJ2N3EmKOPMot%2B0OCk7DFS%2F0f2JbcJCEB%2Bmg2tWG5KqV9tu968SR%2FkC4l2LAyo4ZVRLhQTOWgSYbfhYTL1F%2BIGGWE%2Fi%2BzGYSXKthrVYpC4h7eSeFK%2B3FUQSb6lJ0yScRP%2B%2FRmy6W%2FynJC8F%2BFkYLT%2FJaFE8tKgTUdphHtat0zppFp5UzrOQePc1abSg2uMpKkjvUSt%2FrvJ3WuN7UBj2LQ1ruUV6nx7rS7fSOUazOXmP5ToY5SXbAEx5Dvc9hEyBkxct9ZhbaF5mJE4yQbfn20xaMw73%2Bzvsw0b%2FshwY6pAH8uiCdcXXWNsEYc2g0T7H6fuCFE19VflTSlmBVnGLRTho0y4kCX6k4VIn6xV2dbuTAZzB8U%2Fdms%2FkgIM29DXNdJuJgskulKDnMjK7rRQUe44MUQoxx2P20M8pX0Oq5epgKRGtqxi6%2F8XFh5mJRVhamJwu59WmvLdSvGVsbGJk3oYtTmyEJn4N0or2QWbZdFtfrBGhLlm%2FuTislKvcut0uDWixBfA%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210723T214743Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=e5e4edcf819856f4a689c8a90975a64395df7fb33d60e3ab351e39ad0fe2585c" , "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/647eac4c-538a-430f-aeb9-f9868c812f0a?uploadId=DMgAHXjzyxNyetLEdTxBOGmtAglxYcvCiSdzJGeXlxrELy6LV1u5sV1vJMomNA1ajJLU_Si7MYFsZ2mAvQbrgBl32AKD1ZQ25dgZl0DJsMbEqfC_AciKZWGryKcW.WwzlUXJrbqLSzzqAolhoGDm0A--&partNumber=3&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQD5Kzy1P6NLaYATv93vjMe4xlBvvYXZQCNjWMmASGM%2FKgIhAPQVE0Qjg4muudsXUCgp%2BMcR%2F6Xu8WSPDgEpsDN34m0EKoMECPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMOTkzNzg5OTkyMDYzIgz7JvvTxzNi3xf3K8Aq1wOKZgmdUjLUXjBwryTukT8udQWjmR7nTXydT09euWNE7Sh%2FVztSQhXDXpBXp%2B9%2Ffpyw7CyZJOoJJgqH0DfgqIglXTP%2FUnT7cG89AIryNVDa3Tndtb1P1IlLjf0T%2BWMCXw0U%2BryS5%2BMngDrw5O82e2qeAWPcCJjo0X1SWg%2FzWac44I6vqH02U0dZoQQ%2Bu3n9yiI4DtWMj60wjgt%2FgjGmSY5jD2mILpvOSJpHvtai6%2BMCbQOstEEc6OaY1LeOBlf3Pf8SEfrpHGsHw%2BhJQ5RlpEcudX2ZO8LdZjk44%2FH6INdISZJr4N8gKKBG5%2FiXmOI4qzwcydNgfYJ3lN7yt7YRntBPnJ2N3EmKOPMot%2B0OCk7DFS%2F0f2JbcJCEB%2Bmg2tWG5KqV9tu968SR%2FkC4l2LAyo4ZVRLhQTOWgSYbfhYTL1F%2BIGGWE%2Fi%2BzGYSXKthrVYpC4h7eSeFK%2B3FUQSb6lJ0yScRP%2B%2FRmy6W%2FynJC8F%2BFkYLT%2FJaFE8tKgTUdphHtat0zppFp5UzrOQePc1abSg2uMpKkjvUSt%2FrvJ3WuN7UBj2LQ1ruUV6nx7rS7fSOUazOXmP5ToY5SXbAEx5Dvc9hEyBkxct9ZhbaF5mJE4yQbfn20xaMw73%2Bzvsw0b%2FshwY6pAH8uiCdcXXWNsEYc2g0T7H6fuCFE19VflTSlmBVnGLRTho0y4kCX6k4VIn6xV2dbuTAZzB8U%2Fdms%2FkgIM29DXNdJuJgskulKDnMjK7rRQUe44MUQoxx2P20M8pX0Oq5epgKRGtqxi6%2F8XFh5mJRVhamJwu59WmvLdSvGVsbGJk3oYtTmyEJn4N0or2QWbZdFtfrBGhLlm%2FuTislKvcut0uDWixBfA%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210723T214743Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=e54df1482da076b43b32b7da891fbaa3bf66a458e367739173c74442345e35a1" ] }
```

## Example 2

Get only parts 2 and 3 to upload remaining parts of an object. (200).

### Request

```
curl - X GET - H 'Authorization: Bearer eYeL5gYxAT2j3u9TEerxoJoToNbi' - H 'Content-Type: application/json' 'https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/random_file.bin/signeds3upload?parts=2&firstPart=2&uploadKey={YOUR_UPLOAD_KEY_FROM_PREVIOUS_RESPONSE}'
```

### Response

```
{ "uploadKey" : "{UPLOAD_KEY}" , "uploadExpiration" : "2022-01-25T00:00:00Z" , "urlExpiration" : "2022-01-23T21:56:22Z" , "urls" : [ "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/647eac4c-538a-430f-aeb9-f9868c812f0a?uploadId=DMgAHXjzyxNyetLEdTxBOGmtAglxYcvCiSdzJGeXlxrELy6LV1u5sV1vJMomNA1ajJLU_Si7MYFsZ2mAvQbrgBl32AKD1ZQ25dgZl0DJsMbEqfC_AciKZWGryKcW.WwzlUXJrbqLSzzqAolhoGDm0A--&partNumber=2&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIAd8RyqdB5tMGG8aHY6p9CXuQvK3RJ5TZ1NxdjQ7f2gJAiEA2bon9s9K0mAWnQhPY%2B4iNIf4X%2FO7cL6dagnWF%2F0vzwcqgwQI9v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw5OTM3ODk5OTIwNjMiDOmdjGhbkDw3JeXFPSrXA6kjOdFG53zQBU7dDozGV%2BE2ciYnjpL8shIdLAnagH6mU%2BxCBIkfZYPyYQD42SIk8sowyVpIjTWgqq99uPpNbOCI4GiihWyEW8Lx%2FUAFzc37fuIiXj7OJgfap9kv4uhiQVclBtY8ma1VnfK3xfe6WwBHYEyT9nu2JDzdkUo7X5QwENMeC0MJLB%2FKs06WfNtKAjShax3JebelHS4hIEOHnBihbwstxryb6azqnzCg4w3GwUH%2FA78FJfBn0QlymmNRfiHFEQcv0xVAJDVIOmgSGshJLTr7n9ukUqmS31zFg087CoS9Y1vjFbK3ccWJK%2F3QEpat1m4%2F8Ak9uee3D4ZBXvM5%2FpJxdo%2BqzL9zAV4CU8MSEsvRsdD5c3BUccHGKmg331qaJWqtEoIjL9Tsw8nYgILBeM7gIDC6maed0mcV5fvA1htuNLb%2FGdtZYwd6CBhgZa63fdqLr4NLvBsrhWAT4N%2Fc%2Bqcztvfm4U%2BXSAyYFgttlERV9DfPqG%2F9NeRxf63Pr4T60VS7FGhhhID7u2upy3xB9r8UvoPQCe1hTGP2Byj7yZn%2Fhpq9epI6mUIUDMcZrWZ1f6LgPsw6Sv2w%2BCJu7RFVWOGknmt4SOjcPF96QjYolP9LjW5VrDCMzOyHBjqlAe7BH4ZH62W5Jh8Wy1jg5oz99TUr%2FBJas63lwUt5OEoYcaK3EcV2XN5i0TfF69dP66yABPHNweX%2F0Z3HpHTDexpdEa62HHWjsq8JPIzxr36AR2yv9x2OEHYF3TCaMLSiUM0tD5lDiP9nrkS3eBuSVIJD%2BlfPeWh6kne%2BDCg4mb7W9yw4wZsBDe5gFWthMmCwHT3Q452uh09UIubL5HPlitcDJwJlaQ%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210723T215523Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=a7f248f998c1c9d287a824ad9a3a895e8785bd83dab65f2a2089af8f0f0b8e46" , "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/647eac4c-538a-430f-aeb9-f9868c812f0a?uploadId=DMgAHXjzyxNyetLEdTxBOGmtAglxYcvCiSdzJGeXlxrELy6LV1u5sV1vJMomNA1ajJLU_Si7MYFsZ2mAvQbrgBl32AKD1ZQ25dgZl0DJsMbEqfC_AciKZWGryKcW.WwzlUXJrbqLSzzqAolhoGDm0A--&partNumber=3&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIAd8RyqdB5tMGG8aHY6p9CXuQvK3RJ5TZ1NxdjQ7f2gJAiEA2bon9s9K0mAWnQhPY%2B4iNIf4X%2FO7cL6dagnWF%2F0vzwcqgwQI9v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw5OTM3ODk5OTIwNjMiDOmdjGhbkDw3JeXFPSrXA6kjOdFG53zQBU7dDozGV%2BE2ciYnjpL8shIdLAnagH6mU%2BxCBIkfZYPyYQD42SIk8sowyVpIjTWgqq99uPpNbOCI4GiihWyEW8Lx%2FUAFzc37fuIiXj7OJgfap9kv4uhiQVclBtY8ma1VnfK3xfe6WwBHYEyT9nu2JDzdkUo7X5QwENMeC0MJLB%2FKs06WfNtKAjShax3JebelHS4hIEOHnBihbwstxryb6azqnzCg4w3GwUH%2FA78FJfBn0QlymmNRfiHFEQcv0xVAJDVIOmgSGshJLTr7n9ukUqmS31zFg087CoS9Y1vjFbK3ccWJK%2F3QEpat1m4%2F8Ak9uee3D4ZBXvM5%2FpJxdo%2BqzL9zAV4CU8MSEsvRsdD5c3BUccHGKmg331qaJWqtEoIjL9Tsw8nYgILBeM7gIDC6maed0mcV5fvA1htuNLb%2FGdtZYwd6CBhgZa63fdqLr4NLvBsrhWAT4N%2Fc%2Bqcztvfm4U%2BXSAyYFgttlERV9DfPqG%2F9NeRxf63Pr4T60VS7FGhhhID7u2upy3xB9r8UvoPQCe1hTGP2Byj7yZn%2Fhpq9epI6mUIUDMcZrWZ1f6LgPsw6Sv2w%2BCJu7RFVWOGknmt4SOjcPF96QjYolP9LjW5VrDCMzOyHBjqlAe7BH4ZH62W5Jh8Wy1jg5oz99TUr%2FBJas63lwUt5OEoYcaK3EcV2XN5i0TfF69dP66yABPHNweX%2F0Z3HpHTDexpdEa62HHWjsq8JPIzxr36AR2yv9x2OEHYF3TCaMLSiUM0tD5lDiP9nrkS3eBuSVIJD%2BlfPeWh6kne%2BDCg4mb7W9yw4wZsBDe5gFWthMmCwHT3Q452uh09UIubL5HPlitcDJwJlaQ%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210723T215523Z&X-Amz-SignedHeaders=host&X-Amz-Expires=120&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=ec7aa7d4e348ae70453947b528bef36566001ae64b128c07f5e279b5bfddaab1" ] }
```

## Example 3

Requests a signed URL with which to upload an object using the minutesExpiration parameter to set 15 minutes expiration time. (200).

### Request

```
curl - X GET - H 'Authorization: Bearer eYeL5gYxAT2j3u9TEerxoJoToNbi' - H 'Content-Type: application/json' 'https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/objectKeyFoo/signeds3upload?minutesExpiration=15'
```

### Response

```
{ "uploadKey" : "{UPLOAD_KEY}" , "uploadExpiration" : "2022-01-25T00:00:00Z" , "urlExpiration" : "2022-01-23T21:48:42Z" , "urls" : [ "https://com-autodesk-oss-direct-upload.s3-accelerate.amazonaws.com/signed-url-uploads/647eac4c-538a-430f-aeb9-f9868c812f0a?uploadId=DMgAHXjzyxNyetLEdTxBOGmtAglxYcvCiSdzJGeXlxrELy6LV1u5sV1vJMomNA1ajJLU_Si7MYFsZ2mAvQbrgBl32AKD1ZQ25dgZl0DJsMbEqfC_AciKZWGryKcW.WwzlUXJrbqLSzzqAolhoGDm0A--&partNumber=1&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQD5Kzy1P6NLaYATv93vjMe4xlBvvYXZQCNjWMmASGM%2FKgIhAPQVE0Qjg4muudsXUCgp%2BMcR%2F6Xu8WSPDgEpsDN34m0EKoMECPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMOTkzNzg5OTkyMDYzIgz7JvvTxzNi3xf3K8Aq1wOKZgmdUjLUXjBwryTukT8udQWjmR7nTXydT09euWNE7Sh%2FVztSQhXDXpBXp%2B9%2Ffpyw7CyZJOoJJgqH0DfgqIglXTP%2FUnT7cG89AIryNVDa3Tndtb1P1IlLjf0T%2BWMCXw0U%2BryS5%2BMngDrw5O82e2qeAWPcCJjo0X1SWg%2FzWac44I6vqH02U0dZoQQ%2Bu3n9yiI4DtWMj60wjgt%2FgjGmSY5jD2mILpvOSJpHvtai6%2BMCbQOstEEc6OaY1LeOBlf3Pf8SEfrpHGsHw%2BhJQ5RlpEcudX2ZO8LdZjk44%2FH6INdISZJr4N8gKKBG5%2FiXmOI4qzwcydNgfYJ3lN7yt7YRntBPnJ2N3EmKOPMot%2B0OCk7DFS%2F0f2JbcJCEB%2Bmg2tWG5KqV9tu968SR%2FkC4l2LAyo4ZVRLhQTOWgSYbfhYTL1F%2BIGGWE%2Fi%2BzGYSXKthrVYpC4h7eSeFK%2B3FUQSb6lJ0yScRP%2B%2FRmy6W%2FynJC8F%2BFkYLT%2FJaFE8tKgTUdphHtat0zppFp5UzrOQePc1abSg2uMpKkjvUSt%2FrvJ3WuN7UBj2LQ1ruUV6nx7rS7fSOUazOXmP5ToY5SXbAEx5Dvc9hEyBkxct9ZhbaF5mJE4yQbfn20xaMw73%2Bzvsw0b%2FshwY6pAH8uiCdcXXWNsEYc2g0T7H6fuCFE19VflTSlmBVnGLRTho0y4kCX6k4VIn6xV2dbuTAZzB8U%2Fdms%2FkgIM29DXNdJuJgskulKDnMjK7rRQUe44MUQoxx2P20M8pX0Oq5epgKRGtqxi6%2F8XFh5mJRVhamJwu59WmvLdSvGVsbGJk3oYtTmyEJn4N0or2QWbZdFtfrBGhLlm%2FuTislKvcut0uDWixBfA%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210723T214743Z&X-Amz-SignedHeaders=host&X-Amz-Expires=899&X-Amz-Credential=[AMZ CREDENTIAL]&X-Amz-Signature=269cde4288e380ce720b2a8a039b5e311cb9d4276ccf5e59582b32676a8f378b" , ] }
```
