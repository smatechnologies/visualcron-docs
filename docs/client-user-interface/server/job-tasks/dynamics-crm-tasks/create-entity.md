---
sidebar_label: 'Task Dynamics CRM - Create Entity'
hide_title: 'true'
---

## Task Dynamics CRM - Create Entity

The Dynamics CRM - Create Entity Task creates a record of an entity in Dynamics CRM, using a Dynamics CRM Connection.

![Create entity tab with the Connection details, Entity name with its Fill button, the Entity data grid and the Fill attributes button](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Dynamics%20CRM%20Tasks/Create%20entity.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Create entity tab

- _Connection_: in the _Connection details_ group, the Dynamics CRM Connection to use; see [Connection - Dynamics CRM](../../connection-dynamics-crm). Click the _Settings_ icon to open _Manage Connections_
- _Entity name_: the logical name of the entity (the record type), for example `account` or `contact`. Click _Fill_ to list the entities of the Dynamics CRM instance
- _Entity data_: the attribute values of the new record, one row for each attribute, with the _Attribute name_ and _Attribute value_ columns. Click _Fill attributes_ to list the attributes that an existing record of the selected entity has, then type the values. Variables are resolved in the values. Attributes with an empty value are not set

Values are sent as text. Attributes of other types, such as option sets, lookups, numbers, money and dates, may be rejected by Dynamics CRM, and the Task then fails.

Variables are not resolved in _Entity name_.

### Output and errors

The output is `Created Entity Id: <ID>`, with the ID of the new record. When Dynamics CRM rejects the request, or the Connection cannot connect, the Task fails with the error that is returned.
