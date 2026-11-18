---
sidebar_label: 'Import/Export - Export Settings'
hide_title: 'true'
---
## Import/Export - Export Settings

The ***File*** -> ***Import/Export*** -> ***Export settings*** option saves the settings of the connected Server to one zip file. Use the file as a backup, to copy settings to another Server with [Import settings](import-settings), or as part of a problem report. You need the Export settings permission.

:::tip

Export regularly, and keep a copy of the file away from the Server computer.

:::

If a settings file cannot be loaded when the Server starts, the Server tries to restore that setting from `VC-Settings.zip` in the `backup` folder of the Server installation. Recovery reads only that folder, and opens the file without a password.

:::warning

Start-up recovery cannot use an export that has a _Password_, or one written to a backup folder that was changed in [Settings - Folders](../server/settings-folders). To keep recovery working, also keep an export without a password in the `backup` folder of the Server installation, and store it securely.

:::

![The Export settings window with the Select settings list, the File path options and the Password field](../../../static/img/Client%20User%20Interface/Main%20Menu/File/Export.png)

### Export settings window

- _Select settings_: the object types to export: Certificates, Conditions, Connections, Credentials, Exit codes, Jobs, Managed File Transfer servers, Network drives, Notifications, PGP Key rings, Server settings, Server sync settings objects, SSH keys, Task repository objects, Time exceptions, User groups, Users and Variables. Expand a type to select single objects. ***Deselect all*** clears the list, and the fields under the list filter it
- _Default file path_: the Server writes `VC-Settings.zip` to its backup folder, on the Server computer. The default is the `backup` folder of the Server installation; see [Settings - Folders](../server/settings-folders). The path shown in the window is the backup folder of the Client, not where the file is written
- _Custom file path_: the Client saves the file to the path you enter or browse to, on the Client computer. An existing file with the same name is replaced
- _Password_: encrypts the zip file with this password. Enter the same password when you import
- ***Start***: starts the export. A message tells you when the export is complete

Unless there is a reason not to, export all settings; you can choose what to import later.

:::warning

_Default file path_ replaces any `VC-Settings.zip` that is already in the Server backup folder, without asking, and _Custom file path_ replaces an existing file at the path you enter. The previous export is lost. To keep earlier exports, use _Custom file path_ with a new file name.

:::

:::warning

The file holds the selected Credentials, Connections, Certificates and keys. Set a _Password_ and store the file securely.

:::
