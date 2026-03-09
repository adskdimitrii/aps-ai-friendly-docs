# Retrieve Forms

Source: https://aps.autodesk.com/en/docs/acc/tutorials/forms/retrieve-forms/

---

# Retrieve Forms

This tutorial demonstrates how to retrieve a projectâs Forms.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with the `data:read` scope.
- Verify that you have access to the relevant ACC project.

## [Step 1: Find the Form Template IDs](#step-1-find-the-form-template-ids)

Use the project ID (`9ba6681e-1952-4d54-aac4-9de6d9858dd4`) to retrieve the projectâs Form Templates, by calling [GET form-templates](../http-docs/http-forms-form-templates-GET.md).

### Request

```
curl "https://developer.api.autodesk.com/construction/forms/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/form-templates" -X GET \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/vnd.api+json"

```

### Response

```
{
  "data": [
    {
      "projectId": "9ba6681e-1952-4d54-aac4-9de6d9858dd4",
      "id": "2f634a22-779d-4930-9f08-8391a41fea05",
      "name": "Daily Report",
      "status": "active",
      "templateType": "pg.template_type.daily_report",
      "userPermissions": [
        {
          "permissions": [
            "submit"
          ],
          "userId": "USER123A"
        }
      ],
      "groupPermissions": [
        {
          "permissions": [
            "manage"
          ],
          "roleKey": "hq_access_level:admin",
          "roleName": "Admin"
        }
      ],
      "createdBy": "USER123A",
      "updatedAt": "2020-11-20T16:13:33.615127+00:00",
      "isPdf": true,
      "pdfUrl": "https://link.to/form-template.pdf",
      "forms": {}
    }
  ],
  "pagination": {
    "offset": 0,
    "limit": 50,
    "totalResults": 1,
    "nextUrl": null
  }
}

```

Show More

The response payload includes the Form Template IDs (`data.id`).

## [Step 2: Find the Form IDs](#step-2-find-the-form-ids)

Use the project ID (`9ba6681e-1952-4d54-aac4-9de6d9858dd4`) and template ID (`2f634a22-779d-4930-9f08-8391a41fea05`) from previous step to retrieve the projectâs Forms, by calling [GET forms](../http-docs/http-forms-forms-GET.md).

### Request

```
curl "https://developer.api.autodesk.com/construction/forms/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/forms?templateId=2f634a22-779d-4930-9f08-8391a41fea05" -X GET \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/vnd.api+json"

```

### Response

```
{
  "data": [
    {
      "status": "draft",
      "id": "932da979-e537-4530-b8aa-18607ac6db37",
      "projectId": "9ba6681e-1952-4d54-aac4-9de6d9858dd4",
      "formNum": 1,
      "formDate": "2020-11-20",
      "assigneeId": "USER123A",
      "locationId": "d14ce3a6-e61b-4ab0-a9be-5acf7b5366df",
      "updatedAt": "2020-11-20T16:14:27.615127+00:00",
      "createdBy": "USER123A",
      "notes": "Form notes",
      "description": "Form description",
      "formTemplate": {
        "status": "active",
        "id": "2f634a22-779d-4930-9f08-8391a41fea05",
        "projectId": "9ba6681e-1952-4d54-aac4-9de6d9858dd4",
        "name": "Daily Report",
        "templateType": "pg.template_type.daily_report"
      },
      "pdfValues": [],
      "pdfUrl": null,
      "weather": {
        "summaryKey": "clear",
        "precipitationAccumulation": 2.3,
        "precipitationAccumulationUnit": "in",
        "temperatureMin": 47.1,
        "temperatureMax": 65.1,
        "temperatureUnit": "Fahrenheit",
        "humidity": 0.2,
        "windSpeed": 12.5,
        "windGust": 34.6,
        "speedUnit": "mph",
        "windBearing": 18,
        "hourlyWeather": [
          {
            "id": 1234,
            "hour": "07:00:00",
            "temp": 54.12,
            "windSpeed": 14.2,
            "windBearing": 14,
            "humidity": 0.24,
            "fetchedAt": null,
            "createdAt": "2021-01-20T20:38:32+00:00",
            "updatedAt": "2021-01-20T20:38:32+00:00"
          }
        ]
      },
      "tabularValues": {
        "worklogEntries": [
          {
            "id": "cb95aceb-187a-3a8f-2e5f-502a555c03d5",
            "deleted": false,
            "trade": "Plumbers",
            "timespan": 21600000,
            "headcount": 4,
            "description": "change pipes"
          }
        ],
        "materialsEntries": [
          {
            "id": "2f7e534d-d084-594b-8aa6-147cb8fbc060",
            "deleted": false,
            "item": "Glue",
            "quantity": 3,
            "unit": "qt",
            "description": null
          }
        ],
        "equipmentEntries": [
          {
            "id": "84a32af6-b2b1-c3ae-c186-caef48fe4ffd",
            "deleted": false,
            "item": "Hammer",
            "timespan": 7200000,
            "quantity": 1,
            "description": null
          }
        ]
      },
      "customValues": [
        {
          "sectionLabel": "Observation",
          "itemLabel": "Masks / Face Protection",
          "valueName": "textVal",
          "textVal": "Yes",
          "notes": "Observed Masks and Face Protection"
        }
      ]
    }
  ],
  "pagination": {
    "offset": 0,
    "limit": 50,
    "totalResults": 1,
    "nextUrl": null
  }
}

```

Show More

The response payload includes the Form IDs (`data.id`).

Congratulations! You have retrieved Forms.
