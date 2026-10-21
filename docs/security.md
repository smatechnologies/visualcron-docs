---
sidebar_label: 'Security'
hide_title: 'true'
---

## Security

Many actions have been taken to ensure security. Look at the following chapters to learn more.

### Task Manager Permissions for the Viewers Group (13.2.1)

As of VisualCron 13.2.1, the default Viewers group does not include **Task Manager → Delete**. The Viewers role is intended for read-oriented monitoring access.

Administrators who need to grant delete permissions to a non-administrator role can do so by explicitly adding Task Manager → Delete to a custom group. Existing customized groups are not affected by this default.

### Remote File Explorer — Permissions in Remote Connections (13.2.1)

As of VisualCron 13.2.1, when **Remote File Explorer → Read** is enabled for a remote (non-local) connection, the interface displays the full set of effective permissions for that context. This ensures administrators have a clear view of what access is being granted before saving the configuration.

For least-privilege setups, it is encouraged to review Remote File Explorer permission assignments for any group that is not intended to have write access to the server file system.

### Security Upgrade Note

Please be aware that when upgrading to v12+, the client and server version must match. This version is not backwards compatible with any pre v12 versions. 

![](../static/img/Get%20VisualCron/Download%20Install%20Upgrade%20and%20Uninstall/12.0.0%20Reminder.png)

### TLS Communication Between Client and Server

We are using the [NetTcpBinding](https://learn.microsoft.com/en-us/dotnet/api/system.servicemodel.nettcpbinding?view=dotnet-plat-ext-8.0) class uses TCP for message transport. Security for the transport mode is provided by implementing Transport Layer Security (TLS) over TCP. The TLS implementation is provided by the operating system.

### Import Values are Stored Encrpyted

Important values like Username, Password etc. are encrypted by VisualCron with AES-256 encryption ensuring that no one who gets the hands of the files can read and interpret that information.
