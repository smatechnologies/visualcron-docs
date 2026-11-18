---
sidebar_label: 'Powershell'
hide_title: 'true'
---

## PowerShell

This page shows how to use the VisualCron .NET API from PowerShell: load the API DLLs, connect to a Server and read Variable values. It is for administrators and developers who script VisualCron. To run a PowerShell script as part of a Job instead, use the [PowerShell Task](../client-user-interface/server/job-tasks-task-process-powershell). For an overview of the API, see [VisualCron API](visualcron-api).

The API DLLs are built for .NET Framework 4.8. The installation folder also holds sample scripts in "API\samples\PowerShell". Use the snippets below instead: in the installed samples, the catch block in "VisualCron_API.ps1" does not run in PowerShell, and "VCAPI_Test.ps1" calls a method that the API does not have.

### Connect and read Variables (save as VisualCron_API.ps1)

Save this snippet as "VisualCron_API.ps1". It loads the DLLs, defines the connection settings and adds three functions: `VCAPI-ConnectServer`, `VCAPI-Get-User-Variable` and `VCAPI-Get-Variable`.

```powershell

# Load the VisualCron API DLLs
$VC                = [Reflection.Assembly]::LoadFrom("C:\Program Files (x86)\VisualCron\VisualCron.dll");
$VCAPI        = [Reflection.Assembly]::LoadFrom("C:\Program Files (x86)\VisualCron\VisualCronAPI.dll");
 
# Define Client & Server Objects
# Globals to allow sharing of connections
$Global:Client        = New-Object -TypeName VisualCronAPI.Client
$Global:Server        = New-Object -TypeName VisualCronAPI.Server
 
# Read Only VisualCron User for API Access
# VisualCron UserName and Password from your Site
$Conn_UserName                        =        'username'
$Conn_PassWord                        =        'password'
 
# Standard Settings
$Conn_Port                                =        16444
$Conn_ConnectionType        =        'Remote'
 
# Function to Connect to a VisualCron Server using the API
function VCAPI-ConnectServer ([string]$Conn_Address) {
 
# Define Connection Object
$Conn = New-Object -TypeName VisualCronAPI.Connection
 
# Set Connection Values
$Conn.Address                        =        $Conn_Address
$Conn.UserName                =        $Conn_UserName
$Conn.PassWord                        =        $Conn_PassWord
$Conn.Port                                =        $Conn_Port
$Conn.ConnectionType        =        $Conn_ConnectionType
 
# Try to Connect to the VisualCron Server
try
 {
         $Global:Server = $Client.Connect($conn, $true);
 
 }
catch [VisualCronAPI.Client+ClientLoginFailedException]
 {
  Write-Error ("Logon to VisualCron failed: " + $_.Exception.Message)
  throw
 }
 
}
 
# Function to retrieve a User Variable Value using the API
# wrapper for generic get variable API call below
function VCAPI-Get-User-Variable ([string]$Variable_Name) {
 
$Variable_Value = VCAPI-Get-Variable("USERVAR(" + $Variable_Name + ")")
 
Return $Variable_Value
 
}
 
# wrapper for the get-variable API call
# Returns the Variable value
function VCAPI-Get-Variable ([string]$Variable_Name) {
 
$Variable_Name        = "{" + $Variable_Name + "}"
 
$Variable_Value = $Global:Server.Variables.GetGenericVariable($Variable_Name)
 
Return $Variable_Value
}

``` 
 
### Call the functions from a script

Save this script in the same folder as "VisualCron_API.ps1". It loads the functions, shows two calls that run on the computer running the script, connects to a Server, reads Variables and disconnects.

```powershell

# Load the functions from VisualCron_API.ps1 in the same folder as this script
. (Join-Path $PSScriptRoot 'VisualCron_API.ps1')

# API Information - Example - Direct API Call (on the computer that runs the script)
$OSVersion = [VisualCronAPI.ComputerInfoAPI]::GetOSFriendlyName()
Write-Host '$OSVersion : ' $OSVersion

# API Information - Example - Direct API Call (on the computer that runs the script)
$LocalAdmins = [VisualCronAPI.ComputerInfoAPI]::GetLocalAdministrators()
Write-Host '$LocalAdmins : ' $LocalAdmins

# Set Client Values - Example using $Client Object
$Client.LogToFile = $False

################################################################################
# Server Connection and API Calls
#
################################################################################

# Connect using Server Name (Fully Qualified)
#VCAPI-ConnectServer('washington.somewhere.com.au')
# or
# IP Address
VCAPI-ConnectServer("123.145.167.89")

# Various Variable Calls - Replace First 2 With UserVariable Names from Your Site
$VCUserVariable = VCAPI-Get-User-Variable("SERVER01")
Write-Host '$VCUserVariable : ' $VCUserVariable

$VCServerName = VCAPI-Get-Variable("USERVAR(SERVER02)")
Write-Host '$VCServerName : ' $VCServerName

$VCServerIP = VCAPI-Get-Variable("SERVER(IP)")
Write-Host '$VCServerIP : ' $VCServerIP

$VCServerPort = VCAPI-Get-Variable("SERVER(Port)")
Write-Host '$VCServerPort : ' $VCServerPort

# Disconnect from the Server
[void]$Global:Server.Disconnect()

```

### Community scripts

A collection of PowerShell scripts for VisualCron is published on GitHub by its author: [PowerShell scripts for VisualCron](https://gist.github.com/atifaziz/9400489). It is not part of VisualCron.