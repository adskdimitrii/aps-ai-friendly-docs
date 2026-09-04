# API Basics

Source: https://aps.autodesk.com/en/docs/tokenflex/developers_guide/basics/

---

# API Basics

The Token Flex Usage Data API is separated into three categories:

- *Metadata:* Use these endpoints to get contract details, provisioned tokens by token pool, and customer provided custom category field labels.
- *Usage:* Use these endpoints to retrieve monthly aggregated usage details, such as token consumption by product/service, unique users, custom category, servers, versions, and token adjustments. Also use these APIs to construct ad hoc analytical queries of Token Flex CORE usage data (for example, to obtain a count of tokens consumed for selected desktop products and cloud services for the past seven days). To get started with the query API, see the [walkthrough](../how-to-docs/query.md).
- *Export:* Use these endpoints to receive a bulk export of usage data in CSV file format. Export requests can also be scheduled and managed using this API.


This diagram outlines workflow when using the API. When acquiring a 3-Legged OAuth access token, the associated user must be a Token Flex administrator. Otherwise, [GET contract](../http-docs/http-contract-GET.md) does not return a contract number. All other endpoints require a contract number. Reports return JSON in response to the query endpoint. To download CSV reports, use the export endpoint (see the [walkthrough](../how-to-docs/export.md)).

## [Getting Started](#getting-started)

Use the [Reference Guide](https://aps.autodesk.com/en/docs/tokenflex/v1/reference/http/) to obtain information about interacting with the different API endpoints.
