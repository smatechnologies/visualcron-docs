---
sidebar_label: 'Connection - IIS'
hide_title: 'true'
---

## Connection - IIS

The IIS Connection stores connect and logon properties for local or remote Internet Information Services (IIS) servers.

The IIS Connection is used in the following Tasks:

* [IIS - Add Website](../../client-user-interface/server/job-tasks/iis-tasks/add-website)
* [IIS - Add Application Pool](../../client-user-interface/server/job-tasks/iis-tasks/add-application-pool)
* [IIS - Add Website Application](../../client-user-interface/server/job-tasks/iis-tasks/add-website-application)
* [IIS - Add App Virtual Directory](../../client-user-interface/server/job-tasks/iis-tasks/add-app-virtual-directory)
* [IIS - Change Website State](../../client-user-interface/server/job-tasks/iis-tasks/change-website-state)
* [IIS - Change Application Pool State](../../client-user-interface/server/job-tasks/iis-tasks/change-application-pool-state)
* [IIS - Delete Website](../../client-user-interface/server/job-tasks/iis-tasks/delete-website)
* [IIS - Delete Application Pool](../../client-user-interface/server/job-tasks/iis-tasks/delete-application-pool)
* [IIS - Delete Website Application](../../client-user-interface/server/job-tasks/iis-tasks/delete-website-application)
* [IIS - Delete App Virtual Directory](../../client-user-interface/server/job-tasks/iis-tasks/delete-app-virtual-directory)
* [IIS - Is Application Pool Exists](../../client-user-interface/server/job-tasks/iis-tasks/is-application-pool-exists)

**Manage Connections > Add > IIS > Common settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/IIS/IIS.png)

**Name**

The name of the Connection to uniquely identify it.

**Group**

The group that the connection is a part of.

**Timeout**

The connection timeout in seconds. Connection will fail after this time period.

**Code page**

Code page being used.

**Manage Connections > Add > IIS > Connection settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/IIS/Settings.png)

**Address**

The host name or IP address of the IIS server. Use *localhost* to manage the local IIS instance.

**Username**

The user name used to authenticate against the IIS server. Required when connecting to a remote IIS server.

**Password**

The password used to authenticate against the IIS server. Required when connecting to a remote IIS server.
