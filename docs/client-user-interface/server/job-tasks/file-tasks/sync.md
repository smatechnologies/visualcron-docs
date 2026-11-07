---
sidebar_label: 'Task File - Sync'
hide_title: 'true'
---

## Task File - Sync

The Task file - Sync files Task lets you sync files between two folders according to some file filters.
 
![Add Task dialog for the Sync files Task, with the list of sync items](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Sync%20Files.png)

You can add one or more file sync items in this Task.
 
 
**Add file sync item->Source path and file filter** tab

![Sync files Task with the Add/Edit sync file item dialog open on the Source path and file filter tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Sync%20Files%20Location.png)

Use the regular [file filter](../../../server/job-tasks-file-filter) to filter what kind of files you want to sync.
 
 
**Add file sync item->Destination path and sync settings** tab

![Add/Edit sync file item dialog, Destination path and sync settings tab, General tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Sync%20Files%20Destination.png)

**Credential**

To access a remote computer you may need to use a [Credential](../../../server/global-credentials). Normally that Credential is a remote or AD user with "Local logon" unchecked. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the *Settings* icon to open *Manage Credentials* in order to add or edit Credentials. This Credential is used to access the destination directory.
 
**Destination folder**

Specify an absolute path to the directory you want to sync between.
 
**Destination->General** tab
 
**Sync type**

In this Task, the source is the folder on the **_Source path and file filter_** tab, and the
destination is the *Destination folder*. *Sync type* controls which of them the Task may change:

- *Left to right*: copies new and changed files from the source to the destination; only the
  destination is changed
- *Right to left*: copies new and changed files from the destination to the source; only the source is
  changed
- *Both sides* (default): copies new and changed files in both directions

When a file exists on both sides with the same size, the Task copies the newer one over the older one.
When the sizes differ and *Sync type* is *Both sides*, the Task copies the file only if exactly one side is set
to *Set as master side for the changes*, and then copies that side's version. Otherwise the file is left
unchanged on both sides, and no error is reported.
 
**Propagate Deletions**

Selected by default. This option decides what happens when a file that the Task synced on an earlier
run is deleted on one side.

| *Propagate Deletions* | What the Task does with the copy on the other side |
|---|---|
| Selected (default) | If that copy has not changed since the last run, and *Sync type* lets the Task change that side, the Task deletes it permanently. Otherwise it is copied back to the side where the file was deleted, if *Sync type* lets the Task change that side. |
| Cleared | It is copied back to the side where the file was deleted, if *Sync type* lets the Task change that side. |

A deletion made by this option is permanent. It is not affected by the replaced-file options below.

:::note
When *Propagate Deletions* is selected, deleting a file on one side also deletes it on the other side,
wherever *Sync type* lets the Task change that side. With *Left to right*, for example, deleting a file
in the source folder deletes it in the destination folder. If you want deleted files to be kept, clear
this option or keep a separate backup.

Deletions are detected only for files in folders that exist on both sides. If you delete a folder,
the files in it are not deleted on the other side.
:::

**Deleted/replaced files**

Although their labels say "deleted/replaced", these options act only when the Task overwrites a file
with the file from the other side. They never keep a copy of a file removed by *Propagate Deletions*.

| Option | What happens to the file being overwritten |
|---|---|
| *To do nothing* (default) | It is overwritten. No copy is kept. |
| *Save deleted/replaced files to Recycle bin* | It is moved to the Recycle Bin first. |
| *Save deleted/replaced files adding version* | It is renamed in the same folder by adding a number to the end of its full name, for example `"report.txt1"`. Copy 1 is the oldest. *Save this many versions:* sets how many copies are kept (default 5). Numbered copies are ordinary files, so they can be synced to the other side if they match the file filter. |
| *Save deleted/replaced files to specified folder* | It is moved into the folder you specify, under subfolders that repeat its original path. Its clean-up settings (*Cleanup folder after this many days*, the default, or *Cleanup folder after this many versions, format:*) delete saved copies automatically, so check them before relying on this folder to keep copies. |
 
**Destination->Advanced** tab

![Add/Edit sync file item dialog, Destination path and sync settings tab, Advanced tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Sync%20Files%20Destination%20Advanced.png)

**Copy attributes->Copy file creation time**

If the creation time of the file should be synced over
 
**Copy attributes->Copy attributes**

If file attributes should be synced over
 
**Folder creation options->Create sub folders**

Create sub folders when needed.
 
**Folder creation options->Create full folder structure**

Create the full folder structure including empty folders. Only active when *Create sub folders* is selected.
 
**Folder creation options->Don't create sub folders**

Do not create any sub folders (sync to base folder).

**Analyze**

**Detect File and Folder Moves and Renames**

When checked, the Task attempts to detect when files or folders have been moved or renamed rather than treating them as a delete and a new file. This reduces unnecessary data transfer.

**Estimate disk space required for Sync**

When checked, VisualCron calculates the disk space required on the destination before performing the sync.
 
**Destination->Source side options** tab

![Add/Edit sync file item dialog, Source side options tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Sync%20Files%20Destination%20Source%20Side.png)

**Compare files by->Compare checksum when needed**

If the files are identical in length and the date of the last change, then compare the checksum of the contents of the files
 
**Compare files by->Compare attributes**

If the files are identical in length, modification date and content, then compare attributes
 
**Compare files by->Compare by creation time**

When the size and last-modified time of a file are the same on both sides, the Task can use the creation time to decide which file is newer. Selecting this option on either side turns it on for the sync item. Available in VisualCron 13.1.1 and later.

![Source side options tab with the Compare by creation time option highlighted](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Sync%20Files%20Source%20Side%20Options%20Compare%20by%20Creation%20Time.png)
 
**Deleted/changed conflicts->Do not change**

Do nothing - do not change the situation.
 
**Deleted/changed conflicts->Set as master side for the changes**

When changes are detected on the other side - do not apply changes to this side
 
**Deleted/changed conflicts->Get the newest or larger changes**

If changes are detected on the other side, update the files if they are on the other side newer or larger
 
The *Same file/folder name conflicts* settings on this tab apply when the Task copies a file **from** this side to the other side.

**Same file/folder name conflicts->Do not change**

Do not change the situation.
 
**Same file/folder name conflicts->Add file to folder**

If the other side has a folder with the same name as the file (without its extension), the file is copied into that folder.
 
**Same file/folder name conflicts->Rename file**

If the other side has a folder with the same name as the file, or already has a file with that name, the file is copied with a new name and the existing file is kept. Files on the other side are therefore never overwritten, and the *Deleted/replaced files* options do not apply to them. You can choose how conflicting files are renamed:

- **Numeric mode** (default): Files are renamed with numeric suffixes (e.g. *file1.txt*, *file2.txt*).
- **Custom mask mode**: select *UseMask* and enter a pattern in *Include File Mask*. The pattern
  supports Variables. *UseMask* and *Include File Mask* are shared by both sides of the sync item: if
  *Rename file* is selected on the **_Destination side options_** tab, the mask entered there is used,
  and otherwise the mask on the **_Source side options_** tab is used. The file's extension is kept only
  when the pattern does not include one

![Source side options tab with Rename file selected, showing UseMask and Include File Mask](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Sync%20Files%20Source%20Side%20Options%20Rename%20File.png)

Global file rename settings can be reconfigured under _Main_ -> _Settings_ -> _Main Settings_.

![Settings window, Main settings tab, with the Renaming standard settings highlighted](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/File%20Rename%20settings.png)
 
**Destination->Destination side options** tab

![Add/Edit sync file item dialog, Destination side options tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Sync%20Files%20Destination%20Destination%20Side.png)

**Compare files by->Compare checksum when needed**

If the files are identical in length and the date of the last change, then compare the checksum of the contents of the files
 
**Compare files by->Compare attributes**

If the files are identical in length, modification date and content, then compare attributes
 
**Compare files by->Compare by creation time**

When the size and last-modified time of a file are the same on both sides, the Task can use the creation time to decide which file is newer. Selecting this option on either side turns it on for the sync item. Available in VisualCron 13.1.1 and later.

![Destination side options tab with the Compare by creation time option highlighted](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Sync%20Files%20Destination%20Side%20Options%20Compare%20by%20Creation%20Time.png)
 
**Deleted/changed conflicts->Do not change**

Do nothing - do not change the situation.
 
**Deleted/changed conflicts->Set as master side for the changes**

When changes are detected on the other side - do not apply changes to this side
 
**Deleted/changed conflicts->Get the newest or larger changes**

If changes are detected on the other side, update the files if they are on the other side newer or larger
 
The *Same file/folder name conflicts* settings on this tab apply when the Task copies a file **from** this side to the other side.

**Same file/folder name conflicts->Do not change**

Do not change the situation.
 
**Same file/folder name conflicts->Add file to folder**

If the other side has a folder with the same name as the file (without its extension), the file is copied into that folder.
 
**Same file/folder name conflicts->Rename file**

If the other side has a folder with the same name as the file, or already has a file with that name, the file is copied with a new name and the existing file is kept. The same renaming options as on the Source side apply: numeric suffixes or a custom mask. The custom mask (*UseMask* and *Include File Mask*) is shared by both sides of the sync item, and the mask entered on this tab is the one used when *Rename file* is selected here.

![Destination side options tab with Rename file selected, showing UseMask and Include File Mask](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Sync%20Files%20Destination%20Side%20Options%20Rename%20File.png)
 
**Log copy result to output**

When this setting is checked, the result, source and destination file is added to the Task output. All files that are copied is added to the output.

