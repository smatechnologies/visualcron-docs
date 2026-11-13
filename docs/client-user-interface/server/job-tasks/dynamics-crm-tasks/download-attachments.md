---
sidebar_label: 'Task Dynamics CRM - Download Attachments'
hide_title: 'true'
---

## Task Dynamics CRM - Download Attachments

The Dynamics CRM - Download attachment Task downloads the note attachments whose names match a file mask from Dynamics CRM to a folder, using a Dynamics CRM Connection.

![Download attachment(s) tab with the Connection details, Destination folder with its folder button, and Source file mask with its Refresh button](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Dynamics%20CRM%20Tasks/Download%20attachment(s).png)

:::warning

The Task writes each attachment's content as Dynamics CRM stores it, as Base64 text, so a downloaded file is not the original file and has to be decoded before it is used. A file with the same name in _Destination folder_ is overwritten.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Download attachment(s) tab

- _Connection_: in the _Connection details_ group, the Dynamics CRM Connection to use; see [Connection - Dynamics CRM](../../connection-dynamics-crm). Click the _Settings_ icon to open _Manage Connections_

In the _Download settings_ group:

- _Destination folder_: the folder to save the files in, on the computer that runs the VisualCron Server. Click the _Folder_ icon to browse
- _Source file mask_: the mask that the attachment names must match, "*.*" by default. `*` matches any characters and `?` matches one character, and case is ignored. With "*.*", attachments whose names have no dot are not downloaded. The mask is matched against the note attachments of every record that the Connection's user can read, not only one record. Type the mask: the _Refresh_ button does not read the attachments through the selected Connection, so do not rely on the list it shows

### Output and errors

The output has the path of each downloaded file, one per line. When no attachment matches, the output is empty and the Task succeeds. When Dynamics CRM rejects the request, or the Connection cannot connect, the Task fails with the error that is returned.
