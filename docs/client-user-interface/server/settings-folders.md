---
sidebar_label: 'Settings - Folders'
hide_title: 'true'
---

## Settings - Folders

The **_Folders_** tab shows the folders the Server uses for its logs, settings, backups, output and temporary files. Change a folder here when you need the data on another drive, for example because of disk space. This tab is one of the tabs of the Server settings window (see [Main - Settings](main-settings)).

_Server_ -> _Main settings_ -> _Settings_ -> **_Folders_** tab

![The Folders tab with the Log folder, Settings folder, Backup folder, Output cache folder and Temp folder, each with a folder button and an Open button](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Folders.png)

Each folder has a folder button to browse for a new folder, and an _Open_ button. When the Client runs on the Server computer, _Open_ opens the folder in Windows Explorer. When the Client is connected to a Server on another computer, _Open_ and the folder button both open a window that browses the folders of the Server computer, and you can select a new folder there. Browsing needs the "Remote File Explorer" permission. Changes take effect when you click _Apply settings_.

### Log folder

The folder of the Server log files, one file per day, named "log_server`<yyyyMMdd>`.txt". The default is the "log" folder in the VisualCron installation folder. When you change it, the Server writes its log to the new folder from then on. Existing log files stay in the old folder.

### Settings folder

The folder that holds the Server settings, Jobs and other objects. The default is the "settings" folder in the VisualCron installation folder. When you change it, the Server saves all its settings to the new folder at once and uses that folder from then on, also after a restart.

### Backup folder

The folder where the built-in Job "Backup settings" saves its backup. That Job runs every day at 23:00 and replaces the file "VC-Settings.zip" in this folder each time. The default is the "backup" folder in the VisualCron installation folder. See [Task Internal - Export Settings](job-tasks/internal-tasks/export-settings).

### Output cache folder

The folder for temporary Task output. Its "log" subfolder holds the internal log database, "VisualCron4.sdf" (see [Settings - Log Settings](settings-log-settings)). The default is "C:\ProgramData\VisualCron\output".

:::warning

When you change the _Output cache folder_, the Server moves the internal log database to the "log" subfolder of the new folder. If a file named "VisualCron4.sdf" already exists there, it is deleted first. Before you change the folder, make sure the new folder does not contain a log database you want to keep.

:::

### Temp folder

The folder for temporary files of Tasks. The default is the "VisualCron" folder in the Windows temporary folder of the account the VisualCron service runs as. About every 11 hours, counted from when the VisualCron service started, the Server deletes the files directly in this folder (not in its subfolders) that were created more than one day ago. Do not keep files you need in this folder.