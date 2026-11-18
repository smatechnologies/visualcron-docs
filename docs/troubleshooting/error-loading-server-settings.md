---
sidebar_label: 'Error Loading Server Settings'
hide_title: 'true'
---

## Error Loading Server Settings

### Symptom

The start-up log "server_startup.txt" in the log folder (default "C:\Program Files (x86)\VisualCron\log") contains:

```text
Error loading settings: System.IO.DirectoryNotFoundException: Could not find a part of the path '<folder>\settings_server.xml'.
```

### Cause

The registry value that tells the Server where its settings folder is points to a folder that does not exist.

### Fix

:::warning

While this error appears, the Server has loaded no users, and it may run with only the default user "admin" and no password. Anyone who can reach the Server can then log on as "admin". Block remote access to the Server, as in steps 1 and 2, until the fix is complete.

Editing the registry incorrectly can stop Windows or other programs from working. Change only the value named below, and export the key before you change it.

:::

To point the Server at its settings folder, complete the following steps:

1. On the Server computer, open Windows PowerShell as an administrator.
2. Create an inbound firewall rule that blocks the default Server port and Web API ports:

   ```powershell
   New-NetFirewallRule -DisplayName "VisualCron temporary block" -Direction Inbound -Protocol TCP -LocalPort 16444,8001,8002 -Action Block
   ```

   While this error appears, the Server may be using its default settings, or the settings from its last backup. Block the default ports "16444", "8001" and "8002" and any ports you changed, together, for example `-LocalPort 16444,8001,8002,17000`. Add the Web Client port (default "9000") if the Web Client is installed on this computer. A Block rule overrides any rule that allows the port.

3. When no Jobs are running, stop the *VisualCron* service.
4. Open `regedit` as an administrator.
5. Go to "HKEY_LOCAL_MACHINE\SOFTWARE\V-C".
6. Right-click "V-C" and select *Export* to save a copy of the key.
7. Double-click the string value "ServerSettingsFolder", and enter the folder that holds your existing settings files, such as "settings_server.xml" and "users.xml". By default this is the "settings" folder in the installation folder, "C:\Program Files (x86)\VisualCron\settings".

    :::warning

    Do not point the value at an empty folder. The Server would then start with no Jobs and no users, and would create the default "admin" user with no password.

    :::

8. Start the *VisualCron* service.

   The Server loads the settings from that folder, and the error no longer appears in "server_startup.txt".

9. Connect with the Client and check that your users and Jobs are back.
10. Remove the firewall rule:

    ```powershell
    Remove-NetFirewallRule -DisplayName "VisualCron temporary block"
    ```

When the Server is running, you can view the settings folder on the ***Folders*** tab. See [Settings - Folders](../client-user-interface/server/settings-folders).