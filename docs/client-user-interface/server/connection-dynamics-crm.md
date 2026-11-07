---
sidebar_label: 'Connection - Dynamics CRM'
hide_title: 'true'
---

## Connection - Dynamics CRM

The Dynamics CRM Connection stores the address, sign-in and security settings that the following Dynamics CRM Tasks use to connect to a Microsoft Dynamics CRM organization:

- [Dynamics CRM - Get entity](job-tasks/dynamics-crm-tasks/get-entity)
- [Dynamics CRM - Create entity](job-tasks/dynamics-crm-tasks/create-entity)
- [Dynamics CRM - Update entity](job-tasks/dynamics-crm-tasks/update-entity)
- [Dynamics CRM - Delete entity](job-tasks/dynamics-crm-tasks/delete-entity)
- [Dynamics CRM - List entity](job-tasks/dynamics-crm-tasks/list-entity)
- [Dynamics CRM - Get audit data](job-tasks/dynamics-crm-tasks/get-audit-data)
- [Dynamics CRM - Set audit status](job-tasks/dynamics-crm-tasks/set-audit-status)
- [Dynamics CRM - Start work flow](job-tasks/dynamics-crm-tasks/start-work-flow)
- [Dynamics CRM - Download attachment](job-tasks/dynamics-crm-tasks/download-attachments)
- [Dynamics CRM - Upload attachment](job-tasks/dynamics-crm-tasks/upload-attachment)
- [Dynamics CRM - Delete attachment](job-tasks/dynamics-crm-tasks/delete-attachment)
 
### Common settings

![Dynamics CRM Connection, Common settings tab with the Test button](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Dynamics%20CRM/Dynamics%20CRM.png)

The ***Common settings*** tab is the same for every Connection type that has it; see [Common settings](global-connections#common-settings).

For a Dynamics CRM Connection, _Timeout_ and _Code page_ are not used. _Test_ runs on the Server. It connects with _Address_, _Username_ and _Password_ and reads the list of entities. If the test fails, the message shows the error and a suggested address format.
 
### Main settings

![Dynamics CRM Connection, Main settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Dynamics%20CRM/Settings.png)

These fields are on ***Connection settings*** -> ***Main settings***. _Address_ and _Username_ are required.

- _Address_: the full URL of the Dynamics CRM organization, including `https://` or `http://`. For an on-premises server, include the port if it is not the default, and the organization name, for example `http://<server>:<port>/<orgname>`

**Username**

The user name for the Dynamics CRM server.
 
**Password**

The password for the Dynamics CRM server.
