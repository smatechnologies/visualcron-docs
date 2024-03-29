---
sidebar_label: 'Remote, Silent, and Customized Installation'
hide_title: 'true'
---

## Remote, Silent, and Customized Installation

Perhaps you have the need for an automated installation of VisualCron on different servers. Since the VisualCron installation is based on MSI you can use already existing Windows tools to perform the installation silently and remotely. You are also able to control where you want to install (installation folder) and if you want to install both the Client and the Server package or just the Client.
 
In the download page there is a link for "silent" installation. This means an installation with no user interaction and something you can run across the network if you have the right permissions.
 
**Custom installation**

1. Download the "Custom installation package" from the [download page](https://www.visualcron.com/download.aspx).
2. Unzip the content to an empty folder
3. Open the command window (cmd.exe)
4. In the command window, go to the folder where the installation is unzipped
 
**To install the Client & Server package, write:**

`msiexec /i VisualCron.msi /q INSTALLMODE="1"`
 
**To install the Client only, write:**

`msiexec /i VisualCron.msi /q INSTALLMODE="2"`
 
**To use other than the default installation folder, write:**

`msiexec /i VisualCron.msi /q INSTALLMODE="1" TARGETDIR="C:\Program Files\your folder\"`
 
**Remote installation**

It is possible to install VisualCron remotely - on a domain or private network.  

1. To do this you need to use a tool called "PsExec" which is downloadable from [Microsoft PsExec](https://learn.microsoft.com/en-us/sysinternals/downloads/psexec). Once downloaded, unzip the content of the PSTools.zip file into the `"C:\WINDOWS\system 32\"` folder.
2. Download the "Custom installation package" from the [download page](https://www.visualcron.com/download.aspx).
3. Unzip the package on a shared drive on your network.
4. Open the command window (cmd.exe)
5. Combine the row below with the command string above in the Custom installation section like this:

`psexec \\remoteservername -u adminusername -p adminpassword msiexec /i \\remoteservername\locationofyourmsi\VisualCron.msi`
 
 
In the zip file of the silent installation you have two bat files:
`install_clientSILENT.bat` - **installs the Client only**

```bat

REM
REM path_to_remote_install_folder\psexec \\remote_server_name -u username -p password path_to_remote_install_folder\install_serverANDclientSILENT.bat path_to_local_install_folder
REM
 
REM Set working folder from parameter "path_to_local_install_folder"
cd %1
 
REM Stop running processes
taskkill /F /IM VCtray.exe
taskkill /F /IM VisualCronClient.exe
 
REM Stop the VisualCron service
net stop VisualCron4
 
REM Uninstall the old version
msiexec /x VisualCron.msi /q
 
REM Install new version
msiexec /i VisualCron.msi /q INSTALLMODE="2" REINSTALLMODE=dmus

``` 
 
`install_serverANDclientSILENT.bat` - **installs both Client and Server**
 
```bat

REM
REM path_to_remote_install_folder\psexec \\remote_server_name -u username -p password path_to_remote_install_folder\install_serverANDclientSILENT.bat path_to_local_install_folder
REM
 
REM Set working folder from parameter "path_to_local_install_folder"
cd %1
 
REM Stop running processes
taskkill /F /IM VCtray.exe
taskkill /F /IM VisualCronClient.exe
 
REM Stop the VisualCron service
net stop VisualCron4
 
REM Uninstall the old version
msiexec /x VisualCron.msi /q
 
REM Install new version
msiexec /i VisualCron.msi /q INSTALLMODE="1" REINSTALLMODE=dmus

```