# Retrieve a Smart Register

Source: https://aps.autodesk.com/en/docs/acc/tutorials/autospecs/retrieve-smart-register/

---

# Retrieve a Smart Register

This tutorial demonstrates how to retrieve submittal logs that have been imported to the AutoSpecs Smart Register. The steps include retrieving the hub ID for the account in which you want to retrieve the submittal logs, retrieving the ID of the project in which you want to retrieve the submittal logs, retrieving the ID of the relevant version, and retrieving the Smart Register.

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps), and select the Data Management and Autodesk Construction Cloud APIs.
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with the `data:read` scope.
- Verify that you have access to the relevant ACC account and project. Ensure that the logged in user has access to AutoSpecs.
- Upload a spec book to the project. See the [Upload a Spec Book](https://help.autodesk.com/view/AUTOSPECS/ENU/?guid=AutoSpecs_upload) documentation for more details. Note the AutoSpecs API does not currently support uploading spec books.

## [Step 1: Find the Hub ID for the ACC Account](#step-1-find-the-hub-id-for-the-acc-account)

In order to retrieve the ID of the project in which you want to retrieve the Smart Register, you first need to retrieve the ID of the relevant account. Call [GET hubs](../../data/http-docs/http-hubs-GET.md) to find the hub ID for the ACC account that contains the Smart Register you want to retrieve.

Note that the ACC account ID corresponds to a Data Management hub ID. To convert an account ID into a hub ID you need to add a â**b.**" prefix. For example, an account ID of `d952a4eb-ad57-4d64-b9ab-d540b3b4522e` translates to a hub ID of `**b.**\d952a4eb-ad57-4d64-b9ab-d540b3b4522e`.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/project/v1/hubs"

```

### Response

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": {
      "href": "https://developer.api.autodesk.com/project/v1/hubs"
    }
  },
  "data": [
    {
      "type": "hubs",
      "id": "b.86b832e9-b22b-2acf-344b-454b3431ac8c",
      "attributes": {
        "name": "My First Account",
        "extension": {
          "type": "hubs:autodesk.bim360:Account",
          "version": "1.0",
          "schema": {
            "href": "https://developer.api.autodesk.com/schema/v1/versions/hubs:autodesk.bim360:Account-1.0"
          },
          "data": {}
        }
      }
    }
  ]
}

```

Show More

In this example, assume that the account (and the corresponding Data Management hub) that contains the Smart Register you want to retrieve is called `My First Account`.

Find the hub (`data.name`), and note the hub ID - `b.86b832e9-b22b-2acf-344b-454b3431ac8c`.

## [Step 2: Find the Project ID](#step-2-find-the-project-id)

Use the hub ID (`b.86b832e9-b22b-2acf-344b-454b3431ac8c`) to call [GET hubs/:hub_id/projects](../../data/http-docs/http-hubs-hub_id-projects-GET.md) to get a list of all the projects in the account.

Note that the project ID in ACC corresponds to the project ID in the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/). To convert a project ID in ACC to a project ID in the Data Management API, you need to add a â**b.**" prefix. For example, a project ID of `75c643d1-c80b-4bca-800f-111a1111aa1a` translates to a project ID of `**b.**\75c643d1-c80b-4bca-800f-111a1111aa1a`.

### Request

```
curl -X GET -H "Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT" "https://developer.api.autodesk.com/project/v1/hubs/b.86b832e9-b22b-2acf-344b-454b3431ac8c/projects"

```

### Response

```
  {
       "jsonapi": {
               "version": "1.0"
       },
       "links": {
               "self": {
                       "href": "https://developer.api.autodesk.com/project/v1/hubs/b.cGVyc29uYWw6cGUyOWNjZjMy/projects"
               }
       },
       "data": [{
               "type": "projects",
               "id": "b.75c643d1-c80b-4bca-800f-111a1111aa1a",
               "attributes": {
                       "name": "My First Project",
                       "extension": {
                               "type": "projects:autodesk.core:Project",
                               "version": "1.0"
                       }
               }
       }]
}

```

Show More

In this example, assume that `My First Project` is the project that contains the Smart Register you want to retrieve.

Find the project (`data.attributes.name`), and note the project ID (`data.id`) - `b.75c643d1-c80b-4bca-800f-111a1111aa1a`.

## [Step 3: Find the Spec Version](#step-3-find-the-spec-version)

Use the project ID (`75c643d1-c80b-4bca-800f-111a1111aa1a`) to call [GET metadata](../http-docs/http-autospecs-getprojectmetadata-GET.md) to get a list of the spec versions for the project.

Note that you need to remove the â**b.**" prefix from the project ID.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/autospecs/v1/projects/75c643d1-c80b-4bca-800f-111a1111aa1a/metadata' \
     -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
 "projectId": "75c643d1-c80b-4bca-800f-111a1111aa1a",
 "region": "USA",
 "versions": [
  {
   "name": "IFC",
   "status": "Completed",
   "currentVersion": false,
   "createdAt": "2022-11-02T07:29:06.000Z",
   "updatedAt": "2022-11-02T07:29:25.000Z",
   "id": "100"
  },
  {
   "name": "IFC 2",
   "status": "Completed",
   "currentVersion": true,
   "createdAt": "2022-06-20T07:12:26.000Z",
   "updatedAt": "2022-09-22T14:03:16.000Z",
   "id": "101"
  }
 ]
}

```

Show More

In this example, assume that you want to use the current spec version (`currentVersion: true`).

Note the spec version ID (`versions.id`) - `101` of the current version.

Note that before you can access the submittal logs the import of the specification PDFs needs to be complete. To verify the status of the import, check that the `status` is `Completed`.

## [Step 4: Retrieve the Smart Register](#step-4-retrieve-the-smart-register)

Use the project ID (`75c643d1-c80b-4bca-800f-111a1111aa1a`) and the version ID (`101`) to call [GET smartregister](../http-docs/http-autospecs-getversionsmartregister-GET.md) to retrieve the Smart Register.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/autospecs/v1/projects/75c643d1-c80b-4bca-800f-111a1111aa1a/version/101/smartregister' \
     -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
[
 {
  "submittalsHeading": "Metals",
  "divisionCode": "01",
  "divisionName": "GENERAL REQUIREMENTS",
  "specNumber": "017419",
  "specName": "CONSTRUCTION WASTE MANAGEMENT AND DISPOSAL",
  "submittalDescription": "Paint compatibility certificates",
  "specCategory": "Certificates",
  "targetDate": null,
  "userNotes": null,
  "paraCode": "051213",
  "targetGroup": "DIVISION 01 REQUIREMENTS",
  "versionName": null,
  "specSubmittalNumber": 0,
  "submittalId": "146"
 },
 {
  "submittalsHeading": "ACTION SUBMITTALS",
  "divisionCode": "01",
  "divisionName": "General Requirements",
  "specNumber": "017419",
  "specName": "CONSTRUCTION WASTE MANAGEMENT AND DISPOSAL",
  "submittalDescription": "Waste Management Plan : Submit plan within 30 days of date established for the Notice to",
  "specCategory": "Waste Management Plan",
  "targetDate": null,
  "userNotes": null,
  "paraCode": "1.5-A",
  "targetGroup": "DIVISION 01 REQUIREMENTS",
  "versionName": "v3",
  "specSubmittalNumber": 0,
  "submittalId": "147"
 },
 {
  "submittalsHeading": "ACTION SUBMITTALS",
  "divisionCode": "01",
  "divisionName": "General Requirements",
  "specNumber": "017419",
  "specName": "CONSTRUCTION WASTE MANAGEMENT AND DISPOSAL",
  "submittalDescription": "Waste Management Plan : Submit plan within 30 days of date established for the Notice to",
  "specCategory": "Waste Management Plan",
  "targetDate": null,
  "userNotes": null,
  "paraCode": "1.5-A",
  "targetGroup": "DIVISION 01 REQUIREMENTS",
  "versionName": "v3",
  "specSubmittalNumber": 0,
  "submittalId": "123"
 }
]

```

Show More

Congratulations! You have retrieved a Smart Register.
