---
sidebar_label: 'Task Messaging - Pushbullet - Upload File'
hide_title: 'true'
---

## Task Messaging - Pushbullet - Upload File

The Pushbullet - Upload file Task uploads one or more files to Pushbullet, using a Pushbullet Connection. The output of the Task holds the Pushbullet response for each uploaded file. The response includes the file's URL, so a later Task can use it.

![Pushbullet - Upload file tab, Main settings tab with the Connection group](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Pushbullet%20-%20upload%20file.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Pushbullet - Upload file: Main settings tab

- _Connection_: the Pushbullet Connection to upload with; see [Connection - Pushbullet](../../connection-pushbullet)

  The Task uses the proxy set on the Connection.

### Pushbullet - Upload file: File filter tab

Use the [File Filter](../../job-tasks-file-filter) to choose the files to upload. The Credential of the File filter is used to read the files.

### Output and errors

The responses for the uploaded files follow each other in the output, with no separator. If no file matches the File filter, the Task fails with "No file(s) found". If Pushbullet rejects a file, the Task fails and the remaining files are not uploaded.
