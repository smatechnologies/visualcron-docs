---
sidebar_label: 'Task Process - PowerShell'
hide_title: 'true'
---

## Task Process - PowerShell

The **PowerShell** Task lets you execute PowerShell code on the fly or an existing PowerShell file.

![Add Task window, PowerShell tab, Main settings sub tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Process%20Tasks/Powershell%20Main.png)

### Main settings tab

**Credentials**

With *Local* scope, the script runs as the user of the selected Credential, or as the account the VisualCron service runs under with *No Credential*. This applies with *Load user profile* selected on the Credential (the default); without it, the Credential is used only for network access (see [Local login and Load user profile](global-credentials#local-login-and-load-user-profile)). With *Remote* scope, select a Credential: it is the user that logs on to the remote computer, and the local PowerShell host also runs as that user. Select a Credential in the combo box, or click the *Settings* icon to open *Manage credentials* and add or edit one.
 
**Scope**

Select *Local* to execute the script on the same server that VisualCron is running on. Select *Remote* to execute on a different machine. When *Remote* is selected, the following fields become active:

* *Hostname* - the hostname or IP address of the remote machine
* *Port* - the WinRM port on the remote machine; the default is 5985
* *Authentication mechanism* - the authentication protocol to use when connecting. Options are:
  * *Basic* - transmits credentials as Base64-encoded text. Simple but less secure.
  * *Credssp* - delegates credentials to the remote machine, enabling "second hop" scenarios where the remote machine needs to connect to additional resources.
  * *Default* - uses the transport default (Negotiate or Kerberos for WSMan).
  * *Digest* - transmits credentials as a hash value rather than clear text.
  * *Kerberos* - uses Kerberos authentication.
  * *Negotiate* - uses Kerberos for domain accounts or NTLM for local accounts. Specify the username as domain\username for domain users or servername\username for local users.
  * *NegotiateWithImplicitCredential* - meant to use the credentials of the current Windows account; the Task also passes the selected Credential

The Task connects over HTTP (`http://<Hostname>:<Port>/wsman`); an HTTPS listener is not supported. Without a Credential, the connection fails. *Authentication mechanism* defaults to *Default*.

:::warning

Over HTTP, *Basic* works only if unencrypted WinRM traffic is allowed on both computers, and the password is then sent without encryption.

:::
 
### Script tab
 
**Execute in x86 mode**

When checked, forces 32-bit execution of your PowerShell script.
 
**PowerShell file**

Select this option to execute an existing PowerShell script file. Enter the full path to the .ps1 file in the field below, or use the browse button to select it. The file is read on the VisualCron Server and run as script text, also with *Remote* scope, so `$PSScriptRoot` is empty and paths relative to the script file do not resolve.

**Working directory**

The working directory for the PowerShell process when executing a file. The field can be edited only when *PowerShell file* is selected, but a saved value is also used for script text. If empty, a folder in the VisualCron installation folder is used; set it when the script uses relative paths. It has no effect with *Remote* scope.
 
**PowerShell script text**

Select this option to enter PowerShell code directly. Type or paste your script into the editor below. The code runs in a hosted Windows PowerShell session.
 
### Parameters tab

The Parameters tab lets you define named parameters that are passed into your PowerShell script. Each parameter has a Name, Type, and Value. Use the Add, Edit, and Delete buttons to manage the list.

Each parameter is passed to the script by name, so declare it in a `param()` block at the start of the script:

```powershell
param (
  [string]$parameterkeyname1 = "mydefaultvalue1",
  [string]$parameterkeyname2 = "mydefaultvalue2"
)
Write-Output $parameterkeyname1
```

### Commands tab

The Commands tab lets you build a list of discrete PowerShell commands to execute. The commands form one pipeline that runs before the script on the **_Script_** tab, and their output is passed to the script as pipeline input (`$input`). Each command entry has a Command name, Parameters, and Arguments. Use the Add, Edit, Delete, and Clear all buttons to manage the list.

### Script examples

About Script blocks
More information about script blocks here: [https://www.sapien.com/blog/2019/05/13/advanced-powershell-functions-begin-to-process-to-end/](https://www.sapien.com/blog/2019/05/13/advanced-powershell-functions-begin-to-process-to-end/)
 
### Starting script

In general you need to call the function after the script block. For example:

```powershell
Function Test-ScriptBlock
{
  Param([int]$Number)
  # function content
} #END Function Test-ScriptBlock
 
# the function call
Test-ScriptBlock -Number 1
```

### Passing parameters
 
1. No parameters

```powershell
Function Test-ScriptBlock
{
    BEGIN
    {
        Write-Output "In Begin block"
    }
    PROCESS
    {
        Write-Output "In Process block"
    }
    END
    {
        Write-Output "In End block"
    }
} #END Function Test-ScriptBlock
 
Test-ScriptBlock
``` 

2. parameters after function call

```powershell
Function Test-ScriptBlock
{
 Param
 (
     [int]$Number
 )
    BEGIN
    {
        Write-Output "In Begin block"
    }
    PROCESS
    {
        Write-Output "In Process block"
        Write-Output "Number value: "         $Number
    }
    END
    {
        Write-Output "In End block"
    }
} #END Function Test-ScriptBlock
 
 
Test-ScriptBlock -Number 1
```

3. Value parameters from pipeline

```powershell
Function Test-ScriptBlock
{
 Param
 ( 
     [Parameter(ValueFromPipeline)]
     [int]$Number
 )
    BEGIN
    {
        Write-Output "In Begin block"
    }
    PROCESS
    {
        Write-Output "In Process block"
        Write-Output "Number value: "         $Number
    }
    END
    {
        Write-Output "In End block"
    }
} #END Function Test-ScriptBlock
 
 
1, 2, 3 | Test-ScriptBlock
```

4. Using VisualCron parameters into script block

```powershell
param (
  [int]$Number = 0
)
Function Test-ScriptBlock
{
 Param
 (
     [int]$Number
 )
    BEGIN
    {
        Write-Output "In Begin block"
    }
    PROCESS
    {
        Write-Output "In Process block"
        Write-Output "Number value: "         $Number
    }
    END
    {
        Write-Output "In End block"
    }
} #END Function Test-ScriptBlock
 
 
Test-ScriptBlock -Number $Number
``` 
 
### Passing back data from PowerShell

You can use these PowerShell commands to pass back output to VisualCron:
 
**VisualCron standard output**

```powershell
write-output "my output"
``` 

**VisualCron standard error**

```powershell
write-error "my error"
```
 
**Raising/Throwing errors**

Use the PowerShell `throw` command to raise errors; a `throw` fails the Task with exit code 77777, even when *Contains error output* is cleared. By default the Task also fails if anything is written to error output; to change this, clear *Contains error output* on the **_On error_** tab. With *Extended Task debug logging* selected on the Task's **_Main settings_** tab, diagnostic lines are added to the output. The PowerShell `exit` statement ends the script, but its value is not passed to VisualCron: the Task's exit code is 0, or 77777 when the script fails. (`[System.Environment]::Exit(<n>)`, used in the troubleshooting entry below, ends the host process with that code.)
 
### Troubleshooting

**Scripts or modules blocked by execution policy**

The script itself is run as text, so the PowerShell execution policy does not apply to it; it applies to modules and script files the script loads. If those are blocked, set the policy for the account that runs the Task (the Credential's user, or the account the VisualCron service runs under), or on the Server, for example `Set-ExecutionPolicy RemoteSigned -Scope LocalMachine` as an administrator. 32-bit PowerShell (*Execute in x86 mode*) has its own LocalMachine policy. With *Remote* scope, set the policy on the remote computer.
 
**System.TypeLoadException, or Could not load file or assembly System.Management.Automation 3.0**

The Task needs Windows PowerShell 3.0 or later on the VisualCron Server. Upgrade PowerShell if an older version is installed.
 
**AuthorizationManager check failed**

Please add/insert the share you are trying to access in the script to "trusted sites".
 
**No output using Write-Host**

Write-Host cannot be used in the VisualCron environment, which is different from PowerShell.exe. Use Write-Output or Write-Error instead. Write-Warning output is captured only with *Extended Task debug logging* selected.
 
**How can I use PowerShell 7?**

The PowerShell Task hosts Windows PowerShell (5.1 and earlier) on .NET Framework 4.8, so PowerShell 7 cannot be used in it. A workaround is to use the Execute Task with the PowerShell 7 exe (pwsh.exe) full path in command field and the full path to PowerShell script in argument field.
 
**CmdletBinding - no processing of PROCESS block**

Wrap the script into a function (see example 1 in [Passing parameters](#passing-parameters)).
 
**PowerShell Task hangs**

If you are using dbatools in the command:
 
These links tell about the problem:
 
[https://dba.stackexchange.com/questions/184327/sql-agent-powershell-task-never-finishes](https://dba.stackexchange.com/questions/184327/sql-agent-powershell-task-never-finishes)
[http://glenn-pepper.co.uk/2018/11/22/2-issues-with-powershell-steps-in-sql-agent/](http://glenn-pepper.co.uk/2018/11/22/2-issues-with-powershell-steps-in-sql-agent/)
 
You can try one of the solutions;
 
* Use ```[System.Environment]::Exit(1)``` as last line (you can choose in VC to not raise error on this specific error)
* Use SQLCMD like [https://docs.microsoft.com/en-us/powershell/module/sqlserver/invoke-sqlcmd?view=sqlserver-ps](https://docs.microsoft.com/en-us/powershell/module/sqlserver/invoke-sqlcmd?view=sqlserver-ps)
* Use another method
