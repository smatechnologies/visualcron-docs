---
sidebar_label: 'Task Azure - Create Web Site'
hide_title: 'true'
---

## Task Azure - Create Web Site

The Azure - Create Web Site Task is meant to create a web site in Azure, using a Microsoft Azure Connection.

:::warning

The Task does not create the web site: it sends no request to Azure, writes no output, and the Task reports success. Create the web site in the Azure portal.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Azure - Create web site tab

![Azure - Create web site tab with the Connection list, Hosting plan name, Site name, and Geo region with its Refresh button](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Azure%20Tasks/Create%20Web%20site.png)

- _Connection_: the Microsoft Azure Connection to use; see [Connection - Microsoft Azure](../../connection-microsoft-azure). Click the _Settings_ icon to open _Manage Connections_
- _Hosting plan name_: the name of the hosting plan for the web site
- _Site name_: the name of the new web site
- _Geo region_: the Azure region for the web site. Click _Refresh_ to fill the list
