---
sidebar_label: 'Task IIS - Add Website'
hide_title: 'true'
---

## Task IIS - Add Website

The IIS - Add Website Task creates a website in the IIS of the VisualCron Server computer, using an IIS Connection, with its binding, limits, logging, root folder and failed request tracing settings.

![IIS - Add a new web site Task settings, with the Connection, Web site parameters, Binding parameters, Log file parameters, Limits, Virtual directory parameters and Trace failed requests logging parameters groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Add%20a%20new%20web%20site.png)

:::warning

This Task uses an IIS Connection; see [Connection - IIS](../../connection-iis). The Task always works on the IIS of the VisualCron Server computer: the Connection's _Address_ is not used, and the changes are made as the account of the VisualCron Server service, which must be allowed to change IIS. The Connection's _Username_ and _Password_ are used only for network access.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

For every setting below that is left empty, or that is a check box in its third state (neither selected nor cleared), the IIS default for new websites is used. A number field that does not hold a whole number also gets the IIS default.

### IIS - Add a new web site tab

- _Connection_: the IIS Connection. Required. Click the _Settings_ icon to open _Manage Connections_

#### Web site parameters

- _Name_: the name of the new website. Required
- _App pool name_: the application pool of the website and its applications. Click the _Refresh_ icon to list the application pools of the VisualCron Server computer

#### Binding parameters

The Task builds the binding as `IP address:port:host name`.

- _Binding protocol_: the protocol of the binding, for example "http" or "https"
- _Binding IP address_: the IP address the website listens on, or "*" for all unassigned addresses. Fill in this field: when it is empty, the binding is not built correctly and _Binding port_ is not used
- _Binding host name_: the host name of the binding, to host several websites on the same IP address and port
- _Binding port_: the port the website listens on, for example "80" for HTTP or "443" for HTTPS. Required
- _Certificate_: available only when _Binding protocol_ is "https"

:::warning

The Task does not assign the selected _Certificate_ to the binding, so an "https" website created by this Task has no certificate. Assign the certificate to the binding in IIS Manager after the Task runs.

:::

#### Log file parameters

- _Log file enabled_: when selected, request logging is turned on for the website
- _Log path_: the folder for the log files. Click the _Browse_ icon to select a folder
- _Log file format_: "Iis", "Ncsa", "W3c" or "Custom"
- _Ext file flags_: the fields in W3C log entries. Select any of "Date", "Time", "Client IP", "User name", "Site name", "Computer name", "Server IP", "Method", "Uri Stem", "Uri Query", "Http Status", "Win32 Status", "Bytes Sent", "Bytes Recv", "Time Taken", "Server Port", "User Agent", "Cookie", "Referer", "Protocol Version", "Host" and "Http SubStatus"
- _Target W3C_: where W3C log entries go: "File", "ETW" (Event Tracing for Windows), or both
- _Log File Local Time Rollover_: when selected, a new log file is started based on the local time of the computer instead of UTC
- _RolloverPeriod_: when a new log file is started: "Max Size", "Daily", "Weekly", "Monthly" or "Hourly"
- _LogFileTruncateSize_: the log file size in bytes at which a new file is started, with "Max Size"

#### Limits

- _Connection timeout_: the number of seconds before IIS closes an inactive connection
- _Max connections_: the maximum number of simultaneous connections to the website
- _Max bandwidth_: the maximum network bandwidth of the website, in bytes per second
- _Max url segments_: the maximum number of path segments in a request URL

#### Virtual directory parameters

- _Path_: the physical folder of the website root. Required. Click the _Browse_ icon to select a folder
- _Logon method_: how IIS logs on with the user in _Credential_ to reach the folder: "Interactive", "Batch", "Network" or "Clear text"
- _Credential_: the user that IIS uses to reach the folder. The Task writes the Credential's user name and password into the IIS configuration of the website. Click the _Settings_ icon to open _Manage credentials_; see [Global - Credentials](../../global-credentials)

:::warning

The Task copies the user name and password of the selected _Credential_ into the IIS configuration of the website. IIS keeps its own copy: changing or deleting the Credential in VisualCron later does not change IIS.

:::

#### Trace failed requests logging parameters

- _Trace log file enabled_: when selected, failed request tracing is turned on for the website
- _Trace log path_: the folder for the trace log files. Click the _Browse_ icon to select a folder. Variables are not resolved in this field
- _Max log files_: the maximum number of trace log files kept for the website

### Output and errors

On success, the output is `Site index=` followed by the ID of the new website. When a website with that name already exists, the Task does not change it and writes no output, and the Task reports success. When a step fails, the Task fails; the error names the last step reached.

The ***TimeOut*** tab does not stop this Task.
