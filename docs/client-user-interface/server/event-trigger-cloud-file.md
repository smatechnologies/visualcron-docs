---
sidebar_label: 'Event Trigger - Cloud File'
hide_title: 'true'
---

## Event Trigger- Cloud File

The Cloud file event trigger is able to monitor file events in various online cloud services:
* [Amazon S3](../server/connection-amazon)
* [Box](../server/connection-box)
* [DropBox](../server/connection-dropbox)
* [Google Drive](../server/connection-google-drive)
* [Microsoft Azure](../server/connection-microsoft-azure)
* [OneDrive](../server/connection-onedrive)
 
Different [Connections](../server/global-connections) are used depending on the wanted cloud service provider.
 
**Triggers > Add > Event Trigger > Cloud file > Cloud file > Main settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Cloud.png)

**Watch for changes**

Select which file events the Trigger should fire for:

* **Created files** — fire when a new file appears
* **Modified files (date or size)** — fire when a file's modified date or size changes
* **Deleted files** — fire when a file is removed
 
**Reset status when updating Trigger (_use current files as base_)**

This reloads the internal list of files. You should check this if you for some reason change the Connection.
 
**On error reconnect attempts**

Let say the remote server you watch gets disconnected for some reason, perhaps the network or computer is down. The reconnect attempts value controls how many times VisualCron tries to reconnect. Value 1 to 500 is available. Default value is 5 times.
 
**On error reconnect interval (_seconds_)**

Let say the remote server you watch gets disconnected for some reason, perhaps the network or computer is down. The reconnect interval which you can specify is the number of seconds it will wait between each reconnect attempt, in seconds. Value 1 to 500 is available. Default is 5 seconds which may be a long time when the network is down and a short time if the remote computer is down.
 
**Triggers > Add > Event Trigger > Cloud file > Cloud file > Remote file filter** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Cloud%20Remote%20File.png)

This Trigger uses the [Cloud Remote file filter](../server/job-tasks-cloud-remote-file-filter) for filtering out files to check for.
 
**Triggers > Add > Event Trigger > Cloud file > Cloud file > Download** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Cloud%20Download.png)

**Download file before triggering**

Optionally, you can set the Remote file Trigger to download the file that was just Triggered. When enabled, the _Destination_ group below becomes editable.

**Destination**

**Credentials**

Select a [Credential](../server/global-credentials) if you are going to save to a network drive. Click the Settings icon to populate the drop-down list with available credentials.
 
**Destination folder**

The local folder where the file should be saved. Click the Folder icon in order to browse the folder tree.
 
**Overwrite options**

If the file already exists in the destination folder, choose how it should be handled:

* **Overwrite if existing** — always replace the local file (default)
* **Overwrite if source is newer** — only replace the local file when the remote file is newer
* **Don't overwrite** — keep the existing local file and skip the download
 
**Keep modified/created date**

Sets the modified/created date on locally downloaded files to the same dates as the remote files.

**Download file mask**

A file mask used to limit which files are downloaded. The default is `*`, which downloads any file that triggered the event.
 
**Delete source file after download**

Optionally delete the remote file after download.

**Wait before downloading (seconds)**

The number of seconds to wait between detecting a file and starting the download. This can help when the remote file is still being written when the event fires. Click the variables button to insert a VisualCron variable.
