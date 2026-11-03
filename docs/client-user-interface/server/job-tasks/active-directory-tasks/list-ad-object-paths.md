---
sidebar_label: 'Task Active Directory - List AD Object Paths'
hide_title: 'true'
---

## Task Active Directory - List AD Object Paths

The List AD Object Paths Task lists the LDAP paths of the Active Directory objects, such as computers, users and groups, at and below a container that match a filter.

![List AD Object paths tab with the Credentials list, Get Active Directory object using, Parent path, Object type and Filter](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Active%20Directory%20Tasks/List%20AD%20Object%20paths.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### List AD Object paths tab

- _Credentials_: the Credential that the Task uses to connect to Active Directory; see [Global - Credentials](../../global-credentials). Click the _Settings_ icon to open _Manage credentials_

  With "No Credential", the Task connects as the account that the VisualCron Server service runs as. The account that is used needs permission in Active Directory for what the Task does.

  When the selected Credential has been deleted, the Task fails, but it may already have read Active Directory as the account of the VisualCron Server service.

- _Get Active Directory object using_: how the objects are selected: "Simple filter" (default), "Custom filter" or "ADO Query". The fields below change with the choice
- _Parent path_: the LDAP path of the container to search. The Task searches the container and every container below it, for example `LDAP://OU=<unit>,DC=<domain>,DC=<suffix>`. Click _Select container_ to pick it

With "Simple filter":

- _Object type_: "User" (default), "Computer", "Organization Unit", "Group" or "Printer"
- _Filter_: the name of the objects to list. `*` matches any characters, so `*` lists every object of the type

With "Custom filter":

- _Query statement (SQL or LDAP syntax)_: an LDAP search filter, for example `(&(objectCategory=user)(department=Sales))`. With "Custom filter", the statement is used as an LDAP filter only

:::warning

With "ADO Query", the Client saves the _Query statement_ as a custom filter and not as a query, so the Task does not run the statement and fails. Use "Custom filter" with an LDAP filter instead.

:::

### Output and errors

The output has the LDAP path of each object found, one per line. When no object matches, the output is empty and the Task succeeds.

:::warning

Active Directory returns at most 1,000 objects by default. When more objects match, the rest are left out, and the Task reports success. Narrow the filter or the container.

:::
