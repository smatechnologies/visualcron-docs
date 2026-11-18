---
sidebar_label: 'Event Trigger - Cloud File'
hide_title: 'true'
---

## Event Trigger - Cloud File

The Cloud File Trigger watches files in a cloud storage service. At every *Polling interval* (default 60 seconds) it lists the files that match its filter and compares them with the previous list. It starts the Job once for each file that was created, modified or deleted, depending on *Watch for changes*. The first list is read when the Trigger starts. *Expire after being triggered* is not supported by this Trigger.

It uses a [Connection](global-connections) of one of these types, as the Client names them:

* [Amazon](connection-amazon) (Amazon S3)
* [Box](connection-box)
* [Dropbox](connection-dropbox)
* [Google Cloud](connection-google-cloud) (Google Cloud Storage)
* [Google Drive](connection-google-drive)
* [Microsoft Azure](connection-microsoft-azure): storage access only; Azure Connections set up for Management access are not offered
* [OneDrive](connection-onedrive)

This Trigger fires once per file and can download and delete the file before the Job starts. See [Event Triggers](event-triggers#triggers-that-fire-once-per-item) for how to keep a skipped run from losing a file.

The general settings are on the ***Cloud file*** tab, ***Main settings*** sub tab.

![The Main settings sub tab of the Cloud file tab in the Add/Edit event window: Watch for changes with Created files, Modified files (date or size) and Deleted files; Reset status when updating Trigger (use current files as base) checked; On error reconnect attempts 60; On error reconnect interval (seconds) 10](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Cloud.png)

**Watch for changes**

Select which changes fire the Trigger; at least one is required.

* *Created files*: fires the Trigger when a new file is found (see the timing below)
* *Modified files (date or size)*: fires the Trigger when the modified date or the size of a file changes
* *Deleted files*: fires the Trigger when a file is removed

A new file does not fire *Created* when it is first found. At each later check, VisualCron compares its modified date with the previous check, and fires *Created* when it no longer changes, so *Created* fires at least one *Polling interval* after the file stops changing. While the file still changes, *Modified files (date or size)*, if checked, fires at each check. This always applies; it cannot be turned off.

**Reset status when updating Trigger (use current files as base)**

Checked by default. When the Trigger starts after you save it, the files found at that moment become the starting list, and no event fires for them. Check it again if you change the Connection or the folder, so that existing files are not reported as created or deleted. When cleared, the first check compares the files with the list the Trigger kept from earlier checks. Unlike the [Remote File Trigger](event-trigger-remote-file), saving the Trigger keeps that list.

**On error reconnect attempts**

How many times VisualCron tries again after failed checks in a row, for example when the network or the service is down (1 to 500; default 60). If the check after the last try also fails, the Trigger is deactivated and the error is written to the log. A successful check resets the count.

**On error reconnect interval (seconds)**

How many seconds VisualCron waits after a failed check before it tries again (1 to 500; default 10).

:::warning

Some problems are only written to the log and do not count as failed checks, for example a folder that is not found. If the folder is not found or the Connection is deleted, the check carries on with no files: every file the Trigger knew is reported as deleted, and with *Deleted files* checked the Trigger starts the Job for each of them.

:::

The file filter is on the ***Cloud file*** tab, ***Remote File filter*** sub tab.

![The Remote File filter sub tab of the Cloud file tab, Location tab: the Connection list, Bucket/Container, Source folder, Item mask *, the Files list, Case sensitive and Include sub folders](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Cloud%20Remote%20File.png)

The ***Remote File filter*** sub tab selects the Connection and the files to watch. It works as described in [Cloud remote file filter](job-tasks-cloud-remote-file-filter).

The download settings are on the ***Cloud file*** tab, ***Download*** sub tab.

![The Download sub tab of the Cloud file tab with Download file before triggering checked: Credentials, Destination folder, Download file mask *, Overwrite if existing selected, Overwrite if source is newer, Don't overwrite, Keep modified/created date, Delete source file after download and Wait before downloading (seconds)](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Cloud%20Download.png)

**Download file before triggering**

When checked, VisualCron downloads the file that fired the Trigger before it starts the Job, and the *Destination* settings become available. After a successful download, the result Variable `CloudFile.Result.Downloaded` is `True` and `CloudFile.Result.DestinationPath` is the path of the downloaded file.

:::warning

If the download fails, the Job does not start for that file, the failure counts as a failed check, and the file is not reported again. Other new files found in the same check can be skipped too. Check the *Destination folder* and the Connection before you activate the Trigger.

:::

**Destination**

**Credentials**

The list offers a [Credential](global-credentials) for writing the downloaded file, but the Cloud File Trigger currently does not use it: the file is written as the account the VisualCron service runs as. Make sure that account can write to the *Destination folder*.

**Destination folder**

The folder where the downloaded file is saved. To select it, click the folder icon next to the field.

**Overwrite if existing / Overwrite if source is newer / Don't overwrite**

Select what happens when the file already exists in the *Destination folder*:

* *Overwrite if existing*: the existing file is always replaced (default)
* *Overwrite if source is newer*: the existing file is replaced only when the cloud file is newer
* *Don't overwrite*: the existing file is kept and the file is not downloaded

**Keep modified/created date**

Cleared by default. Sets the modified/created date on locally downloaded files to the same dates as the remote files.

**Download file mask**

The name of the downloaded file. The default `*` keeps the name of the cloud file; for example, `*.txt` changes the extension to `.txt`. Accepts Variables. It does not limit which files are downloaded: to choose which files fire the Trigger, use the ***Remote File filter*** sub tab.

**Delete source file after download**

Cleared by default. Optionally delete the remote file after download. The file is downloaded and deleted before the Job starts, also when the run is then skipped. The next check no longer finds the file: it is reported as deleted, and with *Deleted files* checked the Trigger fires again for it.

**Wait before downloading (seconds)**

How many seconds to wait after the file is found before the download starts. Empty (the default) means no wait. Accepts Variables; a value that is not a whole number is treated as no wait.

**Trigger on existing files**

To start the Job for the files that the filter currently finds, right-click the Job in the Grid and click *Triggers*, then the Cloud File Trigger, then *Fire*. The Trigger fires once for each file, downloads it first when *Download file before triggering* is checked, and starts the Job even during a time exception.

### Result Variables

When the Trigger fires, it sets these result Variables for the file that fired it:

* `CloudFile.Result.Name`, `CloudFile.Result.Folder`, `CloudFile.Result.Path`: the file name, its folder and its full path
* `CloudFile.Result.Size`: the size the service reports
* `CloudFile.Result.Created` and `CloudFile.Result.Modified`: the dates the service reports. For another format, use `CloudFile.Result.Modified|<date format>`, for example `{TRIGGER(Active|LastTrigger|CloudFile.Result.Modified|yyyy-MM-dd)}`
* `CloudFile.Result.SourceFolder`: the filter's source folder
* `CloudFile.Result.DestinationPath`: the path of the downloaded file; without a successful download, the *Destination folder*
* `CloudFile.Result.Downloaded`: `True` when the file was downloaded
* `CloudFile.Result.IsDirectory`: whether the item is a folder

For example, `{TRIGGER(Active|LastTrigger|CloudFile.Result.Path)}` returns the path of the file that fired the Trigger that started the run. *Last run*, `{TRIGGER(Active|LastTrigger|LastRun)}`, returns the time the Trigger fired. See [Variables](global-variables) for how *Last trigger* and the other keys work.
