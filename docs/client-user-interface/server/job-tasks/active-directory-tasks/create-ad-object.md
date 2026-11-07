---
sidebar_label: 'Task Active Directory - Create AD Object'
hide_title: 'true'
---

## Task Active Directory - Create AD Object

The Create AD Object Task creates a computer or an organizational unit in an Active Directory container.

![Create AD Object tab with the Credentials list, Parent path, Type and Name](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Active%20Directory%20Tasks/Create%20AD%20Object.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Create AD Object tab

- _Credentials_: the Credential that the Task uses to connect to Active Directory; see [Global - Credentials](../../global-credentials). Click the _Settings_ icon to open _Manage credentials_

  With "No Credential", the Task connects as the account that the VisualCron Server service runs as. The account that is used needs permission in Active Directory for what the Task does.

  When the selected Credential has been deleted, the Task fails, but it may already have carried out the change as the account of the VisualCron Server service.

- _Parent path_: the LDAP path of the container to create the object in, for example `LDAP://OU=<unit>,DC=<domain>,DC=<suffix>`. Click _Select container_ to pick it
- _Type_: "Computer" (default) or "Organization Unit"
- _Name_: the name of the new object. A computer is created as `CN=<name>` and an organizational unit as `OU=<name>`

### Output and errors

The Task writes no output. When Active Directory rejects the request, for example because the account does not have permission or the object does not exist, the Task fails with the error that Active Directory returns.
