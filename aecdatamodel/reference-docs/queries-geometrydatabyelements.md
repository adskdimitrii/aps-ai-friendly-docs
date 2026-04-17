# geometryDataByElements

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/geometrydatabyelements/

---

Queries

# geometryDataByElements

[](#)

Retrieves geometry data for given elements.

**Template for Query:**

```
query GetGeometryDataByElements($elementIds: [ID!]) {
  geometryDataByElements(elementIds: $elementIds) {
    # GeometryDataByElements Fields
  }
}

```

**Template for Query Variables:**

```
{
  "elementIds" : "<SOME-[ID!]-TYPE-SCALAR-VALUE>"
}

```

## [Arguments](#arguments)

| elementIds   [[ID!]](/en/docs/aecdatamodel/v1/reference/scalars) | Elements to retrieve Geometry Data from. |
| --- | --- |

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [GeometryDataResponse](objects-geometrydataresponse.md) | Represents the response for geometry data requests, including geometry data for elements and download information. |
