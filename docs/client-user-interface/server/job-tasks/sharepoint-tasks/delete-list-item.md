---
sidebar_label: 'Task Sharepoint - Delete List Item'
hide_title: 'true'
---
## Task SharePoint - Delete List Item

The SharePoint - Delete list item(s) Task deletes one item from a list on a SharePoint site, using a SharePoint Connection.

The SharePoint Tasks work with SharePoint 2010, 2013 and 2016 on premises, and with SharePoint Online.

![Delete list item(s) tab with the Connection and the List item Id (full path) box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Sharepoint%20Tasks/delete%20list%20items.png)

:::warning

This Task uses a SharePoint Connection; see [Connection - SharePoint](../../connection-sharepoint). When a certificate is selected in the Connection, the Task accepts any server certificate, and each run of a SharePoint Task changes TLS handling for the whole Server process.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Delete list item(s) tab

- _Connection_: the SharePoint Connection to use. The button next to the list manages Connections
- _List item Id (full path)_: the item to delete, as a path that ends with the title of the list and the ID of the item, as in `<list title>/<item ID>`. The button next to the box opens a browser of the site to select the item. Variables are resolved

The list is found by the next-to-last part of the path, so that part must be the title of the list.

### Output and errors

The Task does not write output. When the list or the item does not exist, the Task fails with the error from SharePoint.

:::warning

The Task deletes the item at _List item Id (full path)_ without a prompt. Check the value before the Task runs.

:::
