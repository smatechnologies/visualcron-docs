---
sidebar_label: 'Servers - Sync Server Objects'
hide_title: 'true'
---

## Servers - Sync Server Objects

The ***Sync Server objects*** window, opened from ***Servers*** -> ***Sync Server objects***, copies Jobs and global objects from another VisualCron Server to this one, for example from a production Server to a test Server.

Each sync setting connects to one remote Server through a [VisualCron Connection](../server/connection-visualcron) and chooses, per object type, which changes on the remote Server are applied on this Server:

* New objects (added on the remote Server)
* Updated objects
* Deleted objects

A sync setting can run automatically, applying each change as it happens on the remote Server, or be run by hand with _Sync now_.

This feature was introduced in version 9.2.0 of VisualCron.

:::warning Sync overwrites and deletes objects on this Server

- An updated object replaces the object with the same identity on this Server, so local changes to a synced object are lost.
- _Sync deleted_ is checked by default. While a sync setting is active, an object deleted on the remote Server is also deleted on this Server.
- With _Sync the following `objecttype` settings_, _Sync now_ deletes an object on this Server when its _Delete_ column is checked and the object no longer exists on the remote Server.

Checking _Use_ on a row, or _Select All Use_, also checks _Delete_. Uncheck _Sync deleted_, or clear the _Delete_ column, where objects on this Server must be kept.

After _Sync now_ deletes an object, the rest of that run can be skipped. Check the _Server Sync log_ and run _Sync now_ again until nothing is left to delete.

:::

### Main window

The grid lists every sync setting. Usually one row is one remote Server to sync from, but more than one sync setting can use the same Server.

![Sync Server objects window with the toolbar and the list of sync settings](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/Sync%20Server%20Objects/Sync%20Server%20Objects.png)

- _Add_: opens the window for a new sync setting
- _Edit_: opens the selected sync setting
- _Delete_: deletes the selected sync setting after a confirmation. The objects already synced are not removed
- _Clone_: opens a copy of the selected sync setting as a new sync setting
- _Change State_: turns automatic sync with the remote Server on or off
- _Sync now_: runs a manual sync of the selected sync setting. It also runs for a sync setting that is not _Active_

Right-click a row and select _Server Sync log_ to see what the sync setting has done.

### Add/Edit Sync setting window

![Sync setting window with the Active check box, the Connection list and the Jobs tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/Sync%20Server%20Objects/Sync%20Server%20Jobs.png)

- _Active_: turns all syncing from the remote Server on or off for this sync setting
- _Connection_: the [VisualCron Connection](../server/connection-visualcron) to the remote Server. Click _Connect_ to load the objects of the remote Server

Each object type has its own tab: ***Users***, ***User groups***, ***Jobs***, ***Connections***, ***Credentials***, ***Notifications***, ***Certificates***, ***Conditions***, ***PGP Key Rings***, ***Time Exceptions***, ***Task repository***, ***Variables***, ***Network drives*** and ***MFT***. On each tab, select one of the following:

- _Sync None_: objects of this type are not synced
- _Sync all `objecttype` settings_: the default. All objects of this type are synced. Use _Sync new_, _Sync updated_ and _Sync deleted_, all checked by default, to choose which changes are applied
- _Sync the following `objecttype` settings_: only the objects checked in the grid are synced. For each object, the _Use_, _New_, _Update_ and _Delete_ columns choose which changes are applied. When this option is selected, every row starts cleared. Right-click the grid to select or clear a whole column at once
