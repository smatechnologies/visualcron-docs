---
sidebar_label: 'Upgrading From VisualCron 8.x to 9.x'
hide_title: 'true'
---

## Upgrading From VisualCron 8.x to 9.x

There some breaking changes in VisualCron related to how we store encrypted values. We have increased encryption from 3DES to AES256. This means old version cannot read AES256 values but new version can convert from old.
 
This means that you cannot do this:
 
* Export from version 9.x to 8.x
* Connect from version 9.x Client to 8.x Server
* Connection from version 8.x Client to 9.x Server.
 
 
You can:

* Import from version 8.x to 9.x (this will happen automatically on upgrade.
 
 
From version 9.0.0 you need .NET 4.8. .NET 4.8 is not supported in XP, Windows Vista, 2003, 2008 (only 2008 R2).