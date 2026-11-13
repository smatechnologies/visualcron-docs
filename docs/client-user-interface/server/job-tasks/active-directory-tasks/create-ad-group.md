---
sidebar_label: 'Task Active Directory - Create AD Group'
hide_title: 'true'
---

## Task Active Directory - Create AD Group

The Create AD Group Task creates an Active Directory group in a parent container. A group is an Active Directory object that holds users, contacts, computers and other groups, so that they can be managed as one unit.

![Create AD Group tab with the Credentials list, Parent path, Name, Display name, Description, Group type and Group scope](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Active%20Directory%20Tasks/Create%20AD%20Group.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Create AD Group tab

- _Credentials_: the Credential that the Task uses to connect to Active Directory; see [Global - Credentials](../../global-credentials). Click the _Settings_ icon to open _Manage credentials_

  With "No Credential", the Task connects as the account that the VisualCron Server service runs as. The account that is used needs permission in Active Directory for what the Task does.

  When the selected Credential has been deleted, the Task fails, but it may already have carried out the change as the account of the VisualCron Server service.

- _Parent path_: the LDAP path of the container to create the group in, for example `LDAP://OU=<unit>,DC=<domain>,DC=<suffix>`. Click _Select container_ to pick it
- _Name_: the name of the group. The Task uses it as both the common name (CN) and the pre-Windows 2000 name of the group
- _Display name_: the display name of the group
- _Description_: the description of the group. When it is empty, no description is set
- _Group type_: "Security" (default) or "Distribution"

  A security group can be given permissions on shared resources and Group Policy settings, and can also be used as an e-mail distribution list. A distribution group is used only as an e-mail distribution list, for example in Microsoft Exchange or Outlook.

- _Group scope_: "Domain Local Group" (default) or "Global Group"

  A domain local group grants permissions on resources in the domain where it is created, and can have members from any domain. A global group holds users with a similar role and can be given access to resources in any domain of the same forest. The Task cannot create a universal group.

### Output and errors

The Task writes no output. When Active Directory rejects the request, for example because the account does not have permission or the object does not exist, the Task fails with the error that Active Directory returns.
