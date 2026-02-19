---
sidebar_label: 'Task Database - Execute SSISDB Package'
hide_title: 'true'
---

## Task Database - Execute SSISDB Package

The Task Database - Execute SSISDB package executes an existing package in from catalogs (SSISDB).
 
**Execute SSISDB package** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Database%20Tasks/Execute%20SSISDB%20Package.png)

**Connection**

Text ...
 
**Credentials**

To control a remote computer you may need to use a Credential. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the Settings icon to open Manage credentials in order to add or edit Credentials.
 
**Package details**

Text ...

**Execution details**

**Use dtexec for package execution**

When enabled, VisualCron uses the dtexec.exe command-line utility to execute the SSIS package instead of the Catalog API. This provides an alternative execution method with several benefits:

- **Process isolation**: Package execution runs in a separate process, reducing impact on the VisualCron service
- **Compatibility**: Better compatibility with certain package types and legacy SQL Server installations
- **Troubleshooting**: Easier to debug through standard command-line output
- **Resource management**: Better suited for long-running packages or resource-constrained environments

When disabled (default), packages are executed using the SQL Server Integration Services Catalog API through .NET Management Objects.

:::warning Empty String Parameters

When using dtexec.exe for package execution, empty string parameter values cannot be processed and will result in error code 6 (internal error). Ensure all string parameters have non-empty values, or use the Catalog API execution mode (uncheck this option) which supports empty string values.

:::

**Execute in 32 bit mode**

Check this option if your SSIS package requires 32-bit execution mode. This is commonly needed when the package uses 32-bit drivers or components.

**Package parameters**

Text ...

:::info Note

- SQL Server Integration Services must be installed on the machine where VisualCron is running
- For dtexec.exe execution mode, the SQL Server client tools must be installed on the VisualCron server
- When using trusted connections, you may need to specify a Credential with appropriate permissions to execute packages in SSISDB
- The SSISDB catalog must be created and configured on the target SQL Server instance

:::

### Troubleshooting

**Error code 6: Internal error when using dtexec**

This error occurs when empty string parameter values are passed to dtexec.exe.

**Solution**:
1. Check all string parameters and ensure they have non-empty values, or
2. Uncheck "Use dtexec for package execution" to use Catalog API mode

**Cannot locate dtexec.exe**

This error indicates that dtexec.exe could not be found on the system.

**Solution**:
1. Verify SQL Server Integration Services is installed on the VisualCron server
2. Check that SQL Server client tools are installed
3. Use Catalog API mode (uncheck "Use dtexec for package execution") which does not require dtexec.exe

**Package execution fails with "Could not load file or assembly" error**

**Solution**:
1. Enable "Execute in 32 bit mode" if your package uses 32-bit components
2. Verify all package dependencies are installed on the VisualCron server