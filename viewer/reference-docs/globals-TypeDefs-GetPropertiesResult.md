# GetPropertiesResult

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/globals/TypeDefs/GetPropertiesResult/

---

Type Definitions

# GetPropertiesResult

Object with properties associated with a dbId.

# Properties

| dbId   number | the id passed into [getProperties](Viewing-Model.md#getProperties/) function. |
| --- | --- |
| externalId   string | an identifier that can be used in the un-translated version of the model. Can be used for desktop application integrations. |
| name   string | The element’s name. |
| properties   Array.<PropertyResult> | list of associated properties |
