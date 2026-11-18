---
sidebar_label: 'Antivirus and Endpoint Protection Exclusions'
hide_title: 'true'
---

## Antivirus and Endpoint Protection Exclusions

VisualCron is a scheduling and automation product. By design it writes to disk continuously, keeps a database file open for as long as the service runs, watches folders for changes, and starts child processes to run Tasks. Real-time antivirus scanners and endpoint detection and response (EDR) products are built to inspect these behaviors.

VisualCron runs with antivirus software active, and there is no requirement to turn protection off. Without any exclusions, you may see file locking, slow Job execution, missed File Triggers, or quarantined VisualCron components.

This page lists what VisualCron uses, so that your security team can decide which exclusions to apply. Every exclusion reduces coverage. Apply the narrowest set that resolves the behavior you see, and review it with whoever owns endpoint security in your organization.

### Quick version

For a stable server that stays protected:

1. Set a password for the "admin" user, as described in [Secure the admin user](download-install-upgrade-uninstall#secure-the-admin-user).
2. Exclude only the VisualCron output, settings, log and database files listed in [Folders to exclude](#folders-to-exclude).
3. Keep scanning the folders where files arrive from outside, including received email, the temporary folders where VisualCron writes scripts, and the program folders. See [Folders to keep scanned](#folders-to-keep-scanned).
4. Allow the VisualCron executables to run, without excluding the files they open from scanning. See [Processes to allow](#processes-to-allow).
5. If Clients connect from other computers, allow inbound TCP 16444 only from those computers. See [Firewall and network](#firewall-and-network).

The rest of this page explains each item.

### Confirm your actual paths first

Several of the folders below can be changed, and they may have been changed on your server. Before you apply exclusions, read the current values in the Client: go to _Server_ -> _Main settings_ -> _Settings_, and open the ***Folders*** tab. See [Settings - Folders](../client-user-interface/server/settings-folders) for a description of each folder.

The paths on this page are the defaults for a standard installation. The default installation folder is "C:\Program Files (x86)\VisualCron" on 64-bit Windows and "C:\Program Files\VisualCron" on 32-bit Windows, or the folder chosen during installation.

### Folders to exclude

VisualCron writes these files. They change often, and a scanner that locks them can slow Jobs down or damage the log database. Task output stored in them can contain data that came from outside VisualCron, but VisualCron stores it as XML and does not run it.

| Folder or files | Default | Contents |
|---|---|---|
| Output cache files | "C:\ProgramData\VisualCron\output\*.xml" and "C:\ProgramData\VisualCron\output\log\VisualCron4.sdf" | One XML file for each Task output and each Job and Task result, created and deleted as Jobs run, and the built-in log database "VisualCron4.sdf" |
| Settings folder | `<installation folder>\settings` | "settings_server.xml", "jobs.xml", "users.xml" and the other Server settings files, written on every settings change |
| Log folder | `<installation folder>\log` | Server log files, for example `log_server<date>.txt`, written while the service runs |
| Web Client database, only if the Web Client is installed | `<installation folder>\WebClient\App_Data` | "VCWeb.sdf" |

Exclude the output cache files, not the output cache folder. VisualCron does not restrict access to this folder, so it has the default permissions of "C:\ProgramData", and other users of the computer may be able to create files in it. A folder exclusion would leave those files unscanned.

Do not exclude the whole installation folder, and do not exclude the `data` subfolder. The `data` folder holds received email (see the next section).

The output cache files matter most. On a busy server the output cache folder sees a high rate of file creation and deletion. When the log database is the built-in one, the service keeps "VisualCron4.sdf" open for as long as it runs. A scanner that locks this file, even briefly, can cause logging errors, slowdowns or a damaged database. If you exclude only one item, exclude these files.

#### Client folders

On computers where the Client runs, each Windows user has these folders:

| Folder | Contents |
|---|---|
| "%LOCALAPPDATA%\VisualCron\settings" | Client settings and the server list |
| "%LOCALAPPDATA%\VisualCron\log" | Client log files |

They are written far less often than the Server folders. Exclude them only if a scanner blocks the Client itself. The Client settings folder can be moved on the ***Folders*** tab of _File_ -> _Settings_ -> _Client settings_.

### Folders to keep scanned

Do not exclude these folders. Files that come from outside VisualCron arrive in them, or VisualCron runs code from them.

| Folder | Why it stays scanned |
|---|---|
| `<installation folder>\data\triggers\mail`, and any other save location set on a Mail Trigger | The Mail Trigger saves each received message and its attachments here |
| Folders that your Jobs read from or write to, including folders watched by a File Trigger | They often receive files from other systems or other organizations |
| The temp folder of the service account, and the VisualCron temp folder inside it, by default "%TEMP%\VisualCron" ("C:\Windows\Temp\VisualCron" when the service runs as Local System) | The Server writes scripts there and then runs them, for Execute Tasks with batch content and Execute Script Tasks with an inline script. Cloud Transfer Sync Tasks also stage downloaded files there. VisualCron deletes files older than one day from its own temp folder |
| The installation folder and its program subfolders, for example `x64\sqlce`, `x86\sqlce`, `PowerShell`, `MSSQL2005` to `MSSQL2025`, `MSSQLSSISDB` and `VCCommand` | They hold the VisualCron programs. The Server and the Client also save components downloaded from the VisualCron website there. See [Assembly Resolver](assembly-resolver) |
| "C:\ProgramData\VisualCron\Tasks" | It holds a copy of "VisualCronWebMacro.exe" |

VisualCron uses the Windows file system watcher to detect changes in folders watched by a File Trigger. An antivirus product that scans a file as it lands in a watched folder can hold a lock on it. The usual symptoms are "file in use" or access denied errors in the Task that follows the Trigger, or a Trigger that fires against a file that cannot be opened yet. See [If a scanner locks files as they arrive](#if-a-scanner-locks-files-as-they-arrive).

#### If a scanner locks files as they arrive

If a scan of a newly arrived file makes the next Task fail, change how the file is scanned rather than turning scanning off for the folder:

- Ask your security team whether the product can scan files when they are closed rather than when they are opened
- On the File Trigger, increase *Consolidate changes (milliseconds)*, so that the Trigger fires only after the file has stopped changing
- Set the Task to retry on error, so that it tries again after the scan has finished

### Processes to allow

VisualCron runs as a Windows service named "VisualCron", with the display name "VisualCron". The service executable is "VisualCronService.exe".

On this page, allowing a process means that your security product does not block, quarantine or raise behavioral alerts for that executable. It does not mean excluding the files that the process opens from scanning.

:::warning

Do not add the VisualCron executables as process exclusions in the sense of "do not scan files opened by this process". The service reads and moves the files that your Jobs receive and runs the scripts that your Tasks write, so such an exclusion would stop scanning in every folder listed under [Folders to keep scanned](#folders-to-keep-scanned).

:::

To run many Tasks, the service starts a separate helper executable instead of doing the work itself. Behavioral detection engines can flag a long-running service that starts short-lived child processes, so you may need to allow the VisualCron executables explicitly.

All of these executables are in the VisualCron installation folder. "VisualCronWebMacro.exe" also has a copy in "C:\ProgramData\VisualCron\Tasks". Most of them are signed by "NetCart AB". Before you create a rule based on the signer, check the signer of the files in your installation: right-click the file, select *Properties*, and open the ***Digital Signatures*** tab. Limit any signer rule to the VisualCron installation folder, so that it does not trust the same signer everywhere in your organization.

If your security product needs named processes, the main ones are:

| Executable | Role |
|---|---|
| "VisualCronService.exe" | The VisualCron Server service |
| "VisualCronClient.exe" | The VisualCron Client |
| "VCTray.exe" | The Tray Client |
| "ServerLauncher.exe" | Starts and monitors Server instances |
| "Restarter.exe" | Restarts the service |
| "InstallController.exe" | Used by the installer |
| "vcu.exe" | Uninstaller |
| `VCCommand\VCCommand.exe` | Command-line interface |
| `PowerShell\TaskPowerShell.exe`, `PowerShell\TaskPowerShellx86.exe` | PowerShell Task |
| "TaskNETCode.exe" | .NET Code Task |
| "NETExecute40.exe", "NETExecute40x86.exe" | Assembly Execute Task |
| "TaskUnmanagedExecute.exe", "TaskUnmanagedExecutex86.exe" | Unmanaged DLL Execute Task |
| "TaskOfficeMacro.exe", "TaskOfficeMacrox86.exe" | Office Macro Task |
| `MSSQL<version>\SSISExecute<version>.exe` and the x86 versions, `MSSQLSSISDB\SSISDBExecute.exe` | SSIS Tasks, one for each SQL Server version |
| "AS400Execute.exe" | AS/400 Task |
| "VisualCron.WebBrowser.exe", "VisualCronWebMacro.exe" | Web browser automation |
| "LockWorkStationNet.exe" | Lock Workstation Task |
| "VirtualServerTasks.Core.Launcher.exe" | Virtual server Tasks |
| "AcquireBearerTokenByUserCredential.exe" | VMware vSphere Tasks |

Define these rules by full path in the installation folder, or by signer together with that path, never by file name alone. Local users can write to the copy of "VisualCronWebMacro.exe" in "C:\ProgramData\VisualCron\Tasks", so do not cover that copy with an allow rule.

VisualCron also ships or uses a few third-party tools that antivirus products flag more often than the VisualCron files themselves:

- "7z.dll" and "7z64.dll", in the installation folder, used by compression Tasks
- "7z.exe", in the installation folder, used for packaging during remote installation
- "jq-win32.exe" and "jq-win64.exe", in the installation folder, used for JSON processing
- "makecert.exe", in the `cert` subfolder, and "installutil.exe" and "msicuu2.exe", in the `install` subfolder, which are installed with VisualCron as support tools
- "PsExec.exe" and "PsExec64.exe", which are not installed as files. The Client writes them to its installation folder only when you use remote installation, and leaves them there until the next remote command. See [PsExec](#psexec)

### Firewall and network

#### Inbound

| Port | Protocol | Purpose | Listens by default |
|---|---|---|---|
| 16444 | TCP | Client and API connections to the VisualCron Server | Yes |
| 8001 | TCP | Web API over HTTP | No, only when *Allow Web API* is selected |
| 8002 | TCP | Web API over HTTPS | No, only when *Allow Web API* is selected |
| 9000 | TCP | Web Client, default port | No, only when the Web Client is installed |

The installer creates no firewall rule. A Client on the same computer as the Server does not need one. The Server port can be changed in the *Server port* setting, so confirm the value on your server before you create a rule. Ports that you configure yourself, for example for MFT servers or HTTP Triggers, need their own rules.

:::warning

A new Server has the user "admin" with no password. Anyone who can reach the Server port, including users signed in to the Server computer, can sign in as "admin". Set a password for "admin" first, as described in [Secure the admin user](download-install-upgrade-uninstall#secure-the-admin-user), before you open port 16444 to other computers. Do this from a Client on the Server computer itself, or from a computer that the firewall already allows.

:::

To let Clients on other computers connect, complete the following steps:

1. Check that the "admin" user has a password.
2. Go to _Server_ -> _Main settings_ -> _Settings_.
3. On the ***Main settings*** tab, click *Firewall denies*.

   The button changes to *Firewall allows*, and Windows Firewall gets an inbound rule named `VisualCronService - <port>`, for example "VisualCronService - 16444". This rule allows connections from any address.

4. Limit the remote addresses of the rule to the computers that run a Client. Use one of the following:

   - In Windows Defender Firewall with Advanced Security, open the properties of the rule, and on the ***Scope*** tab, add the Client computers under *Remote IP address*
   - In PowerShell opened as administrator, run the command below

   ```powershell
   Set-NetFirewallRule -DisplayName "VisualCronService - <port>" -RemoteAddress <addresses>
   ```

The rule now allows only the computers that you listed.

:::warning

If you change *Server port* later, VisualCron removes the rule and creates a new one for the new port that allows any address. Limit the remote addresses again after every port change. Clicking *Firewall allows* removes the rule.

:::

#### Outbound

VisualCron contacts "www.visualcron.com" on TCP 443 for license activation, deactivation and validation, trial registration, version checks, translation files, error reports and reporting.

VisualCron also downloads missing components from "www.visualcron.com":

- The Server, while *Auto download missing dependencies* is cleared
- The Client, from the *Assembly resolver - missing files* window

The Server and the Client use different paths on the site, so allowlist the host rather than a path. To stop the Server from downloading components, select *Auto download missing dependencies*. See [Assembly Resolver](assembly-resolver).

If you use the VisualCron mobile app, the Server also contacts "cloud.visualcron.com".

If your environment uses an intercepting web proxy or TLS inspection, allowlist "www.visualcron.com" and "cloud.visualcron.com". Beyond those, VisualCron only makes the outbound connections that your own Jobs ask for, for example to an SFTP server or a mail server.

### Installation time detections

These detections are expected during installation or remote installation.

#### PsExec

PsExec is a Microsoft Sysinternals remote execution tool. Many antivirus products classify it as a hacking tool or a potentially unwanted application, because attackers use it to move between computers, and some quarantine it on sight.

VisualCron uses PsExec only for remote installation, with *Install VisualCron*, *Upgrade VisualCron* and *Uninstall VisualCron* in _File_ -> _Servers_ -> _Manage Servers_. PsExec is not installed as a file. It is embedded in the Client, and the Client writes "PsExec.exe" and "PsExec64.exe" to its installation folder when you use one of these commands, and leaves them there until the next one. Your antivirus may flag the files then, or during a later scan. If you use remote installation, allow these two files. If you never use remote installation, no exclusion is needed.

#### Windows Defender SmartScreen

A newly released VisualCron version has not yet built a reputation with SmartScreen, so you may see a warning on the first installation. Check that the publisher shown is "NetCart AB".

#### Installer temporary files

The setup program extracts the MSI package to "%TEMP%\VisualCron" of the Windows user who runs it. It also creates a backup folder in the form `%TEMP%\VisualCron<yyyyMMddHHmmss>`, with a copy of the Server settings files. Do not exclude the backup folder from scanning. It holds the same data as the Server settings folder, and the setup program does not delete it, so delete it yourself when you no longer need it. This is the temp folder of the user who runs the setup program, not the service's temp folder. If the installation fails partway through with no clear error, an antivirus product holding a lock on the extracted files is a reasonable first thing to check. Create an MSI log as described in [Installation troubleshooting](download-install-upgrade-uninstall#installation-troubleshooting) before you contact support.

### Notes for EDR and behavioral products

Signature scanning is usually not the difficult part. Behavioral and heuristic rules cause more trouble, because several things VisualCron does normally look like the early stages of an attack when viewed in isolation:

- A service running as Local System that starts command interpreters and script hosts
- PowerShell started by a non-interactive parent process
- Impersonation of other user accounts, which VisualCron does whenever a Task uses a Credential
- Scripted file movement across network shares
- Use of PsExec for remote installation

If your EDR product supports it, write behavioral rules for the named VisualCron executables in the installation folder, rather than a flat list of paths that drifts as you add Tasks. Do not trust the whole tree of child processes that the service starts: the service starts command interpreters, PowerShell and other programs that run whatever your Jobs contain. Ask your vendor about rules based on the signer, limited to the VisualCron installation folder.

### Symptoms that point to antivirus interference

If you are troubleshooting and are not sure whether antivirus is involved, these patterns are typical:

| Symptom | Likely cause |
|---|---|
| Logging errors, or the log database reported as corrupt | Scanner locking "VisualCron4.sdf" in the output cache folder |
| Jobs run noticeably slower than on a comparable server | Real-time scanning of output cache file churn |
| "File in use" or access denied errors in Tasks that follow a File Trigger | Scanner holding the file open as it lands in the watched folder |
| A Task type stops working after an antivirus definition update | Its helper executable was quarantined from the installation folder |
| The service fails to start after an upgrade | Installation or upgrade files quarantined |

Before assuming an exclusion is required, confirm the cause. Check the quarantine log of your antivirus product for VisualCron paths, and check the VisualCron server log in the `log` subfolder for the corresponding failure. See [Debugging and Logging](../debugging-and-logging) for how to raise the log level.

### Related pages

- [Download, Install, Upgrade, and Uninstall](download-install-upgrade-uninstall)
- [Settings - Folders](../client-user-interface/server/settings-folders)
- [Main - Settings](../client-user-interface/server/main-settings)
- [Main - User Permissions](../client-user-interface/server/main-user-permissions)
- [Assembly Resolver - Runtime Download of Components](assembly-resolver)
- [Security](../security)
- [Why Does My Firewall Warn / Why Does VisualCron Try to Access the Internet?](../faq/firewall-warn-internet-access)
