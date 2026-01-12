---
sidebar_label: 'Task SNMP - SNMP Get Bulk'
hide_title: 'true'
---

## Task SNMP - SNMP Get Bulk

Issues a GETBULK message to an SNMP agent in order to inspect a group of variables in a single transaction. This action is particularly useful for retrieving large tables. The GETBULK operation performs a GETNEXT operation for the first number of variable bindings in the request and performs a GETNEXT operation (continuous) for each of the remaining variable bindings in the request list. Note that the SNMP GETBULK command is not supported on devices using SNMPv1.
 
**SNMP Get Bulk > General** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/SNMP%20Tasks/Get%20Bulk.png)

**Agent IP Address**

Text ...
 
**Return variable name for the first**

Text ...
 
**Community**

Text ...
 
**SNMP Get Bulk > Advanced** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/SNMP%20Tasks/Get%20Bulk%20Advanced.png)

**Remote Port**

Text ...
 
**Time out after**

Text ...
 
**Broadcast delay**

Text ...
 
**SNMP version**

Text ...
 
**SNMP Get Bulk > Data bindings** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/SNMP%20Tasks/Get%20Bulk%20Data%20Bindings.png)

**Variable name**

Text ...
 
**Use string notation for OIDs**

Text ...
 
**Use string notation for timetick values**

Text ...