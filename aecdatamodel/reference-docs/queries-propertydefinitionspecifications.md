# propertyDefinitionSpecifications

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/propertydefinitionspecifications/

---

Queries

# propertyDefinitionSpecifications

[](#)

Retrieves property definition specifications that can be used for creating property definitions.

**Template for Query:**

```
query GetPropertyDefinitionSpecifications($pagination: PaginationInput) {
  propertyDefinitionSpecifications(pagination: $pagination) {
    # PropertyDefinitionSpecifications Fields
  }
}

```

**Template for Query Variables:**

```
{
  "pagination" : "<SOME-PAGINATION-INPUT-TYPE-VALUE>"
}

```

## [Arguments](#arguments)

| pagination   [PaginationInput](inputs-paginationinput.md) |  |
| --- | --- |

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [PropertyDefinitionSpecifications](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/objects/propertydefinitionspecifications/) | Contains a list of Property definition specifications |

## [Examples](#examples)
