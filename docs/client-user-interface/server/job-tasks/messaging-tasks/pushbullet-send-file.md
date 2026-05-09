---
sidebar_label: 'Task Messaging - Pushbullet - Send File'
hide_title: 'true'
---

## Task Messaging - Pushbullet - Send File

The Pushbullet - Send file Task sends a file to one or more Pushbullet devices, contacts and/or channels.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Pushbullet%20-%20send%20file.png)

**Connection**

Select an existing global [Pushbullet Connection](../../../server/connection-pushbullet) for storing the connection credentials.

**Body**

The message text sent alongside the file.

**Pushbullet - Send file > File filter** sub tab

Use the standard [File filter](../../../server/job-tasks-file-filter) to select one or more files to send.

**Pushbullet - Send file > Recipients** sub tab

The Recipients section has three nested sub tabs — *Devices*, *Contacts* and *Channels* — that let you choose where the file is delivered. At least one recipient must be selected across the three tabs.

Each recipient sub tab works the same way:

* _Send to all_ - when checked, the file is sent to every recipient of that type and the grid is disabled
* _Refresh_ - queries the selected Connection and populates the grid with the available recipients
* _Select all_ / _Deselect all_ - quickly toggle the *Use* column for every row in the grid
* The grid - check the *Use* column on the rows to choose individual recipients
