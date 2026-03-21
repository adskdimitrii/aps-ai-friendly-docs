# aec/graphql

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/graphqlendpoint/

---

GraphQL Endpoint

POST

# aec/graphql

Sends GraphQL requests to AEC Data Model GraphQL service and returns responses in the JSON format.

## [Resource Information](#resource-information)

| Method and URI | POST <https://developer.api.autodesk.com/aec/graphql> |
| --- | --- |
| Authentication Context | user context required |
| Required OAuth Scopes | `data:create` `data:read` `data:write` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <TOKEN>`, where `<TOKEN>` is an access token obtained by a [three-legged](../../oauth/how-to-docs/get-3-legged-token.md) OAuth flow. |
| --- | --- |
| Content-Type   string | Must be `application/json`. |
| Region   string | Determines the region where the request is sent. Default value is `US`. Possible values are: <br>**US** - (Default) Data center for the US region.**EMEA** - Data center for the Europe, Middle East, and Africa regions.**AUS** - Data center for the Australia region.**CAN** - Data center for the Canada region.**DEU** - Data center for the Germany region.**IND** - Data center for the India region.**JPN** - Data center for the Japan region.**GBR** - Data center for the United Kingdom region. |

* Required

### Request

## [Body Structure](#body-structure)

Request body to send a GraphQL query.

| query*   object | Contains the GraphQL query or mutation to send to the AEC Data Model service. |
| --- | --- |
| variables   object | Contains a set of key-value pairs, where the keys correspond to the names of the variables defined in your GraphQL query, and the values represent the values of those variables. |

* Required

## [Example 1](#example-1)

This example demonstrates how to use cURL to send a GraphQL query to the AEC Data Model service.

### Request

```
curl -v 'https://developer.api.autodesk.com/aec/graphql' \
-X 'POST' \
-H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a...' \
-H 'Content-Type: application/json' \
-d '{
      "query":"query GetProjects($hubId: String!) {
         projects(hubId: $hubId) {
          results {
            id
            name
          }
        }",
        "variables":{
          "hubId":"a.YnVzaW5lc3M6YXV0b2Rlc2syMDA2"
       }
    }'

```

Show More

### Response

```
{
   "data":{
      "projects":{
         "results":[
            {
               "id":"a.YnVzaW5lc3M6YXV0b2Rlc2syMDM5I0QyMDIyMDEzMTUwMzg3NDE5",
               "name":"Default Project"
            },
            {
               "id":"a.YnVzaW5lc3M6YXV0b2Rlc2syMDM5I0QyMDIyMDEzMTUwMzg3NDQ0",
               "name":"Admin Project"
            },
            {
               "id":"a.YnVzaW5lc3M6YXV0b2Rlc2syMDM5I0QyMDIyMDEzMTUwMzg3NDY5",
               "name":"Assets"
            }
         ]
      }
   }
}

```

Show More

## [Example 2](#example-2)

This example demonstrates how to use Axios in JavaScript to send a GraphQL query to the AEC Data Model service.

### Request

```
axios({
  method: 'POST',
  url: 'https://developer.api.autodesk.com/aec/graphql',
  data: {
    query: `{
      hubs {
        results {
          name
        }
      }
    }`
  }
})

```

Show More

**Note:** Axios automatically sets the `Content-Type` header to `application/json`.

### Response

```
{
 "data":{
    "hubs":{
       "results":[
          {
             "id":"a.YnVzaW5lc3M6YXV0b2Rlc2s2MTA0",
             "name":"L2-Forge-Data-Team"
          },
          {
             "id":"a.YnVzaW5lc3M6YXV0b2Rlc2s0NTA5",
             "name":"Michelangelo’s Playground"
          }
       ]
    }
 }
}

```

Show More

## [Example 3](#example-3)

This example demonstrates how to use send and receive http request and response in C# to the AEC Data Model service.

### Request

```
static async Task getHubs(){
var clientHandler = new HttpClientHandler();
var client = new HttpClient(clientHandler);
var request = new HttpRequestMessage
{
   Method = HttpMethod.Post,
   RequestUri = new Uri("https://developer.api.autodesk.com/aec/graphql"),
   Headers =
   {
      { "Authorization", "Bearer <<YOUR TOKEN HERE>>" }
   },
   Content = new StringContent(@"{""query"":""query GetHubs {hubs {pagination{cursor}results{name id}}}"",""variables"":{}}")
   {
      Headers =
      {
      ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue("application/json")
      }
   }
};
using (var response = await client.SendAsync(request))
{
   response.EnsureSuccessStatusCode();
   var body = await response.Content.ReadAsStringAsync();
   Console.WriteLine(body);
}
}

```

Show More

### Response

```
{
   "data":{
      "hubs":{
         "pagination":{
            "cursor":null
         },
         "results":[
            {
               "name":"JM Test",
               "id":"a.YnVzaW5lc3M6YXV0b2Rlc2s1ODcy"
            },
            {
               "name":"AEC Data Model Account",
               "id":"b.03f98b13-ec95-461b-b945-765f496165c1"
            },
            {
               "name":"Developer Advocacy Support",
               "id":"b.489c5e7a-c6c0-4212-81f3-3529a621210b"
            },
            {
               "name":"Construction Records Testing",
               "id":"b.768cae14-76b3-4531-9030-25212dab4e48"
            }
         ]
      }
   }
}

```

Show More
