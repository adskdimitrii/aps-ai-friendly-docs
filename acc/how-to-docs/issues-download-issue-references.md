# Download Issue References

Source: https://aps.autodesk.com/en/docs/acc/tutorials/issues/download-issue-references/

---

# Download Issue References

This tutorial demonstrates how to download references such as ACC photos that are associated with ACC issues. The steps include, finding the ID of the relevant issue, using the Relationships API to find the IDs of the references (such as photos) associated with the relevant issue, retreiving a signed-URL of the reference, and using the signed-URL to download the reference.

## [Before You Begin](#before-you-begin)

- [Register an app](https://aps.autodesk.com/myapps)
- Acquire a [3-legged OAuth token](../../oauth/how-to-docs/get-3-legged-token.md) with the `data:read` scope.
- Verify that you have access to the relevant account and ACC project.
- Find the relevant project ID for the project you want to create an issue in by following the [Retrieve a Project ID](getting-started-retrieve-account-and-project-id.md) tutorial. In this example, assume the project ID is `f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`.

## [Step 1: Find the Relevant Issue](#step-1-find-the-relevant-issue)

Find the ID of the issue you want to download the reference from, by calling [GET issues](../http-docs/http-issues-issues-GET.md) using the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`).

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/issues/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/issues' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "pagination": {
    "limit": 10,
    "offset": 100,
    "totalResults": 25
  },
  "results": [
    {
      "id": "3570f222-6c54-4b01-90e6-e701749f0222",
      "containerId": "2220f222-6c54-4b01-90e6-d701748f0222",
      "deleted": false,
      "displayId": 7,
      "title": "Door missing a screw",
      "description": "The door is missing a screw, please fix this",
      "snapshotUrn": "",
      "issueTypeId": "8770f222-6c54-4e01-93e6-e701749f0222",
      "issueSubtypeId": "1370f222-6c54-3a01-93e6-e701749f0222",
      "status": "open",
      "assignedTo": "A3RGM375QTZ7",
      "assignedToType": "user",
      "dueDate": "2018-07-25",
      "startDate": "1982-06-01",
      "locationId": "35de6f24-39f5-4808-ba5f-6cbbe2a858e1",
      "locationDetails": "issue location details",
      "linkedDocuments": [
        {}
      ],
      "links": [
        {}
      ],
      "ownerId": "",
      "rootCauseId": "2370f222-6c54-3a01-93e6-f701772f0222",
      "officialResponse": {},
      "issueTemplateId": "",
      "permittedStatuses": [
        "open"
      ],
      "permittedAttributes": [
        "title"
      ],
      "published": true,
      "permittedActions": {},
      "commentCount": 3,
      "attachmentCount": "",
      "openedBy": "A3RGM375QTZ7",
      "openedAt": "2018-07-22T15:05:58.033Z",
      "closedBy": "A3RGM375QTZ7",
      "closedAt": "2018-07-22T15:05:58.033Z",
      "createdBy": "A3RGM375QTZ7",
      "createdAt": "2018-07-22T15:05:58.033Z",
      "updatedBy": "A3RGM375QTZ7",
      "updatedAt": "2018-07-22T15:05:58.033Z",
      "watchers": [
        "A3RGM375QTZ7"
      ],
      "customAttributes": [
        {
          "attributeDefinitionId": "2220f222-6c54-4b01-90e6-d701748f0888",
          "value": "368",
          "type": "numeric",
          "title": "Cost Impact ($)"
        }
      ]
    }
  ]
}

```

Show More

Note the ID (`results.[id]`) (`3570f222-6c54-4b01-90e6-e701749f0222`) of the issue you want to download the reference from.

## [Step 2: Find the Photo IDs](#step-2-find-the-photo-ids)

Use the [Relationships API](../http-docs/http-relationship-service-v2-intersect-relationships-POST.md) to find the photos that are associated with the relevant issue. Call [POST relationships](../http-docs/http-relationship-service-v2-intersect-relationships-POST.md) using the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`) and the issue ID (`3570f222-6c54-4b01-90e6-e701749f0222`).

In the request body you need to specify an `issue` type and an `autodesk-bim360-issue` domain.

Note that container ID in the relationships ID is equivalent to the project ID.

### Request

```
curl -v 'https://developer.api.autodesk.com/bim360/relationship/v2/containers/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/relationships:intersect' \
     -X POST \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: application/json' \
     -d '[
           {
             "entities": [
               {
                 "id": "fddd7bcb-91fd-47ff-aacc-a74fdf4f2c1a",
                 "type": "issue",
                 "domain": "autodesk-bim360-issue"
                }
            ]
           }
         ]'

```

Show More

### Response (200)

```
 [

   {
 "page": {
   "syncToken": "eyJMYXN0TW9kaWZpZWQiOnsiRGF0ZVRpbWUiOiIyMDIyLTAzLTAxVDE0OjE3OjM0Ljc4NzAzNTBaIiwiT2Zmc2V0TWludXRlcyI6MH0sIk9wZXJhdGlvbiI6MiwiT3JpZ2luYWxQYXJhbWV0ZXJzIjp7Il9fdHlwZSI6IlN0b3JlSW50ZXJzZWN0UmVsYXRpb25zaGlwczojQXV0b2Rlc2suTnVjbGV1cy5TdG9yZS5SZWxhdGlvbnNoaXBzLk9wZXJhdGlvbnMiLCJDYWxsZXJUeXBlIjoxLCJDb250YWluZXJJZCI6ImExZTBhYzE2LTI2MDMtNGVkMS04YjY0LTdkMTZhNjRjN2QwMSIsIkVudGl0aWVzIjpbeyJBY3Rpdml0eSI6bnVsbCwiRG9tYWluIjoiYXV0b2Rlc2stYmltMzYwLWlzc3VlIiwiRW50aXR5SWQiOiIxNzkyY2YwOC02NmNjLTQyOGUtOTdmYS0zMGNjNDI2NmE1MzkiLCJFbnRpdHlUeXBlIjoiaXNzdWUifV0sIkluY2x1ZGVEZWxldGVkIjpmYWxzZSwiTW9kaWZpZWRBZnRlciI6bnVsbCwiT25seURlbGV0ZWQiOmZhbHNlLCJPeHlnZW5JZCI6IlZVTUpQNEVFOU5ZOCIsIldpdGhFbnRpdGllcyI6bnVsbH0sIlZlcnNpb25OdW1iZXIiOjF9"
 },
 "relationships": [
   {
     "permission": null,
     "id": "b8f676fb-e39b-4557-b10f-f970030b6e41",
     "createdOn": "2022-03-01T14:17:34.781856+00:00",
     "isReadOnly": false,
     "isService": true,
     "isDeleted": false,
     "entities": [
       {
         "createdOn": "2022-01-26T15:17:41.772891+00:00",
         "domain": "autodesk-construction-photo",
         "type": "photo",
         "id": "5439bfb7-8006-4388-a454-f02560f99566"
       },
       {
         "createdOn": "2022-03-01T14:17:34.774043+00:00",
         "domain": "autodesk-bim360-issue",
         "type": "issue",
         "id": "1792cf08-66cc-428e-97fa-30cc4266a539"
       }
     ]
   }
 ]
}

```

Show More

]

Note the photo ID (`relationships.[entities.[id]]`) (`5439bfb7-8006-4388-a454-f02560f99566`)

## [Step 3: Generate a Signed URL](#step-3-generate-a-signed-url)

Use the Photos API to generate a signed URL, which you can use to download the photo directly from S3.

Call [GET photos](../http-docs/http-photos-getphoto-GET.md) using the project ID (`f6a1e3b5-abaa-4b01-b33a-5d55f36ba047`) and photo ID (`5439bfb7-8006-4388-a454-f02560f99566`). To generate the signed URL you need add the `include` query string parameter (`include=signedUrls`).

You need to repeat this step for each photo.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/photos/v1/projects/f6a1e3b5-abaa-4b01-b33a-5d55f36ba047/photos/5439bfb7-8006-4388-a454-f02560f99566?include=signedUrls' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "createdAt": "2021-03-14T10:20:33",
  "createdBy": "PER8KQPK2JRT",
  "deletedAt": "2021-03-19T11:50:33",
  "deletedBy": "PER8KQPK2JRT",
  "description": "The left side of the office",
  "id": "5439bfb7-8006-4388-a454-f02560f99566",
  "isPublic": false,
  "latitude": 37.757497,
  "locked": false,
  "longitude": -122.42115,
  "mediaType": "NORMAL",
  "projectId": "5439bfb7-8006-4388-a454-f02560f99566",
  "signedUrls": {
    "fileUrl": "https://s3.amazonaws.com/com.autodesk.oss-persistent/f0/7b/66/4df1b73d0cc643e6179b85eae7d8d529d2/ce8edd30-ef28-467c-8d99-7d7051097ee0?response-content-disposition=attachment%3B%20filename%3D%22c35b8b28-859e-4256-a3bc-41772a673260.jpg%22&response-content-type=image%2Fjpeg&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCOKZyru7bEOWhRlJOiFZUwLwGSFSWPO5VknX%2BIisldAwIgWN6g5zYxXLOzdiZgR4sYuyY4qr1k1SAQOTOCI7EOmKIqvQMI3P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw5OTM3ODk5OTIwNjMiDK0wr6QcJBV%2BrqLz7iqRA55WGaeF1IZVyH5XzR%2FyR72VqyCRIEwm9D3Pt%2BTOxtaNa519ldQcvjYptWrlwnrgr1T9c3jxtEXxHZveX3XwgaSQq7JyHACBAMVwkKABwczEzPOryCvIJBWjgr2ABoYGr0dDCFdh9IjdoDrOrXDDesn4I5GamK%2BdNzXBR1MJH3ocmoZXxrmaJGigr62ShQ3q7AoqMgIX55XH8DnYMP4k9OlGGJsL7P80OnvOXfNLFl9EVJp5jnp%2BT1eO3FezRxc%2FqkeTG7t6QHh87P4cJKzWV9pW3AQoYvBKyQ5uJn5WA8%2FFg%2BhzYalr5Y%2B4%2FneB0xfn7WS2I%2FvjIo6rOkIqx7K3Ty1p1kuZ6e64%2BlEXx8mYHO2NOYobbSf%2Fx%2B7FU1rhZqvqUGB%2BRoMXFI%2FIkaxe%2B%2Ba6sZYV6Dm6bcim835asw%2B48vkt3XLZ6kBNqOJMdqvIBp%2F7opV9Bc4%2BMkhPc6wT%2BwAoQ0jHGuNZiLh%2BsxcB8EtwziI18v5LFw6WmffTQD3oc8WTb9xUZmoQ8qDq5z%2FY4%2BY2EAq6MNaP7oIGOusBXz4xrUPPH0cr5UO912gp6aysXFnqxu55it8zqPwiGI2Xe0RlaMTAMh1jwDZ4LZD4N2NERk%2F%2BlR1KaRk2Jvo34HIXVnUqNWlYAR3TyV2intl8wwJWlgKQH6DI%2BzwOJ27kDToULG5TQpQk6xAQaToplmERCien7Pi8vlb0JNBCzkoKNh40Z1wPxcS%2BitdU0IkD0n39bvWy5uG0hoUuifHr53vaf7eqFRSdrd%2B%2BYuJ00yT%2FtWS6FLpLKCSgZw8GKoAq3PpfPggmg99bAju7H%2FD8xfVgBPhb91tEGCCdyub4jDtj6euoUFXK%2FiMIVg%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210324T193346Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=ASIA6OYT73R75HNE4VUO%2F20210324%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=e694954290d485482c6334b39b591c87e4a16ba2425f05da1dc25faf47afba2d",
    "thumbnailUrl": "https://s3.amazonaws.com/com.autodesk.oss-opsstaging-persistent/81/b8/3d/e2855b46af2060d595ce31923310079c4b/ce8edd30-ef28-467c-8d99-7d7051097ee0?response-content-disposition=attachment%3B%20filename%3D%22c35b8b28-859e-4256-a3bc-41772a673260_t.jpg%22&response-content-type=image%2Fjpeg&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCOKZyru7bEOWhRlJOiFZUwLwGSFSWPO5VknX%2BIisldAwIgWN6g5zYxXLOzdiZgR4sYuyY4qr1k1SAQOTOCI7EOmKIqvQMI3P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw5OTM3ODk5OTIwNjMiDK0wr6QcJBV%2BrqLz7iqRA55WGaeF1IZVyH5XzR%2FyR72VqyCRIEwm9D3Pt%2BTOxtaNa519ldQcvjYptWrlwnrgr1T9c3jxtEXxHZveX3XwgaSQq7JyHACBAMVwkKABwczEzPOryCvIJBWjgr2ABoYGr0dDCFdh9IjdoDrOrXDDesn4I5GamK%2BdNzXBR1MJH3ocmoZXxrmaJGigr62ShQ3q7AoqMgIX55XH8DnYMP4k9OlGGJsL7P80OnvOXfNLFl9EVJp5jnp%2BT1eO3FezRxc%2FqkeTG7t6QHh87P4cJKzWV9pW3AQoYvBKyQ5uJn5WA8%2FFg%2BhzYalr5Y%2B4%2FneB0xfn7WS2I%2FvjIo6rOkIqx7K3Ty1p1kuZ6e64%2BlEXx8mYHO2NOYobbSf%2Fx%2B7FU1rhZqvqUGB%2BRoMXFI%2FIkaxe%2B%2Ba6sZYV6Dm6bcim835asw%2B48vkt3XLZ6kBNqOJMdqvIBp%2F7opV9Bc4%2BMkhPc6wT%2BwAoQ0jHGuNZiLh%2BsxcB8EtwziI18v5LFw6WmffTQD3oc8WTb9xUZmoQ8qDq5z%2FY4%2BY2EAq6MNaP7oIGOusBXz4xrUPPH0cr5UO912gp6aysXFnqxu55it8zqPwiGI2Xe0RlaMTAMh1jwDZ4LZD4N2NERk%2F%2BlR1KaRk2Jvo34HIXVnUqNWlYAR3TyV2intl8wwJWlgKQH6DI%2BzwOJ27kDToULG5TQpQk6xAQaToplmERCien7Pi8vlb0JNBCzkoKNh40Z1wPxcS%2BitdU0IkD0n39bvWy5uG0hoUuifHr53vaf7eqFRSdrd%2B%2BYuJ00yT%2FtWS6FLpLKCSgZw8GKoAq3PpfPggmg99bAju7H%2FD8xfVgBPhb91tEGCCdyub4jDtj6euoUFXK%2FiMIVg%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210324T193346Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=ASIA6OYT73R75HNE4VUO%2F20210324%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=fac56130302305057c9ae301503860edb2d296c43dcfb5a59ebf3744f5126baa"
  },
  "size": 11359,
  "takenAt": "2021-03-13T18:15:00",
  "title": "Office Dry Wall",
  "type": "FIELD-REPORT",
  "updatedAt": "2021-03-14T11:20:33",
  "updatedBy": "PER8KQPK2JRT",
  "urls": {
    "fileUrl": "https://developer.api.autodesk.com/construction/photos/assets/ce8edd30-ef28-467c-8d99-7d7051097ee0/c35b8b28-859e-4256-a3bc-41772a673260.jpg\"",
    "thumbnailUrl": "https://developer.api.autodesk.com/construction/photos/assets/ce8edd30-ef28-467c-8d99-7d7051097ee0/c35b8b28-859e-4256-a3bc-41772a673260_t.jpg\""
  },
  "userCreatedAt": "2021-03-13T18:20:33"
}

```

Show More

Note the signed URL of the photo (`signedUrl.fileUrl`).

The signed URL expires after a short amount of time. See the `X-Amz-Expires-` value in the signed URL for the length of time. If the time expires you need to call GET photos again to get a new download link.

## [Step 4: Download the Photo](#step-4-download-the-photo)

To download the photo from the signed URL, use a GET method and the `signedUrl.fileUrl` attribute as the URI.

Note that you should not use a bearer token with this call.

### Request

```
curl -X GET "https://s3.amazonaws.com/com.autodesk.oss-persistent/f0/7b/66/4df1b73d0cc643e6179b85eae7d8d529d2/ce8edd30-ef28-467c-8d99-7d7051097ee0?response-content-disposition=attachment%3B%20filename%3D%22c35b8b28-859e-4256-a3bc-41772a673260.jpg%22&response-content-type=image%2Fjpeg&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCOKZyru7bEOWhRlJOiFZUwLwGSFSWPO5VknX%2BIisldAwIgWN6g5zYxXLOzdiZgR4sYuyY4qr1k1SAQOTOCI7EOmKIqvQMI3P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw5OTM3ODk5OTIwNjMiDK0wr6QcJBV%2BrqLz7iqRA55WGaeF1IZVyH5XzR%2FyR72VqyCRIEwm9D3Pt%2BTOxtaNa519ldQcvjYptWrlwnrgr1T9c3jxtEXxHZveX3XwgaSQq7JyHACBAMVwkKABwczEzPOryCvIJBWjgr2ABoYGr0dDCFdh9IjdoDrOrXDDesn4I5GamK%2BdNzXBR1MJH3ocmoZXxrmaJGigr62ShQ3q7AoqMgIX55XH8DnYMP4k9OlGGJsL7P80OnvOXfNLFl9EVJp5jnp%2BT1eO3FezRxc%2FqkeTG7t6QHh87P4cJKzWV9pW3AQoYvBKyQ5uJn5WA8%2FFg%2BhzYalr5Y%2B4%2FneB0xfn7WS2I%2FvjIo6rOkIqx7K3Ty1p1kuZ6e64%2BlEXx8mYHO2NOYobbSf%2Fx%2B7FU1rhZqvqUGB%2BRoMXFI%2FIkaxe%2B%2Ba6sZYV6Dm6bcim835asw%2B48vkt3XLZ6kBNqOJMdqvIBp%2F7opV9Bc4%2BMkhPc6wT%2BwAoQ0jHGuNZiLh%2BsxcB8EtwziI18v5LFw6WmffTQD3oc8WTb9xUZmoQ8qDq5z%2FY4%2BY2EAq6MNaP7oIGOusBXz4xrUPPH0cr5UO912gp6aysXFnqxu55it8zqPwiGI2Xe0RlaMTAMh1jwDZ4LZD4N2NERk%2F%2BlR1KaRk2Jvo34HIXVnUqNWlYAR3TyV2intl8wwJWlgKQH6DI%2BzwOJ27kDToULG5TQpQk6xAQaToplmERCien7Pi8vlb0JNBCzkoKNh40Z1wPxcS%2BitdU0IkD0n39bvWy5uG0hoUuifHr53vaf7eqFRSdrd%2B%2BYuJ00yT%2FtWS6FLpLKCSgZw8GKoAq3PpfPggmg99bAju7H%2FD8xfVgBPhb91tEGCCdyub4jDtj6euoUFXK%2FiMIVg%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210324T193346Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=ASIA6OYT73R75HNE4VUO%2F20210324%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=e694954290d485482c6334b39b591c87e4a16ba2425f05da1dc25faf47afba2d"

```

Congratulations! You have downloaded a photo associated with an ACC issue.
