---
sidebar_label: 'Task System - Environment - List Variables'
hide_title: 'true'
---

## Task System - Environment - List Variables

System - Environment - List variables lists all variables  for a process, user or local machine.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/List%20Variables.png)

**Credentials**

To control a remote computer you may need to use a Credential. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the *Settings* icon to open *Manage credentials* in order to add or edit Credentials.

**Environment variable settings:**

**Variable scope**

Select Process, User or Machine variable scope. These variable scopes refers, more or less, to Windows 10 Process, User and System variables. The Windows process variables consist of Windows User and System variables.
 
The Windows 10 **User environment variables** are stored in the registry key below:

`HKEY_CURRENT_USER\Environment`
 
The Windows 10 **System environment variables** are stored in the registry key below:

`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment`
