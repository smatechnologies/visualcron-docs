---
sidebar_label: 'Main - Settings'
hide_title: 'true'
---

## Main - Settings

The Server settings window holds the settings that apply to the whole Server. Open it from the main menu ***Server*** -> ***Main settings*** -> ***Settings***. You need the "Server settings" permission with "Read" to open the window, and with "Edit" to save changes with ***Apply settings*** (see [Main - User Permissions](main-user-permissions)).

The window has these tabs:

- **_Main settings_**: described on this page
- **_Default flows_**: see [Settings - Default Flows](settings-default-flows)
- **_Users/Logon_**: see [Settings - Users/Logon](settings-users-logon)
- **_Log settings_**: see [Settings - Log Settings](settings-log-settings)
- **_Email settings_**: see [Settings - Email Settings](settings-email-settings)
- **_Proxy_**: see [Settings - Proxy](settings-proxy)
- **_Folders_**: see [Settings - Folders](settings-folders)
- **_Web API_**: see [Settings - Web API](settings-web-api)
- **_Web Client_**: see [Settings - Web Client](settings-web-client)
- **_Password rules_**: see [Settings - Password Rules](settings-password-rules)

Most changes take effect on the Server when you click ***Apply settings***. ***Cancel*** closes the window without saving them.

These buttons act on the Server at once, without ***Apply settings***, and ***Cancel*** does not undo them:

- The firewall button next to _Server port_ and the UAC button, on the **_Main settings_** tab
- ***Add to all existing*** and ***Delete from all existing***, on the **_Default flows_** tab
- ***Create DB tables***, ***Clear all***, ***Recreate table*** and ***Rebuild indexes***, on the **_Log settings_** tab

The buttons on the **_Web Client_** tab also act at once, on the computer where the Client runs.

:::warning

The buttons in the list above do not check the "Edit" permission. Any user who can open this window can use them, for example to delete log data or to remove the firewall rule. Give the "Server settings" permission only to users you trust with these actions.

:::

***Server*** -> ***Main settings*** -> ***Settings*** -> **_Main settings_** tab

![The Main settings tab of the Server settings window, with Installed in cluster environment, Server port 16444 and the Firewall allows button, HTTP settings, Default exit code collection, Renaming standard, Server language, UAC - set UAC status and Assembly resolving options](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Main%20Settings.png)

### Installed in cluster environment

Check _Installed in cluster environment_ when VisualCron is installed in a Windows failover cluster, on two nodes that share a drive. See [Using VisualCron in a clustered environment](../../using-visualcron/using-visualcron-in-a-clustered-environment).

### Server port

Clients on other computers connect to the Server on this TCP port, with encrypted traffic. The default is "16444". To change it, enter a new port number.

VisualCron does not open the port in Windows Firewall by itself. The button next to _Server port_ shows ***Firewall allows*** when VisualCron's own inbound rule for the port exists, and ***Firewall denies*** when it does not. Click ***Firewall denies*** to create the rule, and ***Firewall allows*** to remove it. A rule you created yourself under another name is not detected. The rule that VisualCron creates is named `VisualCronService - <port>` and allows connections from any remote address. To allow only the computers that run a Client, limit the rule's remote addresses in Windows Defender Firewall (see [Firewall and network](../../get-visualcron/antivirus-exclusions#firewall-and-network)).

When you save a new port value while the button shows ***Firewall allows***, VisualCron removes its rule for the old port and creates a new rule, `VisualCronService - <port>`, for the new port. The new rule allows connections from any remote address, also when you had limited the old rule, so limit its remote addresses again after a port change. If VisualCron cannot create the new rule, it creates the rule for the old port again, also open to any remote address, and the new port is still saved: no VisualCron rule then allows the new port. If the button shows ***Firewall denies***, no rule is created for the new port. See [Port and firewall](../../using-visualcron/visualcron-server#port-and-firewall).

The firewall button acts at once, without ***Apply settings***. A new port takes effect as soon as you click ***Apply settings***: the Server starts listening on the new port. Clients that connect from another computer must then use the new port. Change it in their server connection in ***File*** -> ***Servers*** -> ***Manage Servers*** (see [Servers - Manage Servers](../file/manage-servers)).

:::note

If you change the port from a Client on another computer, that Client's own connection to the Server is closed. Update its server connection with the new port and connect again.

:::

### HTTP settings

_Override HTTP connection limit_ sets how many HTTP connections the Server can have open to the same host at the same time. This matters when many HTTP requests run at once, for example from the HTTP Task. The option is checked by default with a limit of "500". You can enter a value from 2 to 10000. When the option is unchecked, the .NET default limit applies.

:::note

The Server reads this setting only when the VisualCron service starts. After you change it, restart the VisualCron service.

:::

### Default exit code collection

The exit code collection that is selected by default on the ***On error*** tab of new Tasks. The default is "Windows (default)".

### Renaming standard

Some Tasks can rename files with a mask. Choose how masks are applied:

- _VisualCron implementation_ (default): VisualCron's own renaming rules, which adjust some rules of the Windows REN command
- _REN command standard_: the renaming rules of the Windows REN command

_Source_, _Mask_ and _Result_ let you try a mask: enter a file name in _Source_ and a mask in _Mask_, and _Result_ shows the renamed file name. _Result_ is calculated with the VisualCron implementation, also when _REN command standard_ is selected.

### Server language

The language the Server uses for the texts it writes, for example in its logs. The default is "English". The new language is used as soon as you click ***Apply settings***.

### UAC - set UAC status

The button shows whether User Account Control (UAC) is turned on for the Server computer: ***UAC is enabled*** or ***UAC is disabled***. Click it to switch UAC on or off. The button changes the Windows setting at once, without ***Apply settings***, and the change takes effect after you restart the computer. If VisualCron cannot read the status, the button shows ***UAC is enabled*** and the error is written to the Client log.

:::warning

Turning UAC off lowers the security of the whole computer, not only of VisualCron. Turn it off only if your security policy allows it.

:::

### Assembly resolving options

Some Tasks use optional component files that are not installed with VisualCron. When a Task needs one of these files and it is missing, the Server can download it from the VisualCron website into the VisualCron installation folder (by default `C:\Program Files (x86)\VisualCron` on 64-bit Windows) and load it. The Server computer must then be able to reach the VisualCron website.

:::note

In the current version, the Server downloads these files only while _Auto download missing dependencies_ is unchecked. While it is checked, the Server does not download them. Check the current state of the option on your Server.

:::

- If your policy does not allow the Server to download files from the Internet, check _Auto download missing dependencies_ and click ***Apply settings***.
- If a Task fails because a component is missing, and your policy allows downloads, uncheck the option and click ***Apply settings***.
