---
sidebar_label: 'Task Database - Execute SSIS Package'
hide_title: 'true'
---

## Task Database - Execute SSIS Package

The Execute SSIS package Task runs an SSIS (SQL Server Integration Services) package from a file or from a SQL Server database. SQL Server Integration Services must be installed on the VisualCron Server. To run a package on a remote server, use the ***Job*** sub tab of the [SQL Task](sql) with a SQL Server Agent job for the package, or the [Execute SSISDB Package](execute-ssisdb-package) Task for a package in an SSIS catalog.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Execute SSIS package tab

![Execute SSIS package tab with the MSSQL server version, Credential for trusted connection and package location settings and the Variables list](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Database%20Tasks/Execute%20SSIS%20Package.png)

**Main settings**

- _MSSQL server version_: The version of SQL Server Integration Services installed on the VisualCron Server: "2005", "2008", "2012", "2014", "2016", "2017", "2019", "2022" or "2025". The default is "2005"
- _Execute in 32bit mode_: When selected, the package runs in a 32-bit process. Select it when the installed Integration Services, or a driver or component that the package uses, is 32-bit
- _Trusted connection_: When selected, Windows authentication is used to load the package from the database, instead of the _Database credential_
- _Credential for trusted connection_: The Windows user that the whole package run uses. With no Credential, the package runs under the account of the VisualCron Server. Click the icon next to the list to open _Manage credentials_; see [Global - Credentials](../../global-credentials)
- _Package password_: The password of the package, if it has one
- _Configuration file_: When selected, the XML configuration file in the field next to it is loaded for the package before it runs. When the file does not exist, the Task fails with the error "Config file was not found."
- _Package located in file_: Select to run a package from a file
- _Package path_: The full path of the package file
- _Package located in database_: Select to run a package stored in a SQL Server database
- _Package name_: The name of the package in the database
- _Database ip/dns name_: The host name or IP address of the SQL Server where the package is stored
- _Database credential_: The Credential with the SQL Server logon used to load the package from the database, when _Trusted connection_ is cleared

**Variables**

The package variables to set before the package runs. Click _Add_ to add a variable, _Edit_ to change the selected variable, or _Delete_ to remove it. Variables can be used in the names and values.

:::info Note

For this Task to work, at least SQL Server Integration Services must be installed on the machine where VisualCron is installed.
For more information, see [SQL Server Integration Services](https://en.wikipedia.org/wiki/SQL_Server_Integration_Services).

:::

### Output and errors

- The package runs in a separate process. Its output and errors are the output and error output of the Task, and the Task fails when the package fails

### Troubleshooting

**Could not load file or assembly '`Microsoft.SqlServer.DTSRuntimeWrap`'.**

1. Install SQL Server Integration Services.
2. Set _Execute in 32bit mode_ to match the 32-bit or 64-bit SQL Server Integration Services that is installed.
