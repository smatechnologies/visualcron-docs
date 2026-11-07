---
sidebar_label: 'Task Active Directory - Get AD Group Members'
hide_title: 'true'
---

## Task Active Directory - Get AD Group Members

The Get AD Group Members Task writes the names of the members of an Active Directory group to the output.

![Get AD Group members tab with the Credentials list, Parent path and the Select group button](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Active%20Directory%20Tasks/Get%20AD%20Group%20Members.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Get AD Group members tab

- _Credentials_: the Credential that the Task uses to connect to Active Directory; see [Global - Credentials](../../global-credentials). Click the _Settings_ icon to open _Manage credentials_

  With "No Credential", the Task connects as the account that the VisualCron Server service runs as. The account that is used needs permission in Active Directory for what the Task does.

  When the selected Credential has been deleted, the Task fails, but it may already have read Active Directory as the account of the VisualCron Server service.

- _Parent path_: despite its label, the LDAP path of the group itself, for example `LDAP://CN=<group>,OU=<unit>,DC=<domain>,DC=<suffix>`. Click _Select group_ to pick it

### Output and errors

The output has the name of each direct member of the group, one per line. A member group is listed by its name; its own members are not listed.

:::warning

When a member cannot be read, the error is written to standard error, the member is left out of the output, and the Task reports success.

:::
