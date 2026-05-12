---
sidebar_label: 'Task Messaging - SysLog'
hide_title: 'true'
---

## Task Messaging - SysLog

The SysLog Task sends a message to a remote SysLog server. SysLog is widely used for computer system management, security auditing and general informational, analysis and debugging messages, and is supported by a wide range of devices (printers, routers, firewalls, etc.) and receivers across multiple platforms — making it a common way to integrate log data from different systems into a central repository.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Syslog.png)

### Connection

**Host**

The host name or IP address of the SysLog server to send the message to.

**Protocol**

Select the transport protocol to use. Available options:

* _UDP_ - send the message over UDP using the *UDP port*
* _TCP_ - send the message over TCP using the *TCP port*

**UDP port**

The UDP port the SysLog server is listening on. Used when *Protocol* is set to _UDP_.

**TCP port**

The TCP port the SysLog server is listening on. Used when *Protocol* is set to _TCP_.

### Message properties

**Facility**

The SysLog facility used for the message (for example *Kernel*, *User*, *Mail*, *Daemon*, *Auth*, *Syslog*, *LPR*, *News*, *UUCP*, *Cron*, *Local0*–*Local7*).

**Level**

The SysLog severity level used for the message (for example *Emergency*, *Alert*, *Critical*, *Error*, *Warning*, *Notice*, *Information*, *Debug*).

**Application**

A free-text application name included in the SysLog message.

**Message**

The body of the SysLog message to send.
