---
sidebar_label: 'Task Cloud Transfer - Sync'
hide_title: 'true'
---

## Task Cloud Transfer - Sync

The Cloud - Sync file(s) Task synchronizes files between a source and a target location. Both source and target can be cloud services (Amazon S3, Box, Dropbox, Google Drive, Google Storage, Microsoft Azure, OneDrive), FTP / SFTP / WinSCP servers, or the local file system.

**Sync > Connections** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Cloud%20Transfer%20Tasks/Sync%20file(s).png)

**Source connection**

Select the connection to use for the source location. Only cloud (Amazon S3, Windows Azure, OneDrive, Google Drive, Google Storage, Dropbox, Box) and FTP / SFTP / WinSCP connections are shown.

**Local files** (source)

When checked, the local file system is used as the source instead of a connection. Checking this disables the *Source connection* selector and forces the target to use a connection (the target *Local files* checkbox is unchecked). Source and target cannot both be local at the same time.

**Target connection**

Select the connection to use for the target location. The same protocols as the source are listed.

**Local files** (target)

When checked, the local file system is used as the target instead of a connection. Checking this disables the *Target connection* selector and forces the source to use a connection.

**Sync > Source file filter** sub tab

Defines which files from the source are included in the sync. The filter shown depends on the source connection type:

* Cloud connection - the standard [Cloud Remote file filter](../../../server/job-tasks-cloud-remote-file-filter)
* FTP / SFTP / WinSCP connection - the standard [Remote file filter](../../job-tasks-remote-file-filter)
* Local files - the standard [File filter](../../job-tasks-file-filter)

Only the sub tab matching the current source type is visible; it switches automatically when the connection or *Local files* toggle changes.

**Sync > Target file filter** sub tab

Defines which files on the target are considered during the sync. Uses the same three filter types as the source, again based on the target connection type, and only the matching sub tab is shown.

**Sync > Sync options** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Cloud%20Transfer%20Tasks/Sync%20Options.png)

**Resolve same name conflicts as**

Select how to handle files that exist in both source and target with the same name but different content. Available options:

* _Take Source_ - always use the source file
* _Take Target_ - always use the target file
* _Take Newer_ - use the file with the more recent modification date (default)
* _Take Older_ - use the file with the older modification date
* _Take Bigger_ - use the larger file
* _Take Smaller_ - use the smaller file
* _Skip_ - do not overwrite either file

**Resolve equal file conflicts as**

Select how to handle files that are considered equal under the *same name* rule (for example, same modification date when *Take Newer* is selected, or same size when *Take Bigger* is selected). Only enabled when the same name conflict resolution is set to _Take Newer_, _Take Older_, _Take Bigger_, or _Take Smaller_. Available options:

* _Take source_ - use the source file
* _Take Target_ - use the target file
* _Skip_ - do not overwrite (default)

**Sync flow**

Select the direction of the synchronization. Available options:

* _Source -> Target_ - copies files from source to target only
* _Target ->Source_ - copies files from target to source only
* _Source &lt;-&gt; Target_ - synchronizes in both directions (default); disables the *Delete source file* option

**Delete source file after download**

When checked, the source file is deleted after it has been successfully copied to the target. The label changes based on the sync flow direction. Only enabled when a one-directional sync flow is selected.

**Source missing action**

Select what to do with files that exist on the target but are missing on the source (for example, files that were deleted from the source but remain on the target after a previous sync). Available options:

* _Delete_ - delete the file from the target
* _Skip_ - leave the file on the target (default)

**Credential**

Select a [Credential](../../global-credentials) to use when source or target points to a network share that requires authentication. Used in addition to (not instead of) any credential set on a Local file filter. Leave empty to use the VisualCron service account.
