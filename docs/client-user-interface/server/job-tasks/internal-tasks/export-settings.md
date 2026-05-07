---
sidebar_label: 'Task Internal - Export Settings'
hide_title: 'true'
---

## Task Internal - Export Settings

The Export settings Task does the same thing as Client File > Import/Export > Export settings but this Task lets automatically backup the VisualCron settings.
 
VisualCron uses a number of XML files to store settings, these are located in the VisualCron settings folder (by default installation: C:\Program Files (x86)\VisualCron\settings). Export/backup is performed by the VisualCron Server that you are currently connected to. You may Export settings across the Internet.
 
It is recommended to perform regular backups/exports to this file. If a setting error occurs and a backup exists in the default backup file path, VisualCron will use the backup file and automatically restore settings. It is a recommendation that you keep a backup file both in the default folder and in another place.
 
VisualCron is automatically adding a Job with the *Export settings* Task and it is a recommendation to keep this Task in your Job list.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Internal%20Tasks/Export%20Settings.png)

**Credentials**

To control a remote computer you may need to use a Credential. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the *Settings* icon to open *Manage credentials* in order to add or edit Credentials.

**Export/backup settings**

**Use default storing path (enables automatic restore)** / **Specific file path**

Select where to store the backup file. Defaults to **Use default storing path (enables automatic restore)**, which saves to `C:\Program Files\VisualCron\backup\VC-Settings.zip`.
 
**Specific file path**

Enter the full file path for the backup file, or use the browse button to select a location. Only available when **Specific file path** is selected.

**Password**

Optional password to encrypt the export file.

**Export all server settings** / **Export the following settings**

Select which settings to export. Defaults to **Export all server settings**. It is recommended to back up all settings.

When **Export the following settings** is selected, choose from the following:

* **Jobs/Tasks**
* **Conditions**
* **Time exceptions**
* **Credentials**
* **Notifications**
* **Sync settings**
* **SSH Keys**
* **Internal settings**
* **Users permissions**
* **Connections**
* **PGP Key Rings**
* **Certificates**
* **Task repository objects**
* **Exit codes**
* **Manage File Transfer**
