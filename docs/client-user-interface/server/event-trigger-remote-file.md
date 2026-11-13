---
sidebar_label: 'Event Trigger - Remote File'
hide_title: 'true'
---

## Event Trigger - Remote File

The Remote File Trigger watches files on an FTP, SFTP or SCP server. At every *Polling interval* (default 60 seconds) it lists the files that match its filter and compares them with the previous list. It starts the Job once for each file that was created, modified or deleted, depending on *Watch for changes*. The first list is read when the Trigger starts. *Expire after being triggered* is not supported by this Trigger.

This Trigger fires once per file and can download and delete the file before the Job starts. See [Event Triggers](event-triggers#triggers-that-fire-once-per-item) for how to keep a skipped run from losing a file.

The settings are on the ***Remote file*** tab, ***Main settings*** sub tab.

![The Main settings sub tab of the Remote file tab in the Add/Edit event window: the Connection list; Watch for changes with Created files and Wait for file being released checked, Modified files (date or size) and Deleted files cleared; Reset status when updating Trigger (use current files as base) checked; On error reconnect attempts 60; On error reconnect interval (seconds) 10](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Remote%20File.png)

**Connection**

Select an FTP, SFTP or SCP Connection from the central [Connections](global-connections). Click the icon next to the list to add or edit Connections.

**Watch for changes**

Select which changes fire the Trigger; at least one is required. *Created files* is checked by default.

*Created files* is currently always included when you save the Trigger, even when you clear it: new files also start the Job, and *Created files* is checked again the next time you open the Trigger. When you watch only for modified or deleted files, make sure the Job can handle new files too. *Wait for file being released* keeps its saved value while it is unavailable.

* *Created files*: fires the Trigger when a new file is found (see the timing below)
* *Modified files (date or size)*: fires the Trigger when the modified date or the size of a file changes
* *Deleted files*: fires the Trigger when a file is removed from the remote server

**Wait for file being released**

Checked by default, and available only while *Created files* is checked. A new file does not fire *Created* when it is first found. At each later check, VisualCron compares the file's modified date with the previous check: while it changes, the file is still being written; when it is the same, *Created* fires. *Created* therefore fires at least one *Polling interval* after the file stops changing. While the file still changes, *Modified files (date or size)*, if checked, fires at each check. When cleared, *Created* fires as soon as a new file is found, even if it is still being written.

**Reset status when updating Trigger (use current files as base)**

Checked by default. When the Trigger starts after you save it, the files found at that moment become the starting list, and no event fires for them. Keep it checked whenever you save the Trigger.

:::warning

Saving the Trigger empties the list of files it has seen. If this option is cleared when you save, the first check reports every matching file as created, and the Trigger starts the Job for each of them. If the first check after saving fails, for example because the server cannot be reached, the next check also reports every matching file as created.

:::

**On error reconnect attempts**

How many times VisualCron tries again after failed checks in a row, for example when the network or the server is down (1 to 500; default 60). If the check after the last try also fails, the Trigger is deactivated and the error is written to the log. A successful check resets the count.

**On error reconnect interval (seconds)**

How many seconds VisualCron waits after a failed check (1 to 500; default 10). The next try is the next *Polling interval* check after that wait.

:::warning

A check that finds no files is not an error. If the Connection is deleted, or, for an FTP Connection, the folder no longer exists, the check finds no files: every file the Trigger knew is reported as deleted, and with *Deleted files* checked the Trigger starts the Job for each of them.

:::

The ***Location***, ***Date***, ***Size*** and ***Test*** sub tabs of the ***Remote file*** tab select which files are watched. They work as described in [Remote file filter](job-tasks-remote-file-filter). On ***Location***, the folder and the include file mask are required. ***Test*** lists the files that the filter currently finds.

The download settings are on the ***Remote file*** tab, ***Download*** sub tab.

![The Download sub tab of the Remote file tab with Download file before triggering cleared and the Destination settings unavailable: Credentials, Destination folder, Download file mask, Overwrite options, resume, Keep modified/created date, Replace unsupported characters with character, Delete source file after download, the three save options and Wait before downloading (seconds)](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Remote%20File%20Download.png)

**Download file before triggering**

When checked, VisualCron downloads the file that fired the Trigger before it starts the Job, and the *Destination* settings become available. The download is part of the check, so the next check waits until it is done. If the download fails, the error is written to the log and the Job still runs; the result Variable `RemoteFile.Result.Downloaded` is then `False`. A *Deleted files* event also tries a download, which fails.

**Destination**

**Credentials**

The [Credential](global-credentials) used to write the downloaded file, for example to a network share. Select it in the list, or click the icon next to it to open *Manage credentials*.

**Destination folder**

The folder the file is downloaded to. Accepts Variables. Click the folder icon to browse.

**Download file mask**

Meant to set the name of the downloaded file (default `*`, the remote file name), as in the Cloud File Trigger. The Remote File Trigger currently does not use it: the file is always saved under its remote name. It never limits which files are downloaded; to choose which files fire the Trigger, use the include and exclude file masks on the ***Location*** sub tab.

**Overwrite options**

What happens when the file already exists in the destination folder:

* *Overwrite - always if existing*: the default
* *Overwrite - if newer*
* *Overwrite - if destination size is*: overwrite only if the existing file is *Same*, *Smaller* (default), *Larger*, *Smaller or larger* or *Different* in size, as chosen in the second list. The second list is available only for this option
* *Append if destination is smaller - otherwise overwrite*
* *Append if destination is smaller - otherwise overwrite if newer*
* *Append if destination is smaller - otherwise skip*
* *Do not overwrite if existing*

**Resume if transfer failed**

*Resume if transfer failed. Try resuming:* when checked, a failed download is resumed up to the number of *times* you enter (1 to 10000; default 3), waiting the *second(s)* you enter between tries (1 to 10000; default 1).

**Keep modified/created date**

Cleared by default. When checked, the downloaded file gets the modified and created dates of the remote file.

**Replace unsupported characters with character**

Checked by default, with `c`. Characters in the remote file name that Windows does not allow in file names are replaced with the character you enter.

**Delete source file after download**

Cleared by default. When checked, the remote file is deleted after it is downloaded. The next check then no longer finds the file: it is reported as deleted, and with *Deleted files* checked the Trigger fires again for it. The file is downloaded and deleted before the Job starts, also when the run is then skipped.

Under *Destination*, select where in the destination folder the file is saved:

* *Save files to destination folder*: directly in the destination folder
* *Save files to destination relative to source path*: the default. The file's subfolders below the *Location* folder are created in the destination folder
* *Save files to destination with full relative path*: the file's full remote folder path is created in the destination folder

**Wait before downloading (seconds)**

How many seconds to wait after the file is found before the download starts. Empty (the default) means no wait. Accepts Variables; a value that is not a whole number is treated as no wait.

### Result Variables

When the Trigger fires, it sets these result Variables for the file that fired it:

* `RemoteFile.Result.Name`: the file name
* `RemoteFile.Result.Folder`: the remote folder of the file
* `RemoteFile.Result.Path`: the full remote path
* `RemoteFile.Result.Size`: the size the server reports
* `RemoteFile.Result.Created` and `RemoteFile.Result.Modified`: the dates the server reports. For another format, use `RemoteFile.Result.Modified|<date format>`, for example `{TRIGGER(Active|LastTrigger|RemoteFile.Result.Modified|yyyy-MM-dd)}`
* `RemoteFile.Result.SourceFolder`: the *Location* folder
* `RemoteFile.Result.DestinationPath`: the path of the downloaded file; without a successful download, the *Destination folder*
* `RemoteFile.Result.Downloaded`: `True` when the file was downloaded
* `RemoteFile.Result.IsDirectory`: whether the item is a folder

For example, `{TRIGGER(Active|LastTrigger|RemoteFile.Result.Path)}` returns the path of the file that fired the Trigger that started the run. *Last run*, `{TRIGGER(Active|LastTrigger|LastRun)}`, returns the time the Trigger fired. See [Variables](global-variables) for how *Last trigger* and the other keys work.
