---
sidebar_label: 'Servers - Sync Server Objects'
hide_title: 'true'
---

## Servers - Sync Server Objects

Server Sync provides the ability to sync Jobs and global objects between two or ore more VisualCron Servers. It is idea for Master/Slave or Productio/Test relationships between Servers.
 
 
One Server can subscribe to the following events for all objects on another Server:
 
* Added (New)
* Updated
* Deleted
 
You can Sync objects manually or setup a Server to sync automatically.
 
 
This feature was introduced in version 9.2.0 of VisualCron.
 
**Main window**
 
The main window contains a list of all automated (real time) sync settings. Normally, one row represents a remote Server you want to sync from but it is possible to setup multiple sync settings against one Server.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/Sync%20Server%20Objects/Sync%20Server%20Objects.png)

**Add**

Opens the window for adding new Sync setting against a Server.
 
**Edit**

Opens the window to edit an existing Sync setting.
 
**Delete**

Deletes the selected Sync setting.
 
**Clone**

Opens the window to edit an existing Sync setting as a new Sync setting based on an existing Sync setting.
 
**Change state**

Turns on/off automatic Sync against a Server.
 
**Sync now**

Run a manual sync.
 
**Sync settings**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/Sync%20Server%20Objects/Sync%20Server%20Jobs.png)

**Active**

This turns on/off all syncing from remote Server.
 
**Connection**

This is the remote [VisualCron Connection](../server/connection-visualcron) being used.
 
**Objects types to sync**

Each object type, Jobs, Settings or other Global objects can be, in detail be synced. This is controlled in respective tab.
 
**Sync all `<objecttype>` settings**

This syncs all objects of that type. You can control the types of events to subscribe to, i.e. if you want to sync new, updated or deleted objects of that type.
 
**Sync the following `<objecttype>` settings**

This syncs selected components of that type. You can control in detail if you want to sync all events (new, updated or deleted) or just some events - down to individual object level. You select this in the grid of objects. Pressing Use selects all for that individual object.