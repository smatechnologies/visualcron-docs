---
sidebar_label: 'Task VMWare - Start VM'
hide_title: 'true'
---

## Task VMWare - Start VM

The VMWare - Start VM Task starts (power on) a virtual machine.
 
**Start VM > Connection** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Start%20VMWare.png)

**Remote VMWare server**

Press this radio button if you want to connect to a remote VMWare server like vSphere.
 
**Connection**

When connecting to a VMWare server you need to setup a [VMWare Connection](../../connection-vmware). Click the *Settings* icon to open the Manage Connections dialog.
 
**Server VMX path**

Path to the VMX file on the server. Click on the refresh button to reload the list with server VMX paths. Click the *Refresh* icon to populate the drop-down Server VMX path list.
 
**Local VMWare workstation**

Press this radio button if you want to connect to a local VMWare workstation.
 
**Local VMX path**

Select the local file VMX path to the local VMWare server. Click the *Folder* icon to display the folder of the server.
 
**Guest OS Credentials**

To control a remote computer you may need to use a Credential. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the *Settings* icon to open *Manage credentials* in order to add or edit Credentials.
 
**Timeout in seconds**

The number of seconds this Task will use to perform the Task. If you have a value in the Timeout tab of the Task it will override this value.
 
**Start VM > VM Task settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Start%20VMWare%20Settings.png)

**Launch GUI**

Displays the interface of the virtual machine in the VMWare workstation application.