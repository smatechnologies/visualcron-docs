---
sidebar_label: 'Task Dynamics CRM - Upload Attachments'
hide_title: 'true'
---

## Task Dynamics CRM - Upload Attachments

The Dynamics CRM - Upload attachment Task uploads the files that match a file filter to Dynamics CRM, as note attachments of a record, using a Dynamics CRM Connection.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Upload attachment: Main settings tab

![Upload attachment tab, Main settings sub tab with the Connection details, Entity name and Entity ID with their Fill buttons, Use if entry id is empty, and the Upload settings box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Dynamics%20CRM%20Tasks/upload%20attachments.png)

- _Connection_: in the _Connection details_ group, the Dynamics CRM Connection to use; see [Connection - Dynamics CRM](../../connection-dynamics-crm). Click the _Settings_ icon to open _Manage Connections_
- _Entity name_: the logical name of the entity (the record type), for example `account` or `contact`. Click _Fill_ to list the entities of the Dynamics CRM instance
- _Entity ID_: the ID of the record. Select an _Entity name_ first, then click _Fill_ to list the records of that entity
- _Use if entry id is empty_: the record ID to use when _Entity ID_ is empty. Variables are resolved in this field

In the _Upload settings_ group:

- _Auto detect_: selected by default. The MIME type of each file is detected from the file
- _Mime type_: the MIME type of the files, used when _Auto detect_ is cleared, for example "application/pdf". The default value, "test/plain", is not a valid MIME type, so change it when you clear _Auto detect_

Variables are not resolved in _Entity name_ and _Entity ID_.

### Upload attachment: File filter tab

The files to upload are set with the standard VisualCron file filter; see [File Filter](../../job-tasks-file-filter).

### Output and errors

Each file is added to the record as a note with the subject "File attachment" and the file's name. The output has the ID of each note created, one per line. When no file matches the filter, the output is empty and the Task succeeds. When a file cannot be uploaded, the Task fails. The other files are still uploaded, and uploaded files stay in Dynamics CRM.
