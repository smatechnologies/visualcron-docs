---
sidebar_label: 'Connection - TCP'
hide_title: 'true'
---

## Connection - TCP

The TCP Connection stores the address, port and encoding settings that the [Net - TCP](job-tasks/net-tasks/tcp) Task and the [Event Trigger - TCP](event-trigger-tcp) Trigger use for plain TCP messaging. The Task uses it as a client that connects to a server. The Trigger uses it as a listener that waits for clients. TCP Connections have no encryption and no ***Proxy*** tab, so messages are sent unencrypted.

### Common settings

![TCP Connection, Common settings tab, with the Test button](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/TCP/TCP.png)

The ***Common settings*** tab is the same for every Connection type that has it; see [Common settings](global-connections#common-settings). For TCP Connections:

- _Test_: the Server opens a TCP connection to *Address* and *Port*, and reports whether it succeeded. It does not send a message
- _Timeout_: how long, in seconds, the Task and the Trigger wait for data once they start reading
- _Code page_: the encoding of the text messages that are sent and received

### Main settings

These fields are on ***Connection settings*** -> ***Main settings***.

![TCP Connection, Main settings tab, with the Server, TCP Listener and Log traffic groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/TCP/Settings.png)

- _Address_: for the Task, the host name or IPv4 address of the server to connect to. For the Trigger, the local IP address to listen on, for example "0.0.0.0" for all local addresses
- _Port_: for the Task, the port of the server. For the Trigger, the port to listen on. A new Connection shows "21"; enter the port you need
- _Maximum number of connected clients_: for the Trigger, how many clients can be connected at the same time. "0" means no limit. *Reset* sets it to "0"
- _Log sent messages to task output_: writes the messages that VisualCron sends into the Task output
- _Log received messages to task output_: writes the messages that VisualCron receives into the Task output

:::warning

Enter only a host name or an IPv4 address in *Address*, without a scheme, a port or a path. When the text contains ":", "/" or "\\", the Client splits it at those characters and saves only the second part. An IPv6 address, an address followed by a colon and a port, or an address followed by a path is saved wrongly, and the Task or Trigger cannot connect.

:::
