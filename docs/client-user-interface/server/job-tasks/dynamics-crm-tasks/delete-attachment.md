---
sidebar_label: 'Task Dynamics CRM - Delete Attachments'
hide_title: 'true'
---

## Task Dynamics CRM - Delete Attachments

The Dynamics CRM - Delete attachment Task deletes the attachments of a record in Dynamics CRM whose file names match a filter, using a Dynamics CRM Connection.

![Delete attachment tab with the Connection details, Entity name and Entity ID with their Fill buttons, and the Filter box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Dynamics%20CRM%20Tasks/delete%20attachment.png)

:::warning

The Task deletes the note attachments and e-mail (activity) attachments of the record whose file names match _Filter_. The filter is matched anywhere in the file name, not against the whole name, so "*.pdf" also matches a file named "report.pdf.txt". The match is case-sensitive, so "*.pdf" does not match "REPORT.PDF". The default, "*", deletes every attachment of the record. VisualCron cannot undo the deletion.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Delete attachment tab

- _Connection_: in the _Connection details_ group, the Dynamics CRM Connection to use; see [Connection - Dynamics CRM](../../connection-dynamics-crm). Click the _Settings_ icon to open _Manage Connections_
- _Entity name_: the logical name of the entity (the record type), for example `account` or `contact`. Click _Fill_ to list the entities of the Dynamics CRM instance
- _Entity ID_: the ID of the record. Select an _Entity name_ first, then click _Fill_ to list the records of that entity
- _Filter_: the file name mask of the attachments to delete, "*" by default. `*` matches any characters and `?` matches one character

Variables are not resolved in _Entity name_ and _Entity ID_.

### Output and errors

The output has the file name of each deleted attachment, one per line. When no attachment matches, the output is empty and the Task succeeds. When Dynamics CRM rejects the request, or the Connection cannot connect, the Task fails with the error that is returned.
