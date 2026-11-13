---
sidebar_label: 'Task Sharepoint - Update List Item'
hide_title: 'true'
---
## Task SharePoint - Update List Item

The SharePoint - Update list item Task changes the values of fields in one item of a list on a SharePoint site, using a SharePoint Connection.

The SharePoint Tasks work with SharePoint 2010, 2013 and 2016 on premises, and with SharePoint Online.

![Update list item tab with the Connection, the List item Id (full path) box and the Field(s) grid](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Sharepoint%20Tasks/Update%20List%20Item.png)

:::warning

This Task uses a SharePoint Connection; see [Connection - SharePoint](../../connection-sharepoint). When a certificate is selected in the Connection, the Task accepts any server certificate, and each run of a SharePoint Task changes TLS handling for the whole Server process.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Update list item tab

- _Connection_: the SharePoint Connection to use. The button next to the list manages Connections
- _List item Id (full path)_: the item to update, as a path that ends with the title of the list and the ID of the item, as in `<list title>/<item ID>`. The button next to the box opens a browser of the site to select the item. The list is found by the next-to-last part of the path, so that part must be the title of the list
- _Field(s)_: one row for each field of the list, with the columns _Use_, _Name_ and _Value_. Check _Use_ and enter a _Value_ for each field to change. Fields that are not checked keep their values. Click _Refresh fields_ to fill the grid with the fields of the list of the item

Variables are resolved in _List item Id (full path)_, _Name_ and _Value_.

### Output and errors

The Task does not write output. When the list, the item or a field does not exist, the Task fails with the error from SharePoint.
