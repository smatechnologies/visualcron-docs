---
sidebar_label: 'Task Dynamics CRM - Start Work Flow'
hide_title: 'true'
---

## Task Dynamics CRM - Start Work Flow

The Dynamics CRM - Start workflow Task starts an on-demand workflow in Dynamics CRM for a record, using a Dynamics CRM Connection.

![Start work flow tab with the Connection details, Entity name and Entity ID with their Fill buttons, and the Workflow list with its Fill button](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Dynamics%20CRM%20Tasks/Start%20work%20flow.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Start work flow tab

- _Connection_: in the _Connection details_ group, the Dynamics CRM Connection to use; see [Connection - Dynamics CRM](../../connection-dynamics-crm). Click the _Settings_ icon to open _Manage Connections_
- _Entity name_: the logical name of the entity (the record type), for example `account` or `contact`. Click _Fill_ to list the entities of the Dynamics CRM instance
- _Entity ID_: the ID of the record. Select an _Entity name_ first, then click _Fill_ to list the records of that entity
- _Workflow_: the workflow to start. Click _Fill_ to list the workflows. Only workflows of the type "on demand" are listed

Variables are not resolved in _Entity name_ and _Entity ID_.

### Output and errors

The output has the values that Dynamics CRM returns for the request, one `<name>|<value>` line each. When Dynamics CRM rejects the request, or the Connection cannot connect, the Task fails with the error that is returned.
