# propertyDefinitionCollectionsByHub

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/propertydefinitioncollectionsbyhub/

---

Queries

# propertyDefinitionCollectionsByHub

[](#)

Retrieves property definition collections from given hub.

**Template for Query:**

```
query GetPropertyDefinitionCollectionsByHub($hubId: ID!, $pagination: PaginationInput) {
  propertyDefinitionCollectionsByHub(hubId: $hubId, pagination: $pagination) {
    # PropertyDefinitionCollectionsByHub Fields
  }
}

```

**Template for Query Variables:**

```
{
  "hubId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "pagination" : "<SOME-PAGINATION-INPUT-TYPE-VALUE>"
}

```

## [Arguments](#arguments)

| hubId*   [ID!](scalars.md) `non-null` | Hub to retrieve property definition collections from. |
| --- | --- |
| pagination   [PaginationInput](inputs-paginationinput.md) | Specifies how to split the response into multiple pages. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [PropertyDefinitionCollections](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/propertydefinitioncollections/) | Contains a list of Property Definition Collections returned in response to a query. |

## [Examples](#examples)
