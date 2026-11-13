---
sidebar_label: 'Task File - Copy Files'
hide_title: 'true'
---

## Task File - Copy Files

The Copy/Move file(s) Task lets you copy files easily based on file filters. Together with Credentials you are able to copy/move from/to network drives.

![Add Task dialog for the Copy files Task, with the list of copy items](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Copy%20File.png)

Use the toolbar buttons to add, edit, clone and delete copy items and to change their order. You can also right-click the grid and select *Add*, *Edit*, *Clone* or *Delete*.
 
One Copy files Task may contain several copy items. For each copy item a source folder, a file mask and a destination folders is defined.
 
Clicking on the Add option opens the File filter > Location tab.
 
**File filter > Location** sub tab

![Copy files Task with the Add/Edit copy file item dialog open on the file filter Location tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Copy%20File%20Location.png)

The [file filter](../../../server/job-tasks-file-filter) sub tab contains the standard [file filter](../../../server/job-tasks-file-filter). You use the file filter to "find" the files you want to copy.
 
**Copy settings** sub tab

![Add/Edit copy file item dialog, Copy settings tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Copy%20File%20Copy%20Settings.png)

In the copy settings sub tab you control destination folder, naming and what should happen if the file already exists.
 
**Credential**

To access a remote computer you may need to use a [Credential](../../../server/global-credentials). Normally that Credential is a remote or AD user with "Local logon" unchecked. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the Settings icon to open *Manage Credentials* in order to add or edit Credentials. This Credential is used to access the destination directory.
 
**Destination folder**

Specify an absolute path to the directory you want to copy to.
 
:::info Note 1 

When you are accessing a network drive (a folder on a remote computer) as source or destination folder you must specify the path in UNC format and not the letter of the logical drive. For example `Y:\remotefolder\` must be specified as `\\remoteservername\remotefolder\`.

:::

:::info Note 2

The folder path is not case-sensitive.

:::

:::info Note 3 

To speed up copying it is recommended that you group the items that are using the same Credential after each other. In this way, VisualCron does not need to switch between different (login) Credentials.

:::

**Destination file name mask**

You can use a wild card to replace the original name. For example `*.pdf` keeps the original name but changes the extension to "`pdf`". You can use `?` and `*` as wild card characters. ? replaces/matches a single letter. When using the Destination file name mask, including a folder path such as "`test\*`" will create a subfolder in the destination folder named "test" and place the files you copy, in to that folder.
 
**Post process mask with Variable**

This property gives you more advanced ways to change the file name. This option works best with *Destination file name mask* set to `"*"`. When checking this property the new name will be stored in a temporary Variable `{NEWNAME()}`. You will be able to use this Variable for processing with other Variable functions. The default value of this field is `"{STRING(Replace|{NEWNAME()}|oldValue|newValue)}"`, which uses the String.Replace function from the Variables window. It uses the `{NEWNAME()}` as input Variable with options to set a value that you want to replace from original file name "oldValue" and the new value "newValue".
 
**Overwrite if existing**

When this setting is checked, all matching files in the destination folder (older or newer) will be replaced by the source files.
 
**Overwrite if source file is newer**

When this setting is checked, the destination file (if existing) will only be replaced if the source file is newer.
 
**Don't overwrite if existing**

When this setting is checked no files are overwritten if they exist.
 
**Delete source file after copy**

When this option is selected, a source file is removed only after it has been copied successfully. If
the file does not exist in the destination folder, it is moved there. If it exists, the result depends
on the overwrite option:

| Overwrite option | Source file |
|---|---|
| *Overwrite if existing* (default) | Copied over the destination file, then deleted. |
| *Overwrite if source file is newer* | Deleted only if it was newer and was copied. Otherwise both files are kept. |
| *Don't overwrite if existing* | Kept. The destination file is not changed. |

A source file that is not copied is never deleted.

**Delete source empty sub folders**

When checked, any empty sub folders left in the source after copying are deleted. Only active when *Delete source file after copy* is checked. When the source is a single folder, that folder itself is not deleted.

**Create empty sub folders**

When checked, sub folders that exist in the source but contain no matching files are still created in the destination.
 
**Folder creation options**

*Create sub folders* — recreates the source sub folder structure in the destination (default).
*Create full folder structure* — when checked, creates the complete directory path from the root down. Only active when *Create sub folders* is selected.
*Don't create sub folders* — places all copied files directly in the destination folder without recreating any sub folder structure.
 
**Log copy result to output**

Selected by default. The destination path of each copied file is written to the Task's standard output,
one path per line. When a copy error is raised under the Task's **_On error_** settings, the file is written to standard
error with its source path, destination path and the error message. The list is also shown in a Client
that is watching the Task's output as it runs; when the Task copies many files over a slow connection,
you can clear this option.
 
### Troubleshooting

**Error 183 creating directory 'xxx': Cannot create a file when that file already exists**

Most likely the destination Credential is wrong.
 
**Writing thread not started**

1. check that you use Credentials when trying to access a share
2.  check that you use UNC paths like: `\\servername\folder`
3. if you use a Credential make sure that local login is unchecked in the Credential settings.
