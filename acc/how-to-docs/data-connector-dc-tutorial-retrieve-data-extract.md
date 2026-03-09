# Find a Job and Retrieve Its Data Extract

Source: https://aps.autodesk.com/en/docs/acc/tutorials/data-connector/dc-tutorial-retrieve-data-extract/

---

# Find a Job and Retrieve Its Data Extract

When an active data request spawns a job, the job extracts data for specified services. To retrieve and examine that data, you need the ID of the job. You receive that ID through the email notification that the job sends on completion and, if you specified a callback URL, a post that the job sends on completion. You may also retrieve a list of jobs spawned by the data request. There you can find the ID of a job whose data extract you wish to examine.

To retrieve the jobâs data extract, first use the job ID to retrieve descriptions of the files in the data extract. You can use those descriptions to determine which of the files youâd like to examine, and then request a URL where you can retrieve your desired files.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with `data:create`, `data:read`, and `data:write` scopes. The tokenâs authenticated user must have executive overview permissions.
- Verify that you have access to a relevant BIM 360 account that contains at least one project. If you donât know your account ID, you can derive it from your hub ID: Use [GET hubs](../../data/http-docs/http-hubs-GET.md) in the Data Management API to retrieve your hub ID. Remove the initial âb.â from the hub ID to get your account ID. For example, a hub ID of `b.c8b0c73d-3ae9` translates to an account ID of `c8b0c73d-3ae9`.

## [Step 1: Get a List of Jobs Spawned By Your Data Request](#step-1-get-a-list-of-jobs-spawned-by-your-data-request)

In this example, weâll assume you donât have the ID of the job whose data extract you want. Use the [GET requests/:requestId/jobs](en/docs/bim360/v1/reference/http/data-connector-requests-requestId-GET/) endpoint to retrieve a list of the jobs that your data request has spawned, or use the GET jobs endpoint to retrieve a list of all the jobs that were spawned for the project you specify. If you think there are many spawned jobs, you can set request parameters to limit the number of returned job descriptions, offset the point where you start returning requests, and set sort order. We wonât specify any of this, so the endpoint will use default settings of ascending sort order, a limit of 20 requests, and no offset.

Youâll need the ID of the data request that spawned the jobs, something you retrieved in the previous tutorials.

### Request

```
curl -X GET 'https://developer.api.autodesk.com/data-connector/v1/accounts/<accountId>/requests/<requestId>/jobs?sort=desc&limit=10&offset=0' \
-H 'Authorization: Bearer <authToken>'

```

### Response

```
{
    "pagination": {
        "limit": 10,
        "offset": 0,
        "totalResults": 1
    },
    "results": [
        {
            "id": "9bd7c8a0-9fde-478b-82b7-44098d27c1c1",
            "requestId": "55e410c5-4294-44ce-becf-68e1cfd6738c",
            "accountId": "872264f8-2433-498d-8d36-16649ecb13fe",
            "projectId": "ffffffff-1f51-4b26-a6b7-6ac0639cb138",
            "createdBy": "73f00c25-a5f9-4c05-861d-ce56d54fa649",
            "createdByEmail": "your.name@autodesk.com",
            "status": "complete",
            "completionStatus": "success",
            "startedAt": "2020-11-19T16:33:04.688Z",
            "completedAt": "2020-11-19T16:34:05.293Z",
            "createdAt": "2020-11-19T16:32:54.672Z"
        }
    ]
}

```

Show More

The response provides an array of job records (in this case, just a single job), each with information about a jobâs status. The beginning of each record is the ID of the job, which youâll use to specify the job in subsequent endpoint calls.

## [Step 2: Examine the Files Contained in the Jobâs Data Extract](#step-2-examine-the-files-contained-in-the-job-s-data-extract)

To see a list of the files contained in your jobâs data extract, use the [GET jobs/:jobId/data-listing](en/docs/bim360/v1/reference/http/data-connector-jobs-jobId-data-listing-GET/) endpoint and use the job ID to specify the job.

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
        "createdAt": "2020-11-19T16:34:04.579Z",
        "size": 8892
    },
    {
        "name": "admin_account_services.csv",
        "createdAt": "2020-11-19T16:33:05.058Z",
        "size": 117
    }

...numerous other .csv file listings...

    {
        "name": "admin_users.csv",
        "createdAt": "2020-11-19T16:33:05.106Z",
        "size": 3104
    },
    {
        "name": "autodesk_data_extract.zip",
        "createdAt": "2020-11-19T16:34:04.591Z",
        "size": 53792
    },

...numerous other .csv file listings...

    {
        "name": "submittals_specs.csv",
        "createdAt": "2020-11-19T16:33:35.170Z",
        "size": 125
    }
]

```

Show More

The first file is a README file that contains information about the schema used in each of the CSV files in the data extract. Listed a bit later is a ZIP file that contains all of the other files in the data extract including the README file. The other files are each CSV files for a particular type of object within a service. Each of the file descriptions returns the filename, when the file was created, and the size of the file in bytes.

## [Step 3: Retrieve a File From a Data Extract](#step-3-retrieve-a-file-from-a-data-extract)

Once you have a job ID and the filename of the file in the data extract that youâd like to retrieve, use [GET jobs/:jobId/data/:name](en/docs/bim360/v1/reference/http/data-connector-jobs-jobId-data-name-GET/) to get a signed URL where you can retrieve that data, in this case the ZIP file that contains all the files in the extract along with information about the schemas used.

### Request

```
curl -X GET 'https://developer.api.autodesk.com/data-connector/v1/accounts/<accountId>/jobs/<jobId>/data/autodesk_data_extract.zip' \
-H 'Authorization: Bearer <authToken>'

```

### Response

```
{
    "name": "autodesk_data_extract.zip",
    "size": 53792,
    "signedUrl": "https://bim360dc-p-ue1-extracts.s3.amazonaws.com/data/872264e8-2433-498d-8d36-16649ecb13fe/9bd7c8a0-9fde-478b-82b7-44098d27c1c1/autodesk_data_extract.zip?AWSAccessKeyId=ASIAWZ7KRFT5U5KAQRUI&Expires=1605806413&Signature=5T68bvEaz0f6p4U%2FDZgmpub957c%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCICvo%2F3hehNnqaTXjleNDCmA6p%2F3yWvrsonrBE4nql5ZZAiEAtjSD1kSupwy2vr%2Bp%2Ftt4TBbHj%2BqorI9iRSMeZzTJe1kq2gEIYhACGgw0NjgxMDY0MjM1NDciDDV9RA39yMDubKMpOSq3AWO%2BzbHgSMkHe180nF2Pj050zZiwml94Ux0CJvGtOzfLrQXHWuEjSsddk6DllxLKp%2BGlFBezGkPeRnAlZRVrDXlAyJu%2FensrqPmPXmugluRmvfblAehj7%2FqwsRTFCbJhzJELMQ40GvyEBMXJMJ5gQ8lcAXrxg6TReuBr8mSHmn5U%2F5r56HwwwO3ddOgw%2FfwUY8mQ%2BIjpbF45EMKDJxCqdL2zA2quQKZ617O4%2FIq4eJl6%2F42J10nK%2FzC%2Ft9r9BTrgASDpnOPAkrMIl44%2FXyucqjMQ8A9Dk8DLAKQiV2SXYxdGyONXLpDdCYc0ZGlVcSOGIJq0J2QYMFKAABT6BipiGq%2FFn8RYeWSZO17Y%2FogJCC6TZipvJD0XbYm%2Bi%2FGfRO9%2BPjK8y1DAPtZE1SWA%2F21uWEigbNXTt9AWKnYUzdojNoz9uFKEmRXf8HA95AU%2Ftc3Q%2FxMoV0f8b0h%2FtbecyljXxCMRfnrhGJ1uaSGTIyVpHuDti0hWCDxFjVODC4mUYqrQoKzwQC6jNjohVqiagKZVNK5MTlA6jhp6U9xQdn8tCOjO"
}

```

Use the signed URL returned in the response within 60 seconds. It will return the specified ZIP file from the data extract.
