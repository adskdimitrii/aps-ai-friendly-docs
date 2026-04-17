# projects/{projectId}/version/{versionId}/smartregister

Source: https://aps.autodesk.com/en/docs/acc/reference/http/autospecs-getversionsmartregister-GET/

---

smartregister

GET

# projects/{projectId}/version/{versionId}/smartregister

Retrieves the submittal logs (Smart Register) that are part of the specification PDFs that were imported into AutoSpecs.
Note that before you can access the submittal logs the import of the specification PDFs needs to be complete. To verify the status of the import, call [GET metadata](http-autospecs-getprojectmetadata-GET.md) and check that the `status` is `Completed`.

Note that we do not currently support updating the Smart Register or Smart Register filtering. In addition, we do not currently support the following columns from the UI: Source version, PDF link, Submittal type group, and Date Issued.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/autospecs/v1/projects/{projectId}/version/{versionId}/smartregister |
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

- projectIdstring The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/developers_guide/overview/) to retrieve the project ID. For more information, see the [Retrieve a Project ID tutorial](../how-to-docs/getting-started-retrieve-account-and-project-id.md). You need to convert the project ID into a project ID for the Forma API by removing the “b.” prefix. For example, a project ID of b.a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.
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

| submittalsHeading   string | The name of the submittal sub section. This is equivalent to *Sub section name* column in the UI. |
| --- | --- |
| divisionCode   string | The division code associated with the submittal. This is the equivalent to the *Division* column in the UI. |
| divisionName   string | The division name associated with the submittal. This is equivalent to the name in the *Division* filter in the UI. |
| submittalId   string | The index of the submittal in the submittal log. This is the equivalent to the *Submittal number* column in the UI. |
| specNumber   string | The CSI specification code of the submittal. This is equivalent to the *Section number* column in the UI. |
| specName   string | The CSI specification name of the submittal. This is equivalent of the *Section name* column in the UI. |
| submittalDescription   string | The description of the submittal. This is equivalent to the *Submittal description* column in the UI. |
| specCategory   enum:string | The type of specification category associated with the submittal. This is equivalent to *Submittal type* in the UI. Possible values: `Test Reports`, `Shop Drawings`, `Schedules`, `Samples`, `Sample Warranty`, `Reports`, `Qualification Data`, `QUALITY ASSURANCE`, `Product Data`, `Performance Data`, `Mfg. Instructions`, `Meeting/Conferences`, `Drawings`, `Delegated-Design`, `Certifications`, `Certificates`, `Calculations`, `Attic Stock`, `Demonstrations`, `General Warranties`, `O&M Manuals`, `Special Warranties`, `LEED`, `As-Builts`, `TESTS AND INSPECTIONS`, `General`, `Manufacturers Instructions`, `Substitutions`, `Mix Design`, `Others` |
| targetDate   string | The submittal target date, in ISO 8601 format. This is equivalent to the *Target date* column in the UI. |
| userNotes   string | The user notes associcated with the submittal. This is equivalent to the *User notes* column in the UI. |
| paraCode   string | The submittal sub section code. This is equivalent to the *Sub section number* column in the UI. |
| targetGroup   enum:string | The submittal group associcated with the submittal. This is equivalent to the *Submittal group* column in the UI. Possible values: `ACTION AND INFORMATIONAL`, `Closeout Submittals`, `DIVISION 01 REQUIREMENTS`, `Field Quality Control`, `Mockups`, `QUALITY ASSURANCE`, `TESTS AND INSPECTIONS` |
| versionName   string | The version name provided by the user when creating the version. |

## [Example](#example)

Successful retrieval of submittal logs

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/autospecs/v1/projects/:projectId/version/:versionId/smartregister' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
[
  {
    "submittalsHeading": "SHOP DRAWINGS",
    "divisionCode": "03",
    "divisionName": "Concrete",
    "specNumber": "03 20 00",
    "specName": "HEAD OFFICE RENEWAL",
    "submittalDescription": ".1 Submit shop drawings and bar lists in accordance with Section 01 33 00\nSubmittal Procedures. Allow ten working days for shop drawing review before\ncommencing fabrication.\n.2 Indicate on shop drawings, bar bending details, lists, quantities of\nreinforcement and wire mesh, sizes, spacing, locations of reinforcement and\nmechanical splices if approved by Consultant, with identifying code marks to\npermit correct placement without reference to structural drawings. Indicate\nsizes, spacing and locations of chairs, spacers and hangers. Prepare\nreinforcement drawings in accordance with Reinforcing Steel Manual of\nStandard Practice - by Reinforcing Steel Institute of Canada. ANSI/ACI 315\nand ACI 315R, Manual of Engineering and Placing Drawings for Reinforced\nConcrete Structure.\n.3 Indicate &#x28;and detail&#x29; all proposed construction joints.\n.4 Show reinforced concrete and reinforced masonry walls and beams in full\nelevation and detail all bars.\n.5 When requested, for slab construction, show top and bottom layer slab\nreinforcing on separate plans. Detail sections to fully illustrate bar placement\nat dowels, curbs, openings, changes of elevation, beams, stairs, and areas of\ncongested steel, and wherever else required.\n.6 Detail placement of reinforcing where special conditions occur.\n.7 Design and detail lap lengths and bar development lengths to CAN/CSA-A23.1\nand CAN3-A23.3, unless otherwise specified on drawings. Use Class B\ntension splices unless otherwise noted.\n.8 Indicate details for placement of dowels.\n.9 CAD drawings of the Consultant may be used asa background for the\npreparation of shop drawings provided thata license agreement, provided by\nthe Consultant, is signed by the reinforcing trade.",
    "specCategory": "Shop Drawings",
    "targetDate": null,
    "userNotes": null,
    "paraCode": "1.4",
    "targetGroup": "ACTION AND INFORMATIONAL",
    "versionName": "Issued For Construction",
    "specSubmittalNumber": 0,
    "submittalId": "1"
  },
  {
    "submittalsHeading": "SOURCE QUALITY CONTROL",
    "divisionCode": "03",
    "divisionName": "Concrete",
    "specNumber": "03 20 00",
    "specName": "HEAD OFFICE RENEWAL",
    "submittalDescription": "Upon request, provide Consultant with certified copy of mill test report of\nreinforcing steel to be supplied, showing physical and chemical analysis,\ncorresponding to identification tagging of material at the fabrication plant\nprior to commencing reinforcing work.",
    "specCategory": "Test Reports",
    "targetDate": null,
    "userNotes": null,
    "paraCode": "2.3-.1",
    "targetGroup": "QUALITY ASSURANCE",
    "versionName": "Issued For Construction",
    "specSubmittalNumber": 0,
    "submittalId": "2"
  },
  {
    "submittalsHeading": "SOURCE QUALITY CONTROL",
    "divisionCode": "03",
    "divisionName": "Concrete",
    "specNumber": "03 20 00",
    "specName": "HEAD OFFICE RENEWAL",
    "submittalDescription": "Inform Consultant of proposed source of material to be supplied. Unidentified\nreinforcement shall not be allowed.",
    "specCategory": "Quality Assurance",
    "targetDate": null,
    "userNotes": null,
    "paraCode": "2.3-.2",
    "targetGroup": "QUALITY ASSURANCE",
    "versionName": "Issued For Construction",
    "specSubmittalNumber": 0,
    "submittalId": "3"
  }
]

```

Show More
