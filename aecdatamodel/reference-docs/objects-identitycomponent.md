# IdentityComponent

Source: https://aps.autodesk.com/en/docs/aecdatamodel/reference/objects/identitycomponent/

---

Objects

# IdentityComponent

[](#)

Component that contains identity information of an entity

## [Fields](#fields)

| componentType*   [ComponentType!](objects-componenttype.md) `non-null` | Type of the component |
| --- | --- |
| name*   [String!](scalars.md) `non-null` | The human-readable name of the entity |
| createdBy   [User](objects-user.md) | User responsible for creating this entity |
| createdOn   [DateTime](scalars.md) | Timestamp of entity creation |
| lastModifiedBy   [User](objects-user.md) | Latest user who modified the data |
| lastModifiedOn   [DateTime](scalars.md) | Latest timestamp when the entity was modified |

* Required

## [Implements](#implements)

| Usage | Used By | Description |
| --- | --- | --- |
| Interface | [ECSComponent](https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/interfaces/ecscomponent/) | Represents a component |
