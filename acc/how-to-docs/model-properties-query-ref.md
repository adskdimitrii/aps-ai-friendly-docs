# Model Property Service Query Language Reference

Source: https://aps.autodesk.com/en/docs/acc/tutorials/model-properties/query-ref/

---

# Model Property Service Query Language Reference

The indexing service is implemented using JSON table scans. Property data from the models specified in the index manifest are extracted and stored as compressed line delimited JSON by the service. Each row in the file represents a row extracted from the underlying SVF PDB (Property Database) files created as part of the SVF file conversions process. When queries are issued to the indexing service, the workflow takes the JSON query expression passed by the client, translates it to SQL-like expression, and applies it line-by-line to each row in the index (table scan). Where rows match the expression, they are written to a cached, compressed, results JSON file, honoring any column restrictions that were passed with the query filter expression.

## [Basic Query Body Structure](#basic-query-body-structure)
> Whether a query targets a basic index or the more complex diff index, the format of the query body passed to the service remains constant.

```
{
    "columns": <columns>,
    "query": <conditions>
}

```

There is a columns property that allows the `columns`, or projections, returned by the service to be restricted. If this property is `null`, this is equivalent to a `SELECT *` in SQL terms. The second property, `query` carries the query filter expression applied to the each row in the index and is equivalent to a `WHERE` clause in SQL.

### `<columns>`

The following column specification

```
{
    "columns":
    {
        "alias1": <expression1>,
        "column2": true
    }
}

```

is equivalent to the following SQL expression

```
SELECT <expression1> AS alias1, column2 FROM ...

```

and would yield a result with the following JSON schema.

```
{
    "alias1": <value>,
    "column2": <value>
}

```

### `<conditions>`

The `query` property consists of a set of conditions that can be combined with `AND` and `OR` semantics. The following table summarizes the various conditions supported by the service. Conditions can contain embedded expressions.

| Condition | Yields |
| --- | --- |
| `[ <condition1>, <condition2>, ... ]` | `<condition1> OR <condition2> OR ...` |
| `{ "<property1>": <expression1>, "<property2>": <expression2>, ... }` | `(<property1> = <expression1> AND <property2> = <expression2> AND ...)` |
| `{ "$not": <condition> }` | `NOT <condition>` |
| `{ "$and": [ <condition1>, <condition2>, ... ]}` | `(<condition1> AND <condition2> AND ...)` |
| `{ "$or": [ <condition1>, <condition2>, ... ]}` | `(<condition1> OR <condition2> OR ...)` |
| `{ "$lt": [ <expression1>, <expression2> ] }` | `(<expression1> < <expression2>)` |
| `{ "$le": [ <expression1>, <expression2> ] }` | `(<expression1> <= <expression2>)` |
| `{ "$eq": [ <expression1>, <expression2> ] }` | `(<expression1> = <expression2>)` |
| `{ "$ne": [ <expression1>, <expression2> ] }` | `(<expression1> != <expression2>)` |
| `{ "$ge": [ <expression1>, <expression2> ] }` | `(<expression1> => <expression2>)` |
| `{ "$gt": [ <expression1>, <expression2> ] }` | `(<expression1> > <expression2>)` |
| `{ "$like": [ <expression1>, <expression2> ] }` | `(<expression1> LIKE <expression2>)` |
| `{ "$between": [ <expression1>, <expression2>, <expression3> ] }` | `(<expression1> BETWEEN <expression2> AND <expression3>)` |
| `{ "$between": { "<propertyName>": [<expression2>, <expression3> ]} }` | `(<propertyName> BETWEEN <expression2> AND <expression3>)` |
| `{ "$in": [ <expression1>, <expression2>, <expression3>, ... ] }` | `(<expression1> IN (<expression2>, <expression3>, ...))` |
| `{ "$in": { <propertyName>: [<expression2>, <expression3>, ... ] } }` | `(<propertyName> IN (<expression2>, <expression3>, ...))` |
| `{ "$contains": [ "<propertyName>", <expression> ] }` | `(<expression> IN <propertyName>)` |
| `{ "$isnull": <expression> }` | `(<expression> IS NULL)` |
| `{ "$notnull": <expression> }` | `(<expression> IS NOT NULL)` |

### `<expression>`

The following `<expression>` are supported by the service:

| Expression | Yields |
| --- | --- |
| `{ "$neg": <expression> }` | `-(<expression>)` |
| `{ "$add": [ <expression1>, <expression2>, ... ]}` | `(<expression1> + <expression2> + ...)` |
| `{ "$sub": [ <expression1>, <expression2>, ... ]}` | `(<expression1> - <expression2> - ...)` |
| `{ "$mul": [ <expression1>, <expression2>, ... ]}` | `(<expression1> * <expression2> * ...)` |
| `{ "$div": [ <expression1>, <expression2>, ... ]}` | `(<expression1> / <expression2> / ...)` |
| `{ "$cat": [ <expression1>, <expression2>, ... ]}` | `(<expression1> || <expression2> ||  ...)` |
| `{ "$coalesce": [ <expression1>, <expression2>, ... ]}` | `COALESCE(<expression1>, <expression2>, ...)` |
| `{ "$mod": [ <expression1>, <expression2> ]}` | `(<expression1> % <expression2>)` |
| `{ "$cast": [ <expression1>, <expression2> ]}` | `(CAST <expression1> AS <expression2>)` |
| `{ "$nullif": [ <expression1>, <expression2> ]}` | `NULLIF(<expression1>, <expression2>)` |
| `{ "$date_add": [ <expression1>, <expression2>, <expression3> ]}` | `DATE_ADD(<expression1>, <expression2>, <expression3>)` |
| `{ "$date_diff": [ <expression1>, <expression2>, <expression3> ]}` | `DATE_DIFF(<expression1>, <expression2>, <expression3>)` |
| `{ "$extract": [ <expression1>, <expression2> ]}` | `EXTRACT(<expression1> FROM <expression2>)` |
| `{ "$substring": [ <expression1>, <expression2> ]}` | `SUBSTRING(<expression1> FROM <expression2>)` |
| `{ "$substring": [ <expression1>, <expression2>, <expression3> ]}` | `SUBSTRING(<expression1> FROM <expression2> FOR <expression3>)` |
| `{ "$to_string": <expression> }` | `TO_STRING(<expression>)` |
| `{ "$to_timestamp": <expression> }` | `TO_TIMESTAMP(<expression>)` |
| `{ "$char_length": <expression> }` | `CHAR_LENGTH(<expression>)` |
| `{ "$lower": <expression> }` | `LOWER(<expression>)` |
| `{ "$upper": <expression> }` | `UPPER(<expression>)` |
| `{ "$count": <expression> }` | `COUNT(<expression>)` |
| `{ "$sum": <expression> }` | `SUM(<expression>)` |
| `{ "$avg": <expression> }` | `AVG(<expression>)` |
| `{ "$min": <expression> }` | `MIN(<expression>)` |
| `{ "$max": <expression> }` | `MAX(<expression>)` |
| `{ "$trim": <expression> }` | `TRIM(<expression>)` |
| `{ "$trim": [<expression1>, <expression2> }` | `TRIM(<expression1> FROM <expression2>)` |
| `{ "$trim": [<"LEADING"|"TRAILING"|"BOTH">, <expression1>, <expression2> }` | `TRIM(<LEADING|TRAILING|BOTH> <expression1> FROM <expression2>)` |
| `{ "$utcnow": true }` | `UTCNOW()` |
| `{ "$case: [ <expression1>, { "$when": <expression2>, "$then": <expression3>}, ... {"$else": <expression4>}] }` | `CASE <expression1> WHEN <expression2> THEN <expression3> ... ELSE <expression4> END` |
| `{ "$case: [ { "$when": <condition1>, "$then": <expression1>}, ... {"$else": <expression2>}] }` | `CASE WHEN <condition> THEN <expression1> ... ELSE <expression2> END` |
| `<number|boolean|string>` | `<number|boolean|string>` |

### String Escaping

SQL string constants have to be single quoted, i.e. `"'Hello'"` is the constant `'Hello'`. Unquoted strings either denote properties (e.g. `"s.p123"`) or keywords (e.g. `"LEADING"`).

## [Query by Example](#query-by-example)

### Get Revit Classification with Column Transform

See the following fields.

```
// Viewer element display name field
{"key":"p153cb174","category":"__name__","type":"String","name":"name","uom":null}
// Revit category name field
{"key":"p20d8441e","category":"__category__","type":"String","name":"_RC","uom":null}
// Revit family name field
{"key":"p30db51f9","category":"__category__","type":"String","name":"_RFN","uom":null}
// Revit type name field
{"key":"p13b6b3a0","category":"__category__","type":"String","name":"_RFT","uom":null}

```

Show More

This example query uses the `$and` expression, combined with `$notnull` and a `$gt`, to filter rows where the views array has a `$count` greater than 0 and the row has a Revit classification.

```
{
    "query": {
        "$and": [
            { "$notnull": "s.props.p20d8441e" },
            { "$notnull": "s.props.p30db51f9" },
            { "$notnull": "s.props.p13b6b3a0" },
            { "$gt": [{ "$count": "s.views" }, 0] }
        ]
    },
    "columns": {
        "s.svf2Id": true,
        "lmvName": "s.props.p153cb174",
        "revitCategory": "s.props.p20d8441e",
        "revitFamily": "s.props.p30db51f9",
        "revitType": "s.props.p13b6b3a0",
        "s.views": true
    }
}

```

Show More

This is equivalent to the following S3 SQL:

```
select
    s.svf2Id,
    s.props.p153cb174 as lmvName,
    s.props.p20d8441e as revitCategory,
    s.props.p30db51f9 as revitFamily,
    s.props.p13b6b3a0 as revitType,
    s.views
from S3Object[*] s
where
    s.props.p20d8441e is not null and
    s.props.p30db51f9 is not null and
    s.props.p13b6b3a0 is not null and
    count(s.views) > 0

```

Show More

### Fuzzy string matching with a dimension constraint

See the following fields.

```
{"key":"p6637df3c","category":"Materials and Finishes","type":"String","name":"Structural Material","uom":null}
{"key":"p69a0daab","category":"Dimensions","type":"Double","name":"Ht","uom":"ft"}

```

This example query uses the `$like` expression combined with `%` wildcard matching to find rows with a structural material description containing âsteelâ that has a Ht dimension of more than 0.5 feet.

```
{
    "query":
    {
        "$and": [
            {
                "$or": [
                    { "$like": ["s.props.p6637df3c", "'%Steel%'"] },
                    { "$like": ["s.props.p6637df3c", "'%steel%'"] }
                ]
            },
            {
                "$ge": ["s.props.p69a0daab", 0.5]
            }
        ]
    }
}

```

Show More

This is equivalent to the following S3 SQL:

```
select s.*
from S3Object[*] s
where
    s.props.p69a0daab >= 0.5 and
    (s.props.p6637df3c like '%Steel%' or s.props.p6637df3c like '%steel%')

```

### Find more examples and sample applications on APS Github

![../../../_images/git-hub-octocat-200px.png](../../../_images/git-hub-octocat-200px.png)

Sample models, an extensive set of examples queries and set of PowerShell helper scripts which can be used to test the API are available on APS Github <https://github.com/autodesk-platform-services/aps-model-properties.powershell>
