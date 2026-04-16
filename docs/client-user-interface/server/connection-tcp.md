---
sidebar_label: 'Connection - TCP'
hide_title: 'true'
---

## Connection - TCP

The TCP Connection stores the IP address, port, and encoding properties used to create TCP listeners or clients and perform simple message-based communication.
 
### About TCP

The Transmission Control Protocol (TCP) is one of the main protocols of the Internet protocol suite. TCP provides reliable, ordered, and error-checked delivery of a stream of bytes between applications running on hosts communicating via an IP network. TCP is connection-oriented, and a connection between client and server is established before data can be sent. The server must be listening (passive open) for connection requests from clients before a connection is established.

The TCP Connection is used in the [Net - TCP](../server/job-tasks/net-tasks/tcp) Task (which acts as a TCP client) and the [Event trigger - TCP](event-trigger-tcp) Trigger (which acts as a TCP server, or listener).

**Manage Connections > Add > TCP > Common settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/TCP/TCP.png)

**Name**

A descriptive name for the connection to distinguish it from other connections.

**Group**

The group that the connection is a part of.
 
**Timeout**

The amount of time, in seconds, that a TCP client (both in the [Net - TCP](../server/job-tasks/net-tasks/tcp) Task and the [Event trigger - TCP](event-trigger-tcp) Trigger) will wait to receive data once a read operation is initiated.
 
**Code page**

The encoding used for text messages sent by the TCP client to the TCP server and vice versa.
 
**Manage Connections > Add > TCP > Connection settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/TCP/Settings.png)

**Address**

The host address of the TCP server. Can be an IP address in dotted-quad notation (IPv4), colon-hexadecimal notation (IPv6), or a DNS name (TCP Task only).
 
**Port**

For the TCP Task: the port number of the remote host to connect to. For the TCP Trigger: the port on which to listen for incoming connection attempts. Default: 9090.
 
**Maximum number of connected clients**

The maximum number of simultaneously connected TCP clients allowed when acting as a TCP listener. Set to 0 for an unlimited number of clients. Click **Reset** to restore the default value.

**Log sent messages to task output**

When checked, all messages sent from VisualCron to the remote TCP server are logged and stored in the Task output.

**Log received messages to task output**

When checked, all messages received by VisualCron from the remote TCP server are logged and stored in the Task output.
