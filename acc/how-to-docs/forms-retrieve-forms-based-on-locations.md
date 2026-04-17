# Retrieve Forms Associated With Specific Locations

Source: https://aps.autodesk.com/en/docs/acc/tutorials/forms/retrieve-forms-based-on-locations/

---

# Retrieve Forms Associated With Specific Locations

This tutorial demonstrates how to retrieve forms that are associated with a specific location in a project.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with the `data:read` scope.
- Verify that you have access to the relevant Forma project, and find the project ID. In the example, the project ID is `9ba6681e-1952-4d54-aac4-9de6d9858dd4`.

## [Step 1: Find the Locations for the Project](#step-1-find-the-locations-for-the-project)

Use the project ID (`9ba6681e-1952-4d54-aac4-9de6d9858dd4`) to retrieve the locations for the project, by calling [GET nodes](../http-docs/http-locations-nodes-GET.md)

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/locations/v2/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/trees/:treeId/nodes' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 3,
    "offset": 0,
    "totalResults": 7,
    "nextUrl": "/locations/v2/containers/4a327b27-897c-4e5a-8e48-6e01c21377f3/trees/default/nodes?limit=3&offset=3"
  },
  "results": [
    {
      "id": "5add4375-f223-4201-88b9-8049e68416aa",
      "parentId": null,
      "type": "Root",
      "name": "Project",
      "description": "Project description",
      "barcode": null,
      "order": 0,
      "documentCount": 0,
      "areaDefined": false
    },
    {
      "id": "d14ce3a6-e61b-4ab0-a9be-5acf7b5366df",
      "parentId": "5add4375-f223-4201-88b9-8049e68416aa",
      "type": "Area",
      "name": "Area 1",
      "description": "An Area 1 node",
      "barcode": "ABC123",
      "order": 0,
      "documentCount": 2,
      "areaDefined": true
    },
    {
      "id": "8da1faf2-a72f-421b-89df-00d77e545faf",
      "parentId": "5add4375-f223-4201-88b9-8049e68416aa",
      "type": "Area",
      "name": "Area 2",
      "description": "An Area 2 node",
      "barcode": "DEF456",
      "order": 1,
      "documentCount": 3,
      "areaDefined": true
    }
  ]
}

```

Show More

The response payload includes the location IDs in the `results` object.

## [Step 2: Find the Forms](#step-2-find-the-forms)

Use the project ID (`9ba6681e-1952-4d54-aac4-9de6d9858dd4`) and the location IDs that you retrieved in the previous step to call [GET forms](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-forms-(Deprecated/)-GET), and use the locations filter to only retrieve forms that are associated with the specified locations.

### request

```
curl "https://developer.api.autodesk.com/construction/forms/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/forms?locationIds=8da1faf2-a72f-421b-89df-00d77e545faf&locationIds=d14ce3a6-e61b-4ab0-a9be-5acf7b5366df" -X GET \
  -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" \
  -H "Content-Type: application/vnd.api+json"

```

### response

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
          "valueName": "numberVal",
          "numberVal": 1,
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

The response payload includes the form IDs (`data.id`) that are associated with the specified locations.

Note that in this example the endpoint only returned a single form (`locationId=d14ce3a6-e61b-4ab0-a9be-5acf7b5366df`) even though it filtered for two locations. This is because only one of the two locations is associated with a form.

Congratulations! You have retrieved forms associated with specific locations.
