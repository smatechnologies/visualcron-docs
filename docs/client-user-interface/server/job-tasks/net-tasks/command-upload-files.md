1---
sidebar_label: 'Command - Upload File(s)'
hide_title: 'true'
---

## Command - Upload File(s)

The upload command sends one or more files and creates recursive folders if necessary.
 
**Upload > File filter** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/Upload%20Settings.png)

For upload, VisualCron uses the standard [file filter](../../../server/job-tasks-file-filter) to specify files that should be uploaded.
 
**Upload** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/Upload.png)

**Delete source file after copy**

When checked, the local source file is deleted after it has been uploaded. Default is unchecked.
 
**Destination folder**

The remote folder on the server where the file(s) should be uploaded. If the server supports relative paths, specify a path such as `/topfolder/subfolder`. Use the folder browse button to select a folder from the server. Default is `/`.
 
**Overwrite options**

Controls what happens when a file with the same name already exists at the destination. Options:

* Overwrite - always if existing** (default) — always replace the destination file
* Overwrite - if newer** — replace only if the source file is newer
* Overwrite - if destination size is** — replace based on size comparison (activates the size dropdown below)
* Append if destination is smaller - otherwise overwrite** — append bytes until size matches source; if not smaller, overwrite
* Append if destination is smaller - otherwise overwrite if newer** — append bytes until size matches; if not smaller, overwrite only if source is newer
* Append if destination is smaller - otherwise skip** — append bytes until size matches; if not smaller, skip the file
* Append if existing - otherwise create** — append to an existing file, or create a new file if it does not exist
* Append if existing - otherwise skip** — append to an existing file; skip if the file does not exist at the destination
* Do not overwrite if existing** — skip the file if it already exists at the destination

**Overwrite size**

Active only when **Overwrite options** is set to "Overwrite - if destination size is". Specifies the size condition for overwriting. Options: Same, Smaller, Larger, Smaller or larger, Different.
 
**Resume if transfer failed. Try resuming**

When checked, VisualCron appends to the partially uploaded file and retries on failure. Set the number of retry attempts and the interval in seconds between retries. Default for both is 999.

**Keep modified/created date**

When checked, the uploaded file's modified and created timestamps are set to match those of the local source file. Default is unchecked.

**Override transfer type set in Connection**

When checked, the transfer type for this command overrides the setting configured in the [Connection](../../../server/global-connections). Select the desired transfer type from the dropdown.

**Maximum number of threads**

The number of simultaneous upload threads. Default is 1, maximum is 8.
