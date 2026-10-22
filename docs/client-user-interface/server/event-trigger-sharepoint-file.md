---
sidebar_label: 'Event Trigger - SharePoint File'
hide_title: 'true'
---

## Event Trigger - SharePoint File

The SharePoint file event trigger monitors a SharePoint library folder for files that are created, modified or deleted. VisualCron checks the folder at the *Polling interval* set in the *Main settings* tab (default 60 seconds) and fires the Trigger when a change is found. The Trigger can also download the file before it fires.

This Trigger uses a SharePoint [Connection](../server/global-connections). The following versions are supported:

* SharePoint 2010
* SharePoint 2013
* SharePoint Online

**Triggers > Add > Event Trigger > SharePoint file > Main settings** tab

**Watch for changes**

Select which file events the Trigger should fire for:

* **Created files** — fire when a new file appears in the folder
* **Modified files (date or size)** — fire when a file's modified date or size changes
* **Deleted files** — fire when a file is removed from the folder

**Reset status when updating Trigger (use current files as base)**

This reloads the internal list of files when the Trigger is saved, so the files that already exist in the folder do not fire the Trigger. It is checked by default. You should check this if you change the Connection or the folder.

**On error reconnect attempts**

Let say the SharePoint site you watch gets disconnected for some reason, perhaps the network or server is down. The reconnect attempts value controls how many times VisualCron tries to reconnect. Default value is 60 times.

**On error reconnect interval (*seconds*)**

The number of seconds VisualCron waits between each reconnect attempt. Default is 10 seconds.

**Triggers > Add > Event Trigger > SharePoint file > Remote File filter** tab

In this tab you select the Connection and folder to monitor and which files to include.

**Connection**

Select the SharePoint Connection to use. Click the *Settings* icon to open the *Manage Connections* dialog.

**Source folder**

The folder in the SharePoint library to monitor. Click the *Folder* icon to use the SharePoint Browser in order to view or select a specific folder.

**Item mask**

A wildcard pattern used to match the files to monitor (e.g. `*` for all files, `*.txt` for text files only).

**Filter**

Select the content filter type to apply when selecting files.

**Case sensitive**

When checked, the item mask matching is case sensitive.

**Include sub folders**

When checked, files in sub folders of the source folder are also monitored.

**Remote File filter > Date** sub tab

**Newer than** / **Older than**

Select a check type and enter a date or variable. Only files newer or older than the specified date are included. Use the AND/OR operator between the two date conditions to control how they are combined.

**Remote File filter > Size** sub tab

**Check if file is smaller than x size** / **Check if file is larger than x size**

When checked, only files smaller or larger than the specified size are included. Select the size unit (bytes, KB, MB, etc.). Use the AND/OR operator between the two size conditions to control how they are combined.

**Remote File filter > Result** sub tab

**Sort**

When checked, the matched file list is sorted. Select the sort column and sort direction.

**Limit**

When checked, the number of matched files is limited to the specified value.

**Remote File filter > Test** sub tab

Click the *Show filtered files* button to preview which files match the current filter settings. The number of matched files and elapsed time are displayed.

**Triggers > Add > Event Trigger > SharePoint file > Download** tab

**Download file before triggering**

When checked, VisualCron downloads the file before the Trigger fires, so the file is ready to use in your Tasks.

**Download file mask**

A wildcard pattern used to match the files to download. Default is `*`.

**Credentials**

Select a Credential if the destination folder requires network credentials. Click on *Manage credentials* to add or edit Credentials.

**Destination folder**

The local folder to save the downloaded files in. Click the folder icon to browse and select a folder.

**Overwrite options**

Select how to handle files that already exist in the destination folder.

- *Overwrite if existing* — overwrite any existing file with the same name (default).
- *Overwrite if source is newer* — only overwrite if the source file is newer than the existing destination file.
- *Don't overwrite* — skip files that already exist in the destination.

**Keep modified/created date**

When checked, the downloaded file keeps the modified and created date of the source file.

**Delete source file after download**

When checked, the source file on the SharePoint site is deleted after it has been successfully downloaded.
