# User

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/user/

---

Objects

# User

[](#)

An object representing a User.

## [Fields](#fields)

| id*   [ID!](scalars.md) `non-null` | The ID that uniquely identifies the User. |
| --- | --- |
| userName   [String](scalars.md) | The display name of the user. |
| firstName   [String](scalars.md) | The user’s first name. |
| lastName   [String](scalars.md) | The user’s last name. |
| email   [String](scalars.md) | The user’s email address. |
| lastModifiedOn   [DateTime](scalars.md) | The date and time the user’s information was last modified. |
| createdOn   [DateTime](scalars.md) | The date and time the user’s information was created. |

* Required

## [Where Used](#where-used)

| Usage | Used By | Description |
| --- | --- | --- |
| Field Of | [Element](objects-element.md) | Represents an element type. |
| Field Of | [Elementgroup](objects-elementgroup.md) | Represents a Revit model. |
| Field Of | [Elementgroupversion](objects-elementgroupversion.md) | Represents a single version of an ElementGroup. |
| Field Of | [Folder](objects-folder.md) | Represents a folder. A folder is a location for storing files, data, and other folders (sub-folders). |
