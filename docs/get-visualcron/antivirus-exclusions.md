---
sidebar_label: 'Antivirus and Endpoint Protection Exclusions'
hide_title: 'true'
---

## Antivirus and Endpoint Protection Exclusions

VisualCron is a scheduling and automation product. By design it writes to disk continuously, keeps a database file open for the lifetime of the service, watches folders for changes, and launches child processes to run Tasks. Those are all behaviors that real-time antivirus scanners and endpoint detection and response (EDR) products are built to inspect.

VisualCron runs correctly with antivirus software active, and there is no requirement to disable protection. However, without exclusions you may see file locking, slow Job execution, missed File Triggers, or quarantined VisualCron components.

This page lists what VisualCron uses so your security team can decide which exclusions to apply. Treat it as a reference for building a policy, not as a mandate. Every exclusion reduces coverage, so apply the narrowest set that resolves the behavior you are seeing, and review it with whoever owns endpoint security in your organization.

### Quick version

If you want the shortest path to a stable server:

1. Exclude the VisualCron installation folder, for example `C:\Program Files\VisualCron`.
2. Exclude the output cache folder, by default `C:\ProgramData\VisualCron\output`.
3. Exclude the temp folder, by default `%TEMP%\VisualCron`.
4. Exclude any folders your own Jobs read from or write to, especially folders watched by a File Trigger.
5. Allow processes to launch from the VisualCron installation folder.
6. Allow inbound TCP 16444 to the server.

The rest of this page explains each item so you can be more selective if you prefer.

### Confirm your actual paths first

Several of the folders below are configurable and may have been changed on your server. Before applying exclusions, read the current values from the Client in **Server > Main settings > Settings > Folders**. See [Settings - Folders](../client-user-interface/server/settings-folders) for a description of each one.

The paths in this page are the defaults for a standard installation.

### Folder exclusions

**Installation folder**

Default: `C:\Program Files\VisualCron`

This folder holds the server, the client, and every helper executable VisualCron launches to run Tasks. Excluding the folder as a whole is the simplest option and covers all of the subfolders below.

If you need to be more targeted, these are the subfolders that see the most activity:

| Subfolder | Contents | Why it matters |
|---|---|---|
| `log` | Server log files, for example `log_serverDATE.txt` | Written to continuously while the service runs |
| `settings` | `settings_server.xml`, Job and Task definitions, per Task state files | Written on every settings change |
| `data` | Runtime data, including `data\triggers\mail` for Mail Trigger state | Written by Triggers |
| `backup` | `VC-Settings.zip` produced by the built in "Backup settings" Job | Written on schedule |
| `cert` | Certificates used for client and server communication | Read at service startup |
| `x64\sqlce` | Native SQL Server Compact components | Loaded into the service process |
| `PowerShell`, `MSSQL2005` through `MSSQL2025` | Helper executables for PowerShell and SSIS Tasks | Launched as child processes |

**Output cache folder**

Default: `C:\ProgramData\VisualCron\output`

This is the single most important exclusion. VisualCron writes one XML file per Task output, Job result, and Task result, then deletes it again when the output is no longer needed. On a busy server this produces a high rate of file create and delete operations, and a real-time scanner inspecting each one adds measurable latency to every Task.

The internal log database also lives here, in the `log` subfolder, as `VisualCron4.sdf`. The service holds this SQL Server Compact file open for as long as it is running. A scanner that locks it, even briefly, can cause logging errors, slowdowns, or database corruption. If you exclude only one path, make it this one.

**Temp folder**

Default: `%TEMP%\VisualCron`

Because the VisualCron service normally runs as LOCAL SYSTEM, this resolves to a path under `C:\Windows\Temp` rather than a user profile. VisualCron uses it for working files during Task execution and cleans it up periodically.

**Client folders**

On machines where the VisualCron Client is installed:

| Path | Contents |
|---|---|
| `%LOCALAPPDATA%\VisualCron\settings` | Client settings, server list, tray client settings |
| `%LOCALAPPDATA%\VisualCron\log` | Client log files |

These are far less write-intensive than the server folders and are usually only worth excluding if you see the Client itself being blocked.

**Your own Job folders**

VisualCron has no way to know these in advance. Any folder your Jobs read from, write to, or move files through should be considered.

Folders watched by a File Trigger deserve particular attention. VisualCron uses the Windows file system watcher to detect changes, and an antivirus product scanning a file at the moment it lands in a watched folder can hold a lock on it. The usual symptoms are "file in use" or access denied errors in the Task that follows the Trigger, Triggers that fire against a file that cannot yet be opened, or Triggers that appear to fire twice.

### Process exclusions

VisualCron runs as a Windows service named **VisualCron**, with the display name **VisualCron** and a dependency on the Windows Management Instrumentation service (`winmgmt`). The service executable is `VisualCronService.exe`.

To run a Task, the service frequently launches a separate helper executable rather than doing the work in process. A long-running service spawning short-lived child processes is a pattern that behavioral detection engines flag, so this is worth allowing explicitly.

All of these executables live inside the VisualCron installation folder and are digitally signed by **NetCart AB**. Allowing execution from the installation folder, or trusting the NetCart AB signing certificate, covers all of them and is easier to maintain than an executable-by-executable list.

If your security product requires named processes, the main ones are:

| Executable | Role |
|---|---|
| `VisualCronService.exe` | The VisualCron Server service |
| `VisualCronClient.exe` | The VisualCron Client |
| `VCTray.exe` | Tray application |
| `ServerLauncher.exe` | Launches and monitors server instances |
| `Restarter.exe` | Restarts the service |
| `InstallController.exe` | Installation and upgrade control |
| `vcu.exe` | Uninstaller |
| `VCCommand.exe` | Command line interface |
| `PowerShell\TaskPowerShell.exe`, `PowerShell\TaskPowerShellx86.exe` | PowerShell Task |
| `TaskNETCode.exe` | .NET Code Task |
| `NETExecute40.exe`, `NETExecute40x86.exe` | Assembly Execute Task |
| `TaskUnmanagedExecute.exe`, `TaskUnmanagedExecutex86.exe` | Unmanaged DLL Execute Task |
| `TaskOfficeMacro.exe`, `TaskOfficeMacrox86.exe` | Office Macro Task |
| `MSSQL*\SSISExecute*.exe`, `SSISDBExecute.exe` | SSIS Tasks, one per SQL Server version |
| `AS400Execute.exe` | AS/400 Task |
| `VisualCron.WebBrowser.exe`, `VisualCronWebMacro.exe` | Web browser automation |
| `LockWorkStationNet.exe` | Lock Workstation Task |
| `VirtualServerTasks.Core.Launcher.exe` | Virtual server Tasks |

VisualCron also ships or uses a small number of third party tools that antivirus products flag more often than the VisualCron binaries themselves:

- `7z.exe`, in the installation folder, used for compression Tasks and for packaging during remote install.
- `jq-win32.exe` and `jq-win64.exe`, in the installation folder, used for JSON processing.
- `makecert.exe`, in the `cert` subfolder, used for certificate generation.
- `installutil.exe` and `msicuu2.exe`, in the `install` subfolder, used during installation and upgrade.
- `PsExec.exe` and `PsExec64.exe`. These are not installed as files. They are embedded in the Client and written to the Client installation folder only when you use the remote install feature in Server Manager. See the note under [Installation time detections](#installation-time-detections) below.

### Firewall and network

**Inbound**

| Port | Protocol | Purpose | Default |
|---|---|---|---|
| 16444 | TCP | Client and API connections to the VisualCron Server | Enabled |
| 8001 | TCP | Web API over HTTP | Disabled |
| 8002 | TCP | Web API over HTTPS | Disabled |

Port 16444 is the one that matters for a normal installation. It is configurable in the server settings, so confirm the value on your server before writing a firewall rule. The Web API ports are only relevant if you have explicitly enabled the Web API.

**Outbound**

VisualCron contacts `https://www.visualcron.com` on TCP 443 for license activation, deactivation and validation, trial registration, version checks, translation files, error reports, and reporting.

The Assembly Resolver also downloads optional components on demand from `https://www.visualcron.com/files/dl/`. These are components left out of the installer to keep its size down, such as language files for the Scan Document Task. See [Assembly Resolver](assembly-resolver) for detail.

If you use the VisualCron mobile app, the server also contacts `cloud.visualcron.com`.

If your environment uses an intercepting web proxy or TLS inspection, allowlist `www.visualcron.com` and `cloud.visualcron.com`. Beyond those, VisualCron only makes the outbound connections your own Jobs ask it to make, for example to an SFTP server or a mail server.

### Installation time detections

Two detections during installation are expected and documented on the [Download, Install, Upgrade and Uninstall](download-install-upgrade-uninstall) page:

**PsExec**

PsExec is a genuine Microsoft Sysinternals remote execution tool. Many antivirus products classify it as a hacking tool or a potentially unwanted application because attackers use it for lateral movement, and some will quarantine it on sight.

VisualCron uses it only for the optional remote install feature, where you push an installation to another machine from the Client's Server Manager. Current versions do not install it as a file. It is embedded in the Client and extracted to the Client installation folder at the moment you use that feature. Your antivirus may still flag it during installation or the first time the feature is used. It is safe to allow. If you never use remote install, you do not need an exclusion for it.

**Windows Defender SmartScreen**

A newly released VisualCron version has not yet built reputation with SmartScreen, so you may see a warning on first install. As long as the publisher shown is **NetCart AB**, the file is ours and is correctly signed.

**Installer temporary files**

The pre-installer extracts the MSI package and supporting files to the Windows temp folder, and creates a timestamped backup folder there in the form `%TEMP%\VisualCronYYYYMMDDHHMMSS`. If installation fails partway through with no clear error, an antivirus product holding a lock on the extracted files is a reasonable first thing to check. Retrieve an MSI log as described in the installation troubleshooting section of the install page before contacting support.

### Notes for EDR and behavioral products

Signature scanning is usually not the difficult part. Behavioral and heuristic rules cause more trouble, because several things VisualCron does normally look like the early stages of an attack when viewed in isolation:

- A service running as LOCAL SYSTEM spawning command interpreters and script hosts.
- PowerShell invoked by a non-interactive parent process.
- Impersonation of other user accounts, which VisualCron does whenever a Task uses a Credential.
- Scripted file movement across network shares.
- Use of PsExec for remote installation.

If your EDR product supports it, the most durable approach is a policy scoped to the VisualCron service and its child process tree, rather than a flat list of paths that will drift as you add Tasks. Ask your vendor about parent process or signer based rules, using the NetCart AB code signing certificate as the anchor.

### Symptoms that point to antivirus interference

If you are troubleshooting and are not sure whether antivirus is involved, these patterns are typical:

| Symptom | Likely cause |
|---|---|
| Logging errors, or the log database reported as corrupt | Scanner locking `VisualCron4.sdf` in the output cache folder |
| Jobs run noticeably slower than on a comparable server | Real-time scanning of output cache file churn |
| "File in use" or access denied errors in Tasks that follow a File Trigger | Scanner holding the file open as it lands in the watched folder |
| A Task type stops working after an antivirus definition update | Its helper executable was quarantined from the installation folder |
| The service fails to start after an upgrade | Installation or upgrade files quarantined |

Before assuming an exclusion is required, confirm the cause. Check the quarantine log of your antivirus product for VisualCron paths, and check the VisualCron server log in the `log` subfolder for the corresponding failure. See [Debugging and Logging](../debugging-and-logging) for how to raise the log level.

### Related pages

- [Download, Install, Upgrade and Uninstall](download-install-upgrade-uninstall)
- [Settings - Folders](../client-user-interface/server/settings-folders)
- [Assembly Resolver - Runtime Download of Components](assembly-resolver)
- [Security](../security)
- [Why Does My Firewall Warn / Why Does VisualCron Try to Access the Internet?](../faq/firewall-warn-internet-access)
