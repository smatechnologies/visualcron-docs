---
sidebar_label: 'Remote, Silent, and Customized Installation'
hide_title: 'true'
---

## Remote, Silent, and Customized Installation

VisualCron is installed from a Windows Installer (MSI) package. The setup program (.exe) runs this package for you, so use the setup program unless you need an unattended or scripted installation. With `msiexec` you can install without user interaction, choose the components and the installation folder, and install on another computer. This page shows the commands and what to do after a silent installation.

### Get the MSI package

To get the MSI package, complete the following steps:

1. Sign in at the [VisualCron download page](https://visualcron.com/download/), as described in [Get VisualCron](get-visualcron.md).
2. Download the custom installation package (.zip): *Customize Latest* for the latest version, or the *Custom Download Link (.zip)* of an older version.
3. Extract the .zip file to an empty folder on the computer where you install VisualCron.

   "VisualCron.msi" is in the version folder inside the extracted package.

### Before you install silently

:::warning

A silent installation with the MSI package differs from the setup program (.exe):

- The MSI package does not start the VisualCron service. Start it yourself after the installation
- The MSI package installs the VisualCron service to run as Local System
- If a different version of VisualCron is installed, `msiexec /i` stops with error 1638 and installs nothing. To upgrade, follow [Upgrade silently](#upgrade-silently)
- The MSI package checks for .NET Framework 4.8 but does not install it. Without it, a silent installation stops with exit code 1603. See [Requirements](../requirements)
- The setup program lengthens the time that Windows waits for a service to start, which takes effect after Windows restarts. The MSI package does not change it
- The new Server has the user "admin" with an empty password, as after any installation

:::

Run all commands from a Command Prompt or PowerShell window opened as administrator.

### Installation properties

| Property | Value | Default |
|---|---|---|
| `INSTALLMODE` | "1" installs the Client and the Server. "2" installs the Client only: the VisualCron service is installed, but disabled | "1" |
| `TARGETDIR` | The installation folder | "C:\Program Files (x86)\VisualCron" on 64-bit Windows, "C:\Program Files\VisualCron" on 32-bit Windows |

The VisualCron service always runs as Local System after an MSI installation. To run it under a Windows account, change the account after the installation, as described in [After a silent installation](#after-a-silent-installation).

### Install on a computer without VisualCron

To install VisualCron silently, complete the following steps:

1. Open Command Prompt as administrator.
2. Go to the version folder that contains "VisualCron.msi":

   ```cmd
   cd /d "<version folder>"
   ```

3. Run one of the following commands. `start "" /wait` makes Command Prompt wait until the installation ends.

   To install the Client and the Server:

   ```cmd
   start "" /wait msiexec /i VisualCron.msi /qn INSTALLMODE=1 /L*V "%TEMP%\VisualCron-install.log"
   ```

   To install the Client only:

   ```cmd
   start "" /wait msiexec /i VisualCron.msi /qn INSTALLMODE=2 /L*V "%TEMP%\VisualCron-install.log"
   ```

   To install in another folder:

   ```cmd
   start "" /wait msiexec /i VisualCron.msi /qn INSTALLMODE=1 TARGETDIR="<folder>" /L*V "%TEMP%\VisualCron-install.log"
   ```

4. Check the exit code:

   ```cmd
   echo %ERRORLEVEL%
   ```

   "0" means success, and "3010" means success with a restart needed. "1603" means that the installation failed, for example because .NET Framework 4.8 is missing; the log file shows why. "1638" means that a different version of VisualCron is installed. If the same version is already installed, the command changes nothing.

5. Complete the steps in [After a silent installation](#after-a-silent-installation).

### After a silent installation

After every installation or upgrade with the MSI package, on the computer itself or remotely, complete the following steps:

1. If you installed the Client and the Server, start the VisualCron service, unless it must stay stopped, for example on a passive cluster node:

   ```cmd
   net start VisualCron
   ```

2. Secure the "admin" user before you allow inbound TCP 16444 from other computers, as described in [Secure the admin user](download-install-upgrade-uninstall#secure-the-admin-user). Connect from a Client on the Server computer, or from a computer on a network that the firewall already allows.
3. Allow inbound TCP 16444 only from the computers that run a Client. The installer does not create a firewall rule; see [Firewall and network](antivirus-exclusions#firewall-and-network).
4. If the service must run under a Windows account, complete these steps:

   1. Open the VisualCron service in Windows *Services*.
   2. On the ***Log On*** tab, select *This account*, and enter the account and its password.
   3. Click *OK*.
   4. If the service should be running, restart it, or start it if it is stopped.

The "admin" user is secured, only the computers that you allowed can reach the Server, and the service runs under the account that it needs.

### Install on a remote computer

#### From the Client

The Client can install, upgrade and uninstall VisualCron on other computers in your network. It uses PsExec, which it writes to its installation folder when you use *Install VisualCron*, *Upgrade VisualCron* or *Uninstall VisualCron*. Some antivirus products flag PsExec; see [PsExec](antivirus-exclusions#psexec). Writing to the installation folder can require the Client to run as administrator.

What the Client does on the remote computer:

- *Install VisualCron* is for a computer without VisualCron. Before it installs, it runs an uninstall with the package that you select. That package cannot remove a different installed version, so on a computer with a different version, *Install VisualCron* stops with an error and installs nothing
- *Upgrade VisualCron* installs the package without uninstalling first. If a different version is installed, it stops with error 1638 and installs nothing. To move a remote computer to a different version, use the upgrade in [With PsExec](#with-psexec)
- Both install into the default installation folder, because the Client does not pass the current folder. To keep another folder, use the upgrade in [With PsExec](#with-psexec)
- The VisualCron service runs as Local System
- With *Client and Server*, the Client starts the VisualCron service. With *Client only*, VisualCron is installed, and the Client then reports an error, because the service is disabled and cannot be started
- The Client copies the package, and the 7-Zip files "7z.exe" and "7z.dll" from its installation folder, to the remote computer through the administrative share C$, and extracts the package there with them. The administrative share of the remote computer must be reachable
- The Client passes the user name and password that you enter to PsExec on the command line of the Client computer. With *Download from official web site (latest version)*, the Client also supplies them as credentials for the download of the package from www.visualcron.com. To avoid that, download the custom installation package yourself, and use *Select installation file*

To install VisualCron on a remote computer, complete the following steps:

1. Go to _File_ -> _Servers_ -> _Manage Servers_.
2. Right-click the computer:

   - To install, right-click it in *Scanning for unassigned servers*, the list of computers found on the network that have no Server connection in the Client
   - To upgrade or uninstall, right-click it in the list of Servers

3. Select *Install VisualCron*, *Upgrade VisualCron* or *Uninstall VisualCron*.

   After *Uninstall VisualCron*, the computer appears in *Scanning for unassigned servers* again, where you can install it again.

4. In the *Login* window, under *Credentials*, enter the *Username* of an administrator on the remote computer.
5. Enter the *Password*.
6. Under *Path to installer*, select *Download from official web site (latest version)* or *Select installation file*.
7. If you selected *Select installation file*, choose a custom installation package (.zip).
8. Under *Install options*, select *Client and Server* or *Client only*.
9. Click *OK*.

   The Client copies the package to the remote computer and runs the installation.

10. After *Install VisualCron* or *Upgrade VisualCron*, complete steps 2 to 4 of [After a silent installation](#after-a-silent-installation) on the remote computer.

If *Upgrade VisualCron* reports error 1638, upgrade the computer with PsExec, as described below.

#### With PsExec

To install VisualCron on a remote computer with PsExec, complete the following steps:

1. Download [PsExec](https://learn.microsoft.com/en-us/sysinternals/downloads/psexec) from Microsoft.
2. Extract it to a folder on your computer.
3. Copy "VisualCron.msi" to a folder on the remote computer, for example "C:\Temp".
4. Open Command Prompt as administrator in the PsExec folder.
5. Install VisualCron on the remote computer:

   ```cmd
   psexec \\<computer> -u <admin-user> -s msiexec /i C:\Temp\VisualCron.msi /qn INSTALLMODE=1 /L*V C:\Temp\VisualCron-install.log
   ```

   PsExec asks for the password of `<admin-user>`, and `-s` runs the installation as Local System on the remote computer.

6. Check the exit code that PsExec reports for msiexec.

   "0" or "3010" means success. For other codes, see step 4 of [Install on a computer without VisualCron](#install-on-a-computer-without-visualcron), and read "C:\Temp\VisualCron-install.log" on the remote computer.

7. Start the VisualCron service on the remote computer:

   ```cmd
   psexec \\<computer> -u <admin-user> -s net start VisualCron
   ```

8. Complete steps 2 to 4 of [After a silent installation](#after-a-silent-installation) on the remote computer.

To upgrade a remote computer with PsExec, complete the following steps:

1. Export the Server settings, as described in [Back up before you upgrade](upgrading%20versions#back-up-before-you-upgrade).
2. Copy the new "VisualCron.msi" and the script "upgrade-visualcron.ps1" from [Upgrade silently](#upgrade-silently) to "C:\Temp" on the remote computer.
3. Run the script on the remote computer:

   ```cmd
   psexec \\<computer> -u <admin-user> -s powershell -NoProfile -ExecutionPolicy RemoteSigned -File C:\Temp\upgrade-visualcron.ps1
   ```

   To leave the service stopped, for example on a passive cluster node, add `-NoStart` at the end:

   ```cmd
   psexec \\<computer> -u <admin-user> -s powershell -NoProfile -ExecutionPolicy RemoteSigned -File C:\Temp\upgrade-visualcron.ps1 -NoStart
   ```

   The script keeps the current installation folder and the Client or Client and Server choice. It starts the service only if the service ran as Local System and you did not add `-NoStart`. Its log is "C:\Temp\VisualCron-upgrade.log". PsExec reports the exit code of the script; for the codes, see step 7 of [Upgrade silently](#upgrade-silently).

4. If you added `-NoStart` on a cluster node, set the startup type of the VisualCron service back to the value the cluster needs.
5. If the service ran under a Windows account, complete step 4 of [After a silent installation](#after-a-silent-installation) on the remote computer.

:::note

PsExec also accepts the password with `-p`, but the password is then visible on the command line. Leave out `-p` to be asked for it.

:::

### Uninstall silently

To uninstall VisualCron from a script, uninstall it by its product code, which Windows records when VisualCron is installed. The settings are kept, as described in [Uninstall VisualCron](download-install-upgrade-uninstall#uninstall-visualcron).

To uninstall VisualCron silently, complete the following steps:

1. Open PowerShell as administrator.
2. Run the following commands:

   ```powershell
   $keys = @(
     'HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*',
     'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*'
   )
   $products = @(Get-ItemProperty -Path $keys -ErrorAction SilentlyContinue |
     Where-Object { $_.DisplayName -like 'VisualCron*' })
   if ($products.Count -eq 0) {
     Write-Output 'No VisualCron installation was found. Nothing was changed.'
   } elseif ($products.Count -gt 1) {
     Write-Output "Found $($products.Count) VisualCron entries. Nothing was changed."
   } else {
     $code = $products[0].PSChildName
     $p = Start-Process -FilePath msiexec.exe -ArgumentList "/x $code /qn" -Wait -PassThru
     Write-Output "Uninstall exit code: $($p.ExitCode)"
   }
   ```

3. Check the output.

   "Uninstall exit code: 0" means success, and "3010" means success with a restart needed. "No VisualCron installation was found" means that VisualCron is not installed for all users of the computer. An installation made with *Just me* may not be found: uninstall it from the list of installed apps, signed in as the user who installed it. If the output reports more than one entry, uninstall VisualCron from the list of installed apps.

### Upgrade silently

The MSI package cannot install over a different installed version, so a silent upgrade uninstalls the installed version first. The settings are kept. The sample script below first checks that "VisualCron.msi" is in its folder and that the program file of the VisualCron service exists. It then reads the current installation folder and the Client or Client and Server choice from the service, uninstalls by product code, checks the result, and installs the new version into the same folder. It starts the service only if the service ran as Local System, because the MSI package installs the service to run as Local System, and another account must be set again first.

:::warning

Use the current installation folder as `TARGETDIR`. Otherwise the new program files go to the default folder, while the Server keeps its settings, logs and backups in the old folder. The sample script does this for you.

:::

To upgrade VisualCron silently, complete the following steps:

1. Export the Server settings, as described in [Back up before you upgrade](upgrading%20versions#back-up-before-you-upgrade).
2. In Windows *Services*, open the VisualCron service.
3. On the ***Log On*** tab, note the account if it is not Local System.
4. Copy the new "VisualCron.msi", from the version folder of the extracted package, and the sample script below to one folder on the computer.
5. Open PowerShell as administrator in that folder.
6. Run the script:

   ```powershell
   powershell -NoProfile -ExecutionPolicy RemoteSigned -File .\upgrade-visualcron.ps1
   ```

   To leave the service stopped, for example on a passive cluster node, add `-NoStart`:

   ```powershell
   powershell -NoProfile -ExecutionPolicy RemoteSigned -File .\upgrade-visualcron.ps1 -NoStart
   ```

   With `-NoStart` on a cluster node, set the startup type of the VisualCron service back to the value the cluster needs.

   If the service ran under a Windows account, the script does not start the service, because the account must be set again first.

7. Check the exit code:

   ```powershell
   $LASTEXITCODE
   ```

   In Command Prompt, use:

   ```cmd
   echo %ERRORLEVEL%
   ```

   - "0": the upgrade finished
   - "3010": the upgrade finished, and Windows must be restarted to complete it
   - "1": the script stopped before it changed anything, for example because "VisualCron.msi" is not in the folder. The script output says why
   - "2": VisualCron was upgraded, but the service did not start. Start it in Windows *Services*, and check the Windows event log
   - Any other code is the exit code of msiexec. The script output says whether the uninstall or the installation failed

8. If the service ran under a Windows account, complete step 4 of [After a silent installation](#after-a-silent-installation).

:::warning

If the script reports that the installation failed, the previous version was already uninstalled, so VisualCron is no longer installed and Jobs do not run. The settings are kept. To recover, install the previous version from its package, or fix the cause shown in the log file and install the new version again. Use the command in [Install on a computer without VisualCron](#install-on-a-computer-without-visualcron) with the `INSTALLMODE` and `TARGETDIR` values that the script reported, and then complete [After a silent installation](#after-a-silent-installation).

:::

Sample script, saved as "upgrade-visualcron.ps1":

```powershell
# Upgrade VisualCron silently. Run as administrator, in the folder that
# contains the new VisualCron.msi. Add -NoStart to leave the service stopped.
param([switch]$NoStart)

$msi = Join-Path $PSScriptRoot 'VisualCron.msi'
$log = Join-Path $PSScriptRoot 'VisualCron-upgrade.log'
$restart = $false

# Check everything before anything is changed
if (-not (Test-Path -LiteralPath $msi)) {
  Write-Output "VisualCron.msi was not found in $PSScriptRoot. Nothing was changed."
  exit 1
}
$svc = Get-CimInstance -ClassName Win32_Service -Filter "Name='VisualCron'"
if (-not $svc) { Write-Output 'The VisualCron service was not found. Nothing was changed.'; exit 1 }
$exe = $null
if ($svc.PathName -match '^"?(.+?\.exe)') { $exe = $Matches[1] }
if (-not $exe -or -not (Test-Path -LiteralPath $exe)) {
  Write-Output "The program file of the VisualCron service was not found: $($svc.PathName). Nothing was changed."
  exit 1
}
$targetDir = Split-Path -Path $exe -Parent
if ($svc.StartMode -eq 'Disabled') { $installMode = 2 } else { $installMode = 1 }
$account = $svc.StartName
Write-Output "Folder: $targetDir  INSTALLMODE: $installMode  Account: $account"

$keys = @(
  'HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*',
  'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*'
)
$products = @(Get-ItemProperty -Path $keys -ErrorAction SilentlyContinue |
  Where-Object { $_.DisplayName -like 'VisualCron*' })
if ($products.Count -ne 1) { Write-Output "Expected one installed VisualCron, found $($products.Count). Nothing was changed."; exit 1 }
$code = $products[0].PSChildName

# Close the Tray Client and the Client
Stop-Process -Name VCTray, VisualCronClient -Force -ErrorAction SilentlyContinue

# Uninstall the installed version by its product code. Settings are kept.
$p = Start-Process -FilePath msiexec.exe -ArgumentList "/x $code /qn" -Wait -PassThru
if ($p.ExitCode -ne 0 -and $p.ExitCode -ne 3010) {
  Write-Output "Uninstall failed with exit code $($p.ExitCode). Nothing was installed."
  exit $p.ExitCode
}
if ($p.ExitCode -eq 3010) { $restart = $true }

# Install the new version into the same folder
$installArgs = "/i `"$msi`" /qn INSTALLMODE=$installMode TARGETDIR=`"$targetDir`" /L*V `"$log`""
$p = Start-Process -FilePath msiexec.exe -ArgumentList $installArgs -Wait -PassThru
if ($p.ExitCode -ne 0 -and $p.ExitCode -ne 3010) {
  Write-Output "Installation failed with exit code $($p.ExitCode). See $log."
  Write-Output 'The previous version was uninstalled, so VisualCron is no longer installed. The settings are kept.'
  Write-Output "To recover, install the previous version from its package, or fix the cause and install this version again, with INSTALLMODE=$installMode TARGETDIR=`"$targetDir`"."
  exit $p.ExitCode
}
if ($p.ExitCode -eq 3010) { $restart = $true }

# The MSI package does not start the service, and installs it to run as Local System
if ($installMode -eq 2) {
  Write-Output 'Client only: the VisualCron service stays disabled.'
} elseif ($NoStart) {
  Write-Output 'The service was not started (-NoStart). On a cluster node, set its startup type back to the value the cluster needs.'
} elseif ($account -ne 'LocalSystem') {
  Write-Output "The service ran as $account and now runs as Local System, so it was not started. Set the account again, and then start the service."
} else {
  try {
    Start-Service -Name VisualCron -ErrorAction Stop
  } catch {
    Write-Output "VisualCron was upgraded, but the service did not start: $($_.Exception.Message)"
    exit 2
  }
}

if ($restart) {
  Write-Output 'Upgrade finished. Restart Windows to complete it.'
  exit 3010
}
Write-Output 'Upgrade finished.'
exit 0
```