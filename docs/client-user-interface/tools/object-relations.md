---
sidebar_label: 'Objects - Object Relations'
hide_title: 'true'
---

## Objects - Object Relations

The ***Object relations*** tab of the ***Object finder*** window shows where an object is used. Many objects, such as Connections, Credentials and Notifications, can be used by many Jobs and Tasks, so check their relations before you delete or change them.

To open it, click ***Tools*** -> ***Objects*** -> ***Object relations***, or right-click an object and click ***Object relations***.

![Object finder window on the Object relations tab, showing a Notification and the Job that uses it](../../../static/img/Client%20User%20Interface/Main%20Menu/Tools/Objects/Object%20Relations.png)

- _Object type_: the type of object to look up. The names of all objects of that type are listed in _Object name_
- _Object name_: the object to look up. The _Filter.._ field narrows the list. When an object is selected, every object that uses it is listed in the grid
- Result grid: _Type_, _Job name_ and _Name/Description_ of each object that uses the selected object. Double-click a row to edit that object. The _Filter:_ field below the grid narrows the list

The ***Object finder*** window also has the ***Object text search/replace*** tab, see [Objects - Object Search](object-search), and the ***Object replace/merge*** tab, see [Objects - Object Replace/Merge](object-replace-merge).
