---
sidebar_label: 'Installation'
sidebar_position: 1
description: How to download, install, upgrade, and uninstall VisualCron on Windows.
---

# Installation

VisualCron runs on Windows and requires .NET Framework 4.8. The installer handles both the Server (Windows service) and the Client (GUI application).

## Prerequisites

- Windows Server 2012 R2 or later (or Windows 10/11)
- [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48)
- Administrator rights on the target machine

## Download

Download the latest version from [visualcron.com/download.aspx](https://www.visualcron.com/download.aspx).

Older versions are available at [visualcron.com/download-latest.aspx](https://www.visualcron.com/download-latest.aspx).

:::tip Backup before upgrading

Before any upgrade, export your existing settings: **File > Import/Export > Export settings**. This lets you roll back to a previous version if needed.

:::

## Install / Upgrade

The installer automatically uninstalls any previous version — no manual removal needed first.

1. Double-click `VisualCron.exe`. The pre-installer prepares the MSI package and stops any running VisualCron processes.

   ![Pre-installer](../../static/img/Get%20VisualCron/Download%20Install%20Upgrade%20and%20Uninstall/1.png)

   *Fig. 1 — The pre-installer preparing the MSI package and stopping any running VisualCron processes.*

2. The MSI installer launches.

   ![MSI installer](../../static/img/Get%20VisualCron/Download%20Install%20Upgrade%20and%20Uninstall/2.png)

   *Fig. 2 — The VisualCron MSI installer welcome screen.*

3. Accept the License Agreement and click **Next**.

   ![License Agreement](../../static/img/Get%20VisualCron/Download%20Install%20Upgrade%20and%20Uninstall/3.png)

   *Fig. 3 — Accept the License Agreement to proceed.*

4. Choose whether to install both the **Server and Client**, or the **Client only**. If you install Client only, the service is installed but set to Disabled — you can enable it later in Services if needed.

   ![Component selection](../../static/img/Get%20VisualCron/Download%20Install%20Upgrade%20and%20Uninstall/4.png)

   *Fig. 4 — Select which components to install: Server + Client, or Client only.*

5. Choose an installation folder and click **Next**.

   ![Installation folder](../../static/img/Get%20VisualCron/Download%20Install%20Upgrade%20and%20Uninstall/5.png)

   *Fig. 5 — Choose the installation directory (the default is recommended).*

6. Click **Next** to begin copying files.

   ![Ready to install](../../static/img/Get%20VisualCron/Download%20Install%20Upgrade%20and%20Uninstall/6.png)

   *Fig. 6 — Ready to install. Click Next to start copying files.*

7. Wait for the progress bar to complete.

   ![Installing](../../static/img/Get%20VisualCron/Download%20Install%20Upgrade%20and%20Uninstall/7.png)

   *Fig. 7 — Installation in progress.*

8. Click **Close** when finished, then choose to start the VisualCron Client.

   ![Complete](../../static/img/Get%20VisualCron/Download%20Install%20Upgrade%20and%20Uninstall/8.png)

   *Fig. 8 — Installation complete. Click Close and launch the Client.*

9. If you see a connection error on first startup, wait 60 seconds and click **Yes** to reconnect. The Server needs time to initialize.

   ![Client startup](../../static/img/Get%20VisualCron/Download%20Install%20Upgrade%20and%20Uninstall/9.png)

   *Fig. 9 — The Client connecting to the Server on first launch. A short wait may be needed.*

## Firewall

Allow VisualCron through your firewall on all ports it uses (default: 16444). During installation, your firewall may prompt for permission — allow all connections for VisualCron.

## Uninstall

Go to **Control Panel > Add/Remove Programs**, find **VisualCron x.x.x**, and click **Remove**. If it does not appear, re-run the installer which will offer a removal option.

## Troubleshooting

**MSI errors** — Run the installer from the command line to generate a log file:

```
msiexec /i "VisualCron.msi" /L*V "C:\install.log"
```

Send `install.log` to support@visualcron.com.

**Antivirus blocking psexec.exe** — VisualCron bundles `psexec.exe` (Microsoft Sysinternals) for optional remote installation. Allow this file — it is safe when the publisher shows **NetCart AB**.

**Windows Defender SmartScreen** — New releases may trigger SmartScreen until they gain reputation. Click **More info > Run anyway** if the publisher shows **NetCart AB**.
