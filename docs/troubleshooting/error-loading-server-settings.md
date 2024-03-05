---
sidebar_label: 'Error Loading Server Settings'
hide_title: 'true'
---

## Error Loading Server Settings

If you get the following in the log file:
 
_Error loading settings: System.IO.DirectoryNotFoundException: Could not find part of the path 'xxx\settings_server.xml'._
 
To resolve this you need to edit the registry on the Server machine.
 
1. Stop the VisualCron service
2. Open RegEdit
3. Go to HKEY_LOCAL_MACHINE\SOFTWARE\V-C
4. Edit key "ServerSettingsFolder" to a working folder path - default value is: C:\Program Files (x86)\VisualCron\settings
5. Start the service