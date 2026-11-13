---
sidebar_label: 'Task Active Directory - Move AD Object'
hide_title: 'true'
---

## Task Active Directory - Move AD Object

The Move AD Object Task moves an Active Directory object to another container. The object keeps its name.

![Move AD Object tab with the Credentials list, Parent path, Move to this container, and the Select object and Select container buttons](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Active%20Directory%20Tasks/Move%20AD%20Object.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Move AD Object tab

- _Credentials_: the Credential that the Task uses to connect to Active Directory; see [Global - Credentials](../../global-credentials). Click the _Settings_ icon to open _Manage credentials_

  With "No Credential", the Task connects as the account that the VisualCron Server service runs as. The account that is used needs permission in Active Directory for what the Task does.

  When the selected Credential has been deleted, the Task fails, but it may already have carried out the change as the account of the VisualCron Server service.

- _Parent path_: despite its label, the LDAP path of the object to move itself, not of its container, for example `LDAP://CN=<name>,OU=<unit>,DC=<domain>,DC=<suffix>`. Click _Select object_ to pick the object. _Select container_ puts the path of a container in the field instead
- _Move to this container_: the LDAP path of the destination container. Click the _Select container_ button below the field to pick it

### Output and errors

The Task writes no output. When Active Directory rejects the request, for example because the account does not have permission or the object does not exist, the Task fails with the error that Active Directory returns.
