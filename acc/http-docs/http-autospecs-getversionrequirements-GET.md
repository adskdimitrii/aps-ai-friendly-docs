# projects/{projectId}/version/{versionId}/requirements

Source: https://aps.autodesk.com/en/docs/acc/reference/http/autospecs-getversionrequirements-GET/

---

requirements

GET

# projects/{projectId}/version/{versionId}/requirements

Retrieves the number of submittals for the submittal groups in each submittal section. To retrieve all submittal data from the Smart Register, call [GET smartregister](http-autospecs-getversionsmartregister-GET.md).

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/autospecs/v1/projects/{projectId}/version/{versionId}/requirements |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is obtained via a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](../how-to-docs/getting-started-retrieve-account-and-project-id.md). You need to convert the project ID into a project ID for the ACC API by removing the “b.” prefix. For example, a project ID of b.a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.
- versionIdstring The AutoSpecs version ID of the project. For information about how to find the version ID, see the first few steps of the [Retrieve Submittal Log](https://aps.autodesk.com/en/docs/acc/v1/tutorials/autospecs/upload-document/) tutorial.

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | OK |
| --- | --- |
| 401   Unauthorized | The provided bearer token is not valid. |
| 403   Forbidden | The user or service represented by the bearer token does not have permission to perform this operation. |
| 404   Not Found | The requested resource could not be found. |
| 500   Internal Server Error | An unknown error occurred on the server. |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| divisionCode   string | The division code associated with the submittal. This is the equivalent to the *Division* column in the UI. |
| --- | --- |
| divisionName   string | The division name associated with the submittal. This is equivalent to the name in the *Division* filter in the UI. |
| specSections   array: object | A list of specification divisions and groups. |
| specName   string | The CSI specification name of the submittal. This is equivalent of the *Section name* column in the UI. |
| specCode   string | The CSI specification code of the submittal. This is equivalent to the *Section number* column in the UI. |
| submittalGroups   array: object | A list of submittal groups. |
| submittalGroupTypes   array: object |  |
| submittalType   enum:string | The type of submittal. This corresponds to the *Submittal type* column in the UI. Possible values: `Test Reports`, `Shop Drawings`, `Schedules`, `Samples`, `Sample Warranty`, `Reports`, `Qualification Data`, `QUALITY ASSURANCE`, `Product Data`, `Performance Data`, `Mfg. Instructions`, `Meeting/Conferences`, `Drawings`, `Delegated-Design`, `Certifications`, `Certificates`, `Calculations`, `Attic Stock`, `Demonstrations`, `General Warranties`, `O&M Manuals`, `Special Warranties`, `LEED`, `As-Builts`, `TESTS AND INSPECTIONS`, `General`, `Manufacturers Instructions`, `Substitutions`, `Mix Design`, `Others` |
| total   int | The number of submittals for the submittal type. |
| submittalGroup   enum:string | The submittal group associcated with the submittal. This is equivalent to the *Submittal group* column in the UI. Possible values: `ACTION AND INFORMATIONAL`, `CLOSEOUT SUBMITTALS`, `DIVISION 01 REQUIREMENTS`, `FIELD QUALITY CONTROL`, `Mockups`, `QUALITY ASSURANCE`, `Tests And Inspections` |
| total   int | The number of submittals for the submittal group. |

## [Example](#example)

Successful retrieval of the number of submittals for the submittal groups in each submittal section

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/autospecs/v1/projects/:projectId/version/:versionId/requirements' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
[
  {
    "divisionCode": "01",
    "divisionName": "General Requirements",
    "specSections": [
      {
        "specName": "STRUCTURAL TESTS AND SPECIAL INSPECTIONS",
        "specCode": "01 45 33",
        "submittalGroups": [
          {
            "submittalGroup": "DIVISION 01 REQUIREMENTS",
            "total": 4
          }
        ]
      }
    ]
  },
  {
    "divisionCode": "03",
    "divisionName": "Concrete",
    "specSections": [
      {
        "specName": "CONCRETE REINFORCING",
        "specCode": "03 20 00",
        "submittalGroups": [
          {
            "submittalGroup": "ACTION AND INFORMATIONAL",
            "total": 5
          },
          {
            "submittalGroup": "QUALITY ASSURANCE",
            "total": 1
          },
          {
            "submittalGroup": "TESTS AND INSPECTIONS",
            "total": 1
          }
        ]
      }
    ]
  }
]

```

Show More
