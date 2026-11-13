---
sidebar_label: 'Objects - Object Replace/Merge'
hide_title: 'true'
---

## Objects - Object Replace/Merge

The ***Object replace/merge*** tab of the ***Object finder*** window replaces every use of one object with another object of the same type. For example, to move many Jobs from an old Credential to a new one, select the old Credential as the source and the new one as the destination.

To open it, click ***Tools*** -> ***Objects*** -> ***Object relations*** or ***Object search***, then click the ***Object replace/merge*** tab.

![Object finder window on the Object replace/merge tab with source and destination objects selected](../../../static/img/Client%20User%20Interface/Main%20Menu/Tools/Objects/Object%20Replace%20-%20Merge.png)

:::warning

***Replace*** changes the objects on the Server at once; there is no confirmation. If you select the "No" entry of the type, for example "No Credential", as the destination, every object that uses the source loses that reference; for example, Tasks are left with no Credential. With _Merge source object into destination object_ checked, the source object is also deleted.

:::

### Source object

The object that is used now and that you want to replace.

- _Object type_: the type of object to replace
- _Object name_: the object to replace. The _Filter.._ field narrows the list
- _Count:_: how many objects use the source object, which is how many will change

### Merge source object into destination object

When checked, the source object is deleted after its uses are moved to the destination object. When unchecked, the uses are moved and the source object is kept.

:::warning

With _Merge source object into destination object_ checked, the source object is deleted from the Server. It can be re-created from its stored versions while its audit log entries are kept; see [Versions](audit-log-versions).

:::

### Destination object

The object that replaces the source object.

- _Object name_: the replacement object. The list starts with a "No" entry for the type, which removes the reference. The _Filter.._ field narrows the list. For some types, such as Connections, only compatible objects are listed
- _Count:_: how many objects use the destination object now

### Result grid

The grid lists the objects that use the source object and will change: _Object type_, _Name/Description_ and _Job name_. Double-click a row to open that object. The _Filter:_ field below the grid narrows the list.

### Replace

Click ***Replace*** to run the operation at once; there is no confirmation. A summary shows how many objects were updated. The source and destination object must be different.
