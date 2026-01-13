---
sidebar_label: 'Task File - Copy  Files'
hide_title: 'true'
---

## Task File - Copy Files

The Copy/Move file(s) Task lets you copy files easily based on file filters. Together with Credentials you are able to to copy/move from/to network drives.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Copy%20File.png)

In the Copy files dialog you add, edit, clone or delete copy items and change order of copy items. Changes may be done either by the toolbar buttons or mouse right click on the grid.
 
One Copy files Task may contain several copy items. For each copy item a source folder, a file mask and a destination folders is defined.
 
Clicking on the Add option opens the File filter > Location tab.
 
**File filter > Location** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Copy%20File%20Location.png)

The [file filter](../../../server/job-tasks-file-filter) sub tab contains the standard [file filter](../../../server/job-tasks-file-filter). You use the file filter to "find" the files you want to copy.
 
**Copy settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Copy%20File%20Copy%20Settings.png)

In the copy settings sub tab you control destination folder, naming and what should happen if the file already exists.
 
**Credential**

To access a remote computer you may need to use a [Credential](../../../server/global-credentials). Normally that Credential is a remote or AD user with "Local logon" unchecked. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the Settings icon to open *Manage credentials* in order to add or edit Credentials. This Credential is used to access the destination directory.
 
**Destination folder**

Specify a absolute path to the directory you want to copy to.
 
:::info Note 1 

When you are accessing a network drive (a folder on a remote computer) as source or destination folder you must specify the path in UNC format and not the letter of the logical drive. For example `Y:\remotefolder\` must be specified as `\\remoteservername\remotefolder\`.

:::

:::info Note 2

The folder path is not case-sensitive.

:::

:::info Note 3 

To speed up copying it is recommended that you group the items that are using the same credential after each other. In this way, VisualCron does not need to switch between different (login) credentials.

:::

**Destination file name mask**

You can use a wild card to replace the original name. For example `*.pdf` keeps the original name but changes the extension to "`pdf`". You can use `?` and `*` as wild card characters. ? replaces/matches a single letter. When using the Destination file name mask, including a folder path such as "`test\*`" will create a subfolder in the destination folder named "test" and place the files you copy, in to that folder.
 
**Post process mask with Variable**

This property gives you more advanced ways to change the file name. We recommend that you use Destination file mask with value `*` when using this property. When checking this property the new name will be stored in a temporary variable `{NEWNAME()}`. You will be able to use this Variable for processing with other Variable functions. As an example we have provided the default value for this property: `{STRING(Replace|{NEWNAME()}|oldValue|newValue)}`. The example uses the String.Replace method from the Variables window. It uses the `{NEWNAME()}` as input Variable with options to set a value that you want to replace from original file name "oldValue" and the new value "newValue".
 
**Overwrite if existing**

When this setting is checked, all matching files in the destination folder (older or never) will be replaced by the source files.
 
**Overwrite if source file is newer**

When this setting is checked, the destination file (if existing) will only be replaced if the source file is newer.
 
**Don't overwrite if existing**

When this setting is checked no files are overwritten if they exist.
 
**Delete source file after copy**

When this setting is checked, the source file (not the folder) will be deleted after a successful copy. Thus, the source file will be deleted even though it wasn't copied due to the settings of *Overwrite if existing* (if it was already existing) and *Overwrite if source file is newer* (if the source file was older than the destination).
 
**Folder creation options**

1. Create full folder structure
Creates the full directory structure from root folder and up.
2. Don't create sub folders
Puts all files in in the same (destination) folder
 
**Log copy result to output**

When this setting is checked, the result, source and destination file is added to the Task output. All files that are copied is added to the output.
 
The output has the following format: Source file path TAB -> TAB Destination file path TAB OK/FAILED
 
Both OK and FAILED files are added to the Task output. To the Task std. error only the failed items are added.
 
This setting is not default as it adds some extra information to send between the server and the client. Use this option only if you have a high speed connection, connecting locally or have a small amount of files.
 
### Troubleshooting

**Error 183 creating directory 'xxx': Cannot create a file when that file already exists**

Most likely the destination Credential is wrong.
 
**Writing thread not started**

1. check that you use Credentials when trying to access a share
2.  check that you use UNC paths like: `\\servername\folder`
3. if you use a Credential make sure that local login is unchecked in the Credential settings.