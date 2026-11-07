---
sidebar_label: 'Overview'
hide_title: 'true'
---

## Overview

Microsoft Hyper-V, formerly known as Windows Server Virtualization, is a native hypervisor; it can create virtual machines on x86-64 systems running Windows.

The Hyper-V Tasks run Hyper-V PowerShell commands, either on the VisualCron Server computer (_Local server_) or on a remote Hyper-V host (_Remote server_). They do not use a Connection.

- With _Local server_, the commands run on the VisualCron Server computer under the account that runs the VisualCron Server service. That computer needs the Hyper-V PowerShell module, and the account needs rights to manage Hyper-V
- With _Remote server_, the VisualCron Server opens a PowerShell remoting session to _Server name_ with the selected Credential, so PowerShell remoting must be turned on for the remote host. Variables are not replaced in _Server name_

For how to set up PowerShell remoting, see:

[http://www.howtogeek.com/117192/how-to-run-powershell-commands-on-remote-computers/](http://www.howtogeek.com/117192/how-to-run-powershell-commands-on-remote-computers/)

:::warning

With _Remote server_, the Task writes the Credential's user name and password as plain text into a PowerShell script that runs on the VisualCron Server computer, and it opens the session with the default PowerShell remoting settings, without HTTPS (WinRM over HTTP, port 5985 by default). Where PowerShell script block logging is turned on for the VisualCron Server computer, that script, including the password, can be written to the Windows event log. The Credential's domain is not used, so enter the user name of a domain account as `DOMAIN\user`. A password that contains `"`, `$` or a backtick can be changed by PowerShell before it is used.

:::

:::warning

The Hyper-V Tasks do not check the errors that PowerShell reports while the script runs, for example an unknown virtual machine name, or a failed remote sign-in. Such an error is not shown, and the Task reports success. Only an error that stops the script makes the Task fail. To confirm the result, check the state of the virtual machine afterward, for example with the [Check VM](check-vm) Task.

:::

### Available Hyper-V Tasks

Virtual machines:

* [List VM](list-vm)
* [Check VM](check-vm)
* [Start VM](start-vm)
* [Stop VM](stop-vm)
* [Pause VM](pause-vm)
* [Resume VM](resume-vm)
* [Suspend VM](suspend-vm)
* [Reset VM](reset-vm)

Snapshots:

* [Create Snapshot](create-snapshot)
* [Apply Snapshot](apply-snapshot)
* [Delete Snapshot](delete-snapshot)
