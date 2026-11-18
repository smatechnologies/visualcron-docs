---
sidebar_label: 'Task Dynamics CRM - List Entity'
hide_title: 'true'
---

## Task Dynamics CRM - List Entity

The Dynamics CRM - List Entity Task writes the value of one attribute of every record of an entity in Dynamics CRM to the output, using a Dynamics CRM Connection. It works like [Task Dynamics CRM - Get Entity](get-entity), but for all records instead of one.

![List entity tab with the Connection details, Entity name with its Fill button, and Attribute name with its Fill button](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Dynamics%20CRM%20Tasks/List%20entity.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### List entity tab

- _Connection_: in the _Connection details_ group, the Dynamics CRM Connection to use; see [Connection - Dynamics CRM](../../connection-dynamics-crm). Click the _Settings_ icon to open _Manage Connections_
- _Entity name_: the logical name of the entity (the record type), for example `account` or `contact`. Click _Fill_ to list the entities of the Dynamics CRM instance
- _Attribute name_: the attribute to list, "ID" by default, which lists the record IDs. Click _Fill_ to list the attribute names

Variables are not resolved in _Entity name_.

### Output and errors

The output has the value of the attribute for each record, one per line. When Dynamics CRM rejects the request, or the Connection cannot connect, the Task fails with the error that is returned.

:::warning

For a record that has no value for the attribute, the error "Entity Id was not found." is written to standard error, the record is left out of the output, and the Task reports success.

:::
