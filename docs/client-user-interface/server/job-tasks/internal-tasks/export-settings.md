---
sidebar_label: 'Task Internal - Export Settings'
hide_title: 'true'
---

## Task Internal - Export Settings

The Export Settings Task does the same as *File* -> *Import/Export* -> [*Export settings*](../../../file/export-settings) in the Client, on a schedule.

The Server that runs the Task writes the file, so paths are on that Server. Settings are kept in XML files in the "settings" folder of the VisualCron installation.

Back up regularly, and keep a copy in another place as well. If a settings file cannot be read when the Server starts, VisualCron restores that setting from "VC-Settings.zip" in the "backup" folder of the installation. Exit codes are not restored this way (a damaged exit codes file restores Credentials from the backup instead), and a backup with a password cannot be read.

VisualCron adds a Job named "Backup settings" that runs this Task every day at 23:00 with the default settings. It is added once: if you delete it, it is not added again.

![Export Settings Task settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Internal%20Tasks/Export%20Settings.png)

**Credentials**

Optional. The Server writes the file as this Credential, for example to a network share. The user who saves the Task needs the *Execute* permission on the Credential. Select a Credential, or click the *Settings* icon to open [*Manage credentials*](../../../server/global-credentials).

**Export/backup settings**

*Use default storing path (enables automatic restore)* / *Specific file path*

Defaults to *Use default storing path (enables automatic restore)*: the file is "VC-Settings.zip" in the Server's *Backup folder*, set on the [***Folders***](../../../server/settings-folders) tab of the Server settings (by default the "backup" folder of the installation). Automatic restore reads only the file in the installation's "backup" folder, so if you change the *Backup folder*, automatic restore does not use this file.

With *Specific file path*, enter the full path of the file, or browse to it. Required; Variables can be used. To keep older backups, put a date in the file name, for example `VC-Settings-{DATEFORMAT(yyyy-MM-dd)}.zip`.

:::warning

The existing file is deleted before the export starts, so if the export fails, no backup is left at that path; with the default path, that is also the file automatic restore uses. Keep a second backup with another Export Settings Task that uses *Specific file path*.

:::

**Password**

Optional. Encrypts the file; the same password is needed to import it. With *Use default storing path (enables automatic restore)*, a password stops automatic restore from using the file.

*Export all server settings* / *Export the following settings*

Select which settings to export. Defaults to *Export all server settings*. It is recommended to back up all settings.

When *Export the following settings* is selected, choose from the following:

* *Jobs/Tasks*
* *Conditions*
* *Time exceptions*
* *Credentials*
* *Notifications*
* *Sync settings*
* *SSH Keys*
* *Internal settings*
* *Users permissions*
* *Connections*
* *PGP Key Rings*
* *Certificates*
* *Task repository objects*
* *Exit codes*
* *Manage File Transfer*

*Export all server settings* also exports *User groups*, *Network drives* and *Variables*, which are not in this list; to include them, use *Export all server settings*.
