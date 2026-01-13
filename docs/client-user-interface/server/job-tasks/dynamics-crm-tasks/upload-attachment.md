---
sidebar_label: 'Task Dynamics CRM - Upload Attachments'
hide_title: 'true'
---

## Task Dynamics CRM - Upload Attachments

The Dynamics CRM - Upload attachment Task uploads one or more attachments to a Dynamics CRM instance.
 
**Upload attachment > Main settings** tab

[](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Dynamics%20CRM%20Tasks/upload%20attachments.png)

**Connection**

To use Dynamics CRM Tasks you need to create a [Connection](../../global-connections) first. Click the *Settings* icon to open the *Manage Connections* dialog.
 
**Entity name**

The logical name of the entity to get information from. Click the *Fill* button to list existing Entities in the Dynamics CRM instance.
 
**Entity Id**

Click the *Fill* button to list existing Entity Id's based on the selected Entity.
 
**Mime type**

Enter the mime type of the file(s) you are uploading if the *Auto detect* option does not work for you.
 
**Upload attachment > File filter > Location** sub tab

This Task uses the standard VisualCron [File filter](../../job-tasks-file-filter) to define the properties of the listed files.