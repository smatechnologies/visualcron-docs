---
sidebar_label: 'Task Sharepoint - Get List'
hide_title: 'true'
---
## Task SharePoint - Get List

The SharePoint - Get list(s) Task returns the titles of all lists on a SharePoint site, using a SharePoint Connection.

The SharePoint Tasks work with SharePoint 2010, 2013 and 2016 on premises, and with SharePoint Online.

![Get list(s) tab with the Connection](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Sharepoint%20Tasks/Get%20Lists.png)

:::warning

This Task uses a SharePoint Connection; see [Connection - SharePoint](../../connection-sharepoint). When a certificate is selected in the Connection, the Task accepts any server certificate, and each run of a SharePoint Task changes TLS handling for the whole Server process.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Get list(s) tab

- _Connection_: the SharePoint Connection to use. The button next to the list manages Connections

### Output and errors

The output of the Task is the title of each list on the site, one per line, including lists that SharePoint hides from the site navigation.
