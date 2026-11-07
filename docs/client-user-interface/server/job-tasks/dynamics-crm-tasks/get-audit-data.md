---
sidebar_label: 'Task Dynamics CRM - Get Audit Data'
hide_title: 'true'
---

## Task Dynamics CRM - Get Audit Data

The Dynamics CRM - Get audit data Task writes the change history (audit records) of a record in Dynamics CRM to the output, using a Dynamics CRM Connection. Changes are recorded only while auditing is enabled; see [Task Dynamics CRM - Set Audit Status](set-audit-status).

![Get audit data tab with the Connection details, and Entity name and Entity ID with their Fill buttons](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Dynamics%20CRM%20Tasks/Get%20audit%20data.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Get audit data tab

- _Connection_: in the _Connection details_ group, the Dynamics CRM Connection to use; see [Connection - Dynamics CRM](../../connection-dynamics-crm). Click the _Settings_ icon to open _Manage Connections_
- _Entity name_: the logical name of the entity (the record type), for example `account` or `contact`. Click _Fill_ to list the entities of the Dynamics CRM instance
- _Entity ID_: the ID of the record. Select an _Entity name_ first, then click _Fill_ to list the records of that entity

Variables are not resolved in _Entity name_ and _Entity ID_.

### Output and errors

For each audit record, the output has the date the record was created, the entity, the action and the operation, and the old and new value of each changed attribute. When Dynamics CRM rejects the request, or the Connection cannot connect, the Task fails with the error that is returned.
