---
sidebar_label: 'Upgrading From VisualCron 4.x to 5.x'
hide_title: 'true'
---

## Upgrading From VisualCron 4.x to 5.x

In version VisualCron version 5 we have optimized a lot of the code structure in earlier version of VisualCron. However, this it was not possible to be completely compatible with version 4, which means that you will lose some information when upgrading from version 4 to 5. Also, other changes exist that may or not affect you. Below is a list of changes for version 5 and how they might affect you and your Jobs.
 
**Install and location**

VisualCron 5 will now install by default in `%PROGRAMFILES%\VisualCron\`. Previously, VisualCron was installed in `%PROGRAMFILES%\VisualCron 4\`. The installation of VisualCron 5 will not uninstall version 4. Both versions can co-exist.
 
**Service name**

The service name for VisualCron 5 is *VisualCron*. For version 4, the service name is *VisualCron 4*. If you previously used a specific user for version 4 you need to set that user to run the VisualCron service for version 5. That information is not transferred automatically.
 
**API**

If you are using the API you have to upgrade to the latest version of the API for version 5 in order to connect to version 5. Old version can still connect to VisualCron 4.
 
**Desktop short cut**

The desktop shortcut is named VisualCron 5.
 
**Task changes**

**SQL Task**

The connection string is no longer stored in the Task. We wanted to make the actual Connection global and we are now storing the connection in [Connections](../client-user-interface/server/global-connections). This means that your old connection string will be missing and that you have to create a Connection and select it in the Task.
 
**FTP/S Task**

We have removed the direct link to the certificate file and are now storing Client certificates in [Certificates](../client-user-interface/server/global-certificates). You need to import any existing certificate in [Certificates](../client-user-interface/server/global-certificates) and the select the actual Certificate in the Task.
 
**SFTP Task**

We have removed the direct link to the certificate file and are now storing Client certificates in [Certificates](../client-user-interface/server/global-certificates). You need to import any existing certificate in [Certificates](../client-user-interface/server/global-certificates) and the select the actual Certificate in the Task.
 
**Notification changes**

**SQL Notification**

The connection string is no longer stored in the Notification. We wanted to make the actual Connection global and we are now storing the connection in [Connections](../client-user-interface/server/global-connections). This means that your old connection string will be missing and that you have to create a Connection and select it in the Notification.
 
**Installation notes**

If VisualCron 4 is already installed and VisualCron 5 is installed, the following notes are applicable:

* The complete VisualCron 4 installation is kept
* A start guide performs VisualCron 5 installation which copies the log, settings and backup sub folders from the `%PROGRAMFILES%\VisualCron 4\` folder to the `%PROGRAMFILES%\VisualCron\` folder. Normally this is done in interactive mode meaning that dialogs are showing the result, but it is also possible to use quiet install (Custom) which performs the same action without dialogs
* A start guide shows a few windows with some basic client/server settings. This guide may be issued later using the client main menu **File-> Start Guide** option
* The VisualCron 4 Tray client is removed
* The *VisualCron 4* service is shut down and disabled. If VisualCron 4 shall be run, the *VisualCron (5)* service has to be stopped manually and the *VisualCron 4* service has to be started manually
* Some settings cannot be copied to VisualCron 5 automatically, see the above notes. These have to be updated manually using the VisualCron 5 client
* When VisualCron 5 is running with all settings verified, you manually uninstall VisualCron 4 by using the *Control Panel -> Add/Remove programs* option
* When uninstalling VisualCron 4, the Tray Client may be stopped/killed. If that happens you just start it again from the *Start menu -> Program -> VisualCron 5 -> VisualCron Tray Client*