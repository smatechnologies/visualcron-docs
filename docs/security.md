---
sidebar_label: 'Security'
hide_title: 'true'
---

## Security

Many actions have been taken to ensure security. Look at the following chapters to learn more.

### Task Manager — Delete Removed from Viewers Default (13.2.1)

Prior to VisualCron 13.2.1, the default Viewers group included **Task Manager → Delete**, which allowed Viewer-role users to terminate system processes on the connected server. This permission has been removed from the Viewers group default in 13.2.1.

Existing customized groups that explicitly granted Task Manager → Delete are not automatically changed. Only installations that have not modified the Viewers group baseline are affected. Administrators who require process termination for a non-administrator role must grant Task Manager → Delete explicitly.

### Remote File Explorer — Effective Permissions in Remote Connections (13.2.1)

When **Remote File Explorer → Read** is enabled for a user connecting remotely (non-local connection), the effective capability includes file upload, modification, and execution running as NT AUTHORITY\SYSTEM on the server host — broader than the "Read" label implies.

As of VisualCron 13.2.1, when Read is enabled on a remote connection the interface surfaces the full set of effective permissions so administrators are not misled by the read-only label.

Administrators should audit any existing group configurations that include Remote File Explorer → Read for remote users. If read-only monitoring is the intended use case, granting this permission to non-administrator groups on remote connections is not recommended.

### TLS Communication Between Client and Server

We are using the [NetTcpBinding](https://learn.microsoft.com/en-us/dotnet/api/system.servicemodel.nettcpbinding?view=dotnet-plat-ext-8.0) class uses TCP for message transport. Security for the transport mode is provided by implementing Transport Layer Security (TLS) over TCP. The TLS implementation is provided by the operating system.

### Import Values are Stored Encrpyted

Important values like Username, Password etc. are encrypted by VisualCron with AES-256 encryption ensuring that no one who gets the hands of the files can read and interpret that information.

### Interactive Logon

Windows 2008 and later security settings for Credential Provider
 
Two security settings are required for "Foreground execution":
 
1. Do not require CTRL+ALT+DEL
To make interactive logon work in Windows 2008 you must disable SAS (Secure Attention Sequence). You do this by opening Administrative tools->Local Security Policy.
 
In the Local policies you need to enable "Interactive logon: Do not require CTRL+ALT+DEL" as in the image below:

![](../static/img/embim4.png)

![](../static/img/ctrlaltdel.png)

This security setting determines whether pressing CTRL+ALT+DEL is required before a user can log on.
 
If this policy is enabled on a computer, a user is not required to press CTRL+ALT+DEL to log on. Not having to press CTRL+ALT+DEL leaves users susceptible to attacks that attempt to intercept the users' passwords. Requiring CTRL+ALT+DEL before users log on ensures that users are communicating by means of a trusted path when entering their passwords.
 
If this policy is disabled, any user is required to press CTRL+ALT+DEL before logging on to Windows.
 
Default on domain-computers: Enabled: At least Windows  8/Disabled: Windows 7 or earlier.
Default on stand-alone computers: Enabled.
 
 
2. User Account Control: Admin Approval Mode for the Built-in Administrator account
To be able to communicate with the Credential Provider you need to disable this setting found in Administrative tools->Local Security Policy->User Account Control: Use Admin Approval Mode for the built-in Administrator account. After applying this setting a reboot of the computer is required.
 
This policy setting controls the behavior of Admin Approval Mode for the built-in Administrator account.
 
The options are:
 
• Enabled: The built-in Administrator account uses Admin Approval Mode. By default, any operation that requires elevation of privilege will prompt the user to approve the operation.
 
• Disabled: (Default) The built-in Administrator account runs all applications with full administrative privilege.

![](../static/img/uacadminapprovalmode.png)