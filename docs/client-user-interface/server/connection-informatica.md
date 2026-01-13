---
sidebar_label: 'Connection - Informatica'
hide_title: 'true'
---

## Connection - Informatica

The Informatica Connection is used in the following place(s):
 
[Informatica Task](../../client-user-interface/server/job-tasks/informatica-tasks/run-job)

This Connection is used for Informatica - Run Job. This connection is for the cloud version only - this will not connect if Informatica is installed locally.

**Manage Connections > Add > Informatica> Common settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Informatica/Informatica.png)

**Name**

The unique name for the Connection

**Group**

The group that the connection is a part of
 
**Timeout**

The connection timeout in seconds. Connection will fail after this time period.
 
**Codepage**

Code page being used.
 
**Manage Connections > Add > IBM Cognos Analytics > Connection Settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Informatica/Settings.png)

**Address**

The address to the Informatica server. This should be set up in the following format: https://" & strAddress & "/ma/api/v2/user/login 

**Login**

Username for the service.
 
**Password**

Password for the service.