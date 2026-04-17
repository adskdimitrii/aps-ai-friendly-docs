# Integrating Cost Management with External ERP Systems

Source: https://aps.autodesk.com/en/docs/acc/tutorials/cost/integrate-with-external-system/

---

# Integrating Cost Management with External ERP Systems

This tutorial demonstrates how to integrate entities, such as budgets, with an external ERP system. It covers two options: integrating an existing BIM 360/Forma budget with an external ERP system and integrating an existing budget from an external ERP system into a BIM 360/Forma budget. The steps include finding the relevant budget, updating the integration-related fields, and verifying synchronization between the systems.

Note that we support integrating the following entities with external ERP systems: budgets, contracts, main contracts, main contract items, cost items, expenses, expense items, change orders, and schedules of values.

For more information about external ERP system integrations, see the [Help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Cost_Integrations).

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:read` and `data:write` scopes.
- Verify that you have access to the relevant BIM 360 account or Forma hub and BIM 360 or Forma project.
- Retrieve the project ID for your project. To obtain a project ID, use [GET projects](../http-docs/http-admin-accounts-accountidprojects-GET.md).
- For this tutorial, use the external ERP system `Morpheus`, and assume that the external ID is `M001`, and the integration state is `locked`.
- Ensure that you have a budget created in your BIM 360/Forma project and that a corresponding budget exists in the external ERP system.

## [Option 1: Sync BIM 360/Forma Budget Information to an ERP System](#option-1-sync-bim-360-forma-budget-information-to-an-erp-system)

This option demonstrates how to sync an existing budget from BIM 360/Forma to an external ERP system. The steps include retrieving the budget ID from BIM 360/Forma, updating the integration-related fields, and mapping it to the external ERP system.

### Step 1: Find a Budget in BIM 360/Forma Cost Management

Call [GET budgets](../http-docs/http-cost-budgets-GET.md) with the container ID `71e6b356-a101-4277-b4ca-98989bff4a90` to retrieve the budget ID needed to sync the BIM 360/Forma budget with the external ERP system.

### Request

```
curl 'https://developer.api.autodesk.com/cost/v1/containers/71e6b356-a101-4277-b4ca-98989bff4a90/budgets?limit=100&offset=0' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5I00'

```

### Response

```
{
  "results": [{
      "formattedCode": "001",
      "origCommitment": "50.0000",
      "id": "bb8cf933-a5ab-47f1-9103-fe6804303f07",
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

Use the budget ID `bb8cf933-a5ab-47f1-9103-fe6804303f07` to update the budget with integration information in the next step.

### Step 2: Create a Mapping to the ERP System

To map the budget in BIM 360/Forma to the external ERP system, use the retrieved budget ID (`bb8cf933-a5ab-47f1-9103-fe6804303f07`), container ID (`71e6b356-a101-4277-b4ca-98989bff4a90`), external system name (`Morpheus`), external ID (`M001`), and set the integration state to `locked` by calling [PATCH budgets](../http-docs/http-cost-budgets-budgetId-PATCH.md).

### Request

```
   curl -v 'https://developer.api.autodesk.com/cost/v1/containers/71e6b356-a101-4277-b4ca-98989bff4a90/budgets/ bb8cf933-a5ab-47f1-9103-fe6804303f07' -X 'PATCH' -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' -H 'Content-Type: application/json' \
-d '{
     "externalMessage": "success",
     "externalSystem": "morpheus",
     "externalId": "M001",
     "integrationState": "locked",
     "lastSyncTime": "2024-02-27T10:00:00.354Z"
   }'

```

Show More

### Response

```
{
    "formattedCode": "l1",
    "id": "bb8cf933-a5ab-47f1-9103-fe6804303f07",
    "containerId": "71e6b356-a101-4277-b4ca-98989bff4a90",
    "parentId": null,
    "rootId": null,
    "name": "l1",
    "code": "l1",
    "scope": "budgetAndCost",
    "description": null,
    "quantity": 1,
    "unitPrice": "100.00000000",
    "...": "...",
    "externalSystem": "morpheus",
    "externalId": "M001",
    "externalMessage": "success",
    "integrationState": "locked",
    "lastSyncTime": "2024-02-27T10:00:00.354Z",
    "mainContract": {
        "id": "d1109c69-d70e-49df-bc88-05032089ead9",
        "name": "mainContract1"
    },
    "...": "..."
}

```

Show More

The budget in BIM 360 is now integrated with the external ERP system. The integrated items’ information can be retrieved from the external ERP system by calling [GET budgets](../http-docs/http-cost-budgets-budgetId-GET.md).

## [Option 2: Sync an ERP System to a BIM 360/Forma Budget](#option-2-sync-an-erp-system-to-a-bim-360-forma-budget)

This option demonstrates how to sync an existing budget from an external ERP system into BIM 360/Forma. The steps include creating a synchronized budget in BIM 360/Forma with the relevant integration information and setting the integration state.

### Step 1: Create a BIM 360/Forma Budget with Integration Information

This step will create the budget inside of Cost Management, linking it to the specified external ERP system.

To sync an existing budget from an external ERP system into BIM 360/Forma, use the container ID (`71e6b356-a101-4277-b4ca-98989bff4a90`), the external system (`MORPHEUS`), the external ID (`M001`), and set the integration state to `locked` to call [POST budgets](../http-docs/http-cost-budgets-POST.md).

### Request:

```
curl --location 'https://developer.api.autodesk.com/construction/cost/v1/projects/71e6b356-a101-4277-b4ca-98989bff4a90/budgets' \
--header 'Content-Type: application/json' \
--data '{
    "code": "1",
    "name": "1",
    "quantity": 1,
    "unitPrice": 0,
    "unit": "ea",
    "segmentCodeMap": {},
    "externalSystem": "morpheus",
    "externalId": "M001",
    "externalMessage": "success",
    "integrationState": "locked",
    "lastSyncTime": "2024-01-23T21:51:57.775Z"
}'

```

Show More

### Response:

```
{
    "formattedCode": "",
    "id": "b16ac870-e151-11ee-b31d-0969f47312bd",
    "containerId": "71e6b356-a101-4277-b4ca-98989bff4a90",
    "name": "1",
    "code": "1",
    "scope": "budgetAndCost",
    "description": null,
    "quantity": 1,
    "unitPrice": "0.00000000",
    "inputQuantity": null,
    "ratio": 1,
    "unit": "ea",
    "originalAmount": "0.0000",
    "budgetCodeId": "b1683060-e151-11ee-b31d-0969f47312bd",
    "contractId": null,
    "mainContractId": "d1109c69-d70e-49df-bc88-05032089ead9",
    "mainContractItemId": null,
    "creatorId": "WHA2J3KBMHKRQCHD",
    "changedBy": "WHA2J3KBMHKRQCHD",
    "createdAt": "2024-03-13T15:52:28.024Z",
    "updatedAt": "2024-03-13T15:52:28.049Z",
    "integrationStateChangedAt": "2024-03-13T15:52:28.024Z",
    "integrationStateChangedBy": "WHA2J3KBMHKRQCHD",
    "isTracked": false,
    "distributionItemId": null,
    "externalSystem": "morpheus",
    "externalId": "MB002",
    "externalMessage": null,
    "integrationState": "locked",
    "lastSyncTime": "2024-01-23T21:51:57.775Z",
    "mainContract": {
        "id": "d1109c69-d70e-49df-bc88-05032089ead9",
        "name": "mainContract1"
    },
    "mainContractItem": null,
    "properties": [],
    "budgetCode": "l1",
    "...": "..."
}

```

Show More

Congratulations! The budget is now synchronized between BIM 360/Forma and the external ERP system.
