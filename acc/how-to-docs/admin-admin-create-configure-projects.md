# Create and Configure Projects

Source: https://aps.autodesk.com/en/docs/acc/tutorials/admin/admin-create-configure-projects/

---

# Create and Configure Projects

This tutorial demonstrates how to create and configure an ACC project. The steps include creating the project, checking the product activation status, assigning members to the project, and retrieving information about the project and its members.

For more information about projects, project templates, and project members, see the [Account Administration API Field Guide](/en/docs/acc/v1/overview/field-guide/admin/).

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps).
-

Acquire a [3-legged](/en/docs/oauth/v2/tutorials/get-3-legged-token/) or [2-legged](/en/docs/oauth/v2/tutorials/get-2-legged-token/) Oauth token with `data:read`, `data:write`, `account:read`, and `account:write` scopes.
:   * For a 3-legged token, ensure that the user is an account administrator (or a project administrator if **Allow project administrators to create projects and project templates** is enabled in Account Settings).
      * For a 2-legged token, the `User-Id` header is required to process the Account Admin endpoints. Retrieve the user ID by calling [GET users/search](/en/docs/acc/v1/reference/http/users-search-GET/) with your 2-legged OAuth token and the userâs email address. Ensure that the user is an account administrator (or a project administrator if **Allow project administrators to create projects and project templates** is enabled in Account Settings).

- Verify that you have access to the relevant account.
- Find the relevant account ID for the account you want to create a project in by following the [Retrieve an Account ID and Project ID](/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. In this example, assume the account ID is `g5s4e3b5-vbta-6b02-d23a-5d55f36ba876`.

## [Step 1: Create a Project](#step-1-create-a-project)

You can create a project in two ways:

- Option 1A â Clone the project from a project template. This assumes an appropriate project template has been created and configured. We strongly recommend this if you expect to implement multiple similar projects.
- Option 1B â Create the project directly. This option works well for a one-off project when you donât have a project template.

Note that you can use [POST projects](/en/docs/acc/v1/reference/http/admin-accountsaccountidprojects-POST/) to create a project template, then use the ACC Build UI to edit the template details and permissions, add project members to the template, and configure the templateâs notification settings. For more information about working with project templates, see [Project Administration > Project Templates](https://help.autodesk.com/view/BUILD/ENU/?guid=Templates_About) and [Account Administration > Project Templates](https://help.autodesk.com/view/BUILD/ENU/?guid=Account_Admin_Project_Templates) in Build Help.

### Option 1A: Clone the project from a project template

To create the project from a template, include `template.projectId` in the request to specify an existing project template from which to copy products and settings for the new project.

Note that you can obtain the project ID of a suitable project template by calling [GET projects](/en/docs/acc/v1/reference/http/admin-accountsaccountidprojects-GET/) with `filter[classification] == template`, inspecting the returned templates, and noting the `id` value of the template you want to use.

#### Request

```
curl -X 'POST' 'https://developer.api.autodesk.com/construction/admin/v1/accounts/g5s4e3b5-vbta-6b02-d23a-5d55f36ba876/projects'
\ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
\ -H 'Content-Type: application/json'
\ -d '{
        "name": "Project 1",
        "classification": "production",
        "startDate": "2010-01-01",
        "endDate": "2015-12-31",
        "type": "Hospital",
        "projectValue": {
            "value": 1650000,
            "currency": "USD"
        },
        "jobNumber": "HP-0002",
        "addressLine1": "123 Main Street",
        "addressLine2": "Suite 2",
        "city": "San Francisco",
        "stateOrProvince": "California",
        "postalCode": "94001",
        "country": "United States",
        "latitude": "37.773972",
        "longitude": "-122.431297",
        "timezone": "America/Los_Angeles",
        "constructionType": "New Construction",
        "deliveryMethod": "Unit Price",
        "currentPhase": "Design",
        "businessUnitId": "802a4a61-3507-4d4e-8e3c-242a31cc0549",
        "template": {
            âprojectIdâ: âljsdfdlskfjsâ
        }
    }'

```

Show More

#### Response

```
{
    "id": "3e354e66-ac8b-41dd-9bc1-93fc182c25dd",
    "name": "Project 1",
    "startDate": "2010-01-01",
    "endDate": "2015-12-31",
    "type": "Hospital",
    "classification": "production",
    "projectValue": {
        "value": 1650000,
        "currency": "USD"
    },
    "status": "active",
    "jobNumber": "HP-0002",
    "addressLine1": "123 Main Street",
    "addressLine2": "Suite 2",
    "city": "San Francisco",
    "stateOrProvince": "California",
    "postalCode": "94001",
    "country": "United States",
    "latitude": "37.773972",
    "longitude": "-122.431297",
    "timezone": "America/Los_Angeles",
    "constructionType": "New Construction",
    "deliveryMethod": "Design-Bid",
    "contractType": "Unit Price",
    "currentPhase": "Design",
    "businessUnitId": "802a4a61-3507-4d4e-8e3c-242a31cc0549",
    "lastSignIn": "2019-01-01T12:45:00.000Z",
    "imageUrl": "https://s3.us-east-1.amazonaws.com/project_image.png",
    "thumbnailImageUrl": "https://s3.us-east-1.amazonaws.com/project_thumbnail_image.png",
    "createdAt": "2018-01-01T12:45:00.000Z",
    "updatedAt": "2019-01-01T12:45:00.000Z",
    "memberGroupId": "3456542",
    "adminGroupId": "3456543",
    "accountId": "d73fc742-4538-401c-8d0f-853b49b750b2",
    "sheetCount": 512,
    "products": [
        {
            "key": "docs",
            "name": "Document Management",
            "status": "activating",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/docs.svg"
        },
        {
            "key": "insight",
            "name": "Insight",
            "status": "active",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/insight.svg"
        },
        {
            "key": "projectAdministration",
            "name": "Project Admin",
            "status": "active",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/tools/settings.svg"
        }
    ],
    "platform": "acc",
    "companyCount": 10,
    "memberCount": 100,
    "jobId": "5d3bc131-c0dc-4222-9a2a-351363f437fa"
}

```

Show More

Find and note the project ID (`id`) - `3e354e66-ac8b-41dd-9bc1-93fc182c25dd`.

Note that this operation does not automatically assign the template project members to the cloned project. You will do this in a later step. Continue to check the projectâs activation status (Step 2).

### Option 1B: Create the project directly

To create the project, call [POST projects](/en/docs/acc/v1/reference/http/admin-accountsaccountidprojects-POST/). This endpoint automatically adds to the project all of the products (and their settings) that are associated with the current ACC account.

#### Request

```
curl -X 'POST' 'https://developer.api.autodesk.com/construction/admin/v1/accounts/g5s4e3b5-vbta-6b02-d23a-5d55f36ba876/projects'
\ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
\ -H 'Content-Type: application/json'
\ -d '{
        "name": "Project 1",
        "classification": "production",
        "startDate": "2010-01-01",
        "endDate": "2015-12-31",
        "type": "Hospital",
        "projectValue": {
            "value": 1650000,
            "currency": "USD"
        },
        "jobNumber": "HP-0002",
        "addressLine1": "123 Main Street",
        "addressLine2": "Suite 2",
        "city": "San Francisco",
        "stateOrProvince": "California",
        "postalCode": "94001",
        "country": "United States",
        "latitude": "37.773972",
        "longitude": "-122.431297",
        "timezone": "America/Los_Angeles",
        "constructionType": "New Construction",
        "deliveryMethod": "Unit Price",
        "currentPhase": "Design",
        "businessUnitId": "802a4a61-3507-4d4e-8e3c-242a31cc0549",
    }'

```

Show More

#### Response

```
{
    "id": "3e354e66-ac8b-41dd-9bc1-93fc182c25dd",
    "name": "Project 1",
    "startDate": "2010-01-01",
    "endDate": "2015-12-31",
    "type": "Hospital",
    "classification": "production",
    "projectValue": {
        "value": 1650000,
        "currency": "USD"
    },
    "status": "pending",
    "jobNumber": "HP-0002",
    "addressLine1": "123 Main Street",
    "addressLine2": "Suite 2",
    "city": "San Francisco",
    "stateOrProvince": "California",
    "postalCode": "94001",
    "country": "United States",
    "latitude": "37.773972",
    "longitude": "-122.431297",
    "timezone": "America/Los_Angeles",
    "constructionType": "New Construction",
    "deliveryMethod": "Design-Bid",
    "contractType": "Unit Price",
    "currentPhase": "Design",
    "businessUnitId": "802a4a61-3507-4d4e-8e3c-242a31cc0549",
    "lastSignIn": "2019-01-01T12:45:00.000Z",
    "imageUrl": "https://s3.us-east-1.amazonaws.com/project_image.png",
    "thumbnailImageUrl": "https://s3.us-east-1.amazonaws.com/project_thumbnail_image.png",
    "createdAt": "2018-01-01T12:45:00.000Z",
    "updatedAt": "2019-01-01T12:45:00.000Z",
    "memberGroupId": "3456542",
    "adminGroupId": "3456543",
    "accountId": "d73fc742-4538-401c-8d0f-853b49b750b2",
    "sheetCount": 512,
    "products": [
        {
            "key": "docs",
            "name": "Docs",
            "status": "activating",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/docs.svg"
        },
        {
            "key": "insight",
            "name": "Insight",
            "status": "active",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/insight.svg"
        },
        {
            "key": "projectAdministration",
            "name": "Project Admin",
            "status": "active",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/tools/settings.svg"
        },
        {
            "key": "designCollaboration",
            "name": "Design Collaboration",
            "status": "active",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/dc.svg"
        },
        {
            "key": "modelCoordination",
            "name": "Model Coordination",
            "status": "active",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/model.svg"
        },
        {
            "key": "takeoff",
            "name": "Takeoff",
            "status": "active",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/quantify.svg"
        },
        {
            "key": "autoSpecs",
            "name": "AutoSpecs",
            "status": "active",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/tools/autospecs.svg"
        },
        {
            "key": "build",
            "name": "Build",
            "status": "active",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/build.svg"
        },
        {
            "key": "cost",
            "name": "Cost Management",
            "status": "active",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/cost.svg"
        },
        {
            "key": "accountAdministration",
            "name": "Account Admin",
            "status": "active",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/tools/settings.svg"
        },
        {
            "key": "financials",
            "name": "Project Financials",
            "status": "active",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/service_icons/cost-icon-1dcf6b647e1d4a4effe28ce9dc77063e.svg"
        },
        {
            "key": "capitalPlanning",
            "name": "Capital Planning",
            "status": "active",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/service_icons/cost-icon-1dcf6b647e1d4a4effe28ce9dc77063e.svg"
        },
        {
            "key": "buildingConnected",
            "name": "BuildingConnected",
            "status": "active",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/buildingconnected.svg"
        }
    ],
    "platform": "acc",
    "companyCount": 10,
    "memberCount": 100,
    "jobId": "5d3bc131-c0dc-4222-9a2a-351363f437fa"
}

```

Show More

Find and note the project ID (`id`) - `3e354e66-ac8b-41dd-9bc1-93fc182c25dd`. Once the project is created, the Account Admin service launches an asynchronous job to activate all of the added products.

Note that currently, you cannot use `jobId` to check the progress of product activation in your project.

## [Step 2: Check Project Activation Status by Polling](#step-2-check-project-activation-status-by-polling)

Before you can continue configuring your new project, it must be active. The activation process occurs automatically, but doesnât finish immediately. Call [GET projects/:projectId](/en/docs/acc/v1/reference/http/admin-projects-projectId-GET/) to check its activation status. The activation process is complete when the value of the project-level `status` field in the response is `active`.

### Request

```
curl -X 'GET' 'https://developer.api.autodesk.com/construction/admin/v1/projects/3e354e66-ac8b-41dd-9bc1-93fc182c25dd'
\ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
    "id": "3e354e66-ac8b-41dd-9bc1-93fc182c25dd",
    "name": "Project 1",
    "startDate": "2010-01-01",
    "endDate": "2015-12-31",
    "type": "Hospital",
    "classification": "production",
    "projectValue": {
        "value": 1650000,
        "currency": "USD"
    },
    "status": "active",
    "jobNumber": "HP-0002",
    "addressLine1": "123 Main Street",
    "addressLine2": "Suite 2",
    "city": "San Francisco",
    "stateOrProvince": "California",
    "postalCode": "94001",
    "country": "United States",
    "latitude": "37.773972",
    "longitude": "-122.431297",
    "timezone": "America/Los_Angeles",
    "constructionType": "New Construction",
    "deliveryMethod": "Design-Bid",
    "contractType": "Unit Price",
    "currentPhase": "Design",
    "businessUnitId": "802a4a61-3507-4d4e-8e3c-242a31cc0549",
    "lastSignIn": "2019-01-01T12:45:00.000Z",
    "imageUrl": "https://s3.us-east-1.amazonaws.com/project_image.png",
    "thumbnailImageUrl": "https://s3.us-east-1.amazonaws.com/project_thumbnail_image.png",
    "createdAt": "2018-01-01T12:45:00.000Z",
    "updatedAt": "2019-01-01T12:45:00.000Z",
    "memberGroupId": "3456542",
    "adminGroupId": "3456543",
    "accountId": "d73fc742-4538-401c-8d0f-853b49b750b2",
    "sheetCount": 512,
    "products": [
        {
            "key": "docs",
            "status": "activating",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/docs.svg",
            "name": "Document Management"
        },
        {
            "key": "insight",
            "status": "active",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/products/insight.svg",
            "name": "Insight"
        },
        {
            "key": "projectAdministration",
            "name": "Project Admin",
            "status": "active",
            "icon": "https://bim360-ea-ue1-prod-storage.s3.amazonaws.com/tools/settings.svg"
        }
    ],
    "platform": "acc",
    "companyCount": 10,
    "memberCount": 100,
    "jobId": "5d3bc131-c0dc-4222-9a2a-351363f437fa"
}

```

Show More

Find the project-level `status` field in the response, and note its value. Keep polling the project until the status is `active`.

Note that you can also use [GET projects/:projectId](/en/docs/acc/v1/reference/http/admin-projects-projectId-GET/) to check the activation status of its products for troubleshooting.

It is strongly recommended that you assign at least a project administrator to your project (Step 3) before doing anything else.

## [Step 3: Assign Members to Your Project](#step-3-assign-members-to-your-project)

How you assign project members depends on how you created your project:

- Option 3A â You just cloned your project from a template. Import the template project members in bulk from the template.
- Option 3B â You created your project directly. Assign one or more project members directly.

### Option 3A: Import template project members (if applicable)

If you just cloned your project from a template, call [POST users](/en/docs/acc/v1/reference/http/admin-projects-projectId-users-POST/) to assign a project administrator to the project, which triggers the assignment of all template project members to the project.

The administrator can be any user who is currently in the same account as the project. Include the products object in the request, with `products.key` set to `projectAdministration`, and `products.access` set to `administrator`.

Note that the template *configuration* members are never automatically assigned to a cloned project.

#### Request

```
curl -X 'POST' 'https://developer.api.autodesk.com/construction/admin/v1/projects/3e354e66-ac8b-41dd-9bc1-93fc182c25dd/users'
\ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
\ -H 'Content-Type: application/json'
\ -d '{
        "email": "sampleUser1@autodesk.com",
        "companyId": "c32ffb13-83f8-43fb-bddf-3e5c0c2dda24",
        "roleIds": [
            "287d5cc2-9008-462c-96e5-c9491db85d97",
            "cda845af-05f0-4c46-9108-71b993946c35",
            "b8e84a73-7506-4d3f-b221-93691df2a359"
        ],
        "products": [
            {
                "key": "projectAdministration",
                "access": "administrator"
            }
        ]
    }'

```

Show More

#### Response

```
{
    "email": "bob.smith@somewhere.com",
    "id": "39712a51-bd64-446a-9c72-48c4e43d0a0d",
    "name": "Bob Smith",
    "firstName": "Bob",
    "lastName": "Smith",
    "autodeskId": "USER123A",
    "analyticsId": "SOMEID123",
    "addressLine1": "123 Main Street",
    "addressLine2": "Suite 2",
    "city": "San Francisco",
    "stateOrProvince": "California",
    "postalCode": "94001",
    "country": "United States",
    "imageUrl": "https://s3.amazonaws.com:443/com.autodesk.storage.public.dev/oxygen/USER123A/profilepictures/x20.jpg",
    "phone": {
        "number": "123-345-1234",
        "phoneType": "mobile",
        "extension": "10"
    },
    "jobTitle": "Owner",
    "industry": "Architecture & Construction Service Providers",
    "aboutMe": "Bob has been in construction for 25 years",
    "accessLevels": {
        "accountAdmin": true,
        "projectAdmin": true,
        "executive": true
    },
    "addedOn": "2018-01-01T12:45:00.000Z",
    "updatedAt": "2018-01-01T12:45:00.000Z",
    "companyId": "c32ffb13-83f8-43fb-bddf-3e5c0c2dda24",
    "companyName": "Sample Company",
    "roleIds": [
        "287d5cc2-9008-462c-96e5-c9491db85d97",
        "cda845af-05f0-4c46-9108-71b993946c35",
        "b8e84a73-7506-4d3f-b221-93691df2a359"
    ],
    "roles": [
        {
            "id": "cda845af-05f0-4c46-9108-71b993946c35",
            "name": "Architect"
        },
        {
            "id": "b8e84a73-7506-4d3f-b221-93691df2a359",
            "name": "Engineer"
        }
    ],
    "status": "active",
    "products": [
        {
            "key": "docs",
            "access": "administrator"
        },
        {
            "key": "insight",
            "access": "administrator"
        },
        {
            "key": "projectAdministration ",
            "access": "administrator"
        }
    ],
    "jobId": "5d3bc131-c0dc-4222-9a2a-351363f437fa"
}

```

Show More

Note that you identify the user by `email` in the request, and the response contains the userâs new project `id`.

Note that if you assign a project administrator who isnât in the cloned projectâs account, the template project members are not automatically assigned to the new project. In that case, you can assign the same members (as well as additional users from the same account) directly to the project (Option 3B).

### Option 3B: Assign one or more project members directly

You can assign project members directly to a cloned or production project:

- If Option 3A was unsuccessful for a cloned project
- As the first step after creating a production project
- To ensure that the project has at least one project administrator
- At any time during the projectâs lifespan

Call [POST projects/:projectId/users:import](en/docs/acc/v1/reference/http/admin-projects-projectId-users-import-POST/) to assign one or more users to the project at a time. Include at least one project administrator if you havenât done so already.

The administrator can be any user who is currently in the same account as the project. Include the products object in the request, with `products.key` set to `projectAdministration`, and `products.access` set to `administrator`.

#### Request

```
curl -X 'POST' 'https://developer.api.autodesk.com/construction/admin/v2/projects/3e354e66-ac8b-41dd-9bc1-93fc182c25dd/users:import'
\ -H 'Authorization: Bearer Auth IPTf4KYLTYGVnOHQ0cuolwCW2a'
\ -H 'Content-Type: application/json'
\ -d '[{
        "email": "sampleUser1@autodesk.com",
        "companyId": "c32ffb13-83f8-43fb-bddf-3e5c0c2dda24",
        "roleIds": [
            "287d5cc2-9008-462c-96e5-c9491db85d97",
            "cda845af-05f0-4c46-9108-71b993946c35",
            "b8e84a73-7506-4d3f-b221-93691df2a359"
        ],
        "products": [
            {
                "key": "takeoff",
                "access": "administrator"
            },
            {
                "key": "projectAdministration ",
                "access": "administrator"
            }
        ]
    },
    {
        "email": "sampleUser2@autodesk.com",
        "companyId": "c32ffb13-83f8-43fb-bddf-3e5c0c2dda24",
        "roleIds": [
            "287d5cc2-9008-462c-96e5-c9491db85d97",
            "cda845af-05f0-4c46-9108-71b993946c35",
            "b8e84a73-7506-4d3f-b221-93691df2a359"
        ],
        "products": [
            {
                "key": "takeoff",
                "access": "member"
            },
            {
                "key": "projectAdministration ",
                "access": "none"
            }
        ]
    }
]'

```

Show More

#### Response

```
{
    "jobId": "5d3bc131-c0dc-4222-9a2a-351363f437fa"
}

```

Note that currently, [POST users:import](/en/docs/acc/v1/reference/http/admin-projects-projectId-users-import-POST/) does not return information about the newly assigned project members.

## [Step 4: Retrieve Information About the Project Members](#step-4-retrieve-information-about-the-project-members)

Note that project members cannot start work on the project until they have been activated to participate in the project.

Use [GET users](/en/docs/acc/v1/reference/http/admin-projects-projectId-users-GET//) to retrieve all users in the project. There are two primary reasons to do this:

- To verify that all users assigned to the project have been activated as members of the project.
- To check other information about members, such as their project user ID, roles, and products.

### Request

```
curl -X 'GET' 'https://developer.api.autodesk.com/construction/admin/v1/projects/3e354e66-ac8b-41dd-9bc1-93fc182c25dd/users
\ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
    "pagination": {
        "limit": 20,
        "offset": 10,
        "totalResults": 121,
        "nextUrl": "https://resource?limit=20&offset=30",
        "previousUrl": "https://resource?limit=20&offset=0"
    },
    "results": [
        {
            "email": "bob.smith@somewhere.com",
            "id": "39712a51-bd64-446a-9c72-48c4e43d0a0d",
            "name": "Bob Smith",
            "firstName": "Bob",
            "lastName": "Smith",
            "autodeskId": "USER123A",
            "analyticsId": "SOMEID123",
            "addressLine1": "123 Main Street",
            "addressLine2": "Suite 2",
            "city": "San Francisco",
            "stateOrProvince": "California",
            "postalCode": "94001",
            "country": "United States",
            "imageUrl": "https://s3.amazonaws.com:443/com.autodesk.storage.public.dev/oxygen/USER123A/profilepictures/x20.jpg",
            "phone": {
                "number": "123-345-1234",
                "phoneType": "mobile",
                "extension": "10"
            },
            "jobTitle": "Owner",
            "industry": "Architecture & Construction Service Providers",
            "aboutMe": "Bob has been in construction for 25 years.",
            "accessLevels": {
                "accountAdmin": true,
                "projectAdmin": true,
                "executive": true
            },
            "addedOn": "2018-01-01T12:45:00.000Z",
            "updatedAt": "2018-01-01T12:45:00.000Z",
            "companyId": "c32ffb13-83f8-43fb-bddf-3e5c0c2dda24",
            "companyName": "Sample Company",
            "roleIds": [
                "cda845af-05f0-4c46-9108-71b993946c35",
                "b8e84a73-7506-4d3f-b221-93691df2a359"
            ],
            "roles": [
                {
                    "id": "cda845af-05f0-4c46-9108-71b993946c35",
                    "name": "Architect"
                },
                {
                    "id": "b8e84a73-7506-4d3f-b221-93691df2a359",
                    "name": "Engineer"
                }
            ],
            "status": "active",
            "products": [
                {
                    "key": "takeoff",
                    "access": "member"
                },
                {
                    "key": "docs",
                    "access": "member"
                },
                {
                    "key": "insight",
                    "access": "member"
                },
                {
                    "key": "projectAdministration",
                    "access": "none"
                }
            ]
        }
    ]
}

```

Show More

Find the userâs project status (`results.status`) and verify thet its value is `active`.

## [(Optional) Step 5: Configure Project Member Access to Products](#optional-step-5-configure-project-member-access-to-products)

If circumstances produce a change in the access to a product (e.g. build, takeoff, or docs) that a project member requires, call [PATCH users/:userId](/en/docs/acc/v1/reference/http/admin-projects-projectId-users-userId-PATCH/) to update the project memberâs access. This example adds two new role IDs along with member access to the Takeoff product for the specified project member.

### Request

```
curl -X 'PATCH' 'https://developer.api.autodesk.com/construction/admin/v1/projects/3e354e66-ac8b-41dd-9bc1-93fc182c25dd/users/39712a51-bd64-446a-9c72-48c4e43d0a0d'
\ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
\ -H 'Content-Type: application/json'
\ -d '{
        "email": "bob.smith@somewhere.com",
        "companyId": "c32ffb13-83f8-43fb-bddf-3e5c0c2dda24",
        "roleIds": [
            "cda845af-05f0-4c46-9108-71b993946c35",
            "b8e84a73-7506-4d3f-b221-93691df2a359"
        ],
        "products": [
            {
                "key": "takeoff",
                "access": "member"
            }
        ]
    }'

```

Show More

### Response

```
{
    "id": "39712a51-bd64-446a-9c72-48c4e43d0a0d",
    "companyId": "c32ffb13-83f8-43fb-bddf-3e5c0c2dda24",
    "roleIds": [
        "287d5cc2-9008-462c-96e5-c9491db85d97",
        "cda845af-05f0-4c46-9108-71b993946c35",
        "b8e84a73-7506-4d3f-b221-93691df2a359"
    ],
    "products": [
        {
            "key": "docs",
            "access": "member"
        },
        {
            "key": "insight",
            "access": "member"
        },
        {
            "key": "projectAdministration",
            "access": "none"
        },
        {
            "key": "takeoff",
            "access": "member"
        }
    ]
}

```

Show More
