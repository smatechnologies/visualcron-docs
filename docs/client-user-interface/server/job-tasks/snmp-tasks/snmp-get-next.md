---
sidebar_label: 'Task SNMP - SNMP Get Next'
hide_title: 'true'
---

## Task SNMP - SNMP Get Next

Issues a GETNEXT message to an SNMP agent in order to inspect the value of the next variable. SNMP (Simple Network Management Protocol) is a UDP-based protocol used mostly in network management systems to monitor network-attached devices for conditions that warrant administrative attention.

**SNMP Get Next > General** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/SNMP%20Tasks/Get%20Next.png)

**Agent IP Address**

The IP address of the SNMP agent (device or host) to query.

**Variable Name**

The OID of the variable to retrieve the next value for. You can enter the OID in numeric format (e.g., `1.3.6.1.2.1.1.1.0`) or string notation (e.g., `system.sysDescr`). Use the Translate button to convert between formats.

**Community**

The SNMP community string used for authentication. The default value is `public`.

**SNMP Get Next > Advanced** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/SNMP%20Tasks/Get%20Next%20Advanced.png)

**Remote Port**

The UDP port number on the remote SNMP agent to send requests to. The default port is 162.

**Time out after**

The amount of time to wait for a response from the SNMP agent before the request times out. The default is 30 seconds.

**Broadcast delay**

The delay to apply when sending broadcast requests, allowing agents time to respond. The default is 3 seconds.

**SNMP version**

The SNMP protocol version to use for the request. The default is SNMPv1.

**SNMP Get Next > Data** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/SNMP%20Tasks/Get%20Next%20Data.png)

**Use string notation for OIDs**

When checked, OID values in the response are displayed using human-readable string notation instead of numeric dot notation.

**Use string notation for timetick values**

When checked, timetick values in the response are displayed as formatted time strings rather than raw numeric values.
