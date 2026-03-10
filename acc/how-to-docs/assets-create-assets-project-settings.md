# Setup ACC Assets Project Settings

Source: https://aps.autodesk.com/en/docs/acc/tutorials/assets/create-assets-project-settings/

---

# Setup ACC Assets Project Settings

This tutorial demonstrates how to setup a new Autodesk Construction Cloud project’s Asset settings. This will include:

- Creating new categories
- Creating new status sets with Asset statuses
- Creating new Asset custom attributes
- Assigning status sets to the desired categories
- Assigning Asset custom attributes to the desired categories
- Adding relationships between categories and other entities (e.g. form templates)

For more details about Autodesk Construction Cloud Assets API, see the [Assets Field Guide](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/assets/).

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps), and select the Data Management and Autodesk Construction Cloud APIs.
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:create` `data:read` and `data:write` scopes.
- Verify that you have access to the relevant Autodesk Construction Cloud account, project, and folder.
- Retrieve the relevant [ACC account and project ID](getting-started-retrieve-account-and-project-id.md). In this tutorial we will use the example project ID `f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`, but you should replace that with the project ID you have retrieved for your project.

## [Step 1: Create Categories](#step-1-create-categories)

Categories are the core organizational structure for assets. Every asset must have a category assignment. The category of an asset in turn determines which Asset statuses are valid for the asset, as well as which custom attributes the asset has. For more discussion on how assets, categories, status sets / statuses, and custom attributes all fit together conceptually, please see the [Assets Field Guide Data Model](https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/assets/#a-settings-components-diagram).

To create a category, use the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`) to call [POST assets/v1/projects/:projectId/categories](../http-docs/http-assets-categories-POST.md).

Every project has a ROOT category created automatically that cannot be altered. When creating a new category, a `parentId` must be included. For the first category creation(s), you may need to call [GET assets/v1/projects/:projectId/categories](../http-docs/http-assets-categories-GET.md) to obtain the ROOT category ID to use as the `parentId`. In this tutorial we will use the example ROOT category ID `123`, but you should replace that with the ROOT category ID you have retrieved for your project.

[*2022-10-08*] You can now add a query parameter `includeUid` to return the *universally* unique category ID for the category. This universally unique ID will be generated upon creation regardless of the query parameter, but will not be included in the response unless flagged to do so. This universally unique category ID will be used with upcoming versions of category APIs.

### Request

```
curl 'https://developer.api.autodesk.com/construction/assets/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/categories?includeUid=true' \
     -X 'POST' \
     -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
     -H 'Content-Type: application/json' \
     -d '{
           "name": "Electrical",
           "description": "Electrical Outlets",
           "parentId": "123"
         }'

```

Show More

### Response

```
{
  "id": "124",
  "uid": "fc24ff3b-1ad9-4327-a91d-84700bc16a5e",
  "createdAt": "2020-05-01T06:00:00.000Z",
  "createdBy": "LA7ZL85MU7ML",
  "updatedAt": "2020-05-01T06:00:00.000Z",
  "updatedBy": "LA7ZL85MU7ML",
  "isActive": true,
  "name": "Electrical",
  "description": "Electrical Outlets",
  "parentId": "123",
  "isRoot": false,
  "isLeaf": true,
  "subcategoryIds": [ ]
}

```

Show More

There is no batch-create API for categories at this time, so each desired category must be created individually. Create requests are subject to the relevant rate limits. For more details on Assets API rate limits, see the [Assets Rate Limits](https://aps.autodesk.com/en/docs/acc/v1/overview/rate-limits/assets-rate-limits/).

## [Step 2: Create Status Sets and Statuses](#step-2-create-status-sets-and-statuses)

Every project has a Default status set created automatically. If additional status sets are desired, status sets and Asset statuses can be created in conjunction to reduce API calls.

To create a status set with statuses, use the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`) to call [POST assets/v1/projects/:projectId/status-step-sets](../http-docs/http-assets-status-step-sets-POST.md).

### Request

```
curl 'https://developer.api.autodesk.com/construction/assets/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/status-step-sets' \
     -X 'POST' \
     -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
     -H 'Content-Type: application/json' \
     -d '{
           "name": "Electrical Status Set",
           "description": "For electrical assets",
           "values": [
             {
               "label": "Ordered",
               "description": "Electrical asset has been ordered",
               "color": "green"
             },
             {
               "label": "Delivered",
               "description": "Electrical asset has been delivered",
               "color": "blue"
             },
             {
               "label": "Installed",
               "description": "Electrical asset has been installed",
               "color": "red"
             }
           ]
         }'

```

Show More

### Response

```
{
  "id": "6eb35939-e5fb-453a-98ed-e2e11f326e73",
  "createdAt": "2020-05-01T06:00:00.000Z",
  "createdBy": "LA7ZL85MU7ML",
  "updatedAt": "2020-05-01T06:00:00.000Z",
  "updatedBy": "LA7ZL85MU7ML",
  "isActive": true,
  "version": 1,
  "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
  "name": "Electrical Status Set",
  "description": "For electrical assets",
  "isDefault": false,
  "values": [
    {
      "id": "b302d910-b5e3-46ba-81d8-6b6d30406e14",
      "label": "Ordered",
      "description": "Electrical asset has been ordered",
      "color": "green",
      "statusStepSetId": "6eb35939-e5fb-453a-98ed-e2e11f326e73",
      "createdAt": "2020-05-01T06:00:00.000Z",
      "createdBy": "LA7ZL85MU7ML",
      "updatedAt": "2020-05-01T06:00:00.000Z",
      "updatedBy": "LA7ZL85MU7ML",
      "isActive": true,
      "version": 2,
      "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
      "bucket": "ordered_1582935184385"
    },
    {
      "id": "e0484858-1683-42fe-9136-6575e43c8eac",
      "label": "Delivered",
      "description": "Electrical asset has been delivered",
      "color": "blue",
      "statusStepSetId": "6eb35939-e5fb-453a-98ed-e2e11f326e73",
      "createdAt": "2020-05-01T06:00:00.000Z",
      "createdBy": "LA7ZL85MU7ML",
      "updatedAt": "2020-05-01T06:00:00.000Z",
      "updatedBy": "LA7ZL85MU7ML",
      "isActive": true,
      "version": 3,
      "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
      "bucket": "delivered_39572949287493"
    },
    {
      "id": "08ec4809-9280-4573-9255-be8c638707e8",
      "label": "Installed",
      "description": "Electrical asset has been installed",
      "color": "red",
      "statusStepSetId": "6eb35939-e5fb-453a-98ed-e2e11f326e73",
      "createdAt": "2020-05-01T06:00:00.000Z",
      "createdBy": "LA7ZL85MU7ML",
      "updatedAt": "2020-05-01T06:00:00.000Z",
      "updatedBy": "LA7ZL85MU7ML",
      "isActive": true,
      "version": 4,
      "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
      "bucket": "installed_927592048492"
    }
  ]
}

```

Show More

If you wish to add more statuses to the status set, you can use [POST assets/v1/projects/:projectId/asset-statuses](../http-docs/http-assets-asset-statuses-POST.md) to create statuses directly.

There is no batch-create API for status sets or statuses at this time, so each desired status set must be created individually. Create requests are subject to the relevant rate limits. For more details on Assets API rate limits, see the [Assets Rate Limits](https://aps.autodesk.com/en/docs/ac/v1/overview/rate-limits/assets-rate-limits/).

## [Step 3: Assign Status Sets to Categories](#step-3-assign-status-sets-to-categories)

Once the desired categories and status sets with statuses have been created, you can assign status sets to categories to specify which statuses are available to assets in the given category.

To assign a status set to a category, use the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`), category ID (`124`), and status set ID (`6eb35939-e5fb-453a-98ed-e2e11f326e73`) to call [PUT assets/v1/projects/:projectId/categories/:categoryId/status-step-set/:statusStepSetId](../http-docs/http-assets-categories-category-id-status-step-set-status-step-set-id-PUT.md). Note: there is no body for this request.

### Request

```
curl 'https://developer.api.autodesk.com/construction/assets/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/categories/124/status-step-set/6eb35939-e5fb-453a-98ed-e2e11f326e73' \
     -X 'PUT' \
     -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT'

```

### Response

```
{
  "id": "4b9382eb-9434-41b5-8ca2-8e81a7a596cf",
  "createdAt": "2020-05-01T06:00:00.000Z",
  "createdBy": "LA7ZL85MU7ML",
  "updatedAt": "2020-05-01T06:00:00.000Z",
  "updatedBy": "LA7ZL85MU7ML",
  "isActive": true,
  "version": 5,
  "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
  "categoryId": "124",
  "statusStepSetId": "6eb35939-e5fb-453a-98ed-e2e11f326e73"
}

```

Show More

There is no batch API for status set to category assignments at this time, so each assignment must be created individually. Create requests are subject to the relevant rate limits. For more details on Assets API rate limits, see the [Assets Rate Limits](https://aps.autodesk.com/en/docs/acc/v1/overview/rate-limits/assets-rate-limits/).

## [Step 4: Create Custom Attributes](#step-4-create-custom-attributes)

To create custom attributes, use the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`) to call [POST assets/v1/projects/:projectId/custom-attributes](../http-docs/http-assets-custom-attributes-POST.md).

The exact schema of the body to create a custom attribute depends on the type of custom attribute being created -

| Field | Conditions |
| --- | --- |
| `enumValues` | Only valid, and required, for `select` and `multi_select` custom attribute data types. |
| `maxLengthOnIngress` | Only valid for `text` custom attribute data types. |
| `defaultValue` | String for `text`, `date`, or `select` custom attribute data types. Number for `numeric` custom attribute data types. Boolean for `boolean` custom attribute data types. Array of strings for `multi_select` custom attribute data types. |

### Request

```
curl 'https://developer.api.autodesk.com/construction/assets/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/custom-attributes' \
     -X 'POST' \
     -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
     -H 'Content-Type: application/json' \
     -d '{
           "displayName": "Voltage",
           "description": "Voltage of the electrical asset",
           "enumValues": [
             "110 V",
             "220 V"
           ],
           "requiredOnIngress": true,
           "defaultValue": "110 V",
           "dataType": "select"
         }'

```

Show More

### Response

```
{
  "id": "3063f212-6ce9-494e-b749-eb73b4445bf0",
  "displayName": "Voltage",
  "description": "Voltage of the electrical asset",
  "enumValues": [
    "110 V",
    "220 V"
  ],
  "requiredOnIngress": true,
  "defaultValue": "110 V",
  "dataType": "select",
  "createdAt": "2020-05-01T06:00:00.000Z",
  "createdBy": "LA7ZL85MU7ML",
  "updatedAt": "2020-05-01T06:00:00.000Z",
  "updatedBy": "LA7ZL85MU7ML",
  "isActive": true,
  "version": 7,
  "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
  "name": "ca1",
  "values": [
    {
      "id": "fd0e4a00-26df-454e-8fba-e76652aa55b4",
      "createdAt": "2020-05-01T06:00:00.000Z",
      "createdBy": "LA7ZL85MU7ML",
      "updatedAt": "2020-05-01T06:00:00.000Z",
      "updatedBy": "LA7ZL85MU7ML",
      "isActive": true,
      "version": 8,
      "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
      "customAttributeId": "3063f212-6ce9-494e-b749-eb73b4445bf0",
      "displayName": "110 V"
    },
    {
      "id": "582eac28-f4e4-475d-b38c-fd57997c9cc6",
      "createdAt": "2020-05-01T06:00:00.000Z",
      "createdBy": "LA7ZL85MU7ML",
      "updatedAt": "2020-05-01T06:00:00.000Z",
      "updatedBy": "LA7ZL85MU7ML",
      "isActive": true,
      "version": 9,
      "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
      "customAttributeId": "3063f212-6ce9-494e-b749-eb73b4445bf0",
      "displayName": "220 V"
    }
  ]
}

```

Show More

There is no batch-create API for Assets custom attributes at this time, so each Assets custom attribute must be created individually. Create requests are subject to the relevant rate limits. For more details on Assets API rate limits, see the [Assets Rate Limits](https://aps.autodesk.com/en/docs/acc/v1/overview/rate-limits/assets-rate-limits/).

## [Step 5: Assign Custom Attributes to Categories](#step-5-assign-custom-attributes-to-categories)

Once the desired categories and custom attributes have been created, you can assign custom attributes to categories to specify which attributes are available to assets in the given category.

To assign a custom attribute to a category, use the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`), category ID (`124`), and custom attribute ID (`3063f212-6ce9-494e-b749-eb73b4445bf0`) to call [PUT assets/v1/projects/:projectId/categories/:categoryId/custom-attributes/:customAttributeId](../http-docs/http-assets-categories-category-id-custom-attributes-custom-attribute-id-PUT.md).

This endpoints will return the custom attributes assigned to the given category. By default this will only return the custom attributes explicitly assigned to the given category. If you wish to return the full set of custom attributes assigned to the given category, you can set the query parameter `includeInherited=true`. When `includeInherited=true` is set, an additional field will be included in the response for each returned custom attribute `inheritedFromCategoryId` which will indicate from which explicit category assignment the custom attribute is inherited from.

### Request

```
curl 'https://developer.api.autodesk.com/construction/assets/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/categories/124/custom-attributes/3063f212-6ce9-494e-b749-eb73b4445bf0?includeInherited=true' \
     -X 'PUT' \
     -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT'

```

### Response

```
{
  "pagination": {
    "limit": 25,
    "offset": 0,
    "totalResults": 1
  },
  "results": [
    {
      "id": "3063f212-6ce9-494e-b749-eb73b4445bf0",
      "displayName": "Voltage",
      "description": "Voltage of the electrical asset",
      "enumValues": [
        "110 V",
        "220 V"
      ],
      "requiredOnIngress": true,
      "defaultValue": "110 V",
      "dataType": "select",
      "createdAt": "2020-05-01T06:00:00.000Z",
      "createdBy": "LA7ZL85MU7ML",
      "updatedAt": "2020-05-01T06:00:00.000Z",
      "updatedBy": "LA7ZL85MU7ML",
      "isActive": true,
      "version": 7,
      "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
      "name": "ca1",
      "values": [
        {
          "id": "fd0e4a00-26df-454e-8fba-e76652aa55b4",
          "createdAt": "2020-05-01T06:00:00.000Z",
          "createdBy": "LA7ZL85MU7ML",
          "updatedAt": "2020-05-01T06:00:00.000Z",
          "updatedBy": "LA7ZL85MU7ML",
          "isActive": true,
          "version": 8,
          "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
          "customAttributeId": "3063f212-6ce9-494e-b749-eb73b4445bf0",
          "displayName": "110 V"
        },
        {
          "id": "582eac28-f4e4-475d-b38c-fd57997c9cc6",
          "createdAt": "2020-05-01T06:00:00.000Z",
          "createdBy": "LA7ZL85MU7ML",
          "updatedAt": "2020-05-01T06:00:00.000Z",
          "updatedBy": "LA7ZL85MU7ML",
          "isActive": true,
          "version": 9,
          "projectId": "f6a1e3b5-abaa-4b01-b33a-5d55f36ba047",
          "customAttributeId": "3063f212-6ce9-494e-b749-eb73b4445bf0",
          "displayName": "220 V"
        }
      ],
      "inheritedFromCategoryId": "124"
    }
  ]
}

```

Show More

## [Step 6: Create Category Attachments](#step-6-create-category-attachments)

Once the desired categories have been created, you can attach form templates to the categories to specify which forms are available to assets in a given category.

You can obtain the available form template IDs for your project using [GET forms/v1/projects/:projectId/form-templates](../http-docs/http-forms-form-templates-GET.md). In this tutorial we will use the example form template ID `2f634a22-779d-4930-9f08-8391a41fea05`, but you should replace that with your own form template ID.

To attach a form template to a category, the preferred means is to use the Relationship API. For more information on how to create relationships please see Create Relationships tutorial</en/docs/bim360/v1/tutorials/relationships/relationships-create/>.

[*2022-10-08*] It is preferred to create category relationships with the new *universally* unique category ID. The `type` with which to create you category relationship depends on which type of category ID you are using - to create a realtionship with the new *universally* unique category ID, please use the `"type": "categoryuid"`, to create a realtionship with the *legacy* category integer ID, please use `"type": "category"`. The example below uses the new `categoryuid` type along with the universally unique category ID obtained above `fc24ff3b-1ad9-4327-a91d-84700bc16a5e`.

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/relationships' \
     -X 'PUT' \
     -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
     -H 'Content-Type: application/json' \
     -d '[{
            "entities": [
              {
                "id": "fc24ff3b-1ad9-4327-a91d-84700bc16a5e",
                "domain": "autodesk-bim360-asset",
                "type": "categoryuid"
              }
              {
                "id": "2f634a22-779d-4930-9f08-8391a41fea05",
                "domain": "autodesk-construction-form",
                "type": "formtemplate"
              }
            ]
         }]'

```

Show More

### Response

```
[
  {
    "id": "52d7cecf-9f88-4aa2-b725-a6e09a0bc549",
    "createdOn": "2020-05-01T06:00:00.000Z",
    "isReadOnly": false,
    "isService": false,
    "isDeleted": false,
    "entities": [
      {
        "id": "fc24ff3b-1ad9-4327-a91d-84700bc16a5e",
        "domain": "autodesk-bim360-asset",
        "type": "categoryuid",
        "createdOn": "2020-05-01T06:00:00.000Z"
      },
      {
        "id": "b1d1e7d4-f0ed-11e9-81b4-2a2ae2dbcce4",
        "type": "formtemplate",
        "domain": "autodesk-construction-form",
        "createdOn": "2020-05-01T06:00:00.000Z"
      }
    ]
  }
]

```

Show More
