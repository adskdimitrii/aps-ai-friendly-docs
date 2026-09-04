# Export Usage Information

Source: https://aps.autodesk.com/en/docs/tokenflex/tutorials/export/

---

# Export Usage Information

## [Before You Begin](#before-you-begin)

Make sure that you have [registered an app](../../oauth/how-to-docs/create-app.md). and successfully [acquired an OAuth token](https://aps.autodesk.com/en/docs/oauth/v1/tutorials/http/get-2-legged-token/) with the `data:write` scope.

To understand how to make a usage data request, review the [query walkthrough](query.md).

## [Step 1: Obtaining an Access Token](#step-1-obtaining-an-access-token)

All calls to the Token Flex Usage Data API must be authenticated and a valid access token is required for each API call. Please refer to this [how-to guide](https://aps.autodesk.com/en/docs/oauth/v2/tutorials/) on how an access token can be obtained.

## [Step 2: Submit an Export request](#step-2-submit-an-export-request)

The Token Flex Usage Data API exposes a [POST /export/:contract_number/requests](../http-docs/http-export-contract_number-requests-POST.md) endpoint that allows for the submission of export requests.
Queries are processed asynchronously. This endpoint returns an export request key, which is then used with the [GET /export/:contract_number/requests/:request_key](../http-docs/http-export-contract_number-requests-request_key-GET.md) endpoint to check the query status and retrieve the results.

### Example Request

Here is an example request to export all manual adjustments and consumptions from year 1 of the contract.

```
CONTRACT_ID = "12345"
curl -H "Content-Type: application/json" -H "Authorization: Bearer hW0DvSvGgszPis1Yhot4c8kWW3NG" -X POST -H 'Content-Type: application/json'
https://developer.api.autodesk.com/tokenflex/v1/export/${CONTRACT_ID}/requests
-d '
{
  "fields": [
      "contractYear",
      "chargedItemID",
      "reasonType",
      "reasonComment",
      "usageCategory",
      "usageDate",
      "transactionDate",
      "productLineCode",
      "productName"
  ],
  "metrics": [
      "tokensConsumed",
      "quantity"
  ],
  "usageCategory": [
      "MANUAL_ADJUSTMENT",
      "MANUAL_CONSUMPTION"
  ],
  "where": "contractYear=1",
  "downloadFileName": "myYear1Adjustments"
}
'

```

Show More

Note that line breaks have been added to the cURL command above for ease of reading. **Make sure to remove them before executing any code in your terminal**.

If successful, the response body looks like:

```
{
  "requestKey": "2018-09-20T22:43:13#7be9d6ac-a077-42e9-8fc0-d276c38eab35",
  "requestStatus": "Requested",
  "downloadFileName": "myYear1Adjustments.csv",
  "exportRequestDate": "2018-09-20T22:43:13.132559Z"
}

```

The response contains a `requestKey` field, which is vital information to be used for the next step.

## [Step 3: Poll for Export Results](#step-3-poll-for-export-results)

Using the `requestKey` value returned in Step 2, poll the [GET /export/:contract_number/requests/:request_key](../http-docs/http-export-contract_number-requests-request_key-GET.md) endpoint to check the status of the export. A status of Error indicates that the query failed due to an error; Requested indicates that the export is queued, and the result is not yet available.

The request key parameter must be URI encoded. For example, `2018-09-20T22:43:13#7be9d6ac-a077-42e9-8fc0-d276c38eab35` is encoded as `2018-09-20T22%3A43%3A13%237be9d6ac-a077-42e9-8fc0-d276c38eab35`.

If successful, the `requestStatus` attribute will be Download and the response body looks like:

```
{
  "requestKey": "2018-09-20T22:43:13#7be9d6ac-a077-42e9-8fc0-d276c38eab35",
  "requestStatus": "Download",
  "downloadFileName": "myYear1Adjustments.csv",
  "downloadUrl": "http://download.autodesk.com/your-file-here",
  "downloadUrlExpireDate": "2018-09-20T22:47:29.549405Z",
  "exportRequestDate": "2018-09-20T22:43:13.132559Z",
  "readFlag": "N"
}

```

Show More

The `downloadUrl` attribute is a pre-signed URL that gives direct access to the exported CSV file. Note that anyone with this link is able to access the file. For security reasons, this link
expires in the (relatively short) period of time specified by `downloadUrlExpireDate`. To refresh this URL and access it again, use [POST /export/:contract_number/requests/:request_key/refreshUrl](../http-docs/http-export-contract_number-requests-request_key-refreshUrl-POST.md).

If the `requestStatus` attribute is Error, you can attempt to retry the export request using [POST /export/:contract_number/requests/:request_key/retry](../http-docs/http-export-contract_number-requests-request_key-retry-POST.md). This resets the status back to Requested.
