---
sidebar_label: 'Task SNMP - SNMP Walk'
hide_title: 'true'
---

## Task SNMP - SNMP Walk

The SNMP Walk Task reads all variables in a subtree of an SNMP agent, by sending GETNEXT requests from the root OID you enter until the agent returns a variable outside the subtree. SNMP (Simple Network Management Protocol) is a UDP-based protocol used mostly by network management systems to monitor network-attached devices.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

The Task settings are on the ***SNMP Walk*** tab, which has the sub tabs ***General***, ***Advanced***, ***Data*** and ***Security***.

### SNMP Walk: General tab

![General tab of the SNMP Walk Task, with the Agent IP Address, Variable Name and Community fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/SNMP%20Tasks/Walk.png)

- _Agent IP Address_: The IPv4 address or host name of the SNMP agent; it can contain Variables

  For a host name, the Task uses its first IPv4 address. A host name that cannot be resolved stops the Task with an error.

- _Variable Name_: The root OID of the subtree to read, as a number such as `1.3.6.1.2.1.1` or a name such as `system`

  Names are case-sensitive. Click _Translate_ to show the other form of the OID you entered.

- _Community_: The community string, "public" by default

  With "SNMPv3" this field is labeled _User_ and holds the SNMPv3 user name.

Variables are resolved only in _Agent IP Address_.

### SNMP Walk: Advanced tab

![Advanced tab of the SNMP Walk Task, with the Remote Port, Time out after, Broadcast delay and SNMP version settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/SNMP%20Tasks/Walk%20Advanced.png)

- _Remote Port_: The UDP port of the SNMP agent

  A new Task shows "162", the port for SNMP traps. SNMP agents normally listen on port "161", so enter the port of your agent.

- _Time out after_: How long to wait for the response, in "milliseconds", "seconds", "minutes" or "hours"

  The default is "30" with the unit "seconds". When no response arrives in time, the Task fails with an error.

- _Broadcast delay_: When _Agent IP Address_ is the broadcast address "255.255.255.255", how long to wait for a response instead of _Time out after_

  The default is "3" with the unit "seconds".

- _SNMP version_: "SNMPv1" (the default), "SNMPv2c" or "SNMPv3"

  With "SNMPv3", the _Community_ label changes to _User_ and the ***Security*** tab appears.

:::warning

With "SNMPv3", the walk does not move past the first variable of the subtree, so the Task does not finish by itself. Use "SNMPv1" or "SNMPv2c" for a walk.

:::

### SNMP Walk: Data tab

![Data tab of the SNMP Walk Task, with the two string notation check boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/SNMP%20Tasks/Walk%20Data.png)

- _Use string notation for OIDs_: Selected by default; writes the OIDs in the output as names instead of numbers
- _Use string notation for timetick values_: Selected by default; writes TimeTicks values as a duration instead of a number

### SNMP Walk: Security tab

The ***Security*** tab appears only with "SNMPv3" on the ***Advanced*** tab.

- _Security Level_: "None" (the default), "Authenticate" or "Authenticate and Encrypt"
- _Authentication Protocol_: "MD5" (the default) or "SHA-1", for "Authenticate" and "Authenticate and Encrypt"
- _Authentication Passphrase_: The authentication passphrase, at least 8 characters
- _Encryption Protocol_: "DES", the only choice, for "Authenticate and Encrypt"
- _Encryption Passphrase_: The encryption passphrase, at least 8 characters
- _Specify Context_: Enables _Context Name_ and _Context Engine ID_
- _Context Name_ and _Context Engine ID_: The SNMPv3 context

  This Task sends _Context Name_; _Context Engine ID_ is not used.

### Output and errors

The output of the Task lists the SNMP version, the community or user name, and the error status and error index of the response, then one line for each variable in this form:

```text
<OID> = <type> : <value>
```

With SNMPv3, the output also lists the security parameters and the context of the response.

:::warning

The walk ends at the end of the subtree or at the first response with an error status. In both cases the output holds the variables read until then, and the Task reports success. When _Agent IP Address_ is a host name with no IPv4 address, or a variable binding cannot be converted, nothing is sent, the output stays empty, and the Task reports success. To catch this, check the output on the ***On error*** tab; see [Task - On Error](../../task-on-error).

:::

:::warning

The output of the Task contains the community string (SNMPv1 and SNMPv2c) or the user name (SNMPv3) in plain text, so anyone who can see the Task output can read it. SNMPv1 and SNMPv2c also send the community string over the network unencrypted.

:::
