---
sidebar_label: 'Task Messaging - Pushbullet - Send File'
hide_title: 'true'
---

## Task Messaging - Pushbullet - Send File

The Pushbullet - Send file Task sends one or more files, with a message, to people, devices or channels, using a Pushbullet Connection.

![Pushbullet - Send file tab, Message tab with the Connection group and the Body field](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Pushbullet%20-%20send%20file.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Pushbullet - Send file: Message tab

- _Connection_: the Pushbullet Connection to send with; see [Connection - Pushbullet](../../connection-pushbullet)

  The Task uses the proxy set on the Connection.

- _Body_: the text sent with each file; Variables are resolved

### Pushbullet - Send file: File filter tab

Use the [File Filter](../../job-tasks-file-filter) to choose the files to send. Each matching file is sent as a separate push, with the same _Body_. The Credential of the File filter is used to read the files.

### Pushbullet - Send file: Recipient(s) tab

The ***Recipient(s)*** tab has three tabs, ***People***, ***Devices*** and ***Channels***. Select at least one recipient on them, or the Task cannot be saved.

Each tab has:

- _Send to all people_, _Send to all devices_ or _Send to all channels_: sends to every recipient of that kind; the grid is then unavailable
- The grid: select _Use_ on each recipient to send to
- _Select all_ and _Deselect all_: select or clear _Use_ on every row
- _Refresh_: loads the people, devices or channels of the Connection's account into the grid, and clears every _Use_ check box

:::warning

_Send to all channels_ is currently not applied: the file goes only to the channels selected in the grid. A Task with only _Send to all channels_ selected can be saved, but no channel receives the file.

:::

### Output and errors

The output holds the path of each file sent, with no separator between the paths, followed by the response from Pushbullet for the last file. If no file matches the File filter, the Task fails with "No file(s) found". If Pushbullet rejects a file, the Task fails and the remaining files are not sent.
