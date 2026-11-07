---
sidebar_label: 'Task Sharepoint - Delete List'
hide_title: 'true'
---
## Task SharePoint - Delete List

The SharePoint - Delete list(s) Task deletes a list, with all its items, from a SharePoint site, using a SharePoint Connection.

The SharePoint Tasks work with SharePoint 2010, 2013 and 2016 on premises, and with SharePoint Online.

![Delete list(s) tab with the Connection and the Title list](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Sharepoint%20Tasks/Delete%20Lists.png)

:::warning

This Task uses a SharePoint Connection; see [Connection - SharePoint](../../connection-sharepoint). When a certificate is selected in the Connection, the Task accepts any server certificate, and each run of a SharePoint Task changes TLS handling for the whole Server process.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Delete list(s) tab

- _Connection_: the SharePoint Connection to use. The button next to the list manages Connections
- _Title_: the exact title of the list to delete. Wildcards are not supported, so one Task deletes one list. Click the button next to the box to show the lists of the site. Variables are resolved

### Output and errors

The Task does not write output. When no list has the title, the Task fails with the error from SharePoint.

:::warning

The Task deletes the list and all its items without a prompt. Check _Title_ before the Task runs.

:::
