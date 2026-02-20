# photos:filter

Source: https://aps.autodesk.com/en/docs/acc/reference/http/photos-getfilteredphotos-POST/

---

# photos:filter

Searches for and returns all specified media (photo or video) within a project visible to
the authenticated user.

This endpoint accepts a set of optional media property filters, then uses supplied filters to
search for and return media within a project that satisfy those filters. If no filters are set,
this endpoint returns all assets within a project.

The endpoint paginates returned media. If you donât specify pagination fields, your query will
execute using the default page size. If you want to specify a different a page size, define
the limit in the request body.

A paginated response includes pagination information that may contain a field nextPost Use the data it provides ( url , body ) as the request url and body respectively to request the next page in the query. Repeat until
the response contains no nextPost value, which means the query is finished returning
objects.

## Resource Information

Method and URI POST https://developer.api.autodesk.com/construction/photos/v1/projects/:projectId/photos:filter Authentication Context user context required Required OAuth Scopes data:read Data Format JSON

### Request

## Headers

Authorization * string Must be Bearer <token> , where <token> is obtained via a three-legged OAuth flow. Content-Type * string Must be application/json

### Request

## URI Parameters

projectId string Unique identifier of the project.

### Request

## Body Structure

cursorState string An opaque cursor token that identifies where the next page of paginated results should start. Itâs returned in each paginated response so that it can be supplied in the next request to continue paginated results. If a paginated response contains no cursorState value, then there are no further pages to return. If provided, all other body parameters are ignored. filter object Parameters to filter media by createdAt string Filter by when the media was submitted to the server. A string that specifies a date and time or a date and time range at which all returned objects mast have been updated. A single date and time takes this format: YYYY-MM-DDThh:mm:ss.SSSZ , A date and time range takes this format: YYYY-MM-DDThh:mm:ss.SSSZ..YYYY-MM-DDThh:mm:ss.SSSZ . Range queries can be closed or open in either direction: YYYY-MM-DDThh:mm:ss.SSSZ.. or ..YYYY-MM-DDThh:mm:ss.SSSZ . createdBy array: string The actor that created the media. This is an Autodesk ID. id array: string List of IDs to filter by mediaType array: string Filter by type of the media
Possible values: NORMAL , INFRARED , PHOTOSPHERE , VIDEO takenAt string Filter by when the media was captured on the camera. A string that specifies a date and time or a date and time range at which all returned objects mast have been updated. A single date and time takes this format: YYYY-MM-DDThh:mm:ss.SSSZ , A date and time range takes this format: YYYY-MM-DDThh:mm:ss.SSSZ..YYYY-MM-DDThh:mm:ss.SSSZ . Range queries can be closed or open in either direction: YYYY-MM-DDThh:mm:ss.SSSZ.. or ..YYYY-MM-DDThh:mm:ss.SSSZ . title string Filter by media title include array: string Extra fields to be returned for each Photo Objects (e.g. signedUrls ) Will always be: signedUrls limit int The maximum number of objects that can be returned in a page. A request might return fewer objects than the limit if the Photos service runs out of specified objects to return - at the end of a set of paged results, for example. The maximum limit is 50; the default limit is 25. sort array: string Define how results are sorted. Provide the field ( createdAt , takenAt ) and the direction ( asc , desc ) eg. ["createdAt", "asc"]

### Response

## HTTP Status Code Summary

200 OK Successful return of the filtered media 400 Bad Request The request could not be understood by the server due to malformed syntax or missing request header 403 Forbidden The request was not accepted because it lacked valid authentication credentials

### Response

## Body Structure (200)

pagination object Pagination details limit int Number of result in a page nextPost object Information to fetch the next results of data via POST body object The POST body to use to get the next result cursorState string An opaque cursor token that identifies where the next page of paginated results should start. Itâs returned in each paginated response so that it can be supplied in the next request to continue paginated results. If a paginated response contains no cursorState value, then there are no further pages to return. url string The URL to get the next result results array: object The filtered media createdAt datetime: ISO 8601 The time when the media was created at (ISO8601 Date time format in UTC). createdBy string The actor that created the media. This is an Autodesk ID. deletedAt datetime: ISO 8601 The time when the media was deleted at (ISO8601 Date time format in UTC). deletedBy string The actor that deleted the media. This is an Autodesk ID. description string Description of the media id string: UUID The ID of the media. Max length: 36 isPublic boolean If true the media is public and visible to everyone latitude number Latitude in decimal degrees locked boolean If true the media cannot be deleted or edited longitude number Longitude in decimal degrees mediaType enum:string The type of the media ( NORMAL is for a normal photo)
Possible values: NORMAL , INFRARED , PHOTOSPHERE , VIDEO projectId string: UUID The id of the project Max length: 36 signedUrls object URLs to the mediaâs assets. Accessible by anyone but is short-lived. Must be explicitly requested via `include field fileUrl string Signed URL to the original asset thumbnailUrl string Signed URL to the thumbnail asset size number Filesize of the media in bytes takenAt datetime: ISO 8601 The time when the media was captured by the camera at (ISO8601 Date time format in UTC). title string Title of the media type enum:string The type of object this media was initially added with
Possible values: FIELD-REPORT , FORM , ISSUE , RFI , MARKUP , ASSET , GALLERY , MEETING , SUBMITTAL , LOGO updatedAt datetime: ISO 8601 The time when the media was last updated (ISO8601 Date time format in UTC). updatedBy string The actor that last updated the media. This is an Autodesk ID. urls object URLs to the mediaâs assets. Requires API auth headers ( data:read ) to access it. fileUrl string URL to the original asset thumbnailUrl string URL to the thumbnail asset userCreatedAt datetime: ISO 8601 The time when the media was added to the project at (whether it was offline/locally or online) at (ISO8601 Date time format in UTC).

Max length: 36

Max length: 36

## Example

Success retrieval of filtered media

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/photos/projects/36c0838c-0360-4cfa-b2c6-85e0056ec7e8/photos:filter' \ -X 'POST' \ -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a' \ -H 'Content-Type: application/json' \ -d '{ "cursorState": "eyJsaW1pdCI6MjUsICJ0aXRsZSI6ICJ3YWxsIn0Ks", "filter": { "createdAt": "2021-03-14T10:10:00..2021-03-16T10:15:00", "createdBy": [ "NCSNR6R5NHUD", "5QCVQ6JAUTHB" ], "id": [ "0c96ea4c-bd3d-4b80-9eb6-c123e1faecd5", "5439bfb7-8006-4388-a454-f02560f99566" ], "mediaType": [ "NORMAL" ], "takenAt": "2021-03-12T10:10:00..2021-03-15T10:15:00", "title": "dry wall" }, "include": [ "signedUrls" ], "limit": 25, "sort": [ "createdAt", "asc" ] }'
```

### Response

```
{ "pagination" : { "limit" : 25 , "nextPost" : { "body" : { "cursorState" : "eyJsaW1pdCI6MjUsICJ0aXRsZSI6ICJ3YWxsIn0Ks" }, "url" : "https://developer.api.autodesk.com/construction/photos/v1/projects/8e52b200-f856-4f17-a57c-c03ba2f6673a/photos:filter" } }, "results" : [ { "createdAt" : "2021-03-14T10:20:33" , "createdBy" : "PER8KQPK2JRT" , "deletedAt" : "2021-03-19T11:50:33" , "deletedBy" : "PER8KQPK2JRT" , "description" : "The left side of the office" , "id" : "5439bfb7-8006-4388-a454-f02560f99566" , "isPublic" : false , "latitude" : 37.757497 , "locked" : false , "longitude" : -122.42115 , "mediaType" : "NORMAL" , "projectId" : "36c0838c-0360-4cfa-b2c6-85e0056ec7e8" , "signedUrls" : { "fileUrl" : "https://s3.amazonaws.com/com.autodesk.oss-persistent/f0/7b/66/4df1b73d0cc643e6179b85eae7d8d529d2/ce8edd30-ef28-467c-8d99-7d7051097ee0?response-content-disposition=attachment%3B%20filename%3D%22c35b8b28-859e-4256-a3bc-41772a673260.jpg%22&response-content-type=image%2Fjpeg&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCOKZyru7bEOWhRlJOiFZUwLwGSFSWPO5VknX%2BIisldAwIgWN6g5zYxXLOzdiZgR4sYuyY4qr1k1SAQOTOCI7EOmKIqvQMI3P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw5OTM3ODk5OTIwNjMiDK0wr6QcJBV%2BrqLz7iqRA55WGaeF1IZVyH5XzR%2FyR72VqyCRIEwm9D3Pt%2BTOxtaNa519ldQcvjYptWrlwnrgr1T9c3jxtEXxHZveX3XwgaSQq7JyHACBAMVwkKABwczEzPOryCvIJBWjgr2ABoYGr0dDCFdh9IjdoDrOrXDDesn4I5GamK%2BdNzXBR1MJH3ocmoZXxrmaJGigr62ShQ3q7AoqMgIX55XH8DnYMP4k9OlGGJsL7P80OnvOXfNLFl9EVJp5jnp%2BT1eO3FezRxc%2FqkeTG7t6QHh87P4cJKzWV9pW3AQoYvBKyQ5uJn5WA8%2FFg%2BhzYalr5Y%2B4%2FneB0xfn7WS2I%2FvjIo6rOkIqx7K3Ty1p1kuZ6e64%2BlEXx8mYHO2NOYobbSf%2Fx%2B7FU1rhZqvqUGB%2BRoMXFI%2FIkaxe%2B%2Ba6sZYV6Dm6bcim835asw%2B48vkt3XLZ6kBNqOJMdqvIBp%2F7opV9Bc4%2BMkhPc6wT%2BwAoQ0jHGuNZiLh%2BsxcB8EtwziI18v5LFw6WmffTQD3oc8WTb9xUZmoQ8qDq5z%2FY4%2BY2EAq6MNaP7oIGOusBXz4xrUPPH0cr5UO912gp6aysXFnqxu55it8zqPwiGI2Xe0RlaMTAMh1jwDZ4LZD4N2NERk%2F%2BlR1KaRk2Jvo34HIXVnUqNWlYAR3TyV2intl8wwJWlgKQH6DI%2BzwOJ27kDToULG5TQpQk6xAQaToplmERCien7Pi8vlb0JNBCzkoKNh40Z1wPxcS%2BitdU0IkD0n39bvWy5uG0hoUuifHr53vaf7eqFRSdrd%2B%2BYuJ00yT%2FtWS6FLpLKCSgZw8GKoAq3PpfPggmg99bAju7H%2FD8xfVgBPhb91tEGCCdyub4jDtj6euoUFXK%2FiMIVg%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210324T193346Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=ASIA6OYT73R75HNE4VUO%2F20210324%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=e694954290d485482c6334b39b591c87e4a16ba2425f05da1dc25faf47afba2d" , "thumbnailUrl" : "https://s3.amazonaws.com/com.autodesk.oss-opsstaging-persistent/81/b8/3d/e2855b46af2060d595ce31923310079c4b/ce8edd30-ef28-467c-8d99-7d7051097ee0?response-content-disposition=attachment%3B%20filename%3D%22c35b8b28-859e-4256-a3bc-41772a673260_t.jpg%22&response-content-type=image%2Fjpeg&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCOKZyru7bEOWhRlJOiFZUwLwGSFSWPO5VknX%2BIisldAwIgWN6g5zYxXLOzdiZgR4sYuyY4qr1k1SAQOTOCI7EOmKIqvQMI3P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw5OTM3ODk5OTIwNjMiDK0wr6QcJBV%2BrqLz7iqRA55WGaeF1IZVyH5XzR%2FyR72VqyCRIEwm9D3Pt%2BTOxtaNa519ldQcvjYptWrlwnrgr1T9c3jxtEXxHZveX3XwgaSQq7JyHACBAMVwkKABwczEzPOryCvIJBWjgr2ABoYGr0dDCFdh9IjdoDrOrXDDesn4I5GamK%2BdNzXBR1MJH3ocmoZXxrmaJGigr62ShQ3q7AoqMgIX55XH8DnYMP4k9OlGGJsL7P80OnvOXfNLFl9EVJp5jnp%2BT1eO3FezRxc%2FqkeTG7t6QHh87P4cJKzWV9pW3AQoYvBKyQ5uJn5WA8%2FFg%2BhzYalr5Y%2B4%2FneB0xfn7WS2I%2FvjIo6rOkIqx7K3Ty1p1kuZ6e64%2BlEXx8mYHO2NOYobbSf%2Fx%2B7FU1rhZqvqUGB%2BRoMXFI%2FIkaxe%2B%2Ba6sZYV6Dm6bcim835asw%2B48vkt3XLZ6kBNqOJMdqvIBp%2F7opV9Bc4%2BMkhPc6wT%2BwAoQ0jHGuNZiLh%2BsxcB8EtwziI18v5LFw6WmffTQD3oc8WTb9xUZmoQ8qDq5z%2FY4%2BY2EAq6MNaP7oIGOusBXz4xrUPPH0cr5UO912gp6aysXFnqxu55it8zqPwiGI2Xe0RlaMTAMh1jwDZ4LZD4N2NERk%2F%2BlR1KaRk2Jvo34HIXVnUqNWlYAR3TyV2intl8wwJWlgKQH6DI%2BzwOJ27kDToULG5TQpQk6xAQaToplmERCien7Pi8vlb0JNBCzkoKNh40Z1wPxcS%2BitdU0IkD0n39bvWy5uG0hoUuifHr53vaf7eqFRSdrd%2B%2BYuJ00yT%2FtWS6FLpLKCSgZw8GKoAq3PpfPggmg99bAju7H%2FD8xfVgBPhb91tEGCCdyub4jDtj6euoUFXK%2FiMIVg%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210324T193346Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=ASIA6OYT73R75HNE4VUO%2F20210324%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=fac56130302305057c9ae301503860edb2d296c43dcfb5a59ebf3744f5126baa" }, "size" : 11359 , "takenAt" : "2021-03-13T18:15:00" , "title" : "Office Dry Wall" , "type" : "FIELD-REPORT" , "updatedAt" : "2021-03-14T11:20:33" , "updatedBy" : "PER8KQPK2JRT" , "urls" : { "fileUrl" : "https://developer.api.autodesk.com/construction/photos/assets/ce8edd30-ef28-467c-8d99-7d7051097ee0/c35b8b28-859e-4256-a3bc-41772a673260.jpg\"" , "thumbnailUrl" : "https://developer.api.autodesk.com/construction/photos/assets/ce8edd30-ef28-467c-8d99-7d7051097ee0/c35b8b28-859e-4256-a3bc-41772a673260_t.jpg\"" }, "userCreatedAt" : "2021-03-13T18:20:33" } ] }
```
