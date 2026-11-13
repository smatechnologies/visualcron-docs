---
sidebar_label: 'Task Active Directory - Get AD Object Path'
hide_title: 'true'
---

## Task Active Directory - Get AD Object Path

The Get AD Object Path Task finds an Active Directory object by name and type and writes its LDAP path to the output.

![Get AD Object path tab with the Credentials list, Parent path, Object type and Name](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Active%20Directory%20Tasks/Get%20AD%20Object%20Path.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Get AD Object path tab

- _Credentials_: the Credential that the Task uses to connect to Active Directory; see [Global - Credentials](../../global-credentials). Click the _Settings_ icon to open _Manage credentials_

  With "No Credential", the Task connects as the account that the VisualCron Server service runs as. The account that is used needs permission in Active Directory for what the Task does.

  When the selected Credential has been deleted, the Task reads Active Directory as the account of the VisualCron Server service, and the Task reports success.

- _Parent path_: the LDAP path of the container to search. The Task searches the container and every container below it, for example `LDAP://OU=<unit>,DC=<domain>,DC=<suffix>`. Click _Select container_ to pick it
- _Object type_: "User" (default), "Computer", "Organization Unit", "Group" or "Printer"
- _Name_: the name of the object to find, for example a user's or computer's name. `*` matches any characters

### Output and errors

The output is the LDAP path of the first object found. When no object of that type and name exists, the Task fails.
