# propertyDefinitionCollection

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/propertydefinitioncollection/

---

Queries

# propertyDefinitionCollection

[](#)

Retrieves property definition collection using given ID.

**Template for Query:**

```
query GetPropertyDefinitionCollection($propertyDefinitionCollectionId: ID!) {
  propertyDefinitionCollection(propertyDefinitionCollectionId: $propertyDefinitionCollectionId) {
    # PropertyDefinitionCollection Fields
  }
}

```

**Template for Query Variables:**

```
{
  "propertyDefinitionCollectionId" : "<SOME-ID-TYPE-SCALAR-VALUE>"
}

```

## [Arguments](#arguments)

| propertyDefinitionCollectionId*   [ID!](scalars.md) `non-null` | Property definition collection to retrieve. |
| --- | --- |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [PropertyDefinitionCollection](objects-propertydefinitioncollection.md) | Data object that represents property definition collection. |

## [Examples](#examples)
