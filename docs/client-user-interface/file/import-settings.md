---
sidebar_label: 'Import/Export - Import Settings'
hide_title: 'true'
---
## Import/Export - Import Settings

The ***File*** -> ***Import/Export*** -> ***Import settings*** option loads settings into the connected Server from a zip file made with [Export settings](export-settings). You need the Import settings permission.

![The Import settings window with the Zip backup file and Password fields and the import options](../../../static/img/Client%20User%20Interface/Main%20Menu/File/Import.png)

### Import settings window

- _Zip backup file_: the exported zip file. Click the browse button to select it. The Client reads the file as soon as you select it, so enter the _Password_ first. A file exported with _Default file path_ is `VC-Settings.zip` in the backup folder on the Server computer
- _Password_: the password the file was exported with, if any. If it is wrong, the Client asks for it again
- _Clear existing_: removes existing objects before the import; see the warning below
- _Update existing_: keeps the existing objects. An object in the file that has the same Id as an existing object updates it; other objects are added. Default
- _Import all server settings_: imports everything in the file. Default
- _Import the following settings_: imports only the types and objects you check in the list. The list shows what the file contains. You can change the _Group_ of a Job or other grouped object in the list to import it into another group, or a new one
- ***Start***: starts the import

The Client refuses a file that was exported from a Server with a different encryption type or certificate.

:::warning

With _Clear existing_ and _Import all server settings_, the Server first removes all existing Certificates, SSH keys, Conditions, Connections, Credentials, Jobs, Notifications, PGP key rings, Time exceptions, User groups, Users, Network drives, Variables, Exit codes, Task repository objects and Server sync settings objects, including types that are not in the file. Managed File Transfer servers and Server settings are not cleared; they are merged or replaced only when the file holds them.

With _Import the following settings_, a type is cleared only when its whole type row is checked. If you clear any object under a type, that type is not cleared, and the checked objects are added or updated.

Export the current settings first, so that you can restore them.

:::

:::warning

If Users are cleared and the file contains no users, the Server creates the default `admin` user with a blank password. Change that password at once.

:::

### Troubleshooting

**Access denied**

When you select the file, this error appears if the Client is not running as administrator or the password is missing.

1. Close the Client.
2. In the Client installation folder, right-click `VisualCronClient.exe`.
3. Click ***Run as administrator***.
4. If the file was exported with a password, enter it in _Password_.
5. Select the file again.

**Import keeps failing**

If the import keeps failing and you want to replace all settings on the destination Server, copy the settings files directly. The settings folder is set in the Server settings; see [Settings - Folders](../server/settings-folders).

:::warning

These steps replace all settings on the destination Server except its license and its Server settings. Copy the destination settings folder to a safe place first. Both Servers must use the same encryption type and certificate, or the Credentials and passwords cannot be decrypted.

:::

1. On the destination Server computer, stop the VisualCron service.
2. In the destination settings folder, delete all files except `license.xml` and `settings_server.xml`.
3. Copy all files except `license.xml` and `settings_server.xml` from the source settings folder to the destination settings folder.
4. Start the VisualCron service.
