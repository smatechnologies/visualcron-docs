---
sidebar_label: 'Connection - SCP'
hide_title: 'true'
---

## Connection - SCP

The SCP Connection stores connect and logon properties for the Secure Copy (SCP) protocol. The SCP protocol is a [network protocol](https://en.wikipedia.org/wiki/Communication_protocol), based on the [BSD](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution) [RCP](https://en.wikipedia.org/wiki/Berkeley_r-commands) protocol, which supports [file transfers](https://en.wikipedia.org/wiki/File_transfer) between hosts on a network.
 
SCP uses [Secure Shell](https://en.wikipedia.org/wiki/Secure_Shell) (SSH) for data transfer and uses the same mechanisms for authentication, thereby ensuring the [authenticity](https://en.wikipedia.org/wiki/Information_security#Authenticity) and [confidentiality](https://en.wikipedia.org/wiki/Confidentiality) of the [data in transit](https://en.wikipedia.org/wiki/Data_in_transit). A client can send (upload) files to a server, optionally including their basic attributes (permissions, timestamps). Clients can also request files or directories from a server (download). SCP runs over [TCP port](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#TCP_ports) 22 by default. Like RCP, there is no [RFC](https://en.wikipedia.org/wiki/Request_for_Comments) that defines the specifics of the protocol.
 
In VisualCron, the SCP Connection is used in the [Net - FTP/FTPS/SFTP/SCP](../server/job-tasks/net-tasks/ftp) Task.
 
**Manage Connections > Add > SCP > Main settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SCP/SCP.png)

**Name**

This is a descriptive name of the connection to distinguish from other connections.
 
**Group**

The group that the connection is a part of.
 
**Timeout**

The connection timeout in seconds. Connection will fail after this time is passed.
 
**Code page**

The table of values that describes the desired character set. Currently this is overridden by the code page in the Task.
 
**Manage Connections > Add > SCP > Connection settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SCP/SCP%20Setting.png)

**Address**

This is the host address to the server. It could be a DNS name or IP number.

**Port**

This is the remote connection port.

**Authentication type**

Password
Public Key

**Username**

The user name for the connection.
 
**Password**

The password for the connection.

**Log Traffic**

Text