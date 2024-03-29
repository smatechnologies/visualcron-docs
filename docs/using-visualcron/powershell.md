---
sidebar_label: 'Powershell'
hide_title: 'true'
---

## Powershell

Some of our users have started to use PowerShell to interact with VisualCron. Below are some basic code snippets:
 
### Snippet #1

```powershell

# Load the VisualCron API Dlls
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
$Conn_Address                        =        'localhost'
 
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
catch [$ClientLoginFailedException ex]
 {
  MessageBox.Show(ex.Message);
 
 }
 
}
 
# Function to retrieve a User Variable Value using the API
# wrapper for generic get variable API call below
function VCAPI-Get-User-Variable ([string]$Variable_Name) {
 
$Variable_Value = VCAPI-Get-Variable("USERVAR(" + $Variable_Name + ")")
 
Return $Variable_Value
 
}
 
# wrapper for the get-variable API call
# Returns Varian;e Value
function VCAPI-Get-Variable ([string]$Variable_Name) {
 
$Variable_Name        = "{" + $Variable_Name + "}"
 
$Variable_Value = $Global:Server.Variables.GetGenericVariable($Variable_Name)
 
Return $Variable_Value
}

``` 
 
### Snippet #2

```powershell

# Determine Script Path
$Path = Split-Path $MyInvocation.MyCommand.Path
 
# Determine Script Drive
$Drive = (Get-Item $Path).Root.Name
 
Remove-Variable -Force HOME
Set-Variable HOME $Path
 
# include the VisualCron API
. "$HOME\VisualCron_API.ps1"
 
# API Information - Example - Direct API Call
$OSVersion = [VisualCronAPI.ComputerInfoAPI]::GetOSVersion()
Write-Host '$OSVersion : ' $OSVersion
 
# API Information - Example - Direct API Call
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
 
```

### Snippet #3

[https://gist.github.com/atifaziz/9400489](https://gist.github.com/atifaziz/9400489)