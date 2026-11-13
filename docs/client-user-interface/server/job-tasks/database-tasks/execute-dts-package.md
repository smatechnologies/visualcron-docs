---
sidebar_label: 'Task Database - Execute DTS Package'
hide_title: 'true'
---

## Task Database - Execute DTS Package

The Execute DTS package Task runs a DTS (Data Transformation Services) package from a file or from a SQL Server database. The DTS runtime must be installed on the VisualCron Server. To run a package on a remote server, use the ***Job*** sub tab of the [SQL Task](sql) with a SQL Server Agent job for the package.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

:::warning

The Task does not run the package as the user in _SQL Credential_. With _Use trusted connection_, the package is loaded from the database under the account of the VisualCron Server, which must have access to the SQL Server.

Variables in the _Value_ of a package variable are not replaced: the value is passed to the package as entered. Variables can be used in the variable name.

:::

### Execute DTS package tab

![Execute DTS package tab with the package location settings and the Variables list](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Database%20Tasks/Execute%20DTS%20Package.png)

**Main settings**

- _Package located in file_: Select to run a package from a structured storage file
- _Package path_: The full path of the package file
- _Password_: The password of the package file, if it has one
- _Package located in database_: Select to run a package stored in a SQL Server database
- _SQL server host name_: The host name or IP address of the SQL Server where the package is stored. When it is empty, the domain of the _SQL Credential_ is used as the host name
- _Package name_: The name of the package in the database
- _SQL Credential_: Required with _Package located in database_. Without _Use trusted connection_, the user name and password of this Credential are used to log on to SQL Server. Click the icon next to the list to open _Manage credentials_; see [Global - Credentials](../../global-credentials)
- _Use trusted connection_: When selected, the package is loaded with Windows authentication, under the account of the VisualCron Server

**Variables**

The global variables to set in the package before it runs. Click _Add_ to add a variable, _Edit_ to change the selected variable, or _Delete_ to remove it.

### Output and errors

- With "Fail on error" selected on the ***On error*** tab, the default, the package stops at its first failed step
- When the _SQL Credential_ is not found, the error "Could not find specified Credential" is written to the error output
