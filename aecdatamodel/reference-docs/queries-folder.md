# folder

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/queries/folder/

---

Queries

# folder

[](#)

Retrieve folder specified by the provided Id

**Template for Query:**

```
query GetFolder($projectId: ID!, $folderId: ID!) {
  folder(projectId: $projectId, folderId: $folderId) {
    # Folder Fields
  }
}

```

**Template for Query Variables:**

```
{
  "projectId" : "<SOME-ID-TYPE-SCALAR-VALUE>",
  "folderId" : "<SOME-ID-TYPE-SCALAR-VALUE>"
}

```

## [Arguments](#arguments)

| projectId*   [ID!](scalars.md) `non-null` | The ID of the project that contains the item. |
| --- | --- |
| folderId*   [ID!](scalars.md) `non-null` | The ID of the item to retrieve. |

* Required

## [Possible Returns](#possible-returns)

| Value Type | Description |
| --- | --- |
| [Folder](objects-folder.md) | Represents a folder. A folder is a location for storing files, data, and other folders (sub-folders). |

## [Examples](#examples)

### Example 1

Retrieves a folder by ID along with its sub folders.

**Query:**

```
query GetFolder($folderId: ID!) {
  folder (folderId: $folderId) {
    id
    name
    objectCount
    folders {
      results {
        id
        name
        objectCount
      }
    }
  }
}

```

Show More

**Query Variables:**

```
{
  "folderId": "Zm9sZH5iLmU0ZmJkMzE1LTJkYzUtNDAyNi04Y2EzLTgwZjA5ZDI0ZmY0Mn5iLjdhZGJmOWZkLWRlYmItNDI5Yy1iZmU1LTMyYTNjMjJjMDY5NX51cm46YWRzay53aXBzdGc6ZnMuZm9sZGVyOmNvLlhvSG9RY3pHUm9LczVZRm4yUDNpWlE"
}

```

**Response:**

```
{
  "data": {
    "folder": {
      "id": "Zm9sZH5iLmU0ZmJkMzE1LTJkYzUtNDAyNi04Y2EzLTgwZjA5ZDI0ZmY0Mn5iLjdhZGJmOWZkLWRlYmItNDI5Yy1iZmU1LTMyYTNjMjJjMDY5NX51cm46YWRzay53aXBzdGc6ZnMuZm9sZGVyOmNvLlhvSG9RY3pHUm9LczVZRm4yUDNpWlE",
      "name": "Project Files",
      "objectCount": 8,
      "folders": {
        "results": [
          {
            "id": "Zm9sZH5iLmU0ZmJkMzE1LTJkYzUtNDAyNi04Y2EzLTgwZjA5ZDI0ZmY0Mn5iLjdhZGJmOWZkLWRlYmItNDI5Yy1iZmU1LTMyYTNjMjJjMDY5NX51cm46YWRzay53aXBzdGc6ZnMuZm9sZGVyOmNvLnBRYjdZcVNlUjlXNTdldmVkZVdvQlE",
            "name": "Model",
            "objectCount": 22
          },
          {
            "id": "Zm9sZH5iLmU0ZmJkMzE1LTJkYzUtNDAyNi04Y2EzLTgwZjA5ZDI0ZmY0Mn5iLjdhZGJmOWZkLWRlYmItNDI5Yy1iZmU1LTMyYTNjMjJjMDY5NX51cm46YWRzay53aXBzdGc6ZnMuZm9sZGVyOmNvLkU1OENuck5pUTZDVW9PTG9Ja29QSUE",
            "name": "Small House",
            "objectCount": 1
          }
        ]
      }
    }
  }
}

```

Show More
