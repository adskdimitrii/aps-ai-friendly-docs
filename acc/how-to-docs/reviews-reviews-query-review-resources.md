# Inspect a Review

Source: https://aps.autodesk.com/en/docs/acc/tutorials/reviews/reviews-query-review-resources/

---

# Inspect a Review

This tutorial demonstrates how to inspect the details of a review by retrieving the file versions included in the review, the workflow snapshot that was captured when the review was created, and the current progress of the review.

By the end, you will understand how to check both the configuration and the status of a review without making changes to it.

The workflow snapshot may differ from the current definition of the approval workflow if the workflow was edited after the review was created. Progress results are returned in reverse chronological order and include only the current round of the review.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps), and select `Forma APIs` in the `API Access` dropdown.
- Acquire a [3-legged](../../oauth/how-to-docs/get-3-legged-token.md) or [2-legged](../../oauth/how-to-docs/get-2-legged-token.md) OAuth token with `data:read` scopes for querying.
  * For a 3-legged token, ensure that the user has permission to access the review and the files.
  * For a 2-legged token, the `x-user-id` header is required. Retrieve the user’s Autodesk ID by calling [GET projects/:projectId/users](../http-docs/http-admin-projectsprojectId-users-GET.md) with your 2-legged OAuth token and the user’s email address. Ensure that the user is a project administrator or a candidate of the review.
- Find the project ID for the project you want to work with by following the [Retrieve a Forma Hub ID and Project ID](getting-started-retrieve-account-and-project-id.md) tutorial. In this example, assume the project ID is `9ba6681e-1952-4d54-aac4-9de6d9858dd4`.
- Find the review ID by calling [GET reviews](../http-docs/http-reviews-reviews-GET.md). In this example, assume the review ID is `4e609369-e950-4097-b7d3-e6cf1c3c5415`.
- Verify that you have access to the relevant Forma hub, project, folders, and files.

## [Step 1: Get File Versions Included in the Review](#step-1-get-file-versions-included-in-the-review)

Use the project ID (`9ba6681e-1952-4d54-aac4-9de6d9858dd4`) and the review ID (`4e609369-e950-4097-b7d3-e6cf1c3c5415`), to call [GET reviews/versions](../http-docs/http-reviews-getreviewversions-GET.md) and retrieve the file versions that were included in the review.

### Request

```
curl 'https://developer.api.autodesk.com/construction/reviews/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/reviews/4e609369-e950-4097-b7d3-e6cf1c3c5415/versions?limit=10&offset=0' \
  -X GET \
  -H 'x-user-id: U5XCJQ22TL8G' \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -H 'Content-Type: application/json'

```

### Response

```
{
  "results": [
    {
      "name": "3rd Floor 3D Models.pdf",
      "urn": "urn:adsk.wipprod:fs.file:vf.Vl6kgO55TuWoHy9EbXAAaQ?version=1",
      "itemUrn": "urn:adsk.wipprod:dm.lineage:Vl6kgO55TuWoHy9EbXAAaQ",
      "approveStatus": null,
      "reviewContent": {
        "name": "3rd Floor 3D Models (shared).pdf",
        "customAttributes": [{
          "id": 10272,
          "type": "string",
          "name": "Reference Document Number",
          "value": "X-3910-3DWA"
        }]
      },
      "copiedFileVersionUrn": null
    }
  ],
  "pagination": {
    "limit": 10,
    "offset": 0,
    "totalResults": 1,
    "nextUrl": ""
  }
}

```

Show More

If the review files are approved or rejected, the `approveStatus` field is set in the response:

```
{
  "results": [
    {
      "name": "3rd Floor 3D Models.pdf",
      "urn": "urn:adsk.wipprod:fs.file:vf.Vl6kgO55TuWoHy9EbXAAaQ?version=1",
      "itemUrn": "urn:adsk.wipprod:dm.lineage:Vl6kgO55TuWoHy9EbXAAaQ",
      "approveStatus": {
        "id": "f44e623d-f04f-47fe-8195-efc43d1d985b",
        "label": "Approved",
        "value": "APPROVED"
      },
      "reviewContent": {
        "name": "3rd Floor 3D Models (shared).pdf",
        "customAttributes": [{
          "id": 10272,
          "type": "string",
          "name": "Reference Document Number",
          "value": "X-3910-3DWA"
        }]
      },
      "copiedFileVersionUrn": "urn:adsk.wipprod:fs.file:vf.JsWkC5LaR-6GGrx2GExVTg?version=1"
    },
    {
      "name": "4th Floor 3D Models.pdf",
      "urn": "urn:adsk.wipprod:fs.file:vf.oYonmqDTS8KXyZ2-tI38-g?version=1",
      "itemUrn": "urn:adsk.wipprod:dm.lineage:oYonmqDTS8KXyZ2-tI38-g",
      "approveStatus": {
        "id": "b2a3c3b7-4fef-40a4-868b-981b23e7182f",
        "label": "Rejected",
        "value": "REJECTED"
      },
      "reviewContent": {
        "name": "3rd Floor 3D Models (shared).pdf",
        "customAttributes": [{
          "id": 10272,
          "type": "string",
          "name": "Reference Document Number",
          "value": "X-4270-3DWB"
        }]
      },
      "copiedFileVersionUrn": null
    }
  ],
  "pagination": {
    "limit": 10,
    "offset": 0,
    "totalResults": 2,
    "nextUrl": ""
  }
}

```

Show More

In this example, the file `4th Floor 3D Models.pdf` has been rejected, so `copiedFileVersionUrn` is `null`, which means it was not copied.

The response shows the files that were included in the review, along with their URNs and current approval status.

## [Step 2: Get Workflow Snapshot for the Review](#step-2-get-workflow-snapshot-for-the-review)

Use the project ID (`9ba6681e-1952-4d54-aac4-9de6d9858dd4`) and the review ID (`4e609369-e950-4097-b7d3-e6cf1c3c5415`) to call [GET reviews/workflow](../http-docs/http-reviews-getreviewworkflow-GET.md) and retrieve the workflow snapshot that was captured when the review was created.

### Request

```
curl 'https://developer.api.autodesk.com/construction/reviews/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/reviews/4e609369-e950-4097-b7d3-e6cf1c3c5415/workflow' \
  -X GET \
  -H 'x-user-id: U5XCJQ22TL8G' \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -H 'Content-Type: application/json'

```

### Response

```
{
  "id": "3f8f0b2d-7b0b-4e4c-928a-87e42c1ff55a",
  "name": "Drawing Review Workflow",
  "steps": [
    {
      "id": "INITIATOR",
      "candidates": [
        {
          "autodeskId": "U5XCJQ22TL8G",
          "name": "Alex Johnson"
        }
      ]
    },
    {
      "id": "REVIEWER",
      "candidates": [
        {
          "autodeskId": "V6YCJR34AB2D",
          "name": "Maria Lee"
        }
      ]
    },
    {
      "id": "APPROVER",
      "candidates": [
        {
          "autodeskId": "W7ZDKE56CF3F",
          "name": "Chris Smith"
        }
      ]
    }
  ]
}

```

Show More

The response shows the workflow steps and candidates that were defined at the time the review was created.

Note that the content of this workflow may differ from what you get using [GET approval workflow](../http-docs/http-reviews-getworkflow-GET.md), because the workflow may have been updated after the review was created. The snapshot returned by this endpoint reflects the state of the workflow at the time of review creation and does not change with subsequent workflow updates.

## [Step 3: Get Progress of the Review](#step-3-get-progress-of-the-review)

Use the project ID (`9ba6681e-1952-4d54-aac4-9de6d9858dd4`) and the review ID (`4e609369-e950-4097-b7d3-e6cf1c3c5415`) to call [GET reviews/progress](../http-docs/http-reviews-getreviewprogress-GET.md) and retrieve the current progress of the review.

### Request

```
curl 'https://developer.api.autodesk.com/construction/reviews/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/reviews/4e609369-e950-4097-b7d3-e6cf1c3c5415/progress?limit=10&offset=0' \
  -X GET \
  -H 'x-user-id: U5XCJQ22TL8G' \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -H 'Content-Type: application/json'

```

### Response

```
{
  "results": [
    {
      "stepId": "REVIEWER",
      "stepName": "Reviewer",
      "claimedBy": {
        "autodeskId": "V6YCJR34AB2D",
        "name": "Maria Lee"
      },
      "actionBy": {
        "autodeskId": "V6YCJR34AB2D",
        "name": "Maria Lee"
      },
      "status": "SUBMITTED",
      "endTime": "2025-09-10T12:30:45Z",
      "notes": "Reviewed and approved.",
      "candidates": {
        "users": [
          {
            "autodeskId": "V6YCJR34AB2D",
            "name": "Maria Lee"
          }
        ]
      }
    }
  ],
  "pagination": {
    "limit": 10,
    "offset": 0,
    "totalResults": 1,
    "nextUrl": ""
  }
}

```

Show More

The response shows the progress of each step in the review’s approval workflow, including who claimed or submitted the step, when it was completed, and any notes recorded. Results are returned in reverse chronological order, and only data for the current round of the review is included.
