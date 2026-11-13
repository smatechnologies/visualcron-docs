---
sidebar_label: 'Task Messaging - SysLog'
hide_title: 'true'
---

## Task Messaging - SysLog

The SysLog Task sends a message to a SysLog server over UDP or TCP. SysLog is a standard way to collect log messages from many kinds of systems and devices, such as printers, routers and firewalls, in one central place.

![SysLog tab with the Connection, Message properties and Message groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Syslog.png)

:::warning

The Task sends the message in RFC 3164 format over plain UDP or TCP, without encryption, so anyone who can see the network traffic can read it.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### SysLog tab

#### Connection

- _Host_: the host name or IP address of the SysLog server

  The Task window does not require a value.

- _UDP_: sends the message over UDP to the _Port_ next to it, "514" by default; selected on a new Task
- _TCP_: sends the message over TCP to the _Port_ next to it, "1468" by default

Variables are resolved in _Host_ and in both _Port_ fields.

#### Message properties

- _Facility_: the SysLog facility of the message: "Kernel", "User", "Mail", "Daemon", "Auth", "Syslog", "Lpr", "News", "UUCP", "ClockDaemon", "SecurityAuthorization", "FTP", "NTP", "LogAudit", "LogAlert", "Cron", or "Local0" to "Local7"
- _Level_: the severity of the message: "Emergency", "Alert", "Critical", "Error", "Warning", "Notice", "Information" or "Debug"
- _Application_: the application name sent with the message, "VisualCron" by default; Variables are resolved

A new Task has _Facility_ "Auth" and _Level_ "Alert".

#### Message

The text of the message. Variables are resolved.

### Output and errors

The Task writes no output. When the message is sent, the Task reports success.

:::warning

Over UDP, the Task gets no confirmation that the message arrived. If the message cannot be sent, for example because the host is unknown, a _Port_ is not a number, or the server refuses the TCP connection, the error is written to the Server log, and the Task reports success.

:::
