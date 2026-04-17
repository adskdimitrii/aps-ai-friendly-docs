# Manage Forms

Source: https://aps.autodesk.com/en/docs/acc/tutorials/forms/create-update-forms/

---

# Manage Forms

This tutorial demonstrates how to manage Forma Forms for a Forma project. The steps include, retrieving the form template that you want to create the form from, creating the form, adding form details, updating main form fields - both tabular and non-tabular, and submitting the form.

For more information about Forms, see the [Forms help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Build_Forms_about_forms_html).

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps), and select Forma APIs.
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:read` and `data:write` scopes.
- Find the relevant project ID, by following the [Retrieve a Project ID](getting-started-retrieve-account-and-project-id.md) tutorial. In this example, assume the project ID is `cd13503e-1265-49c3-b2da-477c57cda60c`.
- Verify that you have access to the relevant Forma project.
- Verify that you were added as a contributor to the form templates in that project, see the [Forms help documentation](https://help.autodesk.com/view/BUILD/ENU/?guid=Build_Forms_about_forms_html) for information about creating and configuring templates.

## [Step 1: Find the Form Template](#step-1-find-the-form-template)

The the project ID (`cd13503e-1265-49c3-b2da-477c57cda60c`) to call [GET form-templates](../http-docs/http-forms-form-templates-GET.md) to retrieve the templates for the project.

### request

```
curl -v 'https://developer.api.autodesk.com/construction/forms/v1/projects/cd13503e-1265-49c3-b2da-477c57cda60c/form-templates' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### response

```
{
  "pagination": {
      "limit": 50,
      "nextUrl": null,
      "offset": 0,
      "totalResults": 1
  },
  "data": [
      {
          "createdBy": "2B86MMXDQA8N",
          "forms": {
              "url": "https://developer.api.autodesk.com/construction/forms/v1/projects/cd13503e-1265-49c3-b2da-477c57cda60c/forms?templateId=a304cc08-fadb-58c8-3181-7bb06fdef93e"
          },
          "groupPermissions": [
              {
                  "permissions": [
                      "review",
                      "submit"
                  ],
                  "roleKey": "hq_access_level:project-user",
                  "roleName": "Project User"
              },
              {
                  "permissions": [
                      "review",
                      "submit",
                      "manage"
                  ],
                  "roleKey": "hq_access_level:admin",
                  "roleName": "Project Admin"
              }
          ],
          "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
          "isPdf": false,
          "name": "Example Template",
          "pdfUrl": null,
          "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
          "status": "active",
          "templateType": null,
          "updatedAt": "2023-03-10T22:08:11.545079+00:00",
          "userPermissions": [
              {
                  "permissions": [
                      "manage"
                  ],
                  "userId": "2B86MMXDQA8N"
              }
          ]
      }
  ]
}

```

Show More

Find the template ID of the template you want to create the form in `(data[i].id)` - (`a304cc08-fadb-58c8-3181-7bb06fdef93e`).

## [Step 2: Create a Form](#step-2-create-a-form)

Use the project ID (`cd13503e-1265-49c3-b2da-477c57cda60c`) and template ID (`a304cc08-fadb-58c8-3181-7bb06fdef93e`) to call [POST forms](../http-docs/http-forms-forms-POST.md) to create a form.

Note that you can optionally add attributes in the request body, such as `formDate` and `description`. If you do not include any attributes in the request body, you need to add an empty object.

### request

```
curl --location --request POST 'https://developer.api.autodesk.com/construction/forms/v1/projects/cd13503e-1265-49c3-b2da-477c57cda60c/form-templates/a304cc08-fadb-58c8-3181-7bb06fdef93e/forms' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{}'

```

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "sectionLabel": "All question types",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "sectionLabel": "All question types",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "sectionLabel": "All question types",
          "valueName": "svgVal"
      }
  ],
  "description": null,
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [],
      "materialsEntries": [],
      "worklogEntries": []
  },
  "updatedAt": "2023-03-10T22:13:03.159984+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

Note the form ID (`id`) - (`76ee8c34-1897-4720-bb4f-9ae82c9af02e`).

Note information about the tabular form fields (`tabularValues`) and the non-tabular form fields (`customValues`), which we will use for updating the main form fields.

For non-tabular fields note the ID of the field (`fieldId`), the name of the field (`itemLabel`), and the type of value that is allowed for the field (`valueName`).

## [Step 3: Add Form Details](#step-3-add-form-details)

Use the project ID (`cd13503e-1265-49c3-b2da-477c57cda60c`), the template ID (`a304cc08-fadb-58c8-3181-7bb06fdef93e`), and the form ID (`76ee8c34-1897-4720-bb4f-9ae82c9af02e`), to call [PATCH forms/:formId](../http-docs/http-forms-forms-formId-PATCH.md) to add form details to the form, such a description. For details about attributes that are included in the form details section of a form, see the [Help](https://help.autodesk.com/view/BUILD/ENU/?guid=Build_Forms_use_html) documentation.

### request

```
curl --location --request PATCH 'https://developer.api.autodesk.com/construction/forms/v1/projects/cd13503e-1265-49c3-b2da-477c57cda60c/form-templates/a304cc08-fadb-58c8-3181-7bb06fdef93e/forms/76ee8c34-1897-4720-bb4f-9ae82c9af02e' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
    "description": "Updated via the API"
  }'

```

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "svgVal"
      }
  ],
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [],
      "materialsEntries": [],
      "worklogEntries": []
  },
  "updatedAt": "2023-03-10T22:49:25.905337+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

## [Step 4: Update the Main Form Fields](#step-4-update-the-main-form-fields)

Use the project ID (`cd13503e-1265-49c3-b2da-477c57cda60c`), the form ID (`76ee8c34-1897-4720-bb4f-9ae82c9af02e`), and the relevant information field information (see Step 2) to call [PUT forms/{formId}/values:batch-update](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-valuesbatch-update-(Deprecated/)-PUT) to update the main form fields - both tabular (`tabularValues`) and non-tabular (`customValues`).

For details about attributes that are included in the main form field section of a form, see the [Help](https://help.autodesk.com/view/BUILD/ENU/?guid=Build_Forms_use_html) documentation.

Note that we do not currently support updating form fields for forms generated from PDF files.

You can update the main form fields in a number of ways. We will describe the following options:

1. Update a preconfigured response field
2. Update a text response field
3. Update a number response field
4. Update a dropdown response field
5. Update a multiple-select response field
6. Update a date field
7. Update a signature
8. Update the work log table
9. Update the equipment log table
10. Update the materials log table

### Option 1: Update a preconfigured response field

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
    "customValues": [
      {
        "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
        "toggleVal": "Yes"
      }
    ],
  }'

```

Show More

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "toggleVal": "Yes",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "sectionLabel": "All question types",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "sectionLabel": "All question types",
          "valueName": "svgVal"
      }
  ],
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [],
      "materialsEntries": [],
      "worklogEntries": []
  },
  "updatedAt": "2023-03-10T22:24:50.201013+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

### Option 2: Update a text response field

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
    "customValues": [
      {
        "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
        "textVal": "This is my response!"
      }
    ]
  }'

```

Show More

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "toggleVal": "Yes",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "textVal": "This is my response!",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "sectionLabel": "All question types",
          "valueName": "svgVal"
      }
  ],
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [],
      "materialsEntries": [],
      "worklogEntries": []
  },
  "updatedAt": "2023-03-10T22:27:35.202321+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

### Option 3: Update a number response field

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
    "customValues": [
      {
        "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
        "numberVal": "42"
      }
    ]
  }'

```

Show More

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "toggleVal": "Yes",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "textVal": "This is my response!",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "notes": null,
          "numberVal": 42.0,
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "sectionLabel": "All question types",
          "valueName": "svgVal"
      }
  ],
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [],
      "materialsEntries": [],
      "worklogEntries": []
  },
  "updatedAt": "2023-03-10T22:29:04.053634+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

### Option 4: Update a dropdown response field

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
    "customValues": [
      {
        "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
        "choiceVal": "Answer 3"
      }
    ]
  }'

```

Show More

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "toggleVal": "Yes",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "textVal": "This is my response!",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "notes": null,
          "numberVal": 42.0,
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "choiceVal": "Answer 2",
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "choiceVal": "Answer 3",
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "sectionLabel": "All question types",
          "valueName": "svgVal"
      }
  ],
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [],
      "materialsEntries": [],
      "worklogEntries": []
  },
  "updatedAt": "2023-03-10T22:31:43.644546+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

### Option 5: Update a multiple-select response field

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
    "customValues": [
      {
        "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
        "arrayVal": ["Answer 2", "Answer 3"]
      }
    ]
  }'

```

Show More

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "toggleVal": "Yes",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "textVal": "This is my response!",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "notes": null,
          "numberVal": 42.0,
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "choiceVal": "Answer 2",
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "choiceVal": "Answer 3",
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "arrayVal": "['Answer 2', 'Answer 3']",
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "sectionLabel": "All question types",
          "valueName": "svgVal"
      }
  ],
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [],
      "materialsEntries": [],
      "worklogEntries": []
  },
  "updatedAt": "2023-03-10T22:33:29.619130+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

### Option 6: Update a date field

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
    "customValues": [
      {
        "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
        "dateVal": "1999-12-31"
      }
    ]
  }'

```

Show More

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "toggleVal": "Yes",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "textVal": "This is my response!",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "notes": null,
          "numberVal": 42.0,
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "choiceVal": "Answer 2",
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "choiceVal": "Answer 3",
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "arrayVal": "['Answer 2', 'Answer 3']",
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "dateVal": "1999-12-31",
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "sectionLabel": "All question types",
          "valueName": "svgVal"
      }
  ],
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [],
      "materialsEntries": [],
      "worklogEntries": []
  },
  "updatedAt": "2023-03-10T22:35:09.886283+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

### Option 7: Update a signature

To create a signature value, start with the XML of the SVG image you want to use:

```
<svg height="200" viewBox="0 0 550 200" width="550" xmlns="http://www.w3.org/2000/svg"><path d="M 78.000,46.500 C 78.000,49.000 78.000,49.000 78.000,51.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 78.000,51.500 C 78.000,55.000 78.000,55.000 78.000,58.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 78.000,58.500 C 78.000,61.000 78.000,61.000 78.000,63.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 78.000,63.500 C 78.000,67.000 78.000,67.000 78.000,70.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 78.000,70.500 C 78.000,74.000 78.000,74.000 78.000,77.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 78.000,77.500 C 78.000,80.500 78.000,80.500 78.000,83.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 78.000,83.500 C 78.000,87.000 78.000,87.000 78.000,90.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 78.000,90.500 C 78.000,93.000 78.000,93.000 78.000,95.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 78.000,95.500 C 78.000,98.000 78.000,98.000 78.000,100.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 78.000,100.500 C 78.000,103.000 78.000,103.000 78.000,105.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 78.000,105.500 C 78.000,110.000 78.319,110.032 78.000,114.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 78.000,114.500 C 77.819,117.032 77.500,117.000 77.000,119.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 77.000,119.500 C 76.500,122.000 76.500,122.000 76.000,124.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 76.000,124.500 C 75.500,127.000 75.419,126.986 75.000,129.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 75.000,129.500 C 74.419,132.986 74.581,133.014 74.000,136.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 111.000,51.500 C 111.000,54.000 111.000,54.000 111.000,56.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 111.000,56.500 C 111.000,59.000 111.000,59.000 111.000,61.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 111.000,61.500 C 111.000,65.000 111.000,65.000 111.000,68.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 111.000,68.500 C 111.000,94.500 111.000,94.500 111.000,120.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 111.000,120.500 C 111.000,123.000 111.000,123.000 111.000,125.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 111.000,125.500 C 111.000,128.000 111.000,128.000 111.000,130.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 78.000,93.500 C 80.500,93.500 80.500,93.500 83.000,93.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 83.000,93.500 C 85.500,93.500 85.500,93.500 88.000,93.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 88.000,93.500 C 90.500,93.500 90.500,93.500 93.000,93.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 93.000,93.500 C 95.500,93.500 95.500,93.500 98.000,93.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 98.000,93.500 C 100.500,93.500 100.507,93.656 103.000,93.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 124.000,109.500 C 127.500,109.500 127.500,109.500 131.000,109.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 131.000,109.500 C 134.500,109.500 134.500,109.500 138.000,109.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 138.000,109.500 C 141.000,109.500 141.000,109.500 144.000,109.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 144.000,109.500 C 146.500,109.500 146.593,109.981 149.000,109.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 149.000,109.500 C 151.593,108.981 151.926,109.056 154.000,107.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 154.000,107.500 C 155.926,106.056 156.318,105.773 157.000,103.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 157.000,103.500 C 157.818,100.773 158.029,100.074 157.000,97.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 157.000,97.500 C 156.029,95.074 155.361,94.916 153.000,93.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 153.000,93.500 C 150.361,91.916 150.045,92.330 147.000,91.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 147.000,91.500 C 144.545,90.830 144.272,89.995 142.000,90.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 142.000,90.500 C 139.772,90.995 138.693,91.189 138.000,93.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 138.000,93.500 C 134.193,106.189 134.254,107.123 133.000,120.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 133.000,120.500 C 132.754,123.123 133.444,123.426 135.000,125.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 135.000,125.500 C 136.444,127.426 136.865,127.219 139.000,128.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 139.000,128.500 C 141.865,130.219 141.949,130.113 145.000,131.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 145.000,131.500 C 147.449,132.613 147.407,132.981 150.000,133.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 150.000,133.500 C 152.407,133.981 152.750,134.250 155.000,133.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 184.000,68.500 C 184.000,75.500 184.000,75.500 184.000,82.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 184.000,82.500 C 184.000,85.000 184.000,85.000 184.000,87.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 184.000,87.500 C 184.000,91.000 184.000,91.000 184.000,94.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 184.000,94.500 C 184.000,97.500 184.000,97.500 184.000,100.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 184.000,100.500 C 184.000,103.000 184.000,103.000 184.000,105.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 184.000,105.500 C 184.000,108.000 184.000,108.000 184.000,110.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 184.000,110.500 C 184.000,113.000 184.000,113.000 184.000,115.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 184.000,115.500 C 184.000,118.500 184.000,118.500 184.000,121.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 184.000,121.500 C 184.000,125.000 184.000,125.000 184.000,128.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 208.000,72.500 C 208.000,76.000 208.000,76.000 208.000,79.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 208.000,79.500 C 208.000,82.000 208.000,82.000 208.000,84.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 208.000,84.500 C 208.000,88.500 208.000,88.500 208.000,92.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 208.000,92.500 C 208.000,95.000 208.000,95.000 208.000,97.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 208.000,97.500 C 208.000,101.000 208.000,101.000 208.000,104.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 208.000,104.500 C 208.000,107.000 208.000,107.000 208.000,109.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 208.000,109.500 C 208.000,112.000 208.000,112.000 208.000,114.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 208.000,114.500 C 208.000,117.000 208.248,117.025 208.000,119.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 208.000,119.500 C 207.748,122.025 207.500,122.000 207.000,124.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 227.000,103.500 C 226.500,106.500 226.544,106.508 226.000,109.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 226.000,109.500 C 225.544,112.008 225.500,112.000 225.000,114.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 225.000,114.500 C 224.500,117.000 224.252,116.975 224.000,119.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 224.000,119.500 C 223.752,121.975 223.250,122.250 224.000,124.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 224.000,124.500 C 224.750,126.750 225.000,127.500 227.000,128.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 227.000,128.500 C 229.000,129.500 229.500,128.500 232.000,128.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 232.000,128.500 C 234.500,128.500 234.500,128.500 237.000,128.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 237.000,128.500 C 239.500,128.500 239.593,128.981 242.000,128.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 242.000,128.500 C 244.593,127.981 244.805,127.963 247.000,126.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 247.000,126.500 C 249.305,124.963 249.463,124.805 251.000,122.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 251.000,122.500 C 252.463,120.305 254.664,119.243 253.000,117.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path><path d="M 253.000,117.500 C 244.164,108.243 241.491,106.458 230.000,100.500" fill="none" stroke="black" stroke-linecap="round" stroke-width="2.250"></path></svg>

```

then base64 encode the svg string and get:

```
PHN2ZyBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDU1MCAyMDAiIHdpZHRoPSI1NTAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTSA3OC4wMDAsNDYuNTAwIEMgNzguMDAwLDQ5LjAwMCA3OC4wMDAsNDkuMDAwIDc4LjAwMCw1MS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDUxLjUwMCBDIDc4LjAwMCw1NS4wMDAgNzguMDAwLDU1LjAwMCA3OC4wMDAsNTguNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw1OC41MDAgQyA3OC4wMDAsNjEuMDAwIDc4LjAwMCw2MS4wMDAgNzguMDAwLDYzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsNjMuNTAwIEMgNzguMDAwLDY3LjAwMCA3OC4wMDAsNjcuMDAwIDc4LjAwMCw3MC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDcwLjUwMCBDIDc4LjAwMCw3NC4wMDAgNzguMDAwLDc0LjAwMCA3OC4wMDAsNzcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw3Ny41MDAgQyA3OC4wMDAsODAuNTAwIDc4LjAwMCw4MC41MDAgNzguMDAwLDgzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsODMuNTAwIEMgNzguMDAwLDg3LjAwMCA3OC4wMDAsODcuMDAwIDc4LjAwMCw5MC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDkwLjUwMCBDIDc4LjAwMCw5My4wMDAgNzguMDAwLDkzLjAwMCA3OC4wMDAsOTUuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw5NS41MDAgQyA3OC4wMDAsOTguMDAwIDc4LjAwMCw5OC4wMDAgNzguMDAwLDEwMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDEwMC41MDAgQyA3OC4wMDAsMTAzLjAwMCA3OC4wMDAsMTAzLjAwMCA3OC4wMDAsMTA1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsMTA1LjUwMCBDIDc4LjAwMCwxMTAuMDAwIDc4LjMxOSwxMTAuMDMyIDc4LjAwMCwxMTQuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCwxMTQuNTAwIEMgNzcuODE5LDExNy4wMzIgNzcuNTAwLDExNy4wMDAgNzcuMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzcuMDAwLDExOS41MDAgQyA3Ni41MDAsMTIyLjAwMCA3Ni41MDAsMTIyLjAwMCA3Ni4wMDAsMTI0LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3Ni4wMDAsMTI0LjUwMCBDIDc1LjUwMCwxMjcuMDAwIDc1LjQxOSwxMjYuOTg2IDc1LjAwMCwxMjkuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc1LjAwMCwxMjkuNTAwIEMgNzQuNDE5LDEzMi45ODYgNzQuNTgxLDEzMy4wMTQgNzQuMDAwLDEzNi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCw1MS41MDAgQyAxMTEuMDAwLDU0LjAwMCAxMTEuMDAwLDU0LjAwMCAxMTEuMDAwLDU2LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMTEuMDAwLDU2LjUwMCBDIDExMS4wMDAsNTkuMDAwIDExMS4wMDAsNTkuMDAwIDExMS4wMDAsNjEuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDExMS4wMDAsNjEuNTAwIEMgMTExLjAwMCw2NS4wMDAgMTExLjAwMCw2NS4wMDAgMTExLjAwMCw2OC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCw2OC41MDAgQyAxMTEuMDAwLDk0LjUwMCAxMTEuMDAwLDk0LjUwMCAxMTEuMDAwLDEyMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCwxMjAuNTAwIEMgMTExLjAwMCwxMjMuMDAwIDExMS4wMDAsMTIzLjAwMCAxMTEuMDAwLDEyNS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCwxMjUuNTAwIEMgMTExLjAwMCwxMjguMDAwIDExMS4wMDAsMTI4LjAwMCAxMTEuMDAwLDEzMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDkzLjUwMCBDIDgwLjUwMCw5My41MDAgODAuNTAwLDkzLjUwMCA4My4wMDAsOTMuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDgzLjAwMCw5My41MDAgQyA4NS41MDAsOTMuNTAwIDg1LjUwMCw5My41MDAgODguMDAwLDkzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA4OC4wMDAsOTMuNTAwIEMgOTAuNTAwLDkzLjUwMCA5MC41MDAsOTMuNTAwIDkzLjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gOTMuMDAwLDkzLjUwMCBDIDk1LjUwMCw5My41MDAgOTUuNTAwLDkzLjUwMCA5OC4wMDAsOTMuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDk4LjAwMCw5My41MDAgQyAxMDAuNTAwLDkzLjUwMCAxMDAuNTA3LDkzLjY1NiAxMDMuMDAwLDkzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMjQuMDAwLDEwOS41MDAgQyAxMjcuNTAwLDEwOS41MDAgMTI3LjUwMCwxMDkuNTAwIDEzMS4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzEuMDAwLDEwOS41MDAgQyAxMzQuNTAwLDEwOS41MDAgMTM0LjUwMCwxMDkuNTAwIDEzOC4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzguMDAwLDEwOS41MDAgQyAxNDEuMDAwLDEwOS41MDAgMTQxLjAwMCwxMDkuNTAwIDE0NC4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDQuMDAwLDEwOS41MDAgQyAxNDYuNTAwLDEwOS41MDAgMTQ2LjU5MywxMDkuOTgxIDE0OS4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDkuMDAwLDEwOS41MDAgQyAxNTEuNTkzLDEwOC45ODEgMTUxLjkyNiwxMDkuMDU2IDE1NC4wMDAsMTA3LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTQuMDAwLDEwNy41MDAgQyAxNTUuOTI2LDEwNi4wNTYgMTU2LjMxOCwxMDUuNzczIDE1Ny4wMDAsMTAzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTcuMDAwLDEwMy41MDAgQyAxNTcuODE4LDEwMC43NzMgMTU4LjAyOSwxMDAuMDc0IDE1Ny4wMDAsOTcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE1Ny4wMDAsOTcuNTAwIEMgMTU2LjAyOSw5NS4wNzQgMTU1LjM2MSw5NC45MTYgMTUzLjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTUzLjAwMCw5My41MDAgQyAxNTAuMzYxLDkxLjkxNiAxNTAuMDQ1LDkyLjMzMCAxNDcuMDAwLDkxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDcuMDAwLDkxLjUwMCBDIDE0NC41NDUsOTAuODMwIDE0NC4yNzIsODkuOTk1IDE0Mi4wMDAsOTAuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE0Mi4wMDAsOTAuNTAwIEMgMTM5Ljc3Miw5MC45OTUgMTM4LjY5Myw5MS4xODkgMTM4LjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTM4LjAwMCw5My41MDAgQyAxMzQuMTkzLDEwNi4xODkgMTM0LjI1NCwxMDcuMTIzIDEzMy4wMDAsMTIwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzMuMDAwLDEyMC41MDAgQyAxMzIuNzU0LDEyMy4xMjMgMTMzLjQ0NCwxMjMuNDI2IDEzNS4wMDAsMTI1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzUuMDAwLDEyNS41MDAgQyAxMzYuNDQ0LDEyNy40MjYgMTM2Ljg2NSwxMjcuMjE5IDEzOS4wMDAsMTI4LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzkuMDAwLDEyOC41MDAgQyAxNDEuODY1LDEzMC4yMTkgMTQxLjk0OSwxMzAuMTEzIDE0NS4wMDAsMTMxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDUuMDAwLDEzMS41MDAgQyAxNDcuNDQ5LDEzMi42MTMgMTQ3LjQwNywxMzIuOTgxIDE1MC4wMDAsMTMzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTAuMDAwLDEzMy41MDAgQyAxNTIuNDA3LDEzMy45ODEgMTUyLjc1MCwxMzQuMjUwIDE1NS4wMDAsMTMzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDY4LjUwMCBDIDE4NC4wMDAsNzUuNTAwIDE4NC4wMDAsNzUuNTAwIDE4NC4wMDAsODIuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE4NC4wMDAsODIuNTAwIEMgMTg0LjAwMCw4NS4wMDAgMTg0LjAwMCw4NS4wMDAgMTg0LjAwMCw4Ny41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTg0LjAwMCw4Ny41MDAgQyAxODQuMDAwLDkxLjAwMCAxODQuMDAwLDkxLjAwMCAxODQuMDAwLDk0LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDk0LjUwMCBDIDE4NC4wMDAsOTcuNTAwIDE4NC4wMDAsOTcuNTAwIDE4NC4wMDAsMTAwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEwMC41MDAgQyAxODQuMDAwLDEwMy4wMDAgMTg0LjAwMCwxMDMuMDAwIDE4NC4wMDAsMTA1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEwNS41MDAgQyAxODQuMDAwLDEwOC4wMDAgMTg0LjAwMCwxMDguMDAwIDE4NC4wMDAsMTEwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDExMC41MDAgQyAxODQuMDAwLDExMy4wMDAgMTg0LjAwMCwxMTMuMDAwIDE4NC4wMDAsMTE1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDExNS41MDAgQyAxODQuMDAwLDExOC41MDAgMTg0LjAwMCwxMTguNTAwIDE4NC4wMDAsMTIxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEyMS41MDAgQyAxODQuMDAwLDEyNS4wMDAgMTg0LjAwMCwxMjUuMDAwIDE4NC4wMDAsMTI4LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAyMDguMDAwLDcyLjUwMCBDIDIwOC4wMDAsNzYuMDAwIDIwOC4wMDAsNzYuMDAwIDIwOC4wMDAsNzkuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDIwOC4wMDAsNzkuNTAwIEMgMjA4LjAwMCw4Mi4wMDAgMjA4LjAwMCw4Mi4wMDAgMjA4LjAwMCw4NC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCw4NC41MDAgQyAyMDguMDAwLDg4LjUwMCAyMDguMDAwLDg4LjUwMCAyMDguMDAwLDkyLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAyMDguMDAwLDkyLjUwMCBDIDIwOC4wMDAsOTUuMDAwIDIwOC4wMDAsOTUuMDAwIDIwOC4wMDAsOTcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDIwOC4wMDAsOTcuNTAwIEMgMjA4LjAwMCwxMDEuMDAwIDIwOC4wMDAsMTAxLjAwMCAyMDguMDAwLDEwNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMDQuNTAwIEMgMjA4LjAwMCwxMDcuMDAwIDIwOC4wMDAsMTA3LjAwMCAyMDguMDAwLDEwOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMDkuNTAwIEMgMjA4LjAwMCwxMTIuMDAwIDIwOC4wMDAsMTEyLjAwMCAyMDguMDAwLDExNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMTQuNTAwIEMgMjA4LjAwMCwxMTcuMDAwIDIwOC4yNDgsMTE3LjAyNSAyMDguMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMTkuNTAwIEMgMjA3Ljc0OCwxMjIuMDI1IDIwNy41MDAsMTIyLjAwMCAyMDcuMDAwLDEyNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI3LjAwMCwxMDMuNTAwIEMgMjI2LjUwMCwxMDYuNTAwIDIyNi41NDQsMTA2LjUwOCAyMjYuMDAwLDEwOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI2LjAwMCwxMDkuNTAwIEMgMjI1LjU0NCwxMTIuMDA4IDIyNS41MDAsMTEyLjAwMCAyMjUuMDAwLDExNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI1LjAwMCwxMTQuNTAwIEMgMjI0LjUwMCwxMTcuMDAwIDIyNC4yNTIsMTE2Ljk3NSAyMjQuMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI0LjAwMCwxMTkuNTAwIEMgMjIzLjc1MiwxMjEuOTc1IDIyMy4yNTAsMTIyLjI1MCAyMjQuMDAwLDEyNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI0LjAwMCwxMjQuNTAwIEMgMjI0Ljc1MCwxMjYuNzUwIDIyNS4wMDAsMTI3LjUwMCAyMjcuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI3LjAwMCwxMjguNTAwIEMgMjI5LjAwMCwxMjkuNTAwIDIyOS41MDAsMTI4LjUwMCAyMzIuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjMyLjAwMCwxMjguNTAwIEMgMjM0LjUwMCwxMjguNTAwIDIzNC41MDAsMTI4LjUwMCAyMzcuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjM3LjAwMCwxMjguNTAwIEMgMjM5LjUwMCwxMjguNTAwIDIzOS41OTMsMTI4Ljk4MSAyNDIuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjQyLjAwMCwxMjguNTAwIEMgMjQ0LjU5MywxMjcuOTgxIDI0NC44MDUsMTI3Ljk2MyAyNDcuMDAwLDEyNi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjQ3LjAwMCwxMjYuNTAwIEMgMjQ5LjMwNSwxMjQuOTYzIDI0OS40NjMsMTI0LjgwNSAyNTEuMDAwLDEyMi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjUxLjAwMCwxMjIuNTAwIEMgMjUyLjQ2MywxMjAuMzA1IDI1NC42NjQsMTE5LjI0MyAyNTMuMDAwLDExNy41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjUzLjAwMCwxMTcuNTAwIEMgMjQ0LjE2NCwxMDguMjQzIDI0MS40OTEsMTA2LjQ1OCAyMzAuMDAwLDEwMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjwvc3ZnPg==

```

Note: the full SVG spec is not supported just simple paths.

We can also pass the `name` parameter to provide a text format of the signature.

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
    "customValues": [
      {
        "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
        "name": "Jane Doe",
        "svgVal": "PHN2ZyBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDU1MCAyMDAiIHdpZHRoPSI1NTAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTSA3OC4wMDAsNDYuNTAwIEMgNzguMDAwLDQ5LjAwMCA3OC4wMDAsNDkuMDAwIDc4LjAwMCw1MS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDUxLjUwMCBDIDc4LjAwMCw1NS4wMDAgNzguMDAwLDU1LjAwMCA3OC4wMDAsNTguNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw1OC41MDAgQyA3OC4wMDAsNjEuMDAwIDc4LjAwMCw2MS4wMDAgNzguMDAwLDYzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsNjMuNTAwIEMgNzguMDAwLDY3LjAwMCA3OC4wMDAsNjcuMDAwIDc4LjAwMCw3MC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDcwLjUwMCBDIDc4LjAwMCw3NC4wMDAgNzguMDAwLDc0LjAwMCA3OC4wMDAsNzcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw3Ny41MDAgQyA3OC4wMDAsODAuNTAwIDc4LjAwMCw4MC41MDAgNzguMDAwLDgzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsODMuNTAwIEMgNzguMDAwLDg3LjAwMCA3OC4wMDAsODcuMDAwIDc4LjAwMCw5MC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDkwLjUwMCBDIDc4LjAwMCw5My4wMDAgNzguMDAwLDkzLjAwMCA3OC4wMDAsOTUuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw5NS41MDAgQyA3OC4wMDAsOTguMDAwIDc4LjAwMCw5OC4wMDAgNzguMDAwLDEwMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDEwMC41MDAgQyA3OC4wMDAsMTAzLjAwMCA3OC4wMDAsMTAzLjAwMCA3OC4wMDAsMTA1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsMTA1LjUwMCBDIDc4LjAwMCwxMTAuMDAwIDc4LjMxOSwxMTAuMDMyIDc4LjAwMCwxMTQuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCwxMTQuNTAwIEMgNzcuODE5LDExNy4wMzIgNzcuNTAwLDExNy4wMDAgNzcuMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzcuMDAwLDExOS41MDAgQyA3Ni41MDAsMTIyLjAwMCA3Ni41MDAsMTIyLjAwMCA3Ni4wMDAsMTI0LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3Ni4wMDAsMTI0LjUwMCBDIDc1LjUwMCwxMjcuMDAwIDc1LjQxOSwxMjYuOTg2IDc1LjAwMCwxMjkuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc1LjAwMCwxMjkuNTAwIEMgNzQuNDE5LDEzMi45ODYgNzQuNTgxLDEzMy4wMTQgNzQuMDAwLDEzNi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCw1MS41MDAgQyAxMTEuMDAwLDU0LjAwMCAxMTEuMDAwLDU0LjAwMCAxMTEuMDAwLDU2LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMTEuMDAwLDU2LjUwMCBDIDExMS4wMDAsNTkuMDAwIDExMS4wMDAsNTkuMDAwIDExMS4wMDAsNjEuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDExMS4wMDAsNjEuNTAwIEMgMTExLjAwMCw2NS4wMDAgMTExLjAwMCw2NS4wMDAgMTExLjAwMCw2OC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCw2OC41MDAgQyAxMTEuMDAwLDk0LjUwMCAxMTEuMDAwLDk0LjUwMCAxMTEuMDAwLDEyMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCwxMjAuNTAwIEMgMTExLjAwMCwxMjMuMDAwIDExMS4wMDAsMTIzLjAwMCAxMTEuMDAwLDEyNS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCwxMjUuNTAwIEMgMTExLjAwMCwxMjguMDAwIDExMS4wMDAsMTI4LjAwMCAxMTEuMDAwLDEzMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDkzLjUwMCBDIDgwLjUwMCw5My41MDAgODAuNTAwLDkzLjUwMCA4My4wMDAsOTMuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDgzLjAwMCw5My41MDAgQyA4NS41MDAsOTMuNTAwIDg1LjUwMCw5My41MDAgODguMDAwLDkzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA4OC4wMDAsOTMuNTAwIEMgOTAuNTAwLDkzLjUwMCA5MC41MDAsOTMuNTAwIDkzLjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gOTMuMDAwLDkzLjUwMCBDIDk1LjUwMCw5My41MDAgOTUuNTAwLDkzLjUwMCA5OC4wMDAsOTMuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDk4LjAwMCw5My41MDAgQyAxMDAuNTAwLDkzLjUwMCAxMDAuNTA3LDkzLjY1NiAxMDMuMDAwLDkzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMjQuMDAwLDEwOS41MDAgQyAxMjcuNTAwLDEwOS41MDAgMTI3LjUwMCwxMDkuNTAwIDEzMS4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzEuMDAwLDEwOS41MDAgQyAxMzQuNTAwLDEwOS41MDAgMTM0LjUwMCwxMDkuNTAwIDEzOC4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzguMDAwLDEwOS41MDAgQyAxNDEuMDAwLDEwOS41MDAgMTQxLjAwMCwxMDkuNTAwIDE0NC4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDQuMDAwLDEwOS41MDAgQyAxNDYuNTAwLDEwOS41MDAgMTQ2LjU5MywxMDkuOTgxIDE0OS4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDkuMDAwLDEwOS41MDAgQyAxNTEuNTkzLDEwOC45ODEgMTUxLjkyNiwxMDkuMDU2IDE1NC4wMDAsMTA3LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTQuMDAwLDEwNy41MDAgQyAxNTUuOTI2LDEwNi4wNTYgMTU2LjMxOCwxMDUuNzczIDE1Ny4wMDAsMTAzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTcuMDAwLDEwMy41MDAgQyAxNTcuODE4LDEwMC43NzMgMTU4LjAyOSwxMDAuMDc0IDE1Ny4wMDAsOTcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE1Ny4wMDAsOTcuNTAwIEMgMTU2LjAyOSw5NS4wNzQgMTU1LjM2MSw5NC45MTYgMTUzLjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTUzLjAwMCw5My41MDAgQyAxNTAuMzYxLDkxLjkxNiAxNTAuMDQ1LDkyLjMzMCAxNDcuMDAwLDkxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDcuMDAwLDkxLjUwMCBDIDE0NC41NDUsOTAuODMwIDE0NC4yNzIsODkuOTk1IDE0Mi4wMDAsOTAuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE0Mi4wMDAsOTAuNTAwIEMgMTM5Ljc3Miw5MC45OTUgMTM4LjY5Myw5MS4xODkgMTM4LjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTM4LjAwMCw5My41MDAgQyAxMzQuMTkzLDEwNi4xODkgMTM0LjI1NCwxMDcuMTIzIDEzMy4wMDAsMTIwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzMuMDAwLDEyMC41MDAgQyAxMzIuNzU0LDEyMy4xMjMgMTMzLjQ0NCwxMjMuNDI2IDEzNS4wMDAsMTI1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzUuMDAwLDEyNS41MDAgQyAxMzYuNDQ0LDEyNy40MjYgMTM2Ljg2NSwxMjcuMjE5IDEzOS4wMDAsMTI4LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzkuMDAwLDEyOC41MDAgQyAxNDEuODY1LDEzMC4yMTkgMTQxLjk0OSwxMzAuMTEzIDE0NS4wMDAsMTMxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDUuMDAwLDEzMS41MDAgQyAxNDcuNDQ5LDEzMi42MTMgMTQ3LjQwNywxMzIuOTgxIDE1MC4wMDAsMTMzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTAuMDAwLDEzMy41MDAgQyAxNTIuNDA3LDEzMy45ODEgMTUyLjc1MCwxMzQuMjUwIDE1NS4wMDAsMTMzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDY4LjUwMCBDIDE4NC4wMDAsNzUuNTAwIDE4NC4wMDAsNzUuNTAwIDE4NC4wMDAsODIuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE4NC4wMDAsODIuNTAwIEMgMTg0LjAwMCw4NS4wMDAgMTg0LjAwMCw4NS4wMDAgMTg0LjAwMCw4Ny41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTg0LjAwMCw4Ny41MDAgQyAxODQuMDAwLDkxLjAwMCAxODQuMDAwLDkxLjAwMCAxODQuMDAwLDk0LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDk0LjUwMCBDIDE4NC4wMDAsOTcuNTAwIDE4NC4wMDAsOTcuNTAwIDE4NC4wMDAsMTAwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEwMC41MDAgQyAxODQuMDAwLDEwMy4wMDAgMTg0LjAwMCwxMDMuMDAwIDE4NC4wMDAsMTA1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEwNS41MDAgQyAxODQuMDAwLDEwOC4wMDAgMTg0LjAwMCwxMDguMDAwIDE4NC4wMDAsMTEwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDExMC41MDAgQyAxODQuMDAwLDExMy4wMDAgMTg0LjAwMCwxMTMuMDAwIDE4NC4wMDAsMTE1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDExNS41MDAgQyAxODQuMDAwLDExOC41MDAgMTg0LjAwMCwxMTguNTAwIDE4NC4wMDAsMTIxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEyMS41MDAgQyAxODQuMDAwLDEyNS4wMDAgMTg0LjAwMCwxMjUuMDAwIDE4NC4wMDAsMTI4LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAyMDguMDAwLDcyLjUwMCBDIDIwOC4wMDAsNzYuMDAwIDIwOC4wMDAsNzYuMDAwIDIwOC4wMDAsNzkuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDIwOC4wMDAsNzkuNTAwIEMgMjA4LjAwMCw4Mi4wMDAgMjA4LjAwMCw4Mi4wMDAgMjA4LjAwMCw4NC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCw4NC41MDAgQyAyMDguMDAwLDg4LjUwMCAyMDguMDAwLDg4LjUwMCAyMDguMDAwLDkyLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAyMDguMDAwLDkyLjUwMCBDIDIwOC4wMDAsOTUuMDAwIDIwOC4wMDAsOTUuMDAwIDIwOC4wMDAsOTcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDIwOC4wMDAsOTcuNTAwIEMgMjA4LjAwMCwxMDEuMDAwIDIwOC4wMDAsMTAxLjAwMCAyMDguMDAwLDEwNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMDQuNTAwIEMgMjA4LjAwMCwxMDcuMDAwIDIwOC4wMDAsMTA3LjAwMCAyMDguMDAwLDEwOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMDkuNTAwIEMgMjA4LjAwMCwxMTIuMDAwIDIwOC4wMDAsMTEyLjAwMCAyMDguMDAwLDExNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMTQuNTAwIEMgMjA4LjAwMCwxMTcuMDAwIDIwOC4yNDgsMTE3LjAyNSAyMDguMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMTkuNTAwIEMgMjA3Ljc0OCwxMjIuMDI1IDIwNy41MDAsMTIyLjAwMCAyMDcuMDAwLDEyNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI3LjAwMCwxMDMuNTAwIEMgMjI2LjUwMCwxMDYuNTAwIDIyNi41NDQsMTA2LjUwOCAyMjYuMDAwLDEwOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI2LjAwMCwxMDkuNTAwIEMgMjI1LjU0NCwxMTIuMDA4IDIyNS41MDAsMTEyLjAwMCAyMjUuMDAwLDExNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI1LjAwMCwxMTQuNTAwIEMgMjI0LjUwMCwxMTcuMDAwIDIyNC4yNTIsMTE2Ljk3NSAyMjQuMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI0LjAwMCwxMTkuNTAwIEMgMjIzLjc1MiwxMjEuOTc1IDIyMy4yNTAsMTIyLjI1MCAyMjQuMDAwLDEyNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI0LjAwMCwxMjQuNTAwIEMgMjI0Ljc1MCwxMjYuNzUwIDIyNS4wMDAsMTI3LjUwMCAyMjcuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI3LjAwMCwxMjguNTAwIEMgMjI5LjAwMCwxMjkuNTAwIDIyOS41MDAsMTI4LjUwMCAyMzIuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjMyLjAwMCwxMjguNTAwIEMgMjM0LjUwMCwxMjguNTAwIDIzNC41MDAsMTI4LjUwMCAyMzcuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjM3LjAwMCwxMjguNTAwIEMgMjM5LjUwMCwxMjguNTAwIDIzOS41OTMsMTI4Ljk4MSAyNDIuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjQyLjAwMCwxMjguNTAwIEMgMjQ0LjU5MywxMjcuOTgxIDI0NC44MDUsMTI3Ljk2MyAyNDcuMDAwLDEyNi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjQ3LjAwMCwxMjYuNTAwIEMgMjQ5LjMwNSwxMjQuOTYzIDI0OS40NjMsMTI0LjgwNSAyNTEuMDAwLDEyMi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjUxLjAwMCwxMjIuNTAwIEMgMjUyLjQ2MywxMjAuMzA1IDI1NC42NjQsMTE5LjI0MyAyNTMuMDAwLDExNy41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjUzLjAwMCwxMTcuNTAwIEMgMjQ0LjE2NCwxMDguMjQzIDI0MS40OTEsMTA2LjQ1OCAyMzAuMDAwLDEwMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjwvc3ZnPg=="
      }
    ]
  }'

```

Show More

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "toggleVal": "Yes",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "textVal": "This is my response!",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "notes": null,
          "numberVal": 42.0,
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "choiceVal": "Answer 2",
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "choiceVal": "Answer 3",
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "arrayVal": "['Answer 2', 'Answer 3']",
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "dateVal": "1999-12-31",
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "name": "Jane Doe",
          "notes": null,
          "sectionLabel": "All question types",
          "svgVal": "PHN2ZyBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDU1MCAyMDAiIHdpZHRoPSI1NTAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTSA3OC4wMDAsNDYuNTAwIEMgNzguMDAwLDQ5LjAwMCA3OC4wMDAsNDkuMDAwIDc4LjAwMCw1MS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDUxLjUwMCBDIDc4LjAwMCw1NS4wMDAgNzguMDAwLDU1LjAwMCA3OC4wMDAsNTguNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw1OC41MDAgQyA3OC4wMDAsNjEuMDAwIDc4LjAwMCw2MS4wMDAgNzguMDAwLDYzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsNjMuNTAwIEMgNzguMDAwLDY3LjAwMCA3OC4wMDAsNjcuMDAwIDc4LjAwMCw3MC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDcwLjUwMCBDIDc4LjAwMCw3NC4wMDAgNzguMDAwLDc0LjAwMCA3OC4wMDAsNzcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw3Ny41MDAgQyA3OC4wMDAsODAuNTAwIDc4LjAwMCw4MC41MDAgNzguMDAwLDgzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsODMuNTAwIEMgNzguMDAwLDg3LjAwMCA3OC4wMDAsODcuMDAwIDc4LjAwMCw5MC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDkwLjUwMCBDIDc4LjAwMCw5My4wMDAgNzguMDAwLDkzLjAwMCA3OC4wMDAsOTUuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw5NS41MDAgQyA3OC4wMDAsOTguMDAwIDc4LjAwMCw5OC4wMDAgNzguMDAwLDEwMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDEwMC41MDAgQyA3OC4wMDAsMTAzLjAwMCA3OC4wMDAsMTAzLjAwMCA3OC4wMDAsMTA1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsMTA1LjUwMCBDIDc4LjAwMCwxMTAuMDAwIDc4LjMxOSwxMTAuMDMyIDc4LjAwMCwxMTQuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCwxMTQuNTAwIEMgNzcuODE5LDExNy4wMzIgNzcuNTAwLDExNy4wMDAgNzcuMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzcuMDAwLDExOS41MDAgQyA3Ni41MDAsMTIyLjAwMCA3Ni41MDAsMTIyLjAwMCA3Ni4wMDAsMTI0LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3Ni4wMDAsMTI0LjUwMCBDIDc1LjUwMCwxMjcuMDAwIDc1LjQxOSwxMjYuOTg2IDc1LjAwMCwxMjkuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc1LjAwMCwxMjkuNTAwIEMgNzQuNDE5LDEzMi45ODYgNzQuNTgxLDEzMy4wMTQgNzQuMDAwLDEzNi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCw1MS41MDAgQyAxMTEuMDAwLDU0LjAwMCAxMTEuMDAwLDU0LjAwMCAxMTEuMDAwLDU2LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMTEuMDAwLDU2LjUwMCBDIDExMS4wMDAsNTkuMDAwIDExMS4wMDAsNTkuMDAwIDExMS4wMDAsNjEuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDExMS4wMDAsNjEuNTAwIEMgMTExLjAwMCw2NS4wMDAgMTExLjAwMCw2NS4wMDAgMTExLjAwMCw2OC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCw2OC41MDAgQyAxMTEuMDAwLDk0LjUwMCAxMTEuMDAwLDk0LjUwMCAxMTEuMDAwLDEyMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCwxMjAuNTAwIEMgMTExLjAwMCwxMjMuMDAwIDExMS4wMDAsMTIzLjAwMCAxMTEuMDAwLDEyNS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCwxMjUuNTAwIEMgMTExLjAwMCwxMjguMDAwIDExMS4wMDAsMTI4LjAwMCAxMTEuMDAwLDEzMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDkzLjUwMCBDIDgwLjUwMCw5My41MDAgODAuNTAwLDkzLjUwMCA4My4wMDAsOTMuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDgzLjAwMCw5My41MDAgQyA4NS41MDAsOTMuNTAwIDg1LjUwMCw5My41MDAgODguMDAwLDkzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA4OC4wMDAsOTMuNTAwIEMgOTAuNTAwLDkzLjUwMCA5MC41MDAsOTMuNTAwIDkzLjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gOTMuMDAwLDkzLjUwMCBDIDk1LjUwMCw5My41MDAgOTUuNTAwLDkzLjUwMCA5OC4wMDAsOTMuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDk4LjAwMCw5My41MDAgQyAxMDAuNTAwLDkzLjUwMCAxMDAuNTA3LDkzLjY1NiAxMDMuMDAwLDkzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMjQuMDAwLDEwOS41MDAgQyAxMjcuNTAwLDEwOS41MDAgMTI3LjUwMCwxMDkuNTAwIDEzMS4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzEuMDAwLDEwOS41MDAgQyAxMzQuNTAwLDEwOS41MDAgMTM0LjUwMCwxMDkuNTAwIDEzOC4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzguMDAwLDEwOS41MDAgQyAxNDEuMDAwLDEwOS41MDAgMTQxLjAwMCwxMDkuNTAwIDE0NC4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDQuMDAwLDEwOS41MDAgQyAxNDYuNTAwLDEwOS41MDAgMTQ2LjU5MywxMDkuOTgxIDE0OS4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDkuMDAwLDEwOS41MDAgQyAxNTEuNTkzLDEwOC45ODEgMTUxLjkyNiwxMDkuMDU2IDE1NC4wMDAsMTA3LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTQuMDAwLDEwNy41MDAgQyAxNTUuOTI2LDEwNi4wNTYgMTU2LjMxOCwxMDUuNzczIDE1Ny4wMDAsMTAzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTcuMDAwLDEwMy41MDAgQyAxNTcuODE4LDEwMC43NzMgMTU4LjAyOSwxMDAuMDc0IDE1Ny4wMDAsOTcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE1Ny4wMDAsOTcuNTAwIEMgMTU2LjAyOSw5NS4wNzQgMTU1LjM2MSw5NC45MTYgMTUzLjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTUzLjAwMCw5My41MDAgQyAxNTAuMzYxLDkxLjkxNiAxNTAuMDQ1LDkyLjMzMCAxNDcuMDAwLDkxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDcuMDAwLDkxLjUwMCBDIDE0NC41NDUsOTAuODMwIDE0NC4yNzIsODkuOTk1IDE0Mi4wMDAsOTAuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE0Mi4wMDAsOTAuNTAwIEMgMTM5Ljc3Miw5MC45OTUgMTM4LjY5Myw5MS4xODkgMTM4LjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTM4LjAwMCw5My41MDAgQyAxMzQuMTkzLDEwNi4xODkgMTM0LjI1NCwxMDcuMTIzIDEzMy4wMDAsMTIwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzMuMDAwLDEyMC41MDAgQyAxMzIuNzU0LDEyMy4xMjMgMTMzLjQ0NCwxMjMuNDI2IDEzNS4wMDAsMTI1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzUuMDAwLDEyNS41MDAgQyAxMzYuNDQ0LDEyNy40MjYgMTM2Ljg2NSwxMjcuMjE5IDEzOS4wMDAsMTI4LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzkuMDAwLDEyOC41MDAgQyAxNDEuODY1LDEzMC4yMTkgMTQxLjk0OSwxMzAuMTEzIDE0NS4wMDAsMTMxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDUuMDAwLDEzMS41MDAgQyAxNDcuNDQ5LDEzMi42MTMgMTQ3LjQwNywxMzIuOTgxIDE1MC4wMDAsMTMzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTAuMDAwLDEzMy41MDAgQyAxNTIuNDA3LDEzMy45ODEgMTUyLjc1MCwxMzQuMjUwIDE1NS4wMDAsMTMzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDY4LjUwMCBDIDE4NC4wMDAsNzUuNTAwIDE4NC4wMDAsNzUuNTAwIDE4NC4wMDAsODIuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE4NC4wMDAsODIuNTAwIEMgMTg0LjAwMCw4NS4wMDAgMTg0LjAwMCw4NS4wMDAgMTg0LjAwMCw4Ny41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTg0LjAwMCw4Ny41MDAgQyAxODQuMDAwLDkxLjAwMCAxODQuMDAwLDkxLjAwMCAxODQuMDAwLDk0LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDk0LjUwMCBDIDE4NC4wMDAsOTcuNTAwIDE4NC4wMDAsOTcuNTAwIDE4NC4wMDAsMTAwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEwMC41MDAgQyAxODQuMDAwLDEwMy4wMDAgMTg0LjAwMCwxMDMuMDAwIDE4NC4wMDAsMTA1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEwNS41MDAgQyAxODQuMDAwLDEwOC4wMDAgMTg0LjAwMCwxMDguMDAwIDE4NC4wMDAsMTEwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDExMC41MDAgQyAxODQuMDAwLDExMy4wMDAgMTg0LjAwMCwxMTMuMDAwIDE4NC4wMDAsMTE1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDExNS41MDAgQyAxODQuMDAwLDExOC41MDAgMTg0LjAwMCwxMTguNTAwIDE4NC4wMDAsMTIxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEyMS41MDAgQyAxODQuMDAwLDEyNS4wMDAgMTg0LjAwMCwxMjUuMDAwIDE4NC4wMDAsMTI4LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAyMDguMDAwLDcyLjUwMCBDIDIwOC4wMDAsNzYuMDAwIDIwOC4wMDAsNzYuMDAwIDIwOC4wMDAsNzkuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDIwOC4wMDAsNzkuNTAwIEMgMjA4LjAwMCw4Mi4wMDAgMjA4LjAwMCw4Mi4wMDAgMjA4LjAwMCw4NC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCw4NC41MDAgQyAyMDguMDAwLDg4LjUwMCAyMDguMDAwLDg4LjUwMCAyMDguMDAwLDkyLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAyMDguMDAwLDkyLjUwMCBDIDIwOC4wMDAsOTUuMDAwIDIwOC4wMDAsOTUuMDAwIDIwOC4wMDAsOTcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDIwOC4wMDAsOTcuNTAwIEMgMjA4LjAwMCwxMDEuMDAwIDIwOC4wMDAsMTAxLjAwMCAyMDguMDAwLDEwNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMDQuNTAwIEMgMjA4LjAwMCwxMDcuMDAwIDIwOC4wMDAsMTA3LjAwMCAyMDguMDAwLDEwOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMDkuNTAwIEMgMjA4LjAwMCwxMTIuMDAwIDIwOC4wMDAsMTEyLjAwMCAyMDguMDAwLDExNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMTQuNTAwIEMgMjA4LjAwMCwxMTcuMDAwIDIwOC4yNDgsMTE3LjAyNSAyMDguMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMTkuNTAwIEMgMjA3Ljc0OCwxMjIuMDI1IDIwNy41MDAsMTIyLjAwMCAyMDcuMDAwLDEyNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI3LjAwMCwxMDMuNTAwIEMgMjI2LjUwMCwxMDYuNTAwIDIyNi41NDQsMTA2LjUwOCAyMjYuMDAwLDEwOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI2LjAwMCwxMDkuNTAwIEMgMjI1LjU0NCwxMTIuMDA4IDIyNS41MDAsMTEyLjAwMCAyMjUuMDAwLDExNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI1LjAwMCwxMTQuNTAwIEMgMjI0LjUwMCwxMTcuMDAwIDIyNC4yNTIsMTE2Ljk3NSAyMjQuMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI0LjAwMCwxMTkuNTAwIEMgMjIzLjc1MiwxMjEuOTc1IDIyMy4yNTAsMTIyLjI1MCAyMjQuMDAwLDEyNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI0LjAwMCwxMjQuNTAwIEMgMjI0Ljc1MCwxMjYuNzUwIDIyNS4wMDAsMTI3LjUwMCAyMjcuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI3LjAwMCwxMjguNTAwIEMgMjI5LjAwMCwxMjkuNTAwIDIyOS41MDAsMTI4LjUwMCAyMzIuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjMyLjAwMCwxMjguNTAwIEMgMjM0LjUwMCwxMjguNTAwIDIzNC41MDAsMTI4LjUwMCAyMzcuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjM3LjAwMCwxMjguNTAwIEMgMjM5LjUwMCwxMjguNTAwIDIzOS41OTMsMTI4Ljk4MSAyNDIuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjQyLjAwMCwxMjguNTAwIEMgMjQ0LjU5MywxMjcuOTgxIDI0NC44MDUsMTI3Ljk2MyAyNDcuMDAwLDEyNi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjQ3LjAwMCwxMjYuNTAwIEMgMjQ5LjMwNSwxMjQuOTYzIDI0OS40NjMsMTI0LjgwNSAyNTEuMDAwLDEyMi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjUxLjAwMCwxMjIuNTAwIEMgMjUyLjQ2MywxMjAuMzA1IDI1NC42NjQsMTE5LjI0MyAyNTMuMDAwLDExNy41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjUzLjAwMCwxMTcuNTAwIEMgMjQ0LjE2NCwxMDguMjQzIDI0MS40OTEsMTA2LjQ1OCAyMzAuMDAwLDEwMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjwvc3ZnPg==",
          "valueName": "svgVal"
      }
  ],
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [],
      "materialsEntries": [],
      "worklogEntries": []
  },
  "updatedAt": "2023-03-10T22:47:01.419140+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

### Option 8: Update the work log table

Create a new UUID to identify each new row, for this example we will use `` e76fe3f4-f587-4309-92c4-6a6f14b9e1bd` ``

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
  "tabularValues": [
      {
          "table": "worklogEntries",
          "id": "e76fe3f4-f587-4309-92c4-6a6f14b9e1bd",
          "columns": [
              {
                  "columnName": "trade",
                  "textVal": "Electrical"
              },
              {
                  "columnName": "timespan",
                  "timespanVal": 7200000
              },
              {
                  "columnName": "headcount",
                  "numberVal": 1
              },
              {
                  "columnName": "description",
                  "textVal": "Room 302 lights"
              }
          ]
      }
  ]
}'

```

Show More

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "toggleVal": "Yes",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "textVal": "This is my response!",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "notes": null,
          "numberVal": 42.0,
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "choiceVal": "Answer 2",
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "choiceVal": "Answer 3",
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "arrayVal": "['Answer 2', 'Answer 3']",
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "dateVal": "1999-12-31",
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "name": "Jone Doe",
          "notes": null,
          "sectionLabel": "All question types",
          "svgVal": "PHN2ZyBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDU1MCAyMDAiIHdpZHRoPSI1NTAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTSA3OC4wMDAsNDYuNTAwIEMgNzguMDAwLDQ5LjAwMCA3OC4wMDAsNDkuMDAwIDc4LjAwMCw1MS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDUxLjUwMCBDIDc4LjAwMCw1NS4wMDAgNzguMDAwLDU1LjAwMCA3OC4wMDAsNTguNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw1OC41MDAgQyA3OC4wMDAsNjEuMDAwIDc4LjAwMCw2MS4wMDAgNzguMDAwLDYzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsNjMuNTAwIEMgNzguMDAwLDY3LjAwMCA3OC4wMDAsNjcuMDAwIDc4LjAwMCw3MC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDcwLjUwMCBDIDc4LjAwMCw3NC4wMDAgNzguMDAwLDc0LjAwMCA3OC4wMDAsNzcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw3Ny41MDAgQyA3OC4wMDAsODAuNTAwIDc4LjAwMCw4MC41MDAgNzguMDAwLDgzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsODMuNTAwIEMgNzguMDAwLDg3LjAwMCA3OC4wMDAsODcuMDAwIDc4LjAwMCw5MC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDkwLjUwMCBDIDc4LjAwMCw5My4wMDAgNzguMDAwLDkzLjAwMCA3OC4wMDAsOTUuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw5NS41MDAgQyA3OC4wMDAsOTguMDAwIDc4LjAwMCw5OC4wMDAgNzguMDAwLDEwMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDEwMC41MDAgQyA3OC4wMDAsMTAzLjAwMCA3OC4wMDAsMTAzLjAwMCA3OC4wMDAsMTA1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsMTA1LjUwMCBDIDc4LjAwMCwxMTAuMDAwIDc4LjMxOSwxMTAuMDMyIDc4LjAwMCwxMTQuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCwxMTQuNTAwIEMgNzcuODE5LDExNy4wMzIgNzcuNTAwLDExNy4wMDAgNzcuMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzcuMDAwLDExOS41MDAgQyA3Ni41MDAsMTIyLjAwMCA3Ni41MDAsMTIyLjAwMCA3Ni4wMDAsMTI0LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3Ni4wMDAsMTI0LjUwMCBDIDc1LjUwMCwxMjcuMDAwIDc1LjQxOSwxMjYuOTg2IDc1LjAwMCwxMjkuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc1LjAwMCwxMjkuNTAwIEMgNzQuNDE5LDEzMi45ODYgNzQuNTgxLDEzMy4wMTQgNzQuMDAwLDEzNi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCw1MS41MDAgQyAxMTEuMDAwLDU0LjAwMCAxMTEuMDAwLDU0LjAwMCAxMTEuMDAwLDU2LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMTEuMDAwLDU2LjUwMCBDIDExMS4wMDAsNTkuMDAwIDExMS4wMDAsNTkuMDAwIDExMS4wMDAsNjEuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDExMS4wMDAsNjEuNTAwIEMgMTExLjAwMCw2NS4wMDAgMTExLjAwMCw2NS4wMDAgMTExLjAwMCw2OC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCw2OC41MDAgQyAxMTEuMDAwLDk0LjUwMCAxMTEuMDAwLDk0LjUwMCAxMTEuMDAwLDEyMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCwxMjAuNTAwIEMgMTExLjAwMCwxMjMuMDAwIDExMS4wMDAsMTIzLjAwMCAxMTEuMDAwLDEyNS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCwxMjUuNTAwIEMgMTExLjAwMCwxMjguMDAwIDExMS4wMDAsMTI4LjAwMCAxMTEuMDAwLDEzMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDkzLjUwMCBDIDgwLjUwMCw5My41MDAgODAuNTAwLDkzLjUwMCA4My4wMDAsOTMuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDgzLjAwMCw5My41MDAgQyA4NS41MDAsOTMuNTAwIDg1LjUwMCw5My41MDAgODguMDAwLDkzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA4OC4wMDAsOTMuNTAwIEMgOTAuNTAwLDkzLjUwMCA5MC41MDAsOTMuNTAwIDkzLjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gOTMuMDAwLDkzLjUwMCBDIDk1LjUwMCw5My41MDAgOTUuNTAwLDkzLjUwMCA5OC4wMDAsOTMuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDk4LjAwMCw5My41MDAgQyAxMDAuNTAwLDkzLjUwMCAxMDAuNTA3LDkzLjY1NiAxMDMuMDAwLDkzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMjQuMDAwLDEwOS41MDAgQyAxMjcuNTAwLDEwOS41MDAgMTI3LjUwMCwxMDkuNTAwIDEzMS4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzEuMDAwLDEwOS41MDAgQyAxMzQuNTAwLDEwOS41MDAgMTM0LjUwMCwxMDkuNTAwIDEzOC4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzguMDAwLDEwOS41MDAgQyAxNDEuMDAwLDEwOS41MDAgMTQxLjAwMCwxMDkuNTAwIDE0NC4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDQuMDAwLDEwOS41MDAgQyAxNDYuNTAwLDEwOS41MDAgMTQ2LjU5MywxMDkuOTgxIDE0OS4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDkuMDAwLDEwOS41MDAgQyAxNTEuNTkzLDEwOC45ODEgMTUxLjkyNiwxMDkuMDU2IDE1NC4wMDAsMTA3LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTQuMDAwLDEwNy41MDAgQyAxNTUuOTI2LDEwNi4wNTYgMTU2LjMxOCwxMDUuNzczIDE1Ny4wMDAsMTAzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTcuMDAwLDEwMy41MDAgQyAxNTcuODE4LDEwMC43NzMgMTU4LjAyOSwxMDAuMDc0IDE1Ny4wMDAsOTcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE1Ny4wMDAsOTcuNTAwIEMgMTU2LjAyOSw5NS4wNzQgMTU1LjM2MSw5NC45MTYgMTUzLjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTUzLjAwMCw5My41MDAgQyAxNTAuMzYxLDkxLjkxNiAxNTAuMDQ1LDkyLjMzMCAxNDcuMDAwLDkxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDcuMDAwLDkxLjUwMCBDIDE0NC41NDUsOTAuODMwIDE0NC4yNzIsODkuOTk1IDE0Mi4wMDAsOTAuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE0Mi4wMDAsOTAuNTAwIEMgMTM5Ljc3Miw5MC45OTUgMTM4LjY5Myw5MS4xODkgMTM4LjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTM4LjAwMCw5My41MDAgQyAxMzQuMTkzLDEwNi4xODkgMTM0LjI1NCwxMDcuMTIzIDEzMy4wMDAsMTIwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzMuMDAwLDEyMC41MDAgQyAxMzIuNzU0LDEyMy4xMjMgMTMzLjQ0NCwxMjMuNDI2IDEzNS4wMDAsMTI1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzUuMDAwLDEyNS41MDAgQyAxMzYuNDQ0LDEyNy40MjYgMTM2Ljg2NSwxMjcuMjE5IDEzOS4wMDAsMTI4LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzkuMDAwLDEyOC41MDAgQyAxNDEuODY1LDEzMC4yMTkgMTQxLjk0OSwxMzAuMTEzIDE0NS4wMDAsMTMxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDUuMDAwLDEzMS41MDAgQyAxNDcuNDQ5LDEzMi42MTMgMTQ3LjQwNywxMzIuOTgxIDE1MC4wMDAsMTMzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTAuMDAwLDEzMy41MDAgQyAxNTIuNDA3LDEzMy45ODEgMTUyLjc1MCwxMzQuMjUwIDE1NS4wMDAsMTMzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDY4LjUwMCBDIDE4NC4wMDAsNzUuNTAwIDE4NC4wMDAsNzUuNTAwIDE4NC4wMDAsODIuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE4NC4wMDAsODIuNTAwIEMgMTg0LjAwMCw4NS4wMDAgMTg0LjAwMCw4NS4wMDAgMTg0LjAwMCw4Ny41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTg0LjAwMCw4Ny41MDAgQyAxODQuMDAwLDkxLjAwMCAxODQuMDAwLDkxLjAwMCAxODQuMDAwLDk0LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDk0LjUwMCBDIDE4NC4wMDAsOTcuNTAwIDE4NC4wMDAsOTcuNTAwIDE4NC4wMDAsMTAwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEwMC41MDAgQyAxODQuMDAwLDEwMy4wMDAgMTg0LjAwMCwxMDMuMDAwIDE4NC4wMDAsMTA1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEwNS41MDAgQyAxODQuMDAwLDEwOC4wMDAgMTg0LjAwMCwxMDguMDAwIDE4NC4wMDAsMTEwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDExMC41MDAgQyAxODQuMDAwLDExMy4wMDAgMTg0LjAwMCwxMTMuMDAwIDE4NC4wMDAsMTE1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDExNS41MDAgQyAxODQuMDAwLDExOC41MDAgMTg0LjAwMCwxMTguNTAwIDE4NC4wMDAsMTIxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEyMS41MDAgQyAxODQuMDAwLDEyNS4wMDAgMTg0LjAwMCwxMjUuMDAwIDE4NC4wMDAsMTI4LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAyMDguMDAwLDcyLjUwMCBDIDIwOC4wMDAsNzYuMDAwIDIwOC4wMDAsNzYuMDAwIDIwOC4wMDAsNzkuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDIwOC4wMDAsNzkuNTAwIEMgMjA4LjAwMCw4Mi4wMDAgMjA4LjAwMCw4Mi4wMDAgMjA4LjAwMCw4NC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCw4NC41MDAgQyAyMDguMDAwLDg4LjUwMCAyMDguMDAwLDg4LjUwMCAyMDguMDAwLDkyLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAyMDguMDAwLDkyLjUwMCBDIDIwOC4wMDAsOTUuMDAwIDIwOC4wMDAsOTUuMDAwIDIwOC4wMDAsOTcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDIwOC4wMDAsOTcuNTAwIEMgMjA4LjAwMCwxMDEuMDAwIDIwOC4wMDAsMTAxLjAwMCAyMDguMDAwLDEwNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMDQuNTAwIEMgMjA4LjAwMCwxMDcuMDAwIDIwOC4wMDAsMTA3LjAwMCAyMDguMDAwLDEwOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMDkuNTAwIEMgMjA4LjAwMCwxMTIuMDAwIDIwOC4wMDAsMTEyLjAwMCAyMDguMDAwLDExNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMTQuNTAwIEMgMjA4LjAwMCwxMTcuMDAwIDIwOC4yNDgsMTE3LjAyNSAyMDguMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMTkuNTAwIEMgMjA3Ljc0OCwxMjIuMDI1IDIwNy41MDAsMTIyLjAwMCAyMDcuMDAwLDEyNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI3LjAwMCwxMDMuNTAwIEMgMjI2LjUwMCwxMDYuNTAwIDIyNi41NDQsMTA2LjUwOCAyMjYuMDAwLDEwOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI2LjAwMCwxMDkuNTAwIEMgMjI1LjU0NCwxMTIuMDA4IDIyNS41MDAsMTEyLjAwMCAyMjUuMDAwLDExNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI1LjAwMCwxMTQuNTAwIEMgMjI0LjUwMCwxMTcuMDAwIDIyNC4yNTIsMTE2Ljk3NSAyMjQuMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI0LjAwMCwxMTkuNTAwIEMgMjIzLjc1MiwxMjEuOTc1IDIyMy4yNTAsMTIyLjI1MCAyMjQuMDAwLDEyNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI0LjAwMCwxMjQuNTAwIEMgMjI0Ljc1MCwxMjYuNzUwIDIyNS4wMDAsMTI3LjUwMCAyMjcuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI3LjAwMCwxMjguNTAwIEMgMjI5LjAwMCwxMjkuNTAwIDIyOS41MDAsMTI4LjUwMCAyMzIuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjMyLjAwMCwxMjguNTAwIEMgMjM0LjUwMCwxMjguNTAwIDIzNC41MDAsMTI4LjUwMCAyMzcuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjM3LjAwMCwxMjguNTAwIEMgMjM5LjUwMCwxMjguNTAwIDIzOS41OTMsMTI4Ljk4MSAyNDIuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjQyLjAwMCwxMjguNTAwIEMgMjQ0LjU5MywxMjcuOTgxIDI0NC44MDUsMTI3Ljk2MyAyNDcuMDAwLDEyNi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjQ3LjAwMCwxMjYuNTAwIEMgMjQ5LjMwNSwxMjQuOTYzIDI0OS40NjMsMTI0LjgwNSAyNTEuMDAwLDEyMi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjUxLjAwMCwxMjIuNTAwIEMgMjUyLjQ2MywxMjAuMzA1IDI1NC42NjQsMTE5LjI0MyAyNTMuMDAwLDExNy41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjUzLjAwMCwxMTcuNTAwIEMgMjQ0LjE2NCwxMDguMjQzIDI0MS40OTEsMTA2LjQ1OCAyMzAuMDAwLDEwMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjwvc3ZnPg==",
          "valueName": "svgVal"
      }
  ],
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "worklogEntries": [
          {
              "deleted": false,
              "description": "Room 302 lights",
              "headcount": 1,
              "id": "e76fe3f4-f587-4309-92c4-6a6f14b9e1bd",
              "timespan": 7200000,
              "trade": "Electrical"
          }
      ]
  },
  "updatedAt": "2023-03-10T23:08:09.543333+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

### Option 9: Update the equipment log table

Create a new UUID to identify each new row, for this example we will use `` d237d262-e5a6-4251-bc06-37f516dbed5c` ``

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
  "tabularValues": [
      {
          "table": "equipmentEntries",
          "id": "d237d262-e5a6-4251-bc06-37f516dbed5c",
          "columns": [
              {
                  "columnName": "item",
                  "textVal": "Forklift"
              },
              {
                  "columnName": "timespan",
                  "timespanVal": 7200000
              },
              {
                  "columnName": "quantity",
                  "numberVal": 1
              },
              {
                  "columnName": "description",
                  "textVal": "Toyota 8FGCU25"
              }
          ]
      }
  ]
}'

```

Show More

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "toggleVal": "Yes",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "textVal": "This is my response!",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "notes": null,
          "numberVal": 42.0,
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "choiceVal": "Answer 2",
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "choiceVal": "Answer 3",
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "arrayVal": "['Answer 2', 'Answer 3']",
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "dateVal": "1999-12-31",
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "name": "Jane Doe",
          "notes": null,
          "sectionLabel": "All question types",
          "svgVal": "PHN2ZyBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDU1MCAyMDAiIHdpZHRoPSI1NTAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTSA3OC4wMDAsNDYuNTAwIEMgNzguMDAwLDQ5LjAwMCA3OC4wMDAsNDkuMDAwIDc4LjAwMCw1MS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDUxLjUwMCBDIDc4LjAwMCw1NS4wMDAgNzguMDAwLDU1LjAwMCA3OC4wMDAsNTguNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw1OC41MDAgQyA3OC4wMDAsNjEuMDAwIDc4LjAwMCw2MS4wMDAgNzguMDAwLDYzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsNjMuNTAwIEMgNzguMDAwLDY3LjAwMCA3OC4wMDAsNjcuMDAwIDc4LjAwMCw3MC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDcwLjUwMCBDIDc4LjAwMCw3NC4wMDAgNzguMDAwLDc0LjAwMCA3OC4wMDAsNzcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw3Ny41MDAgQyA3OC4wMDAsODAuNTAwIDc4LjAwMCw4MC41MDAgNzguMDAwLDgzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsODMuNTAwIEMgNzguMDAwLDg3LjAwMCA3OC4wMDAsODcuMDAwIDc4LjAwMCw5MC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDkwLjUwMCBDIDc4LjAwMCw5My4wMDAgNzguMDAwLDkzLjAwMCA3OC4wMDAsOTUuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw5NS41MDAgQyA3OC4wMDAsOTguMDAwIDc4LjAwMCw5OC4wMDAgNzguMDAwLDEwMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDEwMC41MDAgQyA3OC4wMDAsMTAzLjAwMCA3OC4wMDAsMTAzLjAwMCA3OC4wMDAsMTA1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsMTA1LjUwMCBDIDc4LjAwMCwxMTAuMDAwIDc4LjMxOSwxMTAuMDMyIDc4LjAwMCwxMTQuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCwxMTQuNTAwIEMgNzcuODE5LDExNy4wMzIgNzcuNTAwLDExNy4wMDAgNzcuMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzcuMDAwLDExOS41MDAgQyA3Ni41MDAsMTIyLjAwMCA3Ni41MDAsMTIyLjAwMCA3Ni4wMDAsMTI0LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3Ni4wMDAsMTI0LjUwMCBDIDc1LjUwMCwxMjcuMDAwIDc1LjQxOSwxMjYuOTg2IDc1LjAwMCwxMjkuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc1LjAwMCwxMjkuNTAwIEMgNzQuNDE5LDEzMi45ODYgNzQuNTgxLDEzMy4wMTQgNzQuMDAwLDEzNi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCw1MS41MDAgQyAxMTEuMDAwLDU0LjAwMCAxMTEuMDAwLDU0LjAwMCAxMTEuMDAwLDU2LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMTEuMDAwLDU2LjUwMCBDIDExMS4wMDAsNTkuMDAwIDExMS4wMDAsNTkuMDAwIDExMS4wMDAsNjEuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDExMS4wMDAsNjEuNTAwIEMgMTExLjAwMCw2NS4wMDAgMTExLjAwMCw2NS4wMDAgMTExLjAwMCw2OC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCw2OC41MDAgQyAxMTEuMDAwLDk0LjUwMCAxMTEuMDAwLDk0LjUwMCAxMTEuMDAwLDEyMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCwxMjAuNTAwIEMgMTExLjAwMCwxMjMuMDAwIDExMS4wMDAsMTIzLjAwMCAxMTEuMDAwLDEyNS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCwxMjUuNTAwIEMgMTExLjAwMCwxMjguMDAwIDExMS4wMDAsMTI4LjAwMCAxMTEuMDAwLDEzMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDkzLjUwMCBDIDgwLjUwMCw5My41MDAgODAuNTAwLDkzLjUwMCA4My4wMDAsOTMuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDgzLjAwMCw5My41MDAgQyA4NS41MDAsOTMuNTAwIDg1LjUwMCw5My41MDAgODguMDAwLDkzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA4OC4wMDAsOTMuNTAwIEMgOTAuNTAwLDkzLjUwMCA5MC41MDAsOTMuNTAwIDkzLjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gOTMuMDAwLDkzLjUwMCBDIDk1LjUwMCw5My41MDAgOTUuNTAwLDkzLjUwMCA5OC4wMDAsOTMuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDk4LjAwMCw5My41MDAgQyAxMDAuNTAwLDkzLjUwMCAxMDAuNTA3LDkzLjY1NiAxMDMuMDAwLDkzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMjQuMDAwLDEwOS41MDAgQyAxMjcuNTAwLDEwOS41MDAgMTI3LjUwMCwxMDkuNTAwIDEzMS4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzEuMDAwLDEwOS41MDAgQyAxMzQuNTAwLDEwOS41MDAgMTM0LjUwMCwxMDkuNTAwIDEzOC4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzguMDAwLDEwOS41MDAgQyAxNDEuMDAwLDEwOS41MDAgMTQxLjAwMCwxMDkuNTAwIDE0NC4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDQuMDAwLDEwOS41MDAgQyAxNDYuNTAwLDEwOS41MDAgMTQ2LjU5MywxMDkuOTgxIDE0OS4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDkuMDAwLDEwOS41MDAgQyAxNTEuNTkzLDEwOC45ODEgMTUxLjkyNiwxMDkuMDU2IDE1NC4wMDAsMTA3LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTQuMDAwLDEwNy41MDAgQyAxNTUuOTI2LDEwNi4wNTYgMTU2LjMxOCwxMDUuNzczIDE1Ny4wMDAsMTAzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTcuMDAwLDEwMy41MDAgQyAxNTcuODE4LDEwMC43NzMgMTU4LjAyOSwxMDAuMDc0IDE1Ny4wMDAsOTcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE1Ny4wMDAsOTcuNTAwIEMgMTU2LjAyOSw5NS4wNzQgMTU1LjM2MSw5NC45MTYgMTUzLjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTUzLjAwMCw5My41MDAgQyAxNTAuMzYxLDkxLjkxNiAxNTAuMDQ1LDkyLjMzMCAxNDcuMDAwLDkxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDcuMDAwLDkxLjUwMCBDIDE0NC41NDUsOTAuODMwIDE0NC4yNzIsODkuOTk1IDE0Mi4wMDAsOTAuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE0Mi4wMDAsOTAuNTAwIEMgMTM5Ljc3Miw5MC45OTUgMTM4LjY5Myw5MS4xODkgMTM4LjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTM4LjAwMCw5My41MDAgQyAxMzQuMTkzLDEwNi4xODkgMTM0LjI1NCwxMDcuMTIzIDEzMy4wMDAsMTIwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzMuMDAwLDEyMC41MDAgQyAxMzIuNzU0LDEyMy4xMjMgMTMzLjQ0NCwxMjMuNDI2IDEzNS4wMDAsMTI1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzUuMDAwLDEyNS41MDAgQyAxMzYuNDQ0LDEyNy40MjYgMTM2Ljg2NSwxMjcuMjE5IDEzOS4wMDAsMTI4LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzkuMDAwLDEyOC41MDAgQyAxNDEuODY1LDEzMC4yMTkgMTQxLjk0OSwxMzAuMTEzIDE0NS4wMDAsMTMxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDUuMDAwLDEzMS41MDAgQyAxNDcuNDQ5LDEzMi42MTMgMTQ3LjQwNywxMzIuOTgxIDE1MC4wMDAsMTMzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTAuMDAwLDEzMy41MDAgQyAxNTIuNDA3LDEzMy45ODEgMTUyLjc1MCwxMzQuMjUwIDE1NS4wMDAsMTMzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDY4LjUwMCBDIDE4NC4wMDAsNzUuNTAwIDE4NC4wMDAsNzUuNTAwIDE4NC4wMDAsODIuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE4NC4wMDAsODIuNTAwIEMgMTg0LjAwMCw4NS4wMDAgMTg0LjAwMCw4NS4wMDAgMTg0LjAwMCw4Ny41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTg0LjAwMCw4Ny41MDAgQyAxODQuMDAwLDkxLjAwMCAxODQuMDAwLDkxLjAwMCAxODQuMDAwLDk0LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDk0LjUwMCBDIDE4NC4wMDAsOTcuNTAwIDE4NC4wMDAsOTcuNTAwIDE4NC4wMDAsMTAwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEwMC41MDAgQyAxODQuMDAwLDEwMy4wMDAgMTg0LjAwMCwxMDMuMDAwIDE4NC4wMDAsMTA1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEwNS41MDAgQyAxODQuMDAwLDEwOC4wMDAgMTg0LjAwMCwxMDguMDAwIDE4NC4wMDAsMTEwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDExMC41MDAgQyAxODQuMDAwLDExMy4wMDAgMTg0LjAwMCwxMTMuMDAwIDE4NC4wMDAsMTE1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDExNS41MDAgQyAxODQuMDAwLDExOC41MDAgMTg0LjAwMCwxMTguNTAwIDE4NC4wMDAsMTIxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEyMS41MDAgQyAxODQuMDAwLDEyNS4wMDAgMTg0LjAwMCwxMjUuMDAwIDE4NC4wMDAsMTI4LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAyMDguMDAwLDcyLjUwMCBDIDIwOC4wMDAsNzYuMDAwIDIwOC4wMDAsNzYuMDAwIDIwOC4wMDAsNzkuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDIwOC4wMDAsNzkuNTAwIEMgMjA4LjAwMCw4Mi4wMDAgMjA4LjAwMCw4Mi4wMDAgMjA4LjAwMCw4NC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCw4NC41MDAgQyAyMDguMDAwLDg4LjUwMCAyMDguMDAwLDg4LjUwMCAyMDguMDAwLDkyLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAyMDguMDAwLDkyLjUwMCBDIDIwOC4wMDAsOTUuMDAwIDIwOC4wMDAsOTUuMDAwIDIwOC4wMDAsOTcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDIwOC4wMDAsOTcuNTAwIEMgMjA4LjAwMCwxMDEuMDAwIDIwOC4wMDAsMTAxLjAwMCAyMDguMDAwLDEwNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMDQuNTAwIEMgMjA4LjAwMCwxMDcuMDAwIDIwOC4wMDAsMTA3LjAwMCAyMDguMDAwLDEwOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMDkuNTAwIEMgMjA4LjAwMCwxMTIuMDAwIDIwOC4wMDAsMTEyLjAwMCAyMDguMDAwLDExNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMTQuNTAwIEMgMjA4LjAwMCwxMTcuMDAwIDIwOC4yNDgsMTE3LjAyNSAyMDguMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMTkuNTAwIEMgMjA3Ljc0OCwxMjIuMDI1IDIwNy41MDAsMTIyLjAwMCAyMDcuMDAwLDEyNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI3LjAwMCwxMDMuNTAwIEMgMjI2LjUwMCwxMDYuNTAwIDIyNi41NDQsMTA2LjUwOCAyMjYuMDAwLDEwOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI2LjAwMCwxMDkuNTAwIEMgMjI1LjU0NCwxMTIuMDA4IDIyNS41MDAsMTEyLjAwMCAyMjUuMDAwLDExNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI1LjAwMCwxMTQuNTAwIEMgMjI0LjUwMCwxMTcuMDAwIDIyNC4yNTIsMTE2Ljk3NSAyMjQuMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI0LjAwMCwxMTkuNTAwIEMgMjIzLjc1MiwxMjEuOTc1IDIyMy4yNTAsMTIyLjI1MCAyMjQuMDAwLDEyNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI0LjAwMCwxMjQuNTAwIEMgMjI0Ljc1MCwxMjYuNzUwIDIyNS4wMDAsMTI3LjUwMCAyMjcuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI3LjAwMCwxMjguNTAwIEMgMjI5LjAwMCwxMjkuNTAwIDIyOS41MDAsMTI4LjUwMCAyMzIuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjMyLjAwMCwxMjguNTAwIEMgMjM0LjUwMCwxMjguNTAwIDIzNC41MDAsMTI4LjUwMCAyMzcuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjM3LjAwMCwxMjguNTAwIEMgMjM5LjUwMCwxMjguNTAwIDIzOS41OTMsMTI4Ljk4MSAyNDIuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjQyLjAwMCwxMjguNTAwIEMgMjQ0LjU5MywxMjcuOTgxIDI0NC44MDUsMTI3Ljk2MyAyNDcuMDAwLDEyNi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjQ3LjAwMCwxMjYuNTAwIEMgMjQ5LjMwNSwxMjQuOTYzIDI0OS40NjMsMTI0LjgwNSAyNTEuMDAwLDEyMi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjUxLjAwMCwxMjIuNTAwIEMgMjUyLjQ2MywxMjAuMzA1IDI1NC42NjQsMTE5LjI0MyAyNTMuMDAwLDExNy41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjUzLjAwMCwxMTcuNTAwIEMgMjQ0LjE2NCwxMDguMjQzIDI0MS40OTEsMTA2LjQ1OCAyMzAuMDAwLDEwMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjwvc3ZnPg==",
          "valueName": "svgVal"
      }
  ],
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [
          {
              "deleted": false,
              "description": "Toyota 8FGCU25",
              "id": "d237d262-e5a6-4251-bc06-37f516dbed5c",
              "item": "Forklift",
              "quantity": 1.0,
              "timespan": 7200000
          }
      ],
      "worklogEntries": [
          {
              "deleted": false,
              "description": "Room 302 lights",
              "headcount": 1,
              "id": "e76fe3f4-f587-4309-92c4-6a6f14b9e1bd",
              "timespan": 7200000,
              "trade": "Electrical"
          }
      ]
  },
  "updatedAt": "2023-03-10T23:12:45.627778+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

### Option 10: Update the materials log table

Create a new UUID to identify each new row, for this example we will use `` 5b4fe828-fd45-4a9e-a660-6b70cb47c39f` ``

```
curl --location --request PUT 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/forms/:formId/values:batch-update' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
  "tabularValues": [
      {
          "table": "materialsEntries",
          "id": "5b4fe828-fd45-4a9e-a660-6b70cb47c39f",
          "columns": [
              {
                  "columnName": "item",
                  "textVal": "Sand"
              },
              {
                  "columnName": "quantity",
                  "numberVal": 2
              },
              {
                  "columnName": "unit",
                  "textVal": "tons"
              },
              {
                  "columnName": "description",
                  "textVal": "fill for pool area"
              }
          ]
      }
  ]
}'

```

Show More

### response

```
{{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "toggleVal": "Yes",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "textVal": "This is my response!",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "notes": null,
          "numberVal": 42.0,
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "choiceVal": "Answer 2",
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "choiceVal": "Answer 3",
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "arrayVal": "['Answer 2', 'Answer 3']",
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "dateVal": "1999-12-31",
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "name": "Jane Doe",
          "notes": null,
          "sectionLabel": "All question types",
          "svgVal": "PHN2ZyBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDU1MCAyMDAiIHdpZHRoPSI1NTAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTSA3OC4wMDAsNDYuNTAwIEMgNzguMDAwLDQ5LjAwMCA3OC4wMDAsNDkuMDAwIDc4LjAwMCw1MS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDUxLjUwMCBDIDc4LjAwMCw1NS4wMDAgNzguMDAwLDU1LjAwMCA3OC4wMDAsNTguNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw1OC41MDAgQyA3OC4wMDAsNjEuMDAwIDc4LjAwMCw2MS4wMDAgNzguMDAwLDYzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsNjMuNTAwIEMgNzguMDAwLDY3LjAwMCA3OC4wMDAsNjcuMDAwIDc4LjAwMCw3MC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDcwLjUwMCBDIDc4LjAwMCw3NC4wMDAgNzguMDAwLDc0LjAwMCA3OC4wMDAsNzcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw3Ny41MDAgQyA3OC4wMDAsODAuNTAwIDc4LjAwMCw4MC41MDAgNzguMDAwLDgzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsODMuNTAwIEMgNzguMDAwLDg3LjAwMCA3OC4wMDAsODcuMDAwIDc4LjAwMCw5MC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDkwLjUwMCBDIDc4LjAwMCw5My4wMDAgNzguMDAwLDkzLjAwMCA3OC4wMDAsOTUuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw5NS41MDAgQyA3OC4wMDAsOTguMDAwIDc4LjAwMCw5OC4wMDAgNzguMDAwLDEwMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDEwMC41MDAgQyA3OC4wMDAsMTAzLjAwMCA3OC4wMDAsMTAzLjAwMCA3OC4wMDAsMTA1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsMTA1LjUwMCBDIDc4LjAwMCwxMTAuMDAwIDc4LjMxOSwxMTAuMDMyIDc4LjAwMCwxMTQuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCwxMTQuNTAwIEMgNzcuODE5LDExNy4wMzIgNzcuNTAwLDExNy4wMDAgNzcuMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzcuMDAwLDExOS41MDAgQyA3Ni41MDAsMTIyLjAwMCA3Ni41MDAsMTIyLjAwMCA3Ni4wMDAsMTI0LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3Ni4wMDAsMTI0LjUwMCBDIDc1LjUwMCwxMjcuMDAwIDc1LjQxOSwxMjYuOTg2IDc1LjAwMCwxMjkuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc1LjAwMCwxMjkuNTAwIEMgNzQuNDE5LDEzMi45ODYgNzQuNTgxLDEzMy4wMTQgNzQuMDAwLDEzNi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCw1MS41MDAgQyAxMTEuMDAwLDU0LjAwMCAxMTEuMDAwLDU0LjAwMCAxMTEuMDAwLDU2LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMTEuMDAwLDU2LjUwMCBDIDExMS4wMDAsNTkuMDAwIDExMS4wMDAsNTkuMDAwIDExMS4wMDAsNjEuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDExMS4wMDAsNjEuNTAwIEMgMTExLjAwMCw2NS4wMDAgMTExLjAwMCw2NS4wMDAgMTExLjAwMCw2OC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCw2OC41MDAgQyAxMTEuMDAwLDk0LjUwMCAxMTEuMDAwLDk0LjUwMCAxMTEuMDAwLDEyMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCwxMjAuNTAwIEMgMTExLjAwMCwxMjMuMDAwIDExMS4wMDAsMTIzLjAwMCAxMTEuMDAwLDEyNS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCwxMjUuNTAwIEMgMTExLjAwMCwxMjguMDAwIDExMS4wMDAsMTI4LjAwMCAxMTEuMDAwLDEzMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDkzLjUwMCBDIDgwLjUwMCw5My41MDAgODAuNTAwLDkzLjUwMCA4My4wMDAsOTMuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDgzLjAwMCw5My41MDAgQyA4NS41MDAsOTMuNTAwIDg1LjUwMCw5My41MDAgODguMDAwLDkzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA4OC4wMDAsOTMuNTAwIEMgOTAuNTAwLDkzLjUwMCA5MC41MDAsOTMuNTAwIDkzLjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gOTMuMDAwLDkzLjUwMCBDIDk1LjUwMCw5My41MDAgOTUuNTAwLDkzLjUwMCA5OC4wMDAsOTMuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDk4LjAwMCw5My41MDAgQyAxMDAuNTAwLDkzLjUwMCAxMDAuNTA3LDkzLjY1NiAxMDMuMDAwLDkzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMjQuMDAwLDEwOS41MDAgQyAxMjcuNTAwLDEwOS41MDAgMTI3LjUwMCwxMDkuNTAwIDEzMS4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzEuMDAwLDEwOS41MDAgQyAxMzQuNTAwLDEwOS41MDAgMTM0LjUwMCwxMDkuNTAwIDEzOC4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzguMDAwLDEwOS41MDAgQyAxNDEuMDAwLDEwOS41MDAgMTQxLjAwMCwxMDkuNTAwIDE0NC4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDQuMDAwLDEwOS41MDAgQyAxNDYuNTAwLDEwOS41MDAgMTQ2LjU5MywxMDkuOTgxIDE0OS4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDkuMDAwLDEwOS41MDAgQyAxNTEuNTkzLDEwOC45ODEgMTUxLjkyNiwxMDkuMDU2IDE1NC4wMDAsMTA3LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTQuMDAwLDEwNy41MDAgQyAxNTUuOTI2LDEwNi4wNTYgMTU2LjMxOCwxMDUuNzczIDE1Ny4wMDAsMTAzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTcuMDAwLDEwMy41MDAgQyAxNTcuODE4LDEwMC43NzMgMTU4LjAyOSwxMDAuMDc0IDE1Ny4wMDAsOTcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE1Ny4wMDAsOTcuNTAwIEMgMTU2LjAyOSw5NS4wNzQgMTU1LjM2MSw5NC45MTYgMTUzLjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTUzLjAwMCw5My41MDAgQyAxNTAuMzYxLDkxLjkxNiAxNTAuMDQ1LDkyLjMzMCAxNDcuMDAwLDkxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDcuMDAwLDkxLjUwMCBDIDE0NC41NDUsOTAuODMwIDE0NC4yNzIsODkuOTk1IDE0Mi4wMDAsOTAuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE0Mi4wMDAsOTAuNTAwIEMgMTM5Ljc3Miw5MC45OTUgMTM4LjY5Myw5MS4xODkgMTM4LjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTM4LjAwMCw5My41MDAgQyAxMzQuMTkzLDEwNi4xODkgMTM0LjI1NCwxMDcuMTIzIDEzMy4wMDAsMTIwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzMuMDAwLDEyMC41MDAgQyAxMzIuNzU0LDEyMy4xMjMgMTMzLjQ0NCwxMjMuNDI2IDEzNS4wMDAsMTI1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzUuMDAwLDEyNS41MDAgQyAxMzYuNDQ0LDEyNy40MjYgMTM2Ljg2NSwxMjcuMjE5IDEzOS4wMDAsMTI4LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzkuMDAwLDEyOC41MDAgQyAxNDEuODY1LDEzMC4yMTkgMTQxLjk0OSwxMzAuMTEzIDE0NS4wMDAsMTMxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDUuMDAwLDEzMS41MDAgQyAxNDcuNDQ5LDEzMi42MTMgMTQ3LjQwNywxMzIuOTgxIDE1MC4wMDAsMTMzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTAuMDAwLDEzMy41MDAgQyAxNTIuNDA3LDEzMy45ODEgMTUyLjc1MCwxMzQuMjUwIDE1NS4wMDAsMTMzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDY4LjUwMCBDIDE4NC4wMDAsNzUuNTAwIDE4NC4wMDAsNzUuNTAwIDE4NC4wMDAsODIuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE4NC4wMDAsODIuNTAwIEMgMTg0LjAwMCw4NS4wMDAgMTg0LjAwMCw4NS4wMDAgMTg0LjAwMCw4Ny41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTg0LjAwMCw4Ny41MDAgQyAxODQuMDAwLDkxLjAwMCAxODQuMDAwLDkxLjAwMCAxODQuMDAwLDk0LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDk0LjUwMCBDIDE4NC4wMDAsOTcuNTAwIDE4NC4wMDAsOTcuNTAwIDE4NC4wMDAsMTAwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEwMC41MDAgQyAxODQuMDAwLDEwMy4wMDAgMTg0LjAwMCwxMDMuMDAwIDE4NC4wMDAsMTA1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEwNS41MDAgQyAxODQuMDAwLDEwOC4wMDAgMTg0LjAwMCwxMDguMDAwIDE4NC4wMDAsMTEwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDExMC41MDAgQyAxODQuMDAwLDExMy4wMDAgMTg0LjAwMCwxMTMuMDAwIDE4NC4wMDAsMTE1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDExNS41MDAgQyAxODQuMDAwLDExOC41MDAgMTg0LjAwMCwxMTguNTAwIDE4NC4wMDAsMTIxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEyMS41MDAgQyAxODQuMDAwLDEyNS4wMDAgMTg0LjAwMCwxMjUuMDAwIDE4NC4wMDAsMTI4LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAyMDguMDAwLDcyLjUwMCBDIDIwOC4wMDAsNzYuMDAwIDIwOC4wMDAsNzYuMDAwIDIwOC4wMDAsNzkuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDIwOC4wMDAsNzkuNTAwIEMgMjA4LjAwMCw4Mi4wMDAgMjA4LjAwMCw4Mi4wMDAgMjA4LjAwMCw4NC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCw4NC41MDAgQyAyMDguMDAwLDg4LjUwMCAyMDguMDAwLDg4LjUwMCAyMDguMDAwLDkyLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAyMDguMDAwLDkyLjUwMCBDIDIwOC4wMDAsOTUuMDAwIDIwOC4wMDAsOTUuMDAwIDIwOC4wMDAsOTcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDIwOC4wMDAsOTcuNTAwIEMgMjA4LjAwMCwxMDEuMDAwIDIwOC4wMDAsMTAxLjAwMCAyMDguMDAwLDEwNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMDQuNTAwIEMgMjA4LjAwMCwxMDcuMDAwIDIwOC4wMDAsMTA3LjAwMCAyMDguMDAwLDEwOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMDkuNTAwIEMgMjA4LjAwMCwxMTIuMDAwIDIwOC4wMDAsMTEyLjAwMCAyMDguMDAwLDExNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMTQuNTAwIEMgMjA4LjAwMCwxMTcuMDAwIDIwOC4yNDgsMTE3LjAyNSAyMDguMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMTkuNTAwIEMgMjA3Ljc0OCwxMjIuMDI1IDIwNy41MDAsMTIyLjAwMCAyMDcuMDAwLDEyNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI3LjAwMCwxMDMuNTAwIEMgMjI2LjUwMCwxMDYuNTAwIDIyNi41NDQsMTA2LjUwOCAyMjYuMDAwLDEwOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI2LjAwMCwxMDkuNTAwIEMgMjI1LjU0NCwxMTIuMDA4IDIyNS41MDAsMTEyLjAwMCAyMjUuMDAwLDExNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI1LjAwMCwxMTQuNTAwIEMgMjI0LjUwMCwxMTcuMDAwIDIyNC4yNTIsMTE2Ljk3NSAyMjQuMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI0LjAwMCwxMTkuNTAwIEMgMjIzLjc1MiwxMjEuOTc1IDIyMy4yNTAsMTIyLjI1MCAyMjQuMDAwLDEyNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI0LjAwMCwxMjQuNTAwIEMgMjI0Ljc1MCwxMjYuNzUwIDIyNS4wMDAsMTI3LjUwMCAyMjcuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI3LjAwMCwxMjguNTAwIEMgMjI5LjAwMCwxMjkuNTAwIDIyOS41MDAsMTI4LjUwMCAyMzIuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjMyLjAwMCwxMjguNTAwIEMgMjM0LjUwMCwxMjguNTAwIDIzNC41MDAsMTI4LjUwMCAyMzcuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjM3LjAwMCwxMjguNTAwIEMgMjM5LjUwMCwxMjguNTAwIDIzOS41OTMsMTI4Ljk4MSAyNDIuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjQyLjAwMCwxMjguNTAwIEMgMjQ0LjU5MywxMjcuOTgxIDI0NC44MDUsMTI3Ljk2MyAyNDcuMDAwLDEyNi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjQ3LjAwMCwxMjYuNTAwIEMgMjQ5LjMwNSwxMjQuOTYzIDI0OS40NjMsMTI0LjgwNSAyNTEuMDAwLDEyMi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjUxLjAwMCwxMjIuNTAwIEMgMjUyLjQ2MywxMjAuMzA1IDI1NC42NjQsMTE5LjI0MyAyNTMuMDAwLDExNy41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjUzLjAwMCwxMTcuNTAwIEMgMjQ0LjE2NCwxMDguMjQzIDI0MS40OTEsMTA2LjQ1OCAyMzAuMDAwLDEwMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjwvc3ZnPg==",
          "valueName": "svgVal"
      }
  ],
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "draft",
  "tabularValues": {
      "equipmentEntries": [
          {
              "deleted": false,
              "description": "Toyota 8FGCU25",
              "id": "d237d262-e5a6-4251-bc06-37f516dbed5c",
              "item": "Forklift",
              "quantity": 1.0,
              "timespan": 7200000
          }
      ],
      "materialsEntries": [
          {
              "deleted": false,
              "description": "fill for pool area",
              "id": "5b4fe828-fd45-4a9e-a660-6b70cb47c39f",
              "item": "Sand",
              "quantity": 2.0,
              "unit": "tons"
          }
      ],
      "worklogEntries": [
          {
              "deleted": false,
              "description": "Room 302 lights",
              "headcount": 1,
              "id": "e76fe3f4-f587-4309-92c4-6a6f14b9e1bd",
              "timespan": 7200000,
              "trade": "Electrical"
          }
      ]
  },
  "updatedAt": "2023-03-10T23:16:20.758371+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null

```

Show More

}

## [Step 5: Submit the Form](#step-5-submit-the-form)

The [PATCH forms/:formId](../http-docs/http-forms-forms-formId-PATCH.md) endpoint is used to submit the form, see the endpoint documentation for supported fields.

Using data from previous steps:

- Project ID (`cd13503e-1265-49c3-b2da-477c57cda60c`)
- Template ID (`a304cc08-fadb-58c8-3181-7bb06fdef93e`)
- Form ID (`76ee8c34-1897-4720-bb4f-9ae82c9af02e`)

call [PATCH forms/:formId](../http-docs/http-forms-forms-formId-PATCH.md).

### request

```
curl --location --request PATCH 'https://developer.api.autodesk.com/construction/forms/v1/projects/:projectId/form-templates/:templateId/forms/:formId' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  --data-raw '{
    "status": "submitted"
  }'

```

### response

```
{
  "assigneeId": null,
  "assigneeType": null,
  "createdAt": "2023-03-10T22:13:03.159982+00:00",
  "createdBy": "2B86MMXDQA8N",
  "customValues": [
      {
          "fieldId": "a184ac19-01b5-250e-43d3-56c63b61f952",
          "itemLabel": "Preconfigured response",
          "notes": null,
          "sectionLabel": "All question types",
          "toggleVal": "Yes",
          "valueName": "toggleVal"
      },
      {
          "fieldId": "4aa5a9fa-754c-233d-83bb-7a87654c45f0",
          "itemLabel": "Text response",
          "notes": null,
          "sectionLabel": "All question types",
          "textVal": "This is my response!",
          "valueName": "textVal"
      },
      {
          "fieldId": "c22f00f7-cb45-165e-0222-43b62b75ef82",
          "itemLabel": "Number response",
          "notes": null,
          "numberVal": 42.0,
          "sectionLabel": "All question types",
          "valueName": "numberVal"
      },
      {
          "choiceVal": "Answer 2",
          "fieldId": "cad4dad2-f757-ba11-4301-b3d45af067fd",
          "itemLabel": "Single-select response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "choiceVal": "Answer 3",
          "fieldId": "819a9cac-f1fe-f503-5e05-6a88a96f440d",
          "itemLabel": "Dropdown response",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "choiceVal"
      },
      {
          "arrayVal": "['Answer 2', 'Answer 3']",
          "fieldId": "44bd91a4-0173-6b30-7259-8f38fcd21eaa",
          "itemLabel": "Multiple-select responses",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "arrayVal"
      },
      {
          "dateVal": "1999-12-31",
          "fieldId": "14a92003-39d3-4d1d-fa33-824af6f5dd06",
          "itemLabel": "Date",
          "notes": null,
          "sectionLabel": "All question types",
          "valueName": "dateVal"
      },
      {
          "fieldId": "fa398168-8a80-06bb-06e5-f77710dd507b",
          "itemLabel": "Signature",
          "name": "Jone Doe",
          "notes": null,
          "sectionLabel": "All question types",
          "svgVal": "PHN2ZyBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDU1MCAyMDAiIHdpZHRoPSI1NTAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTSA3OC4wMDAsNDYuNTAwIEMgNzguMDAwLDQ5LjAwMCA3OC4wMDAsNDkuMDAwIDc4LjAwMCw1MS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDUxLjUwMCBDIDc4LjAwMCw1NS4wMDAgNzguMDAwLDU1LjAwMCA3OC4wMDAsNTguNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw1OC41MDAgQyA3OC4wMDAsNjEuMDAwIDc4LjAwMCw2MS4wMDAgNzguMDAwLDYzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsNjMuNTAwIEMgNzguMDAwLDY3LjAwMCA3OC4wMDAsNjcuMDAwIDc4LjAwMCw3MC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDcwLjUwMCBDIDc4LjAwMCw3NC4wMDAgNzguMDAwLDc0LjAwMCA3OC4wMDAsNzcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw3Ny41MDAgQyA3OC4wMDAsODAuNTAwIDc4LjAwMCw4MC41MDAgNzguMDAwLDgzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsODMuNTAwIEMgNzguMDAwLDg3LjAwMCA3OC4wMDAsODcuMDAwIDc4LjAwMCw5MC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDkwLjUwMCBDIDc4LjAwMCw5My4wMDAgNzguMDAwLDkzLjAwMCA3OC4wMDAsOTUuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCw5NS41MDAgQyA3OC4wMDAsOTguMDAwIDc4LjAwMCw5OC4wMDAgNzguMDAwLDEwMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDEwMC41MDAgQyA3OC4wMDAsMTAzLjAwMCA3OC4wMDAsMTAzLjAwMCA3OC4wMDAsMTA1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3OC4wMDAsMTA1LjUwMCBDIDc4LjAwMCwxMTAuMDAwIDc4LjMxOSwxMTAuMDMyIDc4LjAwMCwxMTQuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc4LjAwMCwxMTQuNTAwIEMgNzcuODE5LDExNy4wMzIgNzcuNTAwLDExNy4wMDAgNzcuMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzcuMDAwLDExOS41MDAgQyA3Ni41MDAsMTIyLjAwMCA3Ni41MDAsMTIyLjAwMCA3Ni4wMDAsMTI0LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA3Ni4wMDAsMTI0LjUwMCBDIDc1LjUwMCwxMjcuMDAwIDc1LjQxOSwxMjYuOTg2IDc1LjAwMCwxMjkuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDc1LjAwMCwxMjkuNTAwIEMgNzQuNDE5LDEzMi45ODYgNzQuNTgxLDEzMy4wMTQgNzQuMDAwLDEzNi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCw1MS41MDAgQyAxMTEuMDAwLDU0LjAwMCAxMTEuMDAwLDU0LjAwMCAxMTEuMDAwLDU2LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMTEuMDAwLDU2LjUwMCBDIDExMS4wMDAsNTkuMDAwIDExMS4wMDAsNTkuMDAwIDExMS4wMDAsNjEuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDExMS4wMDAsNjEuNTAwIEMgMTExLjAwMCw2NS4wMDAgMTExLjAwMCw2NS4wMDAgMTExLjAwMCw2OC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCw2OC41MDAgQyAxMTEuMDAwLDk0LjUwMCAxMTEuMDAwLDk0LjUwMCAxMTEuMDAwLDEyMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCwxMjAuNTAwIEMgMTExLjAwMCwxMjMuMDAwIDExMS4wMDAsMTIzLjAwMCAxMTEuMDAwLDEyNS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTExLjAwMCwxMjUuNTAwIEMgMTExLjAwMCwxMjguMDAwIDExMS4wMDAsMTI4LjAwMCAxMTEuMDAwLDEzMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gNzguMDAwLDkzLjUwMCBDIDgwLjUwMCw5My41MDAgODAuNTAwLDkzLjUwMCA4My4wMDAsOTMuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDgzLjAwMCw5My41MDAgQyA4NS41MDAsOTMuNTAwIDg1LjUwMCw5My41MDAgODguMDAwLDkzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSA4OC4wMDAsOTMuNTAwIEMgOTAuNTAwLDkzLjUwMCA5MC41MDAsOTMuNTAwIDkzLjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gOTMuMDAwLDkzLjUwMCBDIDk1LjUwMCw5My41MDAgOTUuNTAwLDkzLjUwMCA5OC4wMDAsOTMuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDk4LjAwMCw5My41MDAgQyAxMDAuNTAwLDkzLjUwMCAxMDAuNTA3LDkzLjY1NiAxMDMuMDAwLDkzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMjQuMDAwLDEwOS41MDAgQyAxMjcuNTAwLDEwOS41MDAgMTI3LjUwMCwxMDkuNTAwIDEzMS4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzEuMDAwLDEwOS41MDAgQyAxMzQuNTAwLDEwOS41MDAgMTM0LjUwMCwxMDkuNTAwIDEzOC4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzguMDAwLDEwOS41MDAgQyAxNDEuMDAwLDEwOS41MDAgMTQxLjAwMCwxMDkuNTAwIDE0NC4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDQuMDAwLDEwOS41MDAgQyAxNDYuNTAwLDEwOS41MDAgMTQ2LjU5MywxMDkuOTgxIDE0OS4wMDAsMTA5LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDkuMDAwLDEwOS41MDAgQyAxNTEuNTkzLDEwOC45ODEgMTUxLjkyNiwxMDkuMDU2IDE1NC4wMDAsMTA3LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTQuMDAwLDEwNy41MDAgQyAxNTUuOTI2LDEwNi4wNTYgMTU2LjMxOCwxMDUuNzczIDE1Ny4wMDAsMTAzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTcuMDAwLDEwMy41MDAgQyAxNTcuODE4LDEwMC43NzMgMTU4LjAyOSwxMDAuMDc0IDE1Ny4wMDAsOTcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE1Ny4wMDAsOTcuNTAwIEMgMTU2LjAyOSw5NS4wNzQgMTU1LjM2MSw5NC45MTYgMTUzLjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTUzLjAwMCw5My41MDAgQyAxNTAuMzYxLDkxLjkxNiAxNTAuMDQ1LDkyLjMzMCAxNDcuMDAwLDkxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDcuMDAwLDkxLjUwMCBDIDE0NC41NDUsOTAuODMwIDE0NC4yNzIsODkuOTk1IDE0Mi4wMDAsOTAuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE0Mi4wMDAsOTAuNTAwIEMgMTM5Ljc3Miw5MC45OTUgMTM4LjY5Myw5MS4xODkgMTM4LjAwMCw5My41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTM4LjAwMCw5My41MDAgQyAxMzQuMTkzLDEwNi4xODkgMTM0LjI1NCwxMDcuMTIzIDEzMy4wMDAsMTIwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzMuMDAwLDEyMC41MDAgQyAxMzIuNzU0LDEyMy4xMjMgMTMzLjQ0NCwxMjMuNDI2IDEzNS4wMDAsMTI1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzUuMDAwLDEyNS41MDAgQyAxMzYuNDQ0LDEyNy40MjYgMTM2Ljg2NSwxMjcuMjE5IDEzOS4wMDAsMTI4LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxMzkuMDAwLDEyOC41MDAgQyAxNDEuODY1LDEzMC4yMTkgMTQxLjk0OSwxMzAuMTEzIDE0NS4wMDAsMTMxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNDUuMDAwLDEzMS41MDAgQyAxNDcuNDQ5LDEzMi42MTMgMTQ3LjQwNywxMzIuOTgxIDE1MC4wMDAsMTMzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxNTAuMDAwLDEzMy41MDAgQyAxNTIuNDA3LDEzMy45ODEgMTUyLjc1MCwxMzQuMjUwIDE1NS4wMDAsMTMzLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDY4LjUwMCBDIDE4NC4wMDAsNzUuNTAwIDE4NC4wMDAsNzUuNTAwIDE4NC4wMDAsODIuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDE4NC4wMDAsODIuNTAwIEMgMTg0LjAwMCw4NS4wMDAgMTg0LjAwMCw4NS4wMDAgMTg0LjAwMCw4Ny41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMTg0LjAwMCw4Ny41MDAgQyAxODQuMDAwLDkxLjAwMCAxODQuMDAwLDkxLjAwMCAxODQuMDAwLDk0LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDk0LjUwMCBDIDE4NC4wMDAsOTcuNTAwIDE4NC4wMDAsOTcuNTAwIDE4NC4wMDAsMTAwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEwMC41MDAgQyAxODQuMDAwLDEwMy4wMDAgMTg0LjAwMCwxMDMuMDAwIDE4NC4wMDAsMTA1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEwNS41MDAgQyAxODQuMDAwLDEwOC4wMDAgMTg0LjAwMCwxMDguMDAwIDE4NC4wMDAsMTEwLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDExMC41MDAgQyAxODQuMDAwLDExMy4wMDAgMTg0LjAwMCwxMTMuMDAwIDE4NC4wMDAsMTE1LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDExNS41MDAgQyAxODQuMDAwLDExOC41MDAgMTg0LjAwMCwxMTguNTAwIDE4NC4wMDAsMTIxLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAxODQuMDAwLDEyMS41MDAgQyAxODQuMDAwLDEyNS4wMDAgMTg0LjAwMCwxMjUuMDAwIDE4NC4wMDAsMTI4LjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAyMDguMDAwLDcyLjUwMCBDIDIwOC4wMDAsNzYuMDAwIDIwOC4wMDAsNzYuMDAwIDIwOC4wMDAsNzkuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDIwOC4wMDAsNzkuNTAwIEMgMjA4LjAwMCw4Mi4wMDAgMjA4LjAwMCw4Mi4wMDAgMjA4LjAwMCw4NC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCw4NC41MDAgQyAyMDguMDAwLDg4LjUwMCAyMDguMDAwLDg4LjUwMCAyMDguMDAwLDkyLjUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2Utd2lkdGg9IjIuMjUwIj48L3BhdGg+PHBhdGggZD0iTSAyMDguMDAwLDkyLjUwMCBDIDIwOC4wMDAsOTUuMDAwIDIwOC4wMDAsOTUuMDAwIDIwOC4wMDAsOTcuNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS13aWR0aD0iMi4yNTAiPjwvcGF0aD48cGF0aCBkPSJNIDIwOC4wMDAsOTcuNTAwIEMgMjA4LjAwMCwxMDEuMDAwIDIwOC4wMDAsMTAxLjAwMCAyMDguMDAwLDEwNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMDQuNTAwIEMgMjA4LjAwMCwxMDcuMDAwIDIwOC4wMDAsMTA3LjAwMCAyMDguMDAwLDEwOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMDkuNTAwIEMgMjA4LjAwMCwxMTIuMDAwIDIwOC4wMDAsMTEyLjAwMCAyMDguMDAwLDExNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMTQuNTAwIEMgMjA4LjAwMCwxMTcuMDAwIDIwOC4yNDgsMTE3LjAyNSAyMDguMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjA4LjAwMCwxMTkuNTAwIEMgMjA3Ljc0OCwxMjIuMDI1IDIwNy41MDAsMTIyLjAwMCAyMDcuMDAwLDEyNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI3LjAwMCwxMDMuNTAwIEMgMjI2LjUwMCwxMDYuNTAwIDIyNi41NDQsMTA2LjUwOCAyMjYuMDAwLDEwOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI2LjAwMCwxMDkuNTAwIEMgMjI1LjU0NCwxMTIuMDA4IDIyNS41MDAsMTEyLjAwMCAyMjUuMDAwLDExNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI1LjAwMCwxMTQuNTAwIEMgMjI0LjUwMCwxMTcuMDAwIDIyNC4yNTIsMTE2Ljk3NSAyMjQuMDAwLDExOS41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI0LjAwMCwxMTkuNTAwIEMgMjIzLjc1MiwxMjEuOTc1IDIyMy4yNTAsMTIyLjI1MCAyMjQuMDAwLDEyNC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI0LjAwMCwxMjQuNTAwIEMgMjI0Ljc1MCwxMjYuNzUwIDIyNS4wMDAsMTI3LjUwMCAyMjcuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjI3LjAwMCwxMjguNTAwIEMgMjI5LjAwMCwxMjkuNTAwIDIyOS41MDAsMTI4LjUwMCAyMzIuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjMyLjAwMCwxMjguNTAwIEMgMjM0LjUwMCwxMjguNTAwIDIzNC41MDAsMTI4LjUwMCAyMzcuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjM3LjAwMCwxMjguNTAwIEMgMjM5LjUwMCwxMjguNTAwIDIzOS41OTMsMTI4Ljk4MSAyNDIuMDAwLDEyOC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjQyLjAwMCwxMjguNTAwIEMgMjQ0LjU5MywxMjcuOTgxIDI0NC44MDUsMTI3Ljk2MyAyNDcuMDAwLDEyNi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjQ3LjAwMCwxMjYuNTAwIEMgMjQ5LjMwNSwxMjQuOTYzIDI0OS40NjMsMTI0LjgwNSAyNTEuMDAwLDEyMi41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjUxLjAwMCwxMjIuNTAwIEMgMjUyLjQ2MywxMjAuMzA1IDI1NC42NjQsMTE5LjI0MyAyNTMuMDAwLDExNy41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjxwYXRoIGQ9Ik0gMjUzLjAwMCwxMTcuNTAwIEMgMjQ0LjE2NCwxMDguMjQzIDI0MS40OTEsMTA2LjQ1OCAyMzAuMDAwLDEwMC41MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjI1MCI+PC9wYXRoPjwvc3ZnPg==",
          "valueName": "svgVal"
      }
  ],
  "description": "Updated via API",
  "formDate": "2023-03-10",
  "formNum": 1,
  "formTemplate": {
      "id": "a304cc08-fadb-58c8-3181-7bb06fdef93e",
      "name": "Example Template",
      "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
      "status": "active",
      "templateType": null
  },
  "id": "76ee8c34-1897-4720-bb4f-9ae82c9af02e",
  "lastSubmitterSignature": null,
  "locationId": null,
  "notes": null,
  "projectId": "cd13503e-1265-49c3-b2da-477c57cda60c",
  "status": "submitted",
  "tabularValues": {
      "equipmentEntries": [
          {
              "deleted": false,
              "description": "Toyota 8FGCU25",
              "id": "d237d262-e5a6-4251-bc06-37f516dbed5c",
              "item": "Forklift",
              "quantity": null,
              "timespan": 7200000
          }
      ],
      "materialsEntries": [
          {
              "deleted": false,
              "description": "fill for pool area",
              "id": "5b4fe828-fd45-4a9e-a660-6b70cb47c39f",
              "item": "Sand",
              "quantity": 2.0,
              "unit": "tons"
          }
      ],
      "worklogEntries": [
          {
              "deleted": false,
              "description": "Room 302 lights",
              "headcount": 1,
              "id": "e76fe3f4-f587-4309-92c4-6a6f14b9e1bd",
              "timespan": 7200000,
              "trade": "Electrical"
          }
      ]
  },
  "updatedAt": "2023-03-10T23:16:51.330439+00:00",
  "userCreatedAt": "2023-03-10T22:13:03.163068+00:00",
  "weather": null
}

```

Show More

Congratulations! You have created and updated forms.
