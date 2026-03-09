# Open a Potential Change Order (PCO)

Source: https://aps.autodesk.com/en/docs/acc/tutorials/cost/open-pco/

---

# Open a Potential Change Order (PCO)

This tutorial demonstrates how to open a potential change order (PCO) through a workflow action.

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps).
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:create` `data:read` and `data:write` scopes.
- Verify that you have access to the relevant BIM 360 account and BIM 360 project.
- Retrieve the project ID for your project. To obtain a project ID, use [GET projects](../http-docs/http-admin-accounts-accountidprojects-GET.md).
- Ensure that there is a PCO in the project. If there isnât a PCO in the project, see [Create a Potential Change Order (PCO)](https://aps.autodesk.com/en/docs/bim360/v1/tutorials/create-pco/) to create one.

## [Step 1: Find a PCO in BIM 360 Cost Management](#step-1-find-a-pco-in-bim-360-cost-management)

Find the ID of the PCO by calling [GET PCO](../http-docs/http-cost-change-orders-changeOrder-GET.md). In this example, assume that the container ID is `18ece8b1-204d-11e8-ad71-d73b169f902a` .

### Request

```
curl 'https://developer.api.autodesk.com/cost/v1/containers/18ece8b1-204d-11e8-ad71-d73b169f902a/change-orders/pco?limit=100&offset=0' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0'

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

In this example, the PCO ID is in the first part of the response (`results[0].id`) which is `55254a50-44d9-11e9-99d7-79aa05d3109e`. Youâll use it in the next step.

## [Step 2: Find the Available Actions For the PCO](#step-2-find-the-available-actions-for-the-pco)

Use the PCO ID (`55254a50-44d9-11e9-99d7-79aa05d3109e`) to call [GET actions](../http-docs/http-cost-actions-GET.md) to get the available actions for the PCO.
All the actions are associated to an items in Cost Management, for example change order, by the associationId and associationType. For a PCO, the associationId value is the PCO ID `55254a50-44d9-11e9-99d7-79aa05d3109e` and the associationType value is `FormInstance`.

### Request

```
curl 'https://developer.api.autodesk.com/cost/v1/containers/18ece8b1-204d-11e8-ad71-d73b169f902a/workflows/FormInstance/5254a50-44d9-11e9-99d7-79aa05d3109e/actions' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0' -H 'Content-Type: application/json'

```

### Response

```
[{
    "name": "open",
    "transforms": [{
            "key": "budgetStatusId",
            "to": "open"
        },
        {
            "key": "costStatusId",
            "to": "open"
        }
    ],
    "rules": [{
            "key": "budgetStatusId",
            "only": ["draft"]
        },
        {
            "key": "costStatusId",
            "only": ["draft"]
        }
    ]
}]

```

Show More

The name `open` is the action we can perform on this PCO. The transforms are what the action will perform on the PCO in this action: setting `budgetStatusId` and `costStatusId` to``open``. The rules are the conditions required to perform the action. For example, we can only perform the `open` action when both the `budgetStatus` and `costStatus` are set to `draft`, otherwise the action will fail.

## [Step 3: Open the PCO](#step-3-open-the-pco)

Use the action `open` and the PCO ID to call [POST cost/v1/containers/:containerId/workflows/actions](../http-docs/http-cost-actions-POST.md)

### Request

```
curl -X POST 'https://developer.api.autodesk.com/cost/v1/containers/18ece8b1-204d-11e8-ad71-d73b169f902a/workflows/actions' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0' \
-H 'Content-Type: application/json'
-d '[
        {
            "action": "open",
            "associationId": "55254a50-44d9-11e9-99d7-79aa05d3109e",
            "associationType": "FormInstance",
        }
    ]'

```

Show More

### Response

```
[
    {
        "action": "open",
        "associationId": "55254a50-44d9-11e9-99d7-79aa05d3109e",
        "associationType": "FormInstance",
        "errors": []
    }
]

```

Show More

If the action succeeded, the `errors` value in the response will be empty. If the action failed, the `errors` value will include details about why the action failed.

Congratulations! You have opened the PCO and now can start using other change processes.
