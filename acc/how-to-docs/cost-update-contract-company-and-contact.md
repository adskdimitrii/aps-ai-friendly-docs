# Update a Contract’s Company

Source: https://aps.autodesk.com/en/docs/acc/tutorials/cost/update-contract-company-and-contact/

---

# Update a Contract’s Company

This tutorial demonstrates how to get the company list from BIM 360 Admin and update the supplier company of a contract.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:read` and `data:write` scopes.
- Verify that you have access to the relevant BIM 360 account and BIM 360 project.
- Retrieve the project ID for your project. To obtain a project ID, use [GET projects](../http-docs/http-admin-accounts-accountidprojects-GET.md).
- A couple of contracts have been created or imported.

## [Step 1: Find a Contract in BIM 360 Cost Management](#step-1-find-a-contract-in-bim-360-cost-management)

Find the ID of the contract you want to update by calling [GET Contracts](../http-docs/http-cost-contracts-GET.md). In this example, assume that the container ID is `e94b9bc8-1775-4d76-9b1d-c613e120ccff` .

### Request

```
curl 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/contracts?limit=100&offset=0' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0'

```

### Response

```
{
  "results": [{
      "id": "55254a50-44d9-11e9-99d7-79aa05d3109e",
      "...":"...",
  }],
  "pagination": {
      "totalResults": 1,
      "limit": 100,
      "offset": 0
  }
}

```

Show More

In this example, the contract ID is in the first part of the response (`results[0].id`). It’s `55254a50-44d9-11e9-99d7-79aa05d3109e`. You’ll use it in the next step.

## [Step 2: Get the Project’s Companies from BIM 360 Admin](#step-2-get-the-project-s-companies-from-bim-360-admin)

Use the project ID (`18ece8b1-204d-11e8-ad71-d73b169f902a`) and account ID(`aade5ed8-f16d-4ec0-9c0a-59f5ff7a2134`) to call [GET companies](../http-docs/http-projects--project_id-companies-GET.md) to get the project’s companies and find the `member_group_id` of the company you want.

### Request

```
curl -v 'https://developer.api.autodesk.com/hq/v1/accounts/aade5ed8-f16d-4ec0-9c0a-59f5ff7a2134/projects/18ece8b1-204d-11e8-ad71-d73b169f902a/companies?limit=1&offset=0' -H 'Authorization: Bearer 07YyCEjv3qs8FA7ysntmsuErYXHv'

```

### Response

```
[
    {
        "id": "fc830fd8-f1ef-4cd6-9163-fb115dc698d7",
        "account_id": "aade5ed8-f16d-4ec0-9c0a-59f5ff7a2134",
        "project_id": "18ece8b1-204d-11e8-ad71-d73b169f902a",
        "name": "Autodesk",
        "trade": "Concrete",
        "address_line_1": "The Fifth Avenue",
        "address_line_2": "#301",
        "city": "New York",
        "postal_code": "10011",
        "state_or_province": "New York",
        "country": "United States",
        "phone": "(503)623-1525",
        "website_url": "http://www.autodesk.com",
        "description": "Autodesk, Inc., is a leader in 3D design, engineering and entertainment software.",
        "created_at": "2016-05-20T02:24:21.400Z",
        "updated_at": "2016-05-20T02:24:21.400Z",
        "erp_id": "c79bf096-5a3e-41a4-aaf8-a771ed329047",
        "tax_id": "213-73-8867",
        "member_group_id": "764893"
    }
]

```

Show More

Find the company you want by name in the response and note its `member_group_id` value. This is the company ID. We’ll use it to update the contract’s company.

## [Step 3: Update the Contract](#step-3-update-the-contract)

Use the container ID (`e94b9bc8-1775-4d76-9b1d-c613e120ccff`), contract ID(`55254a50-44d9-11e9-99d7-79aa05d3109e`), and company ID (`764893`) noted above to call [PATCH contracts/:id](../http-docs/http-cost-contracts-contractId-PATCH.md) to update the contract.

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/contracts/55254a50-44d9-11e9-99d7-79aa05d3109e' -X 'PATCH' -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' -H 'Content-Type: application/json' -d '{"companyId": "764893",}'

```

### Response

You’ll get the full content of the updated contract.

```
{
  "id": "f6445638-ca68-4e3c-9160-15864de6b818",
  "code": "GC-01",
  "name": "Site Management Staff",
  "description": "Site Management Staff",
  "companyId": "764893",
  "type": "consultant",
  "...": "..."
}

```

Show More

Congratulations! You have successfully updated the contract’s company.
