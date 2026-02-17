---
sidebar_label: 'Task SNMP - SNMP Set'
hide_title: 'true'
---

## Task SNMP - SNMP Set

Issues an SNMP SET message to an SNMP agent in order to alter the value of a variable. SNMP (Simple Network Management Protocol) is a UDP-based protocol used mostly in network management systems to monitor network-attached devices for conditions that warrant administrative attention.

**SNMP Set > General** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/SNMP%20Tasks/Set%20General.png)

**Agent IP Address**

The IP address of the SNMP agent (device or host) to send the SET request to.

**Variable Name**

The OID of the variable to set. You can enter the OID in numeric format (e.g., `1.3.6.1.2.1.1.4.0`) or string notation (e.g., `system.sysContact.0`). Use the Translate button to convert between formats.

**Community**

The SNMP community string used for authentication. The default value is `public`.

**Variable syntax**

The data type of the value being set (e.g., integer, string, OID). Select the appropriate syntax to match the variable's expected type. The default is `integer`.

**Variable value**

The new value to assign to the specified variable.

**SNMP Set > Advanced** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/SNMP%20Tasks/Set%20Advanced.png)

**Remote Port**

The UDP port number on the remote SNMP agent to send requests to. The default port is 162.

**Time out after**

The amount of time to wait for a response from the SNMP agent before the request times out. The default is 30 seconds.

**Broadcast delay**

The delay to apply when sending broadcast requests, allowing agents time to respond. The default is 3 seconds.

**SNMP version**

The SNMP protocol version to use for the request. The default is SNMPv1.
