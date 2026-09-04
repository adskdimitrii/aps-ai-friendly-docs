# Query Usage Information

Source: https://aps.autodesk.com/en/docs/tokenflex/tutorials/query/

---

# Query Usage Information

## [Before You Begin](#before-you-begin)

Make sure that you have [registered an app](../../oauth/how-to-docs/create-app.md). and successfully [acquired an OAuth token](https://aps.autodesk.com/en/docs/oauth/v1/tutorials/http/get-2-legged-token/) with the `data:read` scope.

## [Step 1: Obtaining an Access Token](#step-1-obtaining-an-access-token)

All calls to the Token Flex Usage Data API must be authenticated and a valid access token is required for each API call. Please refer to this [how-to guide](https://aps.autodesk.com/en/docs/oauth/v2/tutorials/) on how an access token can be obtained.

## [Step 2: Submit Query](#step-2-submit-query)

The Token Flex Usage Data API exposes a [POST usage/:contract_number/query](../http-docs/http-usage-contract_number-query-POST.md) endpoint that allows for the submission of queries.
Queries are processed asynchronously. This endpoint returns a query ID, which is then used with the [GET usage/query/:query_id](https://aps.autodesk.com/en/docs/tokenflex/v1/reference/http/usage-query_query_ud-GET/) endpoint to check the query status and retrieve the results.

### Example Request

```
CONTRACT_NUMBER = "12345"
curl -H "Content-Type: application/json" -H "Authorization: Bearer hW0DvSvGgszPis1Yhot4c8kWW3NG" -X POST -H 'Content-Type: application/json'
https://developer.api.autodesk.com/tokenflex/v1/usage/${CONTRACT_NUMBER}/query
-d '
{
  "fields": [
    "usageCategory",
    "productName"
  ],
  "metrics": [
    "tokensConsumed"
  ],
  "where": "contractYear=1 AND productName IN ('Revit Live', 'Vault Office', 'Moldflow Adviser Ultimate', 'ReMake')"
}
'

```

Show More

Note that line breaks have been added to the cURL command above for ease of reading. **Make sure to remove them before executing any code in your terminal**.

If successful, the response body looks like:

```
{
  "status": "QUEUED",
  "id": "query:dd8a8fa076a3a82cb994eb9689392d31d6ee18c7222fd7035efffe51",
  "detail_uri": "/v1/usage/12345/query/query:dd8a8fa076a3a82cb994eb9689392d31d6ee18c7222fd7035efffe51"
}

```

The response contains a `detail_uri` field, which is vital information to be used for the next steps.

## [Step 3: Poll for Query Results](#step-3-poll-for-query-results)

Using the `detail_url` value returned in Step 2, poll the [GET usage/:contract_number/query/:query_id](../http-docs/http-usage-contract_number-query-query_id-GET.md) endpoint to check the status of the query. A status of “FAILED” or “TIMEOUT” indicates that the query failed due to an error; “EXPIRED” indicates that the query results
are no longer available. Use the `offset` and `limit` query parameters to paginate through the query results; by default the first 100 results will be returned.

If successful, the response body looks like:

```
{
  "status": "DONE",
  "result": {
    "columns": [
      "usageCategory",
      "productName",
      "tokensConsumed"
    ],
    "rows": [
      [
          "PRODUCT_CONSUMPTION",
          "Moldflow Adviser Ultimate",
          60.0
      ],
      [
          "PRODUCT_CONSUMPTION",
          "ReMake",
          46.0
      ],
      [
          "PRODUCT_CONSUMPTION",
          "Revit Live",
          128.0
      ],
      [
          "PRODUCT_CONSUMPTION",
          "Vault Office",
          3.0
      ]
    ],
    "total": 4,
    "offset": 0,
    "limit": 100,
  }
}

```

Show More

Within the `result` element, the `columns` array identifies the columns in the query result and the `rows` array identifies the values in each row/column.
For the example above, the value of the `productName` column in the second row is `Remake`.

## [(Optional) Step 4: Get the results as a CSV file](#optional-step-4-get-the-results-as-a-csv-file)

Sometimes, you want to acquire the output of the query as a CSV file for ingestion into another system. You may be required to do this if your query fetches a lot of data and exceeds the 5-minute time limit.
In those cases, use the [Export API](../http-docs/http-export-contract_number-requests-POST.md).

Continue to the [Export walkthrough](export.md).
