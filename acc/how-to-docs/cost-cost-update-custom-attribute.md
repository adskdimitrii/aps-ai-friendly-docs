# Update a PCOâs Custom Attributes

Source: https://aps.autodesk.com/en/docs/acc/tutorials/cost/cost-update-custom-attribute/

---

# Update a PCOâs Custom Attributes

This tutorial demonstrates how to update a PCOâs custom attributes.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:read` and `data:write` scopes.
- Verify that you have access to the relevant BIM 360 account and BIM 360 project.
- Retrieve the project ID for your project. To obtain a project ID, use [GET projects](../http-docs/http-admin-accounts-accountidprojects-GET.md).
- Create PCOs and add custom attributes in the BIM 360 Project Admin module. See the [`](#id1)Help documentation <<https://help.autodesk.com/view/BIM360D/ENU/?guid=BIM360D_Cost_Management_about_cost_management_html>> for more information.

## [Step 1: Get a PCO in BIM 360 Cost Management](#step-1-get-a-pco-in-bim-360-cost-management)

Find the ID of the PCO you want to update by calling [GET change-orders/:changeOrder](../http-docs/http-cost-change-orders-changeOrder-GET.md). In this example, assume that the container ID is `e94b9bc8-1775-4d76-9b1d-c613e120ccff`. Add the `include=attributes` query string parameter to include the custom attributes in the response.

### Request

```
curl 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/change-orders/pco?limit=100&offset=0&include=attributes' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0'

```

### Response

```
{
        "results": [{
        "id": "1a53c5c0-61b6-11e8-b4c8-f7f2ad363daa",
        "number": "0001",
        "name": "Revised Entrance Layout",
        "scope": "out",
        "type": "",
        "description": "",
        "note": "",
        "...": "...",
        "createdAt": "2018-05-27T13:58:58.844Z",
        "updatedAt": "2018-12-26T05:40:42.665Z",
        "properties": [{
            "name": "Revised Substantial Completion",
            "value": "2020-6-1",
            "propertyDefinitionId": "9240df60-61b5-11e8-9d14-7f96380922a0",
            "...": "...",
        }]
    }],
    "pagination": {
        "totalResults": 1,
        "limit": 100,
        "offset": 0
    }
}

```

Show More

Note the PCO ID (`results[0].id`) in the first part of the response - `55254a50-44d9-11e9-99d7-79aa05d3109e`, and the custom attribute definition ID (`9240df60-61b5-11e8-9d14-7f96380922a0`).

## [Step 2: Update the Custom Attribute Value](#step-2-update-the-custom-attribute-value)

Use the container ID (`e94b9bc8-1775-4d76-9b1d-c613e120ccff`), PCO ID (`55254a50-44d9-11e9-99d7-79aa05d3109e`), and custom attribute definition ID (`9240df60-61b5-11e8-9d14-7f96380922a0`) to call [POST property-values:batch-update](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/cost-property-valuesbatch-update-POS/) to update the custom attribute value.

### Request

```
curl -v 'https://developer.api.autodesk.com/cost/v1/containers/e94b9bc8-1775-4d76-9b1d-c613e120ccff/property-values:batch-update' -X 'POST' -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' -H 'Content-Type: application/json' \
-d '[{associationId: "55254a50-44d9-11e9-99d7-79aa05d3109e", associationType: "FormInstance", propertyDefinitionId: "9240df60-61b5-11e8-9d14-7f96380922a0", value: "2020-06-16T16:00:00.000Z"}]'

```

For change orders including PCOs, the `associationType` is `FormInstance`, and the PCO ID is `associationId`. For other modules, the `associationType` is the module name, for example, `Budget`, or `Contract`, and the `associationId` is always the empty UUID `00000000-0000-0000-0000-000000000000`.

### Response

You get the full content of the updated custom attribute value.

```
[{
      "name": "Revised Substantial Completion",
      "value": "2020-06-16T16:00:00.000Z",
      "propertyDefinitionId": "9240df60-61b5-11e8-9d14-7f96380922a0",
  "...": "...",
}]

```

Multiple custom attributes can be updated altogether.

Congratulations! You have successfully updated the PCOâs custom attribute value.
