---
sidebar_label: 'Objects - Audit Log'
hide_title: 'true'
---

## Objects - Audit Log

The ***Audit log*** window lists the changes made to VisualCron objects: who changed what, and when.

To open it, click ***Tools*** -> ***Objects*** -> ***Audit log***. It also opens from other places with a filter already set. For example, right-click a Job and click ***Audit log*** to see only the changes to that Job, or open it from the Credentials window to see the changes to all Credentials.

![Audit log window with filters at the top and a list of change events](../../../static/img/Client%20User%20Interface/Main%20Menu/Tools/Objects/Audit%20Log.png)

The grid shows:

- _Event date_: when the change was made
- _User_: who made the change
- _Type_: the type of object that was changed
- _Job_: the Job that the object belongs to, if any
- _Object_: the name of the object
- _Event type_: the kind of change, such as add, update, delete, run, activate or deactivate
- _Diff_: whether the change has differences from the previous version
- _Summary_: a short description of the change

### Filters

Refine the list with _User_, _Object type_, _Job_ (with a _Filter.._ field), _Event type_, _Objects_ and _Timespan_, then click ***Search***. ***Export..*** exports the listed events.

When the window opens, _Timespan_ is set to the period that holds events for the current filter. The list is filled at once when there are at most 100 events; otherwise click ***Search***.

How long audit data is kept is set in [Settings - Log Settings](../server/settings-log-settings).

### Versions and revert

Double-click a row to open the ***Versions..*** window, see [Versions](audit-log-versions). You can also right-click a row and click ***Versions and details*** or ***Revert to selected***.
