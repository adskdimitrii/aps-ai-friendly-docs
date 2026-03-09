# Create a Review

Source: https://aps.autodesk.com/en/docs/acc/tutorials/reviews/reviews-create-review/

---

# Create a Review

This tutorial demonstrates how to create a review in a project. The steps include preparing the review details, creating the review, confirming the review, and optionally using webhooks to monitor creation status.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps), and select `Autodesk Construction Cloud APIs` in the `API Access` dropdown.
- Acquire a [3-legged](../../oauth/how-to-docs/get-3-legged-token.md) or [2-legged](../../oauth/how-to-docs/get-2-legged-token.md) OAuth token with `data:read` and `data:write` scopes.
  * For a 3-legged token, ensure that the user has permission to access the project and files.
  * For a 2-legged token, the `x-user-id` header is required. Retrieve the userâs Autodesk ID by calling [GET projects/:projectId/users](../http-docs/http-admin-projectsprojectId-users-GET.md) with your 2-legged OAuth token and the userâs email address. Ensure that the user is a project administrator or a candidate in the workflow.
- Find the project ID for the project you want to work with by following the [Retrieve an Account ID and Project ID](getting-started-retrieve-account-and-project-id.md) tutorial. In this example, assume the project ID is `9ba6681e-1952-4d54-aac4-9de6d9858dd4`.
- Find the workflow ID for the approval workflow you want to use by calling [GET workflows](../http-docs/http-reviews-workflows-GET.md). In this example, assume the workflow ID is `a4e60936-e950-4097-b7d3-e6cf1c3c5415`.
- Obtain the URNs of the file versions that you want to include in the review. To find file version URNs, follow the first four steps of the [Download a File](files-download-document-s3.md) tutorial.
- Verify that you have access to the relevant ACC account, project, folders, and files.

## [Step 1 (optional): Gather Required IDs and URNs](#step-1-optional-gather-required-ids-and-urns)

Use the project ID (`9ba6681e-1952-4d54-aac4-9de6d9858dd4`) to call [GET workflows](../http-docs/http-reviews-workflows-GET.md) and retrieve available approval workflows (including their steps). Choose a workflow, note its `id` and the Reviewer step `id`, then gather the file version URNs you want to include (and optionally a target folder URN).

### Request

```
curl 'https://developer.api.autodesk.com/construction/reviews/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/workflows?limit=10&offset=0' \
  -X GET \
  -H 'x-user-id: U5XCJQ22TL8G' \
  -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
  -H 'Content-Type: application/json'

```

### Response

```
{
  "results": [
    {
      "id": "4e609369-e950-4097-b7d3-e6cf1c3c5415",
      "name": "Drawing Review Workflow",
      "steps": [
        { "id": "INITIATOR", "name": "Initiator" },
        { "id": "Lane_3ReoxO2T0o", "name": "Reviewer" },
        { "id": "APPROVER", "name": "Approver" }
      ],
      "additionalOptions": { "allowInitiatorToEdit": true },
      "copyFilesOptions": { "enabled": true, "allowOverride": true }
    }
  ],
  "pagination": { "limit": 10, "offset": 0, "totalResults": 1, "nextUrl": "" }
}

```

Show More

### Notes

- **Reviewer step ID** â Use the Reviewer step `id` (e.g., `Lane_3ReoxO2T0o`) if you plan to override candidates in your request (`workflowOptions.steps[].id`).
- **File version URNs** â To find file version URNs, follow the first four steps of the [Download a File](files-download-document-s3.md) tutorial and note the `included.id` values.
- **Target folder URN (optional)** â If you plan to set `workflowOptions.copyFilesOptions.folderUrn`, ensure the workflow allows it (`copyFilesOptions.enabled = true` and `copyFilesOptions.allowOverride = true`). You can locate a folder URN using the [Upload Files to the ACC Files tool](files-upload-document-s3.md) tutorial and note the `data.id`.
- To override reviewer candidates, the workflow must allow it: `additionalOptions.allowInitiatorToEdit = true`.

## [Step 2: Create a Review](#step-2-create-a-review)

Use the project ID (`9ba6681e-1952-4d54-aac4-9de6d9858dd4`) to call [POST reviews](../http-docs/http-reviews-createreview-POST.md) with the request payload you prepared in Step 1. This creates a new review instance in the project.

### Request

```
curl 'https://developer.api.autodesk.com/construction/reviews/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/reviews' \
  -X POST \
  -H 'x-user-id: HWUBNU689CRU' \
  -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "The 2nd Floor Design Review",
    "workflowId": "4e609369-e950-4097-b7d3-e6cf1c3c5415",
    "notes": "For the No. 3 Building on the 2nd floor, please review the design and provide feedback.",
    "fileVersions": [
      { "urn": "urn:adsk.wipprod:fs.file:vf.hC6k4hndRWaeIVhIjvHu8w?version=1" },
      { "urn": "urn:adsk.wipprod:fs.file:vf.7vIu5GjLQeaGBMW99tntyg?version=2" }
    ],
    "workflowOptions": {
      "copyFilesOptions": {
        "folderUrn": "urn:adsk.wipprod:fs.folder:co.CplBAmvXRWGqsvN1Nabvd2"
      },
      "steps": [
        {
          "id": "Lane_3ReoxO2T0o",
          "candidates": {
            "users":     [ { "autodeskId": "83QFRYJA3LRX" } ],
            "roles":     [ { "autodeskId": "1473817" } ],
            "companies": [ { "autodeskId": "26980302" } ]
          }
        }
      ]
    }
  }'

```

Show More

### Response

```
{
  "id": "c7fc352d-c33d-4e4b-9472-3dfd054be1f7",
  "name": "The 2nd Floor Design Review",
  "status": "OPEN",
  "sequenceId": 9,
  "currentStepId": "Lane_3ReoxO2T0o",
  "currentStepDueDate": "2025-06-21T21:14:14.027Z",
  "createdBy": {
    "autodeskId": "HWUBNU689CRU",
    "name": "James Smith"
  },
  "createdAt": "2025-06-18T21:14:14.672Z",
  "updatedAt": "2025-06-18T21:14:14.672Z",
  "finishedAt": null,
  "archived": false,
  "workflowId": "4e609369-e950-4097-b7d3-e6cf1c3c5415",
  "nextActionBy": {
    "claimedBy": [],
    "candidates": {
      "companies": [ { "autodeskId": "26980302", "name": "Autodesk Co. Ltd." } ],
      "roles":     [ { "autodeskId": "1473817", "name": "Architect" } ],
      "users":     [ { "autodeskId": "83QFRYJA3LRX", "name": "Bob Smith" } ]
    }
  }
}

```

Show More

### Notes

- When a review is created, its `status` is `OPEN` and the `currentStepId` is the first Reviewer step ID, or the Approver step ID if no Reviewer step exists.
- To query the note created during review creation, call [GET reviews/progress](../http-docs/http-reviews-getreviewprogress-GET.md).

## [Step 3: Confirm the Review](#step-3-confirm-the-review)

After creating a review, confirm that it was created successfully by calling [GET reviews/:reviewId](../http-docs/http-reviews-getreview-GET.md) with the review ID returned in Step 2. This retrieves the full details of the new review.

### Request

```
curl 'https://developer.api.autodesk.com/construction/reviews/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/reviews/c7fc352d-c33d-4e4b-9472-3dfd054be1f7' \
  -X GET \
  -H 'x-user-id: HWUBNU689CRU' \
  -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
  -H 'Content-Type: application/json'

```

### Response

```
{
  "id": "c7fc352d-c33d-4e4b-9472-3dfd054be1f7",
  "name": "The 2nd Floor Design Review",
  "status": "OPEN",
  "sequenceId": 9,
  "currentStepId": "Lane_3ReoxO2T0o",
  "createdBy": {
    "autodeskId": "HWUBNU689CRU",
    "name": "James Smith"
  },
  "createdAt": "2025-06-18T21:14:14.672Z",
  "workflowId": "4e609369-e950-4097-b7d3-e6cf1c3c5415"
}

```

Show More

### Notes

- Confirm that the `status` is `OPEN` and that the `workflowId` matches the workflow you selected.
- If you need to inspect the reviewâs steps and progress, use [GET reviews/workflow](../http-docs/http-reviews-getreviewworkflow-GET.md) for the workflow snapshot or [GET reviews/progress](../http-docs/http-reviews-getreviewprogress-GET.md) for progress updates.

## [Step 4 (optional): Use a Webhook to Monitor Review Creation](#step-4-optional-use-a-webhook-to-monitor-review-creation)

When a review is created, the system validates its files in the background.
If any file is invalid or missing, the review may later change from `OPEN` to `FAILED` even though the initial request returned `201 Created`.

Rather than repeatedly calling [GET reviews/:id](../http-docs/http-reviews-getreview-GET.md), register a webhook for the `review.created-1.0` event. See the [Creating a Webhook and Listening to Events](../../webhooks/how-to-docs/create-a-hook-reviews.md) tutorial for more details.
ACC sends a POST message to your callback URL when the review finishes initializationâwhether successful or failed.

When registering a webhook, you must provide a callback endpoint with a POST method to receive messages about the result of the Review creation.

In this example, assume the callback URL is:

```
https://your-webhook-url.com/callback

```

### Request

```
curl 'https://developer.api.autodesk.com/webhooks/v1/systems/autodesk.construction.reviews/events/review.created-1.0/hooks' \
  -X POST \
  -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
  -H 'Content-Type: application/json' \
  -H 'region: US' \
  -d '{
         "callbackUrl": "https://your-webhook-url.com/callback",
         "scope": {
           "project": "9ba6681e-1952-4d54-aac4-9de6d9858dd4"
         },
         "hookAttribute": {
           "projectId": "9ba6681e-1952-4d54-aac4-9de6d9858dd4"
         }
      }'

```

Show More

After the review finishes initialization, ACC sends a POST request to your callback URL with the following payload:

### Response

```
{
  "version": "1.0",
  "resourceUrn": "c7fc352d-c33d-4e4b-9472-3dfd054be1f7",
  "hook": {
      "hookId": "271e19ed-0443-44a8-9c0d-9fbcf2b0848d",
      "tenant": "9ba6681e-1952-4d54-aac4-9de6d9858dd4",
      "callbackUrl": "https://your-webhook-url.com/callback",
      "createdBy": "HWUBNU689CRU",
      "event": "review.created-1.0",
      "createdDate": "2025-08-05T21:47:11.233+00:00",
      "lastUpdatedDate": "2025-08-05T21:47:11.233+00:00",
      "system": "autodesk.construction.reviews",
      "creatorType": "O2User",
      "status": "active",
      "scope": {
          "project": "9ba6681e-1952-4d54-aac4-9de6d9858dd4"
      },
      "hookAttribute": {
          "projectId": "9ba6681e-1952-4d54-aac4-9de6d9858dd4"
      },
      "autoReactivateHook": true,
      "urn": "urn:adsk.webhooksprod:events.hook:271e19ed-0443-44a8-9c0d-9fbcf2b0848d",
      "callbackWithEventPayloadOnly": false,
      "__self__": "/systems/autodesk.construction.reviews/events/review.created-1.0/hooks/271e19ed-0443-44a8-9c0d-9fbcf2b0848d"
  },
  "payload": {
      "roundNum": 1,
      "sequenceId": "9",
      "status": "OPEN"
  }
}

```

Show More

### Notes

- The default value for `region` is `US`, but we recommend explicitly specifying the region when sending requests.
For the complete list of supported region API values, see the [Regions](https://aps.autodesk.com/en/docs/acc/v1/overview/acc-regions/) page.
- The `payload` includes the reviewâs creation status.
If an error occurs, an `errorCode` field is returned.

Example of a failed `payload`:

```
{
  "roundNum": 1,
  "sequenceId": "9",
  "status": "FAILED",
  "errorCode": "INVALID_FILE_VERSION"
}

```

The `errorCode` value indicates the type of error that occurred:

- `NO_VALID_VERSION_URN` â Some of the provided URNs are invalid.
- `MALWARE_DETECTED` â A file was detected as malware.
- `VERSIONS_NOT_EXISTED` â One or more version files no longer exist (for example, they were deleted).
- `DIFFERENT_PROJECT_VERSIONS` â One or more URNs belong to a different project.
- `PARENT_FOLDER_NOT_EXISTED` â A parent folder no longer exists (it may have been deleted).
- `VERSIONS_ACCESS_DENIED` â The initiator does not have permission to access the specified files.
- `RETRYABLE_TEMP_ERROR` â The review creation failed due to a temporary error; you can retry the request later.

## [Step 5 (optional): List Reviews in a Project](#step-5-optional-list-reviews-in-a-project)

To retrieve all reviews that you can access in a project, call [GET reviews](../http-docs/http-reviews-reviews-GET.md). Use the `limit` and `offset` parameters for pagination. The default `limit` is 50 and the default `offset` is 0.

If the response does not include a `nextUrl`, it means you have reached the last page of results.

### Request

```
curl 'https://developer.api.autodesk.com/construction/reviews/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/reviews?limit=10&offset=0&filter[status]=OPEN' \
  -X GET \
  -H 'x-user-id: 83QFRYJA3LRX' \
  -H 'Authorization: Bearer nFRJxzCD8OOUr7hzBwbr06D76zAT' \
  -H 'Content-Type: application/json'

```

### Response

```
{
  "results": [
    {
      "id": "c7fc352d-c33d-4e4b-9472-3dfd054be1f7",
      "name": "The 2nd Floor Design Review",
      "status": "OPEN",
      "sequenceId": 9,
      "currentStepId": "Lane_3ReoxO2T0o",
      "currentStepDueDate": "2025-06-21T21:14:14.027Z",
      "createdBy": {
        "autodeskId": "HWUBNU689CRU",
        "name": "James Smith"
      },
      "createdAt": "2025-06-18T21:14:14.672Z",
      "workflowId": "4e609369-e950-4097-b7d3-e6cf1c3c5415",
      "nextActionBy": {
        "candidates": {
          "companies": [ { "autodeskId": "26980302", "name": "Autodesk Co. Ltd." } ],
          "roles":     [ { "autodeskId": "1473817", "name": "Architect" } ],
          "users":     [ { "autodeskId": "83QFRYJA3LRX", "name": "Bob Smith" } ]
        }
      }
    },
    ...
  ],
  "pagination": {
    "limit": 10,
    "offset": 0,
    "totalResults": 100,
    "nextUrl": "https://developer.api.autodesk.com/construction/reviews/v1/projects/9ba6681e-1952-4d54-aac4-9de6d9858dd4/reviews?limit=10&offset=10&filter[status]=OPEN"
  }
}

```

Show More

### Notes

- Use the `filter[status]` parameter (as shown above) to restrict results by status, such as `OPEN` or `CLOSED`.
- Use the `nextUrl` field in the response to retrieve additional pages of results.
