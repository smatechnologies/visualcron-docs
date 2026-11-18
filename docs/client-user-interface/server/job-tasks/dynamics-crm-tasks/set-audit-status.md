---
sidebar_label: 'Task Dynamics CRM - Set Audit Status'
hide_title: 'true'
---

## Task Dynamics CRM - Set Audit Status

The Dynamics CRM - Set audit status Task turns auditing on or off for the organization, for an entity, or both, in Dynamics CRM, using a Dynamics CRM Connection.

![Set audit status tab with the Connection details, Entity name with its Fill button, and the Audit settings box with Action type and two check boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Dynamics%20CRM%20Tasks/Set%20audit%20status.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Set audit status tab

- _Connection_: in the _Connection details_ group, the Dynamics CRM Connection to use; see [Connection - Dynamics CRM](../../connection-dynamics-crm). Click the _Settings_ icon to open _Manage Connections_
- _Entity name_: the logical name of the entity whose auditing to change. It is used only with _Auditing for entity_. Click _Fill_ to list the entities

In the _Audit settings_ group:

- _Action type_: "Enable" (default) or "Disable"
- _Auditing for organization_: applies the action to auditing for the whole organization
- _Auditing for entity_: applies the action to auditing for the selected entity

When neither check box is selected, the Task changes nothing and succeeds.

:::note

If auditing is not enabled at the organization level, auditing of entities and attributes, even if it is enabled, does not occur. By default, auditing is enabled on all auditable entity attributes but is disabled at the entity and organization level.

:::

### Output and errors

The Task writes no output. When Dynamics CRM rejects the request, or the Connection cannot connect, the Task fails with the error that is returned.
