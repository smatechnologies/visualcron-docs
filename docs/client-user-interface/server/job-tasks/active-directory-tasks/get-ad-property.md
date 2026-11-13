---
sidebar_label: 'Task Active Directory - Get AD Property'
hide_title: 'true'
---

## Task Active Directory - Get AD Property

The Get AD Property Task writes the values of one or more properties of an Active Directory object to the output.

![Get AD Object property tab with the Credentials list, Parent path, Property name, and the Select object and Select container buttons](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Active%20Directory%20Tasks/Get%20AD%20Object%20property.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Get AD Object property tab

- _Credentials_: the Credential that the Task uses to connect to Active Directory; see [Global - Credentials](../../global-credentials). Click the _Settings_ icon to open _Manage credentials_

  With "No Credential", the Task connects as the account that the VisualCron Server service runs as. The account that is used needs permission in Active Directory for what the Task does.

  When the selected Credential has been deleted, the Task fails, but it may already have read Active Directory as the account of the VisualCron Server service.

- _Parent path_: despite its label, the LDAP path of the object to read itself, not of its container, for example `LDAP://CN=<name>,OU=<unit>,DC=<domain>,DC=<suffix>`. Click _Select object_ to pick the object. _Select container_ puts the path of a container in the field instead
- _Property name_: the LDAP name of the property, for example `cn`, `distinguishedName` or `mail`. To read several properties, separate the names with commas and no spaces, for example `cn,mail`

### Output and errors

The output has the values in the order of the names, separated by commas. Large-number date properties, such as `pwdLastSet` and `lastLogon`, are shown as a UTC date, or "Never" when they are 0. For a property with several values, the output shows `System.Object[]` instead of the values.

:::warning

When a property does not exist or has no value, its position in the output is empty, the error is written to standard error, and the Task reports success.

:::
