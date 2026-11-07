---
sidebar_label: 'Task Dynamics CRM - Get Entity'
hide_title: 'true'
---

## Task Dynamics CRM - Get Entity

The Dynamics CRM - Get Entity Task writes the value of one attribute of a record in Dynamics CRM to the output, using a Dynamics CRM Connection.

![Get entity tab with the Connection details, Entity name and Entity ID with their Fill buttons, and Attribute name with its Fill button](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Dynamics%20CRM%20Tasks/Get%20entity.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Get entity tab

- _Connection_: in the _Connection details_ group, the Dynamics CRM Connection to use; see [Connection - Dynamics CRM](../../connection-dynamics-crm). Click the _Settings_ icon to open _Manage Connections_
- _Entity name_: the logical name of the entity (the record type), for example `account` or `contact`. Click _Fill_ to list the entities of the Dynamics CRM instance
- _Entity ID_: the ID of the record. Select an _Entity name_ first, then click _Fill_ to list the records of that entity
- _Attribute name_: the attribute to read, "ID" by default. Click _Fill_ to list the attribute names. On this Task, "ID" is not an attribute of the record, so choose an attribute such as the record's own ID attribute, for example `accountid` for an account

Variables are not resolved in _Entity name_ and _Entity ID_.

### Output and errors

The output is the value of the attribute. When Dynamics CRM rejects the request, or the Connection cannot connect, the Task fails with the error that is returned.

:::warning

When the record has no value for the attribute, or the attribute does not exist, the error "Entity Id was not found." is written to standard error, the output is empty, and the Task reports success.

:::
