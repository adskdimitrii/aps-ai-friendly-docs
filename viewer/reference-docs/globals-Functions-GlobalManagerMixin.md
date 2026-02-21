# GlobalManagerMixin

Source: https://aps.autodesk.com/en/docs/viewer/v7/reference/globals/Functions/GlobalManagerMixin/

---

Functions

# GlobalManagerMixin

Adds the GlobalManagerProvider methods to the prototype of another class.

This function can be used to add the GlobalManagerProvider functionality to a class without directly inheriting from the GlobalManagerProvider class. The downside will be that there will not be correct type information for the globalManager property.

It is mainly provided for backwards compatibility because this pattern is used in all existing extensions. Where possible, prefer to inherit from the GlobalManagerProvider class.
