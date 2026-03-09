# Link Budgets to Contracts (new)

Source: https://aps.autodesk.com/en/docs/acc/tutorials/cost/link-budgets-and-contract-new/

---

# Link Budgets to Contracts (new)

This tutorial demonstrates how to link budgets to contracts. The steps include finding the ID of the contracts you want to link to, finding the ID of the relevant budgets and linking them to each other.

Note that this workflow is replacing the current workflow that can only link a single budget to a single contract.

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:read` and `data:write` scopes.
- Verify that you have access to the relevant BIM 360 or ACC account and BIM 360 or ACC project.
- Retrieve the project ID for your project. To obtain a project ID, use [GET projects](../http-docs/http-admin-accounts-accountidprojects-GET.md).
- Ensure that you have created or imported multiple budgets and, if needed, multiple contracts for linking and unlinking operations in your project.

## [Step 1: Find a List of Contracts](#step-1-find-a-list-of-contracts)

To find a list of contracts you want to link to, use the containter ID (`18ece8b1-204d-11e8-ad71-d73b169f902a`), to call [GET Contracts](../http-docs/http-cost-contracts-GET.md).

### Request

```
curl 'https://developer.api.autodesk.com/cost/v1/containers/18ece8b1-204d-11e8-ad71-d73b169f902a/contracts?limit=100&offset=0' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0'

```

### Response

```
{
  "results": [
    {
      "id": "55254a50-44d9-11e9-99d7-79aa05d3109e",
      "name": "Contract 1",
      "...":"...",
    },
    {
      "id": "55254a50-44d9-11e9-99d7-79aa05d3109f",
      "name": "Contract 2",
      "...":"...",
    }
  ],
  "pagination": {
      "totalResults": 2,
      "limit": 100,
      "offset": 0
  }
}

```

Show More

In this example, assume that the contracts you want to link to are `Contract 1` and `Contract 2`. Find the contracts (`results[i].name`), and note the corresponding contract IDs (`results[i].id`) - `55254a50-44d9-11e9-99d7-79aa05d3109e` and `55254a50-44d9-11e9-99d7-79aa05d3109f`.

## [Step 2: Find the Relevant Budgets](#step-2-find-the-relevant-budgets)

To find the IDs of the budgets you want to link to the contract, use the containter ID (`18ece8b1-204d-11e8-ad71-d73b169f902a`), to call [GET Budgets](../http-docs/http-cost-budgets-GET.md).

### Request

```
curl 'https://developer.api.autodesk.com/cost/v1/containers/18ece8b1-204d-11e8-ad71-d73b169f902a/budgets?limit=100&offset=0' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0'

```

### Response

```
{
  "results": [
    {
      "name": "Doors",
      "id": "5573e292-4355-4d00-a204-2cba97b7025a",
      "...":"...",
    },
    {
      "name": "Windows",
      "id": "f7840135-dd11-45d2-9b54-b0887ab3c29b",
      "...":"...",
    },
    {
      "name": "Flooring",
      "id": "f7840135-dd11-45d2-9b54-b0887ab3c29c",
      "...":"...",
    }
  ],
  "pagination": {
      "totalResults": 3,
      "limit": 100,
      "offset": 0
  }
}

```

Show More

In this example, assume that the budgets you want to link to contracts are `Doors`, `Windows`, and `Flooring`. Find the budgets (`results[i].name`) and note the corresponding budget IDs (`results[i].id`) - `5573e292-4355-4d00-a204-2cba97b7025a`, `f7840135-dd11-45d2-9b54-b0887ab3c29b` and `f7840135-dd11-45d2-9b54-b0887ab3c29c`.

## [Step 3: Link Budgets to Contracts](#step-3-link-budgets-to-contracts)

To link budgets to contracts, use the containter ID (`18ece8b1-204d-11e8-ad71-d73b169f902a`), the contract IDs (`55254a50-44d9-11e9-99d7-79aa05d3109e`, `55254a50-44d9-11e9-99d7-79aa05d3109f`), and the budget IDs (`5573e292-4355-4d00-a204-2cba97b7025a`, `f7840135-dd11-45d2-9b54-b0887ab3c29b`, `f7840135-dd11-45d2-9b54-b0887ab3c29c`) to call [POST budgets-contracts:link](../http-docs/http-cost-budgets-contractslink-POST.md).

In this example, weâll link two budgets (`5573e292-4355-4d00-a204-2cba97b7025a` and `f7840135-dd11-45d2-9b54-b0887ab3c29b`) to Contract 1 (`55254a50-44d9-11e9-99d7-79aa05d3109e`) and one budget(`f7840135-dd11-45d2-9b54-b0887ab3c29c`) to Contract 2 (`55254a50-44d9-11e9-99d7-79aa05d3109f`)

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/18ece8b1-204d-11e8-ad71-d73b169f902a/budgets-contracts:link' -d '{
  "create": [
    {
      "budgetId": "5573e292-4355-4d00-a204-2cba97b7025a",
      "contractId": "55254a50-44d9-11e9-99d7-79aa05d3109e"
    },
    {
      "budgetId": "f7840135-dd11-45d2-9b54-b0887ab3c29b",
      "contractId": "55254a50-44d9-11e9-99d7-79aa05d3109e"
    },
    {
      "budgetId": "f7840135-dd11-45d2-9b54-b0887ab3c29c",
      "contractId": "55254a50-44d9-11e9-99d7-79aa05d3109f"
    },
  ]
}' -X 'POST' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0'

```

Show More

### Response

The response returns status `200`.

Congratulations! The budgets and contract are linked.

Note that you can also unlink budgets to contracts. For more information, see [POST budgets-contracts:link](https://developer.api.autodesk.com/en/docs/bim360/v1/reference/http/cost-budgets-contractslink-POST/).
