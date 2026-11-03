---
sidebar_label: 'Task Sharepoint - Add List Item'
hide_title: 'true'
---
## Task SharePoint - Add List Item

The SharePoint - Add list item Task adds one item to an existing list on a SharePoint site, using a SharePoint Connection.

The SharePoint Tasks work with SharePoint 2010, 2013 and 2016 on premises, and with SharePoint Online.

![Add list item tab with the Connection, the Title list and the Field(s) grid](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Sharepoint%20Tasks/Add%20List%20item.png)

:::warning

This Task uses a SharePoint Connection; see [Connection - SharePoint](../../connection-sharepoint). When a certificate is selected in the Connection, the Task accepts any server certificate, and each run of a SharePoint Task changes TLS handling for the whole Server process.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Add list item tab

- _Connection_: the SharePoint Connection to use. The button next to the list manages Connections
- _Title_: the title of the list to add the item to. Click the button next to the box to show the lists of the site. Variables are not resolved in _Title_
- _Field(s)_: one row for each field of the list, with the columns _Use_, _Name_ and _Value_. Check _Use_ and enter a _Value_ for each field to set in the new item. Click _Refresh fields_ to fill the grid with the fields of the list in _Title_. Variables are resolved in _Name_ and _Value_

For a lookup field, enter the value of the looked-up column; the Task finds the matching item in the looked-up list. When no item there has that value, the field is left empty in the new item.

### Output and errors

The Task does not write output.

:::warning

When no list on the site has the title in _Title_, the Task adds nothing, and the Task reports success.

:::
