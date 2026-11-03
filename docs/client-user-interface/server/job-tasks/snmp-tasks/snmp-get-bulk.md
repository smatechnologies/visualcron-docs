---
sidebar_label: 'Task SNMP - SNMP Get Bulk'
hide_title: 'true'
---

## Task SNMP - SNMP Get Bulk

The SNMP Get Bulk Task sends a GETBULK request to an SNMP agent to read a group of variables in one request, which is useful for large tables. For the first variable bindings in the request it performs one GETNEXT each; for each of the other bindings it performs repeated GETNEXT operations. GETBULK is not available in SNMPv1.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

The Task settings are on the ***SNMP Get Bulk*** tab, which has the sub tabs ***General***, ***Advanced***, ***Data Bindings*** and ***Security***.

### SNMP Get Bulk: General tab

![General tab of the SNMP Get Bulk Task, with the Agent IP Address, Return variable for the first, Max number of variables and Community fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/SNMP%20Tasks/Get%20Bulk.png)

- _Agent IP Address_: The IPv4 address or host name of the SNMP agent; it can contain Variables

  For a host name, the Task uses its first IPv4 address. A host name that cannot be resolved stops the Task with an error.

- _Return variable for the first_: The number of variable bindings, counted from the top of the list on the ***Data Bindings*** tab, for which one GETNEXT is performed (non-repeaters); "1" by default
- _Max number of variables to be returned for the rest of the variable bindings_: The maximum number of variables returned for each of the other bindings (max-repetitions); "1" by default

- _Community_: The community string, "public" by default

  With "SNMPv3" this field is labeled _User_ and holds the SNMPv3 user name.

Variables are resolved only in _Agent IP Address_.

### SNMP Get Bulk: Advanced tab

![Advanced tab of the SNMP Get Bulk Task, with the Remote Port, Time out after, Broadcast delay and SNMP version settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/SNMP%20Tasks/Get%20Bulk%20Advanced.png)

- _Remote Port_: The UDP port of the SNMP agent

  A new Task shows "162", the port for SNMP traps. SNMP agents normally listen on port "161", so enter the port of your agent.

- _Time out after_: How long to wait for the response, in "milliseconds", "seconds", "minutes" or "hours"

  The default is "30" with the unit "seconds". When no response arrives in time, the Task fails with an error.

- _Broadcast delay_: When _Agent IP Address_ is the broadcast address "255.255.255.255", how long to wait for a response instead of _Time out after_

  The default is "3" with the unit "seconds".

- _SNMP version_: "SNMPv2c" or "SNMPv3"; GETBULK does not exist in SNMPv1

  A new Task shows no version, and the request is then sent as "SNMPv2c". With "SNMPv3", the _Community_ label changes to _User_ and the ***Security*** tab appears.

### SNMP Get Bulk: Data Bindings tab

![Data Bindings tab of the SNMP Get Bulk Task, with the variable list, the Add, Edit and Delete buttons and the two string notation check boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/SNMP%20Tasks/Get%20Bulk%20Data%20Bindings.png)

- _Variable Name_: The list of OIDs in the request, at least one

  Click _Add..._ or _Edit..._ to open the _Define variable binding_ window, enter the OID in _Variable name_ as a number or a name, and click _Translate_ to show the other form. Click _Delete_ to remove the selected OID.

- _Use string notation for OIDs_: Selected by default; writes the OIDs in the output as names instead of numbers
- _Use string notation for timetick values_: Selected by default; writes TimeTicks values as a duration instead of a number

### SNMP Get Bulk: Security tab

The ***Security*** tab appears only with "SNMPv3" on the ***Advanced*** tab.

- _Security Level_: "None" (the default), "Authenticate" or "Authenticate and Encrypt"
- _Authentication Protocol_: "MD5" (the default) or "SHA-1", for "Authenticate" and "Authenticate and Encrypt"
- _Authentication Passphrase_: The authentication passphrase, at least 8 characters
- _Encryption Protocol_: "DES", the only choice, for "Authenticate and Encrypt"
- _Encryption Passphrase_: The encryption passphrase, at least 8 characters
- _Specify Context_: Enables _Context Name_ and _Context Engine ID_
- _Context Name_ and _Context Engine ID_: The SNMPv3 context

  This Task does not use these values: it uses the context that the agent reports.

### Output and errors

The output of the Task lists the SNMP version, the community or user name, and the error status and error index of the response, then one line for each variable in this form:

```text
<OID> = <type> : <value>
```

With SNMPv3, the output also lists the security parameters and the context of the response.

When the agent answers with an error status, the Task fails with that status as the error.

:::warning

When _Agent IP Address_ is a host name with no IPv4 address, or a variable binding cannot be converted, nothing is sent, the output stays empty, and the Task reports success. To catch this, check on the ***On error*** tab whether the output is empty (see [Task - On Error](../../task-on-error)).

:::

:::warning

The output of the Task contains the community string (SNMPv1 and SNMPv2c) or the user name (SNMPv3) in plain text, so anyone who can see the Task output can read it. SNMPv1 and SNMPv2c also send the community string over the network unencrypted.

:::
