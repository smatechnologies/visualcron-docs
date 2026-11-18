---
sidebar_label: 'Task Net - Check Port'
hide_title: 'true'
---

## Task Net - Check Port

The Check Port Task checks whether a host accepts connections on a port.

![Check Port Task settings, with the Hostname, Port, Protocol and Timeout in milliseconds fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/Check%20Port.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

- _Hostname_: the host name or IP address to check

  The list also shows the computers on the network.

- _Port_: the port to check

  The default, "16444", is the port of the VisualCron Server, so change it to the port you want to check.

- _Protocol_: "TCP" (default) or "UDP"
- _Timeout in milliseconds_: how long sending and receiving can take, "5000" by default

  With "TCP", it does not limit the connection attempt, so an unreachable host can take as long as Windows waits for a connection. To limit how long the Task runs, use the Task's ***TimeOut*** tab (see [Task - Timeout](../../task-timeout)).

When the check passes, the output is "Connected". Otherwise the output is "Not connected" and the Task fails.

:::warning

With "UDP", a missing reply counts as success, because an open UDP port does not have to answer. The Task fails only when the host reports that the port is closed. A host that is down, or a firewall that drops the traffic, passes the check. Use "TCP" when you need a reliable result.

:::
