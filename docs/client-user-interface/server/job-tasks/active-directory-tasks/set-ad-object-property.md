---
sidebar_label: 'Task Active Directory - Set AD Object Property'
hide_title: 'true'
---

## Task Active Directory - Set AD Object Property

The Set AD Object Property Task sets one property of an Active Directory object to a value.

![Set AD Object property tab with the Credentials list, Parent path, Property name, Property value, and the Select object and Select container buttons](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Active%20Directory%20Tasks/Set%20AD%20Object%20Property.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Set AD Object property tab

- _Credentials_: the Credential that the Task uses to connect to Active Directory; see [Global - Credentials](../../global-credentials). Click the _Settings_ icon to open _Manage credentials_

  With "No Credential", the Task connects as the account that the VisualCron Server service runs as. The account that is used needs permission in Active Directory for what the Task does.

  When the selected Credential has been deleted, the Task fails, but it may already have carried out the change as the account of the VisualCron Server service.

- _Parent path_: despite its label, the LDAP path of the object to change itself, not of its container, for example `LDAP://CN=<name>,OU=<unit>,DC=<domain>,DC=<suffix>`. Click _Select object_ to pick the object. _Select container_ puts the path of a container in the field instead
- _Property name_: the LDAP name of the property, for example `description` or `telephoneNumber`
- _Property value_: the new value. It replaces every value that the property has. When it is empty, the property is cleared

:::warning

The Task overwrites the property: every existing value is replaced, and an empty _Property value_ clears the property. VisualCron keeps no copy of the old value.

:::

### Output and errors

The Task writes no output. When Active Directory rejects the request, for example because the account does not have permission or the object does not exist, the Task fails with the error that Active Directory returns.
