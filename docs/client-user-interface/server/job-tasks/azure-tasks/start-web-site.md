---
sidebar_label: 'Task Azure - Start Web Site'
hide_title: 'true'
---

## Task Azure - Start Web Site

The Azure - Start Web Site Task starts an existing web site in Azure, using a Microsoft Azure Connection.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Azure - Start web site tab

![Azure - Start web site tab with the Connection list and the Web site list with its Refresh button](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Azure%20Tasks/Start%20Web%20Site.png)

- _Connection_: the Microsoft Azure Connection to use; see [Connection - Microsoft Azure](../../connection-microsoft-azure). Click the _Settings_ icon to open _Manage Connections_
- _Web site_: the name of the Azure web site. Click _Refresh_ to fill the list

### Output and errors

The Task writes no output. When Azure returns an error, the Task fails.

:::warning

When the selected Connection no longer exists, the Task does nothing, writes no output, and the Task reports success.

:::
