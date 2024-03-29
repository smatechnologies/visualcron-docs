---
sidebar_label: 'Upgrading From VisualCron 5.x to 6.x'
hide_title: 'true'
---

## Upgrading From VisualCron 5.x to 6.x

A full list of changes between version 5 and 6 can be found here: [Change Log](../changelog)
 
**API**

If you are using the API you have to upgrade to the latest version of the API for version 6 in order to connect to version 6.
 
**Desktop short cut**

The desktop shortcut is named VisualCron 6.
 
**Installation notes**

Always make a backup before upgrading to another version. You can do a backup in Client **File > Import/Export > Export settings** - export to another location than default.
 
Version 6 version requires .NET 3.5 (previous version required 2.0). .NET redistributable can be downloaded here: [http://www.microsoft.com/download/en/details.aspx?id=21](http://www.microsoft.com/download/en/details.aspx?id=21)
 
VisualCron installer will uninstall the current version and install the new version. Old settings will remain and if needed properties will be upgraded.
 
You may need to verify these Task types because of changes from version 5.x:
 
* PGP Encrypt/Decrypt
* Rename Task
* Archive compress/decompress
 
Especially check source and destination folder properties.
 
Credentials
The way we handle Credentials have changed to provide more control of the actual Credential. Please read more about [Credentials](../client-user-interface/server/global-credentials)