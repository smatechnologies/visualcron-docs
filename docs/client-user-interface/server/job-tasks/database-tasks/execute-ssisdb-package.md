---
sidebar_label: 'Task Database - Execute SSISDB Package'
hide_title: 'true'
---

## Task Database - Execute SSISDB Package

The Execute SSISDB package Task runs a package that is deployed to an SSIS catalog (SSISDB) on SQL Server, using a SQL Connection.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Execute SSISDB package tab

![Execute SSISDB package tab with the Connection and Credential fields, the Package details, the Package parameters grid and the Execution details](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Database%20Tasks/Execute%20SSISDB%20Package.png)

**Connection**

- _Connection_: The SQL Connection to the SQL Server that hosts the catalog; see [Connection - SQL](../../connection-sql) and [Global - Connections](../../global-connections)
- _Credential_: The Windows user the package run uses. It is also used when the Client loads the lists below. With Windows authentication, this user needs permission to run packages in the catalog. With no Credential, the account of the VisualCron Server is used

**Package details**

Click _Refresh_ next to a field to load its list from the server.

- _Catalog_: The SSIS catalog. The default is "SSISDB"
- _Folder_: The folder in the catalog that contains the project
- _Project name_: The SSIS project
- _Package name_: The package to run
- _Environment_: Optional. The environment reference of the project to use for the run

Variables can be used in these fields and in the parameter names and values.

**Package parameters and Project parameters**

The ***Package parameters*** and ***Project parameters*** sub tabs list the parameters of the selected package and project, with their _Name_, _Data type_, _Direction_ and _Value_. Click _Refresh_ to load them from the server, and use _Add_, _Edit_ and _Delete_ to change the list.

**Execution details**

- _Execute in 32 bit mode (on 64 bit systems)_: When selected, the package runs in 32-bit mode. Select it when the package uses 32-bit drivers or components
- _Use dtexec for package execution_: When selected, the package is run with the `dtexec.exe` command-line utility of SQL Server instead of the Integration Services catalog API. When cleared, the default, the catalog API is used

With _Use dtexec for package execution_:

- The package runs with Windows authentication, as the user in _Credential_ or the account of the VisualCron Server. A user name and password in the Connection are not used
- The package path always uses the catalog "SSISDB", whatever _Catalog_ is set to
- An empty value of a numeric parameter is sent as "0", and a Boolean value other than "True" or "1" is sent as "False"
- The name and value of every parameter, including sensitive values, can be written to the VisualCron log

:::warning

When using dtexec.exe for package execution, empty string parameter values cannot be processed and will result in error code 6 (internal error). Ensure all string parameters have non-empty values, or use the catalog API (clear _Use dtexec for package execution_), which supports empty string values.

:::

:::info Note

- SQL Server Integration Services must be installed on the machine where VisualCron is running
- With _Use dtexec for package execution_, the SQL Server client tools must be installed on the VisualCron Server
- The SSISDB catalog must be created and configured on the target SQL Server instance

:::

### Output and errors

- The package runs in a separate process, and the Task fails when the package fails or is canceled
- With the catalog API, the messages of the package run and the line "ExecutePackage->Completed without any serious errors" are written to the error output, also when the package succeeds. Keep this in mind when you add an error condition on the error output on the ***On error*** tab

### Troubleshooting

**Error code 6: Internal error when using dtexec**

This error occurs when empty string parameter values are passed to dtexec.exe.

**Solution**:

- Give every string parameter a non-empty value
- Clear _Use dtexec for package execution_ to use the catalog API

**Cannot locate dtexec.exe**

This error indicates that dtexec.exe could not be found on the system.

**Solution**:
1. Verify SQL Server Integration Services is installed on the VisualCron Server
2. Check that SQL Server client tools are installed
3. Use the catalog API (clear _Use dtexec for package execution_), which does not require dtexec.exe

**Package execution fails with "Could not load file or assembly" error**

**Solution**:
1. Select _Execute in 32 bit mode (on 64 bit systems)_ if your package uses 32-bit components
2. Verify all package dependencies are installed on the VisualCron Server
