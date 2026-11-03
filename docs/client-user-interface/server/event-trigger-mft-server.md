---
sidebar_label: 'Event Trigger - MFT Server'
hide_title: 'true'
---

## Event Trigger - MFT Server

The MFT Server Trigger fires on events of the MFT servers in VisualCron, for example when a file is uploaded or a user logs in. To create and configure an MFT server, see [MFT Server Settings](../servers/servers-mft).
 
The settings are on the ***MFT Server*** tab, ***MFT event type*** sub tab.

![MFT event type sub tab of the Add/Edit event window with the MFT Servers, Event types and MFT Users groups, each with an All checkbox and a list](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20MFT.png)

Each group has an *All* checkbox and a list in which you can check several entries. Check *All* to match every entry (the list is then unavailable), or clear *All* and check the entries to match. The Trigger fires when an event matches all three groups.

**MFT Servers**

Check *All* to react to events of every MFT server, or check one or more servers. Each entry shows the server name and its protocol: "FTP", "SFTP", "SFTPAdvanced" or "HTTP". You must check *All* or at least one server.
 
**Event types**

Check *All* to react to every event type, or check one or more event types. You must check *All* or at least one event type. The list contains:

* Folders: *Directory listed*, *Directory created*, *Directory renamed*, *Directory moved*, *Directory deleted*
* Files: *File created*, *File renamed*, *File moved*, *File deleted*
* Transfers: *File upload start*, *File uploaded*, *File uploaded (failed)*, *File downloaded*
* Logins and sessions: *Login succeeded*, *Login failed*, *Session connected*, *Session connected (failed)*, *Session disconnected*
* Users: *User created*, *User updated*, *User deleted*, *User enabled*, *User disabled*
* Server: *Server started*, *Server stopped*, *Server active*, *Server inactive*

:::note

The list also offers *Server error*, *Directory copied* and *File copied*. The MFT server does not send these events to Triggers, so a Trigger that checks only these never fires.

:::
 
**MFT Users**

Check *All* to match events of any MFT user, or check one or more users. A user linked to a VisualCron user is listed by that user's full name; other users by their login.

:::warning

*All* is cleared for a new Trigger, and the Client lets you save the Trigger with no user checked. Such a Trigger never fires. Check *All* under *MFT Users*, or check the users. An event that has no MFT user matches only when *All* is checked.

:::

### Result Variables

When the Trigger fires, it sets result Variables, listed in the *Variables* window under the Job's Trigger, *Result*. See [Variables](global-variables).

In a run that this Trigger started, `{TRIGGER(Active|LastTrigger|MFT.Result.Message)}` returns a sentence that describes the event, for example `File '<full path>' was uploaded`. The window also lists Variables per event type, for example `{TRIGGER(Active|LastTrigger|MFT.Result.FileUpload.FileFullPath)}` for the full path of an uploaded file.

A Variable of one event type does not return a value when the Trigger fired for another event type. It returns text that ends in `is Null`, and a date Variable returns text that starts with `An error occured converting date format`.
