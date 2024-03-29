---
sidebar_label: 'VisualCron error: Missing System File perfc009.dat'
hide_title: 'true'
---

## VisualCron error: Missing System File perfc009.dat

The error behind this message is: System.InvalidOperationException: Process performance counter is disabled, so the requested operation cannot be performed.
 
Probably a third party application has deleted an important system file called perfc009.dat. Just download it from [here](http://www.visualcron.com/files/perfc009.zip) and extract with WinZip it to your system32 directory (normally "C:\WINDOWS\system32\"), then start VisualCron again.
 
Also, check that you have read access to the following key: _HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT \CurrentVersion\Perflib\009_