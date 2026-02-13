---
sidebar_label: 'Connection - Box'
hide_title: 'true'
---

## Connection - Box

The Box Connection stores connect and logon properties for the Box cloud services.
 
Box is a cloud service from Google that you have to pay for. You can use VisualCron to sync files between that service and a local folder.
 
The GoogleDrive Connection is used in the Cloud Tasks:

* [Cloud - Upload file(s)](../../client-user-interface/server/job-tasks/cloud-transfer-tasks/upload-file)
* [Cloud - List item(s)](../../client-user-interface/server/job-tasks/cloud-transfer-tasks/list-item)
* [Cloud - Download file(s)](../../client-user-interface/server/job-tasks/cloud-transfer-tasks/download-file)
* [Cloud - Create folder](../../client-user-interface/server/job-tasks/cloud-transfer-tasks/create-folder)
* [Cloud - Delete item(s)](../../client-user-interface/server/job-tasks/cloud-transfer-tasks/delete-item)
 
**Manage Connections > Add > Box > Common settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Box/Box.png)

**Name**

The name of the Connection to uniquely identifying it.

**Group**

The group that the connection is a part of
 
**Timeout**

The connection timeout in seconds. Connection will fail after this time period.
 
**Code page**

Code page being used.
 
**Manage Connections > Add > Box > Connection Settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Box/Settings.png)

**Client Id**

Client Id which you gets when registering application at [Box](https://www.box.com/platform). See sample below:

![](../../../static/img/boxoacredentials.png)

**Client secret**

Client secret which you gets when registering application at [Box](https://www.box.com/platform).

**Redirect Url**

Please note that this url need to match url on Box web site like this:

![](../../../static/img/boxredirecturi.png)

**Authenticate**

Click on the Authenticate link to start authentication.