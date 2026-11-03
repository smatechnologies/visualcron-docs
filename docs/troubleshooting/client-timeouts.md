---
sidebar_label: 'VisualCron Client Timeouts When Connecting'
hide_title: 'true'
---

## VisualCron Client Timeouts When Connecting

### Symptom

The Client waits for the Server and then times out, and the login does not appear.

### Cause

The two most common causes are:

- The VisualCron service was stopped, started or upgraded while the Client was connected, and the Server is not accepting connections yet
- Another program is already using the Server port (default "16444"), so the Server cannot listen on it

### Fix

#### The service was restarted or upgraded

To check the service, complete the following steps:

1. On the computer where the VisualCron Server is installed, open `services.msc`.
2. Check that the *VisualCron* service shows *Running*.
3. If it does not, right-click *VisualCron* and select *Start*.
4. If it is running but the Client still times out, wait until no Jobs are running, then right-click *VisualCron* and select *Restart*.
5. Wait about one minute, then connect again from the Client.

   The Client connects and shows the login.

#### The Server port is in use

To find the program that uses the port, complete the following steps:

1. On the Server computer, open the Server log `log_server<yyyyMMdd>.txt` in the log folder. By default the log folder is "C:\Program Files (x86)\VisualCron\log". See [Settings - Folders](../client-user-interface/server/settings-folders) if it was moved.
2. Look for "AddressAlreadyInUseException".

   When VisualCron can identify the other program, the log also contains a line that starts with `The process '<name>' with PID '<pid>' is already using port '<port>'`.

   If the entry has an inner exception, and the entry's own message contains "It is likely that certificate", the cause may be the Server certificate rather than another program. See [Certificate error in the log](i-cant-connect-to-visualcron-server#certificate-error-in-the-log). In that case the Server runs the same clean-up as *Delete certificates*, which shows a message before it removes anything. When the Server runs as the Windows service, that message cannot be shown, and nothing is removed. When the Server runs in the VisualCron Server window ("VisualCronService.exe" started by hand), every certificate in the computer's Personal store whose subject contains "vc" is removed, without further prompting. Before you open that window, check the store and export any certificate you need, as described on that page.

3. Stop or reconfigure the other program, or change the Server port on the ***Main settings*** tab of the *Settings* window (see [Main - Settings](../client-user-interface/server/main-settings)).

   If you change the port, update the port in the Server connection of each Client. Then check the inbound firewall rules for the new port. If a VisualCron rule allowed the old port, VisualCron moves that rule to the new port when you click *Apply settings*, and the moved rule allows any address. Limit it to the computers that run a Client, rather than adding another rule. If no rule exists, create an inbound TCP rule for the new port, only from those computers.

4. When no Jobs are running, restart the *VisualCron* service.
5. Connect again from the Client.

   The Server starts listening and the Client connects.

#### Collect a debug log for support

If neither cause applies, turn on *Extended debug logging*: on the ***Server*** tab, click *Settings*, then select it on the ***Settings*** tab of the ***Log settings*** tab (see [Settings - Log Settings](../client-user-interface/server/settings-log-settings)). Try to connect again, and send `log_server<yyyyMMdd>.txt` to [support@visualcron.com](mailto:support@visualcron.com). Review the log for user names, paths and server names before you send it.

If no Client can connect, you can turn the setting on in the settings file. To edit the settings file, complete the following steps:

1. When no Jobs are running, stop the *VisualCron* service.
2. Copy "settings_server.xml" from the settings folder (default "C:\Program Files (x86)\VisualCron\settings") to a safe location.
3. Start Notepad as an administrator, and open "settings_server.xml".

    :::warning

    Type "true" and "false" in lowercase only. The Server cannot read "True" and loads its backup or default settings instead. If that happens, stop the service and put back the copy you made in step 2.

    :::

4. Change `<ExtendedDebugging>false</ExtendedDebugging>` to `<ExtendedDebugging>true</ExtendedDebugging>`.
5. Save the file.
6. Start the *VisualCron* service.

   The Server writes debug entries to `log_server<yyyyMMdd>.txt`.

Turn *Extended debug logging* off when support is done, because it slows the Server.