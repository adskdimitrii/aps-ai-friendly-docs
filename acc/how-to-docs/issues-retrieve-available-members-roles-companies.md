# Retrieve Available Members Roles and Companies

Source: https://aps.autodesk.com/en/docs/acc/tutorials/issues/retrieve-available-members-roles-companies/

---

# Retrieve Available Members Roles and Companies

This tutorial demonstrates how to determine the members of a project. This is important for users with *Create for my company* or *Create for other companies* permissions, who can only assign issues to members of the project.

In addition, the tutorial shows how to verify the company that was assigned to each user within the project. This information is important when the person assigning an issue has *Create for my company* permissions or when adding or removing a watcher who has *Create for my company* permissions. This is because an assigner with *Create for my company* permissions can only assign an issue to someone who is a member of the same company.

This workflow uses the [Data Connector](https://aps.autodesk.com/en/docs/bim360/v1/overview/field-guide/data-connector/) API to extract project user and user company data in CSV files.

Note that this workflow is a temporary method for determining permissions, and we will be releasing endpoints that directly retrieve project users by companies in the near future.

## [Before You Begin](#before-you-begin)

- [Register an app](/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with the `data:read` scope.
- Verify that you have project admin or executive overview permissions.
- Verify that you have access to the relevant account and ACC project.
- Find the relevant project ID for the project you want to retrieve users for by following the [Retrieve an Account ID and Project ID](getting-started-retrieve-account-and-project-id.md) tutorial. In this example, assume the account ID is `g5s4e3b5-vbta-6b02-d23a-5d55f36ba876`, and the project ID is `f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`.

## [Step 1: Submit a Data Request](#step-1-submit-a-data-request)

Submit a data request by calling [POST requests](../http-docs/http-data-connector-requests-POST.md) using the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`) to retrieve the data about the project including the members of the project and the companies associated with the users. Specify the `admin` service group to get information about users and companies.

In this tutorial we will use a callback URL to retrieve the data. For details about the workflow for polling the data see the [Data Connector](https://aps.autodesk.com/en/docs/bim360/v1/tutorials/data-connector/) tutorials.

Note that the data extraction process can take time depending on the amount of data that you are retrieving.

We recommend that you set up the workflow to extract data once a day (`DAY`) so you can update your database every day. For more details about different data extraction interval options, see [POST requests](../http-docs/http-data-connector-requests-POST.md). Note that the user needs to have project admin or executive overview permissions.

### Request

```
curl --location --request POST 'https://developer.api.autodesk.com/data-connector/v1/accounts/g5s4e3b5-vbta-6b02-d23a-5d55f36ba876/requests' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'
  --header 'Content-Type: application/json' \
  --data-raw '{
      "description": "Issues Daily Extract",
      "scheduleInterval": "DAY",
      "effectiveFrom": "2022-09-08T13:54:05.332Z",
      "effectiveTo": "2023-11-19T16:00:00Z",
      "reoccuringInterval": 1,
      "serviceGroups": ["admin"],
      "projectId": "78246834-79c9-4271-b584-7252a5456f72",
      "callbackUrl": "<CALLBACK_URL>"
  }'

```

Show More

### Response

```
{
  "id": "6c2ceb8d-792b-4439-b6b1-def3e2c7b4f2",
  "description": "Issues Daily Extract",
  "isActive": true,
  "accountId": "g5s4e3b5-vbta-6b02-d23a-5d55f36ba876",
  "projectId": "78246834-79c9-4271-b584-7252a5456f72",
  "createdBy": "89ac8716-88c5-417f-ac02-935461db9ca1",
  "createdByEmail": "jon.doe@build.com",
  "createdAt": "2022-09-11T14:49:50.915Z",
  "updatedBy": "89ac8716-88c5-417f-ac02-935461db9ca1",
  "updatedAt": "2022-09-11T14:49:50.915Z",
  "scheduleInterval": "DAY",
  "reoccuringInterval": 1,
  "effectiveFrom": "2022-09-08T13:54:05.332Z",
  "effectiveTo": "2023-11-19T16:00:00Z",
  "lastQueuedAt": null,
  "serviceGroups": [
      "admin"
  ],
  "callbackUrl": "<CALLBACK_URL>",
  "sendEmail": true
}

```

Show More

The data request has been submitted.

## [Step 2: Receive the Callback URL](#step-2-receive-the-callback-url)

Every time a Data Connector request has finished processing, you receive a notification to the callback URL with a JSON payload that includes details about the specific job.

The example below shows the type of data you should receive.

### Request

```
curl --location --request POST '<CALLBACK_URL>' \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "state": "complete",
      "accountId": "g5s4e3b5-vbta-6b02-d23a-5d55f36ba876",
      "requestId": "6b2b85d5-6629-456e-a8d3-4a68ef5b3188",
      "jobId": "b0783d6e-791f-4430-ac6d-35864cf266db",
      "success": true
  }'

```

Show More

Note the `jobId` (`b0783d6e-791f-4430-ac6d-35864cf266db`) for the extraction, which you will need to use to retrieve the extracted data.

## [Step 3: Examine the Files Contained in the Jobâs Data Extract](#step-3-examine-the-files-contained-in-the-job-s-data-extract)

To see a list of the files contained in your jobâs data extract, call [GET jobs/:jobId/data-listing](en/docs/bim360/v1/reference/http/data-connector-jobs-jobId-data-listing-GET/) using the job ID (`b0783d6e-791f-4430-ac6d-35864cf266db`).

### Request

```
curl -X GET 'https://developer.api.autodesk.com/data-connector/v1/accounts/<accountId>/jobs/<jobId>/data-listing' \
-H 'Authorization: Bearer <authToken>'

```

### Response

```
[
{
    "name": "README.html",
    "createdAt": "2022-09-10T23:49:01.785Z",
    "size": 9738
},
{
    "name": "admin_account_services.csv",
    "createdAt": "2022-09-10T23:38:03.119Z",
    "size": 533
},
{
    "name": "admin_accounts.csv",
    "createdAt": "2022-09-10T23:38:02.911Z",
    "size": 141
},
{
    "name": "admin_companies.csv",
    "createdAt": "2022-09-10T23:38:02.903Z",
    "size": 633
},
{
    "name": "admin_project_companies.csv",
    "createdAt": "2022-09-10T23:38:02.959Z",
    "size": 424
},
{
    "name": "admin_project_products.csv",
    "createdAt": "2022-09-10T23:38:02.967Z",
    "size": 872
},
{
    "name": "admin_project_roles.csv",
    "createdAt": "2022-09-10T23:38:02.919Z",
    "size": 3837
},
{
    "name": "admin_project_user_companies.csv",
    "createdAt": "2022-09-10T23:38:02.911Z",
    "size": 354
},
{
    "name": "admin_projects.csv",
    "createdAt": "2022-09-10T23:38:04.811Z",
    "size": 452
},
{
    "name": "admin_roles.csv",
    "createdAt": "2022-09-10T23:38:04.811Z",
    "size": 3447
},
{
    "name": "admin_users.csv",
    "createdAt": "2022-09-10T23:38:06.311Z",
    "size": 1008
},
{
    "name": "autodesk_data_extract.zip",
    "createdAt": "2022-09-10T23:49:01.821Z",
    "size": 142025
}
]

```

Show More

The files contain data about the project, including information about project members and companies.

## [Step 4: Download the Files from the Data Extract](#step-4-download-the-files-from-the-data-extract)

To dowload project data call [GET jobs/:jobId/data/:name](../http-docs/http-data-connector-jobs-jobId-data-name-GET.md) specifying the relevant files:

- `admin_users.csv`
- `admin_companies.csv`
- `admin_project_user_companies.csv`

Alternatively, you can download the ZIP file, which contains all the files.

### Request

```
curl --location --request GET 'https://developer.api.autodesk.com/data-connector/v1/accounts/g5s4e3b5-vbta-6b02-d23a-5d55f36ba876/jobs/b0783d6e-791f-4430-ac6d-35864cf266db/data/autodesk_data_extract.zip' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
    "name": "autodesk_data_extract.zip",
    "size": 1152,
    "signedUrl": "https://bim360dc-s-ue1-extracts.s3.amazonaws.com/data/5c07c84c-bbd9-476e-8712-547f74c5b76b/b0783d6e-791f-4430-ac6d-35864cf266db/admin_users.csv?AWSAccessKeyId=ASIAX4NRGUIN3T674OXQ&Expires=1662913320&Signature=8WZ70JCtiP855ch0ySgeil2USAM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDoItRVB4RE%2BRFXFaTDuld3ht5wudsRnzG0mca22sAPNwIgMGHW9G3KEKgeTXLZrBlLLvOsew0Ccawr4GXtdz9bqMIqiwMIeRACGgw1NDIwNzQzODA4MjciDBksP21QdYraPE5WUCroAiobOr0EEPBEg2xGIXiAZzmItu15wdWT5pvC5ci7RH%2Bz6tMOSo6teD5jR9p380aPFmF6N0PgX%2BJwgab1Cnl3Wsu8L9Ay8kk4yI26DLG8yDGj5ZVOS%2BfJArcn%2FHWzhJnrg2yu2o8hcQbGbYHKIYR%2Fjb4WKgI%2Bnc0TnHq7BGD95gACce19uk3atblL5HhJKR%2FZ8Vd%2F%2FYGhkONezkFXoe0SAq1OEzuJA%2BbreJoLRkit72Iz%2BQZPVp2aS40m4XvI7LPDHQmeeEPz%2BIDRLtQ52c1pagCXONti44ceHkxvuM0oRSX%2BYoes0mefU5SzlVUpTnUKBI2lW8urvyVAvTNHem9agfm1W9%2FQdmpLp%2Blp6yCVIZkjitBauylqo0E5mMQQjUpmda8Wc6cD4AoxZiKca1KqEBmPhOB5flQd6qMYDDiwr%2Fb%2FmjlkjQSAVU%2BpQM5VqsjOyVfu7anR0RNt8sQFQIfyckpr5H5V4Yn9yTDWlfiYBjqdAY%2BHuvnfG0jgHbeHPhcVuYoMkmnmsLt%2B4RxWOO0Ihqvpj6O3g%2B4R6nkEmyut0qchu5iMkcVD6HJYmWKJ2%2FN73Nb%2BNER9a9Ab%2F8aHnJpLfVV1x0W0MsAiRUwRN7onrHfOiPrieifpihA59RXupDmL7CxobofuE6ARk0s7OadEcnWqyN3dXQn9G7rRRcuieh396vbOQ%2BNSdGWfiLNPY6s%3D"
}

```

To download the file from the signed URL, use a GET method and the `signedUrl` attribute as the URI. Note that you should not use a bearer token with this call.

## [Step 5: Examine the Data](#step-5-examine-the-data)

To get a list of all the members of the project, use the `admin_users.csv` file.

To verify the company that is assigned to each user within the project, you need to examine 3 CSV files:

- `admin_users.csv`
- `admin_companies.csv`
- `admin_project_user_companies.csv`

1. Use `admin_users.csv` to get the **IDs of the users** of the project. Note the data in the `name` (user name) column and the `id` (user ID) column.
2. Use `admin_companies.csv` to get the **IDs of the companies**. Note the data in the `name` (company name) column and the `id` (company ID) column.
3. Use `admin_project_user_companies.csv` to find **the companies that are assigned to the users**. The user IDs that you found in (a) is equivalent to the `user_id` column, and the company IDs that you found in (b) is equivalent to the `company_oxygen_id` column. Use this file to verify the company that is assigned to each user.
![../../../_images/fetching-permitted-users-step3.png](../../../_images/fetching-permitted-users-step3.png)![../../../_images/fetching-permitted-users-step4-companies.png](../../../_images/fetching-permitted-users-step4-companies.png)![../../../_images/fetching-permitted-users-step4-user-companies.png](../../../_images/fetching-permitted-users-step4-user-companies.png)
