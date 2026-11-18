---
sidebar_label: 'Multiple Clients on the Same Machine'
hide_title: 'true'
---

## Multiple Clients on the Same Machine

The VisualCron Client works best when its version matches the version of the Server it connects to, because new features can be added to either the Client or the Server. When the versions differ, the Client and the Server can misread each other, which can lead to unwanted settings or behavior.

The installer installs one version of the Client on a machine. When you install the Client and the Server together, they are always the same version.

If you need to connect to Servers of different versions from one machine, you can run another Client version from its own folder without installing it.

:::warning

All Client versions that one Windows user runs on a machine share the same Client settings folder, by default "%LOCALAPPDATA%\VisualCron\settings". This folder holds the Client settings and the server list, and every Client version reads and saves the same files. Back up this folder before you start a second Client version. If you change the folder on the ***Folders*** tab of _File_ -> _Settings_ -> _Client settings_, the change applies to every Client version of that Windows user.

:::

### Extract a Client version to its own folder

:::note

The steps below apply from version 12.2.1. For versions up to 12.1.4, extract the setup program (.exe) with 7-Zip instead of steps 1 to 4, and then copy the extracted folder to where you want it.

:::

To extract a Client version to its own folder, complete the following steps:

1. Download the custom installation package (.zip) for the Client version you need. See [Get VisualCron](get-visualcron.md).
2. Extract the .zip file to an empty folder.

   The package contains a folder named after the version, with "VisualCron.msi" inside.

3. Open Command Prompt as administrator.
4. Run an administrative installation into the folder where you want this Client version:

   ```cmd
   msiexec /a "<version folder>\VisualCron.msi" /qb TARGETDIR="<target folder>"
   ```

   The files are unpacked into the target folder. Nothing is installed on the machine, and no service is created.

5. In the target folder, right-click "VisualCronClient.exe" and select *Create shortcut*. On Windows 11, *Create shortcut* is under *Show more options*.
6. Move the shortcut to the desktop.
7. Rename the shortcut with the version number, for example "VisualCron - Client (12.3.1)".

:::note

The installer checks for .NET Framework 4.8, but a Client that you extract to a folder does not. Make sure the machine meets the [requirements](../requirements).

:::

### Run two Clients at the same time

By default, only one Client runs at a time in a Windows session, whatever its version. If you start a second Client, the Client that is already running comes to the front instead.

To allow more than one Client at the same time, complete the following steps:

1. In the running Client, go to _File_ -> _Settings_ -> _Client settings_.
2. On the ***Main settings*** tab, select *Allow multiple Client instances at the same time*.
3. Click *Apply settings*.

Every Client version of the same Windows user then accepts a second instance, because they share the same settings. See [Settings - Client Settings](../client-user-interface/file/client-settings).
