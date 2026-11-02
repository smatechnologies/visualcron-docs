---
sidebar_label: 'I Forgot My Server Password'
hide_title: 'true'
---

## I Forgot My Server Password

### Symptom

You cannot log on to the Server because the password is lost.

### Cause

The password of your VisualCron user is lost. A user in the *Administrators* group can set a new one.

### Fix

First ask another user who is in the *Administrators* group to set a new password for you: on the ***Server*** tab, click *User permissions* (see [Main - User Permissions](../client-user-interface/server/main-user-permissions)).

If no other administrator can log on, you can reset the users file on the Server computer.

:::warning

This removes every user on the Server, internal and Active Directory, not only yours. The Server then creates the default user "admin" with no password. Until you set a password, anyone who can reach the Server through a Client, the Web API or the Web Client can log on as "admin", including other users who are signed in to the Server computer. Block remote access first, as in steps 1 and 2.

:::

To reset the users file, complete the following steps:

1. On the Server computer, open Windows PowerShell as an administrator.
2. Create an inbound firewall rule that blocks the Server port and, if the Web API is turned on, the Web API ports:

   ```powershell
   New-NetFirewallRule -DisplayName "VisualCron temporary block" -Direction Inbound -Protocol TCP -LocalPort 16444,8001,8002 -Action Block
   ```

   Leave out "8001" and "8002" if the Web API is not turned on. Add the Web Client port (default "9000") if the Web Client is installed on this computer. If you changed a port, use your port. A Block rule overrides any rule that allows the port, so it works even where no VisualCron rule exists.

3. Make sure that no other users are signed in to the Server computer.
4. Exit all VisualCron Clients.
5. When no Jobs are running, open `services.msc`, right-click *VisualCron* and select *Stop*.
6. Open the settings folder. By default this is "C:\Program Files (x86)\VisualCron\settings". If it was moved, the path is in the registry value "HKEY_LOCAL_MACHINE\SOFTWARE\V-C\ServerSettingsFolder".
7. Rename "users.xml" to "users.xml.bak". Do not delete it: keep it as a reference for re-creating the users.
8. In `services.msc`, right-click *VisualCron* and select *Start*.
9. Start the Client on the Server computer, and log on with user name "admin" and an empty password.
10. Set a password for "admin": on the ***Server*** tab, click *User permissions*.
11. Re-create the other users.
12. Remove the firewall rule:

    ```powershell
    Remove-NetFirewallRule -DisplayName "VisualCron temporary block"
    ```

    You can log on as "admin" with the new password, and other computers can connect again.