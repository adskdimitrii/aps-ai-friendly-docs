# buckets/:bucketKey/objects/batchcompleteupload

Source: https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-batchcompleteupload-POST/

---

# buckets/:bucketKey/objects/batchcompleteupload

Instructs OSS to complete the object creation process for numerous objects after their bytes have been uploaded directly to S3.

An object will not be accessible until you complete the object creation process, either with this endpoint or the single Complete Upload endpoint.

This endpoint accepts batch sizes of up to 25. Any larger and the request will fail.

Note: When uploading for a new OSS object, either data:write or data:create (or both) can be present. If requesting a URL to upload a blob to overwrite the content of an existing OSS object, then exactly data:write must be present; data:create cannot also be present.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/oss/v2/buckets/:bucketKey/objects/batchcompleteupload Authentication Context user context optional Required OAuth Scopes data:write data:create Data Format JSON

### Request

## Headers

Authorization * string Must be âBearer <token> â, where <token> is obtained via POST token .

### Request

## URI Parameters

bucketKey * string The URL-encoded name/key of the bucket containing the object for which to complete the upload

### Request

## Body Structure

requests * array: object An array of objects, each of which represents an upload to complete. See requests object structure.

## Requests object Structure

objectKey * string The key/name of the object for which to complete an upload. uploadKey * string The identifier of the upload session, which was provided by OSS in the response to the Get Upload URL/s request. size integer The expected size of the uploaded object. If provided, OSS will check this against the blob in S3 and return an error if the size does not match. eTags array: string An array of eTags. S3 returns an eTag to each upload request, be it for a chunk or an entire file. For a single-part upload, this array contains the expected eTag of the entire object. For a multipart upload, this array contains the expected eTag of each part of the upload; the index of an eTag in the array corresponds to its part number in the upload. If provided, OSS will validate these eTags against the content in S3, and return an error if the eTags do not match (indicating some form of data corruption). x-ads-meta-Content-Type string The Content-Type value that OSS will store in the record for the uploaded object. x-ads-meta-Content-Disposition string The Content-Disposition value that OSS will store in the record for the uploaded object. x-ads-meta-Content-Encoding string The Content-Encoding value that OSS will store in the record for the uploaded object. x-ads-meta-Cache-Control string The Cache-Control value that OSS will store in the record for the uploaded object.

### Response

## HTTP Status Code Summary

200 OK 400 BAD REQUEST The request could not be understood by the server due to malformed syntax or missing request headers. The client SHOULD NOT repeat the request without modifications.
The response body may give an indication of what is wrong with the request. 401 UNAUTHORIZED The supplied Authorization header was not valid or the supplied token scope was not acceptable. Verify Authentication and try again. 403 FORBIDDEN The Authorization was successfully validated but permission is not granted. Donât try again unless you solve permissions first. 500 INTERNAL SERVER ERROR Internal failure while processing the request, reason depends on error

### Response

## Body Structure (200)

results object A map of the returned results; each key in the map corresponds to an object key in the batch, and the value includes the results for that object. See results object structure

## Results object Structure

status string A string indicating whether the object completion failed. If this is not present, assume the completion succeeded. If this is âerrorâ, then the object completion failed. bucketKey string The key of the bucket into which the object was uploaded. objectId string The URN of the object. objectKey string The key of the object. size integer See the size object structure contentType string The Content-Type stored for the object, if provided. contentDisposition string The Content-Disposition stored for the object, if provided. contentEncoding string The Content-Encoding stored for the object, if provided. cacheControl string The Cache-Control stored for the object, if provided. parts integer See the parts object structure. reason string The reason for the failure, if the status is âerrorâ.

## Size object Structure

expected integer The expected object size provided in the request. detected integer The actual size of the object in S3, in bytes.

## Parts object Structure

part integer The index of the part in the multipart upload. status string Indicates whether this particular part uploaded to S3 is valid. Possible values are: - Pending: no part has been uploaded to S3 for this index. - Unexpected: the eTag of the part in S3 does not match the one provided in the request. - TooSmall: the chunk uploaded to S3 is smaller than 5MB, for any chunk except the final one. - Unexpected+TooSmall: the chunk is both too small and has an eTag mismatch. - Ok: The chunk has no issues. size integer The size of the corresponding part detected in S3. eTag string The eTag of the detected part in S3.

## Example 1

Basic Request to Complete 3 objects (200).

### Request

```
curl - X POST 'https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/batchcompleteupload' - H 'Authorization: Bearer {YOUR_TOKEN}' - H 'Content-Type: application/json' -- data - raw '{"requests": [ { "objectKey":"testbatch01.txt", "uploadKey":"AQICAHjeHUjisASnZxsm7tPGV29MH-UPjJcPt5rO5olTycJejgFVSwCDb2WydWPOh3xEOZGaAAABsDCCAawGCSqGSIb3DQEHBqCCAZ0wggGZAgEAMIIBkgYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAzWVTKRP-tGiBA_5gICARCAggFjKfypHjeDTaiKT5HAOsxtB4RUKlNXxZlrDwO4wKB1PK-onJcfTgGVhqSaCgo-Kp4-HQFdckhuApYkHREFLm4_51YBJ-vtBIUYrwd68ttbHJERabFhAZNiyj228JmELup4PpmmVVafJx7-dzwTDJuFZcim31lDmZ2vDJbR86wTyca3klgJYiBapkHMPrLO4GQ65jFKBGdmOTCtT3CkIM3CGcG-8mnuAbLJYdhi8AiiwZMTaeIIkC_QOciVjNOIPsX5urrMgY48Gn6Zq631z1SvfoAXwv2TmXpOoWxcJHZuPD_Hgs1Wi31WsRkNEnyCcQbs3xfRz7bIVPQPrFSrKf0RiULh_6G-lOVula05MaSZBnMG_Zz2m35Xh7OLl8R1qQcN7fCD_zjdnDH5VzsDM-puWCtHEoUR27nGFuVBIwQW32IwJPdY6XDgpKz2ReqPNi4NqDgNWpxc-fO9ZZ4_8K5z5ZgwTQ==" },{ "objectKey":"testbatch02.txt", "uploadKey":"AQICAHjeHUjisASnZxsm7tPGV29MH-UPjJcPt5rO5olTycJejgE9BnkwWget1YobK2FPdzGtAAABsTCCAa0GCSqGSIb3DQEHBqCCAZ4wggGaAgEAMIIBkwYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAyURzvsziCJZEcFppQCARCAggFk-4g7xBRoyaQ0mmn4bs4p-gRlu4rA-wCVlzMTokJgmUqHwAaUS-YNM9kAKBQDPzHLXr5QevMIIzTqEz_3Jl-ev3MIU-VpiJw9eP30aJQUOcYZlmknfjq2A8CrCLzPBvmzNaoDNIH_OvYzirAIrFEPBFITijVeYrr3mKXOvQS4CSo9mE9Ucg6pex6MH8NHtuQMYk5KViGEo2BgrCWwPkfeisd829TFPzjdRBTbWVjMQ-w9QTiir3pUJTvEx53m8yajPt44KDXjeLai3paxgB6zXvjZ2GXSIBBRutOrZEk4lo3nir3DcZuQqd0xRjJLRBoTi9aYdwTwsfhkPRDguOR3ucUIuUKSSXfcEUJD4HW2JanyvSukoG08I5j-jFVg4WNTDk9d2AiY9ZZbcZAGgA-vUDhJbeBG9OvVzQH7DgYk_BTnx0kNdk3mjlzVvSJ3u0aWM5qoirr6Jqe8Wmw_9ifd6IN7NHo=" },{ "objectKey":"testbatch03.txt", "uploadKey":"AQICAHjeHUjisASnZxsm7tPGV29MH-UPjJcPt5rO5olTycJejgGJjDZJI4bapoxpw2YZR5ejAAABsDCCAawGCSqGSIb3DQEHBqCCAZ0wggGZAgEAMIIBkgYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAwwUrsLZY3L2Rf5LZQCARCAggFjcYQ05_wWDU64JjN4mJKJ0_5Cy6U_-UUpoJRrOzu1c5R8nofaGOsdT3eRr82PNNb5K4-aeVUwxgJBvavSfFLe_uspY5limnmQcyQX9ALh8bUFxc4wAVsQU2cSI0KeQfD5Uh8rZXX6IL5cQvIFGpI_pjFUCCSztp50wVafMGVJSiVqqG23u8eq5BjUl1kDeklXCQTGq_wcbK9AcreerpQEw7n_VbNFlmzVsK74F_LYKPumqwvK5p1Y3VvdeRw1taKc9jD829P7XfrjNaLZVyJpjYRYaOcqA299eXcr95mvrgJAb8I-na4h9TJXmOeLijcB9q29BPnhxUddVrxPcLrFxswUNI_4lh8xk_4XLiIjxhe3RzDaaBagEMfaoHadivGm1TRfxZRh2ed_gWVCcNhdvL7LS1DxSCyGHXzsuwQQxEwShugJvcvh2db-dPodYJQLYuQ-e2Bp7KGZFY8lOfHC-4cSWA==" } ]}'
```

### Response

```
{ "results" :{ "testbatch01.txt" :{ "bucketKey" : "sampleosstestbucket202109021050" , "objectId" : "urn:adsk.objects:os.object:sampleosstestbucket202109021050/testbatch01.txt" , "objectKey" : "testbatch01.txt" , "size" : 6000000 , "contentType" : "application/octet-stream" , "location" : "https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/testbatch01.txt" }, "testbatch02.txt" :{ "bucketKey" : "sampleosstestbucket202109021050" , "objectId" : "urn:adsk.objects:os.object:sampleosstestbucket202109021050/testbatch02.txt" , "objectKey" : "testbatch02.txt" , "size" : 100 , "contentType" : "application/octet-stream" , "location" : "https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/testbatch02.txt" }, "testbatch03.txt" :{ "bucketKey" : "sampleosstestbucket202109021050" , "objectId" : "urn:adsk.objects:os.object:sampleosstestbucket202109021050/testbatch03.txt" , "objectKey" : "testbatch03.txt" , "size" : 100 , "contentType" : "application/octet-stream" , "location" : "https://developer.api.autodesk.com/oss/v2/buckets/apptestbucket/objects/testbatch03.txt" } } }
```

## Example 2

Sample Request with mixed failures - Missing Parts, Invalid Object Keys and a Successful complete with setting of Content-Type, Content-Disposition, etc. (200).

### Request

```
curl - X POST 'https://developer.api.autodesk.com//oss/v2/buckets/tdomim_test/objects/batchcompleteupload' - H 'Content-Type: application/json' - H 'Authorization: Bearer {YOUR_TOKEN}' -- data - raw '{ "requests":[ { "objectKey":"test.txt", "uploadKey":"AQICAHi2MQEvNztHttduUoui5X3zRZIFWbN8fglsja7Dn-mbGAEkKXMLUPPQfHW-pgs_EwlGAAABozCCAZ8GCSqGSIb3DQEHBqCCAZAwggGMAgEAMIIBhQYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAzwVOdoYHvGfipKLmUCARCAggFWFEOCBHAe7BWUrmHtmcGiMT3bb5J7yI5Uw6onaPU2zrPdsKXkYpVsMEK2r3cugL-24IyWfx7ov4YSdqWn9SkXqmNzzGcIbFJj84PY7_2EDXn8EOqKs9cyADSIKW_NRXC5yYIk_wT_K-0lJAWUJKuaQ_2Up6-c5IVVILTOugIVzNZQfA-PkX4cSdXtQPopMW8LH3Bu8diUqHq6PbUJQ9Ncj76A7Ng7JfPeyMFdsQlG8JjE4jQK54JGFLpSz-LZQ6xiDti-dCfG9eFna6AZZsTibWUKdf7yywn-URjaclqtwvyV3LZQpPkCyNiqcrsd6KqL7j_xg5pLJ5-LsIgFSuCG4c3cx6tbEhpwyzlXobR0Ux_l5FPWK7aY9GcUaL3vROl2iR5HWIkOtXoFJuPllIheI3ajKJdc4XSUG6XUj8jUvKSZsOywKE_cXxfR5xIZrQN2oONxCk8H" }, { "objectKey":"test2.txt", "uploadKey":"AQICAHi2MQEvNztHttduUoui5X3zRZIFWbN8fglsja7Dn-mbGAFlUZy7409q9I0aHYz3CwO_AAABpTCCAaEGCSqGSIb3DQEHBqCCAZIwggGOAgEAMIIBhwYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAx9kZGRn6DmzGd5Kp0CARCAggFY_VD_0zyU-o6MFFjftfQSJIgegojUvg_8YrIc_mjoClzByS9vu4qbR4SgPb-8w0bWheu_hf7GdjIJsdSbTnsLs0YORzEwIawyL9nYzXe2l9OnIU9TbgJfMSteUaQ8AoOQ_aQN4zzlJORrF0eDvseRmNYsh-fuNcxAQplK0QxYdTXdq5f0Z0xNuPQatsPhDpf-455kBFg7zFKAMXqwA8AZjbhtd5zC9D2X3J-29q3V6pODyZxDyYieKkQtYBIA8pl2mPm0kgDa664jtI8SXfVkSkgzPASVJPBK3juTjCIFvyQSLLYreR20ttk0AnvJUMQMCeDr5yL9CVPzbm9-lhpSQ6M3aFTkR3CCopkYLeLXj_MQnYz0K8jDMBw-nR1REwDOx1dETziNWLCI3muMxBADY7kuQ5__smRV2XlJpS5eGuUZoHmtTpDZsJoejtzY4k86Ge6vdYxyivI=", "size":44, "x-ads-meta-Content-Type":"text/plain" }, { "objectKey":"test3.txt", "uploadKey":"AQICAHi2MQEvNztHttduUoui5X3zRZIFWbN8fglsja7Dn-mbGAGCFdKIEEWH3zjP7Tljc_MGAAABoTCCAZ0GCSqGSIb3DQEHBqCCAY4wggGKAgEAMIIBgwYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAwIYO1QJjFMVHOiSFECARCAggFUi2ZEwUuEC1wyEYTY6Ueg-5-O8IlXSOBp-NQ2kfdwcumwj2mBBz4dBWyTHfVvX5TabHKELdK_4N7IiNdYzSxdmlmMJcqDcxe7Xk6L6ZatZ9U5UYUNDzubuE0H9N-k2gBqUUoRFHDo67ht-pu8_t_YFYiByR9FBG1Gi-95iJLihQY0QIHovKtIIfVn4UNfq5B7VYrcTQKKOYzGfqkkso_LxuvuS2mAXwhwTArPg7lbmdmYzfiiE0T4atbSPMPIu-qHO5T6hdaKpvESl7j3bbql5myhIjxmQjT5olVl6a-WrS_GbXn2xGtamo1mrFmvJQyGQdQKO7D1wuGVTdCPKX4JveiWVdY7esErahF1wwJjZZ4ReA9lmVRhsgB9YMeYgeZlJvPSRgz-89goItUKuhvCWsaHJC5NY53zIFhOz5yIPLYxy4rXT0GF54TvStGGe5frhJMUmw==", "size":359, "x-ads-meta-Content-Type":"text/plain", "x-ads-meta-Content-Disposition":"inline", "x-ads-meta-Content-Encoding":"gzip", "x-ads-meta-Cache-Control":"max-age=60" } ] }'
```

### Response

```
{ "results" :{ "test.txt" :{ "uploadKey" : "AQICAHi2MQEvNztHttduUoui5X3zRZIFWbN8fglsja7Dn-mbGAEkKXMLUPPQfHW-pgs_EwlGAAABozCCAZ8GCSqGSIb3DQEHBqCCAZAwggGMAgEAMIIBhQYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAzwVOdoYHvGfipKLmUCARCAggFWFEOCBHAe7BWUrmHtmcGiMT3bb5J7yI5Uw6onaPU2zrPdsKXkYpVsMEK2r3cugL-24IyWfx7ov4YSdqWn9SkXqmNzzGcIbFJj84PY7_2EDXn8EOqKs9cyADSIKW_NRXC5yYIk_wT_K-0lJAWUJKuaQ_2Up6-c5IVVILTOugIVzNZQfA-PkX4cSdXtQPopMW8LH3Bu8diUqHq6PbUJQ9Ncj76A7Ng7JfPeyMFdsQlG8JjE4jQK54JGFLpSz-LZQ6xiDti-dCfG9eFna6AZZsTibWUKdf7yywn-URjaclqtwvyV3LZQpPkCyNiqcrsd6KqL7j_xg5pLJ5-LsIgFSuCG4c3cx6tbEhpwyzlXobR0Ux_l5FPWK7aY9GcUaL3vROl2iR5HWIkOtXoFJuPllIheI3ajKJdc4XSUG6XUj8jUvKSZsOywKE_cXxfR5xIZrQN2oONxCk8H" , "status" : "error" , "reason" : "MissingOrInvalidParts" , "size" :{ "expected" : 32 , "detected" : 44 }, "parts" :[ { "part" : 1 , "size" : 44 , "eTag" : "f120c8688b905564bbc17b1913a8ea95" , "status" : "Ok" } ] }, "test2.txt" :{ "uploadKey" : "AQICAHi2MQEvNztHttduUoui5X3zRZIFWbN8fglsja7Dn-mbGAFlUZy7409q9I0aHYz3CwO_AAABpTCCAaEGCSqGSIb3DQEHBqCCAZIwggGOAgEAMIIBhwYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAx9kZGRn6DmzGd5Kp0CARCAggFY_VD_0zyU-o6MFFjftfQSJIgegojUvg_8YrIc_mjoClzByS9vu4qbR4SgPb-8w0bWheu_hf7GdjIJsdSbTnsLs0YORzEwIawyL9nYzXe2l9OnIU9TbgJfMSteUaQ8AoOQ_aQN4zzlJORrF0eDvseRmNYsh-fuNcxAQplK0QxYdTXdq5f0Z0xNuPQatsPhDpf-455kBFg7zFKAMXqwA8AZjbhtd5zC9D2X3J-29q3V6pODyZxDyYieKkQtYBIA8pl2mPm0kgDa664jtI8SXfVkSkgzPASVJPBK3juTjCIFvyQSLLYreR20ttk0AnvJUMQMCeDr5yL9CVPzbm9-lhpSQ6M3aFTkR3CCopkYLeLXj_MQnYz0K8jDMBw-nR1REwDOx1dETziNWLCI3muMxBADY7kuQ5__smRV2XlJpS5eGuUZoHmtTpDZsJoejtzY4k86Ge6vdYxyivI=" , "status" : "error" , "reason" : "InvalidUploadKey" }, "test3.txt" :{ "bucketKey" : "tdomim_test" , "objectId" : "urn:adsk.objects:os.object:tdomim_test/test3.txt" , "objectKey" : "test3.txt" , "size" : 359 , "contentType" : "text/plain" , "location" : "https://developer.api.autodesk.com/oss/v2/buckets/tdomim_test/objects/test3.txt" } } }
```
