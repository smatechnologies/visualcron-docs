---
sidebar_label: 'Task SNMP - SNMP Walk'
hide_title: 'true'
---

## Task SNMP - SNMP Walk

Issues a Walk message to an SNMP agent in order to inspect a group of variables. SNMP (Simple Network Management Protocol) is a UDP-based protocol used mostly in network management systems to monitor network-attached devices for conditions that warrant administrative attention.

**SNMP Walk > General** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/SNMP%20Tasks/Walk.png)

**Agent IP Address**

The IP address of the SNMP agent (device or host) to query.

**Variable Name**

The root OID from which the walk begins, traversing all variables in the subtree. You can enter the OID in numeric format (e.g., `1.3.6.1.1`) or string notation (e.g., `system`). Use the Translate button to convert between formats.

**Community**

The SNMP community string used for authentication. The default value is `public`.

**SNMP Walk > Advanced** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/SNMP%20Tasks/Walk%20Advanced.png)

**Remote Port**

The UDP port number on the remote SNMP agent to send requests to. The default port is 162.

**Time out after**

The amount of time to wait for a response from the SNMP agent before the request times out. The default is 30 seconds.

**Broadcast delay**

The delay to apply when sending broadcast requests, allowing agents time to respond. The default is 3 seconds.

**SNMP version**

The SNMP protocol version to use for the request. The default is SNMPv1.

**SNMP Walk > Data** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/SNMP%20Tasks/Walk%20Data.png)

**Use string notation for OIDs**

When checked, OID values in the response are displayed using human-readable string notation instead of numeric dot notation.

**Use string notation for timetick values**

When checked, timetick values in the response are displayed as formatted time strings rather than raw numeric values.
