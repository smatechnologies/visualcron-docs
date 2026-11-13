---
sidebar_label: 'Upgrading Versions'
hide_title: 'true'
---

## Upgrading Versions

Keep the Client and the Server on the same, current version. This page helps you plan an upgrade, back up your settings first, and go back if you need to. For the upgrade itself, see [Download, Install, Upgrade, and Uninstall](download-install-upgrade-uninstall).

When you plan an upgrade, consider these approaches:

- If you are several major versions behind, consider [upgrading one major version at a time](#upgrade-one-major-version-at-a-time)
- [Test the new version in a test environment](#test-in-a-test-environment) first

### Upgrade one major version at a time

The setup program removes whichever VisualCron version is installed and installs the new one, so the installer does not need intermediate versions. Each major version can still change how some Jobs, Tasks and connections behave. If you are several major versions behind, you can upgrade one major version at a time and check your Jobs after each step. This makes it easier to see which version changed a behavior.

### Test in a test environment

Install the new VisualCron version on a test computer, with *VisualCron Client and Server*, and import the settings from your production Server. The export contains your Credentials and connections, and imported Jobs can reach the same systems as production.

:::warning

Imported Jobs can run on the test Server as soon as the Server is on. Turn the test Server off before you import, and keep it off until you have reviewed the imported settings. If you import *Server settings*, the test Server takes the on or off status from the file, which is "On" for a production Server. Where possible, also make sure that the test Server cannot reach production systems.

:::

To set up the test Server, complete the following steps:

1. Install VisualCron on the test computer, as described in [Download, Install, Upgrade, and Uninstall](download-install-upgrade-uninstall).
2. Secure the "admin" user on the test Server, as described in [Secure the admin user](download-install-upgrade-uninstall#secure-the-admin-user).
3. Go to _Server_ -> _Main settings_, and click _Server [On]_.

   The button shows *Server [Off]*, and the test Server stops running Jobs.

4. Go to _File_ -> _Import/Export_ -> _Import settings_.
5. If the export file has a password, enter it in *Password*.
6. In *Zip backup file*, select the export file from production.
7. Select *Update existing* or *Clear existing*.

   With *Import the following settings*, *Clear existing* deletes only the types that you select, before the import.

8. Select *Import the following settings*.

   All types are unchecked.

9. Check every type except *Server settings*, so that the test Server stays off.
10. Click *Start*.
11. Check that the "admin" user still has a password, in _Server_ -> _Main settings_ -> _User permissions_.
12. Review the imported Credentials and connections, and change them to test systems where needed.
13. Deactivate the Jobs that must not run on the test Server.
14. Click *Server [Off]* to turn the test Server on.

For the import options, see [Restore the backup](#restore-the-backup).

### What an upgrade keeps and changes

An upgrade with the setup program keeps your Server settings and the installation folder. It sets the startup type of the VisualCron service to "Automatic" and starts the service, unless you select *VisualCron Client only*. It also resets the account that the service runs as to Local System; if the service ran under a Windows account, the setup program asks for that account's password. The MSI package does not ask: after a silent upgrade, set the account again. For details, see [Download, Install, Upgrade, and Uninstall](download-install-upgrade-uninstall#upgrade-visualcron).

### Back up before you upgrade

To export the Server settings, complete the following steps:

1. In the Client, connect to the Server that you are about to upgrade.
2. Go to _File_ -> _Import/Export_ -> _Export settings_.

   ![File tab of the Client with the Export settings button in the Import/Export group](../../static/img/Get%20VisualCron/Download%20Install%20Upgrade%20and%20Uninstall/Export%201.png)

   The *Export settings* window opens.

3. Under *Select settings*, make sure that every setting is checked.
4. Under *File path*, select *Custom file path*.
5. Enter a path outside the VisualCron installation folder.

   The default file path is in the backup folder of the installation folder.

6. In *Password*, enter a password to protect and encrypt the file. Keep the password: you need it to import the file.
7. Click *Start*.

   ![Export settings window with all settings checked, the file path options, the Password box and the Start button](../../static/img/Get%20VisualCron/Download%20Install%20Upgrade%20and%20Uninstall/Export%202.png)

   The Client writes the selected settings to one .zip file.

The setup program also copies the Server settings files to a backup folder in the Windows temporary folder before it removes the installed version. Rely on your export file as the backup.

For the export options, see [Import/Export - Export Settings](../client-user-interface/file/export-settings).

### Restore the backup

:::warning

*Clear existing* together with *Import all server settings* deletes every type of setting on the Server before the import, including users, Credentials and Jobs, whether or not the file contains that type. Use that combination only with a file that contains every setting. For a file with only some settings, select *Update existing*, or select *Import the following settings* and choose the types. After any import, check that the "admin" user still has a password.

:::

To import the settings, complete the following steps:

1. In the Client, connect to the Server.
2. Go to _File_ -> _Import/Export_ -> _Import settings_.

   ![File tab of the Client with the Import settings button in the Import/Export group](../../static/img/Get%20VisualCron/Download%20Install%20Upgrade%20and%20Uninstall/Import.png)

3. If the export file has a password, enter it in *Password*.
4. In *Zip backup file*, select the export file.
5. Select *Update existing*, or *Clear existing* only for a full export, as described in the warning above.
6. Select *Import all server settings*, or select *Import the following settings* and check the types to import.
7. Click *Start*.

   The Client sends the selected settings to the Server, which imports them.

   ![Import settings window with the zip backup file, Password, Clear existing and Update existing, the settings list and the Start button](../../static/img/Get%20VisualCron/Download%20Install%20Upgrade%20and%20Uninstall/Import%20Settings.png)

8. Check that the "admin" user still has a password, in _Server_ -> _Main settings_ -> _User permissions_.

For the import options, see [Import/Export - Import Settings](../client-user-interface/file/import-settings).

### Return to the previous version

To go back to the version you had before the upgrade, complete the following steps:

1. Run the setup program of the previous version.

   The pre-installer removes the installed version and installs the previous one. The settings folder is kept.

2. In the Client, connect to the Server.
3. Import the export file that you made before the upgrade, with *Clear existing* and *Import all server settings*, as described in [Restore the backup](#restore-the-backup).
4. Check that the "admin" user still has a password.
5. Check that your Jobs run as expected.
