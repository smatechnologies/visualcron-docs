---
sidebar_label: 'Task IIS - Add Website Application'
hide_title: 'true'
---

## Task IIS - Add Website Application

The IIS - Add Website Application Task creates an application in an existing website, in the IIS of the VisualCron Server computer, using an IIS Connection. An application is a group of web content that is reached through a URL path of the website.

![IIS - Add a new application Task settings, with the Connection, Application parameters and Virtual directory parameters groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Add%20a%20new%20application.png)

:::warning

This Task uses an IIS Connection; see [Connection - IIS](../../connection-iis). The Task always works on the IIS of the VisualCron Server computer: the Connection's _Address_ is not used, and the changes are made as the account of the VisualCron Server service, which must be allowed to change IIS. The Connection's _Username_ and _Password_ are used only for network access.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### IIS - Add a new application tab

- _Connection_: the IIS Connection. Required. Click the _Settings_ icon to open _Manage Connections_
- _Site name_ (_Application parameters_ group): the name of the website. Click the _Refresh_ icon to list the websites of the VisualCron Server computer. The name must match exactly, including case
- _Application url_: the path of the new application in the website, for example "/myapp"
- _App pool name_: the application pool of the application. Required. Click the _Refresh_ icon to list the application pools of the VisualCron Server computer
- _Enabled protocols_: the protocols enabled for the application, separated by commas, for example "http,https". When empty, the IIS default is used
- _Path_ (_Virtual directory parameters_ group): the physical folder of the application root. Click the _Browse_ icon to select a folder
- _Logon method_: how IIS logs on with the user in _Credential_ to reach the folder: "Interactive", "Batch", "Network" or "Clear text". When empty, the IIS default is used
- _Credential_: the user that IIS uses to reach the folder. The Task writes the Credential's user name and password into the IIS configuration of the application. When no Credential is selected, the IIS default is used. Click the _Settings_ icon to open _Manage credentials_; see [Global - Credentials](../../global-credentials)

:::warning

The Task copies the user name and password of the selected _Credential_ into the IIS configuration of the application. IIS keeps its own copy: changing or deleting the Credential in VisualCron later does not change IIS.

:::

### Output and errors

On success, the output is "Success". When the website is not found, the Task does nothing and writes no output, and the Task reports success.

The ***TimeOut*** tab does not stop this Task.
