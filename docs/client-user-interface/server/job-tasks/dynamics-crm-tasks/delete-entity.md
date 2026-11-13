---
sidebar_label: 'Task Dynamics CRM - Delete Entity'
hide_title: 'true'
---

## Task Dynamics CRM - Delete Entity

The Dynamics CRM - Delete Entity Task deletes a record of an entity in Dynamics CRM, using a Dynamics CRM Connection.

![Delete entity tab with the Connection details, and Entity name and Entity ID with their Fill buttons](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Dynamics%20CRM%20Tasks/Delete%20entity.png)

:::warning

The Task deletes the record with the selected _Entity ID_. VisualCron cannot undo the deletion.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Delete entity tab

- _Connection_: in the _Connection details_ group, the Dynamics CRM Connection to use; see [Connection - Dynamics CRM](../../connection-dynamics-crm). Click the _Settings_ icon to open _Manage Connections_
- _Entity name_: the logical name of the entity (the record type), for example `account` or `contact`. Click _Fill_ to list the entities of the Dynamics CRM instance
- _Entity ID_: the ID of the record. Select an _Entity name_ first, then click _Fill_ to list the records of that entity

Variables are not resolved in _Entity name_ and _Entity ID_.

### Output and errors

The output is `Deleted Entity Id: <ID>`. When Dynamics CRM rejects the request, or the Connection cannot connect, the Task fails with the error that is returned.
